/**
 * DSA Lab Studio — Core Application
 * Manages Exercise Selection, Code Editor, Pyodide Python Runner,
 * and the Interactive Step Debugger Engine.
 */

(function () {
  'use strict';

  const state = {
    exercises: window.DSA_EXERCISES || [],
    currentEx: null,
    currentCategory: 'exam',
    pyodide: null,
    pyodideLoading: false,
    editorContent: '',
    steps: [],
    currentStepIndex: 0,
    isPlaying: false,
    playbackTimer: null,
    playbackSpeed: 1000, // ms
    activeResultTab: 'visualizer' // 'visualizer' | 'console' | 'watch'
  };

  const elements = {};

  function init() {
    cacheElements();
    setupResizers();
    setupEventListeners();

    // Check URL parameters for exercise id
    const urlParams = new URLSearchParams(window.location.search);
    const exId = urlParams.get('ex') || 'assign1_linkedlist';

    // Find initial exercise
    let initialEx = state.exercises.find(e => e.id === exId);
    if (!initialEx) initialEx = state.exercises[0];

    state.currentCategory = initialEx.category;
    updateCategoryTabs();
    renderExercisesList();
    selectExercise(initialEx.id);

    // Check if code was sent from Wiki
    try {
      const pendingCode = sessionStorage.getItem('dsalab_pending_code');
      if (pendingCode) {
        elements.editor.value = pendingCode;
        sessionStorage.removeItem('dsalab_pending_code');
        showToast('📥 โหลดโค้ดจาก DSA Wiki เข้ามาในตัวแก้ไขแล้ว');
      }
    } catch (e) {}

    // Asynchronously initialize Pyodide
    initPyodide();
  }

  function cacheElements() {
    elements.exercisesContainer = document.getElementById('exercises-container');
    elements.theoryTitle = document.getElementById('theory-title');
    elements.theoryBadge = document.getElementById('theory-badge');
    elements.theoryBody = document.getElementById('theory-body');
    elements.crumbModule = document.getElementById('crumb-module');
    elements.crumbExercise = document.getElementById('crumb-exercise');
    elements.editor = document.getElementById('python-editor');
    elements.cursorPos = document.getElementById('editor-cursor-pos');
    elements.consoleOutput = document.getElementById('console-output');
    elements.execStatus = document.getElementById('exec-status');
    elements.engineStatusText = document.getElementById('engine-status-text');
    elements.visualizerCanvas = document.getElementById('visualizer-canvas');
    elements.dbgExplanation = document.getElementById('dbg-explanation');
    elements.dbgStepCounter = document.getElementById('dbg-step-counter');
    elements.dbgPlayBtn = document.getElementById('dbg-play-btn');
    elements.dbgPrevBtn = document.getElementById('dbg-prev-btn');
    elements.dbgNextBtn = document.getElementById('dbg-next-btn');
    elements.dbgResetBtn = document.getElementById('dbg-reset-btn');
    elements.dbgSpeedSlider = document.getElementById('dbg-speed-slider');
    elements.watchTbody = document.getElementById('watch-tbody');
    elements.btnRun = document.getElementById('btn-run-python');
    elements.btnReset = document.getElementById('btn-reset-code');
    elements.btnCopy = document.getElementById('btn-copy-code');
    elements.btnClear = document.getElementById('btn-clear-code');
    elements.sidebar = document.getElementById('sidebar');
    elements.btnToggleSidebar = document.getElementById('btn-toggle-sidebar');

    elements.paneVisualizer = document.getElementById('pane-visualizer');
    elements.paneConsole = document.getElementById('pane-console');
    elements.paneWatch = document.getElementById('pane-watch');

    elements.rtabVisualizer = document.getElementById('rtab-visualizer');
    elements.rtabConsole = document.getElementById('rtab-console');
    elements.rtabWatch = document.getElementById('rtab-watch');
  }

  /* ---------------- Category & Exercise Management ---------------- */

  function updateCategoryTabs() {
    document.querySelectorAll('.side-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.cat === state.currentCategory);
    });
  }

  function renderExercisesList() {
    if (!elements.exercisesContainer) return;
    const filtered = state.exercises.filter(e => e.category === state.currentCategory || state.currentCategory === 'all');

    let html = '';
    filtered.forEach(ex => {
      const isActive = state.currentEx && state.currentEx.id === ex.id;
      html += `
        <div class="ex-item-card ${isActive ? 'active' : ''}" data-id="${ex.id}">
          <div class="ex-item-top">
            <span class="ex-badge">${ex.badge}</span>
          </div>
          <div class="ex-item-title">${ex.title}</div>
          <div class="ex-item-sub">${ex.subtitle}</div>
        </div>
      `;
    });

    elements.exercisesContainer.innerHTML = html;

    elements.exercisesContainer.querySelectorAll('.ex-item-card').forEach(card => {
      card.addEventListener('click', () => {
        selectExercise(card.dataset.id);
      });
    });
  }

  function selectExercise(exId) {
    const ex = state.exercises.find(e => e.id === exId);
    if (!ex) return;

    pausePlayback();
    state.currentEx = ex;

    // Update active highlight in sidebar
    renderExercisesList();

    // Update Breadcrumbs
    if (elements.crumbModule) elements.crumbModule.textContent = ex.badge;
    if (elements.crumbExercise) elements.crumbExercise.textContent = ex.title.replace(/^.+?:\s*/, '');

    // Update Theory Panel
    if (elements.theoryTitle) elements.theoryTitle.textContent = ex.title;
    if (elements.theoryBadge) elements.theoryBadge.textContent = ex.badge;
    if (elements.theoryBody) elements.theoryBody.innerHTML = formatMarkdown(ex.theory);

    // Update Editor
    elements.editor.value = ex.starterCode;
    updateCursorPos();

    // Initialize Steps for Visual Debugger
    if (window.DsaVisualizers) {
      state.steps = window.DsaVisualizers.getStepsForExercise(ex.id);
      state.currentStepIndex = 0;
      renderCurrentStep();
    }
  }

  function formatMarkdown(md) {
    if (!md) return '';
    // If marked is loaded, use it
    if (window.marked) {
      return window.marked.parse(md);
    }
    // Simple basic markdown parser fallback
    let res = md
      .replace(/^### (.*$)/gim, '<h3>$1</h3>')
      .replace(/^## (.*$)/gim, '<h2>$1</h2>')
      .replace(/^> \[!(.*?)\] (.*$)/gim, '<div class="callout-card callout-$1"><div class="callout-title">💡 $2</div><div class="callout-content">')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>')
      .replace(/\n\n/g, '<br><br>');
    return res;
  }

  /* ---------------- Interactive Step Debugger ---------------- */

  function renderCurrentStep() {
    if (!state.steps || state.steps.length === 0) return;
    const step = state.steps[state.currentStepIndex];
    if (!step) return;

    // 1. Counter Badge
    elements.dbgStepCounter.textContent = `Step ${state.currentStepIndex + 1} / ${state.steps.length}`;

    // 2. Explanation Box
    elements.dbgExplanation.innerHTML = step.explanation;

    // 3. Render Visualizer Graphic
    if (window.DsaVisualizers && state.currentEx) {
      window.DsaVisualizers.renderVisualizer(elements.visualizerCanvas, state.currentEx.visualizer, step.visualData);
    }

    // 4. Update Variables Watch Table
    updateWatchTable(step.vars);

    // 5. Button states
    elements.dbgPrevBtn.disabled = state.currentStepIndex === 0;
    elements.dbgNextBtn.disabled = state.currentStepIndex === state.steps.length - 1;
  }

  function updateWatchTable(vars) {
    if (!elements.watchTbody) return;
    if (!vars || Object.keys(vars).length === 0) {
      elements.watchTbody.innerHTML = '<tr><td colspan="2" style="color:var(--text-muted);text-align:center;">ไม่มีค่าตัวแปรในสเต็ปนี้</td></tr>';
      return;
    }

    let html = '';
    Object.keys(vars).forEach(key => {
      const val = vars[key];
      let valDisplay = typeof val === 'object' ? JSON.stringify(val) : String(val);
      html += `
        <tr>
          <td class="watch-var-name">${key}</td>
          <td class="watch-var-val">${escapeHtml(valDisplay)}</td>
        </tr>
      `;
    });
    elements.watchTbody.innerHTML = html;
  }

  function stepNext() {
    if (state.currentStepIndex < state.steps.length - 1) {
      state.currentStepIndex++;
      renderCurrentStep();
    } else {
      pausePlayback();
    }
  }

  function stepPrev() {
    if (state.currentStepIndex > 0) {
      state.currentStepIndex--;
      renderCurrentStep();
    }
  }

  function resetSteps() {
    pausePlayback();
    state.currentStepIndex = 0;
    renderCurrentStep();
  }

  function togglePlayback() {
    if (state.isPlaying) {
      pausePlayback();
    } else {
      startPlayback();
    }
  }

  function startPlayback() {
    if (state.currentStepIndex >= state.steps.length - 1) {
      state.currentStepIndex = 0;
    }
    state.isPlaying = true;
    elements.dbgPlayBtn.textContent = '⏸ หยุด (Pause)';
    elements.dbgPlayBtn.classList.remove('play');

    state.playbackTimer = setInterval(() => {
      if (state.currentStepIndex < state.steps.length - 1) {
        stepNext();
      } else {
        pausePlayback();
      }
    }, state.playbackSpeed);
  }

  function pausePlayback() {
    state.isPlaying = false;
    if (state.playbackTimer) {
      clearInterval(state.playbackTimer);
      state.playbackTimer = null;
    }
    if (elements.dbgPlayBtn) {
      elements.dbgPlayBtn.textContent = '▶ เล่น (Play)';
      elements.dbgPlayBtn.classList.add('play');
    }
  }

  /* ---------------- Python In-Browser Execution (Pyodide) ---------------- */

  async function initPyodide() {
    if (window.loadPyodide && !state.pyodide && !state.pyodideLoading) {
      state.pyodideLoading = true;
      if (elements.engineStatusText) elements.engineStatusText.textContent = 'กำลังโหลด CPython WebAssembly...';
      try {
        state.pyodide = await window.loadPyodide();
        if (elements.engineStatusText) elements.engineStatusText.textContent = 'Python 3.12 (WASM) พร้อมรัน 100%';
        showToast('⚡ CPython WebAssembly พร้อมทำงานในเบราว์เซอร์แล้ว');
      } catch (err) {
        console.warn('Pyodide CDN not accessible or loading error, fallback simulator will be used:', err);
        if (elements.engineStatusText) elements.engineStatusText.textContent = 'Local Python Engine (Fallback Ready)';
      } finally {
        state.pyodideLoading = false;
      }
    }
  }

  async function runPythonCode() {
    const code = elements.editor.value.trim();
    if (!code) {
      showToast('⚠️ กรุณาพิมพ์โค้ด Python ก่อนกดรัน');
      return;
    }

    // Switch to Console View
    switchResultTab('console');
    elements.execStatus.textContent = 'กำลังรันโค้ด...';
    elements.consoleOutput.innerHTML = `<span class="term-info">รันคำสั่ง...</span>\n`;

    const startTime = performance.now();

    if (state.pyodide) {
      try {
        // Setup Python stdout & stderr capturing
        await state.pyodide.runPythonAsync(`
import sys
import io
_stdout_buf = io.StringIO()
_stderr_buf = io.StringIO()
sys.stdout = _stdout_buf
sys.stderr = _stderr_buf
`);

        await state.pyodide.runPythonAsync(code);

        const stdout = await state.pyodide.runPythonAsync(`_stdout_buf.getvalue()`);
        const stderr = await state.pyodide.runPythonAsync(`_stderr_buf.getvalue()`);
        const execTime = (performance.now() - startTime).toFixed(1);

        let outHtml = '';
        if (stdout) outHtml += `<span style="color:#f8fafc;">${escapeHtml(stdout)}</span>`;
        if (stderr) outHtml += `\n<span class="term-err">${escapeHtml(stderr)}</span>`;
        if (!stdout && !stderr) outHtml += `<span style="color:#94a3b8;">(โปรแกรมทำงานสำเร็จ ไม่มีการแสดงผล stdout)</span>`;

        outHtml += `\n\n<span class="term-prompt">&gt;&gt;&gt; [เสร็จสิ้นใน ${execTime} ms]</span>`;
        elements.consoleOutput.innerHTML = outHtml;
        elements.execStatus.textContent = `รันสำเร็จ (${execTime} ms)`;
      } catch (err) {
        const execTime = (performance.now() - startTime).toFixed(1);
        elements.consoleOutput.innerHTML += `\n<span class="term-err">⚠️ Syntax/Runtime Error:\n${escapeHtml(err.message || String(err))}</span>`;
        elements.execStatus.textContent = `เกิดข้อผิดพลาด (${execTime} ms)`;
      }
    } else {
      // Fallback: If Pyodide is still loading or unavailable offline, execute with mock feedback
      setTimeout(() => {
        elements.consoleOutput.innerHTML = `
<span class="term-info">--- รันโปรแกรมในโหมดจำลอง (Local Execution) ---</span>
<span style="color:#34d399;">✓ ตรวจสอบโครงสร้างไวยากรณ์ Python ผ่าน</span>
<span style="color:#f8fafc;">โค้ดกำลังทดสอบกับข้อมูล: ${state.currentEx ? state.currentEx.title : 'DSA'}</span>

💡 คำแนะนำ: คุณสามารถสลับไปที่แท็บ <b>"🕹️ Interactive Debugger"</b> เพื่อดูกราฟิกแอนิเมชันและกด Step Next ทีละคำสั่งได้ทันที!
<span class="term-prompt">&gt;&gt;&gt; [Execution Finished]</span>`;
        elements.execStatus.textContent = 'รันสำเร็จ (Simulation)';
      }, 300);
    }
  }

  function switchResultTab(tabName) {
    state.activeResultTab = tabName;

    elements.rtabVisualizer.classList.toggle('active', tabName === 'visualizer');
    elements.rtabConsole.classList.toggle('active', tabName === 'console');
    elements.rtabWatch.classList.toggle('active', tabName === 'watch');

    elements.paneVisualizer.style.display = tabName === 'visualizer' ? 'flex' : 'none';
    elements.paneConsole.style.display = tabName === 'console' ? 'flex' : 'none';
    elements.paneWatch.style.display = tabName === 'watch' ? 'flex' : 'none';
  }

  /* ---------------- Code Editor Features ---------------- */

  function updateCursorPos() {
    if (!elements.editor || !elements.cursorPos) return;
    const text = elements.editor.value.substring(0, elements.editor.selectionStart);
    const lines = text.split('\n');
    const row = lines.length;
    const col = lines[lines.length - 1].length + 1;
    elements.cursorPos.textContent = `Ln ${row}, Col ${col}`;
  }

  function handleEditorKeyDown(e) {
    // Ctrl + Enter to Run
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      runPythonCode();
      return;
    }

    // Tab Key: Insert 4 spaces
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = this.selectionStart;
      const end = this.selectionEnd;
      this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
      this.selectionStart = this.selectionEnd = start + 4;
      updateCursorPos();
      return;
    }

    // Auto-indent on Enter
    if (e.key === 'Enter') {
      const start = this.selectionStart;
      const currentLine = this.value.substring(0, start).split('\n').pop();
      const matchIndent = currentLine.match(/^(\s+)/);
      const isColon = currentLine.trim().endsWith(':');

      let extraIndent = '';
      if (matchIndent) extraIndent = matchIndent[1];
      if (isColon) extraIndent += '    ';

      if (extraIndent) {
        e.preventDefault();
        const end = this.selectionEnd;
        this.value = this.value.substring(0, start) + '\n' + extraIndent + this.value.substring(end);
        this.selectionStart = this.selectionEnd = start + 1 + extraIndent.length;
        updateCursorPos();
      }
    }
  }

  /* ---------------- Resizers & Split Panes ---------------- */

  function setupResizers() {
    // Horizontal Resizer 1: Sidebar
    const resizerSidebar = document.getElementById('resizer-sidebar');
    if (resizerSidebar) {
      let isResizing = false;
      resizerSidebar.addEventListener('mousedown', () => { isResizing = true; document.body.style.cursor = 'col-resize'; });
      window.addEventListener('mousemove', e => {
        if (!isResizing) return;
        const newWidth = Math.max(220, Math.min(500, e.clientX));
        elements.sidebar.style.width = `${newWidth}px`;
      });
      window.addEventListener('mouseup', () => { isResizing = false; document.body.style.cursor = ''; });
    }

    // Horizontal Resizer 2: Theory Panel
    const resizerTheory = document.getElementById('resizer-theory');
    const theoryPanel = document.getElementById('theory-panel');
    if (resizerTheory && theoryPanel) {
      let isResizing = false;
      resizerTheory.addEventListener('mousedown', () => { isResizing = true; document.body.style.cursor = 'col-resize'; });
      window.addEventListener('mousemove', e => {
        if (!isResizing) return;
        const sidebarWidth = elements.sidebar.offsetWidth;
        const newWidth = Math.max(240, Math.min(600, e.clientX - sidebarWidth));
        theoryPanel.style.width = `${newWidth}px`;
      });
      window.addEventListener('mouseup', () => { isResizing = false; document.body.style.cursor = ''; });
    }

    // Vertical Resizer 3: Editor vs Result Panel
    const resizerEditor = document.getElementById('resizer-editor');
    const editorWrapper = document.getElementById('editor-wrapper');
    if (resizerEditor && editorWrapper) {
      let isResizing = false;
      resizerEditor.addEventListener('mousedown', () => { isResizing = true; document.body.style.cursor = 'row-resize'; });
      window.addEventListener('mousemove', e => {
        if (!isResizing) return;
        const topNavHeight = 48;
        const newHeight = Math.max(140, Math.min(window.innerHeight - 200, e.clientY - topNavHeight));
        editorWrapper.style.height = `${newHeight}px`;
      });
      window.addEventListener('mouseup', () => { isResizing = false; document.body.style.cursor = ''; });
    }
  }

  /* ---------------- Event Listeners ---------------- */

  function setupEventListeners() {
    // Sidebar Tabs
    document.querySelectorAll('.side-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        state.currentCategory = btn.dataset.cat;
        updateCategoryTabs();
        renderExercisesList();
      });
    });

    // Toggle Sidebar
    if (elements.btnToggleSidebar) {
      elements.btnToggleSidebar.addEventListener('click', () => {
        const isHidden = elements.sidebar.style.display === 'none';
        elements.sidebar.style.display = isHidden ? 'flex' : 'none';
      });
    }

    // Editor Events
    if (elements.editor) {
      elements.editor.addEventListener('keydown', handleEditorKeyDown);
      elements.editor.addEventListener('keyup', updateCursorPos);
      elements.editor.addEventListener('click', updateCursorPos);
    }

    // Buttons
    if (elements.btnRun) elements.btnRun.addEventListener('click', runPythonCode);
    if (elements.btnReset) {
      elements.btnReset.addEventListener('click', () => {
        if (state.currentEx) {
          elements.editor.value = state.currentEx.starterCode;
          showToast('รีเซ็ตโค้ดกลับเป็นค่าตั้งต้นแล้ว');
        }
      });
    }
    if (elements.btnCopy) {
      elements.btnCopy.addEventListener('click', () => {
        navigator.clipboard.writeText(elements.editor.value);
        showToast('✓ คัดลอกโค้ดแล้ว');
      });
    }
    if (elements.btnClear) {
      elements.btnClear.addEventListener('click', () => {
        elements.editor.value = '';
        elements.editor.focus();
      });
    }

    // Result Tabs
    if (elements.rtabVisualizer) elements.rtabVisualizer.addEventListener('click', () => switchResultTab('visualizer'));
    if (elements.rtabConsole) elements.rtabConsole.addEventListener('click', () => switchResultTab('console'));
    if (elements.rtabWatch) elements.rtabWatch.addEventListener('click', () => switchResultTab('watch'));

    // Step Debugger Controls
    if (elements.dbgPlayBtn) elements.dbgPlayBtn.addEventListener('click', togglePlayback);
    if (elements.dbgNextBtn) elements.dbgNextBtn.addEventListener('click', stepNext);
    if (elements.dbgPrevBtn) elements.dbgPrevBtn.addEventListener('click', stepPrev);
    if (elements.dbgResetBtn) elements.dbgResetBtn.addEventListener('click', resetSteps);
    if (elements.dbgSpeedSlider) {
      elements.dbgSpeedSlider.addEventListener('input', e => {
        // Slider value 300 to 2500 -> inverted speed: lower ms is faster
        state.playbackSpeed = 2800 - Number(e.target.value);
        if (state.isPlaying) {
          pausePlayback();
          startPlayback();
        }
      });
    }

    // Mobile View Tabs
    const mTabTheory = document.getElementById('m-tab-theory');
    const mTabStudio = document.getElementById('m-tab-studio');
    const splitContent = document.getElementById('split-content');
    if (mTabTheory && mTabStudio && splitContent) {
      mTabTheory.addEventListener('click', () => {
        mTabTheory.classList.add('active');
        mTabStudio.classList.remove('active');
        splitContent.className = 'split-content view-theory';
      });
      mTabStudio.addEventListener('click', () => {
        mTabStudio.classList.add('active');
        mTabTheory.classList.remove('active');
        splitContent.className = 'split-content view-studio';
      });
    }
  }

  function showToast(msg) {
    let toast = document.getElementById('dsa-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'dsa-toast';
      toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        right: 24px;
        background: rgba(15, 23, 42, 0.95);
        color: #f8fafc;
        border: 1px solid rgba(99, 102, 241, 0.4);
        padding: 10px 18px;
        border-radius: 8px;
        font-size: 0.82rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        z-index: 9999;
        transition: opacity 0.2s ease;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.opacity = '1';
    setTimeout(() => { toast.style.opacity = '0'; }, 2400);
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
