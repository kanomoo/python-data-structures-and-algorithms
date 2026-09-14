/**
 * DSA LAB STUDIO — INTERACTIVE VISUAL DEBUGGER ENGINE
 * High-precision algorithm tracing, interactive tree/array rendering,
 * and step-by-step debugger widgets for all core data structures.
 */

/* ================================================================
   1. UTILITIES & REUSABLE DEBUGGER WIDGET FACTORY
================================================================ */

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function buildDebuggerWidget(container, opts) {
  if (!container) return null;

  const id = opts.id;
  container.innerHTML = `
    <!-- TOP CONTROLS TOOLBAR: ANCHORED, STICKY & ZERO LAYOUT SHIFT -->
    <div class="debugger-head-toolbar">
      <div class="controls controls-top">
        <button class="ctrl-btn" id="${id}_resetBtn" title="เริ่มใหม่ (R)">⟲ Reset</button>
        ${opts.showJump ? `<button class="ctrl-btn ghost" id="${id}_prevJump" title="ข้ามไปตัวก่อนหน้า">⏮ ตัวก่อนหน้า</button>` : ''}
        <button class="ctrl-btn" id="${id}_prevBtn" title="ย้อนกลับ 1 ขั้น (←)">◀ Prev</button>
        <button class="ctrl-btn primary btn-next-prominent" id="${id}_nextBtn" title="ก้าวถัดไป 1 ขั้น (Space หรือ →)">Next ▶</button>
        ${opts.showJump ? `<button class="ctrl-btn ghost" id="${id}_nextJump" title="ข้ามไปตัวถัดไป">ตัวถัดไป ⏭</button>` : ''}
        <button class="ctrl-btn" id="${id}_playBtn">▶ Auto Play</button>
        <span class="step-counter" id="${id}_stepCounter">Step 0 / 0</span>
        <span class="kbd-hint-pill mono">คีย์ลัด: <kbd>Space</kbd> หรือ <kbd>→</kbd></span>
      </div>
      <div class="progress-track" style="margin-top:10px; margin-bottom:0;">
        <div class="progress-fill" id="${id}_progressFill" style="width:0%"></div>
      </div>
    </div>

    <div class="dbg-grid">
      <div>
        <div class="panel-box tree-panel-box">
          <div class="panel-title">
            <span>${opts.treeTitle || 'Tree View'}</span>
            <span id="${id}_sizeTag" class="mono tag-accent">currentSize = 0</span>
          </div>
          <svg class="tree" id="${id}_treeSvg" viewBox="0 0 760 400" xmlns="http://www.w3.org/2000/svg"></svg>
        </div>
        <div class="panel-box array-panel-box" style="margin-top:14px;">
          <div class="panel-title">
            <span>${opts.arrayTitle || 'Array View'}</span>
            <span class="mono">${opts.arraySubtitle || 'index 0 ไม่ใช้งาน'}</span>
          </div>
          <div class="array-row" id="${id}_arrayRow"></div>
          <div class="legend" id="${id}_legend">
            <span><i class="hole"></i> hole (ตำแหน่งว่าง)</span>
            <span><i class="compare"></i> กำลังเปรียบเทียบ</span>
            <span><i class="moved"></i> เพิ่งย้ายค่า</span>
            <span><i class="final"></i> ค่าสุดท้ายที่วาง</span>
          </div>
        </div>
      </div>
      <div>
        <div class="panel-box code-panel-box">
          <div class="panel-title">
            <span>Source Code</span>
            <span class="mono tag-accent">python</span>
          </div>
          <div class="code-block" id="${id}_codeBlock"></div>
        </div>
        <div class="panel-box watch-panel-box" style="margin-top:14px;">
          <div class="panel-title">Watch Variables</div>
          <div class="watch-list" id="${id}_watchList"></div>
        </div>
        <div class="badge-slot-fixed" id="${id}_badgeSlot"></div>
        <div class="narration-fixed" id="${id}_narration">กด "Next ▶" เพื่อเริ่มไล่โค้ดทีละบรรทัด</div>
      </div>
    </div>

    <!-- BOTTOM CONTROLS (MIRRORED & ROCK SOLID AT CONSTANT POSITION) -->
    <div class="controls controls-bottom" style="margin-top: 18px; margin-bottom: 8px;">
      <button class="ctrl-btn" id="${id}_resetBtn_b" title="เริ่มใหม่ (R)">⟲ Reset</button>
      ${opts.showJump ? `<button class="ctrl-btn ghost" id="${id}_prevJump_b" title="ข้ามไปตัวก่อนหน้า">⏮ ตัวก่อนหน้า</button>` : ''}
      <button class="ctrl-btn" id="${id}_prevBtn_b" title="ย้อนกลับ 1 ขั้น (←)">◀ Prev</button>
      <button class="ctrl-btn primary btn-next-prominent" id="${id}_nextBtn_b" title="ก้าวถัดไป 1 ขั้น (Space หรือ →)">Next ▶</button>
      ${opts.showJump ? `<button class="ctrl-btn ghost" id="${id}_nextJump_b" title="ข้ามไปตัวถัดไป">ตัวถัดไป ⏭</button>` : ''}
      <button class="ctrl-btn" id="${id}_playBtn_b">▶ Auto Play</button>
      <span class="step-counter" id="${id}_stepCounter_b">Step 0 / 0</span>
    </div>

    <div class="console">
      <div class="console-title">Debug Console</div>
      <div id="${id}_consoleLog"></div>
    </div>
  `;

  const st = {
    mode: opts.defaultMode || 'default',
    trace: [],
    markers: [0],
    idx: 0,
    playing: false,
    timer: null
  };

  function renderTree(step) {
    const svg = document.getElementById(`${id}_treeSvg`);
    if (!svg) return;

    if (opts.customRenderTree) {
      opts.customRenderTree(svg, step, id);
      return;
    }

    const size = step.currentSize || (step.array ? step.array.length - 1 : 0);
    const values = step.array || [];
    const highlightMap = {};
    (step.highlights || []).forEach(h => {
      if (h.index != null) highlightMap[h.index] = h.type;
    });

    const W = 760, marginX = 40;
    const nodes = [];
    for (let i = 1; i <= size; i++) {
      const depth = Math.floor(Math.log2(i));
      const levelStart = Math.pow(2, depth);
      const posInLevel = i - levelStart;
      const x = marginX + (posInLevel + 0.5) * (W - 2 * marginX) / levelStart;
      const y = 46 + depth * 95;
      nodes.push({ i, x, y, val: values[i] });
    }

    let edges = '';
    nodes.forEach(n => {
      const p = Math.floor(n.i / 2);
      if (p >= 1) {
        const pn = nodes.find(nn => nn.i === p);
        if (pn) edges += `<line class="edge" x1="${pn.x}" y1="${pn.y}" x2="${n.x}" y2="${n.y}"/>`;
      }
    });

    let circles = '';
    nodes.forEach(n => {
      const type = highlightMap[n.i];
      let stroke = '#3a3d4b', fill = '#20222c', dash = '';
      if (type === 'hole') { stroke = 'var(--amber)'; fill = 'rgba(245,166,35,0.12)'; dash = '6,4'; }
      else if (type === 'compare') { stroke = 'var(--cyan)'; fill = 'rgba(79,209,232,0.12)'; }
      else if (type === 'compare2') { stroke = 'var(--cyan)'; fill = 'rgba(79,209,232,0.05)'; dash = '3,3'; }
      else if (type === 'moved') { stroke = 'var(--green)'; fill = 'rgba(74,222,128,0.14)'; }
      else if (type === 'final') { stroke = 'var(--violet)'; fill = 'rgba(183,148,246,0.18)'; }

      const label = (n.val === null || n.val === undefined) ? '∅' : n.val;
      circles += `<g>
        <circle cx="${n.x}" cy="${n.y}" r="22" fill="${fill}" stroke="${stroke}" stroke-width="2" stroke-dasharray="${dash}"/>
        <text class="node-text" x="${n.x}" y="${n.y + 1}">${label}</text>
        <text class="node-idx" x="${n.x}" y="${n.y - 30}">[${n.i}]</text>
      </g>`;
    });

    svg.innerHTML = edges + circles;
    const tag = document.getElementById(`${id}_sizeTag`);
    if (tag) tag.textContent = `currentSize = ${size}`;
  }

  function renderArray(step) {
    const row = document.getElementById(`${id}_arrayRow`);
    if (!row) return;

    if (opts.customRenderArray) {
      opts.customRenderArray(row, step, id);
      return;
    }

    const highlightMap = {};
    (step.highlights || []).forEach(h => {
      if (h.index != null) highlightMap[h.index] = h.type;
    });

    const maxIdx = Math.max((step.array ? step.array.length - 1 : 0), step.currentSize || 0);
    let html = '';
    for (let i = 0; i <= maxIdx; i++) {
      if (i === 0) {
        html += `<div class="abox dead"><span class="aidx">0</span>·</div>`;
        continue;
      }
      const val = step.array ? step.array[i] : null;
      const type = highlightMap[i];
      let cls = 'abox';
      if (i > (step.currentSize || 0)) cls += ' dead';
      if (type) cls += ' ' + type;
      const label = (val === null || val === undefined) ? (i <= step.currentSize ? '∅' : '') : val;
      html += `<div class="${cls}"><span class="aidx">${i}</span>${label}</div>`;
    }
    row.innerHTML = html;
  }

  function renderCode(step) {
    const code = opts.getCode ? opts.getCode(st.mode) : [];
    const box = document.getElementById(`${id}_codeBlock`);
    if (!box) return;

    let html = '';
    code.forEach((line, i) => {
      const lineNo = i + 1;
      const active = lineNo === step.line;
      html += `<div class="code-line${active ? ' active' : ''}"><span class="ln">${lineNo}</span><span>${escapeHtml(line)}</span></div>`;
    });
    box.innerHTML = html;
    const activeEl = box.querySelector('.active');
    if (activeEl) {
      box.scrollTop = activeEl.offsetTop - (box.clientHeight / 2) + (activeEl.clientHeight / 2);
    }
  }

  function renderWatch(step) {
    const list = document.getElementById(`${id}_watchList`);
    if (!list) return;

    const entries = Object.entries(step.watch || {});
    if (entries.length === 0) {
      list.innerHTML = `<div class="watch-item"><span class="k">—</span><span class="v">ยังไม่มีตัวแปร</span></div>`;
      return;
    }
    list.innerHTML = entries.map(([k, v]) =>
      `<div class="watch-item"><span class="k">${escapeHtml(k)}</span><span class="v">${escapeHtml(v)}</span></div>`
    ).join('');
  }

  function renderBadge(step) {
    const slot = document.getElementById(`${id}_badgeSlot`);
    if (!slot) return;
    if (step.meta) {
      slot.innerHTML = `<div class="insert-badge">🔧 กำลังดำเนินการ: ${escapeHtml(step.meta.label || `ตัวที่ ${step.meta.num || ''} : ค่า ${step.meta.value || ''}`)}</div>`;
    } else {
      slot.innerHTML = `<div class="insert-badge insert-badge-placeholder"><span>⚡ พร้อมดำเนินการสเต็ปถัดไป</span></div>`;
    }
  }

  function renderConsole() {
    const log = document.getElementById(`${id}_consoleLog`);
    if (!log) return;

    let html = '';
    st.trace.forEach((s, i) => {
      if (i > st.idx) return;
      const cur = i === st.idx ? ' current' : '';
      const mk = s.boundary ? ' marker' : '';
      html += `<div class="console-line${cur}${mk}"><b>[step ${i}]</b> ${escapeHtml(s.note)}</div>`;
    });
    log.innerHTML = html;
    log.scrollTop = log.scrollHeight;
  }

  function render() {
    if (!st.trace || st.trace.length === 0) return;
    const step = st.trace[st.idx] || st.trace[0];
    renderTree(step);
    renderArray(step);
    renderCode(step);
    renderWatch(step);
    renderBadge(step);

    const nar = document.getElementById(`${id}_narration`);
    if (nar) nar.textContent = step.note || '';

    const counterText = `Step ${st.idx} / ${Math.max(0, st.trace.length - 1)}`;
    const counter = document.getElementById(`${id}_stepCounter`);
    if (counter) counter.textContent = counterText;
    const counterB = document.getElementById(`${id}_stepCounter_b`);
    if (counterB) counterB.textContent = counterText;

    const fill = document.getElementById(`${id}_progressFill`);
    if (fill) {
      const pct = st.trace.length > 1 ? (st.idx / (st.trace.length - 1)) * 100 : 0;
      fill.style.width = `${pct}%`;
    }

    const isFirst = st.idx === 0;
    const isLast = st.idx >= st.trace.length - 1;

    ['prevBtn', 'prevBtn_b'].forEach(bid => {
      const b = document.getElementById(`${id}_${bid}`);
      if (b) b.disabled = isFirst;
    });

    ['nextBtn', 'nextBtn_b'].forEach(bid => {
      const b = document.getElementById(`${id}_${bid}`);
      if (b) b.disabled = isLast;
    });

    renderConsole();
  }

  function stopPlay() {
    st.playing = false;
    clearInterval(st.timer);
    ['playBtn', 'playBtn_b'].forEach(bid => {
      const btn = document.getElementById(`${id}_${bid}`);
      if (btn) btn.textContent = '▶ Auto Play';
    });
  }

  function setMode(mode) {
    st.mode = mode;
    const res = opts.buildTrace(mode);
    if (Array.isArray(res)) {
      st.trace = res;
      st.markers = [0];
    } else if (res && res.trace) {
      st.trace = res.trace;
      st.markers = res.markers && res.markers.length ? res.markers : [0];
    }
    st.idx = 0;
    stopPlay();
    render();
  }

  function handleNext() {
    if (st.idx < st.trace.length - 1) {
      st.idx++;
      render();
    }
    if (st.idx === st.trace.length - 1) stopPlay();
  }

  function handlePrev() {
    if (st.idx > 0) {
      st.idx--;
      render();
    }
  }

  function handleReset() {
    st.idx = 0;
    stopPlay();
    render();
  }

  function handlePlay() {
    if (st.playing) {
      stopPlay();
      return;
    }
    st.playing = true;
    ['playBtn', 'playBtn_b'].forEach(bid => {
      const btn = document.getElementById(`${id}_${bid}`);
      if (btn) btn.textContent = '⏸ Pause';
    });
    st.timer = setInterval(() => {
      if (st.idx < st.trace.length - 1) {
        st.idx++;
        render();
      } else {
        stopPlay();
      }
    }, 1200);
  }

  function handleNextJump() {
    const nxt = st.markers.find(m => m > st.idx);
    st.idx = nxt !== undefined ? nxt : st.trace.length - 1;
    stopPlay();
    render();
  }

  function handlePrevJump() {
    const past = st.markers.filter(m => m < st.idx);
    st.idx = past.length ? past[past.length - 1] : 0;
    stopPlay();
    render();
  }

  // Bind Buttons (Both Top and Bottom)
  ['nextBtn', 'nextBtn_b'].forEach(bid => {
    const btn = document.getElementById(`${id}_${bid}`);
    if (btn) btn.addEventListener('click', handleNext);
  });

  ['prevBtn', 'prevBtn_b'].forEach(bid => {
    const btn = document.getElementById(`${id}_${bid}`);
    if (btn) btn.addEventListener('click', handlePrev);
  });

  ['resetBtn', 'resetBtn_b'].forEach(bid => {
    const btn = document.getElementById(`${id}_${bid}`);
    if (btn) btn.addEventListener('click', handleReset);
  });

  ['playBtn', 'playBtn_b'].forEach(bid => {
    const btn = document.getElementById(`${id}_${bid}`);
    if (btn) btn.addEventListener('click', handlePlay);
  });

  if (opts.showJump) {
    ['nextJump', 'nextJump_b'].forEach(bid => {
      const btn = document.getElementById(`${id}_${bid}`);
      if (btn) btn.addEventListener('click', handleNextJump);
    });
    ['prevJump', 'prevJump_b'].forEach(bid => {
      const btn = document.getElementById(`${id}_${bid}`);
      if (btn) btn.addEventListener('click', handlePrevJump);
    });
  }

  return { setMode, render, getTrace: () => st.trace };
}


/* ================================================================
   2. BINARY HEAP ALGORITHM SIMULATION & TRACE GENERATION
================================================================ */

const HEAP_INSERT_CODE = [
  "def insert(self, x):",
  "    if self.is_full():",
  "        return",
  "    self.currentSize += 1",
  "    hole = self.currentSize",
  "    while hole > 1 and x < self.array[hole // 2]:",
  "        self.array[hole] = self.array[hole // 2]",
  "        hole //= 2",
  "    self.array[hole] = x"
];

const HEAP_DELETE_CODE = [
  "def delete_min(self):",
  "    min_item = self.array[1]",
  "    self.array[1] = self.array[self.currentSize]",
  "    self.currentSize -= 1",
  "    self._percolate_down(1)",
  "    return min_item",
  "",
  "def _percolate_down(self, hole):",
  "    temp = self.array[hole]",
  "    while hole * 2 <= self.currentSize:",
  "        child = hole * 2",
  "        if child != self.currentSize and self.array[child+1] < self.array[child]:",
  "            child += 1",
  "        if self.array[child] < temp:",
  "            self.array[hole] = self.array[child]",
  "        else:",
  "            break",
  "        hole = child",
  "    self.array[hole] = temp"
];

function insertOnce(array, currentSize, x, meta) {
  array = array.slice();
  const trace = [];

  function snap(line, note, highlights, watch, boundary) {
    trace.push({
      line,
      note,
      watch: Object.assign({}, watch),
      array: array.slice(),
      currentSize,
      highlights: highlights || [],
      meta: meta || null,
      boundary: !!boundary
    });
  }

  snap(2, `ตรวจสอบ is_full() → heap ยังไม่เต็ม ข้ามเงื่อนไขนี้ไป`, [], { x }, true);

  currentSize += 1;
  while (array.length <= currentSize) array.push(null);
  snap(4, `currentSize += 1  →  currentSize = ${currentSize}`, [], { x, currentSize });

  let hole = currentSize;
  array[hole] = null;
  snap(5, `hole = currentSize = ${hole}  (สร้างช่องว่างที่ตำแหน่งสุดท้ายของ array)`, [{ index: hole, type: 'hole' }], { x, currentSize, hole });

  while (true) {
    const condA = hole > 1;
    snap(6, `ตรวจ while: hole > 1  →  ${hole} > 1  =  ${condA}`, [{ index: hole, type: 'hole' }], { x, currentSize, hole });
    if (!condA) break;

    const parent = Math.floor(hole / 2);
    const condB = x < array[parent];
    snap(6, `เปรียบเทียบ x < array[hole // 2]  →  ${x} < array[${parent}] (${array[parent]})  =  ${condB}`,
      [{ index: hole, type: 'hole' }, { index: parent, type: 'compare' }],
      { x, currentSize, hole, "parent(hole//2)": parent });

    if (!condB) break;

    array[hole] = array[parent];
    snap(7, `array[hole] = array[hole // 2]  →  ย้ายค่า ${array[parent]} จากตำแหน่ง ${parent} มาไว้ที่ ${hole}`,
      [{ index: hole, type: 'moved' }, { index: parent, type: 'compare' }],
      { x, currentSize, hole, "parent(hole//2)": parent });

    array[parent] = null;
    hole = parent;
    snap(8, `hole //= 2  →  hole = ${hole}  (ช่องว่างขยับขึ้นไปแทนตำแหน่งพ่อ)`, [{ index: hole, type: 'hole' }], { x, currentSize, hole });
  }

  array[hole] = x;
  snap(9, `array[hole] = x  →  ใส่ค่า ${x} ที่ตำแหน่ง ${hole}  ✔ จบการ insert ค่านี้`, [{ index: hole, type: 'final' }], { x, currentSize, hole });

  return { trace, array, currentSize };
}

function traceBuildFromScratch(values) {
  let array = [null];
  let currentSize = 0;
  let full = [];
  const markers = [];

  full.push({
    line: 1,
    note: `เริ่มต้น: heap ว่างเปล่า (currentSize = 0) — เตรียม insert ทั้งหมด ${values.length} ค่า`,
    watch: {},
    array: array.slice(),
    currentSize: 0,
    highlights: [],
    meta: null,
    boundary: true
  });

  values.forEach((v, i) => {
    markers.push(full.length);
    const res = insertOnce(array, currentSize, v, { num: i + 1, total: values.length, value: v });
    res.trace[0].boundary = true;
    full = full.concat(res.trace);
    array = res.array;
    currentSize = res.currentSize;
  });

  return { trace: full, markers };
}

function traceInsertSingle(initArray, initSize, x) {
  const res = insertOnce(initArray, initSize, x, { label: `insert(${x}) เดี่ยว` });
  return res.trace;
}

function traceDeleteMin(initArray, initSize) {
  const trace = [];
  let array = initArray.slice();
  let currentSize = initSize;

  function snap(line, note, highlights, watch) {
    trace.push({
      line,
      note,
      watch: Object.assign({}, watch),
      array: array.slice(),
      currentSize,
      highlights: highlights || []
    });
  }

  const min_item = array[1];
  snap(2, `min_item = array[1]  →  min_item = ${min_item}`, [{ index: 1, type: 'final' }], { min_item });

  array[1] = array[currentSize];
  snap(3, `array[1] = array[currentSize]  →  นำค่า ${array[1]} (จากตำแหน่งสุดท้าย ${currentSize}) มาไว้ที่ root`, [{ index: 1, type: 'hole' }], { min_item });

  currentSize -= 1;
  snap(4, `currentSize -= 1  →  currentSize = ${currentSize}`, [{ index: 1, type: 'hole' }], { min_item, currentSize });

  snap(5, `เรียก self._percolate_down(1)  →  เริ่มต้นดันค่าลงไปจัดระเบียบ Heap`, [{ index: 1, type: 'hole' }], { min_item, currentSize });

  let hole = 1;
  let temp = array[hole];
  snap(9, `temp = array[hole]  →  temp = ${temp}`, [{ index: hole, type: 'hole' }], { min_item, currentSize, hole, temp });

  while (true) {
    const condA = hole * 2 <= currentSize;
    snap(10, `ตรวจ while: hole*2 <= currentSize  →  ${hole * 2} <= ${currentSize}  =  ${condA}`, [{ index: hole, type: 'hole' }], { min_item, currentSize, hole, temp });
    if (!condA) break;

    let child = hole * 2;
    snap(11, `child = hole*2  →  child = ${child}  (ลูกซ้าย)`, [{ index: hole, type: 'hole' }, { index: child, type: 'compare' }], { min_item, currentSize, hole, child, temp });

    const rightExists = (child + 1) <= currentSize;
    const condC = rightExists && (child !== currentSize) && (array[child + 1] < array[child]);
    snap(12, `เช็คลูกขวา: child != currentSize (${child}!=${currentSize}) และ array[${child + 1}]=${rightExists ? array[child + 1] : '—'} < array[${child}]=${array[child]}  →  ${condC}`,
      [{ index: hole, type: 'hole' }, { index: child, type: 'compare' }, { index: rightExists ? child + 1 : null, type: 'compare2' }],
      { min_item, currentSize, hole, child, temp });

    if (condC) {
      child += 1;
      snap(13, `child += 1  →  child = ${child}  (ลูกขวาน้อยกว่า จึงเลือกลูกขวาเพื่อเทียบ)`, [{ index: hole, type: 'hole' }, { index: child, type: 'compare' }], { min_item, currentSize, hole, child, temp });
    }

    const condD = array[child] < temp;
    snap(14, `ตรวจ: array[child]=${array[child]} < temp=${temp}  →  ${condD}`, [{ index: hole, type: 'hole' }, { index: child, type: 'compare' }], { min_item, currentSize, hole, child, temp });

    if (condD) {
      array[hole] = array[child];
      snap(15, `array[hole] = array[child]  →  ย้าย ${array[child]} ขึ้นไปที่ตำแหน่ง ${hole}`, [{ index: hole, type: 'moved' }, { index: child, type: 'compare' }], { min_item, currentSize, hole, child, temp });

      array[child] = null;
      hole = child;
      snap(18, `hole = child  →  hole = ${hole}  (ช่องว่างขยับลงมาแทนตำแหน่งลูก)`, [{ index: hole, type: 'hole' }], { min_item, currentSize, hole, temp });
    } else {
      snap(17, `array[child] (${array[child]}) ไม่น้อยกว่า temp (${temp})  →  break ออกจาก while loop`, [{ index: hole, type: 'hole' }, { index: child, type: 'compare' }], { min_item, currentSize, hole, child, temp });
      break;
    }
  }

  array[hole] = temp;
  snap(19, `array[hole] = temp  →  ใส่ค่า ${temp} กลับที่ตำแหน่ง ${hole}  ✔ จบ _percolate_down()`, [{ index: hole, type: 'final' }], { min_item, currentSize, hole, temp });
  snap(6, `return min_item  →  คืนค่า ${min_item} เป็นผลลัพธ์ของ deleteMin() สมบูรณ์!`, [], { min_item, currentSize });

  return trace;
}


/* ================================================================
   3. BINARY SEARCH TREE (BST) ALGORITHM SIMULATION
================================================================ */

const BST_CODE = [
  "def insert(self, root, val):",
  "    if not root: return TreeNode(val)",
  "    if val < root.val:",
  "        root.left = self.insert(root.left, val)",
  "    elif val > root.val:",
  "        root.right = self.insert(root.right, val)",
  "    return root",
  "",
  "def delete(self, root, key):",
  "    if not root: return None",
  "    if key < root.val:",
  "        root.left = self.delete(root.left, key)",
  "    elif key > root.val:",
  "        root.right = self.delete(root.right, key)",
  "    else: # Found key",
  "        if not root.left: return root.right # Case 1 & 2",
  "        if not root.right: return root.left",
  "        # Case 3: 2 children -> Find In-order Successor",
  "        succ = self.find_min(root.right)",
  "        root.val = succ.val",
  "        root.right = self.delete(root.right, succ.val)",
  "    return root"
];

function traceBstBuild(values) {
  const trace = [];
  let treeState = null;

  trace.push({
    line: 1,
    note: `เริ่มต้น: ต้นไม้ BST ว่างเปล่า (Empty Tree) — เตรียม insert ทั้งหมด ${values.length} ค่า`,
    watch: {},
    bstNodes: [],
    boundary: true
  });

  function cloneTree(n) {
    if (!n) return null;
    return { val: n.val, left: cloneTree(n.left), right: cloneTree(n.right) };
  }

  function insertNode(root, val, markers) {
    if (!root) {
      trace.push({
        line: 2,
        note: `if not root  →  สร้างโหนดใหม่ TreeNode(${val}) วางที่ตำแหน่งนี้`,
        watch: { val },
        bstNodes: getBstNodeList(treeState, [{ val, type: 'final' }])
      });
      return { val, left: null, right: null };
    }

    trace.push({
      line: 3,
      note: `เปรียบเทียบค่า ${val} กับโหนดปัจจุบัน ${root.val}`,
      watch: { val, "root.val": root.val },
      bstNodes: getBstNodeList(treeState, [{ val: root.val, type: 'compare' }])
    });

    if (val < root.val) {
      trace.push({
        line: 4,
        note: `${val} < ${root.val}  →  เลี้ยวซ้ายไปยัง root.left`,
        watch: { val, "root.val": root.val, dir: 'left' },
        bstNodes: getBstNodeList(treeState, [{ val: root.val, type: 'moved' }])
      });
      root.left = insertNode(root.left, val, markers);
    } else if (val > root.val) {
      trace.push({
        line: 6,
        note: `${val} > ${root.val}  →  เลี้ยวขวาไปยัง root.right`,
        watch: { val, "root.val": root.val, dir: 'right' },
        bstNodes: getBstNodeList(treeState, [{ val: root.val, type: 'moved' }])
      });
      root.right = insertNode(root.right, val, markers);
    }
    return root;
  }

  values.forEach((v, i) => {
    trace.push({
      line: 1,
      note: `[แทรกตัวที่ ${i + 1}/${values.length}] เตรียมแทรกค่า ${v} ลงใน BST`,
      watch: { val: v },
      bstNodes: getBstNodeList(treeState),
      meta: { num: i + 1, total: values.length, value: v },
      boundary: true
    });
    treeState = insertNode(treeState, v);
  });

  return { trace, markers: [0, 4, 9, 15, 22, 28, 35] };
}

function getBstNodeList(root, highlights = []) {
  if (!root) return [];
  const nodes = [];
  const hlMap = {};
  highlights.forEach(h => hlMap[h.val] = h.type);

  function traverse(node, depth, pos, parentX, parentY) {
    if (!node) return;
    const W = 760;
    const levelWidth = W / Math.pow(2, depth);
    const x = pos * levelWidth + levelWidth / 2;
    const y = 46 + depth * 80;

    nodes.push({
      val: node.val,
      x,
      y,
      parentX,
      parentY,
      type: hlMap[node.val] || null
    });

    traverse(node.left, depth + 1, pos * 2, x, y);
    traverse(node.right, depth + 1, pos * 2 + 1, x, y);
  }

  traverse(root, 0, 0, null, null);
  return nodes;
}

function renderBstSvg(svg, step, id) {
  const nodes = step.bstNodes || [];
  let edges = '';
  let circles = '';

  nodes.forEach(n => {
    if (n.parentX != null && n.parentY != null) {
      edges += `<line class="edge" x1="${n.parentX}" y1="${n.parentY}" x2="${n.x}" y2="${n.y}"/>`;
    }
  });

  nodes.forEach(n => {
    let stroke = '#3a3d4b', fill = '#20222c', dash = '';
    if (n.type === 'compare') { stroke = 'var(--cyan)'; fill = 'rgba(79,209,232,0.14)'; }
    else if (n.type === 'moved') { stroke = 'var(--amber)'; fill = 'rgba(245,166,35,0.12)'; }
    else if (n.type === 'final') { stroke = 'var(--green)'; fill = 'rgba(74,222,128,0.18)'; }
    else if (n.type === 'hole') { stroke = 'var(--rose)'; fill = 'rgba(255,107,129,0.15)'; dash = '4,4'; }

    circles += `<g>
      <circle cx="${n.x}" cy="${n.y}" r="20" fill="${fill}" stroke="${stroke}" stroke-width="2" stroke-dasharray="${dash}"/>
      <text class="node-text" x="${n.x}" y="${n.y + 1}">${n.val}</text>
    </g>`;
  });

  svg.innerHTML = edges + circles;
  const tag = document.getElementById(`${id}_sizeTag`);
  if (tag) tag.textContent = `Nodes = ${nodes.length}`;
}

function renderBstInorderArray(row, step) {
  const nodes = (step.bstNodes || []).slice().sort((a, b) => a.val - b.val);
  let html = `<div class="abox dead"><span class="aidx">In-order</span>·</div>`;
  nodes.forEach((n, i) => {
    let cls = 'abox';
    if (n.type) cls += ' ' + n.type;
    html += `<div class="${cls}"><span class="aidx">${i + 1}</span>${n.val}</div>`;
  });
  row.innerHTML = html;
}

function traceBstOperations(mode) {
  // Demo cases: insert(18), search(30), del1: delete(10)[leaf], del2: delete(35)[1 child], del3: delete(25)[2 children]
  const baseTree = {
    val: 25,
    left: { val: 15, left: { val: 10, left: null, right: null }, right: { val: 20, left: null, right: null } },
    right: { val: 35, left: { val: 30, left: null, right: null }, right: { val: 40, left: null, right: null } }
  };

  const trace = [];

  if (mode === 'insert') {
    trace.push({ line: 1, note: `เรียก insert(root, 18) เริ่มเปรียบเทียบที่ Root (25)`, watch: { val: 18 }, bstNodes: getBstNodeList(baseTree, [{ val: 25, type: 'compare' }]) });
    trace.push({ line: 3, note: `18 < 25  →  เดินไปกิ่งซ้าย (15)`, watch: { val: 18, "root.val": 25 }, bstNodes: getBstNodeList(baseTree, [{ val: 15, type: 'compare' }]) });
    trace.push({ line: 5, note: `18 > 15  →  เดินไปกิ่งขวา (20)`, watch: { val: 18, "root.val": 15 }, bstNodes: getBstNodeList(baseTree, [{ val: 20, type: 'compare' }]) });
    trace.push({ line: 3, note: `18 < 20  →  กิ่งซ้ายของ 20 ว่าง (None)  →  สร้างโหนด 18 แทรกเป็นลูกซ้ายของ 20`, watch: { val: 18, "root.val": 20 }, bstNodes: getBstNodeList({
      val: 25,
      left: { val: 15, left: { val: 10, left: null, right: null }, right: { val: 20, left: { val: 18, left: null, right: null }, right: null } },
      right: { val: 35, left: { val: 30, left: null, right: null }, right: { val: 40, left: null, right: null } }
    }, [{ val: 18, type: 'final' }]) });
  } else if (mode === 'search') {
    trace.push({ line: 1, note: `เรียก search(root, 30)  →  เปรียบเทียบกับ Root (25)`, watch: { key: 30, "root.val": 25 }, bstNodes: getBstNodeList(baseTree, [{ val: 25, type: 'compare' }]) });
    trace.push({ line: 5, note: `30 > 25  →  เลี้ยวขวาไปยังโหนด (35)`, watch: { key: 30, "root.val": 35 }, bstNodes: getBstNodeList(baseTree, [{ val: 35, type: 'compare' }]) });
    trace.push({ line: 3, note: `30 < 35  →  เลี้ยวซ้ายไปยังโหนด (30)`, watch: { key: 30, "root.val": 30 }, bstNodes: getBstNodeList(baseTree, [{ val: 30, type: 'final' }]) });
    trace.push({ line: 6, note: `พบโหนด 30 ตรงตามที่ค้นหา! Return Node(30) สำเร็จใน 3 สเต็ป`, watch: { key: 30, result: 'Found' }, bstNodes: getBstNodeList(baseTree, [{ val: 30, type: 'final' }]) });
  } else if (mode === 'del1') {
    // delete leaf 10
    trace.push({ line: 9, note: `เรียก delete(root, 10): ค้นหา 10 จาก Root (25) → เดินซ้ายไป 15 → ซ้ายไป 10`, watch: { key: 10 }, bstNodes: getBstNodeList(baseTree, [{ val: 10, type: 'compare' }]) });
    trace.push({ line: 15, note: `พบโหนด 10 ซึ่งไม่มีลูกทั้งซ้ายและขวา (Leaf Node) → ปลดตัวชี้จาก 15 กลายเป็น None`, watch: { key: 10, case: 'Case 1: Leaf' }, bstNodes: getBstNodeList(baseTree, [{ val: 10, type: 'hole' }]) });
    trace.push({ line: 16, note: `ลบโหนด 10 สำเร็จ Tree ยังคงคุณสมบัติ BST สมบูรณ์`, watch: { key: 10 }, bstNodes: getBstNodeList({
      val: 25,
      left: { val: 15, left: null, right: { val: 20, left: null, right: null } },
      right: { val: 35, left: { val: 30, left: null, right: null }, right: { val: 40, left: null, right: null } }
    }) });
  } else if (mode === 'del2') {
    // delete 35 where we pretend it only has 1 child
    const oneChildTree = {
      val: 25,
      left: { val: 15, left: { val: 10, left: null, right: null }, right: null },
      right: { val: 35, left: null, right: { val: 40, left: null, right: null } }
    };
    trace.push({ line: 9, note: `เรียก delete(root, 35): เดินขวาจาก 25 พบโหนด 35`, watch: { key: 35 }, bstNodes: getBstNodeList(oneChildTree, [{ val: 35, type: 'compare' }]) });
    trace.push({ line: 16, note: `โหนด 35 มีลูกเพียงข้างเดียว (ลูกขวา 40) → Case 2: ดึงลูก 40 ขึ้นมาต่อกับ 25 โดยตรง`, watch: { key: 35, case: 'Case 2: 1 Child' }, bstNodes: getBstNodeList(oneChildTree, [{ val: 35, type: 'hole' }, { val: 40, type: 'moved' }]) });
    trace.push({ line: 17, note: `ลบ 35 สำเร็จ โหนด 40 เข้ามาแทนที่ตำแหน่งเดิมอย่างถูกต้อง`, watch: { key: 35 }, bstNodes: getBstNodeList({
      val: 25,
      left: { val: 15, left: { val: 10, left: null, right: null }, right: null },
      right: { val: 40, left: null, right: null }
    }) });
  } else if (mode === 'del3') {
    // delete root 25 (2 children)
    trace.push({ line: 9, note: `เรียก delete(root, 25): โหนด 25 มีลูกครบทั้ง 2 ข้าง (Case 3)`, watch: { key: 25, case: 'Case 3: 2 Children' }, bstNodes: getBstNodeList(baseTree, [{ val: 25, type: 'compare' }]) });
    trace.push({ line: 18, note: `ค้นหา In-order Successor: เดินไป Subtree ขวา (35) แล้วเดินซ้ายสุด พบโหนด 30 (ค่าน้อยที่สุดในกิ่งขวา)`, watch: { key: 25, successor: 30 }, bstNodes: getBstNodeList(baseTree, [{ val: 25, type: 'hole' }, { val: 30, type: 'final' }]) });
    trace.push({ line: 19, note: `คัดลอกค่า Successor (30) มาเขียนทับที่ตำแหน่ง Root (25)`, watch: { key: 25, "root.val": 30 }, bstNodes: getBstNodeList({
      val: 30,
      left: { val: 15, left: { val: 10, left: null, right: null }, right: { val: 20, left: null, right: null } },
      right: { val: 35, left: { val: 30, left: null, right: null }, right: { val: 40, left: null, right: null } }
    }, [{ val: 30, type: 'final' }]) });
    trace.push({ line: 20, note: `เรียก delete แบบ Recursive เพื่อลบโหนด Successor (30) เดิมทิ้ง ซึ่งเป็น Leaf Node ลบได้ง่ายดาย!`, watch: { key: 30 }, bstNodes: getBstNodeList({
      val: 30,
      left: { val: 15, left: { val: 10, left: null, right: null }, right: { val: 20, left: null, right: null } },
      right: { val: 35, left: null, right: { val: 40, left: null, right: null } }
    }) });
  }

  return trace;
}


/* ================================================================
   4. HASH TABLE ALGORITHM SIMULATION (CHAINING & PROBING)
================================================================ */

const HASH_CHAIN_CODE = [
  "def insert_chain(self, key):",
  "    index = key % self.table_size",
  "    bucket = self.table[index]",
  "    for node in bucket:",
  "        if node.key == key: return # Key exists",
  "    bucket.append(key) # Collision chained!",
  "    self.num_elements += 1"
];

const HASH_PROBE_CODE = [
  "def insert_linear(self, key):",
  "    base_idx = key % self.table_size",
  "    for i in range(self.table_size):",
  "        idx = (base_idx + i) % self.table_size",
  "        if self.table[idx] is None:",
  "            self.table[idx] = key # Placed successfully",
  "            return True",
  "        # Collision occurred -> probe next slot"
];

function traceHashChaining(keys, M = 10) {
  const trace = [];
  const table = Array.from({ length: M }, () => []);

  trace.push({
    line: 1,
    note: `เริ่มต้น: ตาราง Hash Table ว่างเปล่า ขนาด M = ${M} (Index 0 .. ${M - 1})`,
    watch: { M, total_keys: keys.length },
    table: table.map(b => b.slice()),
    highlights: []
  });

  keys.forEach((k, i) => {
    const idx = k % M;
    trace.push({
      line: 2,
      note: `คำนวณ Hash Function: index = ${k} % ${M} = ${idx}`,
      watch: { key: k, M, index: idx },
      table: table.map(b => b.slice()),
      highlights: [{ bucket: idx, type: 'compare' }]
    });

    const isCollision = table[idx].length > 0;
    if (isCollision) {
      trace.push({
        line: 6,
        note: `เกิด Collision ที่ Bucket ${idx}! มีสมาชิกเดิม ${table[idx].join(', ')} อยู่แล้ว → นำ ${k} ไปต่อท้าย Linked List`,
        watch: { key: k, index: idx, collision: true },
        table: table.map(b => b.slice()),
        highlights: [{ bucket: idx, type: 'hole' }]
      });
    }

    table[idx].push(k);
    trace.push({
      line: 7,
      note: `แทรก ${k} ลงใน Bucket ${idx} สำเร็จ (ขนาดลูกโซ่ = ${table[idx].length})`,
      watch: { key: k, index: idx, chain_len: table[idx].length },
      table: table.map(b => b.slice()),
      highlights: [{ bucket: idx, type: 'final' }]
    });
  });

  return trace;
}

function traceHashProbing(keys, M = 10) {
  const trace = [];
  const table = Array.from({ length: M }, () => null);

  trace.push({
    line: 1,
    note: `เริ่มต้น: ตาราง Open Addressing ขนาด M = ${M}`,
    watch: { M, keys_count: keys.length },
    array: table.slice(),
    highlights: []
  });

  keys.forEach((k) => {
    const base = k % M;
    trace.push({
      line: 2,
      note: `แทรกคีย์ ${k}: base_idx = ${k} % ${M} = ${base}`,
      watch: { key: k, base_idx: base },
      array: table.slice(),
      highlights: [{ index: base, type: 'compare' }]
    });

    for (let i = 0; i < M; i++) {
      const idx = (base + i) % M;
      if (table[idx] === null) {
        table[idx] = k;
        trace.push({
          line: 6,
          note: `ช่อง [${idx}] ว่าง (i=${i})  →  วาง ${k} ลงในช่องนี้สำเร็จ!`,
          watch: { key: k, placed_at: idx, probe_steps: i },
          array: table.slice(),
          highlights: [{ index: idx, type: 'final' }]
        });
        break;
      } else {
        trace.push({
          line: 8,
          note: `ช่อง [${idx}] ชนกับค่า ${table[idx]}!  →  Probe ขยับไปช่องถัดไป (i = ${i + 1})`,
          watch: { key: k, collided_at: idx, collision_with: table[idx], i: i + 1 },
          array: table.slice(),
          highlights: [{ index: idx, type: 'hole' }]
        });
      }
    }
  });

  return trace;
}


/* ================================================================
   5. STACK: INFIX TO POSTFIX ALGORITHM SIMULATION
================================================================ */

const STACK_CODE = [
  "def infix_to_postfix(expr):",
  "    stack = []",
  "    output = []",
  "    for token in expr.split():",
  "        if is_operand(token): output.append(token)",
  "        elif token == '(': stack.push(token)",
  "        elif token == ')':",
  "            while stack and stack.top() != '(': output.append(stack.pop())",
  "            stack.pop() # Remove '('",
  "        else: # Operator",
  "            while stack and precedence(stack.top()) >= precedence(token):",
  "                output.append(stack.pop())",
  "            stack.push(token)",
  "    while stack: output.append(stack.pop())",
  "    return ' '.join(output)"
];

function traceInfixToPostfix(expr) {
  const tokens = expr.replace(/\(/g, ' ( ').replace(/\)/g, ' ) ').trim().split(/\s+/);
  const prec = { '^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0 };

  const trace = [];
  const stack = [];
  const output = [];

  trace.push({
    line: 1,
    note: `เริ่มต้น: เตรียมแปลงนิพจน์ Infix "${expr}" เป็น Postfix`,
    watch: { expr, tokens_left: tokens.length },
    stack: stack.slice(),
    output: output.slice(),
    token: null
  });

  tokens.forEach((t) => {
    if (/^[A-Za-z0-9]+$/.test(t)) {
      output.push(t);
      trace.push({
        line: 5,
        note: `อ่านพบ Operand "${t}"  →  ส่งตรงไปยัง Output ทันที`,
        watch: { token: t, type: 'Operand', output: output.join(' ') },
        stack: stack.slice(),
        output: output.slice(),
        token: t
      });
    } else if (t === '(') {
      stack.push(t);
      trace.push({
        line: 6,
        note: `อ่านพบวงเล็บเปิด "("  →  Push ลง Stack เป็นตัวคั่นขอบเขต`,
        watch: { token: t, stack: stack.join(' ') },
        stack: stack.slice(),
        output: output.slice(),
        token: t
      });
    } else if (t === ')') {
      trace.push({
        line: 7,
        note: `อ่านพบวงเล็บปิด ")"  →  เตรียมนิมนต์ Pop ตัวดำเนินการทั้งหมดจนกว่าจะเจอ "("`,
        watch: { token: t },
        stack: stack.slice(),
        output: output.slice(),
        token: t
      });
      while (stack.length && stack[stack.length - 1] !== '(') {
        const popped = stack.pop();
        output.push(popped);
        trace.push({
          line: 8,
          note: `Pop "${popped}" ออกจาก Stack ส่งไปที่ Output`,
          watch: { popped, output: output.join(' ') },
          stack: stack.slice(),
          output: output.slice(),
          token: t
        });
      }
      stack.pop(); // remove '('
      trace.push({
        line: 9,
        note: `Pop และทิ้ง "(" ออกจาก Stack สำเร็จ`,
        watch: { token: t, stack: stack.join(' ') },
        stack: stack.slice(),
        output: output.slice(),
        token: t
      });
    } else {
      // Operator
      const curPrec = prec[t] || 0;
      trace.push({
        line: 10,
        note: `อ่านพบ Operator "${t}" (Precedence = ${curPrec})`,
        watch: { token: t, precedence: curPrec },
        stack: stack.slice(),
        output: output.slice(),
        token: t
      });

      while (stack.length && (prec[stack[stack.length - 1]] || 0) >= curPrec) {
        const topOp = stack.pop();
        output.push(topOp);
        trace.push({
          line: 12,
          note: `Precedence ของ "${topOp}" ใน Stack ≥ "${t}"  →  Pop "${topOp}" ออกไปที่ Output`,
          watch: { popped: topOp, output: output.join(' ') },
          stack: stack.slice(),
          output: output.slice(),
          token: t
        });
      }
      stack.push(t);
      trace.push({
        line: 13,
        note: `Push "${t}" ลงบน Stack`,
        watch: { token: t, stack: stack.join(' ') },
        stack: stack.slice(),
        output: output.slice(),
        token: t
      });
    }
  });

  while (stack.length) {
    const popped = stack.pop();
    output.push(popped);
    trace.push({
      line: 14,
      note: `สแกนนิพจน์หมดแล้ว  →  Pop ตัวดำเนินการที่ตกค้างใน Stack "${popped}" ออกไปที่ Output`,
      watch: { popped, output: output.join(' ') },
      stack: stack.slice(),
      output: output.slice(),
      token: 'EOF'
    });
  }

  trace.push({
    line: 15,
    note: `✔ แปลงสำเร็จสมบูรณ์! ผลลัพธ์ Postfix: "${output.join(' ')}"`,
    watch: { result: output.join(' ') },
    stack: [],
    output: output.slice(),
    token: 'DONE'
  });

  return trace;
}


/* ================================================================
   6. APPLICATION INITIALIZATION & DOM BINDINGS
================================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // -------------------------------------------------------------
  // TOPIC SWITCHER LOGIC
  // -------------------------------------------------------------
  const topicPills = document.querySelectorAll('.topic-pill');
  const topicViews = document.querySelectorAll('.topic-view');
  const subTocLinks = document.getElementById('subTocLinks');

  const subTocMap = {
    heap: [
      { href: '#heap-principle', text: '① หลักการ Priority Queue' },
      { href: '#heap-build', text: '② สร้าง Heap ทีละตัว (10 ตัว)' },
      { href: '#heap-demo', text: '③ Insert(14) & DeleteMin() เดี่ยว' },
      { href: '#heap-sandbox', text: '④ Interactive Sandbox' }
    ],
    bst: [
      { href: '#bst-principle', text: '① หลักการ & Invariant' },
      { href: '#bst-build', text: '② สร้าง BST ทีละตัว' },
      { href: '#bst-demo', text: '③ Insert / Search / Delete 3 เคส' }
    ],
    hash: [
      { href: '#hash-principle', text: '① หลักการ & Load Factor' },
      { href: '#hash-chaining', text: '② Separate Chaining' },
      { href: '#hash-probing', text: '③ Linear Probing' }
    ],
    stack: [
      { href: '#stack-principle', text: '① หลักการ & Precedence' },
      { href: '#stack-shunting', text: '② Shunting-Yard Stepper' }
    ],
    assign1: [
      { href: '#assign1-principle', text: '① กฎการสลับโหนด' },
      { href: '#assign1-swap-debug', text: '② Linked List Pointer Swap Debugger' }
    ],
    test1: [
      { href: '#test1-principle', text: '① โครงสร้างโค้ด program.py' },
      { href: '#test1-queue-debug', text: '② Queue Over/Underflow Debugger' }
    ],
    test2: [
      { href: '#test2-principle', text: '① ทฤษฎี Position Move & Pass' },
      { href: '#test2-sorting-debug', text: '② Interactive Sorting Debugger' }
    ],
    assign4: [
      { href: '#assign4-principle', text: '① ตาราง Known, d_v, p_v' },
      { href: '#assign4-bfs-debug', text: '② Graph BFS Shortest Path Debugger' }
    ]
  };

  function switchTopic(topicKey) {
    topicPills.forEach(p => p.classList.toggle('active', p.dataset.topic === topicKey));
    topicViews.forEach(v => v.classList.toggle('active', v.id === `topic-${topicKey}`));

    if (subTocLinks && subTocMap[topicKey]) {
      subTocLinks.innerHTML = subTocMap[topicKey].map(item =>
        `<a href="${item.href}">${escapeHtml(item.text)}</a>`
      ).join('');
    }
  }

  const topicPillsEl = document.getElementById('topicPills');
  const scrollLeftBtn = document.getElementById('pillsScrollLeft');
  const scrollRightBtn = document.getElementById('pillsScrollRight');

  if (scrollLeftBtn && topicPillsEl) {
    scrollLeftBtn.addEventListener('click', () => {
      topicPillsEl.scrollBy({ left: -180, behavior: 'smooth' });
    });
  }

  if (scrollRightBtn && topicPillsEl) {
    scrollRightBtn.addEventListener('click', () => {
      topicPillsEl.scrollBy({ left: 180, behavior: 'smooth' });
    });
  }

  topicPills.forEach(pill => {
    pill.addEventListener('click', () => {
      switchTopic(pill.dataset.topic);
      pill.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    });
  });

  // -------------------------------------------------------------
  // 1. BINARY HEAP WIDGETS
  // -------------------------------------------------------------
  const EXAM_HEAP_VALUES = [13, 21, 16, 24, 31, 19, 68, 65, 26, 32];
  const EXAM_INIT_ARRAY = [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32];
  const EXAM_INIT_SIZE = 10;

  // Build Heap from scratch debugger
  const heapBuildWidget = buildDebuggerWidget(document.getElementById('heapBuildDebugger'), {
    id: 'h_bld',
    defaultMode: 'build',
    showJump: true,
    getCode: () => HEAP_INSERT_CODE,
    buildTrace: () => traceBuildFromScratch(EXAM_HEAP_VALUES)
  });
  if (heapBuildWidget) heapBuildWidget.setMode('build');

  // Single-op Heap debugger (insert(14) vs deleteMin())
  const heapSingleWidget = buildDebuggerWidget(document.getElementById('heapSingleDebugger'), {
    id: 'h_sgl',
    defaultMode: 'insert',
    showJump: false,
    getCode: (mode) => mode === 'insert' ? HEAP_INSERT_CODE : HEAP_DELETE_CODE,
    buildTrace: (mode) => mode === 'insert'
      ? traceInsertSingle(EXAM_INIT_ARRAY, EXAM_INIT_SIZE, 14)
      : traceDeleteMin(EXAM_INIT_ARRAY, EXAM_INIT_SIZE)
  });
  if (heapSingleWidget) heapSingleWidget.setMode('insert');

  // Tabs for Single-Op Heap
  document.querySelectorAll('[data-heap-demo]').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (heapSingleWidget) heapSingleWidget.setMode(btn.dataset.heapDemo);
    });
  });

  // -------------------------------------------------------------
  // HEAP SANDBOX (INTERACTIVE OPERATIONS)
  // -------------------------------------------------------------
  let sbxHeap = [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32];
  let sbxSize = 10;

  function renderSbxHeap(note = '') {
    const svg = document.getElementById('sbx_heapTreeSvg');
    const row = document.getElementById('sbx_heapArrayRow');
    const tag = document.getElementById('sbx_heapSizeTag');
    const nar = document.getElementById('sbx_heapNarration');

    if (tag) tag.textContent = `currentSize = ${sbxSize}`;
    if (nar && note) nar.textContent = note;

    // Render Array
    if (row) {
      let html = `<div class="abox dead"><span class="aidx">0</span>·</div>`;
      for (let i = 1; i <= Math.max(sbxSize, 10); i++) {
        const val = sbxHeap[i];
        const isDead = i > sbxSize;
        html += `<div class="abox${isDead ? ' dead' : ''}"><span class="aidx">${i}</span>${isDead ? '' : (val ?? '∅')}</div>`;
      }
      row.innerHTML = html;
    }

    // Render Tree SVG
    if (svg) {
      const W = 760, marginX = 40;
      const nodes = [];
      for (let i = 1; i <= sbxSize; i++) {
        const depth = Math.floor(Math.log2(i));
        const levelStart = Math.pow(2, depth);
        const posInLevel = i - levelStart;
        const x = marginX + (posInLevel + 0.5) * (W - 2 * marginX) / levelStart;
        const y = 46 + depth * 95;
        nodes.push({ i, x, y, val: sbxHeap[i] });
      }

      let edges = '';
      nodes.forEach(n => {
        const p = Math.floor(n.i / 2);
        if (p >= 1) {
          const pn = nodes.find(nn => nn.i === p);
          if (pn) edges += `<line class="edge" x1="${pn.x}" y1="${pn.y}" x2="${n.x}" y2="${n.y}"/>`;
        }
      });

      let circles = '';
      nodes.forEach(n => {
        circles += `<g>
          <circle cx="${n.x}" cy="${n.y}" r="22" fill="#20222c" stroke="#3a3d4b" stroke-width="2"/>
          <text class="node-text" x="${n.x}" y="${n.y + 1}">${n.val}</text>
          <text class="node-idx" x="${n.x}" y="${n.y - 30}">[${n.i}]</text>
        </g>`;
      });

      svg.innerHTML = edges + circles;
    }
  }

  renderSbxHeap('เริ่มต้น: Heap ตัวอย่างจากข้อสอบ (10 โหนด)');

  const btnHeapInsert = document.getElementById('btnHeapInsert');
  if (btnHeapInsert) {
    btnHeapInsert.addEventListener('click', () => {
      const input = document.getElementById('heapCustomVal');
      const val = parseInt(input ? input.value : 0, 10);
      if (isNaN(val)) return;

      sbxSize++;
      while (sbxHeap.length <= sbxSize) sbxHeap.push(null);
      let hole = sbxSize;
      sbxHeap[hole] = null;

      while (hole > 1 && val < sbxHeap[Math.floor(hole / 2)]) {
        sbxHeap[hole] = sbxHeap[Math.floor(hole / 2)];
        hole = Math.floor(hole / 2);
      }
      sbxHeap[hole] = val;
      renderSbxHeap(`✔ แทรกค่า ${val} สำเร็จ! Percolate Up ไปอยู่ที่ index [${hole}]`);
    });
  }

  const btnHeapDeleteMin = document.getElementById('btnHeapDeleteMin');
  if (btnHeapDeleteMin) {
    btnHeapDeleteMin.addEventListener('click', () => {
      if (sbxSize === 0) {
        renderSbxHeap('⚠️ Heap ว่างเปล่า ไม่สามารถ deleteMin ได้');
        return;
      }
      const minVal = sbxHeap[1];
      sbxHeap[1] = sbxHeap[sbxSize];
      sbxSize--;

      let hole = 1;
      const temp = sbxHeap[hole];
      while (hole * 2 <= sbxSize) {
        let child = hole * 2;
        if (child !== sbxSize && sbxHeap[child + 1] < sbxHeap[child]) {
          child++;
        }
        if (sbxHeap[child] < temp) {
          sbxHeap[hole] = sbxHeap[child];
          hole = child;
        } else {
          break;
        }
      }
      if (sbxSize > 0) sbxHeap[hole] = temp;
      renderSbxHeap(`✔ deleteMin() สำเร็จ! ดึงค่า ${minVal} ออก และ Percolate Down จัดระเบียบเรียบร้อย`);
    });
  }

  const btnHeapResetExam = document.getElementById('btnHeapResetExam');
  if (btnHeapResetExam) {
    btnHeapResetExam.addEventListener('click', () => {
      sbxHeap = [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32];
      sbxSize = 10;
      renderSbxHeap('🔄 คืนค่า Heap 10 โหนดตามข้อสอบเรียบร้อย');
    });
  }

  const btnHeapRandom = document.getElementById('btnHeapRandom');
  if (btnHeapRandom) {
    btnHeapRandom.addEventListener('click', () => {
      sbxHeap = [null];
      sbxSize = 0;
      const count = 7 + Math.floor(Math.random() * 4);
      for (let i = 0; i < count; i++) {
        const val = 10 + Math.floor(Math.random() * 85);
        sbxSize++;
        let hole = sbxSize;
        while (hole > 1 && val < sbxHeap[Math.floor(hole / 2)]) {
          sbxHeap[hole] = sbxHeap[Math.floor(hole / 2)];
          hole = Math.floor(hole / 2);
        }
        sbxHeap[hole] = val;
      }
      renderSbxHeap(`🎲 สุ่มสร้าง Heap ใหม่ขนาด ${sbxSize} โหนดสำเร็จ`);
    });
  }

  const btnHeapClear = document.getElementById('btnHeapClear');
  if (btnHeapClear) {
    btnHeapClear.addEventListener('click', () => {
      sbxHeap = [null];
      sbxSize = 0;
      renderSbxHeap('🗑️ ล้าง Heap เรียบร้อย (currentSize = 0)');
    });
  }

  // -------------------------------------------------------------
  // 2. BST WIDGETS
  // -------------------------------------------------------------
  const BST_BUILD_VALUES = [25, 15, 35, 10, 20, 30, 40];

  const bstBuildWidget = buildDebuggerWidget(document.getElementById('bstBuildDebugger'), {
    id: 'bst_bld',
    defaultMode: 'build',
    showJump: true,
    treeTitle: 'BST Tree View',
    arrayTitle: 'In-Order Traversal Representation',
    arraySubtitle: 'left < root < right',
    getCode: () => BST_CODE,
    customRenderTree: renderBstSvg,
    customRenderArray: renderBstInorderArray,
    buildTrace: () => traceBstBuild(BST_BUILD_VALUES)
  });
  if (bstBuildWidget) bstBuildWidget.setMode('build');

  const bstSingleWidget = buildDebuggerWidget(document.getElementById('bstSingleDebugger'), {
    id: 'bst_sgl',
    defaultMode: 'insert',
    showJump: false,
    treeTitle: 'BST Operations Tree',
    arrayTitle: 'In-Order Traversal',
    getCode: () => BST_CODE,
    customRenderTree: renderBstSvg,
    customRenderArray: renderBstInorderArray,
    buildTrace: (mode) => traceBstOperations(mode)
  });
  if (bstSingleWidget) bstSingleWidget.setMode('insert');

  document.querySelectorAll('[data-bst-demo]').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (bstSingleWidget) bstSingleWidget.setMode(btn.dataset.bstDemo);
    });
  });

  // -------------------------------------------------------------
  // 3. HASH TABLE WIDGETS
  // -------------------------------------------------------------
  const HASH_EXAM_KEYS = [15, 25, 35, 12, 22, 45];

  // Chaining Widget
  const hashChainingWidget = buildDebuggerWidget(document.getElementById('hashChainingDebugger'), {
    id: 'hsh_chn',
    defaultMode: 'chain',
    showJump: false,
    treeTitle: 'Bucket & Linked List Chains',
    arrayTitle: 'Hash Buckets (M = 10)',
    arraySubtitle: 'h(k) = k % 10',
    getCode: () => HASH_CHAIN_CODE,
    customRenderTree: (svg, step) => {
      const table = step.table || [];
      let html = '';
      table.forEach((bucket, i) => {
        const y = 30 + i * 36;
        const hl = (step.highlights || []).find(h => h.bucket === i);
        let stroke = '#3a3d4b', fill = '#1b1d25';
        if (hl) {
          stroke = hl.type === 'hole' ? 'var(--amber)' : hl.type === 'final' ? 'var(--green)' : 'var(--cyan)';
          fill = hl.type === 'hole' ? 'rgba(245,166,35,0.15)' : 'rgba(79,209,232,0.12)';
        }

        // Slot
        html += `<rect x="30" y="${y}" width="60" height="28" rx="6" fill="${fill}" stroke="${stroke}" stroke-width="1.8"/>
          <text x="60" y="${y + 18}" fill="var(--cyan)" font-family="JetBrains Mono" font-weight="700" font-size="12" text-anchor="middle">[${i}]</text>`;

        // Chains
        bucket.forEach((k, ci) => {
          const cx = 130 + ci * 80;
          html += `<line x1="${cx - 40}" y1="${y + 14}" x2="${cx}" y2="${y + 14}" stroke="var(--border)" stroke-width="2"/>
            <polygon points="${cx},${y + 14} ${cx - 6},${y + 10} ${cx - 6},${y + 18}" fill="var(--muted)"/>
            <rect x="${cx}" y="${y}" width="54" height="28" rx="6" fill="#20222c" stroke="var(--cyan)" stroke-width="1.5"/>
            <text x="${cx + 27}" y="${y + 18}" fill="var(--text)" font-family="JetBrains Mono" font-weight="600" font-size="12" text-anchor="middle">${k}</text>`;
        });
      });
      svg.setAttribute('viewBox', '0 0 760 410');
      svg.innerHTML = html;
    },
    customRenderArray: (row, step) => {
      const table = step.table || [];
      let html = '';
      table.forEach((bucket, i) => {
        html += `<div class="abox"><span class="aidx">${i}</span>${bucket.length ? bucket.join(',') : '·'}</div>`;
      });
      row.innerHTML = html;
    },
    buildTrace: () => traceHashChaining(HASH_EXAM_KEYS)
  });
  if (hashChainingWidget) hashChainingWidget.setMode('chain');

  // Linear Probing Widget
  const hashProbingWidget = buildDebuggerWidget(document.getElementById('hashProbingDebugger'), {
    id: 'hsh_prb',
    defaultMode: 'probe',
    showJump: false,
    treeTitle: 'Open Addressing Memory View',
    arrayTitle: 'Table Slots [0 .. 9]',
    getCode: () => HASH_PROBE_CODE,
    buildTrace: () => traceHashProbing(HASH_EXAM_KEYS)
  });
  if (hashProbingWidget) hashProbingWidget.setMode('probe');

  // -------------------------------------------------------------
  // 4. STACK: INFIX TO POSTFIX WIDGET
  // -------------------------------------------------------------
  const EXAM_EXPR = "(A + B) * C - (D - E) * (F + G)";

  const stackShuntingWidget = buildDebuggerWidget(document.getElementById('stackShuntingDebugger'), {
    id: 'stk_snt',
    defaultMode: 'shunting',
    showJump: false,
    treeTitle: 'Operator Stack Visualizer',
    arrayTitle: 'Postfix Output Stream',
    arraySubtitle: 'Reverse Polish Notation',
    getCode: () => STACK_CODE,
    customRenderTree: (svg, step) => {
      const stack = step.stack || [];
      let html = `<line x1="300" y1="360" x2="460" y2="360" stroke="var(--cyan)" stroke-width="3"/>`;
      html += `<line x1="300" y1="360" x2="300" y2="80" stroke="var(--border)" stroke-width="2"/>`;
      html += `<line x1="460" y1="360" x2="460" y2="80" stroke="var(--border)" stroke-width="2"/>`;

      stack.forEach((op, i) => {
        const y = 315 - i * 44;
        html += `<rect x="310" y="${y}" width="140" height="36" rx="6" fill="rgba(79,209,232,0.15)" stroke="var(--cyan)" stroke-width="1.8"/>
          <text x="380" y="${y + 23}" fill="var(--text)" font-family="JetBrains Mono" font-weight="700" font-size="16" text-anchor="middle">${op}</text>`;
      });

      if (step.token) {
        html += `<rect x="60" y="80" width="160" height="50" rx="8" fill="#1b1d25" stroke="var(--amber)" stroke-width="2"/>
          <text x="140" y="102" fill="var(--muted)" font-family="JetBrains Mono" font-size="11" text-anchor="middle">CURRENT TOKEN</text>
          <text x="140" y="122" fill="var(--amber)" font-family="JetBrains Mono" font-weight="700" font-size="16" text-anchor="middle">${step.token}</text>`;
      }

      svg.setAttribute('viewBox', '0 0 760 400');
      svg.innerHTML = html;
    },
    customRenderArray: (row, step) => {
      const output = step.output || [];
      if (output.length === 0) {
        row.innerHTML = `<div class="abox dead"><span class="aidx">Out</span>(ยังไม่มีผลลัพธ์)</div>`;
        return;
      }
      row.innerHTML = output.map((token, i) =>
        `<div class="abox moved"><span class="aidx">${i + 1}</span>${token}</div>`
      ).join('');
    },
    buildTrace: () => traceInfixToPostfix(EXAM_EXPR)
  });
  if (stackShuntingWidget) stackShuntingWidget.setMode('shunting');

  // -------------------------------------------------------------
  // 4. ASSIGNMENT 1: LINKED LIST POINTER SWAP DEBUGGER
  // -------------------------------------------------------------
  const ASSIGN1_CODE = [
    'class Node:',
    '    def __init__(self, data):',
    '        self.data = data',
    '        self.next = None',
    '',
    'def swap_nodes(head, x, y):',
    '    if x == y: return head',
    '    prevA, currA = None, head',
    '    while currA and currA.data != x:',
    '        prevA, currA = currA, currA.next',
    '    prevB, currB = None, head',
    '    while currB and currB.data != y:',
    '        prevB, currB = currB, currB.next',
    '    if not currA or not currB: return head',
    '    if prevA: prevA.next = currB',
    '    else: head = currB',
    '    if prevB: prevB.next = currA',
    '    else: head = currA',
    '    currA.next, currB.next = currB.next, currA.next',
    '    return head'
  ];

  function traceAssign1(mode) {
    const trace = [];
    if (mode === 'lecture') {
      // Lecture 3: 4-node pointer swap: 1 -> 4 -> 3 -> 2 -> 5
      trace.push({
        line: 6,
        vars: { state: 'Initial 1->2->3->4->5' },
        nodes: ['1', '2', '3', '4', '5'],
        badge: 'INIT',
        narration: 'เริ่มต้นโครงสร้างห้องเรียน: 1 -> 2 -> 3 -> 4 -> 5 ต้องการสลับเป็น 1 -> 4 -> 3 -> 2 -> 5',
        console: 'โจทย์หน้า 3: node1 -> node2 -> node3 -> node4 -> node5'
      });
      trace.push({
        line: 14,
        vars: { 'node2.next': 'node5' },
        nodes: ['1', '4', '3', '2', '5'],
        badge: 'STEP 1',
        narration: 'คำสั่ง 1: node2.next = node5 (ผูก node2 ให้ชี้ไปที่ node5 รอไว้ล่วงหน้า)',
        console: 'node2.next = node5'
      });
      trace.push({
        line: 17,
        vars: { 'node3.next': 'node2' },
        nodes: ['1', '4', '3', '2', '5'],
        badge: 'STEP 2',
        narration: 'คำสั่ง 2: node3.next = node2 (ผูก node3 ให้ชี้กลับมาที่ node2)',
        console: 'node3.next = node2'
      });
      trace.push({
        line: 18,
        vars: { 'node4.next': 'node3' },
        nodes: ['1', '4', '3', '2', '5'],
        badge: 'STEP 3',
        narration: 'คำสั่ง 3: node4.next = node3 (ผูก node4 ให้ชี้มาที่ node3)',
        console: 'node4.next = node3'
      });
      trace.push({
        line: 20,
        vars: { 'node1.next': 'node4', result: '1 -> 4 -> 3 -> 2 -> 5' },
        nodes: ['1', '4', '3', '2', '5'],
        badge: 'COMPLETE',
        narration: 'คำสั่ง 4: node1.next = node4 (ปรับหัวลิสต์ให้ชี้ไปที่ node4 เป็นตัวแรก) เสร็จสมบูรณ์!',
        console: '✔ สลับ 4 โหนดสำเร็จ: 1 -> 4 -> 3 -> 2 -> 5 ตรงตามเฉลยอาจารย์ประดิษฐ์'
      });
      return trace;
    }

    // Default student ID mode: 6 -> 1 -> 2 -> 0 -> 3 -> 7, swap 1 and 3
    trace.push({
      line: 6,
      vars: { x: 1, y: 3, head: '6', prevA: 'None', currA: '6', prevB: 'None', currB: '6' },
      nodes: ['6', '1', '2', '0', '3', '7'],
      badge: 'START',
      narration: 'เริ่มต้น: Singly Linked List รหัสนักศึกษา [6 -> 1 -> 2 -> 0 -> 3 -> 7] ต้องการสลับโหนดค่า 1 กับโหนดค่า 3',
      console: '>>> swap_nodes(head, x=1, y=3)'
    });
    trace.push({
      line: 8,
      vars: { x: 1, y: 3, head: '6', prevA: 'None', currA: '6' },
      nodes: ['6', '1', '2', '0', '3', '7'],
      badge: 'SEARCH A',
      narration: 'เริ่มค้นหาโหนด x=1: prevA = None, currA = head (โหนด 6) -> 6 != 1 เลื่อนต่อ',
      console: 'traverse: prevA = 6, currA = 1'
    });
    trace.push({
      line: 10,
      vars: { x: 1, y: 3, prevA: 'Node(6)', currA: 'Node(1)' },
      nodes: ['6', '1', '2', '0', '3', '7'],
      badge: 'FOUND A',
      narration: 'พบโหนด x=1 แล้ว! บันทึกพอยน์เตอร์: prevA = Node(6), currA = Node(1)',
      console: '✔ Found x=1 at currA'
    });
    trace.push({
      line: 11,
      vars: { x: 1, y: 3, prevB: 'None', currB: 'head (6)' },
      nodes: ['6', '1', '2', '0', '3', '7'],
      badge: 'SEARCH B',
      narration: 'เริ่มค้นหาโหนด y=3 จากหัวลิสต์: prevB = None, currB = head',
      console: 'traverse to find y=3'
    });
    trace.push({
      line: 13,
      vars: { x: 1, y: 3, prevB: 'Node(0)', currB: 'Node(3)' },
      nodes: ['6', '1', '2', '0', '3', '7'],
      badge: 'FOUND B',
      narration: 'พบโหนด y=3 แล้ว! บันทึกพอยน์เตอร์: prevB = Node(0), currB = Node(3)',
      console: '✔ Found y=3 at currB'
    });
    trace.push({
      line: 15,
      vars: { 'prevA.next': 'currB (3)', currA: '1', currB: '3' },
      nodes: ['6', '3', '2', '0', '1', '7'],
      badge: 'LINK 1',
      narration: 'คำสั่ง prevA.next = currB: ให้โหนด 6 ชี้ข้ามไปยังโหนด 3 ทันที',
      console: 'Pointer: prevA(6).next = currB(3)'
    });
    trace.push({
      line: 18,
      vars: { 'prevB.next': 'currA (1)', currA: '1', currB: '3' },
      nodes: ['6', '3', '2', '0', '1', '7'],
      badge: 'LINK 2',
      narration: 'คำสั่ง prevB.next = currA: ให้โหนด 0 ชี้กลับมายังโหนด 1',
      console: 'Pointer: prevB(0).next = currA(1)'
    });
    trace.push({
      line: 20,
      vars: { 'currA.next': '7', 'currB.next': '2' },
      nodes: ['6', '3', '2', '0', '1', '7'],
      badge: 'SWAP NEXT',
      narration: 'สลับเส้นเชื่อม next: currA.next (1 ชี้ 7), currB.next (3 ชี้ 2)',
      console: 'Pointer swap: currA.next, currB.next = currB.next, currA.next'
    });
    trace.push({
      line: 21,
      vars: { result: '6 -> 3 -> 2 -> 0 -> 1 -> 7' },
      nodes: ['6', '3', '2', '0', '1', '7'],
      badge: 'DONE',
      narration: '✔ สลับโหนดสำเร็จ! ได้ลิสต์ 6 -> 3 -> 2 -> 0 -> 1 -> 7 โดยที่ไม่มีโหนดหลุดหายและไม่ต้อง copy ข้อมูล!',
      console: '✔ Complete swap_nodes! Time: O(N), Space: O(1)'
    });
    return trace;
  }

  const assign1Widget = buildDebuggerWidget(document.getElementById('assign1Debugger'), {
    id: 'asg1',
    defaultMode: 'swap',
    showJump: false,
    treeTitle: 'Linked List Pointer Architecture',
    arrayTitle: 'Node Traversal Order',
    arraySubtitle: 'Singly Linked List chain',
    getCode: () => ASSIGN1_CODE,
    customRenderTree: (svg, step) => {
      const nodes = step.nodes || ['6', '1', '2', '0', '3', '7'];
      let html = '';
      const startX = 50;
      const spacing = 110;
      const y = 170;

      // Head pointer indicator
      html += `<rect x="20" y="70" width="56" height="26" rx="5" fill="#1e293b" stroke="var(--cyan)" stroke-width="1.5"/>
        <text x="48" y="87" fill="var(--cyan)" font-family="JetBrains Mono" font-weight="700" font-size="12" text-anchor="middle">head</text>
        <line x1="48" y1="96" x2="48" y2="150" stroke="var(--cyan)" stroke-width="2"/>
        <polygon points="48,158 44,148 52,148" fill="var(--cyan)"/>`;

      nodes.forEach((val, i) => {
        const x = startX + i * spacing;
        const isA = (val === '1' && step.badge && step.badge.includes('A'));
        const isB = (val === '3' && step.badge && step.badge.includes('B'));
        let fill = '#171924';
        let stroke = '#3a3d4b';
        if (isA || isB) {
          fill = 'rgba(79, 209, 232, 0.2)';
          stroke = 'var(--cyan)';
        } else if (step.badge === 'DONE') {
          fill = 'rgba(16, 185, 129, 0.15)';
          stroke = 'var(--green)';
        }

        // Data part & Next pointer box
        html += `<g>
          <rect x="${x}" y="${y}" width="46" height="42" rx="6" fill="${fill}" stroke="${stroke}" stroke-width="2"/>
          <text x="${x + 23}" y="${y + 27}" fill="var(--text)" font-family="Chakra Petch" font-weight="700" font-size="18" text-anchor="middle">${val}</text>
          <rect x="${x + 46}" y="${y}" width="28" height="42" rx="4" fill="#1b1d25" stroke="${stroke}" stroke-width="1.5"/>
          <circle cx="${x + 60}" cy="${y + 21}" r="4" fill="var(--cyan)"/>
          <text x="${x + 37}" y="${y - 10}" fill="var(--muted)" font-family="JetBrains Mono" font-size="10" text-anchor="middle">[${i}]</text>
        </g>`;

        // Next Arrow
        if (i < nodes.length - 1) {
          const nextX = startX + (i + 1) * spacing;
          html += `<line x1="${x + 74}" y1="${y + 21}" x2="${nextX}" y2="${y + 21}" stroke="var(--cyan)" stroke-width="2"/>
            <polygon points="${nextX},${y + 21} ${nextX - 7},${y + 16} ${nextX - 7},${y + 26}" fill="var(--cyan)"/>`;
        } else {
          // Null pointer
          html += `<line x1="${x + 74}" y1="${y + 21}" x2="${x + 95}" y2="${y + 21}" stroke="var(--muted)" stroke-width="2"/>
            <text x="${x + 104}" y="${y + 25}" fill="var(--muted)" font-family="JetBrains Mono" font-weight="700" font-size="12">None</text>`;
        }
      });

      svg.setAttribute('viewBox', '0 0 760 360');
      svg.innerHTML = html;
    },
    customRenderArray: (row, step) => {
      const nodes = step.nodes || [];
      row.innerHTML = nodes.map((val, i) =>
        `<div class="abox moved"><span class="aidx">Node ${i}</span>${val}</div>`
      ).join('');
    },
    buildTrace: (mode) => traceAssign1(mode)
  });
  if (assign1Widget) assign1Widget.setMode('swap');

  document.querySelectorAll('[data-assign1-mode]').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (assign1Widget) assign1Widget.setMode(btn.dataset.assign1Mode);
    });
  });

  // -------------------------------------------------------------
  // 5. TEST PROGRAM 1: QUEUE OVERFLOW & UNDERFLOW DEBUGGER
  // -------------------------------------------------------------
  const TEST1_CODE = [
    '# Paphavin Thitichunhakun 6806021612037',
    'class Queue:',
    '    def __init__(self, limit):',
    '        self.items = []',
    '        self.limit = limit',
    '        self.front = 0',
    '        self.rear = -1',
    '        self.size = 0',
    '',
    '    def isEmpty(self):',
    '        return len(self.items) <= 0',
    '',
    '    def enQueue(self, item):',
    '        if len(self.items) >= self.limit:',
    '            print("Queue is overflow")',
    '        else:',
    '            self.items.append(item)',
    '            self.rear += 1',
    '            self.size += 1',
    '',
    '    def deQueue(self):',
    '        if self.isEmpty():',
    '            print("Queue is underflow")',
    '        else:',
    '            self.items.pop(0)',
    '            self.size = self.size - 1',
    '            self.rear = self.size - 1'
  ];

  function traceTest1Queue() {
    const trace = [];
    trace.push({
      line: 3,
      vars: { limit: 5, size: 0, front: 0, rear: -1, items: '[]' },
      items: [],
      limit: 5,
      front: 0,
      rear: -1,
      badge: 'INIT',
      narration: 'เริ่มต้นสร้าง queue = Queue(5): กำหนด limit=5, items=[] ว่างเปล่า, front=0, rear=-1',
      console: '>>> queue = Queue(5) สร้างคิวขนาดจำกัด 5 ช่อง'
    });

    const pushVals = [6, 1, 2, 0, 3];
    let curItems = [];
    pushVals.forEach((v, i) => {
      curItems.push(v);
      trace.push({
        line: 17,
        vars: { item: v, limit: 5, size: i + 1, front: 0, rear: i, items: `[${curItems.join(', ')}]` },
        items: [...curItems],
        limit: 5,
        front: 0,
        rear: i,
        badge: 'ENQUEUE',
        narration: `enQueue(${v}): เพิ่ม ${v} ต่อท้าย, ขยับ rear=${i}, size=${i + 1}`,
        console: `queue.enQueue(${v}) -> items: [${curItems.join(', ')}]`
      });
    });

    // Overflow attempt:
    trace.push({
      line: 15,
      vars: { item: 7, limit: 5, size: 5, 'len(items)': 5 },
      items: [6, 1, 2, 0, 3],
      limit: 5,
      front: 0,
      rear: 4,
      badge: 'OVERFLOW!',
      narration: '⚠️ enQueue(7): len(self.items) >= self.limit (5 >= 5) เป็นจริง! พิมพ์ "Queue is overflow" ทาง stdout',
      console: 'Queue is overflow (คิวเต็ม ไม่สามารถแทรก 7 ได้)'
    });

    // Reset to Queue(6)
    trace.push({
      line: 3,
      vars: { limit: 6, size: 6, front: 0, rear: 5, items: '[6, 1, 2, 0, 3, 7]' },
      items: [6, 1, 2, 0, 3, 7],
      limit: 6,
      front: 0,
      rear: 5,
      badge: 'RESET Q(6)',
      narration: 'เริ่มส่วนที่ 2 ของโปรแกรม: สร้าง queue = Queue(6) และ enQueue 6, 1, 2, 0, 3, 7 ครบ 6 ตัว',
      console: '>>> queue = Queue(6) เตรียมทดสอบ DeQueue จนเกลี้ยง'
    });

    let deqItems = [6, 1, 2, 0, 3, 7];
    for (let step = 0; step < 6; step++) {
      const removed = deqItems.shift();
      trace.push({
        line: 25,
        vars: { popped: removed, size: deqItems.length, rear: deqItems.length - 1, items: `[${deqItems.join(', ')}]` },
        items: [...deqItems],
        limit: 6,
        front: 0,
        rear: deqItems.length - 1,
        badge: 'DEQUEUE',
        narration: `deQueue(): ดึง ${removed} ออกจากหัวคิว (pop(0)), size ลดเหลือ ${deqItems.length}, rear = ${deqItems.length - 1}`,
        console: `queue.deQueue() -> ดึง ${removed} ออก, เหลือ [${deqItems.join(', ')}]`
      });
    }

    // Underflow attempt:
    trace.push({
      line: 23,
      vars: { 'isEmpty()': 'True', size: 0, items: '[]' },
      items: [],
      limit: 6,
      front: 0,
      rear: -1,
      badge: 'UNDERFLOW!',
      narration: '⚠️ สั่ง deQueue() ครั้งที่ 7 ในขณะที่คิวว่างเปล่า (isEmpty() == True) $\to$ พิมพ์ "Queue is underflow"',
      console: 'Queue is underflow (คิวว่างเปล่า ไม่สามารถ deQueue ได้)'
    });

    return trace;
  }

  const test1Widget = buildDebuggerWidget(document.getElementById('test1Debugger'), {
    id: 'tst1',
    defaultMode: 'queue',
    showJump: false,
    treeTitle: 'Queue Conveyor Architecture',
    arrayTitle: 'Array Storage (self.items)',
    arraySubtitle: 'FIFO Queue buffer',
    getCode: () => TEST1_CODE,
    customRenderTree: (svg, step) => {
      const items = step.items || [];
      const limit = step.limit || 6;
      let html = '';

      // Conveyor chamber
      html += `<rect x="60" y="120" width="640" height="120" rx="14" fill="#14151b" stroke="var(--border)" stroke-width="2"/>
        <text x="80" y="150" fill="var(--muted)" font-family="JetBrains Mono" font-size="12">QUEUE CONVEYOR BUFFER (limit=${limit})</text>`;

      for (let i = 0; i < limit; i++) {
        const x = 90 + i * 100;
        const val = items[i];
        const isPresent = val !== undefined;
        let fill = isPresent ? 'rgba(79, 209, 232, 0.15)' : '#1b1d25';
        let stroke = isPresent ? 'var(--cyan)' : '#333745';
        if (step.badge === 'OVERFLOW!' && i === limit - 1) {
          fill = 'rgba(245, 166, 35, 0.25)';
          stroke = 'var(--amber)';
        } else if (step.badge === 'UNDERFLOW!') {
          fill = 'rgba(255, 107, 129, 0.15)';
          stroke = 'var(--red)';
        }

        html += `<g>
          <rect x="${x}" y="170" width="80" height="50" rx="8" fill="${fill}" stroke="${stroke}" stroke-width="2"/>
          <text x="${x + 40}" y="202" fill="${isPresent ? 'var(--text)' : 'var(--muted)'}" font-family="Chakra Petch" font-weight="700" font-size="20" text-anchor="middle">${isPresent ? val : '-'}</text>
          <text x="${x + 40}" y="238" fill="var(--muted)" font-family="JetBrains Mono" font-size="10" text-anchor="middle">[${i}]</text>
        </g>`;
      }

      // Front / Rear Pointers
      if (items.length > 0) {
        // Front pointer
        html += `<g>
          <text x="130" y="85" fill="var(--green)" font-family="JetBrains Mono" font-weight="700" font-size="12" text-anchor="middle">FRONT (0)</text>
          <line x1="130" y1="92" x2="130" y2="160" stroke="var(--green)" stroke-width="2"/>
          <polygon points="130,165 126,155 134,155" fill="var(--green)"/>
        </g>`;

        // Rear pointer
        const rearIdx = items.length - 1;
        const rx = 130 + rearIdx * 100;
        html += `<g>
          <text x="${rx}" y="300" fill="var(--amber)" font-family="JetBrains Mono" font-weight="700" font-size="12" text-anchor="middle">REAR (${rearIdx})</text>
          <line x1="${rx}" y1="285" x2="${rx}" y2="230" stroke="var(--amber)" stroke-width="2"/>
          <polygon points="${rx},225 126,235 134,235" fill="var(--amber)"/>
        </g>`;
      }

      svg.setAttribute('viewBox', '0 0 760 360');
      svg.innerHTML = html;
    },
    customRenderArray: (row, step) => {
      const items = step.items || [];
      if (items.length === 0) {
        row.innerHTML = `<div class="abox dead"><span class="aidx">Items</span>[] (Queue is empty)</div>`;
        return;
      }
      row.innerHTML = items.map((val, i) =>
        `<div class="abox moved"><span class="aidx">[${i}]</span>${val}</div>`
      ).join('');
    },
    buildTrace: () => traceTest1Queue()
  });
  if (test1Widget) test1Widget.setMode('queue');

  // -------------------------------------------------------------
  // 6. TEST PROGRAM 2 & LECTURE 9: SORTING TRACE & POSITION MOVE
  // -------------------------------------------------------------
  const TEST2_SORT_CODE = [
    '# Sorting Algorithms: Insertion, Selection, Bubble',
    'def insertion_sort(arr):',
    '    for p in range(1, len(arr)):',
    '        temp = arr[p]',
    '        j = p',
    '        moves = 0',
    '        while j > 0 and temp < arr[j - 1]:',
    '            arr[j] = arr[j - 1]',
    '            j -= 1',
    '            moves += 1',
    '        arr[j] = temp',
    '    return arr'
  ];

  function traceSorting(algo) {
    if (algo === 'selection') {
      const trace = [];
      trace.push({
        line: 2,
        vars: { pass: 0, arr: '[64, 25, 12, 22, 11]' },
        arr: [64, 25, 12, 22, 11],
        highlights: [],
        badge: 'INIT',
        narration: 'เริ่มต้น Selection Sort: ชุดข้อมูล [64, 25, 12, 22, 11]',
        console: 'Selection Sort เริ่มต้น'
      });
      trace.push({
        line: 7,
        vars: { pass: 1, min_idx: 4, min_val: 11, swap_with: 64 },
        arr: [11, 25, 12, 22, 64],
        highlights: [{ idx: 0, type: 'final' }, { idx: 4, type: 'moved' }],
        badge: 'PASS 1 SWAP',
        narration: 'Pass 1: ค่าน้อยสุดคือ 11 (index 4) $\to$ สลับกับ array[0] (64)',
        console: 'Pass 1: swap(arr[0]=64, arr[4]=11) -> [11, 25, 12, 22, 64]'
      });
      trace.push({
        line: 7,
        vars: { pass: 2, min_idx: 2, min_val: 12, swap_with: 25 },
        arr: [11, 12, 25, 22, 64],
        highlights: [{ idx: 1, type: 'final' }, { idx: 2, type: 'moved' }],
        badge: 'PASS 2 SWAP',
        narration: 'Pass 2: ค่าน้อยสุดในส่วนที่เหลือคือ 12 $\to$ สลับกับ array[1] (25)',
        console: 'Pass 2: swap(arr[1]=25, arr[2]=12) -> [11, 12, 25, 22, 64]'
      });
      trace.push({
        line: 7,
        vars: { pass: 3, min_idx: 3, min_val: 22, swap_with: 25 },
        arr: [11, 12, 22, 25, 64],
        highlights: [{ idx: 2, type: 'final' }, { idx: 3, type: 'moved' }],
        badge: 'PASS 3 SWAP',
        narration: 'Pass 3: ค่าน้อยสุดคือ 22 $\to$ สลับกับ array[2] (25)',
        console: 'Pass 3: swap(arr[2]=25, arr[3]=22) -> [11, 12, 22, 25, 64]'
      });
      trace.push({
        line: 11,
        vars: { pass: 4, result: 'SORTED' },
        arr: [11, 12, 22, 25, 64],
        highlights: [{ idx: 0, type: 'final' }, { idx: 1, type: 'final' }, { idx: 2, type: 'final' }, { idx: 3, type: 'final' }, { idx: 4, type: 'final' }],
        badge: 'DONE',
        narration: 'Pass 4: 25 อยู่ในตำแหน่งถูกต้องแล้ว $\to$ สิ้นสุดการจัดเรียง O(N^2)',
        console: '✔ Selection Sort เสร็จสมบูรณ์ [11, 12, 22, 25, 64]'
      });
      return trace;
    } else if (algo === 'bubble') {
      const trace = [];
      trace.push({
        line: 2,
        vars: { pass: 0, arr: '[5, 1, 4, 2, 8]' },
        arr: [5, 1, 4, 2, 8],
        highlights: [],
        badge: 'INIT',
        narration: 'เริ่มต้น Bubble Sort: [5, 1, 4, 2, 8]',
        console: 'Bubble Sort เริ่มต้น'
      });
      trace.push({
        line: 7,
        vars: { pass: 1, compare: '(5, 1)', swap: 'True' },
        arr: [1, 5, 4, 2, 8],
        highlights: [{ idx: 0, type: 'moved' }, { idx: 1, type: 'moved' }],
        badge: 'PASS 1 (5>1)',
        narration: 'Pass 1.1: เปรียบเทียบ 5 กับ 1 $\to$ 5 > 1 ทำการ Swap เป็น [1, 5, 4, 2, 8]',
        console: 'Swap (5, 1)'
      });
      trace.push({
        line: 7,
        vars: { pass: 1, compare: '(5, 4)', swap: 'True' },
        arr: [1, 4, 5, 2, 8],
        highlights: [{ idx: 1, type: 'moved' }, { idx: 2, type: 'moved' }],
        badge: 'PASS 1 (5>4)',
        narration: 'Pass 1.2: เปรียบเทียบ 5 กับ 4 $\to$ 5 > 4 ทำการ Swap เป็น [1, 4, 5, 2, 8]',
        console: 'Swap (5, 4)'
      });
      trace.push({
        line: 7,
        vars: { pass: 1, compare: '(5, 2)', swap: 'True' },
        arr: [1, 4, 2, 5, 8],
        highlights: [{ idx: 2, type: 'moved' }, { idx: 3, type: 'moved' }, { idx: 4, type: 'final' }],
        badge: 'PASS 1 END',
        narration: 'Pass 1.3: เปรียบเทียบ 5 กับ 2 $\to$ 5 > 2 Swap $\to$ เลข 8 ตกตะกอนที่ตำแหน่งท้ายสุด',
        console: 'Pass 1 จบ: 8 อยู่ตำแหน่งสุดท้าย'
      });
      trace.push({
        line: 7,
        vars: { pass: 2, compare: '(4, 2)', swap: 'True' },
        arr: [1, 2, 4, 5, 8],
        highlights: [{ idx: 1, type: 'moved' }, { idx: 2, type: 'moved' }, { idx: 3, type: 'final' }, { idx: 4, type: 'final' }],
        badge: 'PASS 2 END',
        narration: 'Pass 2: เปรียบเทียบ 4 กับ 2 $\to$ Swap $\to$ เลข 5 ตกตะกอน',
        console: 'Pass 2 จบ: [1, 2, 4, 5, 8]'
      });
      trace.push({
        line: 11,
        vars: { pass: 3, swapped: 'False', early_break: 'True' },
        arr: [1, 2, 4, 5, 8],
        highlights: [{ idx: 0, type: 'final' }, { idx: 1, type: 'final' }, { idx: 2, type: 'final' }, { idx: 3, type: 'final' }, { idx: 4, type: 'final' }],
        badge: 'EARLY BREAK',
        narration: 'Pass 3: ไม่มีการสลับค่าใดๆ เกิดขึ้นเลย (swapped == False) $\to$ ตัดจบการทำงานทันที!',
        console: '✔ Early exit triggered! อาร์เรย์เรียงลำดับสมบูรณ์'
      });
      return trace;
    } else {
      // Insertion Sort with Position Move!
      const trace = [];
      trace.push({
        line: 2,
        vars: { pass: 0, total_moves: 0, arr: '[34, 8, 64, 51, 32, 21]' },
        arr: [34, 8, 64, 51, 32, 21],
        highlights: [{ idx: 0, type: 'final' }],
        badge: 'INIT',
        narration: 'เริ่มต้น Insertion Sort จากเอกสารอาจารย์: [34, 8, 64, 51, 32, 21]',
        console: 'Insertion Sort เริ่มต้น (index 0 ถือว่าจัดเสร็จแล้ว)'
      });
      trace.push({
        line: 4,
        vars: { p: 1, temp: 8, 'position move': 1, total_moves: 1 },
        arr: [8, 34, 64, 51, 32, 21],
        highlights: [{ idx: 0, type: 'final' }, { idx: 1, type: 'moved' }],
        badge: 'PASS 1 (MOVE 1)',
        narration: 'Pass 1 (temp=8): 8 < 34 $\to$ เลื่อน 34 ไปทางขวา 1 ตำแหน่ง (Position Move = 1)',
        console: 'Pass 1: temp=8, move=1 -> [8, 34, 64, 51, 32, 21]'
      });
      trace.push({
        line: 4,
        vars: { p: 2, temp: 64, 'position move': 0, total_moves: 1 },
        arr: [8, 34, 64, 51, 32, 21],
        highlights: [{ idx: 0, type: 'final' }, { idx: 1, type: 'final' }, { idx: 2, type: 'final' }],
        badge: 'PASS 2 (MOVE 0)',
        narration: 'Pass 2 (temp=64): 64 > 34 $\to$ ไม่ต้องเลื่อนข้อมูลใดๆ (Position Move = 0)',
        console: 'Pass 2: temp=64, move=0'
      });
      trace.push({
        line: 4,
        vars: { p: 3, temp: 51, 'position move': 1, total_moves: 2 },
        arr: [8, 34, 51, 64, 32, 21],
        highlights: [{ idx: 2, type: 'final' }, { idx: 3, type: 'moved' }],
        badge: 'PASS 3 (MOVE 1)',
        narration: 'Pass 3 (temp=51): 51 < 64 $\to$ เลื่อน 64 ไปทางขวา 1 ตำแหน่ง (Position Move = 1)',
        console: 'Pass 3: temp=51, move=1'
      });
      trace.push({
        line: 4,
        vars: { p: 4, temp: 32, 'position move': 3, total_moves: 5 },
        arr: [8, 32, 34, 51, 64, 21],
        highlights: [{ idx: 1, type: 'final' }, { idx: 4, type: 'moved' }],
        badge: 'PASS 4 (MOVE 3)',
        narration: 'Pass 4 (temp=32): 32 น้อยกว่า 64, 51, 34 $\to$ เลื่อนสมาชิก 3 ตัวขวา (Position Move = 3)',
        console: 'Pass 4: temp=32, move=3'
      });
      trace.push({
        line: 4,
        vars: { p: 5, temp: 21, 'position move': 4, total_moves: 9 },
        arr: [8, 21, 32, 34, 51, 64],
        highlights: [{ idx: 1, type: 'final' }, { idx: 5, type: 'moved' }],
        badge: 'PASS 5 (MOVE 4)',
        narration: 'Pass 5 (temp=21): 21 น้อยกว่า 64, 51, 34, 32 $\to$ เลื่อนสมาชิก 4 ตัวขวา (Position Move = 4)',
        console: 'Pass 5: temp=21, move=4'
      });
      trace.push({
        line: 12,
        vars: { total_moves: 9, result: '[8, 21, 32, 34, 51, 64]' },
        arr: [8, 21, 32, 34, 51, 64],
        highlights: [{ idx: 0, type: 'final' }, { idx: 1, type: 'final' }, { idx: 2, type: 'final' }, { idx: 3, type: 'final' }, { idx: 4, type: 'final' }, { idx: 5, type: 'final' }],
        badge: 'TOTAL 9 MOVES',
        narration: '✔ สิ้นสุดการเรียงลำดับ! รวมจำนวน Position Move ทั้งสิ้น = 1 + 0 + 1 + 3 + 4 = 9 ครั้ง ตรงตามเฉลยอาจารย์',
        console: '✔ สรุปผลรวม Position Move ทั้งสิ้น = 9 ครั้ง'
      });
      return trace;
    }
  }

  const test2Widget = buildDebuggerWidget(document.getElementById('test2Debugger'), {
    id: 'tst2',
    defaultMode: 'insertion',
    showJump: false,
    treeTitle: 'Sorting Pass Visualizer',
    arrayTitle: 'Array Elements & Bar Heights',
    arraySubtitle: 'Pass-by-Pass Tracing',
    getCode: () => TEST2_SORT_CODE,
    customRenderTree: (svg, step) => {
      const arr = step.arr || [34, 8, 64, 51, 32, 21];
      const maxVal = Math.max(...arr, 64);
      let html = '';
      const startX = 80;
      const spacing = 100;
      const baseH = 260;

      arr.forEach((val, i) => {
        const x = startX + i * spacing;
        const barH = Math.max(30, Math.round((val / maxVal) * 180));
        const y = baseH - barH;
        const hl = (step.highlights || []).find(h => h.idx === i);
        let fill = 'linear-gradient(180deg, #3b82f6, #1d4ed8)';
        let stroke = '#60a5fa';
        if (hl) {
          fill = hl.type === 'final' ? 'linear-gradient(180deg, #10b981, #059669)' : 'linear-gradient(180deg, #f59e0b, #d97706)';
          stroke = hl.type === 'final' ? '#34d399' : '#fbbf24';
        }

        html += `<g>
          <rect x="${x}" y="${y}" width="54" height="${barH}" rx="8" fill="${stroke}" fill-opacity="0.25" stroke="${stroke}" stroke-width="2"/>
          <text x="${x + 27}" y="${y - 12}" fill="var(--text)" font-family="JetBrains Mono" font-weight="700" font-size="14" text-anchor="middle">${val}</text>
          <text x="${x + 27}" y="${baseH + 24}" fill="var(--muted)" font-family="JetBrains Mono" font-size="11" text-anchor="middle">[${i}]</text>
        </g>`;
      });

      // Ground line
      html += `<line x1="40" y1="${baseH}" x2="720" y2="${baseH}" stroke="var(--border)" stroke-width="2"/>`;

      svg.setAttribute('viewBox', '0 0 760 340');
      svg.innerHTML = html;
    },
    customRenderArray: (row, step) => {
      const arr = step.arr || [];
      row.innerHTML = arr.map((val, i) => {
        const hl = (step.highlights || []).find(h => h.idx === i);
        const cls = hl ? (hl.type === 'final' ? 'final' : 'moved') : '';
        return `<div class="abox ${cls}"><span class="aidx">[${i}]</span>${val}</div>`;
      }).join('');
    },
    buildTrace: (algo) => traceSorting(algo)
  });
  if (test2Widget) test2Widget.setMode('insertion');

  document.querySelectorAll('[data-sort-algo]').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (test2Widget) test2Widget.setMode(btn.dataset.sortAlgo);
    });
  });

  // -------------------------------------------------------------
  // 7. ASSIGNMENT 4 & LECTURE 11: GRAPH BFS SHORTEST PATH DEBUGGER
  // -------------------------------------------------------------
  const ASSIGN4_GRAPH_CODE = [
    '# Graph Unweighted Shortest Path (BFS)',
    'def unweighted_shortest_path(graph, start):',
    '    table = {v: {"known": False, "d": float("inf"), "p": 0} for v in graph}',
    '    table[start]["d"] = 0',
    '    queue = [start]',
    '    while queue:',
    '        v = queue.pop(0)',
    '        table[v]["known"] = True',
    '        for w in graph[v]:',
    '            if table[w]["d"] == float("inf"):',
    '                table[w]["d"] = table[v]["d"] + 1',
    '                table[w]["p"] = v',
    '                queue.append(w)',
    '    return table'
  ];

  function traceGraphBfs() {
    const trace = [];
    trace.push({
      line: 4,
      vars: { start: 'v1', queue: "['v1']", current: 'None' },
      table: {
        v1: { known: false, d: 0, p: 0 },
        v2: { known: false, d: '∞', p: 0 },
        v3: { known: false, d: '∞', p: 0 },
        v4: { known: false, d: '∞', p: 0 },
        v5: { known: false, d: '∞', p: 0 },
        v6: { known: false, d: '∞', p: 0 },
        v7: { known: false, d: '∞', p: 0 }
      },
      queue: ['v1'],
      activeV: 'v1',
      badge: 'INIT BFS',
      narration: 'เริ่มต้น BFS ที่จุดยอด v1: กำหนด d(v1)=0, จุดยอดอื่น d=∞, นำ v1 เข้าคิว [v1]',
      console: '>>> Start Unweighted Shortest Path จากจุด v1'
    });

    trace.push({
      line: 7,
      vars: { current: 'v1', 'neighbors(v1)': "['v2', 'v4']", queue: "['v2', 'v4']" },
      table: {
        v1: { known: true, d: 0, p: 0 },
        v2: { known: false, d: 1, p: 'v1' },
        v3: { known: false, d: '∞', p: 0 },
        v4: { known: false, d: 1, p: 'v1' },
        v5: { known: false, d: '∞', p: 0 },
        v6: { known: false, d: '∞', p: 0 },
        v7: { known: false, d: '∞', p: 0 }
      },
      queue: ['v2', 'v4'],
      activeV: 'v1',
      badge: 'DEQ v1',
      narration: 'Dequeue v1 (Known=True) $\to$ ตรวจสอบเพื่อนบ้าน v2, v4: อัปเดต d=1, p=v1 แล้ว Enqueue ทั้งคู่',
      console: 'v1 Known! Update v2 (d=1, p=v1), v4 (d=1, p=v1)'
    });

    trace.push({
      line: 7,
      vars: { current: 'v2', 'neighbors(v2)': "['v4', 'v5']", queue: "['v4', 'v5']" },
      table: {
        v1: { known: true, d: 0, p: 0 },
        v2: { known: true, d: 1, p: 'v1' },
        v3: { known: false, d: '∞', p: 0 },
        v4: { known: false, d: 1, p: 'v1' },
        v5: { known: false, d: 2, p: 'v2' },
        v6: { known: false, d: '∞', p: 0 },
        v7: { known: false, d: '∞', p: 0 }
      },
      queue: ['v4', 'v5'],
      activeV: 'v2',
      badge: 'DEQ v2',
      narration: 'Dequeue v2 (Known=True) $\to$ v4 มีค่า d แล้วข้ามไป, อัปเดต v5: d=2, p=v2 แล้ว Enqueue(v5)',
      console: 'v2 Known! Update v5 (d=2, p=v2)'
    });

    trace.push({
      line: 7,
      vars: { current: 'v4', 'neighbors(v4)': "['v3', 'v6', 'v7']", queue: "['v5', 'v3', 'v6', 'v7']" },
      table: {
        v1: { known: true, d: 0, p: 0 },
        v2: { known: true, d: 1, p: 'v1' },
        v3: { known: false, d: 2, p: 'v4' },
        v4: { known: true, d: 1, p: 'v1' },
        v5: { known: false, d: 2, p: 'v2' },
        v6: { known: false, d: 2, p: 'v4' },
        v7: { known: false, d: 2, p: 'v4' }
      },
      queue: ['v5', 'v3', 'v6', 'v7'],
      activeV: 'v4',
      badge: 'DEQ v4',
      narration: 'Dequeue v4 (Known=True) $\to$ เพื่อนบ้าน v3, v6, v7 ได้รับการอัปเดต d=2, p=v4 แล้วเข้าคิวทั้งหมด',
      console: 'v4 Known! Update v3, v6, v7 (d=2, p=v4)'
    });

    trace.push({
      line: 7,
      vars: { current: 'v5', queue: "['v3', 'v6', 'v7']" },
      table: {
        v1: { known: true, d: 0, p: 0 },
        v2: { known: true, d: 1, p: 'v1' },
        v3: { known: false, d: 2, p: 'v4' },
        v4: { known: true, d: 1, p: 'v1' },
        v5: { known: true, d: 2, p: 'v2' },
        v6: { known: false, d: 2, p: 'v4' },
        v7: { known: false, d: 2, p: 'v4' }
      },
      queue: ['v3', 'v6', 'v7'],
      activeV: 'v5',
      badge: 'DEQ v5',
      narration: 'Dequeue v5 (Known=True) $\to$ เพื่อนบ้าน v7 มีค่า d=2 แล้ว ไม่ต้องอัปเดตซ้ำ',
      console: 'v5 Known! ไม่มีการอัปเดตใหม่'
    });

    trace.push({
      line: 14,
      vars: { queue: '[]', result: 'COMPLETE' },
      table: {
        v1: { known: true, d: 0, p: 0 },
        v2: { known: true, d: 1, p: 'v1' },
        v3: { known: true, d: 2, p: 'v4' },
        v4: { known: true, d: 1, p: 'v1' },
        v5: { known: true, d: 2, p: 'v2' },
        v6: { known: true, d: 2, p: 'v4' },
        v7: { known: true, d: 2, p: 'v4' }
      },
      queue: [],
      activeV: null,
      badge: 'ALL KNOWN',
      narration: '✔ Dequeue v3, v6, v7 จนคิวว่างเปล่า! ตารางสถิติระยะทางสั้นสุดสมบูรณ์แบบ ตรงตามเฉลยข้อสอบอาจารย์ประดิษฐ์ 100%',
      console: '✔ สิ้นสุดขั้นตอนวิธี BFS Unweighted Shortest Path'
    });

    return trace;
  }

  const assign4Widget = buildDebuggerWidget(document.getElementById('assign4Debugger'), {
    id: 'asg4',
    defaultMode: 'bfs',
    showJump: false,
    treeTitle: '7-Vertex Digraph Visualization',
    arrayTitle: 'BFS Active Queue',
    arraySubtitle: 'FIFO Queue for unvisited neighbors',
    getCode: () => ASSIGN4_GRAPH_CODE,
    customRenderTree: (svg, step) => {
      const vPos = {
        v1: { x: 90, y: 190 },
        v2: { x: 250, y: 80 },
        v4: { x: 250, y: 300 },
        v3: { x: 410, y: 190 },
        v5: { x: 410, y: 80 },
        v7: { x: 570, y: 300 },
        v6: { x: 570, y: 190 }
      };

      const edges = [
        ['v1', 'v2'], ['v1', 'v4'],
        ['v2', 'v4'], ['v2', 'v5'],
        ['v3', 'v1'], ['v3', 'v6'],
        ['v4', 'v3'], ['v4', 'v6'], ['v4', 'v7'],
        ['v5', 'v7'], ['v7', 'v6']
      ];

      let html = '';

      // Edges with arrows
      edges.forEach(([u, v]) => {
        const p1 = vPos[u], p2 = vPos[v];
        const dx = p2.x - p1.x, dy = p2.y - p1.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const r = 24;
        const x1 = p1.x + (dx / dist) * r;
        const y1 = p1.y + (dy / dist) * r;
        const x2 = p2.x - (dx / dist) * (r + 4);
        const y2 = p2.y - (dy / dist) * (r + 4);

        html += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#3a3d4b" stroke-width="1.8"/>`;
      });

      // Vertices
      const tbl = step.table || {};
      Object.keys(vPos).forEach(key => {
        const { x, y } = vPos[key];
        const info = tbl[key] || { known: false, d: '∞', p: 0 };
        const isActive = step.activeV === key;
        let stroke = '#3a3d4b', fill = '#171924';
        if (isActive) {
          stroke = 'var(--amber)';
          fill = 'rgba(245, 166, 35, 0.25)';
        } else if (info.known) {
          stroke = 'var(--green)';
          fill = 'rgba(16, 185, 129, 0.18)';
        }

        html += `<g>
          <circle cx="${x}" cy="${y}" r="22" fill="${fill}" stroke="${stroke}" stroke-width="2.2"/>
          <text x="${x}" y="${y + 5}" fill="var(--text)" font-family="Chakra Petch" font-weight="700" font-size="14" text-anchor="middle">${key}</text>
          <text x="${x}" y="${y - 28}" fill="${info.known ? 'var(--green)' : 'var(--muted)'}" font-family="JetBrains Mono" font-size="10" text-anchor="middle">d=${info.d}</text>
        </g>`;
      });

      svg.setAttribute('viewBox', '0 0 760 380');
      svg.innerHTML = html;
    },
    customRenderArray: (row, step) => {
      const q = step.queue || [];
      if (q.length === 0) {
        row.innerHTML = `<div class="abox dead"><span class="aidx">Queue</span>(คิวว่างเปล่า — การกระจายเสร็จสิ้น)</div>`;
        return;
      }
      row.innerHTML = q.map((v, i) =>
        `<div class="abox moved"><span class="aidx">[${i}]</span>${v}</div>`
      ).join('');
    },
    buildTrace: () => traceGraphBfs()
  });
  if (assign4Widget) assign4Widget.setMode('bfs');

  // -------------------------------------------------------------
  // URL QUERY PARAMETER AUTO-ROUTING (?topic=assign1, ?ex=...)
  // -------------------------------------------------------------
  const urlParams = new URLSearchParams(window.location.search);
  const topicParam = urlParams.get('topic') || urlParams.get('ex');
  if (topicParam) {
    if (subTocMap[topicParam]) {
      switchTopic(topicParam);
    } else if (topicParam.includes('assign1') || topicParam.includes('linked')) {
      switchTopic('assign1');
    } else if (topicParam.includes('test1') || topicParam.includes('queue')) {
      switchTopic('test1');
    } else if (topicParam.includes('test2') || topicParam.includes('sort')) {
      switchTopic('test2');
    } else if (topicParam.includes('assign4') || topicParam.includes('graph')) {
      switchTopic('assign4');
    } else if (topicParam.includes('heap')) {
      switchTopic('heap');
    } else if (topicParam.includes('bst')) {
      switchTopic('bst');
    } else if (topicParam.includes('hash')) {
      switchTopic('hash');
    } else if (topicParam.includes('stack')) {
      switchTopic('stack');
    }
  }

  // -------------------------------------------------------------
  // GLOBAL KEYBOARD SHORTCUTS (Space / ArrowRight = Next, ArrowLeft = Prev, R = Reset)
  // -------------------------------------------------------------
  window.addEventListener('keydown', (e) => {
    // Skip if user is typing in an input field
    const activeEl = document.activeElement;
    if (activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA' || activeEl.isContentEditable)) {
      return;
    }

    const activeView = document.querySelector('.topic-view.active');
    if (!activeView) return;

    if (e.code === 'Space' || e.key === 'ArrowRight') {
      e.preventDefault();
      // Find visible debugger's Next button
      const nextBtns = Array.from(activeView.querySelectorAll('.btn-next-prominent:not(:disabled)'));
      if (nextBtns.length > 0) {
        // Find the one closest to viewport or first
        const best = nextBtns.find(b => {
          const rect = b.getBoundingClientRect();
          return rect.top >= -50 && rect.bottom <= window.innerHeight + 100;
        }) || nextBtns[0];
        best.click();
      }
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      const prevBtns = Array.from(activeView.querySelectorAll('.ctrl-btn[id$="_prevBtn"]:not(:disabled)'));
      if (prevBtns.length > 0) {
        const best = prevBtns.find(b => {
          const rect = b.getBoundingClientRect();
          return rect.top >= -50 && rect.bottom <= window.innerHeight + 100;
        }) || prevBtns[0];
        best.click();
      }
    } else if (e.key === 'r' || e.key === 'R') {
      const resetBtns = Array.from(activeView.querySelectorAll('.ctrl-btn[id$="_resetBtn"]'));
      if (resetBtns.length > 0) {
        const best = resetBtns.find(b => {
          const rect = b.getBoundingClientRect();
          return rect.top >= -50 && rect.bottom <= window.innerHeight + 100;
        }) || resetBtns[0];
        best.click();
      }
    }
  });

});
