/**
 * DSA Wiki Web Reader — Core Application
 * Handles Markdown rendering, Obsidian Callouts, Mermaid diagrams,
 * Table of Contents with scrollspy, Omni-search, and cross-linking to DSA Lab.
 */

(function () {
  'use strict';

  // Application State
  const state = {
    wikiData: window.WIKI_DATA || null,
    currentDocId: null,
    currentMode: 'curriculum', // 'curriculum' | 'exam'
    completedDocs: new Set(),
    theme: localStorage.getItem('wiki_theme') || 'dark',
    fontSize: parseInt(localStorage.getItem('wiki_font_size') || '16', 10),
    tocHeadings: [],
    searchIndex: [],
    pyodide: null,
    pyodideLoading: false
  };

  const CALLOUT_CONFIGS = {
    summary: { title: 'ภาพรวม (Summary)', icon: '📝', class: 'callout-summary' },
    definition: { title: 'นิยาม (Definition)', icon: '📐', class: 'callout-definition' },
    info: { title: 'เกร็ดความรู้ (Info)', icon: '💡', class: 'callout-info' },
    tip: { title: 'ข้อแนะนำ (Tip)', icon: '✨', class: 'callout-tip' },
    warning: { title: 'ข้อควรระวัง (Warning)', icon: '⚠️', class: 'callout-warning' },
    caution: { title: 'อันตราย (Caution)', icon: '🚨', class: 'callout-caution' },
    important: { title: 'สำคัญมาก (Important)', icon: '❗', class: 'callout-warning' },
    example: { title: 'ตัวอย่าง (Example)', icon: '🔍', class: 'callout-example' },
    note: { title: 'บันทึก (Note)', icon: '📌', class: 'callout-info' },
    question: { title: 'คำถาม (Question)', icon: '❓', class: 'callout-example' }
  };

  const elements = {};

  function initApp() {
    cacheElements();
    applyTheme(state.theme);
    applyFontSize(state.fontSize);
    loadCompletedState();
    initPyodide();

    // Native DSA Lab Architecture Models are used directly (Zero Mermaid dependency)

    buildSearchIndex();
    setupEventListeners();

    // Determine initial document from hash or default to Chapter 1
    const hashDoc = getDocFromHash();
    const initialDoc = hashDoc || (state.wikiData ? state.wikiData.initialDocId : '01.1 - Introduction to Data Structures & Algorithm Analysis');

    // Auto-detect mode based on document
    if (initialDoc && (initialDoc.startsWith('11.') || initialDoc.includes('Glossary') || initialDoc.includes('Index'))) {
      state.currentMode = 'exam';
    } else {
      state.currentMode = 'curriculum';
    }

    updateModeTabs();
    renderSidebar();
    navigateToDoc(initialDoc, getAnchorFromHash());
  }

  function cacheElements() {
    elements.sidebarNav = document.getElementById('sidebar-nav');
    elements.articleTitle = document.getElementById('article-title');
    elements.articleBody = document.getElementById('article-body');
    elements.articleMeta = document.getElementById('article-meta');
    elements.breadcrumbCategory = document.getElementById('breadcrumb-category');
    elements.breadcrumbCurrent = document.getElementById('breadcrumb-current');
    elements.markReadBtn = document.getElementById('mark-read-btn');
    elements.tocList = document.getElementById('toc-list');
    elements.paginationNav = document.getElementById('article-pagination');
    elements.progressBar = document.getElementById('reading-progress-bar');
    elements.themeToggleBtn = document.getElementById('theme-toggle-btn');
    elements.mobileToggleBtn = document.getElementById('mobile-toggle-btn');
    elements.sidebar = document.getElementById('sidebar');
    elements.sidebarBackdrop = document.getElementById('sidebar-backdrop');
    elements.searchModal = document.getElementById('search-modal');
    elements.searchInput = document.getElementById('search-input');
    elements.searchResults = document.getElementById('search-results');
    elements.diagramModal = document.getElementById('diagram-modal');
    elements.diagramCanvas = document.getElementById('diagram-canvas');
    elements.toast = document.getElementById('wiki-toast');

    elements.tabModeCurriculum = document.getElementById('tab-mode-curriculum');
    elements.tabModeExam = document.getElementById('tab-mode-exam');
  }

  function loadCompletedState() {
    try {
      const stored = localStorage.getItem('dsa_wiki_completed_docs');
      if (stored) state.completedDocs = new Set(JSON.parse(stored));
    } catch (e) {}
  }

  function saveCompletedState() {
    try {
      localStorage.setItem('dsa_wiki_completed_docs', JSON.stringify([...state.completedDocs]));
    } catch (e) {}
  }

  function applyTheme(theme) {
    state.theme = theme;
    document.body.className = theme === 'light' ? 'theme-light' : '';
    localStorage.setItem('wiki_theme', theme);
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.innerHTML = theme === 'light' ? '🌙' : '☀️';
    }
  }

  function applyFontSize(size) {
    state.fontSize = Math.min(22, Math.max(14, size));
    document.documentElement.style.setProperty('--reading-font-size', `${state.fontSize}px`);
    localStorage.setItem('wiki_font_size', state.fontSize);
  }

  function updateModeTabs() {
    if (elements.tabModeCurriculum) elements.tabModeCurriculum.classList.toggle('active', state.currentMode === 'curriculum');
    if (elements.tabModeExam) elements.tabModeExam.classList.toggle('active', state.currentMode === 'exam');
  }

  function formatDocNavTitle(docId, originalTitle) {
    if (docId.startsWith('01.1')) return 'บทที่ 1: บทนำ & การวิเคราะห์อัลกอริทึม (Big-O)';
    if (docId.startsWith('02.1')) return 'บทที่ 2: ทบทวนภาษา Python & OOP พื้นฐาน';
    if (docId.startsWith('03.1')) return 'บทที่ 3: Singly, Doubly & Circular Linked Lists';
    if (docId.startsWith('04.1')) return 'บทที่ 4.1: Stack & วงเล็บ & นิพจน์ Postfix';
    if (docId.startsWith('04.2')) return 'บทที่ 4.2: Queue & Circular Array Queue';
    if (docId.startsWith('05.1')) return 'บทที่ 5.1: ต้นไม้ (Trees) & Tree Traversals';
    if (docId.startsWith('05.2')) return 'บทที่ 5.2: Binary Search Trees (BST) & การแทรก';
    if (docId.startsWith('05.3')) return 'บทที่ 5.3: BST Removal (การลบโหนดทุกกรณี)';
    if (docId.startsWith('06.1')) return 'บทที่ 6: Hash Tables & Collision Resolution';
    if (docId.startsWith('07.1')) return 'บทที่ 7: Priority Queue & Binary Heaps';
    if (docId.startsWith('08.1')) return 'บทที่ 8: ขั้นตอนวิธีเรียงลำดับ (Sorting)';
    if (docId.startsWith('09.1')) return 'บทที่ 9: กราฟ (Graph) & BFS / DFS';
    if (docId.startsWith('10.1')) return 'บทที่ 10: วิถีสั้นสุด (Dijkstra Shortest Path)';

    // Exam items
    if (docId.startsWith('11.6')) return '🏁 ข้อสอบปลายภาค Final Exam Prep & Traps (2568)';
    if (docId.startsWith('11.1')) return '🎯 ข้อสอบจริง Midterm Real Mock (2026)';
    if (docId.startsWith('11.2')) return '🎯 ข้อสอบเก็ง Predicted Midterm 2026';
    if (docId.startsWith('11.3')) return '🎯 เจาะข้อสอบ Stack Practice (Exam Style)';
    if (docId.startsWith('11.4')) return '🎯 เจาะข้อสอบ Queue Practice (Exam Style)';
    if (docId.startsWith('11.5')) return '🎯 ตะลุยคลังข้อสอบ 20 ข้อ + ทบทวน';
    if (docId.includes('Glossary')) return '⚡ ตารางสรุป Big-O & คำศัพท์ (Cheat Sheet)';
    if (docId === 'Index') return '📌 สารบัญภาพรวม (Master Index)';

    return originalTitle;
  }

  function renderSidebar() {
    if (!state.wikiData) return;
    const categories = state.currentMode === 'curriculum'
      ? (state.wikiData.curriculumCategories || state.wikiData.categories.filter(c => c.type === 'curriculum'))
      : (state.wikiData.examCategories || state.wikiData.categories.filter(c => c.type === 'exam'));

    let html = '';
    categories.forEach(cat => {
      html += `
        <div class="sidebar-category">
          <div class="category-header">
            <span>${escapeHtml(cat.title)}</span>
          </div>
          <div class="category-docs">
      `;

      cat.docs.forEach(doc => {
        const isCompleted = state.completedDocs.has(doc.id);
        const isActive = doc.id === state.currentDocId;
        const displayNavTitle = formatDocNavTitle(doc.id, doc.title);
        const isExamDoc = state.currentMode === 'exam' || displayNavTitle.includes('🎯');

        html += `
          <a class="doc-nav-item ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''} ${isExamDoc ? 'exam-doc-item' : ''}" 
             data-doc-id="${escapeHtml(doc.id)}" 
             href="#/${encodeURIComponent(doc.id)}">
            <span class="doc-status-box" title="${isCompleted ? 'อ่านจบแล้ว' : 'ยังไม่ได้อ่าน'}">
              ${isCompleted ? '✓' : ''}
            </span>
            <div class="doc-nav-title">
              <div class="doc-nav-title-text">${escapeHtml(displayNavTitle)}</div>
              <div class="doc-nav-meta">⏱️ ${doc.estMinutes} นาที · ${doc.headingsCount} หัวข้อ</div>
            </div>
          </a>
        `;
      });

      html += `
          </div>
        </div>
      `;
    });

    elements.sidebarNav.innerHTML = html;

    elements.sidebarNav.querySelectorAll('.doc-nav-item').forEach(item => {
      item.addEventListener('click', e => {
        e.preventDefault();
        navigateToDoc(item.dataset.docId);
        closeMobileSidebar();
      });
    });
  }

  function updateSidebarActiveState() {
    if (!elements.sidebarNav) return;
    elements.sidebarNav.querySelectorAll('.doc-nav-item').forEach(item => {
      const docId = item.dataset.docId;
      const isCompleted = state.completedDocs.has(docId);
      const isActive = docId === state.currentDocId;
      item.classList.toggle('active', isActive);
      item.classList.toggle('completed', isCompleted);
      const statusBox = item.querySelector('.doc-status-box');
      if (statusBox) statusBox.textContent = isCompleted ? '✓' : '';
    });
  }

  function navigateToDoc(docId, anchor) {
    if (!state.wikiData || !state.wikiData.documents) return;

    let doc = state.wikiData.documents[docId];
    if (!doc) {
      const keys = Object.keys(state.wikiData.documents);
      const match = keys.find(k => k.toLowerCase() === docId.toLowerCase() || k.replace(/\.md$/, '').toLowerCase() === docId.toLowerCase());
      if (match) doc = state.wikiData.documents[match];
    }

    if (!doc) {
      doc = state.wikiData.documents['01.1 - Introduction to Data Structures & Algorithm Analysis'] || Object.values(state.wikiData.documents)[0];
    }
    if (!doc) return;

    // Check if doc belongs to exam category to auto-switch mode tab
    const isExamDoc = doc.id.startsWith('11.') || doc.id.includes('Glossary') || doc.id.includes('Index');
    const targetMode = isExamDoc ? 'exam' : 'curriculum';
    if (state.currentMode !== targetMode) {
      state.currentMode = targetMode;
      updateModeTabs();
      renderSidebar();
    }

    state.currentDocId = doc.id;
    window.location.hash = `#/${encodeURIComponent(doc.id)}${anchor ? '#' + anchor : ''}`;
    window.scrollTo({ top: 0, behavior: 'instant' });

    renderDocument(doc, anchor);
    updateSidebarActiveState();
  }

  function getMarkedParser() {
    if (window.marked) {
      if (typeof window.marked.parse === 'function') return window.marked.parse.bind(window.marked);
      if (typeof window.marked === 'function') return window.marked;
    }
    if (typeof marked !== 'undefined') {
      if (typeof marked.parse === 'function') return marked.parse.bind(marked);
      if (typeof marked === 'function') return marked;
    }
    return null;
  }

  function renderDocument(doc, anchor) {
    const cat = findCategoryForDoc(doc.id);
    if (elements.breadcrumbCategory) {
      elements.breadcrumbCategory.textContent = cat ? cat.title.replace(/^.+?\s/, '') : 'บทเรียน';
    }
    if (elements.breadcrumbCurrent) {
      const formattedTitle = formatDocNavTitle(doc.id, doc.title);
      elements.breadcrumbCurrent.textContent = formattedTitle;
      elements.breadcrumbCurrent.title = formattedTitle;
    }

    elements.articleTitle.textContent = doc.title;

    elements.articleMeta.innerHTML = `
      <span class="meta-badge">⏱️ อ่านประมาณ ${doc.estMinutes} นาที</span>
      <span class="meta-badge">📝 ${(doc.charCount).toLocaleString()} ตัวอักษร</span>
    `;

    const isRead = state.completedDocs.has(doc.id);
    updateMarkReadBtnState(isRead);

    const bodyContent = stripFrontmatter(doc.content);
    const processedMd = preprocessMarkdown(bodyContent);

    const parser = getMarkedParser();
    let htmlContent = '';
    if (parser) {
      try {
        if (window.marked && window.marked.setOptions) {
          window.marked.setOptions({
            gfm: true,
            breaks: true,
            highlight: function (code, lang) {
              if (window.Prism && window.Prism.languages[lang]) {
                return window.Prism.highlight(code, window.Prism.languages[lang], lang);
              }
              return code;
            }
          });
        }
        htmlContent = parser(processedMd);
      } catch (err) {
        console.error('Marked parse error:', err);
        htmlContent = `<div class="error-box">ข้อผิดพลาดในการประมวลผล Markdown: ${escapeHtml(err.message)}</div>`;
      }
    } else {
      console.warn('Marked parser not found, displaying fallback');
      htmlContent = `<pre>${escapeHtml(bodyContent)}</pre>`;
    }

    elements.articleBody.innerHTML = postprocessHtml(htmlContent);

    // Render LaTeX Math Equations with KaTeX
    if (window.renderMathInElement) {
      try {
        window.renderMathInElement(elements.articleBody, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });
      } catch (e) {
        console.warn('KaTeX render error:', e);
      }
    }

    // Mount Interactive Visualizer Studio Widgets
    if (window.DsaWikiStudio) {
      try {
        window.DsaWikiStudio.mountWidgetsForDoc(doc.id, elements.articleBody);
      } catch (e) {
        console.warn('Studio widget mount error:', e);
      }
    }

    setTimeout(() => {
      renderMermaidDiagrams();
    }, 80);

    generateTableOfContents();
    renderPagination(doc.id);

    if (anchor) {
      setTimeout(() => {
        const el = document.getElementById(anchor);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 150);
    }
  }

  function findCategoryForDoc(docId) {
    if (!state.wikiData || !state.wikiData.categories) return null;
    return state.wikiData.categories.find(cat => cat.docs.some(d => d.id === docId));
  }

  function updateMarkReadBtnState(isRead) {
    if (!elements.markReadBtn) return;
    elements.markReadBtn.classList.toggle('is-read', isRead);
    elements.markReadBtn.innerHTML = isRead
      ? `<span>✓</span> อ่านจบแล้ว`
      : `<span>○</span> ทำเครื่องหมายว่าอ่านแล้ว`;
  }

  function stripFrontmatter(text) {
    let clean = text;
    if (clean.startsWith('---')) {
      const endIdx = clean.indexOf('\n---', 3);
      if (endIdx !== -1) clean = clean.slice(endIdx + 4).trim();
    }
    // Strip leading Markdown H1 (# ...) if present, because elements.articleTitle already displays it
    clean = clean.replace(/^\s*#\s+[^\n]*\n?/, '').trim();
    return clean;
  }

  function preprocessMarkdown(md) {
    let result = md.replace(/\r\n/g, '\n');

    // Wiki-links: [[Doc Name]]
    result = result.replace(/\[\[(.*?)(?:\|(.*?))?\]\]/g, (match, target, alias) => {
      const label = alias || target;
      const parts = target.split('#');
      const docTarget = parts[0].trim();
      const anchorTarget = parts[1] ? parts[1].trim() : '';
      return `<a href="#/${encodeURIComponent(docTarget)}${anchorTarget ? '#' + anchorTarget : ''}" class="wiki-link" data-doc="${escapeHtml(docTarget)}" data-anchor="${escapeHtml(anchorTarget)}">📄 ${escapeHtml(label)}</a>`;
    });

    // Obsidian Callouts
    const lines = result.split('\n');
    const out = [];
    let inCallout = false;
    let calloutType = '';
    let calloutTitle = '';
    let calloutLines = [];

    const parser = getMarkedParser();

    function flushCallout() {
      if (!inCallout) return;
      const conf = CALLOUT_CONFIGS[calloutType.toLowerCase()] || {
        title: calloutType.toUpperCase(),
        icon: '📌',
        class: 'callout-info'
      };
      const displayTitle = calloutTitle || conf.title;
      const innerMd = calloutLines.join('\n');
      const innerHtml = parser ? parser(innerMd) : innerMd;

      out.push(`
<div class="callout-card ${conf.class}">
  <div class="callout-header">
    <span class="callout-icon">${conf.icon}</span>
    <span class="callout-title">${escapeHtml(displayTitle)}</span>
  </div>
  <div class="callout-content">${innerHtml}</div>
</div>
      `);

      inCallout = false;
      calloutType = '';
      calloutTitle = '';
      calloutLines = [];
    }

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const matchCallout = line.match(/^>\s*\[!([a-zA-Z]+)\]\s*(.*)$/);

      if (matchCallout) {
        flushCallout();
        inCallout = true;
        calloutType = matchCallout[1].toLowerCase();
        calloutTitle = matchCallout[2].trim();
        continue;
      }

      if (inCallout) {
        if (line.startsWith('>')) {
          calloutLines.push(line.replace(/^>\s?/, ''));
        } else if (line.trim() === '') {
          if (i + 1 < lines.length && lines[i + 1].startsWith('>')) calloutLines.push('');
          else { flushCallout(); out.push(line); }
        } else {
          flushCallout();
          out.push(line);
        }
      } else {
        out.push(line);
      }
    }
    flushCallout();

    return out.join('\n');
  }

  function postprocessHtml(html) {
    let result = html;

    result = result.replace(/<table\b([^>]*)>([\s\S]*?)<\/table>/gi, (match) => {
      return `<div class="table-responsive-wrapper">${match}</div>`;
    });

    const codeBlockRegex = /<pre><code(?:\s+class="([^"]*)")?>([\s\S]*?)<\/code><\/pre>/g;
    result = result.replace(codeBlockRegex, (match, classAttr, codeContent) => {
      const langMatch = (classAttr || '').match(/language-([a-zA-Z0-9_-]+)/);
      const lang = langMatch ? langMatch[1].toLowerCase() : 'text';

      if (lang === 'mermaid') {
        const decodedCode = unescapeHtml(codeContent.trim());
        const nativeVisual = buildNativeDsaVisual(decodedCode, state.currentDoc ? state.currentDoc.id : '');

        return `
          <div class="dsa-model-card dsa-native-card">
            <div class="dsa-model-header">
              <div class="dsa-model-title-group">
                <span class="dsa-term-dots"><i class="dot-red"></i><i class="dot-yellow"></i><i class="dot-green"></i></span>
                <span class="dsa-studio-chip">DSA LAB MODEL</span>
                <span class="dsa-model-title">${escapeHtml(nativeVisual.title)}</span>
              </div>
              <div class="dsa-model-actions">
                <a href="../DsaLab/index.html${nativeVisual.topicHash || ''}" target="_blank" class="dsa-model-btn highlight" title="เปิดทดลองใน DSA Lab Studio">
                  ⚡ เปิดใน DSA Lab
                </a>
                <button class="dsa-model-btn btn-diagram-zoom" onclick="window.WikiApp.openDiagramZoom(this)" title="ขยายดูภาพเต็ม">
                  🔍 ขยายภาพ
                </button>
              </div>
            </div>
            <div class="dsa-model-viewport">
              ${nativeVisual.html}
            </div>
          </div>
        `;
      }

      const isPython = lang === 'python' || lang === 'py';
      const pythonActionBtns = isPython
        ? `<button class="code-btn code-btn-run-live" onclick="window.WikiApp.toggleInlineRunner(this)" title="รันและทดลองแก้โค้ดในหน้านี้ทันทีโดยไม่ต้องเปลี่ยนหน้า">
             ▶ รันโค้ดทันที (Run Live)
           </button>
           <button class="code-btn code-btn-run-sql" onclick="window.WikiApp.runInDsaLab(this)" title="ส่งโค้ดนี้ไปเปิดใน DSA Lab เต็มจอ">
             🔬 เปิดใน Lab ใหญ่
           </button>`
        : '';

      return `
        <div class="code-card-wrapper">
          <div class="code-card-header">
            <span class="code-lang-tag">${escapeHtml(lang)}</span>
            <div class="code-actions-group">
              ${pythonActionBtns}
              <button class="code-btn code-btn-copy" onclick="window.WikiApp.copyCode(this)" title="คัดลอกโค้ด">
                📋 คัดลอก
              </button>
            </div>
          </div>
          <pre><code class="${classAttr || ''}">${codeContent}</code></pre>
        </div>
      `;
    });

    return result;
  }

  function getArchitectureTitle(code) {
    const lower = code.toLowerCase();
    // Strip diagram direction definition e.g. "graph td", "graph lr", "flowchart lr"
    const content = lower.replace(/^(graph|flowchart)\s+(td|lr|tb|bt|rl)/i, '').trim();
    if (content.includes('knowledge map') || (content.includes('data structures') && content.includes('m1') && content.includes('m2'))) {
      return '🗺️ DSA Curriculum Architecture & Master Knowledge Map';
    }
    if (content.includes('shortest') || content.includes('dijkstra')) return '🗺️ Shortest Path & Dijkstra Algorithm Flow Architecture';
    if (content.includes('digraph') || content.includes('traversal') || content.includes('bfs') || content.includes('dfs') || content.includes('adjacency') || content.includes('vertex')) return '🕸️ Graph Structure & Traversal Architecture';
    if (content.includes('big-o') || content.includes('growth') || content.includes('notation') || content.includes('o_notation') || content.includes('constant time') || content.includes('logarithmic')) return '📈 Big-O & Complexity Hierarchy Model';
    if (content.includes('adt') || content.includes('abstract')) return '🏛️ Abstract Data Type (ADT) Logical Architecture';
    if (/\b(oop|class|classes|object)\b/i.test(content) && !content.includes('loop')) return '🐍 Python OOP Class & Object Architecture';
    if (content.includes('heap') || content.includes('priority')) return '⚡ Binary Heap Complete Tree Architecture';
    if (content.includes('tree') || content.includes('bst')) return '🌲 Binary Tree Structure Model';
    if (content.includes('stack') || content.includes('lifo') || content.includes('infix') || content.includes('postfix')) return '🥞 Stack ADT & Frame Architecture';
    if (content.includes('queue') || content.includes('fifo')) return '🚶 Queue FIFO Flow Architecture';
    if (content.includes('hash') || content.includes('collision') || content.includes('probing') || content.includes('chaining')) return '🔑 Hash Table & Collision Architecture';
    if (content.includes('sort') || content.includes('bubble') || content.includes('quick') || content.includes('merge')) return '🔀 Sorting Algorithm Workflow';
    return '🔬 แบบจำลองโครงสร้างสถาปัตยกรรม (DSA Studio Architecture)';
  }

  function buildNativeDsaVisual(code, docId) {
    const lower = code.toLowerCase();

    // Helper: Defs for Neon Glow Filters
    const svgDefs = `
      <defs>
        <filter id="dsa-glow-cyan" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="dsa-glow-amber" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="dsa-glow-emerald" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="dsa-glow-red" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <marker id="dsa-arrow-cyan" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M 0 1 L 7 4 L 0 7 z" fill="#4fd1e8" />
        </marker>
        <marker id="dsa-arrow-amber" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M 0 1 L 7 4 L 0 7 z" fill="#f59e0b" />
        </marker>
      </defs>
    `;

    // 1. Binary Min-Heap (Exam Preset & Insert 14 Tracing - Chapter 07.1 & 11.6)
    if (code.includes('H13') || (code.includes('13') && code.includes('21') && (code.includes('31') || code.includes('32') || code.includes('hole') || code.includes('Hole')))) {
      return {
        title: '⚡ Binary Min-Heap Architecture: 10 Nodes + Slot [11] Candidate Hole (Insert 14)',
        topicHash: '#heap',
        html: `
          <div class="dsa-native-heap-wrap">
            <svg viewBox="0 0 760 320" style="width:100%;max-width:760px;">
              ${svgDefs}
              <!-- Branch Lines Level 0 to 1 -->
              <line x1="380" y1="42" x2="200" y2="115" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="42" x2="560" y2="115" stroke="#334155" stroke-width="2.5" />

              <!-- Branch Lines Level 1 to 2 -->
              <line x1="200" y1="115" x2="110" y2="188" stroke="#334155" stroke-width="2.5" />
              <line x1="200" y1="115" x2="290" y2="188" stroke="#334155" stroke-width="2.5" />
              <line x1="560" y1="115" x2="470" y2="188" stroke="#334155" stroke-width="2.5" />
              <line x1="560" y1="115" x2="650" y2="188" stroke="#334155" stroke-width="2.5" />

              <!-- Branch Lines Level 2 to 3 -->
              <line x1="110" y1="188" x2="65" y2="262" stroke="#334155" stroke-width="2.5" />
              <line x1="110" y1="188" x2="155" y2="262" stroke="#334155" stroke-width="2.5" />
              <line x1="290" y1="188" x2="245" y2="262" stroke="#334155" stroke-width="2.5" />
              <line x1="290" y1="188" x2="335" y2="262" stroke="#f59e0b" stroke-width="2.2" stroke-dasharray="4 4" />

              <!-- Level 0: Root 13 [1] -->
              <circle cx="380" cy="42" r="24" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="380" y="47" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">13</text>
              <text x="380" y="16" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">[1] Root</text>

              <!-- Level 1: 21 [2] & 16 [3] -->
              <circle cx="200" cy="115" r="22" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" filter="url(#dsa-glow-cyan)" />
              <text x="200" y="120" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">21</text>
              <text x="200" y="90" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">[2]</text>

              <circle cx="560" cy="115" r="22" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" filter="url(#dsa-glow-cyan)" />
              <text x="560" y="120" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">16</text>
              <text x="560" y="90" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">[3]</text>

              <!-- Level 2: 24 [4], 31 [5], 19 [6], 68 [7] -->
              <circle cx="110" cy="188" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="110" y="193" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">24</text>
              <text x="110" y="164" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">[4]</text>

              <circle cx="290" cy="188" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="290" y="193" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">31</text>
              <text x="290" y="164" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">[5]</text>

              <circle cx="470" cy="188" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="470" y="193" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">19</text>
              <text x="470" y="164" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">[6]</text>

              <circle cx="650" cy="188" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="650" y="193" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">68</text>
              <text x="650" y="164" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">[7]</text>

              <!-- Level 3: 65 [8], 26 [9], 32 [10], and Hole [11] -->
              <circle cx="65" cy="262" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="65" y="267" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">65</text>
              <text x="65" y="238" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[8]</text>

              <circle cx="155" cy="262" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="155" y="267" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">26</text>
              <text x="155" y="238" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[9]</text>

              <circle cx="245" cy="262" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="245" y="267" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">32</text>
              <text x="245" y="238" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[10]</text>

              <!-- Candidate Hole [11] -->
              <circle cx="335" cy="262" r="19" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4 4" filter="url(#dsa-glow-amber)" />
              <text x="335" y="267" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="800" text-anchor="middle">14?</text>
              <text x="335" y="238" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" text-anchor="middle">[11] Hole</text>
            </svg>

            <!-- 1-Based Memory Array Representation (All 11 Slots) -->
            <div class="dsa-heap-array-row">
              <div class="dsa-heap-cell">
                <span class="cell-idx">[0]</span>
                <span class="cell-val" style="color:#64748b;">-</span>
              </div>
              <div class="dsa-heap-cell root-cell">
                <span class="cell-idx">[1] Root</span>
                <span class="cell-val">13</span>
              </div>
              <div class="dsa-heap-cell" style="border-color:#38bdf8;">
                <span class="cell-idx">[2] Target</span>
                <span class="cell-val">21</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[3]</span>
                <span class="cell-val">16</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[4]</span>
                <span class="cell-val">24</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[5]</span>
                <span class="cell-val">31</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[6]</span>
                <span class="cell-val">19</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[7]</span>
                <span class="cell-val">68</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[8]</span>
                <span class="cell-val">65</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[9]</span>
                <span class="cell-val">26</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[10]</span>
                <span class="cell-val">32</span>
              </div>
              <div class="dsa-heap-cell" style="border-color:#f59e0b;background:rgba(245,158,11,0.12);border-style:dashed;">
                <span class="cell-idx" style="color:#fbbf24;">[11] Hole</span>
                <span class="cell-val" style="color:#fbbf24;">14?</span>
              </div>
            </div>

            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip" style="background:rgba(245,158,11,0.15);border-color:rgba(245,158,11,0.4);color:#fbbf24;">
                🎯 Percolate Up (Swim): Round 1 (14 &lt; 31) ➔ Round 2 (14 &lt; 21) ➔ Round 3 (14 &gt; 13 หยุดลูป!) ➔ บรรจุ 14 ที่ Index [2]
              </span>
            </div>
          </div>
        `
      };
    }

    // 2. Binary Min-Heap (7-Node Complete Tree)
    if (code.includes('Min-Heap Root') || (code.includes('13') && code.includes('14') && code.includes('16') && code.includes('68'))) {
      return {
        title: '⚡ Binary Min-Heap: Complete Binary Tree & 1-Based Array Indexing',
        topicHash: '#heap',
        html: `
          <div class="dsa-native-heap-wrap">
            <svg viewBox="0 0 520 200" style="width:100%;max-width:520px;">
              ${svgDefs}
              <line x1="260" y1="36" x2="150" y2="92" stroke="#334155" stroke-width="2.5" />
              <line x1="260" y1="36" x2="370" y2="92" stroke="#334155" stroke-width="2.5" />
              <line x1="150" y1="92" x2="100" y2="152" stroke="#334155" stroke-width="2.5" />
              <line x1="150" y1="92" x2="200" y2="152" stroke="#334155" stroke-width="2.5" />
              <line x1="370" y1="92" x2="320" y2="152" stroke="#334155" stroke-width="2.5" />
              <line x1="370" y1="92" x2="420" y2="152" stroke="#334155" stroke-width="2.5" />

              <circle cx="260" cy="36" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="260" y="42" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">13</text>
              <text x="260" y="14" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">[1] Min</text>

              <circle cx="150" cy="92" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="150" y="97" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">14</text>
              <text x="150" y="68" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">[2]</text>

              <circle cx="370" cy="92" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="370" y="97" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">16</text>
              <text x="370" y="68" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">[3]</text>

              <circle cx="100" cy="152" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="100" y="157" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">24</text>
              <text x="100" y="130" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[4]</text>

              <circle cx="200" cy="152" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="200" y="157" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">21</text>
              <text x="200" y="130" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[5]</text>

              <circle cx="320" cy="152" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="320" y="157" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">19</text>
              <text x="320" y="130" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[6]</text>

              <circle cx="420" cy="152" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="420" y="157" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">68</text>
              <text x="420" y="130" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">[7]</text>
            </svg>

            <div class="dsa-heap-array-row">
              <div class="dsa-heap-cell">
                <span class="cell-idx">[0]</span>
                <span class="cell-val" style="color:#64748b;">-</span>
              </div>
              <div class="dsa-heap-cell root-cell">
                <span class="cell-idx">[1] Root</span>
                <span class="cell-val">13</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[2] L</span>
                <span class="cell-val">14</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[3] R</span>
                <span class="cell-val">16</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[4] LL</span>
                <span class="cell-val">24</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[5] LR</span>
                <span class="cell-val">21</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[6] RL</span>
                <span class="cell-val">19</span>
              </div>
              <div class="dsa-heap-cell">
                <span class="cell-idx">[7] RR</span>
                <span class="cell-val">68</span>
              </div>
            </div>

            <div class="dsa-heap-formulas">
              <span>Parent(i) = ⌊i/2⌋</span>
              <span>Left(i) = 2 × i</span>
              <span>Right(i) = 2 × i + 1</span>
            </div>
          </div>
        `
      };
    }

    // 3. Binary Search Tree (BST Insertion - Chapter 05.2)
    if (code.includes('แทรกใหม่รอบที่ 3') || code.includes('N5["5 (โหนดใหม่)"]') || (code.includes('N6') && code.includes('N2') && code.includes('N8') && code.includes('N4') && code.includes('N5'))) {
      return {
        title: '🌲 Binary Search Tree: การแทรกเลข 5 สำเร็จที่รอบ 3 (Insertion Tracing)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <svg viewBox="0 0 540 290" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="42" x2="160" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="42" x2="380" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="100" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="220" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="220" y1="170" x2="180" y2="235" stroke="#334155" stroke-width="2.5" />
              <line x1="220" y1="170" x2="260" y2="235" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 4" />

              <circle cx="270" cy="42" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="47" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">6</text>
              <text x="270" y="16" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Root</text>

              <circle cx="160" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="110" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">2</text>
              <text x="160" y="78" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">5 &lt; 6 (L)</text>

              <circle cx="380" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="380" y="110" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">8</text>

              <circle cx="100" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="100" y="175" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>

              <circle cx="220" cy="170" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" />
              <text x="220" y="175" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>
              <text x="220" y="142" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">5 &gt; 2 (R)</text>

              <circle cx="180" cy="235" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="180" y="240" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>

              <!-- Newly Inserted Node 5 -->
              <circle cx="260" cy="235" r="20" fill="#064e3b" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" />
              <text x="260" y="240" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="800" text-anchor="middle">5</text>
              <text x="260" y="270" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" text-anchor="middle">✨ โหนดใหม่</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.4);color:#6ee7b7;">
                🎯 Round 1: 5 &lt; 6 (ซ้าย) ➔ Round 2: 5 &gt; 2 (ขวา) ➔ Round 3: 5 &gt; 4 (ขวาว่าง ➔ แทรก 5 ที่ current_node.right สำเร็จ!)
              </span>
            </div>
          </div>
        `
      };
    }

    // 4. Binary Search Tree (BST Insertion - Pre-insert tree)
    if (code.includes('N6["6 (Root)"]') || (code.includes('N6["6"]') && code.includes('N4["4"]'))) {
      return {
        title: '🌲 Binary Search Tree: โครงสร้างก่อนแทรกเลข 5 (Candidate Tree)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <svg viewBox="0 0 540 260" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="42" x2="160" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="42" x2="380" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="100" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="220" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="220" y1="170" x2="180" y2="235" stroke="#334155" stroke-width="2.5" />

              <circle cx="270" cy="42" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="47" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">6</text>
              <text x="270" y="16" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Root</text>

              <circle cx="160" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="110" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">2</text>

              <circle cx="380" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="380" y="110" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">8</text>

              <circle cx="100" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="100" y="175" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>

              <circle cx="220" cy="170" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" />
              <text x="220" y="175" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>

              <circle cx="180" cy="235" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="180" y="240" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 เตรียมแทรกค่า 5: จะต้องเปรียบเทียบจาก 6 ➔ 2 ➔ 4</span>
            </div>
          </div>
        `
      };
    }

    // 5. Binary Search Tree (BST Deletion Cases - Chapter 05.3 & 11.6)
    if (code.includes('BeforeDelete') || code.includes('AfterDelete') || code.includes('โหนดที่จะลบ - มีลูก 2 ข้าง') || (code.includes('Successor') && code.includes('Delete'))) {
      return {
        title: '✂️ BST Case 3 Deletion: การแทนที่ด้วย Inorder Successor (Before & After Comparison)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:20px;width:100%;">
              <div style="background:#131622;padding:16px;border-radius:10px;border:1px solid rgba(239,68,68,0.3);text-align:center;">
                <div style="font-size:12px;font-weight:700;color:#f87171;margin-bottom:10px;">🔴 ก่อนลบ: โหนด 4 (เป้าหมาย) &amp; โหนด 5 (Inorder Successor)</div>
                <svg viewBox="0 0 280 200" style="width:100%;max-width:280px;">
                  ${svgDefs}
                  <line x1="140" y1="30" x2="80" y2="80" stroke="#334155" stroke-width="2" />
                  <line x1="140" y1="30" x2="200" y2="80" stroke="#334155" stroke-width="2" />
                  <line x1="80" y1="80" x2="45" y2="135" stroke="#334155" stroke-width="2" />
                  <line x1="80" y1="80" x2="115" y2="135" stroke="#10b981" stroke-width="2.5" />
                  <line x1="45" y1="135" x2="25" y2="180" stroke="#334155" stroke-width="2" />

                  <circle cx="140" cy="30" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                  <text x="140" y="34" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">6</text>

                  <circle cx="80" cy="80" r="20" fill="#450a0a" stroke="#ef4444" stroke-width="2.8" filter="url(#dsa-glow-red)" />
                  <text x="80" y="85" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">4</text>

                  <circle cx="200" cy="80" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                  <text x="200" y="84" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">7</text>

                  <circle cx="45" cy="135" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                  <text x="45" y="139" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">3</text>

                  <circle cx="115" cy="135" r="18" fill="#064e3b" stroke="#10b981" stroke-width="2.5" filter="url(#dsa-glow-emerald)" />
                  <text x="115" y="140" fill="#fff" font-size="13" font-weight="800" text-anchor="middle">5</text>

                  <circle cx="25" cy="180" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
                  <text x="25" y="184" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">2</text>
                </svg>
              </div>

              <div style="background:#131622;padding:16px;border-radius:10px;border:1px solid rgba(16,185,129,0.3);text-align:center;">
                <div style="font-size:12px;font-weight:700;color:#34d399;margin-bottom:10px;">🟢 หลังลบ: ก๊อปปี้ 5 มาทับ 4 และลบ 5 ตัวล่างทิ้ง</div>
                <svg viewBox="0 0 280 200" style="width:100%;max-width:280px;">
                  ${svgDefs}
                  <line x1="140" y1="30" x2="80" y2="80" stroke="#334155" stroke-width="2" />
                  <line x1="140" y1="30" x2="200" y2="80" stroke="#334155" stroke-width="2" />
                  <line x1="80" y1="80" x2="45" y2="135" stroke="#334155" stroke-width="2" />
                  <line x1="45" y1="135" x2="25" y2="180" stroke="#334155" stroke-width="2" />

                  <circle cx="140" cy="30" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                  <text x="140" y="34" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">6</text>

                  <circle cx="80" cy="80" r="20" fill="#064e3b" stroke="#10b981" stroke-width="2.8" filter="url(#dsa-glow-emerald)" />
                  <text x="80" y="85" fill="#fff" font-size="14" font-weight="800" text-anchor="middle">5</text>

                  <circle cx="200" cy="80" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                  <text x="200" y="84" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">7</text>

                  <circle cx="45" cy="135" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                  <text x="45" y="139" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">3</text>

                  <circle cx="25" cy="180" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
                  <text x="25" y="184" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">2</text>
                </svg>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚖️ Case 3 Rule: เดินขวา 1 ก้าวแล้วซ้ายสุด ➔ ได้ Inorder Successor (5) ➔ ก๊อปปี้แทนที่ 4</span>
            </div>
          </div>
        `
      };
    }

    // 6. BST Standard 7-Node Model (6, 4, 7, 3, 5, 2, 1)
    if (code.includes('6 (Root)') && (code.includes('4 < 6') || code.includes('4 (4 < 6)'))) {
      return {
        title: '🌲 Binary Search Tree (BST) Architecture & Inorder Property',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <svg viewBox="0 0 540 280" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="40" x2="160" y2="100" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="40" x2="380" y2="100" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="100" x2="100" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="100" x2="220" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="100" y1="160" x2="60" y2="215" stroke="#334155" stroke-width="2.5" />
              <line x1="60" y1="215" x2="30" y2="260" stroke="#334155" stroke-width="2.5" />

              <circle cx="270" cy="40" r="24" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="46" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">6</text>
              <text x="270" y="16" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600" text-anchor="middle">Root</text>

              <circle cx="160" cy="100" r="22" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="106" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">4</text>
              <text x="160" y="76" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">&lt; 6</text>

              <circle cx="380" cy="100" r="22" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" filter="url(#dsa-glow-cyan)" />
              <text x="380" y="106" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">7</text>
              <text x="380" y="76" fill="#4fd1e8" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">&gt; 6</text>

              <circle cx="100" cy="160" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="100" y="166" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>

              <circle cx="220" cy="160" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="220" y="166" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">5</text>

              <circle cx="60" cy="215" r="19" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="60" y="221" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">2</text>

              <circle cx="30" cy="260" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="30" y="265" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="13" font-weight="700" text-anchor="middle">1</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚖️ กฎ BST: L &lt; Root &lt; R</span>
              <span class="dsa-tree-chip" style="background:rgba(79,209,232,0.15);border-color:rgba(79,209,232,0.4);color:#4fd1e8;">
                🔀 Inorder Traversal: [ 1 ➔ 2 ➔ 3 ➔ 4 ➔ 5 ➔ 6 ➔ 7 ] (เรียงลำดับเสมอ)
              </span>
            </div>
          </div>
        `
      };
    }

    // 7. Tree Terminology & Levels (Chapter 05.1)
    if (code.includes('Root: A') || (code.includes('Internal Node') && code.includes('Leaf, Depth'))) {
      return {
        title: '🌲 Tree Terminology Architecture: Root, Internal Nodes, Leaves & Depth/Height Levels',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <svg viewBox="0 0 540 240" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="40" x2="160" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="40" x2="380" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="110" y2="175" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="210" y2="175" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="105" x2="380" y2="175" stroke="#334155" stroke-width="2.5" />

              <circle cx="270" cy="40" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="46" fill="#fff" font-size="15" font-weight="700" text-anchor="middle">A</text>
              <text x="270" y="16" fill="#f59e0b" font-size="10.5" font-weight="700" text-anchor="middle">Root (Depth=0, Height=2)</text>

              <circle cx="160" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="110" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">B</text>
              <text x="160" y="80" fill="#94a3b8" font-size="9" text-anchor="middle">Internal Node</text>

              <circle cx="380" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="380" y="110" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">C</text>
              <text x="380" y="80" fill="#94a3b8" font-size="9" text-anchor="middle">Internal Node</text>

              <circle cx="110" cy="175" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="110" y="180" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">D</text>
              <text x="110" y="205" fill="#34d399" font-size="9" text-anchor="middle">Leaf</text>

              <circle cx="210" cy="175" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="210" y="180" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">E</text>
              <text x="210" y="205" fill="#34d399" font-size="9" text-anchor="middle">Leaf</text>

              <circle cx="380" cy="175" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="380" y="180" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">F</text>
              <text x="380" y="205" fill="#34d399" font-size="9" text-anchor="middle">Leaf</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🍃 Leaves: D, E, F (Degree 0, Height 0)</span>
              <span class="dsa-tree-chip">👑 Root: A (Depth 0)</span>
            </div>
          </div>
        `
      };
    }

    // 8. Full vs Complete Binary Tree (Chapter 05.1)
    if (code.includes('FullBT') || code.includes('CompleteBT') || (code.includes('Full Binary Tree') && code.includes('Complete Binary Tree'))) {
      return {
        title: '🌴 Structural Comparison: Full Binary Tree vs Complete Binary Tree',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:20px;width:100%;">
              <div style="background:#131622;padding:16px;border-radius:10px;border:1px solid rgba(79,209,232,0.25);text-align:center;">
                <div style="font-size:12.5px;font-weight:700;color:#38bdf8;margin-bottom:10px;">🌟 Full Binary Tree (ทุกโหนดมีลูก 0 หรือ 2 ตัว)</div>
                <svg viewBox="0 0 260 160" style="width:100%;max-width:260px;">
                  <line x1="130" y1="25" x2="70" y2="75" stroke="#334155" stroke-width="2" />
                  <line x1="130" y1="25" x2="190" y2="75" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="75" x2="40" y2="125" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="75" x2="100" y2="125" stroke="#334155" stroke-width="2" />
                  <circle cx="130" cy="25" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="130" y="29" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">A</text>
                  <circle cx="70" cy="75" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="70" y="79" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">B</text>
                  <circle cx="190" cy="75" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="190" y="79" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">C</text>
                  <circle cx="40" cy="125" r="14" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="40" y="129" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">D</text>
                  <circle cx="100" cy="125" r="14" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="100" y="129" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">E</text>
                </svg>
              </div>

              <div style="background:#131622;padding:16px;border-radius:10px;border:1px solid rgba(245,158,11,0.25);text-align:center;">
                <div style="font-size:12.5px;font-weight:700;color:#fbbf24;margin-bottom:10px;">⚡ Complete Binary Tree (เติมเต็มซ้ายไปขวา ใช้ใน Heap)</div>
                <svg viewBox="0 0 260 160" style="width:100%;max-width:260px;">
                  <line x1="130" y1="25" x2="70" y2="75" stroke="#334155" stroke-width="2" />
                  <line x1="130" y1="25" x2="190" y2="75" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="75" x2="40" y2="125" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="75" x2="100" y2="125" stroke="#334155" stroke-width="2" />
                  <line x1="190" y1="75" x2="160" y2="125" stroke="#334155" stroke-width="2" />
                  <circle cx="130" cy="25" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="130" y="29" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">A</text>
                  <circle cx="70" cy="75" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="70" y="79" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">B</text>
                  <circle cx="190" cy="75" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="190" y="79" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">C</text>
                  <circle cx="40" cy="125" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="40" y="129" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">D</text>
                  <circle cx="100" cy="125" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="100" y="129" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">E</text>
                  <circle cx="160" cy="125" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="160" y="129" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">F</text>
                </svg>
              </div>
            </div>
          </div>
        `
      };
    }

    // 9. Tree Traversals Slide 2 (Chapter 05.1: 10, 3, 19, 8, 5, 15, 24)
    if (code.includes('N10["10 (Root)"]') || (code.includes('10 (Root)') && code.includes('19'))) {
      return {
        title: '🌲 Binary Tree Traversals: Pre-order, In-order, and Post-order Tracing',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-tree-wrap">
            <svg viewBox="0 0 540 220" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="36" x2="160" y2="95" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="36" x2="380" y2="95" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="95" x2="110" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="95" x2="210" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="95" x2="330" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="95" x2="430" y2="160" stroke="#334155" stroke-width="2.5" />

              <circle cx="270" cy="36" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="41" fill="#fff" font-size="15" font-weight="700" text-anchor="middle">10</text>
              <text x="270" y="12" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="middle">Root</text>

              <circle cx="160" cy="95" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="160" y="100" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">3</text>

              <circle cx="380" cy="95" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="380" y="100" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">19</text>

              <circle cx="110" cy="160" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="110" y="165" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">8</text>

              <circle cx="210" cy="160" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="210" y="165" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">5</text>

              <circle cx="330" cy="160" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="330" y="165" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">15</text>

              <circle cx="430" cy="160" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="430" y="165" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">24</text>
            </svg>
            <div class="dsa-tree-footer" style="flex-direction:column;gap:8px;">
              <span class="dsa-tree-chip">🔵 Pre-Order (Root ➔ L ➔ R): 10, 3, 8, 5, 19, 15, 24</span>
              <span class="dsa-tree-chip" style="background:rgba(79,209,232,0.15);border-color:rgba(79,209,232,0.4);color:#4fd1e8;">🟡 In-Order (L ➔ Root ➔ R): 8, 3, 5, 10, 15, 19, 24</span>
              <span class="dsa-tree-chip" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.4);color:#6ee7b7;">🟢 Post-Order (L ➔ R ➔ Root): 8, 5, 3, 15, 24, 19, 10</span>
            </div>
          </div>
        `
      };
    }

    // 10. Singly Linked List
    if ((lower.includes('head =') || lower.includes('headptr')) && lower.includes('data:') && !lower.includes('prev:')) {
      const matches = [...code.matchAll(/Node\s*(?:\d+)?\s*@\s*(0x[0-9A-Fa-f]+)[\s\S]*?Data:\s*([^\s\]"]+)[\s\S]*?next:\s*([^\s\]"]+)/g)];
      if (matches.length >= 2) {
        let headAddr = '0x100';
        const headMatch = code.match(/head\s*=\s*(0x[0-9A-Fa-f]+)/i);
        if (headMatch) headAddr = headMatch[1];

        let nodesHtml = '';
        matches.forEach((m, idx) => {
          const addr = m[1];
          const val = m[2];
          const nextAddr = m[3];
          nodesHtml += `
            <div class="ll-node-card">
              <div class="ll-addr">Node ${idx + 1} @ ${escapeHtml(addr)}</div>
              <div class="ll-data">${escapeHtml(val)}</div>
              <div class="ll-next">next: ${escapeHtml(nextAddr)}</div>
            </div>
            <span class="ll-pointer-arrow">➔</span>
          `;
        });

        return {
          title: '🔗 Singly Linked List Memory Model (โครงสร้างพอยน์เตอร์ในหน่วยความจำ)',
          topicHash: '',
          html: `
            <div class="dsa-native-ll-model singly">
              <div class="ll-head-badge">
                <span class="badge-label">HEAD</span>
                <span class="badge-addr">${escapeHtml(headAddr)}</span>
              </div>
              <span class="ll-pointer-arrow">➔</span>
              ${nodesHtml}
              <div class="ll-null-badge">🚫 None (จุดสิ้นสุด List)</div>
            </div>
          `
        };
      }
    }

    // 11. Doubly Linked List Check
    if (lower.includes('prev:') && lower.includes('next:') && lower.includes('data:')) {
      const matches = [...code.matchAll(/Node\s*(\d+)?\s*@\s*(0x[0-9A-Fa-f]+)[\s\S]*?prev:\s*([^\s\]"]+)[\s\S]*?Data:\s*([^\s\]"]+)[\s\S]*?next:\s*([^\s\]"]+)/g)];
      if (matches.length >= 2) {
        let headAddr = matches[0][2];
        let nodesHtml = '';
        matches.forEach((m, idx) => {
          const nodeNum = m[1] || (idx + 1);
          const addr = m[2];
          const prevAddr = m[3];
          const val = m[4];
          const nextAddr = m[5];
          const arrow = (idx < matches.length - 1)
            ? '<span class="ll-pointer-arrow double">⇄</span>'
            : '<span class="ll-pointer-arrow">➔</span>';
          nodesHtml += `
            <div class="ll-node-card doubly">
              <div class="ll-addr">Node ${nodeNum} @ ${escapeHtml(addr)}</div>
              <div class="ll-data">${escapeHtml(val)}</div>
              <div class="ll-doubly-row">
                <span class="ll-prev">prev: ${escapeHtml(prevAddr)}</span>
                <span class="ll-next">next: ${escapeHtml(nextAddr)}</span>
              </div>
            </div>
            ${arrow}
          `;
        });

        return {
          title: '🔗 Doubly Linked List Model (แบบจำลองเชื่อมโยงสองทิศทาง)',
          topicHash: '',
          html: `
            <div class="dsa-native-ll-model doubly">
              <div class="ll-head-badge">
                <span class="badge-label">HEAD</span>
                <span class="badge-addr">${escapeHtml(headAddr)}</span>
              </div>
              <span class="ll-pointer-arrow">➔</span>
              ${nodesHtml}
              <div class="ll-null-badge">🚫 None</div>
            </div>
          `
        };
      }
    }

    // 12. Circular Linked List
    if (lower.includes('chead') || lower.includes('circular linked list') || (lower.includes('head') && lower.includes('cn1'))) {
      return {
        title: '🔄 Circular Linked List Architecture (โหนดท้ายวนกลับมาชี้ Head)',
        topicHash: '',
        html: `
          <div class="dsa-native-ll-model circular">
            <div class="ll-head-badge">
              <span class="badge-label">HEAD</span>
              <span class="badge-addr">0x100</span>
            </div>
            <span class="ll-pointer-arrow">➔</span>
            <div class="ll-node-card">
              <div class="ll-addr">Node 1 @ 0x100</div>
              <div class="ll-data">10</div>
              <div class="ll-next">next: 0x240 ➔</div>
            </div>
            <span class="ll-pointer-arrow">➔</span>
            <div class="ll-node-card">
              <div class="ll-addr">Node 2 @ 0x240</div>
              <div class="ll-data">20</div>
              <div class="ll-next">next: 0x380 ➔</div>
            </div>
            <span class="ll-pointer-arrow">➔</span>
            <div class="ll-node-card">
              <div class="ll-addr">Node 3 @ 0x380</div>
              <div class="ll-data">30</div>
              <div class="ll-next">next: 0x100 (วนกลับ Head!)</div>
            </div>
            <span class="ll-pointer-arrow" style="color:var(--amber, #f59e0b);">⤴ วนรอบสมบูรณ์</span>
          </div>
        `
      };
    }

    // 13. Stack Architecture (Chapter 04.1)
    if (lower.includes('stack') || lower.includes('lifo') || lower.includes('push') || lower.includes('pop')) {
      return {
        title: '🥞 Stack ADT Memory Model: LIFO (Last-In First-Out) Canister',
        topicHash: '',
        html: `
          <div style="display:flex;align-items:center;justify-content:center;gap:30px;flex-wrap:wrap;padding:16px;">
            <div style="display:flex;flex-direction:column;align-items:center;">
              <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#f59e0b;font-weight:700;margin-bottom:6px;">TOP ➔ [ชี้สมาชิกบนสุด]</div>
              <div style="width:140px;border:2px solid #6366f1;border-top:none;border-radius:0 0 12px 12px;padding:8px 8px 12px;display:flex;flex-direction:column;gap:6px;background:rgba(99,102,241,0.06);">
                <div style="background:#1e2235;border:1px solid #f59e0b;border-radius:6px;padding:8px;text-align:center;font-weight:700;color:#fbbf24;box-shadow:0 0 10px rgba(245,158,11,0.3);">30 (Top)</div>
                <div style="background:#191c28;border:1px solid #4fd1e8;border-radius:6px;padding:8px;text-align:center;font-weight:700;color:#fff;">20</div>
                <div style="background:#191c28;border:1px solid #4fd1e8;border-radius:6px;padding:8px;text-align:center;font-weight:700;color:#fff;">10 (Bottom)</div>
              </div>
            </div>
            <div style="display:flex;flex-direction:column;gap:10px;font-size:12.5px;">
              <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.3);padding:8px 14px;border-radius:8px;color:#34d399;">
                📥 <b>push(x)</b>: ใส่ข้อมูลลงบนสุดของ Stack (O(1))
              </div>
              <div style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);padding:8px 14px;border-radius:8px;color:#fca5a5;">
                📤 <b>pop()</b>: ดึงข้อมูลบนสุด (Top) ออกมาก่อนเสมอ (O(1))
              </div>
              <div style="background:rgba(79,209,232,0.12);border:1px solid rgba(79,209,232,0.3);padding:8px 14px;border-radius:8px;color:#4fd1e8;">
                👀 <b>peek()</b>: ส่องดูค่าบนสุดโดยไม่นำออก (O(1))
              </div>
            </div>
          </div>
        `
      };
    }

    // 14. Fallback: Universal Smart DSA Lab SVG Generator (Zero Mermaid dependency)
    return generateGenericDsaLabVisual(code, getArchitectureTitle(code));
  }

  // Universal Smart DSA Lab SVG Generator
  function generateGenericDsaLabVisual(code, title) {
    const lines = code.split('\n');
    const nodes = new Map();
    const edges = [];

    // Parse Mermaid-like syntax
    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('graph') || trimmed.startsWith('flowchart') || trimmed.startsWith('subgraph') || trimmed.startsWith('end') || trimmed.startsWith('style') || trimmed.startsWith('classDef')) return;

      // Match edge pattern: A --> B or A["Label"] --> B["Label"] or A -->|label| B
      const edgeRegex = /([A-Za-z0-9_]+)(?:\["([^"]*)"\]|\(([^)]*)\))?\s*(-+>|---)\s*(?:\|([^|]*)\|)?\s*([A-Za-z0-9_]+)(?:\["([^"]*)"\]|\(([^)]*)\))?/;
      const match = trimmed.match(edgeRegex);

      if (match) {
        const uId = match[1];
        const uLabel = match[2] || match[3] || uId;
        const edgeText = match[5] || '';
        const vId = match[6];
        const vLabel = match[7] || match[8] || vId;

        if (!nodes.has(uId)) nodes.set(uId, { id: uId, label: uLabel });
        if (!nodes.has(vId)) nodes.set(vId, { id: vId, label: vLabel });

        edges.push({ from: uId, to: vId, text: edgeText });
      } else {
        // Standalone node: A["Label"]
        const nodeMatch = trimmed.match(/([A-Za-z0-9_]+)(?:\["([^"]*)"\]|\(([^)]*)\))/);
        if (nodeMatch) {
          const id = nodeMatch[1];
          const label = nodeMatch[2] || nodeMatch[3] || id;
          if (!nodes.has(id)) nodes.set(id, { id, label });
        }
      }
    });

    const nodeList = Array.from(nodes.values());
    if (nodeList.length === 0) {
      return {
        title: title || '🔬 DSA Studio Architecture Model',
        topicHash: '',
        html: `
          <div style="padding:24px;text-align:center;font-family:'JetBrains Mono',monospace;color:#94a3b8;font-size:13px;">
            💎 โครงสร้างแบบจำลองสถาปัตยกรรม DSA Lab Studio
          </div>
        `
      };
    }

    // Compute node layers using BFS
    const inDegree = new Map();
    nodeList.forEach(n => inDegree.set(n.id, 0));
    edges.forEach(e => {
      inDegree.set(e.to, (inDegree.get(e.to) || 0) + 1);
    });

    const roots = nodeList.filter(n => inDegree.get(n.id) === 0);
    if (roots.length === 0 && nodeList.length > 0) roots.push(nodeList[0]);

    const layers = [];
    const visited = new Set();
    let currentLevel = [...roots];

    while (currentLevel.length > 0 && layers.length < 8) {
      layers.push(currentLevel);
      currentLevel.forEach(n => visited.add(n.id));

      const nextLevel = [];
      currentLevel.forEach(n => {
        edges.filter(e => e.from === n.id).forEach(e => {
          if (!visited.has(e.to) && !nextLevel.some(x => x.id === e.to)) {
            const nextNode = nodes.get(e.to);
            if (nextNode) nextLevel.push(nextNode);
          }
        });
      });
      currentLevel = nextLevel;
    }

    // Place remaining unvisited nodes into a final layer
    const unvisited = nodeList.filter(n => !visited.has(n.id));
    if (unvisited.length > 0) layers.push(unvisited);

    // Coordinate calculation
    const maxNodesInLayer = Math.max(...layers.map(l => l.length), 1);
    const W = Math.max(640, maxNodesInLayer * 140);
    const H = Math.max(200, layers.length * 90 + 50);

    const nodeCoords = new Map();
    layers.forEach((layer, layerIdx) => {
      const y = 44 + layerIdx * 85;
      const count = layer.length;
      layer.forEach((node, nodeIdx) => {
        const x = (nodeIdx + 0.5) * (W / count);
        nodeCoords.set(node.id, { x, y, label: node.label });
      });
    });

    // Render Edges
    let edgesSvg = '';
    edges.forEach(e => {
      const from = nodeCoords.get(e.from);
      const to = nodeCoords.get(e.to);
      if (from && to) {
        edgesSvg += `<line x1="${from.x}" y1="${from.y}" x2="${to.x}" y2="${to.y}" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />`;
        if (e.text) {
          const midX = (from.x + to.x) / 2;
          const midY = (from.y + to.y) / 2 - 6;
          edgesSvg += `<text x="${midX}" y="${midY}" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">${escapeHtml(e.text)}</text>`;
        }
      }
    });

    // Render Nodes
    let nodesSvg = '';
    nodeCoords.forEach((coord, id) => {
      const isShort = coord.label.length <= 4;
      if (isShort) {
        nodesSvg += `
          <g>
            <circle cx="${coord.x}" cy="${coord.y}" r="22" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
            <text x="${coord.x}" y="${coord.y + 5}" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">${escapeHtml(coord.label)}</text>
          </g>
        `;
      } else {
        const rectW = Math.max(100, Math.min(coord.label.length * 8 + 24, 200));
        const rectH = 34;
        nodesSvg += `
          <g>
            <rect x="${coord.x - rectW / 2}" y="${coord.y - rectH / 2}" width="${rectW}" height="${rectH}" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" filter="url(#dsa-glow-cyan)" />
            <text x="${coord.x}" y="${coord.y + 4}" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="12" font-weight="600" text-anchor="middle">${escapeHtml(coord.label)}</text>
          </g>
        `;
      }
    });

    return {
      title: title || '🔬 DSA Studio Architecture Model',
      topicHash: '',
      html: `
        <div class="dsa-native-tree-wrap">
          <svg viewBox="0 0 ${W} ${H}" style="width:100%;max-width:${W}px;">
            <defs>
              <filter id="dsa-glow-cyan" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="3" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
              <marker id="dsa-arrow-cyan" markerWidth="8" markerHeight="8" refX="16" refY="4" orient="auto">
                <path d="M 0 1 L 7 4 L 0 7 z" fill="#4fd1e8" />
              </marker>
            </defs>
            ${edgesSvg}
            ${nodesSvg}
          </svg>
        </div>
      `
    };
  }

  async function renderMermaidDiagrams() {
    // 100% native DSA Lab models are rendered synchronously in postprocessHtml.
    // Zero Mermaid JS runtime calls needed.
  }

  function generateTableOfContents() {
    if (!elements.tocList) return;
    state.tocHeadings = [];

    const headings = elements.articleBody.querySelectorAll('h1, h2, h3');
    if (headings.length === 0) {
      elements.tocList.innerHTML = '<li class="toc-item"><span style="color:var(--text-muted);font-size:12px;">ไม่มีหัวข้อย่อยในบทนี้</span></li>';
      return;
    }

    let tocHtml = '';
    headings.forEach((heading, idx) => {
      if (!heading.id) {
        const cleanText = heading.textContent.trim().toLowerCase().replace(/[^\w\u0E00-\u0E7F\s-]/g, '').replace(/\s+/g, '-');
        heading.id = cleanText || `heading-${idx}`;
      }
      const level = parseInt(heading.tagName.substring(1), 10);
      const title = heading.textContent.replace(/^🗣️|📚|🧩|💡|⚙️|🔍|📌|🏛️|🔀|\d+\.\s*/g, '').trim();

      state.tocHeadings.push({ id: heading.id, el: heading });

      tocHtml += `
        <li class="toc-item">
          <a href="#${heading.id}" class="toc-link level-${level}" data-target="${heading.id}" title="${escapeHtml(heading.textContent)}">
            ${escapeHtml(title || heading.textContent)}
          </a>
        </li>
      `;
    });

    elements.tocList.innerHTML = tocHtml;

    elements.tocList.querySelectorAll('.toc-link').forEach(link => {
      link.addEventListener('click', e => {
        e.preventDefault();
        const targetEl = document.getElementById(link.dataset.target);
        if (targetEl) targetEl.scrollIntoView({ behavior: 'smooth' });
      });
    });
  }

  function updateScrollspy() {
    if (!state.tocHeadings || state.tocHeadings.length === 0) return;
    const scrollY = window.scrollY + 100;
    let activeId = state.tocHeadings[0].id;

    for (let i = 0; i < state.tocHeadings.length; i++) {
      if (scrollY >= state.tocHeadings[i].el.offsetTop) activeId = state.tocHeadings[i].id;
      else break;
    }

    if (elements.tocList) {
      elements.tocList.querySelectorAll('.toc-link').forEach(link => {
        link.classList.toggle('active', link.dataset.target === activeId);
      });
    }
  }

  function updateProgressBar() {
    if (!elements.progressBar) return;
    const docEl = document.documentElement;
    const scrollTotal = docEl.scrollHeight - docEl.clientHeight;
    if (scrollTotal <= 0) { elements.progressBar.style.width = '0%'; return; }
    const percent = Math.min(100, Math.max(0, (window.scrollY / scrollTotal) * 100));
    elements.progressBar.style.width = `${percent}%`;
  }

  function renderPagination(currentDocId) {
    if (!elements.paginationNav || !state.wikiData) return;
    const allDocs = getAllDocsOrderedInCurrentMode();
    const currentIndex = allDocs.findIndex(d => d.id === currentDocId);

    const prevDoc = currentIndex > 0 ? allDocs[currentIndex - 1] : null;
    const nextDoc = currentIndex < allDocs.length - 1 ? allDocs[currentIndex + 1] : null;

    let html = '';
    if (prevDoc) {
      html += `
        <a href="#/${encodeURIComponent(prevDoc.id)}" class="page-nav-card prev" data-doc-id="${escapeHtml(prevDoc.id)}">
          <span class="page-nav-direction">← บทก่อนหน้า</span>
          <span class="page-nav-title">${escapeHtml(formatDocNavTitle(prevDoc.id, prevDoc.title))}</span>
        </a>
      `;
    } else { html += '<div></div>'; }

    if (nextDoc) {
      html += `
        <a href="#/${encodeURIComponent(nextDoc.id)}" class="page-nav-card next" data-doc-id="${escapeHtml(nextDoc.id)}">
          <span class="page-nav-direction">บทถัดไป →</span>
          <span class="page-nav-title">${escapeHtml(formatDocNavTitle(nextDoc.id, nextDoc.title))}</span>
        </a>
      `;
    }

    elements.paginationNav.innerHTML = html;
    elements.paginationNav.querySelectorAll('.page-nav-card').forEach(card => {
      card.addEventListener('click', e => {
        e.preventDefault();
        navigateToDoc(card.dataset.docId);
      });
    });
  }

  function getAllDocsOrderedInCurrentMode() {
    const list = [];
    if (!state.wikiData) return list;
    const categories = state.currentMode === 'curriculum'
      ? (state.wikiData.curriculumCategories || [])
      : (state.wikiData.examCategories || []);
    categories.forEach(cat => cat.docs.forEach(doc => list.push(doc)));
    return list;
  }

  function buildSearchIndex() {
    state.searchIndex = [];
    if (!state.wikiData || !state.wikiData.documents) return;
    Object.values(state.wikiData.documents).forEach(doc => {
      state.searchIndex.push({
        id: doc.id,
        title: doc.title,
        excerpt: doc.excerpt,
        content: doc.content.toLowerCase()
      });
    });
  }

  function openSearchModal() {
    if (!elements.searchModal) return;
    elements.searchModal.classList.add('open');
    elements.searchInput.value = '';
    renderSearchResults('');
    setTimeout(() => { elements.searchInput.focus(); }, 50);
  }

  function closeSearchModal() {
    if (!elements.searchModal) return;
    elements.searchModal.classList.remove('open');
  }

  function renderSearchResults(query) {
    if (!elements.searchResults) return;
    const q = (query || '').trim().toLowerCase();

    if (!q) {
      let recentsHtml = '<div style="font-size:12px;color:var(--text-muted);padding:8px 12px;font-weight:600;">⚡ บทเรียนสำคัญที่แนะนำ:</div>';
      const featured = [
        '01.1 - Introduction to Data Structures & Algorithm Analysis',
        '02.1 - Linked Lists (Singly, Doubly, Circular)',
        '02.2 - Stacks & Applications (Infix, Postfix, Parentheses)',
        '03.2 - Binary Search Trees (BST) & Insertion',
        '04.1 - Priority Queue & Binary Heaps (Min-Heap, Max-Heap)',
        '05.1 - Sorting Algorithms (Bubble, Selection, Insertion, Merge, Quick)',
        '05.3 - Shortest Path Algorithms (Dijkstra, Unweighted Shortest Path)'
      ];
      featured.forEach(id => {
        const doc = state.wikiData.documents[id];
        if (doc) {
          recentsHtml += `
            <div class="search-result-item" data-doc-id="${escapeHtml(doc.id)}">
              <div class="search-result-title">📖 ${escapeHtml(formatDocNavTitle(doc.id, doc.title))}</div>
              <div class="search-result-snippet">${escapeHtml(doc.excerpt || 'คลิกเพื่ออ่านบทเรียน')}</div>
            </div>
          `;
        }
      });
      elements.searchResults.innerHTML = recentsHtml;
      attachSearchResultClicks();
      return;
    }

    const matches = [];
    state.searchIndex.forEach(item => {
      let score = 0;
      if (item.title.toLowerCase().includes(q)) score += 10;
      if (item.id.toLowerCase().includes(q)) score += 8;
      if (item.content.includes(q)) score += 2;
      if (score > 0) matches.push({ item, score });
    });

    matches.sort((a, b) => b.score - a.score);

    if (matches.length === 0) {
      elements.searchResults.innerHTML = `<div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 13px;">ไม่พบบทเรียนที่ตรงกับ "<b>${escapeHtml(query)}</b>"</div>`;
      return;
    }

    let html = '';
    matches.slice(0, 10).forEach(m => {
      html += `
        <div class="search-result-item" data-doc-id="${escapeHtml(m.item.id)}">
          <div class="search-result-title">📄 ${escapeHtml(formatDocNavTitle(m.item.id, m.item.title))}</div>
          <div class="search-result-snippet">${escapeHtml(m.item.excerpt || '')}</div>
        </div>
      `;
    });

    elements.searchResults.innerHTML = html;
    attachSearchResultClicks();
  }

  function attachSearchResultClicks() {
    elements.searchResults.querySelectorAll('.search-result-item').forEach(item => {
      item.addEventListener('click', () => {
        navigateToDoc(item.dataset.docId);
        closeSearchModal();
      });
    });
  }

  let currentZoom = 1.0;
  function openDiagramZoom(btn) {
    const card = btn.closest('.dsa-model-card, .mermaid-card');
    if (!card) return;
    const viewport = card.querySelector('.dsa-model-viewport, .mermaid-viewport');
    if (!viewport) return;
    elements.diagramCanvas.innerHTML = viewport.innerHTML;
    currentZoom = 1.0;
    elements.diagramModal.classList.add('open');
  }

  function closeDiagramZoom() {
    if (elements.diagramModal) elements.diagramModal.classList.remove('open');
  }

  function copyCode(btn) {
    const wrapper = btn.closest('.code-card-wrapper');
    if (!wrapper) return;
    const codeEl = wrapper.querySelector('code');
    if (!codeEl) return;
    navigator.clipboard.writeText(codeEl.textContent).then(() => {
      const orig = btn.innerHTML;
      btn.innerHTML = '✓ คัดลอกแล้ว!';
      setTimeout(() => { btn.innerHTML = orig; }, 2000);
      showToast('คัดลอกโค้ดไปยังคลิปบอร์ดแล้ว');
    });
  }

  function runInDsaLab(btn) {
    const wrapper = btn.closest('.code-card-wrapper');
    if (!wrapper) return;
    const codeEl = wrapper.querySelector('code');
    if (!codeEl) return;
    try {
      sessionStorage.setItem('dsalab_pending_code', codeEl.textContent);
    } catch (e) {}
    window.location.href = '../DsaLab/index.html';
  }

  function showToast(msg) {
    if (!elements.toast) return;
    elements.toast.textContent = msg;
    elements.toast.classList.add('show');
    setTimeout(() => { elements.toast.classList.remove('show'); }, 2500);
  }

  function setupEventListeners() {
    window.addEventListener('scroll', () => {
      updateProgressBar();
      updateScrollspy();
    }, { passive: true });

    window.addEventListener('hashchange', () => {
      const docId = getDocFromHash();
      const anchor = getAnchorFromHash();
      if (docId && docId !== state.currentDocId) navigateToDoc(docId, anchor);
    });

    // Sidebar Mode Tabs
    if (elements.tabModeCurriculum) {
      elements.tabModeCurriculum.addEventListener('click', () => {
        state.currentMode = 'curriculum';
        updateModeTabs();
        renderSidebar();
        // If current doc is an exam doc, navigate to Chapter 1
        if (state.currentDocId && (state.currentDocId.startsWith('11.') || state.currentDocId.includes('Glossary') || state.currentDocId.includes('Index'))) {
          navigateToDoc('01.1 - Introduction to Data Structures & Algorithm Analysis');
        }
      });
    }

    if (elements.tabModeExam) {
      elements.tabModeExam.addEventListener('click', () => {
        state.currentMode = 'exam';
        updateModeTabs();
        renderSidebar();
        // If current doc is not an exam doc, navigate to first exam mock
        if (state.currentDocId && !state.currentDocId.startsWith('11.') && !state.currentDocId.includes('Glossary') && !state.currentDocId.includes('Index')) {
          navigateToDoc('11.1 - Midterm Real Exam Mock & Solutions');
        }
      });
    }

    const fontDec = document.getElementById('font-decrease-btn');
    const fontInc = document.getElementById('font-increase-btn');
    if (fontDec) fontDec.addEventListener('click', () => applyFontSize(state.fontSize - 1));
    if (fontInc) fontInc.addEventListener('click', () => applyFontSize(state.fontSize + 1));

    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', () => applyTheme(state.theme === 'dark' ? 'light' : 'dark'));
    }

    if (elements.markReadBtn) {
      elements.markReadBtn.addEventListener('click', () => {
        if (!state.currentDocId) return;
        if (state.completedDocs.has(state.currentDocId)) {
          state.completedDocs.delete(state.currentDocId);
          updateMarkReadBtnState(false);
          showToast('ยกเลิกเครื่องหมายอ่านจบแล้ว');
        } else {
          state.completedDocs.add(state.currentDocId);
          updateMarkReadBtnState(true);
          showToast('🎉 บันทึกว่าอ่านจบบทนี้แล้ว!');
        }
        saveCompletedState();
        updateSidebarActiveState();
      });
    }

    if (elements.mobileToggleBtn) {
      elements.mobileToggleBtn.addEventListener('click', () => {
        elements.sidebar.classList.toggle('open');
        elements.sidebarBackdrop.classList.toggle('open');
      });
    }
    if (elements.sidebarBackdrop) {
      elements.sidebarBackdrop.addEventListener('click', closeMobileSidebar);
    }

    const searchTriggerBtn = document.getElementById('search-trigger-btn');
    if (searchTriggerBtn) searchTriggerBtn.addEventListener('click', openSearchModal);
    const searchCloseBtn = document.getElementById('search-close-btn');
    if (searchCloseBtn) searchCloseBtn.addEventListener('click', closeSearchModal);
    if (elements.searchModal) {
      elements.searchModal.addEventListener('click', e => { if (e.target === elements.searchModal) closeSearchModal(); });
    }
    if (elements.searchInput) {
      elements.searchInput.addEventListener('input', e => renderSearchResults(e.target.value));
    }

    window.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openSearchModal();
      } else if (e.key === 'Escape') {
        closeSearchModal();
        closeDiagramZoom();
        closeMobileSidebar();
      }
    });

    const diagramCloseBtn = document.getElementById('diagram-close-btn');
    if (diagramCloseBtn) diagramCloseBtn.addEventListener('click', closeDiagramZoom);

    if (elements.articleBody) {
      elements.articleBody.addEventListener('click', e => {
        const link = e.target.closest('.wiki-link');
        if (link) {
          e.preventDefault();
          navigateToDoc(link.dataset.doc, link.dataset.anchor);
        }
      });
    }
  }

  function closeMobileSidebar() {
    if (elements.sidebar) elements.sidebar.classList.remove('open');
    if (elements.sidebarBackdrop) elements.sidebarBackdrop.classList.remove('open');
  }

  function getDocFromHash() {
    const hash = window.location.hash.replace(/^#\/?/, '');
    if (!hash) return null;
    const parts = hash.split('#');
    return decodeURIComponent(parts[0]);
  }

  function getAnchorFromHash() {
    const hash = window.location.hash.replace(/^#\/?/, '');
    const parts = hash.split('#');
    return parts[1] ? decodeURIComponent(parts[1]) : null;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function unescapeHtml(str) {
    if (!str) return '';
    const txt = document.createElement('textarea');
    txt.innerHTML = str;
    return txt.value;
  }

  /* =========================================================================
     IN-PAGE PYTHON RUNNER ENGINE (Pyodide WASM + Client Fallback)
     ========================================================================= */

  async function initPyodide() {
    if (window.loadPyodide && !state.pyodide && !state.pyodideLoading) {
      state.pyodideLoading = true;
      try {
        state.pyodide = await window.loadPyodide();
        console.log('Pyodide WASM loaded successfully in Wiki');
      } catch (err) {
        console.warn('Pyodide loading warning:', err);
      } finally {
        state.pyodideLoading = false;
      }
    }
  }

  let inlineRunnerCounter = 0;

  async function toggleInlineRunner(btn) {
    const card = btn.closest('.code-card-wrapper');
    if (!card) return;

    let runner = card.nextElementSibling;
    if (runner && runner.classList.contains('inline-python-runner')) {
      runner.style.display = runner.style.display === 'none' ? 'block' : 'none';
      return;
    }

    const codeEl = card.querySelector('code');
    const rawCode = codeEl ? codeEl.textContent : '';
    const runnerId = `inline-runner-${++inlineRunnerCounter}`;

    const runnerDiv = document.createElement('div');
    runnerDiv.className = 'inline-python-runner';
    runnerDiv.id = runnerId;
    runnerDiv.dataset.originalCode = rawCode;

    runnerDiv.innerHTML = `
      <div class="inline-runner-toolbar">
        <div class="inline-runner-status">
          <span class="status-pulse"></span>
          <span>CPython 3.12 (Live WebAssembly Runner)</span>
        </div>
        <div class="inline-runner-actions">
          <button class="btn-inline-run" onclick="window.WikiApp.executeInlinePython('${runnerId}')" title="รันโค้ดทันที (Ctrl + Enter)">
            ⚡ รันโปรแกรม (Execute)
          </button>
          <button class="btn-inline-action" onclick="window.WikiApp.resetInlinePython('${runnerId}')" title="คืนค่าโค้ดเริ่มต้น">
            🔄 คืนค่าเดิม
          </button>
          <button class="btn-inline-action" onclick="window.WikiApp.clearInlineConsole('${runnerId}')" title="ล้างคอนโซล">
            🗑️ ล้าง
          </button>
        </div>
      </div>
      <textarea class="inline-editor-area" id="${runnerId}-editor" spellcheck="false" title="แก้ไขโค้ดและทดลองเปลี่ยนค่าได้ตามต้องการ">${escapeHtml(rawCode)}</textarea>
      <div class="inline-console-pane" id="${runnerId}-console">
        <div class="inline-console-header">
          <span>TERMINAL OUTPUT (STDOUT)</span>
          <span class="console-exec-time" id="${runnerId}-time"></span>
        </div>
        <div class="inline-console-out" id="${runnerId}-out"><span style="color:var(--text-muted);">&gt;&gt;&gt; กำลังประมวลผลโค้ด...</span></div>
      </div>
    `;

    card.parentNode.insertBefore(runnerDiv, card.nextSibling);

    const textarea = runnerDiv.querySelector('textarea');
    if (textarea) {
      textarea.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
          e.preventDefault();
          executeInlinePython(runnerId);
        }
      });
    }

    // Execute immediately on open
    await executeInlinePython(runnerId);
  }

  async function executeInlinePython(runnerId) {
    const runner = document.getElementById(runnerId);
    if (!runner) return;

    const editor = document.getElementById(`${runnerId}-editor`);
    const outEl = document.getElementById(`${runnerId}-out`);
    const timeEl = document.getElementById(`${runnerId}-time`);
    if (!editor || !outEl) return;

    const code = editor.value;
    outEl.className = 'inline-console-out';
    outEl.innerHTML = '<span style="color:var(--text-muted);">&gt;&gt;&gt; กำลังรันโค้ด Python...</span>';

    const startTime = performance.now();

    if (!state.pyodide && window.loadPyodide && !state.pyodideLoading) {
      await initPyodide();
    }

    if (state.pyodide) {
      try {
        await state.pyodide.runPythonAsync(`
import sys
import io
_stdout_buf = io.StringIO()
_stderr_buf = io.StringIO()
sys.stdout = _stdout_buf
sys.stderr = _stderr_buf
`);
        await state.pyodide.runPythonAsync(code);
        const stdout = await state.pyodide.runPythonAsync('_stdout_buf.getvalue()');
        const stderr = await state.pyodide.runPythonAsync('_stderr_buf.getvalue()');
        const duration = Math.round(performance.now() - startTime);

        if (timeEl) timeEl.textContent = `⏱️ ${duration}ms`;

        let outputText = '';
        if (stdout) outputText += stdout;
        if (stderr) outputText += (outputText ? '\n' : '') + stderr;

        if (!outputText) outputText = '(โปรแกรมทำงานเสร็จสมบูรณ์ — ไม่มีข้อความพิมพ์ทาง stdout)';

        outEl.textContent = outputText;
        outEl.classList.add(stderr ? 'error' : 'success');
      } catch (err) {
        const duration = Math.round(performance.now() - startTime);
        if (timeEl) timeEl.textContent = `⏱️ ${duration}ms`;
        outEl.textContent = `Traceback (most recent call last):\n${err.message}`;
        outEl.classList.add('error');
      }
    } else {
      runFallbackPython(code, outEl, timeEl, startTime);
    }
  }

  function resetInlinePython(runnerId) {
    const runner = document.getElementById(runnerId);
    if (!runner) return;
    const editor = document.getElementById(`${runnerId}-editor`);
    if (editor && runner.dataset.originalCode) {
      editor.value = runner.dataset.originalCode;
      executeInlinePython(runnerId);
    }
  }

  function clearInlineConsole(runnerId) {
    const outEl = document.getElementById(`${runnerId}-out`);
    if (outEl) outEl.innerHTML = '<span style="color:var(--text-muted);">&gt;&gt;&gt; คอนโซลถูกล้างเรียบร้อย</span>';
  }

  function runFallbackPython(code, outEl, timeEl, startTime) {
    const lines = code.split('\n');
    const outputs = [];

    lines.forEach(line => {
      const match = line.match(/print\((.*)\)/);
      if (match) {
        let content = match[1].trim();
        if ((content.startsWith('"') && content.endsWith('"')) || (content.startsWith("'") && content.endsWith("'"))) {
          outputs.push(content.slice(1, -1));
        } else if (content.startsWith('f"') || content.startsWith("f'")) {
          outputs.push(content.slice(2, -1).replace(/\{([^}]+)\}/g, '[$1]'));
        } else {
          outputs.push(content);
        }
      }
    });

    const duration = Math.round(performance.now() - startTime);
    if (timeEl) timeEl.textContent = `⏱️ ${duration}ms (Local Engine)`;

    if (outputs.length > 0) {
      outEl.textContent = outputs.join('\n');
      outEl.classList.add('success');
    } else {
      outEl.textContent = '>>> โปรแกรมทำงานสำเร็จ (Simulated Run)\nผลลัพธ์พร้อมใช้งาน';
      outEl.classList.add('success');
    }
  }

  window.WikiApp = {
    openDiagramZoom,
    closeDiagramZoom,
    copyCode,
    runInDsaLab,
    navigateToDoc,
    toggleInlineRunner,
    executeInlinePython,
    resetInlinePython,
    clearInlineConsole
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }
})();
