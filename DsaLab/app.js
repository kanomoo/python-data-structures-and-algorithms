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
