/**
 * DsaLab Interactive Visualizers Engine
 * Generates step-by-step snapshots and renders high-fidelity SVG/Canvas animations.
 */

window.DsaVisualizers = (function () {
  'use strict';

  // ========================================================
  // 1. Singly Linked List Visualizer
  // ========================================================
  function createLinkedListSteps(initialData) {
    const steps = [];
    let list = JSON.parse(JSON.stringify(initialData || []));

    steps.push({
      line: 14,
      explanation: 'สถานะเริ่มต้น: รายการเชื่อมโยง (Singly Linked List) พร้อมข้อมูลนักศึกษา 4 คน',
      vars: { head: list[0] ? list[0].id : 'None', size: list.length },
      visualData: {
        nodes: JSON.parse(JSON.stringify(list)),
        headIdx: 0,
        currentIdx: -1,
        prevIdx: -1,
        deletedIdx: -1
      }
    });

    const targetId = '612045';
    let prev = -1;
    let curr = 0;

    steps.push({
      line: 42,
      explanation: `เริ่มค้นหาเพื่อลบ: targetId = "${targetId}" | ตั้ง curr = head (ตำแหน่งที่ 0)`,
      vars: { curr: list[0].id, prev: 'None', target: targetId },
      visualData: {
        nodes: JSON.parse(JSON.stringify(list)),
        headIdx: 0,
        currentIdx: 0,
        prevIdx: -1
      }
    });

    while (curr < list.length && list[curr].id !== targetId) {
      prev = curr;
      curr++;
      steps.push({
        line: 44,
        explanation: `curr.student_id ("${list[prev].id}") ไม่ตรงกับเป้าหมาย -> เลื่อน prev = curr, curr = curr.next`,
        vars: { curr: list[curr].id, prev: list[prev].id, target: targetId },
        visualData: {
          nodes: JSON.parse(JSON.stringify(list)),
          headIdx: 0,
          currentIdx: curr,
          prevIdx: prev
        }
      });
    }

    if (curr < list.length && list[curr].id === targetId) {
      steps.push({
        line: 48,
        explanation: `🎉 พบโหนดเป้าหมาย! curr.student_id == "${targetId}" (${list[curr].name}) เตรียมปลดพอยน์เตอร์`,
        vars: { curr: list[curr].id, prev: list[prev].id, match: true },
        visualData: {
          nodes: JSON.parse(JSON.stringify(list)),
          headIdx: 0,
          currentIdx: curr,
          prevIdx: prev,
          highlightTarget: curr
        }
      });

      steps.push({
        line: 52,
        explanation: `สั่ง prev.next = curr.next: ข้ามโหนด "${targetId}" (${list[curr].name}) โหนดถูกตัดออกจาก List แล้ว!`,
        vars: { prev_next: list[curr + 1] ? list[curr + 1].id : 'None', size: list.length - 1 },
        visualData: {
          nodes: JSON.parse(JSON.stringify(list)),
          headIdx: 0,
          currentIdx: -1,
          prevIdx: prev,
          deletedIdx: curr
        }
      });

      list.splice(curr, 1);

      steps.push({
        line: 54,
        explanation: `ลบข้อมูลสำเร็จ! ปัจจุบัน Linked List เหลือทั้งหมด ${list.length} โหนด`,
        vars: { head: list[0].id, size: list.length },
        visualData: {
          nodes: JSON.parse(JSON.stringify(list)),
          headIdx: 0,
          currentIdx: -1,
          prevIdx: -1
        }
      });
    }

    return steps;
  }

  function renderLinkedList(container, visualData) {
    const { nodes, headIdx, currentIdx, prevIdx, deletedIdx, highlightTarget } = visualData;
    if (!nodes || nodes.length === 0) {
      container.innerHTML = '<div class="viz-empty-msg">Linked List ว่างเปล่า (Head = None)</div>';
      return;
    }

    let html = '<div class="ll-container">';
    nodes.forEach((node, idx) => {
      let cardClass = 'll-node-card';
      if (idx === currentIdx) cardClass += ' is-curr';
      if (idx === prevIdx) cardClass += ' is-prev';
      if (idx === deletedIdx) cardClass += ' is-deleted';
      if (idx === highlightTarget) cardClass += ' is-target';

      let badges = '';
      if (idx === headIdx && idx !== deletedIdx) badges += '<span class="ll-badge head">HEAD</span>';
      if (idx === currentIdx) badges += '<span class="ll-badge curr">CURR (p)</span>';
      if (idx === prevIdx) badges += '<span class="ll-badge prev">PREV</span>';
      if (idx === nodes.length - 1 && idx !== deletedIdx) badges += '<span class="ll-badge tail">TAIL</span>';

      html += `
        <div class="ll-node-wrapper">
          <div class="ll-badges-bar">${badges}</div>
          <div class="${cardClass}">
            <div class="ll-node-header">
              <span class="ll-id">#${node.id}</span>
              <span class="ll-gpa">GPA ${node.gpa}</span>
            </div>
            <div class="ll-name">${node.name}</div>
            <div class="ll-pointer-slot">
              <span>next</span>
              <span class="pointer-dot">●</span>
            </div>
          </div>
        </div>
      `;

      if (idx < nodes.length - 1) {
        html += `
          <div class="ll-arrow ${idx === prevIdx && deletedIdx !== -1 ? 'relinking' : ''}">
            <svg width="40" height="24" viewBox="0 0 40 24">
              <line x1="0" y1="12" x2="32" y2="12" stroke="currentColor" stroke-width="2.5" />
              <polyline points="26,6 32,12 26,18" fill="none" stroke="currentColor" stroke-width="2.5" />
            </svg>
          </div>
        `;
      } else {
        html += `
          <div class="ll-null">
            <span class="null-text">None</span>
          </div>
        `;
      }
    });
    html += '</div>';
    container.innerHTML = html;
  }

  // ========================================================
  // 2. Circular Queue Visualizer
  // ========================================================
  function createQueueSteps() {
    const steps = [];
    const capacity = 6;
    let arr = [10, 20, 30, 40, null, null];
    let front = 0;
    let rear = 3;
    let size = 4;

    steps.push({
      line: 7,
      explanation: 'สถานะเริ่มต้นของ Queue: capacity=6, front=0, rear=3, size=4 (มีข้อมูล 10, 20, 30, 40)',
      vars: { front, rear, size, capacity },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'init' }
    });

    const deq1 = arr[front];
    arr[front] = null;
    front = (front + 1) % capacity;
    size--;
    steps.push({
      line: 30,
      explanation: `คำสั่ง dequeue(): นำข้อมูล ${deq1} ออกจากตำแหน่ง front (index 0) -> เลื่อน front = (0 + 1) % 6 = 1`,
      vars: { dequeued: deq1, front, rear, size },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'dequeue', deqIdx: 0, deqVal: deq1 }
    });

    const deq2 = arr[front];
    arr[front] = null;
    front = (front + 1) % capacity;
    size--;
    steps.push({
      line: 30,
      explanation: `คำสั่ง dequeue(): นำข้อมูล ${deq2} ออกจากตำแหน่ง front (index 1) -> เลื่อน front = (1 + 1) % 6 = 2`,
      vars: { dequeued: deq2, front, rear, size },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'dequeue', deqIdx: 1, deqVal: deq2 }
    });

    rear = (rear + 1) % capacity;
    arr[rear] = 50;
    size++;
    steps.push({
      line: 21,
      explanation: `คำสั่ง enqueue(50): เลื่อน rear = (3 + 1) % 6 = 4 -> ใส่ค่า 50 ที่ตำแหน่ง index 4`,
      vars: { enqueued: 50, front, rear, size },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'enqueue', enqIdx: rear }
    });

    rear = (rear + 1) % capacity;
    arr[rear] = 60;
    size++;
    steps.push({
      line: 21,
      explanation: `คำสั่ง enqueue(60): เลื่อน rear = (4 + 1) % 6 = 5 -> ใส่ค่า 60 ที่ตำแหน่ง index 5 (เต็มขอบขวา)`,
      vars: { enqueued: 60, front, rear, size },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'enqueue', enqIdx: rear }
    });

    rear = (rear + 1) % capacity;
    arr[rear] = 70;
    size++;
    steps.push({
      line: 21,
      explanation: `🔥 Circular Wrap-Around! enqueue(70): เลื่อน rear = (5 + 1) % 6 = 0 -> วนกลับมาใส่ที่ index 0!`,
      vars: { enqueued: 70, front, rear, size, circularWrap: true },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'enqueue', enqIdx: 0, circularWrap: true }
    });

    return steps;
  }

  function renderQueue(container, visualData) {
    const { arr, front, rear, size, capacity, op, enqIdx, deqIdx } = visualData;

    let html = `
      <div class="queue-meta-bar">
        <div class="q-stat"><span class="q-label">Capacity:</span> <b>${capacity}</b></div>
        <div class="q-stat"><span class="q-label">Size:</span> <b>${size}</b></div>
        <div class="q-stat"><span class="q-label">Front Index:</span> <b style="color:#06b6d4;">${front}</b></div>
        <div class="q-stat"><span class="q-label">Rear Index:</span> <b style="color:#a855f7;">${rear}</b></div>
      </div>
      <div class="queue-slots-grid">
    `;

    arr.forEach((val, idx) => {
      const isFront = idx === front && size > 0;
      const isRear = idx === rear && size > 0;
      const isEnq = idx === enqIdx;
      const isDeq = idx === deqIdx;

      let slotClass = 'q-slot';
      if (val !== null) slotClass += ' filled';
      if (isEnq) slotClass += ' just-enq';
      if (isDeq) slotClass += ' just-deq';

      let badges = '';
      if (isFront && isRear) badges += '<span class="q-badge both">F & R</span>';
      else {
        if (isFront) badges += '<span class="q-badge front">FRONT</span>';
        if (isRear) badges += '<span class="q-badge rear">REAR</span>';
      }

      html += `
        <div class="q-slot-wrapper">
          <div class="q-slot-badges">${badges}</div>
          <div class="${slotClass}">
            <span class="q-slot-val">${val !== null ? val : '—'}</span>
            <span class="q-slot-idx">[${idx}]</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    container.innerHTML = html;
  }

  // ========================================================
  // 3. Binary Search Tree (BST Deletion with 2 Children)
  // ========================================================
  function createBstSteps() {
    const steps = [];

    const t1 = {
      50: { val: 50, x: 260, y: 35, left: 30, right: 70 },
      30: { val: 30, x: 140, y: 95, left: 20, right: 40 },
      70: { val: 70, x: 380, y: 95, left: 60, right: 80 },
      20: { val: 20, x: 80, y: 155, left: null, right: null },
      40: { val: 40, x: 200, y: 155, left: null, right: null },
      60: { val: 60, x: 320, y: 155, left: null, right: 65 },
      80: { val: 80, x: 440, y: 155, left: null, right: null },
      65: { val: 65, x: 350, y: 215, left: null, right: null }
    };

    steps.push({
      line: 38,
      explanation: 'สถานะเริ่มต้น: ต้นไม้ BST มี 8 โหนด ต้องการลบโหนด 70 (ซึ่งมีลูก 2 ตัว: 60 และ 80)',
      vars: { root: 50, targetToDelete: 70 },
      visualData: { tree: JSON.parse(JSON.stringify(t1)), targetId: 70, successorId: null, phase: 'init' }
    });

    steps.push({
      line: 44,
      explanation: 'ค้นหาโหนด 70: เริ่มจาก Root 50 -> 70 > 50 เลี้ยวขวา -> พบโหนด 70!',
      vars: { current: 70, matchFound: true },
      visualData: { tree: JSON.parse(JSON.stringify(t1)), targetId: 70, searchPath: [50, 70], phase: 'found_target' }
    });

    steps.push({
      line: 56,
      explanation: 'โหนด 70 มีลูก 2 ตัว! เรียก find_min(node.right) เข้าไปในกิ่งขวาเพื่อหา In-order Successor',
      vars: { right_subtree_root: 80 },
      visualData: { tree: JSON.parse(JSON.stringify(t1)), targetId: 70, successorId: 80, phase: 'find_successor' }
    });

    steps.push({
      line: 58,
      explanation: 'พบ In-order Successor = 80 (ค่าน้อยที่สุดในกิ่งขวาของ 70)',
      vars: { successor: 80 },
      visualData: { tree: JSON.parse(JSON.stringify(t1)), targetId: 70, successorId: 80, phase: 'found_successor' }
    });

    const t2 = JSON.parse(JSON.stringify(t1));
    t2[70].val = 80;
    steps.push({
      line: 60,
      explanation: 'คัดลอกค่า Successor (80) มาทับที่โหนด 70 -> โหนด 70 เปลี่ยนค่าเป็น 80 เรียบร้อย',
      vars: { node_key: 80, old_val: 70 },
      visualData: { tree: JSON.parse(JSON.stringify(t2)), targetId: 70, successorId: 80, phase: 'copied_val' }
    });

    const t3 = JSON.parse(JSON.stringify(t2));
    delete t3[80];
    t3[70].right = null;
    steps.push({
      line: 61,
      explanation: 'สั่งลบโหนด 80 เดิมในกิ่งขวาออก (เนื่องจากเป็น Leaf Node ตัดทิ้งได้ทันที) -> ได้ BST ที่ถูกต้องสมบูรณ์!',
      vars: { deleted: 80, bst_valid: true },
      visualData: { tree: JSON.parse(JSON.stringify(t3)), targetId: null, successorId: null, phase: 'complete' }
    });

    return steps;
  }

  function renderBst(container, visualData) {
    const { tree, targetId, successorId, searchPath, phase } = visualData;

    let svgHtml = '<svg class="bst-svg" viewBox="0 0 520 270">';

    Object.values(tree).forEach(node => {
      if (node.left && tree[node.left]) {
        const leftNode = tree[node.left];
        svgHtml += `<line x1="${node.x}" y1="${node.y}" x2="${leftNode.x}" y2="${leftNode.y}" class="bst-edge" />`;
      }
      if (node.right && tree[node.right]) {
        const rightNode = tree[node.right];
        svgHtml += `<line x1="${node.x}" y1="${node.y}" x2="${rightNode.x}" y2="${rightNode.y}" class="bst-edge" />`;
      }
    });

    Object.values(tree).forEach(node => {
      let nodeClass = 'bst-node-circle';
      let label = '';
      if (node.val === 70 || (targetId && node.val === tree[targetId]?.val && phase === 'found_target')) {
        nodeClass += ' is-target';
        label = 'Target';
      }
      if (successorId && node.val === successorId) {
        nodeClass += ' is-successor';
        label = 'Successor';
      }
      if (searchPath && searchPath.includes(node.val)) {
        nodeClass += ' on-path';
      }

      svgHtml += `
        <g class="bst-node-group" transform="translate(${node.x}, ${node.y})">
          <circle r="20" class="${nodeClass}"></circle>
          <text text-anchor="middle" dy="5" class="bst-node-text">${node.val}</text>
          ${label ? `<text text-anchor="middle" dy="-26" class="bst-node-label">${label}</text>` : ''}
        </g>
      `;
    });

    svgHtml += '</svg>';
    container.innerHTML = svgHtml;
  }

  // ========================================================
  // 4. Binary Min-Heap Visualizer
  // ========================================================
  function createHeapSteps() {
    const steps = [];
    let heap = [0, 10, 12, 20, 14, 16, 25, 30, 22];

    steps.push({
      line: 5,
      explanation: 'สถานะเริ่มต้น: Binary Min-Heap ใน Array [10, 12, 20, 14, 16, 25, 30, 22] (ขนาด = 8)',
      vars: { size: heap.length - 1, min: heap[1] },
      visualData: { heap: [...heap], activeIdx: -1, parentIdx: -1, op: 'init' }
    });

    heap.push(8);
    let i = heap.length - 1;
    steps.push({
      line: 9,
      explanation: `แทรก 8: นำค่า 8 ใส่ที่ตำแหน่งท้ายสุด index ${i} -> เตรียมตรวจสอบ Percolate Up กับ Parent`,
      vars: { inserted: 8, index: i, parent: Math.floor(i / 2) },
      visualData: { heap: [...heap], activeIdx: i, parentIdx: Math.floor(i / 2), op: 'insert' }
    });

    let p = Math.floor(i / 2);
    steps.push({
      line: 15,
      explanation: `เปรียบเทียบ: heap[${i}] (8) < heap[${p}] (${heap[p]}) -> สลับตำแหน่งขึ้นไป!`,
      vars: { swap: `8 with ${heap[p]}` },
      visualData: { heap: [...heap], activeIdx: i, parentIdx: p, op: 'swap' }
    });

    let temp = heap[i];
    heap[i] = heap[p];
    heap[p] = temp;
    i = p;
    p = Math.floor(i / 2);

    steps.push({
      line: 15,
      explanation: `เปรียบเทียบต่อ: ตอนนี้ 8 อยู่ที่ index ${i} | Parent คือ index ${p} (ค่า ${heap[p]}) -> 8 < 12 สลับอีกครั้ง!`,
      vars: { index: i, parent: p },
      visualData: { heap: [...heap], activeIdx: i, parentIdx: p, op: 'swap' }
    });

    temp = heap[i];
    heap[i] = heap[p];
    heap[p] = temp;
    i = p;
    p = Math.floor(i / 2);

    steps.push({
      line: 15,
      explanation: `เปรียบเทียบกับ Root: 8 อยู่ที่ index ${i} | Parent คือ Root index 1 (ค่า ${heap[1]}) -> 8 < 10 สลับขึ้นเป็นรากใหม่!`,
      vars: { index: i, parent: 1 },
      visualData: { heap: [...heap], activeIdx: i, parentIdx: 1, op: 'swap' }
    });

    temp = heap[i];
    heap[i] = heap[1];
    heap[1] = temp;

    steps.push({
      line: 18,
      explanation: `🎉 Percolate Up สำเร็จ: 8 กลายเป็น Min Root ตัวใหม่ของ Heap!`,
      vars: { new_min: 8, root: heap[1] },
      visualData: { heap: [...heap], activeIdx: 1, parentIdx: -1, op: 'complete' }
    });

    return steps;
  }

  function renderHeap(container, visualData) {
    const { heap, activeIdx, parentIdx } = visualData;

    let html = '<div class="heap-dual-container">';

    html += '<div class="heap-array-view"><div class="heap-view-title">📋 Array Index View [1 .. n]</div><div class="heap-array-slots">';
    for (let idx = 1; idx < heap.length; idx++) {
      let slotClass = 'h-slot';
      if (idx === activeIdx) slotClass += ' is-active';
      if (idx === parentIdx) slotClass += ' is-parent';

      let badge = '';
      if (idx === activeIdx) badge = '<span class="h-badge act">Active</span>';
      if (idx === parentIdx) badge = '<span class="h-badge par">Parent</span>';

      html += `
        <div class="h-slot-wrapper">
          ${badge}
          <div class="${slotClass}">
            <span class="h-val">${heap[idx]}</span>
            <span class="h-idx">[${idx}]</span>
          </div>
        </div>
      `;
    }
    html += '</div></div>';

    const coords = [
      null,
      { x: 260, y: 35 },
      { x: 140, y: 90 },
      { x: 380, y: 90 },
      { x: 80, y: 145 },
      { x: 200, y: 145 },
      { x: 320, y: 145 },
      { x: 440, y: 145 },
      { x: 50, y: 200 },
      { x: 110, y: 200 }
    ];

    html += '<div class="heap-tree-view"><div class="heap-view-title">🌲 Tree Structure View</div><svg class="heap-svg" viewBox="0 0 520 230">';

    for (let i = 1; i < heap.length; i++) {
      const left = i * 2;
      const right = i * 2 + 1;
      if (left < heap.length && coords[left]) {
        html += `<line x1="${coords[i].x}" y1="${coords[i].y}" x2="${coords[left].x}" y2="${coords[left].y}" class="bst-edge" />`;
      }
      if (right < heap.length && coords[right]) {
        html += `<line x1="${coords[i].x}" y1="${coords[i].y}" x2="${coords[right].x}" y2="${coords[right].y}" class="bst-edge" />`;
      }
    }

    for (let i = 1; i < heap.length; i++) {
      if (!coords[i]) continue;
      let nodeClass = 'bst-node-circle';
      if (i === activeIdx) nodeClass += ' is-target';
      if (i === parentIdx) nodeClass += ' is-successor';

      html += `
        <g transform="translate(${coords[i].x}, ${coords[i].y})">
          <circle r="18" class="${nodeClass}"></circle>
          <text text-anchor="middle" dy="5" class="bst-node-text">${heap[i]}</text>
          <text text-anchor="middle" dy="28" class="bst-node-label" style="font-size:10px;">i=${i}</text>
        </g>
      `;
    }

    html += '</svg></div></div>';
    container.innerHTML = html;
  }

  // ========================================================
  // 5. Sorting Algorithms Visualizer (Test Program 2)
  // ========================================================
  function createSortingSteps(initialArr) {
    const steps = [];
    const arr = [...(initialArr || [45, 12, 89, 34, 70, 23, 56, 18])];
    const n = arr.length;
    let comps = 0;
    let swaps = 0;

    steps.push({
      line: 6,
      explanation: 'ข้อมูลเริ่มต้น: [45, 12, 89, 34, 70, 23, 56, 18] พร้อมเริ่ม Bubble Sort',
      vars: { comparisons: 0, swaps: 0, n },
      visualData: { arr: [...arr], compIdxA: -1, compIdxB: -1, swapped: false, comps: 0, swaps: 0, sortedIdx: n }
    });

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        comps++;
        const shouldSwap = arr[j] > arr[j + 1];

        steps.push({
          line: 10,
          explanation: `เปรียบเทียบ arr[${j}] (${arr[j]}) กับ arr[${j + 1}] (${arr[j + 1]}) -> ${shouldSwap ? 'มากกว่า สลับที่!' : 'ถูกต้องแล้ว ไม่ต้องสลับ'}`,
          vars: { i, j, comp: `${arr[j]} > ${arr[j+1]}`, comparisons: comps, swaps },
          visualData: { arr: [...arr], compIdxA: j, compIdxB: j + 1, willSwap: shouldSwap, comps, swaps, sortedIdx: n - i }
        });

        if (shouldSwap) {
          const temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
          swaps++;

          steps.push({
            line: 12,
            explanation: `สลับค่าสำเร็จ! arr[${j}] กลายเป็น ${arr[j]} และ arr[${j + 1}] กลายเป็น ${arr[j + 1]}`,
            vars: { swaps, comparisons: comps },
            visualData: { arr: [...arr], compIdxA: j, compIdxB: j + 1, swapped: true, comps, swaps, sortedIdx: n - i }
          });
        }
      }
    }

    steps.push({
      line: 17,
      explanation: `🎉 จัดเรียงข้อมูลเรียบร้อยสมบูรณ์! ผลลัพธ์: [${arr.join(', ')}] (เปรียบเทียบ ${comps} ครั้ง, สลับ ${swaps} ครั้ง)`,
      vars: { total_comps: comps, total_swaps: swaps, is_sorted: true },
      visualData: { arr: [...arr], compIdxA: -1, compIdxB: -1, comps, swaps, sortedIdx: 0 }
    });

    return steps;
  }

  function renderSorting(container, visualData) {
    const { arr, compIdxA, compIdxB, willSwap, swapped, comps, swaps, sortedIdx } = visualData;
    const maxVal = Math.max(...arr, 90);

    let html = `
      <div class="sorting-meta-bar">
        <div class="sort-stat"><span>การเปรียบเทียบ (Comps):</span> <b>${comps}</b></div>
        <div class="sort-stat"><span>การสลับ (Swaps):</span> <b style="color:#f43f5e;">${swaps}</b></div>
      </div>
      <div class="sorting-bars-container">
    `;

    arr.forEach((val, idx) => {
      const heightPercent = Math.max(15, Math.round((val / maxVal) * 100));
      let barClass = 'sort-bar';

      if (idx === compIdxA || idx === compIdxB) {
        if (swapped) barClass += ' swapped';
        else if (willSwap) barClass += ' will-swap';
        else barClass += ' comparing';
      } else if (idx >= sortedIdx) {
        barClass += ' sorted';
      }

      html += `
        <div class="sort-bar-wrapper">
          <span class="bar-val">${val}</span>
          <div class="${barClass}" style="height: ${heightPercent}%;"></div>
          <span class="bar-idx">[${idx}]</span>
        </div>
      `;
    });

    html += '</div>';
    container.innerHTML = html;
  }

  // ========================================================
  // 6. Dijkstra Shortest Path Visualizer (Assignment 4)
  // ========================================================
  function createDijkstraSteps() {
    const steps = [];

    const tableInit = {
      v1: { known: true, dv: 0, pv: '-' },
      v2: { known: false, dv: 2, pv: 'v1' },
      v3: { known: false, dv: '∞', pv: '-' },
      v4: { known: false, dv: 1, pv: 'v1' },
      v5: { known: false, dv: '∞', pv: '-' },
      v6: { known: false, dv: '∞', pv: '-' },
      v7: { known: false, dv: '∞', pv: '-' }
    };

    steps.push({
      line: 6,
      explanation: 'รอบที่ 0: จุดเริ่มต้น v1 | ตั้งค่า dist[v1] = 0, จุดอื่นๆ = ∞, Known = True สำหรับ v1',
      vars: { current: 'v1', known: ['v1'] },
      visualData: {
        table: JSON.parse(JSON.stringify(tableInit)),
        currentV: 'v1',
        knownNodes: ['v1'],
        highlightEdges: ['v1-v2', 'v1-v4']
      }
    });

    const t1 = JSON.parse(JSON.stringify(tableInit));
    t1.v4.known = true;
    t1.v3.dv = 3; t1.v3.pv = 'v4';
    t1.v5.dv = 3; t1.v5.pv = 'v4';
    t1.v6.dv = 9; t1.v6.pv = 'v4';
    t1.v7.dv = 5; t1.v7.pv = 'v4';

    steps.push({
      line: 14,
      explanation: 'รอบที่ 1: เลือก v4 (Known=False และ dv=1 น้อยสุด) -> ปรับระยะทางเพื่อนบ้าน v3(3), v5(3), v6(9), v7(5)',
      vars: { current: 'v4', known: ['v1', 'v4'] },
      visualData: {
        table: t1,
        currentV: 'v4',
        knownNodes: ['v1', 'v4'],
        highlightEdges: ['v1-v4', 'v4-v3', 'v4-v5', 'v4-v7']
      }
    });

    const t2 = JSON.parse(JSON.stringify(t1));
    t2.v2.known = true;

    steps.push({
      line: 14,
      explanation: 'รอบที่ 2: เลือก v2 (dv=2) -> ตรวจสอบทางเชื่อมไปยัง v4 และ v5 แต่ระยะทางเดิมสั้นกว่าจึงไม่เปลี่ยน',
      vars: { current: 'v2', known: ['v1', 'v4', 'v2'] },
      visualData: {
        table: t2,
        currentV: 'v2',
        knownNodes: ['v1', 'v4', 'v2'],
        highlightEdges: ['v1-v2']
      }
    });

    const t3 = JSON.parse(JSON.stringify(t2));
    t3.v3.known = true;
    t3.v6.dv = 8; t3.v6.pv = 'v3';

    steps.push({
      line: 14,
      explanation: 'รอบที่ 3: เลือก v3 (dv=3) -> ปรับระยะทาง v6 จาก 9 ลดเหลือ 8 (เดินผ่าน v3)!',
      vars: { current: 'v3', known: ['v1', 'v4', 'v2', 'v3'] },
      visualData: {
        table: t3,
        currentV: 'v3',
        knownNodes: ['v1', 'v4', 'v2', 'v3'],
        highlightEdges: ['v4-v3', 'v3-v6']
      }
    });

    const t4 = JSON.parse(JSON.stringify(t3));
    t4.v5.known = true;

    steps.push({
      line: 14,
      explanation: 'รอบที่ 4: เลือก v5 (dv=3) -> ตรวจสอบเส้นทางไป v7 (3+6=9 > 5 คงเดิม)',
      vars: { current: 'v5', known: ['v1', 'v4', 'v2', 'v3', 'v5'] },
      visualData: {
        table: t4,
        currentV: 'v5',
        knownNodes: ['v1', 'v4', 'v2', 'v3', 'v5'],
        highlightEdges: ['v4-v5']
      }
    });

    const t5 = JSON.parse(JSON.stringify(t4));
    t5.v7.known = true;
    t5.v6.dv = 6; t5.v6.pv = 'v7';

    steps.push({
      line: 14,
      explanation: 'รอบที่ 5: เลือก v7 (dv=5) -> ปรับระยะทาง v6 จาก 8 ลดเหลือ 6 (เดินผ่าน v7)!',
      vars: { current: 'v7', known: ['v1', 'v4', 'v2', 'v3', 'v5', 'v7'] },
      visualData: {
        table: t5,
        currentV: 'v7',
        knownNodes: ['v1', 'v4', 'v2', 'v3', 'v5', 'v7'],
        highlightEdges: ['v4-v7', 'v7-v6']
      }
    });

    const t6 = JSON.parse(JSON.stringify(t5));
    t6.v6.known = true;

    steps.push({
      line: 20,
      explanation: '🎉 คำนวณ Dijkstra เสร็จสิ้นครบทุกจุดยอด! ได้วิถีสั้นสุดจาก v1 ไปยังทุกโหนดใน Assignment 4 เรียบร้อย',
      vars: { all_known: true },
      visualData: {
        table: t6,
        currentV: 'v6',
        knownNodes: ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7'],
        highlightEdges: ['v1-v4', 'v1-v2', 'v4-v3', 'v4-v5', 'v4-v7', 'v7-v6']
      }
    });

    return steps;
  }

  function renderDijkstra(container, visualData) {
    const { table, currentV, knownNodes, highlightEdges } = visualData;

    const nodeCoords = {
      v1: { x: 70, y: 110 },
      v2: { x: 190, y: 40 },
      v3: { x: 190, y: 180 },
      v4: { x: 260, y: 110 },
      v5: { x: 380, y: 40 },
      v6: { x: 450, y: 110 },
      v7: { x: 380, y: 180 }
    };

    const graphEdges = [
      { u: 'v1', v: 'v2', w: 2 },
      { u: 'v1', v: 'v4', w: 1 },
      { u: 'v2', v: 'v4', w: 3 },
      { u: 'v2', v: 'v5', w: 10 },
      { u: 'v3', v: 'v1', w: 4 },
      { u: 'v3', v: 'v6', w: 5 },
      { u: 'v4', v: 'v3', w: 2 },
      { u: 'v4', v: 'v5', w: 2 },
      { u: 'v4', v: 'v6', w: 8 },
      { u: 'v4', v: 'v7', w: 4 },
      { u: 'v5', v: 'v7', w: 6 },
      { u: 'v7', v: 'v6', w: 1 }
    ];

    let html = '<div class="dijkstra-dual-container">';

    html += '<div class="dijkstra-graph-view"><svg class="dijkstra-svg" viewBox="0 0 520 220">';

    graphEdges.forEach(e => {
      const u = nodeCoords[e.u];
      const v = nodeCoords[e.v];
      const edgeKey1 = `${e.u}-${e.v}`;
      const isHighlighted = highlightEdges && highlightEdges.includes(edgeKey1);
      const edgeClass = isHighlighted ? 'dijk-edge highlighted' : 'dijk-edge';

      const mx = (u.x + v.x) / 2;
      const my = (u.y + v.y) / 2 - 4;

      html += `
        <line x1="${u.x}" y1="${u.y}" x2="${v.x}" y2="${v.y}" class="${edgeClass}" />
        <rect x="${mx - 8}" y="${my - 8}" width="16" height="14" rx="3" fill="#0f172a" />
        <text x="${mx}" y="${my + 3}" text-anchor="middle" class="dijk-edge-w">${e.w}</text>
      `;
    });

    Object.keys(nodeCoords).forEach(id => {
      const pos = nodeCoords[id];
      const isKnown = knownNodes && knownNodes.includes(id);
      const isCurr = id === currentV;

      let nodeClass = 'dijk-node';
      if (isCurr) nodeClass += ' is-curr';
      else if (isKnown) nodeClass += ' is-known';

      html += `
        <g transform="translate(${pos.x}, ${pos.y})">
          <circle r="18" class="${nodeClass}"></circle>
          <text text-anchor="middle" dy="5" class="dijk-node-text">${id}</text>
        </g>
      `;
    });

    html += '</svg></div>';

    html += `
      <div class="dijkstra-table-view">
        <table class="dijk-table">
          <thead>
            <tr>
              <th>Vertex</th>
              <th>Known</th>
              <th>d<sub>v</sub></th>
              <th>p<sub>v</sub></th>
            </tr>
          </thead>
          <tbody>
    `;

    Object.keys(table).forEach(v => {
      const row = table[v];
      const isCurr = v === currentV;
      html += `
        <tr class="${isCurr ? 'curr-row' : ''}">
          <td><b>${v}</b></td>
          <td><span class="known-tag ${row.known ? 'true' : 'false'}">${row.known ? 'True' : 'False'}</span></td>
          <td><b>${row.dv}</b></td>
          <td>${row.pv}</td>
        </tr>
      `;
    });

    html += '</tbody></table></div></div>';
    container.innerHTML = html;
  }

  // ========================================================
  // 7. Stack Postfix Evaluator Visualizer
  // ========================================================
  function createStackSteps() {
    const steps = [];
    const tokens = ['5', '3', '+', '8', '2', '-', '*', '4', '/'];
    let stack = [];

    steps.push({
      line: 3,
      explanation: 'เริ่มต้นคำนวณ Postfix: โทเค็นทั้งหมด = [5, 3, +, 8, 2, -, *, 4, /]',
      vars: { stack: [], token: 'none' },
      visualData: { stack: [], currentToken: null, op: 'init' }
    });

    tokens.forEach(tok => {
      if (!isNaN(tok)) {
        stack.push(Number(tok));
        steps.push({
          line: 9,
          explanation: `อ่านได้ตัวเลข '${tok}' -> Push ลงใน Stack`,
          vars: { pushed: tok, stack: [...stack] },
          visualData: { stack: [...stack], currentToken: tok, op: 'push' }
        });
      } else {
        const b = stack.pop();
        const a = stack.pop();
        let res = 0;
        if (tok === '+') res = a + b;
        else if (tok === '-') res = a - b;
        else if (tok === '*') res = a * b;
        else if (tok === '/') res = Math.floor(a / b);

        steps.push({
          line: 13,
          explanation: `อ่านได้เครื่องหมาย '${tok}' -> Pop ${b} และ ${a} ออกมาคำนวณ: ${a} ${tok} ${b} = ${res}`,
          vars: { operator: tok, operandA: a, operandB: b, result: res },
          visualData: { stack: [...stack], currentToken: tok, op: 'calc', calcDesc: `${a} ${tok} ${b} = ${res}` }
        });

        stack.push(res);
        steps.push({
          line: 18,
          explanation: `Push ผลลัพธ์ ${res} กลับลงใน Stack`,
          vars: { pushed: res, stack: [...stack] },
          visualData: { stack: [...stack], currentToken: tok, op: 'push' }
        });
      }
    });

    steps.push({
      line: 22,
      explanation: `🎉 สิ้นสุดนิพจน์! ค่าสุดท้ายใน Stack คือผลลัพธ์: ${stack[0]}`,
      vars: { final_answer: stack[0] },
      visualData: { stack: [...stack], currentToken: null, op: 'complete' }
    });

    return steps;
  }

  function renderStack(container, visualData) {
    const { stack, currentToken, calcDesc } = visualData;

    let html = `
      <div class="stack-meta-bar">
        <div class="s-token">โทเค็นปัจจุบัน: <span class="tok-badge">${currentToken || '—'}</span></div>
        ${calcDesc ? `<div class="s-calc">${calcDesc}</div>` : ''}
      </div>
      <div class="stack-bucket-wrapper">
        <div class="stack-bucket">
    `;

    if (stack.length === 0) {
      html += '<div class="stack-empty">Stack ว่างเปล่า</div>';
    } else {
      for (let i = stack.length - 1; i >= 0; i--) {
        const isTop = i === stack.length - 1;
        html += `
          <div class="stack-item ${isTop ? 'is-top' : ''}">
            <span class="stack-val">${stack[i]}</span>
            ${isTop ? '<span class="stack-top-badge">TOP</span>' : ''}
          </div>
        `;
      }
    }

    html += '</div><div class="stack-base"></div></div>';
    container.innerHTML = html;
  }

  return {
    getStepsForExercise: function (exId) {
      if (exId === 'assign1_linkedlist') return createLinkedListSteps(window.DSA_EXERCISES[0].defaultData);
      if (exId === 'test1_queue') return createQueueSteps();
      if (exId === 'lecture5_bst_delete') return createBstSteps();
      if (exId === 'assign3_heap') return createHeapSteps();
      if (exId === 'test2_sorting') return createSortingSteps();
      if (exId === 'assign4_dijkstra') return createDijkstraSteps();
      if (exId === 'stack_postfix') return createStackSteps();
      return createLinkedListSteps();
    },

    renderVisualizer: function (container, exType, visualData) {
      if (!container || !visualData) return;
      if (exType === 'linked_list') renderLinkedList(container, visualData);
      else if (exType === 'queue') renderQueue(container, visualData);
      else if (exType === 'bst') renderBst(container, visualData);
      else if (exType === 'heap') renderHeap(container, visualData);
      else if (exType === 'sorting') renderSorting(container, visualData);
      else if (exType === 'dijkstra') renderDijkstra(container, visualData);
      else if (exType === 'stack') renderStack(container, visualData);
      else renderLinkedList(container, visualData);
    }
  };
})();
