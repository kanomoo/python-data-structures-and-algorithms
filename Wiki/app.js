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

    if (window.mermaid) {
      try {
        window.mermaid.initialize({
          startOnLoad: false,
          suppressErrorRendering: true,
          theme: state.theme === 'dark' ? 'dark' : 'default',
          securityLevel: 'loose',
          fontFamily: 'Noto Sans Thai, sans-serif'
        });
      } catch (e) {
        console.warn('Mermaid init warning:', e);
      }
    }

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
      elements.breadcrumbCurrent.textContent = formatDocNavTitle(doc.id, doc.title);
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
    if (text.startsWith('---')) {
      const endIdx = text.indexOf('\n---', 3);
      if (endIdx !== -1) return text.slice(endIdx + 4).trim();
    }
    return text;
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
        return `
          <div class="mermaid-card">
            <div class="mermaid-card-header">
              <span class="diagram-label">📊 แผนผัง Mermaid Diagram</span>
              <button class="btn-diagram-zoom" onclick="window.WikiApp.openDiagramZoom(this)" title="ขยายดูภาพเต็ม">
                🔍 ขยายดูภาพเต็ม
              </button>
            </div>
            <div class="mermaid-viewport">
              <div class="mermaid-code-raw" style="display:none;">${escapeHtml(decodedCode)}</div>
              <div class="mermaid-render-target"></div>
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

  async function renderMermaidDiagrams() {
    if (!window.mermaid) return;
    document.querySelectorAll('div[id^="dmermaid-"], svg[id^="dmermaid-"]').forEach(el => el.remove());

    const containers = elements.articleBody.querySelectorAll('.mermaid-card');
    for (let idx = 0; idx < containers.length; idx++) {
      const card = containers[idx];
      const rawCodeEl = card.querySelector('.mermaid-code-raw');
      const targetEl = card.querySelector('.mermaid-render-target');
      if (!rawCodeEl || !targetEl) continue;

      const code = rawCodeEl.textContent.trim();
      const uniqueId = `mermaid-svg-${Date.now()}-${idx}`;

      try {
        await window.mermaid.parse(code);
        let result = await window.mermaid.render(uniqueId, code, targetEl);
        targetEl.innerHTML = result.svg;
      } catch (err) {
        document.querySelectorAll(`div[id^="d${uniqueId}"], div[id^="dmermaid-"]`).forEach(el => el.remove());
        targetEl.innerHTML = `
          <div style="color: #f87171; font-size: 13px; padding: 10px; border: 1px dashed rgba(239,68,68,0.3); border-radius: 6px;">
            ⚠️ ไม่สามารถแสดงผลไดอะแกรมอัตโนมัติได้ (${escapeHtml(err.message || String(err))})
          </div>
        `;
      }
    }
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
    const card = btn.closest('.mermaid-card');
    if (!card) return;
    const svgEl = card.querySelector('svg');
    if (!svgEl) return;
    elements.diagramCanvas.innerHTML = svgEl.outerHTML;
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
