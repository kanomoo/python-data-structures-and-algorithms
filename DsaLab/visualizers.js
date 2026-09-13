/**
 * DSA Lab Studio — High-Fidelity Interactive Visualizers Engine
 * Features fully dynamic simulation engines for:
 * 1. Binary Heap (Min & Max with Percolate Up/Down, Dual Tree & 1-Based Array)
 * 2. Binary Search Tree (Dynamic Insert, Search, Deletion Cases 0/1/2, Traversals)
 * 3. Hash Table & Collision Resolution (Separate Chaining vs Linear Probing with Load Factor)
 * 4. Infix to Postfix Converter with Operator Stack
 * 5. Singly Linked List, Circular Array Queue, Sorting Algorithms, Dijkstra
 */

window.DsaVisualizers = (function () {
  'use strict';

  // =========================================================================
  // 1. DYNAMIC BINARY HEAP ENGINE (Min-Heap & Max-Heap) — Exams/Heap.py
  // =========================================================================
  let heapType = 'min'; // 'min' | 'max'
  // 1-indexed array. Index 0 is sentinel None. Default preset matches Exams/Heap.py
  let heapArray = [0, 13, 14, 16, 19, 21, 19, 68, 65, 26, 32, 31];

  function getHeapState() {
    return [...heapArray];
  }

  function setHeapState(arr) {
    heapArray = [...arr];
  }

  function resetHeapToExamPreset() {
    heapType = 'min';
    heapArray = [0, 13, 14, 16, 19, 21, 19, 68, 65, 26, 32, 31];
    return createHeapDefaultSteps('รีเซ็ตกลับเป็นข้อมูลตัวอย่างตามข้อสอบ Exams/Heap.py สำเร็จ');
  }

  function createHeapDefaultSteps(customMsg) {
    const steps = [];
    const h = [...heapArray];
    const n = h.length - 1;
    const isMin = heapType === 'min';

    steps.push({
      line: 3,
      explanation: customMsg || `📌 <b>Binary ${isMin ? 'Min-Heap' : 'Max-Heap'}</b>: โครงสร้าง Complete Binary Tree ขนาด <b>${n}</b> โหนด (ราก Root = <b>${n > 0 ? h[1] : 'ว่าง'}</b>)`,
      vars: {
        type: isMin ? 'Min-Heap' : 'Max-Heap',
        size: n,
        root_value: n > 0 ? h[1] : 'None',
        array_slice: n > 0 ? h.slice(1).join(', ') : 'Empty'
      },
      visualData: {
        heap: [...h],
        heapType,
        holeIdx: -1,
        parentIdx: -1,
        childIdx: -1,
        activeIdx: n > 0 ? 1 : -1,
        op: 'init',
        highlightIndices: []
      }
    });

    return steps;
  }

  function createHeapInsertSteps(val) {
    const num = parseInt(val, 10);
    if (isNaN(num)) return createHeapDefaultSteps();

    const steps = [];
    let h = [...heapArray];
    const isMin = heapType === 'min';

    if (h.length >= 24) {
      steps.push({
        line: 6,
        explanation: '⚠️ <b>ความจุเต็ม</b>: ไม่สามารถแทรกโหนดเพิ่มได้ (จำกัดเพื่อความคมชัดของภาพ 23 โหนด)',
        vars: { size: h.length - 1 },
        visualData: { heap: [...h], heapType, holeIdx: -1, parentIdx: -1, activeIdx: -1, op: 'full' }
      });
      return steps;
    }

    // Step 1: Place hole at end of array
    h.push(num);
    let hole = h.length - 1;
    let parent = Math.floor(hole / 2);

    steps.push({
      line: 7, // self.currentSize += 1; hole = self.currentSize
      explanation: `📥 <b>Insert(${num}) สเต็ปที่ 1</b>: เพิ่มความจุ currentSize += 1 -> สร้างช่องว่าง <code>hole</code> ที่ท้ายอาร์เรย์ index <b>${hole}</b> เตรียมเริ่ม <b>Percolate Up</b> ตรวจสอบกับโหนดแม่ Parent index <b>${parent}</b> (ค่า <b>${h[parent]}</b>)`,
      vars: {
        insert_val: num,
        hole_index: hole,
        parent_index: parent,
        'heap[parent]': h[parent]
      },
      visualData: {
        heap: [...h],
        heapType,
        holeIdx: hole,
        parentIdx: parent,
        activeIdx: hole,
        op: 'insert_start',
        val: num
      }
    });

    // Step 2: Percolate Up loop
    while (hole > 1) {
      let p = Math.floor(hole / 2);
      const violates = isMin ? (num < h[p]) : (num > h[p]);
      const conditionStr = isMin ? `${num} < ${h[p]}` : `${num} > ${h[p]}`;

      if (violates) {
        steps.push({
          line: 9, // while hole > 1 and x < self.array[hole // 2]:
          explanation: `🔍 <b>ตรวจเงื่อนไข Percolate Up</b>: <code>${conditionStr}</code> เป็น <b>จริง (True)</b> -> ค่าใหม่ ${num} ${isMin ? 'น้อยกว่า' : 'มากกว่า'} โหนดแม่ (${h[p]}) จึงต้องเลื่อนแม่ลงมาที่ index ${hole}`,
          vars: {
            hole: hole,
            parent: p,
            comparison: `${conditionStr} -> True`,
            action: `Shift parent ${h[p]} down to index ${hole}`
          },
          visualData: {
            heap: [...h],
            heapType,
            holeIdx: hole,
            parentIdx: p,
            activeIdx: hole,
            op: 'compare_up',
            val: num
          }
        });

        // Shift parent down
        h[hole] = h[p];
        hole = p;

        steps.push({
          line: 11, // self.array[hole] = self.array[hole // 2]; hole //= 2
          explanation: `⬆️ <b>เลื่อนช่องว่างขึ้น</b>: ช่องว่าง hole ขยับขึ้นไปที่ index <b>${hole}</b> -> คำนวณ Parent ถัดไป: <code>⌊${hole} / 2⌋ = ${Math.floor(hole / 2)}</code>`,
          vars: {
            new_hole: hole,
            next_parent: Math.floor(hole / 2),
            current_array: h.slice(1).join(', ')
          },
          visualData: {
            heap: [...h],
            heapType,
            holeIdx: hole,
            parentIdx: Math.floor(hole / 2),
            activeIdx: hole,
            op: 'shifted_up',
            val: num
          }
        });
      } else {
        steps.push({
          line: 9,
          explanation: `🛑 <b>เงื่อนไขสมบูรณ์</b>: <code>${conditionStr}</code> เป็น <b>เท็จ (False)</b> -> ค่าใหม่ ${num} ไม่ละเมิดกฎของ ${isMin ? 'Min-Heap' : 'Max-Heap'} หยุด Percolate Up`,
          vars: {
            hole: hole,
            parent: p,
            comparison: `${conditionStr} -> False`,
            action: `Stop bubbling up`
          },
          visualData: {
            heap: [...h],
            heapType,
            holeIdx: hole,
            parentIdx: p,
            activeIdx: hole,
            op: 'stop_up',
            val: num
          }
        });
        break;
      }
    }

    // Step 3: Place element into final hole slot
    h[hole] = num;
    steps.push({
      line: 12, // self.array[hole] = x
      explanation: `🎉 <b>วางค่าสำเร็จ</b>: บรรจุค่า <b>${num}</b> ลงในช่อง <code>heap[${hole}]</code> -> ได้โครงสร้าง Complete Binary ${isMin ? 'Min-Heap' : 'Max-Heap'} ที่ถูกต้องสมบูรณ์! (Root ปัจจุบัน = <b>${h[1]}</b>)`,
      vars: {
        final_index: hole,
        placed_val: num,
        new_root: h[1],
        total_nodes: h.length - 1
      },
      visualData: {
        heap: [...h],
        heapType,
        holeIdx: -1,
        parentIdx: -1,
        activeIdx: hole,
        op: 'complete',
        val: num
      }
    });

    heapArray = [...h];
    return steps;
  }

  function createHeapDeleteMinSteps() {
    const steps = [];
    let h = [...heapArray];
    const isMin = heapType === 'min';

    if (h.length <= 1) {
      steps.push({
        line: 14,
        explanation: '⚠️ <b>Heap ว่างเปล่า (Empty Heap)</b>: ไม่สามารถนำข้อมูลออกได้',
        vars: { size: 0 },
        visualData: { heap: [0], heapType, holeIdx: -1, parentIdx: -1, activeIdx: -1, op: 'empty' }
      });
      return steps;
    }

    if (h.length === 2) {
      const removed = h[1];
      steps.push({
        line: 15,
        explanation: `🗑️ <b>Delete ${isMin ? 'Min' : 'Max'}</b>: นำโหนดเดียวในฮีป <b>${removed}</b> ออก -> ฮีปว่างเปล่า`,
        vars: { deleted: removed, remaining_size: 0 },
        visualData: { heap: [0], heapType, holeIdx: -1, parentIdx: -1, activeIdx: -1, op: 'complete' }
      });
      heapArray = [0];
      return steps;
    }

    const removedItem = h[1];
    const lastItem = h.pop();
    const temp = lastItem;
    let hole = 1;

    steps.push({
      line: 15, // min_item = self.array[1]
      explanation: `🗑️ <b>Delete ${isMin ? 'Min' : 'Max'} สเต็ปที่ 1</b>: เก็บค่าราก <code>heap[1] = ${removedItem}</code> ออกมา -> ดึงค่าตัวสุดท้ายของอาร์เรย์ <code>temp = ${temp}</code> มาพักไว้เพื่อเตรียมนำลงราก`,
      vars: {
        removed_root: removedItem,
        temp_val: temp,
        new_size: h.length - 1
      },
      visualData: {
        heap: [0, temp, ...h.slice(2)],
        heapType,
        holeIdx: 1,
        parentIdx: -1,
        activeIdx: 1,
        op: 'delete_start',
        removed: removedItem,
        temp: temp
      }
    });

    // Percolate Down Loop
    while (hole * 2 <= h.length - 1) {
      let child = hole * 2;
      const rightChild = child + 1;
      const hasRight = rightChild <= h.length - 1;

      // Compare left and right child to pick the extreme child
      let pickedChild = child;
      if (hasRight) {
        const pickRight = isMin ? (h[rightChild] < h[child]) : (h[rightChild] > h[child]);
        if (pickRight) {
          pickedChild = rightChild;
        }

        steps.push({
          line: 25, // if child != self.currentSize and self.array[child + 1] < self.array[child]:
          explanation: `👀 <b>เปรียบเทียบลูกซ้าย-ขวา</b>: ลูกซ้าย <code>heap[${child}] = ${h[child]}</code> กับ ลูกขวา <code>heap[${rightChild}] = ${h[rightChild]}</code> -> เลือกลูกตัวที่ <b>${isMin ? 'น้อยกว่า' : 'มากกว่า'}</b> คือ <code>heap[${pickedChild}] = ${h[pickedChild]}</code>`,
          vars: {
            hole: hole,
            left_child: `${h[child]} (idx ${child})`,
            right_child: `${h[rightChild]} (idx ${rightChild})`,
            picked_child: `${h[pickedChild]} (idx ${pickedChild})`
          },
          visualData: {
            heap: [...h],
            heapType,
            holeIdx: hole,
            parentIdx: hole,
            childIdx: pickedChild,
            activeIdx: pickedChild,
            op: 'compare_children',
            temp: temp
          }
        });
      }

      child = pickedChild;
      const violates = isMin ? (h[child] < temp) : (h[child] > temp);
      const condStr = isMin ? `heap[${child}] (${h[child]}) < temp (${temp})` : `heap[${child}] (${h[child]}) > temp (${temp})`;

      if (violates) {
        steps.push({
          line: 27, // if self.array[child] < temp:
          explanation: `⬇️ <b>Percolate Down ต่อ</b>: <code>${condStr}</code> เป็น <b>จริง (True)</b> -> เลื่อนลูก (${h[child]}) ขึ้นมาแทนที่ <code>heap[${hole}]</code> แล้วเลื่อนช่องว่าง hole ลงไปที่ index <b>${child}</b>`,
          vars: {
            hole: hole,
            child: child,
            action: `Shift child ${h[child]} up to index ${hole}`
          },
          visualData: {
            heap: [...h],
            heapType,
            holeIdx: hole,
            parentIdx: hole,
            childIdx: child,
            activeIdx: child,
            op: 'shift_down',
            temp: temp
          }
        });

        h[hole] = h[child];
        hole = child;
      } else {
        steps.push({
          line: 29, // else: break
          explanation: `🛑 <b>หยุด Percolate Down</b>: <code>${condStr}</code> เป็น <b>เท็จ (False)</b> -> ค่าลูกตัวที่ ${isMin ? 'น้อยที่สุด' : 'มากที่สุด'} ไม่ละเมิดกฎ Min/Max-Heap จึงหยุดเลื่อน`,
          vars: {
            hole: hole,
            child: child,
            action: 'Stop percolate down'
          },
          visualData: {
            heap: [...h],
            heapType,
            holeIdx: hole,
            parentIdx: -1,
            childIdx: -1,
            activeIdx: hole,
            op: 'stop_down',
            temp: temp
          }
        });
        break;
      }
    }

    h[hole] = temp;
    steps.push({
      line: 32, // self.array[hole] = temp
      explanation: `🎉 <b>Delete สำเร็จ</b>: วาง <code>temp = ${temp}</code> ลงในช่องว่างสุดท้าย <code>heap[${hole}]</code> -> ได้ค่าที่ลบออกคือ <b>${removedItem}</b> และรากใหม่คือ <b>${h[1]}</b>`,
      vars: {
        deleted_item: removedItem,
        final_hole_slot: hole,
        placed_val: temp,
        new_root: h[1]
      },
      visualData: {
        heap: [...h],
        heapType,
        holeIdx: -1,
        parentIdx: -1,
        childIdx: -1,
        activeIdx: hole,
        op: 'complete',
        removed: removedItem
      }
    });

    heapArray = [...h];
    return steps;
  }

  function createHeapFindMinSteps() {
    const steps = [];
    const h = [...heapArray];
    const isMin = heapType === 'min';

    if (h.length <= 1) {
      return createHeapDefaultSteps('⚠️ Heap ว่างเปล่า ไม่มีข้อมูล');
    }

    steps.push({
      line: 4, // def find_min(self): return self.array[1]
      explanation: `⚡ <b>Find ${isMin ? 'Min' : 'Max'}</b>: ใน Binary ${isMin ? 'Min-Heap' : 'Max-Heap'} ค่าที่ ${isMin ? 'น้อยที่สุด' : 'มากที่สุด'} จะอยู่ที่ราก <code>heap[1] = ${h[1]}</code> เสมอ ทำงานได้เร็วระดับความซับซ้อน <b>O(1)</b> คงที่ ไม่ต้องค้นหาทั้งต้นไม้!`,
      vars: {
        operation: `find_${isMin ? 'min' : 'max'}()`,
        result: h[1],
        index: 1,
        time_complexity: 'O(1)'
      },
      visualData: {
        heap: [...h],
        heapType,
        holeIdx: -1,
        parentIdx: -1,
        childIdx: -1,
        activeIdx: 1,
        op: 'find_min'
      }
    });

    return steps;
  }

  function renderHeap(container, visualData) {
    const { heap, heapType, holeIdx, parentIdx, childIdx, activeIdx, op } = visualData;
    const n = heap.length - 1;
    const isMin = heapType === 'min';

    let html = `
      <div class="heap-dual-container">
        <!-- 1. Array Representation Box -->
        <div class="heap-view-box">
          <div class="heap-view-header">
            <div class="heap-view-title">
              <span class="view-icon">📋</span>
              <span>1-Based Array Index Representation [1 .. ${n}]</span>
            </div>
            <div class="heap-tag">${isMin ? 'Min-Heap' : 'Max-Heap'} (Exams/Heap.py)</div>
          </div>
          <div class="heap-array-slots">
            <!-- Sentinel Index 0 -->
            <div class="h-slot-wrapper">
              <span class="h-badge sentinel-badge">Sentinel</span>
              <div class="h-slot is-sentinel">
                <span class="h-val">None</span>
                <span class="h-idx">[0]</span>
              </div>
            </div>
    `;

    for (let idx = 1; idx <= n; idx++) {
      let slotClass = 'h-slot';
      let badge = '';

      if (idx === holeIdx) {
        slotClass += ' is-hole';
        badge = '<span class="h-badge act">Hole</span>';
      } else if (idx === parentIdx) {
        slotClass += ' is-parent';
        badge = '<span class="h-badge par">Parent</span>';
      } else if (idx === childIdx) {
        slotClass += ' is-child';
        badge = '<span class="h-badge child">Child</span>';
      } else if (idx === 1) {
        badge = '<span class="h-badge root">Root</span>';
      }

      if (idx === activeIdx && idx !== holeIdx && idx !== parentIdx && idx !== childIdx) {
        slotClass += ' is-active';
      }

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

    html += `
          </div>
        </div>
    `;

    // 2. Tree Structure View Box (Dynamically layout SVG)
    if (n === 0) {
      html += `
        <div class="heap-view-box">
          <div class="empty-placeholder">ฮีปว่างเปล่า กรุณากดปุ่ม Insert เพื่อเพิ่มข้อมูล</div>
        </div>
      </div>`;
      container.innerHTML = html;
      return;
    }

    const maxLevel = Math.max(1, Math.floor(Math.log2(n)));
    const svgWidth = Math.max(560, Math.pow(2, maxLevel) * 44);
    const svgHeight = 45 + (maxLevel + 1) * 65;

    // Calculate node coordinates dynamically
    const coords = [null];
    for (let i = 1; i <= n; i++) {
      const level = Math.floor(Math.log2(i));
      const slots = Math.pow(2, level);
      const col = i - slots;
      const x = (col + 0.5) * (svgWidth / slots);
      const y = 35 + level * 62;
      coords.push({ x: Math.round(x), y: Math.round(y), level });
    }

    html += `
      <div class="heap-view-box">
        <div class="heap-view-header">
          <div class="heap-view-title">
            <span class="view-icon">🌲</span>
            <span>Complete Binary Tree View (ความสูง ${maxLevel + 1} ชั้น)</span>
          </div>
          <div class="heap-tag">Parent = ⌊i/2⌋, Left = 2i, Right = 2i+1</div>
        </div>
        <div class="svg-scroll-wrapper">
          <svg class="heap-svg" viewBox="0 0 ${svgWidth} ${svgHeight}" style="min-width:${svgWidth}px; height:${svgHeight}px;">
            <defs>
              <linearGradient id="grad-active-node" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b" />
                <stop offset="100%" stop-color="#d97706" />
              </linearGradient>
              <linearGradient id="grad-parent-node" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#6366f1" />
                <stop offset="100%" stop-color="#4f46e5" />
              </linearGradient>
              <linearGradient id="grad-child-node" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#06b6d4" />
                <stop offset="100%" stop-color="#0284c7" />
              </linearGradient>
              <linearGradient id="grad-root-node" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#10b981" />
                <stop offset="100%" stop-color="#059669" />
              </linearGradient>
              <filter id="glow-filter" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="3" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
            </defs>
    `;

    // Draw tree edges
    for (let i = 2; i <= n; i++) {
      const p = Math.floor(i / 2);
      if (coords[p] && coords[i]) {
        const isPath = (i === holeIdx && p === parentIdx) || (i === childIdx && p === holeIdx);
        html += `
          <line x1="${coords[p].x}" y1="${coords[p].y}" x2="${coords[i].x}" y2="${coords[i].y}" 
                class="heap-edge ${isPath ? 'is-active-edge' : ''}" />
        `;
      }
    }

    // Draw tree nodes
    for (let i = 1; i <= n; i++) {
      const c = coords[i];
      let circleClass = 'heap-circle';
      let fillAttr = 'var(--bg-surface-elevated)';
      let filterAttr = '';
      let tagLabel = '';

      if (i === holeIdx) {
        circleClass += ' is-hole';
        fillAttr = 'url(#grad-active-node)';
        filterAttr = 'filter="url(#glow-filter)"';
        tagLabel = 'HOLE';
      } else if (i === parentIdx) {
        circleClass += ' is-parent';
        fillAttr = 'url(#grad-parent-node)';
        tagLabel = 'PARENT';
      } else if (i === childIdx) {
        circleClass += ' is-child';
        fillAttr = 'url(#grad-child-node)';
        tagLabel = 'CHILD';
      } else if (i === 1) {
        circleClass += ' is-root';
        fillAttr = 'url(#grad-root-node)';
        tagLabel = 'ROOT';
      }

      html += `
        <g class="heap-node-group" transform="translate(${c.x}, ${c.y})">
          <circle r="20" fill="${fillAttr}" class="${circleClass}" ${filterAttr}></circle>
          <text text-anchor="middle" dy="5" class="heap-node-text">${heap[i]}</text>
          <text text-anchor="middle" dy="-26" class="heap-index-badge">idx [${i}]</text>
          ${tagLabel ? `<text text-anchor="middle" dy="34" class="heap-role-label">${tagLabel}</text>` : ''}
        </g>
      `;
    }

    html += `
          </svg>
        </div>
      </div>
    </div>`;

    container.innerHTML = html;
  }

  // =========================================================================
  // 2. DYNAMIC BINARY SEARCH TREE (BST) ENGINE — Exams/BinarySearchTrees.py
  // =========================================================================
  class BstNode {
    constructor(val) {
      this.val = val;
      this.left = null;
      this.right = null;
    }
  }

  let bstRoot = null;

  function initBstPreset() {
    const presetValues = [50, 30, 70, 20, 40, 60, 80, 65];
    bstRoot = null;
    presetValues.forEach(v => {
      bstRoot = bstInsertRaw(bstRoot, v);
    });
  }

  function bstInsertRaw(root, val) {
    if (!root) return new BstNode(val);
    if (val < root.val) root.left = bstInsertRaw(root.left, val);
    else if (val > root.val) root.right = bstInsertRaw(root.right, val);
    return root;
  }

  function cloneBst(root) {
    if (!root) return null;
    const n = new BstNode(root.val);
    n.left = cloneBst(root.left);
    n.right = cloneBst(root.right);
    return n;
  }

  // Calculate layout coordinates for SVG rendering
  function calculateBstLayout(root) {
    if (!root) return { nodes: [], edges: [], width: 500, height: 260 };

    let currentX = 30;
    const nodes = [];
    const edges = [];

    // In-order traversal to assign X coordinates
    function assignCoords(node, depth) {
      if (!node) return;
      assignCoords(node.left, depth + 1);

      node._x = currentX;
      node._y = 40 + depth * 60;
      currentX += 45;

      assignCoords(node.right, depth + 1);
    }

    assignCoords(root, 0);
    const width = Math.max(540, currentX + 30);

    function collectElements(node) {
      if (!node) return;
      nodes.push({ val: node.val, x: node._x, y: node._y });

      if (node.left) {
        edges.push({ x1: node._x, y1: node._y, x2: node.left._x, y2: node.left._y });
        collectElements(node.left);
      }
      if (node.right) {
        edges.push({ x1: node._x, y1: node._y, x2: node.right._x, y2: node.right._y });
        collectElements(node.right);
      }
    }

    collectElements(root);
    const maxDepth = nodes.reduce((max, n) => Math.max(max, n.y), 40);
    return { nodes, edges, width, height: maxDepth + 60 };
  }

  function createBstDefaultSteps(customMsg) {
    if (!bstRoot) initBstPreset();
    const steps = [];
    const layout = calculateBstLayout(bstRoot);

    steps.push({
      line: 3,
      explanation: customMsg || '🌳 <b>Binary Search Tree (BST)</b>: โครงสร้างต้นไม้ค้นหาแบบทวิภาค (Left < Root < Right) พร้อมรองรับ Insert, Delete, Search และ Traversal แบบไดนามิก',
      vars: {
        root: bstRoot ? bstRoot.val : 'None',
        total_nodes: layout.nodes.length,
        invariants: 'Left < Root < Right'
      },
      visualData: {
        tree: layout,
        targetVal: null,
        successorVal: null,
        searchPath: [],
        phase: 'init'
      }
    });

    return steps;
  }

  function createDynamicBstInsertSteps(val) {
    const num = parseInt(val, 10);
    if (isNaN(num)) return createBstDefaultSteps();

    if (!bstRoot) initBstPreset();
    const steps = [];
    let treeCopy = cloneBst(bstRoot);
    const searchPath = [];

    steps.push({
      line: 14, // def insert(self, value):
      explanation: `📥 <b>เริ่ม Insert(${num})</b>: เริ่มต้นตรวจสอบจาก Root (${treeCopy.val}) เพื่อหากิ่งที่ต้องลงไปตามคุณสมบัติ BST`,
      vars: { insert_value: num, current_node: treeCopy.val },
      visualData: {
        tree: calculateBstLayout(treeCopy),
        targetVal: num,
        searchPath: [treeCopy.val],
        phase: 'search'
      }
    });

    let curr = treeCopy;
    let parent = null;

    while (curr) {
      searchPath.push(curr.val);
      parent = curr;
      if (num < curr.val) {
        steps.push({
          line: 19, // if value < current_node.value:
          explanation: `🔍 <code>${num} < ${curr.val}</code> -> ค่าใหม่น้อยกว่า จึงเลี้ยวซ้ายเข้าสู่กิ่งย่อยทางซ้าย (Left Subtree)`,
          vars: { condition: `${num} < ${curr.val} (True)`, direction: 'Left', current: curr.val },
          visualData: {
            tree: calculateBstLayout(treeCopy),
            targetVal: num,
            searchPath: [...searchPath],
            phase: 'traverse'
          }
        });
        if (!curr.left) {
          curr.left = new BstNode(num);
          break;
        }
        curr = curr.left;
      } else if (num > curr.val) {
        steps.push({
          line: 24, // elif value > current_node.value:
          explanation: `🔍 <code>${num} > ${curr.val}</code> -> ค่าใหม่มากกว่า จึงเลี้ยวขวาเข้าสู่กิ่งย่อยทางขวา (Right Subtree)`,
          vars: { condition: `${num} > ${curr.val} (True)`, direction: 'Right', current: curr.val },
          visualData: {
            tree: calculateBstLayout(treeCopy),
            targetVal: num,
            searchPath: [...searchPath],
            phase: 'traverse'
          }
        });
        if (!curr.right) {
          curr.right = new BstNode(num);
          break;
        }
        curr = curr.right;
      } else {
        steps.push({
          line: 29,
          explanation: `⚠️ <b>พบค่าซ้ำ</b>: ค่า ${num} มีอยู่ในต้นไม้แล้ว ไม่ต้องแทรกซ้ำ`,
          vars: { status: 'Duplicate key' },
          visualData: {
            tree: calculateBstLayout(treeCopy),
            targetVal: num,
            searchPath: [...searchPath],
            phase: 'duplicate'
          }
        });
        return steps;
      }
    }

    searchPath.push(num);
    steps.push({
      line: 22,
      explanation: `🎉 <b>Insert(${num}) สำเร็จ</b>: สร้างโหนดใหม่ <code>Node(${num})</code> เชื่อมต่อเป็นลูกของโหนด <b>${parent.val}</b> เรียบร้อย!`,
      vars: { parent: parent.val, new_node: num, status: 'Inserted successfully' },
      visualData: {
        tree: calculateBstLayout(treeCopy),
        targetVal: num,
        searchPath: [...searchPath],
        phase: 'complete'
      }
    });

    bstRoot = treeCopy;
    return steps;
  }

  function createDynamicBstDeleteSteps(val) {
    const num = parseInt(val, 10);
    if (isNaN(num)) return createBstDefaultSteps();

    if (!bstRoot) initBstPreset();
    const steps = [];
    let treeCopy = cloneBst(bstRoot);
    const searchPath = [];

    // Step 1: Search for target node
    let curr = treeCopy;
    let parent = null;
    while (curr && curr.val !== num) {
      searchPath.push(curr.val);
      parent = curr;
      if (num < curr.val) curr = curr.left;
      else curr = curr.right;
    }

    if (!curr) {
      steps.push({
        line: 36,
        explanation: `⚠️ <b>ไม่พบข้อมูล</b>: ไม่พบโหนดค่า <b>${num}</b> ในต้นไม้ BST`,
        vars: { target: num, found: false },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: num,
          searchPath: [...searchPath],
          phase: 'not_found'
        }
      });
      return steps;
    }

    searchPath.push(curr.val);

    // Case Analysis: 0, 1, or 2 children
    const hasLeft = curr.left !== null;
    const hasRight = curr.right !== null;

    if (!hasLeft && !hasRight) {
      // Case 1: Leaf Node (0 Child)
      steps.push({
        line: 39, // if current_node.left is None: return current_node.right
        explanation: `🎯 <b>Case 1: Leaf Node (ไม่มีลูก)</b>: โหนด <b>${num}</b> เป็นโหนดใบ สามารถตัดทิ้ง (ลบ) ได้ทันทีโดยไม่ต้องจัดเรียงพอยน์เตอร์ใหม่`,
        vars: { target: num, case: 'Case 1 (Leaf)', parent: parent ? parent.val : 'Root' },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: num,
          searchPath: [...searchPath],
          phase: 'leaf_delete'
        }
      });

      treeCopy = bstDeleteRecursive(treeCopy, num);

      steps.push({
        line: 39,
        explanation: `🎉 <b>ลบโหนดใบ ${num} สำเร็จ</b>: ตัดโหนดใบออกจากต้นไม้เรียบร้อย`,
        vars: { deleted: num, status: 'Completed' },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: null,
          searchPath: [],
          phase: 'complete'
        }
      });
    } else if (!hasLeft || !hasRight) {
      // Case 2: One Child
      const childVal = hasLeft ? curr.left.val : curr.right.val;
      steps.push({
        line: 40, // elif current_node.right is None: return current_node.left
        explanation: `🎯 <b>Case 2: One Child (มีลูก 1 ตัว)</b>: โหนด <b>${num}</b> มีลูกเพียงตัวเดียวคือ <b>${childVal}</b> -> สามารถดึงลูกขึ้นมาเชื่อมต่อกับโหนดแม่แทนที่ได้ทันที`,
        vars: { target: num, case: 'Case 2 (1 Child)', child: childVal },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: num,
          successorVal: childVal,
          searchPath: [...searchPath],
          phase: 'one_child'
        }
      });

      treeCopy = bstDeleteRecursive(treeCopy, num);

      steps.push({
        line: 40,
        explanation: `🎉 <b>ลบโหนด ${num} สำเร็จ</b>: ดึงโหนดลูก <b>${childVal}</b> ขึ้นมาแทนตำแหน่งเดิมเรียบร้อย`,
        vars: { deleted: num, promoted: childVal },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: null,
          successorVal: null,
          searchPath: [],
          phase: 'complete'
        }
      });
    } else {
      // Case 3: Two Children (The Classic Exam Question!)
      // Find In-order Successor (min in right subtree)
      let succ = curr.right;
      let succPath = [curr.val, succ.val];
      while (succ.left) {
        succ = succ.left;
        succPath.push(succ.val);
      }

      steps.push({
        line: 42, // temp_node = self._min_value_node(current_node.right)
        explanation: `🎯 <b>Case 3: Two Children (มีลูก 2 ตัว)</b>: โหนด <b>${num}</b> มีลูกทั้งซ้ายและขวา! ต้องหา <b>In-order Successor</b> (ค่าน้อยที่สุดในกิ่งขวา <code>min_node(node.right)</code>)`,
        vars: { target: num, case: 'Case 3 (2 Children)', right_child: curr.right.val },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: num,
          searchPath: [...searchPath],
          phase: 'find_successor'
        }
      });

      steps.push({
        line: 43, // current_node.value = temp_node.value
        explanation: `🔍 <b>พบ In-order Successor = ${succ.val}</b>: เตรียมคัดลอกค่า <b>${succ.val}</b> มาแทนที่โหนด <b>${num}</b>`,
        vars: { target: num, successor: succ.val, action: 'Copy value to target' },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: num,
          successorVal: succ.val,
          searchPath: [...succPath],
          phase: 'found_successor'
        }
      });

      treeCopy = bstDeleteRecursive(treeCopy, num);

      steps.push({
        line: 44, // current_node.right = self._delete_recursive(...)
        explanation: `🎉 <b>Case 3 สำเร็จ</b>: โคลนค่า <b>${succ.val}</b> มาแทนที่ และสั่งลบโหนดใบ <b>${succ.val}</b> ตัวเดิมในกิ่งขวาออก -> ได้ต้นไม้ BST ที่คงกฎถูกต้องสมบูรณ์!`,
        vars: { replaced: num, with_value: succ.val, status: 'Valid BST' },
        visualData: {
          tree: calculateBstLayout(treeCopy),
          targetVal: null,
          successorVal: null,
          searchPath: [],
          phase: 'complete'
        }
      });
    }

    bstRoot = treeCopy;
    return steps;
  }

  function bstDeleteRecursive(root, key) {
    if (!root) return null;
    if (key < root.val) root.left = bstDeleteRecursive(root.left, key);
    else if (key > root.val) root.right = bstDeleteRecursive(root.right, key);
    else {
      if (!root.left) return root.right;
      if (!root.right) return root.left;
      let minNode = root.right;
      while (minNode.left) minNode = minNode.left;
      root.val = minNode.val;
      root.right = bstDeleteRecursive(root.right, minNode.val);
    }
    return root;
  }

  function renderBst(container, visualData) {
    const { tree, targetVal, successorVal, searchPath, phase } = visualData;
    const { nodes, edges, width, height } = tree;

    let html = `
      <div class="bst-sim-container">
        <div class="bst-header-bar">
          <div class="bst-meta-stat">
            <span>โหนดทั้งหมด:</span> <b>${nodes.length}</b>
          </div>
          <div class="bst-meta-stat">
            <span>กฎ BST:</span> <b>Left &lt; Node &lt; Right</b>
          </div>
          <div class="bst-meta-stat">
            <span>สถานะ:</span> <b style="color:#38bdf8;">${phase.toUpperCase()}</b>
          </div>
        </div>
        <div class="svg-scroll-wrapper">
          <svg class="bst-svg" viewBox="0 0 ${width} ${height}" style="min-width:${width}px; height:${height}px;">
            <defs>
              <linearGradient id="grad-target" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f43f5e" />
                <stop offset="100%" stop-color="#e11d48" />
              </linearGradient>
              <linearGradient id="grad-successor" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b" />
                <stop offset="100%" stop-color="#d97706" />
              </linearGradient>
              <linearGradient id="grad-path" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#06b6d4" />
                <stop offset="100%" stop-color="#0284c7" />
              </linearGradient>
            </defs>
    `;

    // Edges
    edges.forEach(e => {
      html += `<line x1="${e.x1}" y1="${e.y1}" x2="${e.x2}" y2="${e.y2}" class="bst-edge" />`;
    });

    // Nodes
    nodes.forEach(n => {
      let circleClass = 'bst-circle';
      let fillAttr = 'var(--bg-surface-elevated)';
      let label = '';

      if (n.val === targetVal) {
        circleClass += ' is-target';
        fillAttr = 'url(#grad-target)';
        label = 'Target';
      } else if (n.val === successorVal) {
        circleClass += ' is-successor';
        fillAttr = 'url(#grad-successor)';
        label = 'Successor';
      } else if (searchPath && searchPath.includes(n.val)) {
        circleClass += ' on-path';
        fillAttr = 'url(#grad-path)';
      }

      html += `
        <g class="bst-node-group" transform="translate(${n.x}, ${n.y})">
          <circle r="20" fill="${fillAttr}" class="${circleClass}"></circle>
          <text text-anchor="middle" dy="5" class="bst-node-text">${n.val}</text>
          ${label ? `<text text-anchor="middle" dy="-26" class="bst-node-label">${label}</text>` : ''}
        </g>
      `;
    });

    html += `
          </svg>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // 3. DYNAMIC HASH TABLE & COLLISION RESOLUTION — Exams/Hash.py
  // =========================================================================
  let hashStrategy = 'chaining'; // 'chaining' | 'linear_probing'
  let hashCapacity = 10;
  let hashBuckets = Array.from({ length: 10 }, () => []);

  function resetHashTable() {
    hashBuckets = Array.from({ length: hashCapacity }, () => []);
    // Preset keys from Exams/Hash.py
    const presets = ['AB', 'HELLO', 'DSA', 'PYTHON'];
    presets.forEach(k => insertHashKeyDirect(k));
    return createHashSteps('HELLO', hashCapacity);
  }

  function insertHashKeyDirect(key) {
    let sum = 0;
    for (let c of key) sum += c.charCodeAt(0);
    const slot = sum % hashCapacity;
    if (hashStrategy === 'chaining') {
      if (!hashBuckets[slot].includes(key)) hashBuckets[slot].push(key);
    } else {
      let s = slot;
      while (hashBuckets[s].length > 0 && hashBuckets[s][0] !== key) {
        s = (s + 1) % hashCapacity;
      }
      hashBuckets[s] = [key];
    }
  }

  function createHashSteps(keyToHash, tableSize) {
    const key = (keyToHash || 'HELLO').trim().toUpperCase();
    const m = tableSize || hashCapacity;
    const steps = [];

    let sum = 0;
    const charSteps = [];

    steps.push({
      line: 3,
      explanation: `📐 <b>Hash Calculation:</b> เตรียมแฮชสตริงก์ <code>"${key}"</code> ลงในตารางแฮชขนาด <b>m = ${m}</b> ตามสูตร <code>hash_val = sum(ord(c)) % m</code>`,
      vars: { key, table_size: m, hash_formula: 'sum(ord(c)) % table_size' },
      visualData: {
        key,
        tableSize: m,
        char: null,
        ord: null,
        sum: 0,
        targetSlot: -1,
        buckets: hashBuckets,
        strategy: hashStrategy
      }
    });

    for (let i = 0; i < key.length; i++) {
      const char = key[i];
      const ord = char.charCodeAt(0);
      sum += ord;

      steps.push({
        line: 5, // hash_val += ord(char)
        explanation: `🔤 <b>ตัวอักษรที่ [${i + 1}]: '${char}'</b> -> รหัส ASCII = <code>ord('${char}') = ${ord}</code> -> ผลรวมสะสม: <b>${sum}</b>`,
        vars: { char, ascii_code: ord, accumulated_sum: sum },
        visualData: {
          key,
          tableSize: m,
          char,
          ord,
          sum,
          targetSlot: -1,
          buckets: hashBuckets,
          strategy: hashStrategy
        }
      });
    }

    const slot = sum % m;
    steps.push({
      line: 6, // return hash_val % table_size
      explanation: `🎯 <b>คำนวณตำแหน่ง Bucket</b>: <code>${sum} % ${m} = ${slot}</code> -> ช่องเป้าหมายคือ <b>Bucket [${slot}]</b>`,
      vars: { total_ascii: sum, modulo: m, target_slot: slot },
      visualData: {
        key,
        tableSize: m,
        char: null,
        ord: null,
        sum,
        targetSlot: slot,
        buckets: hashBuckets,
        strategy: hashStrategy
      }
    });

    // Check for collision
    const existing = hashBuckets[slot];
    if (existing.length > 0 && !existing.includes(key)) {
      if (hashStrategy === 'chaining') {
        steps.push({
          line: 7,
          explanation: `⚡ <b>เกิดการชนกัน (Collision)!</b>: ช่อง [${slot}] มีข้อมูล <code>"${existing.join(', ')}"</code> อยู่แล้ว -> แก้ไขด้วย <b>Separate Chaining</b> เชื่อมต่อ Linked List Node ใหม่เข้ากับบัคเก็ตนี้`,
          vars: { collision_at_slot: slot, existing_data: existing.join(', '), strategy: 'Separate Chaining' },
          visualData: {
            key,
            tableSize: m,
            sum,
            targetSlot: slot,
            buckets: hashBuckets,
            collision: true,
            strategy: 'chaining'
          }
        });
        hashBuckets[slot].push(key);
      } else {
        // Linear probing
        let probe = slot;
        let pCount = 0;
        while (hashBuckets[probe].length > 0 && pCount < m) {
          probe = (probe + 1) % m;
          pCount++;
          steps.push({
            line: 7,
            explanation: `🔄 <b>Linear Probing ก้าวที่ ${pCount}</b>: ช่อง [${(probe - 1 + m) % m}] เต็ม -> เลื่อนไปตรวจช่องถัดไป: <code>(${slot} + ${pCount}) % ${m} = ${probe}</code>`,
            vars: { probe_step: pCount, testing_slot: probe },
            visualData: {
              key,
              tableSize: m,
              sum,
              targetSlot: probe,
              buckets: hashBuckets,
              probing: true,
              strategy: 'linear_probing'
            }
          });
        }
        hashBuckets[probe] = [key];
      }
    } else if (!existing.includes(key)) {
      hashBuckets[slot].push(key);
    }

    steps.push({
      line: 6,
      explanation: `🎉 <b>จัดเก็บสำเร็จ</b>: ข้อมูล <code>"${key}"</code> ถูกบรรจุลงในตารางแฮชเรียบร้อย!`,
      vars: { stored_key: key, final_slot: slot, total_keys: hashBuckets.flat().length },
      visualData: {
        key,
        tableSize: m,
        sum,
        targetSlot: slot,
        buckets: hashBuckets,
        strategy: hashStrategy,
        complete: true
      }
    });

    return steps;
  }

  function renderHash(container, visualData) {
    const { key, tableSize, char, ord, sum, targetSlot, buckets, strategy } = visualData;
    const m = tableSize || 10;
    const totalKeys = buckets ? buckets.flat().length : 0;
    const loadFactor = (totalKeys / m).toFixed(2);

    let html = `
      <div class="hash-sim-container">
        <div class="hash-calc-hud">
          <div class="hud-item">
            <span class="hud-lbl">Key ปัจจุบัน:</span>
            <span class="hud-val highlight-blue">"${key || 'HELLO'}"</span>
          </div>
          <div class="hud-item">
            <span class="hud-lbl">ASCII Sum:</span>
            <span class="hud-val highlight-green">${sum || 0}</span>
          </div>
          <div class="hud-item">
            <span class="hud-lbl">สูตร Modulo:</span>
            <span class="hud-val">h(k) = ${sum || 0} % ${m} = <b>${targetSlot >= 0 ? targetSlot : '?'}</b></span>
          </div>
          <div class="hud-item">
            <span class="hud-lbl">Load Factor (λ):</span>
            <span class="hud-val ${loadFactor >= 0.75 ? 'warn-red' : 'highlight-amber'}">${loadFactor} (${totalKeys}/${m})</span>
          </div>
        </div>

        <div class="hash-table-grid">
    `;

    for (let i = 0; i < m; i++) {
      const isTarget = i === targetSlot;
      const bucketItems = buckets && buckets[i] ? buckets[i] : [];

      html += `
        <div class="hash-bucket-card ${isTarget ? 'is-target-bucket' : ''}">
          <div class="hash-bucket-header">
            <span class="bucket-idx">Slot [${i}]</span>
            ${isTarget ? '<span class="target-indicator">TARGET</span>' : ''}
          </div>
          <div class="hash-bucket-nodes">
      `;

      if (bucketItems.length === 0) {
        html += '<span class="empty-node">Empty (None)</span>';
      } else {
        bucketItems.forEach((item, idx) => {
          html += `
            <div class="hash-chain-node">
              <span>${item}</span>
              ${idx < bucketItems.length - 1 ? '<span class="chain-arrow">➔</span>' : ''}
            </div>
          `;
        });
      }

      html += `
          </div>
        </div>
      `;
    }

    html += `
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // 4. DYNAMIC INFIX TO POSTFIX CONVERTER (STACK) — Exams/InfixToPostFix.py
  // =========================================================================
  const PRECEDENCE = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
  };

  function createStackSteps(customExpr) {
    const expr = (customExpr || '(A + B) * C - D / E').replace(/\s+/g, '');
    const steps = [];

    const stack = [];
    let postfix = '';

    steps.push({
      line: 3,
      explanation: `🥞 <b>Infix to Postfix Conversion</b>: เตรียมแปลงนิพจน์คณิตศาสตร์ <code>"${expr}"</code> โดยใช้ **Stack** จัดการลำดับความสำคัญของเครื่องหมาย (Precedence)`,
      vars: {
        expression: expr,
        stack_state: '[]',
        postfix_output: '""',
        rule: 'Operand ออกทันที | Operator เทียบ Precedence'
      },
      visualData: {
        expr,
        tokenIdx: -1,
        stack: [],
        postfix: '',
        op: 'init'
      }
    });

    for (let i = 0; i < expr.length; i++) {
      const token = expr[i];

      if (/[A-Za-z0-9]/.test(token)) {
        // Operand
        postfix += token;
        steps.push({
          line: 6,
          explanation: `🔤 <b>อ่านพบตัวถูกดำเนินการ (Operand): '${token}'</b> -> นำออกไปต่อท้ายผลลัพธ์ Postfix ทันทีโดยไม่ต้องเข้า Stack`,
          vars: { token, type: 'Operand', postfix_output: postfix, stack: stack.join(' ') },
          visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'operand' }
        });
      } else if (token === '(') {
        // Open parenthesis
        stack.push(token);
        steps.push({
          line: 9,
          explanation: `📌 <b>อ่านพบวงเล็บเปิด '(':</b> Push ลงสู่ Stack เพื่อกำหนดขอบเขตกลุ่มการคำนวณ`,
          vars: { token: '(', action: 'Push to stack', stack: stack.join(' ') },
          visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'push' }
        });
      } else if (token === ')') {
        // Close parenthesis: pop until '('
        steps.push({
          line: 12,
          explanation: `🔍 <b>อ่านพบวงเล็บปิด ')':</b> ต้องสั่ง Pop เครื่องหมายทั้งหมดใน Stack ออกไปใส่ Postfix จนกว่าจะพบ '('`,
          vars: { token: ')', action: 'Pop until (' },
          visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'close_paren' }
        });

        while (stack.length > 0 && stack[stack.length - 1] !== '(') {
          const popped = stack.pop();
          postfix += popped;
          steps.push({
            line: 14,
            explanation: `⬆️ <b>Pop '${popped}' ออกจาก Stack</b> -> นำไปต่อท้ายผลลัพธ์ Postfix: <code>"${postfix}"</code>`,
            vars: { popped, postfix_output: postfix, stack: stack.join(' ') },
            visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'pop' }
          });
        }
        if (stack.length > 0 && stack[stack.length - 1] === '(') {
          stack.pop(); // discard '('
        }
      } else if (PRECEDENCE[token] !== undefined) {
        // Operator (+, -, *, /, ^)
        const curPrec = PRECEDENCE[token];
        steps.push({
          line: 18,
          explanation: `⚡ <b>อ่านพบตัวดำเนินการ '${token}' (Precedence = ${curPrec})</b>: เปรียบเทียบกับเครื่องหมายบนยอด Stack`,
          vars: { token, precedence: curPrec, top_of_stack: stack.length > 0 ? stack[stack.length - 1] : 'Empty' },
          visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'compare_prec' }
        });

        while (stack.length > 0 && PRECEDENCE[stack[stack.length - 1]] >= curPrec) {
          const popped = stack.pop();
          postfix += popped;
          steps.push({
            line: 20,
            explanation: `⬆️ เครื่องหมายบนยอด Stack '${popped}' มีศักดิ์ <b>มากกว่าหรือเท่ากับ</b> '${token}' -> สั่ง Pop '${popped}' ออกไปใส่ Postfix`,
            vars: { popped, reason: `Precedence(${popped}) >= Precedence(${token})`, postfix_output: postfix },
            visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'pop' }
          });
        }

        stack.push(token);
        steps.push({
          line: 22,
          explanation: `📥 <b>Push '${token}' ลงใน Stack</b> หลังจัดการตัวที่มีศักดิ์สูงกว่าหมดแล้ว`,
          vars: { pushed: token, stack: stack.join(' ') },
          visualData: { expr, tokenIdx: i, stack: [...stack], postfix, op: 'push' }
        });
      }
    }

    // Pop all remaining operators in stack
    if (stack.length > 0) {
      steps.push({
        line: 25,
        explanation: '🏁 <b>สิ้นสุดการอ่านนิพจน์</b>: สั่ง Pop เครื่องหมายที่ยังตกค้างใน Stack ออกมาต่อท้าย Postfix ให้หมด',
        vars: { remaining_in_stack: stack.join(' ') },
        visualData: { expr, tokenIdx: expr.length, stack: [...stack], postfix, op: 'flush_start' }
      });

      while (stack.length > 0) {
        const popped = stack.pop();
        postfix += popped;
        steps.push({
          line: 27,
          explanation: `⬆️ Pop <b>'${popped}'</b> ออกสู่ Postfix -> ปัจจุบันได้: <code>"${postfix}"</code>`,
          vars: { popped, postfix_output: postfix, stack: stack.join(' ') },
          visualData: { expr, tokenIdx: expr.length, stack: [...stack], postfix, op: 'pop' }
        });
      }
    }

    steps.push({
      line: 30,
      explanation: `🎉 <b>แปลงนิพจน์สำเร็จสมบูรณ์!</b><br>Infix: <code>"${expr}"</code><br>Postfix: <b style="color:#10b981; font-size:1.1rem;">"${postfix}"</b>`,
      vars: { final_postfix: postfix, original_infix: expr, status: 'Completed' },
      visualData: { expr, tokenIdx: expr.length, stack: [], postfix, op: 'complete' }
    });

    return steps;
  }

  function renderStack(container, visualData) {
    const { expr, tokenIdx, stack, postfix, op } = visualData;

    let html = `
      <div class="stack-sim-container">
        <!-- 1. Scanned Expression Stream -->
        <div class="expr-stream-box">
          <div class="box-label">Infix Expression Stream:</div>
          <div class="token-pills">
    `;

    for (let i = 0; i < expr.length; i++) {
      const isCur = i === tokenIdx;
      const isPast = i < tokenIdx;
      html += `
        <span class="token-pill ${isCur ? 'is-current-token' : ''} ${isPast ? 'is-past-token' : ''}">
          ${expr[i]}
        </span>
      `;
    }

    html += `
          </div>
        </div>

        <!-- 2. Dual Panel: Operator Stack & Postfix Output -->
        <div class="stack-dual-panel">
          <!-- Stack Visualizer -->
          <div class="stack-column-box">
            <div class="box-label">🥞 Operator Stack (LIFO):</div>
            <div class="stack-v-container">
    `;

    if (stack.length === 0) {
      html += '<div class="stack-empty-slot">Stack ว่าง (Empty)</div>';
    } else {
      for (let i = stack.length - 1; i >= 0; i--) {
        const isTop = i === stack.length - 1;
        html += `
          <div class="stack-element ${isTop ? 'is-stack-top' : ''}">
            <span class="stack-val">${stack[i]}</span>
            ${isTop ? '<span class="stack-top-badge">TOP</span>' : ''}
          </div>
        `;
      }
    }

    html += `
            </div>
          </div>

          <!-- Postfix String Builder -->
          <div class="postfix-column-box">
            <div class="box-label">📤 ผลลัพธ์ Postfix Output Buffer:</div>
            <div class="postfix-output-display">
              ${postfix ? `<span class="postfix-string">${postfix}</span>` : '<span class="placeholder-text">(กำลังรอข้อมูล...)</span>'}
            </div>
            <div class="precedence-card">
              <div class="prec-title">ลำดับความสำคัญ (Precedence Hierarchy):</div>
              <div class="prec-item">1. <code>^</code> (ยกกำลัง) = ระดับ 3</div>
              <div class="prec-item">2. <code>*</code>, <code>/</code> (คูณ, หาร) = ระดับ 2</div>
              <div class="prec-item">3. <code>+</code>, <code>-</code> (บวก, ลบ) = ระดับ 1</div>
            </div>
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // 5. SINGLY LINKED LIST, QUEUE, SORTING, DIJKSTRA ENGINES
  // =========================================================================
  function createLinkedListSteps(initialData) {
    const list = JSON.parse(JSON.stringify(initialData || [
      { id: '612037', name: 'Somchai', gpa: 3.50 },
      { id: '612045', name: 'Somsak', gpa: 2.85 },
      { id: '612089', name: 'Wichai', gpa: 3.90 },
      { id: '612102', name: 'Apinya', gpa: 3.15 }
    ]));

    const steps = [];
    steps.push({
      line: 45,
      explanation: '🔗 <b>Singly Linked List</b>: รายชื่อนักศึกษา 4 คน พร้อมตัวชี้ <code>head</code> ชี้ไปยังโหนดแรก',
      vars: { head: list[0].id, size: list.length },
      visualData: { nodes: list, headIdx: 0, currentIdx: 0, prevIdx: -1 }
    });

    // Simulate delete '612045'
    steps.push({
      line: 68,
      explanation: '🔍 ค้นหาเพื่อลบรหัส "612045": ตั้ง <code>curr = head</code> และ <code>prev = None</code>',
      vars: { target: '612045', curr: list[0].id, prev: 'None' },
      visualData: { nodes: list, headIdx: 0, currentIdx: 0, prevIdx: -1 }
    });

    steps.push({
      line: 71,
      explanation: '➡️ เลื่อนพอยน์เตอร์: <code>prev = curr</code> และ <code>curr = curr.next</code> -> พบโหนดเป้าหมาย "612045"!',
      vars: { target: '612045', curr: list[1].id, prev: list[0].id, match: true },
      visualData: { nodes: list, headIdx: 0, currentIdx: 1, prevIdx: 0, highlightTarget: 1 }
    });

    steps.push({
      line: 79,
      explanation: '✂️ ปลดพอยน์เตอร์: <code>prev.next = curr.next</code> เพื่อตัดโหนด "612045" ออกจาก List',
      vars: { action: 'Bypass node 612045' },
      visualData: { nodes: list, headIdx: 0, currentIdx: -1, prevIdx: 0, deletedIdx: 1 }
    });

    const remaining = list.filter((_, idx) => idx !== 1);
    steps.push({
      line: 82,
      explanation: '🎉 ลบโหนดสำเร็จ! รายการเหลือ 3 คน และรักษาความต่อเนื่องของ Linked List',
      vars: { head: remaining[0].id, size: remaining.length },
      visualData: { nodes: remaining, headIdx: 0, currentIdx: -1, prevIdx: -1 }
    });

    return steps;
  }

  function renderLinkedList(container, visualData) {
    const { nodes, headIdx, currentIdx, prevIdx, deletedIdx, highlightTarget } = visualData;
    let html = '<div class="ll-container">';

    nodes.forEach((node, idx) => {
      let cardClass = 'll-node-card';
      if (idx === currentIdx) cardClass += ' is-curr';
      if (idx === prevIdx) cardClass += ' is-prev';
      if (idx === deletedIdx) cardClass += ' is-deleted';
      if (idx === highlightTarget) cardClass += ' is-target';

      html += `
        <div class="ll-node-wrapper">
          <div class="${cardClass}">
            <div class="ll-node-id">${node.id}</div>
            <div class="ll-node-name">${node.name}</div>
            <div class="ll-node-gpa">GPA: ${node.gpa}</div>
            ${idx === headIdx ? '<span class="ll-badge head-badge">HEAD</span>' : ''}
            ${idx === currentIdx ? '<span class="ll-badge curr-badge">CURR</span>' : ''}
            ${idx === prevIdx ? '<span class="ll-badge prev-badge">PREV</span>' : ''}
          </div>
          ${idx < nodes.length - 1 ? '<div class="ll-pointer-arrow">➔</div>' : '<div class="ll-null-badge">None</div>'}
        </div>
      `;
    });

    html += '</div>';
    container.innerHTML = html;
  }

  function createQueueSteps() {
    const capacity = 6;
    let arr = [null, 20, 30, 40, null, null];
    let front = 1, rear = 3, size = 3;
    const steps = [];

    steps.push({
      line: 3,
      explanation: '🔄 <b>Circular Array Queue</b>: คิวแบบวงกลมขนาด 6 ช่อง (Front = 1, Rear = 3, Size = 3)',
      vars: { front, rear, size, capacity },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'init' }
    });

    // Dequeue 20
    arr[1] = null;
    front = (front + 1) % capacity;
    size--;
    steps.push({
      line: 15,
      explanation: '📤 <b>dequeue()</b>: นำ 20 ออกจากตำแหน่ง front -> เลื่อน <code>front = (1 + 1) % 6 = 2</code>',
      vars: { dequeued: 20, front, rear, size },
      visualData: { arr: [...arr], front, rear, size, capacity, op: 'dequeue' }
    });

    // Enqueue 50, 60, 70 (Wrap around)
    const toEnq = [50, 60, 70];
    toEnq.forEach(v => {
      rear = (rear + 1) % capacity;
      arr[rear] = v;
      size++;
      steps.push({
        line: 21,
        explanation: `📥 <b>enqueue(${v})</b>: เลื่อน <code>rear = (rear + 1) % 6 = ${rear}</code> ${rear === 0 ? '🔥 <b>Circular Wrap Around สู่ index 0!</b>' : ''}`,
        vars: { enqueued: v, front, rear, size },
        visualData: { arr: [...arr], front, rear, size, capacity, op: 'enqueue', enqIdx: rear }
      });
    });

    return steps;
  }

  function renderQueue(container, visualData) {
    const { arr, front, rear, size, capacity, enqIdx } = visualData;
    let html = `
      <div class="queue-meta-bar">
        <div class="q-stat"><span>Capacity:</span> <b>${capacity}</b></div>
        <div class="q-stat"><span>Size:</span> <b>${size}</b></div>
        <div class="q-stat"><span>Front:</span> <b style="color:#06b6d4;">${front}</b></div>
        <div class="q-stat"><span>Rear:</span> <b style="color:#a855f7;">${rear}</b></div>
      </div>
      <div class="queue-slots-grid">
    `;

    arr.forEach((val, idx) => {
      const isFront = idx === front && size > 0;
      const isRear = idx === rear && size > 0;
      let slotClass = 'q-slot';
      if (val !== null) slotClass += ' filled';
      if (idx === enqIdx) slotClass += ' just-enq';

      let badges = '';
      if (isFront && isRear) badges = '<span class="q-badge both">F & R</span>';
      else if (isFront) badges = '<span class="q-badge front">FRONT</span>';
      else if (isRear) badges = '<span class="q-badge rear">REAR</span>';

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

  function createSortingSteps() {
    const arr = [64, 34, 25, 12, 22, 11, 90];
    const steps = [];
    steps.push({
      line: 3,
      explanation: '📊 <b>Bubble Sort</b>: เริ่มต้นเปรียบเทียบข้อมูล 7 จำนวนเพื่อเรียงจากน้อยไปหามาก',
      vars: { array: arr.join(', ') },
      visualData: { arr: [...arr], comparing: [-1, -1], sortedIdx: -1 }
    });

    const a = [...arr];
    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < a.length - 1 - i; j++) {
        steps.push({
          line: 7,
          explanation: `🔍 เปรียบเทียบ <code>a[${j}] (${a[j]})</code> กับ <code>a[${j+1}] (${a[j+1]})</code>`,
          vars: { 'a[j]': a[j], 'a[j+1]': a[j+1] },
          visualData: { arr: [...a], comparing: [j, j + 1], sortedIdx: a.length - i }
        });
        if (a[j] > a[j + 1]) {
          const temp = a[j];
          a[j] = a[j + 1];
          a[j + 1] = temp;
          steps.push({
            line: 9,
            explanation: `🔄 สลับตำแหน่ง: ${a[j + 1]} > ${a[j]}`,
            vars: { swapped: `${a[j]} <-> ${a[j+1]}` },
            visualData: { arr: [...a], comparing: [j, j + 1], sortedIdx: a.length - i }
          });
        }
      }
    }

    return steps;
  }

  function renderSorting(container, visualData) {
    const { arr, comparing, sortedIdx } = visualData;
    const maxVal = Math.max(...arr, 100);

    let html = '<div class="sorting-bars-container">';
    arr.forEach((v, idx) => {
      const isComp = comparing && comparing.includes(idx);
      const isSorted = sortedIdx !== undefined && idx >= sortedIdx;
      const heightPercent = Math.max(15, (v / maxVal) * 100);

      html += `
        <div class="sorting-bar-col">
          <span class="bar-val">${v}</span>
          <div class="sorting-bar ${isComp ? 'is-comparing' : ''} ${isSorted ? 'is-sorted' : ''}" 
               style="height:${heightPercent}%;"></div>
          <span class="bar-idx">[${idx}]</span>
        </div>
      `;
    });
    html += '</div>';
    container.innerHTML = html;
  }

  function createDijkstraSteps() {
    const steps = [];
    steps.push({
      line: 3,
      explanation: '🕸️ <b>Dijkstra Shortest Path</b>: คำนวณระยะทางสั้นสุดจาก Node A ไปยังทุกโหนด',
      vars: { start_node: 'A', 'dist[A]': 0 },
      visualData: { activeNode: 'A', visited: ['A'] }
    });
    return steps;
  }

  function renderDijkstra(container, visualData) {
    container.innerHTML = `
      <div style="padding:24px; text-align:center; color:var(--text-secondary);">
        <h3>🕸️ Dijkstra Algorithm Visualizer</h3>
        <p>โหนดเริ่มต้น: <b>${visualData.activeNode || 'A'}</b> | ปล่อยคลื่นตรวจจับเส้นทางสั้นสุดผ่าน Priority Queue</p>
      </div>
    `;
  }

  // =========================================================================
  // EXAM CODE SNIPPETS (Directly synchronized with Exams/*.py)
  // =========================================================================
  const EXAM_CODE_SNIPPETS = {
    assign3_heap: {
      filename: 'Exams/Heap.py',
      lines: [
        '# Exams/Heap.py — Binary Min-Heap Implementation',
        'class BinaryHeap:',
        '    def __init__(self, capacity = 100):',
        '        self.array = [None] * (capacity + 1)',
        '        self.currentSize = 0',
        '',
        '    def insert(self, x):',
        '        self.currentSize += 1',
        '        hole = self.currentSize',
        '        while hole > 1 and x < self.array[hole // 2]:',
        '            self.array[hole] = self.array[hole // 2]',
        '            hole //= 2',
        '        self.array[hole] = x',
        '',
        '    def delete_min(self):',
        '        min_item = self.array[1]',
        '        self.array[1] = self.array[self.currentSize]',
        '        self.currentSize -= 1',
        '        self._percolate_down(1)',
        '        return min_item',
        '',
        '    def _percolate_down(self, hole):',
        '        temp = self.array[hole]',
        '        while hole * 2 <= self.currentSize:',
        '            child = hole * 2',
        '            if child != self.currentSize and self.array[child + 1] < self.array[child]:',
        '                child += 1',
        '            if self.array[child] < temp:',
        '                self.array[hole] = self.array[child]',
        '            else:',
        '                break',
        '            hole = child',
        '        self.array[hole] = temp'
      ]
    },
    lecture5_bst_delete: {
      filename: 'Exams/BinarySearchTrees.py',
      lines: [
        '# Exams/BinarySearchTrees.py — Binary Search Tree Deletion',
        'class Node:',
        '    def __init__(self, value):',
        '        self.value = value',
        '        self.left = None',
        '        self.right = None',
        '',
        'class BinarySearchTree:',
        '    def __init__(self):',
        '        self.root = None',
        '',
        '    def insert(self, value):',
        '        if self.root is None: self.root = Node(value)',
        '        else: self._insert_recursive(self.root, value)',
        '',
        '    def _insert_recursive(self, current_node: Node, value):',
        '        if value < current_node.value:',
        '            if current_node.left is None:',
        '                current_node.left = Node(value)',
        '            else:',
        '                self._insert_recursive(current_node.left, value)',
        '        elif value > current_node.value:',
        '            if current_node.right is None:',
        '                current_node.right = Node(value)',
        '            else:',
        '                self._insert_recursive(current_node.right, value)',
        '',
        '    def delete(self, value):',
        '        self.root = self._delete_recursive(self.root, value)',
        '',
        '    def _delete_recursive(self, current_node: Node, value):',
        '        if current_node is None: return current_node',
        '        if value < current_node.value:',
        '            current_node.left = self._delete_recursive(current_node.left, value)',
        '        elif value > current_node.value:',
        '            current_node.right = self._delete_recursive(current_node.right, value)',
        '        else:',
        '            # Case 1 & 2: 0 or 1 child',
        '            if current_node.left is None: return current_node.right',
        '            elif current_node.right is None: return current_node.left',
        '            # Case 3: 2 children -> In-order Successor',
        '            temp_node = self._min_value_node(current_node.right)',
        '            current_node.value = temp_node.value',
        '            current_node.right = self._delete_recursive(current_node.right, temp_node.value)',
        '        return current_node',
        '',
        '    def _min_value_node(self, current_node: Node) -> Node:',
        '        if current_node.left is None: return current_node',
        '        return self._min_value_node(current_node.left)'
      ]
    },
    stack_postfix: {
      filename: 'Exams/InfixToPostFix.py',
      lines: [
        '# Exams/InfixToPostFix.py — Infix to Postfix Converter',
        'def infix_to_postfix(expression):',
        '    stack = []',
        '    postfix = []',
        '    for token in expression:',
        '        if token.isalnum():',
        '            postfix.append(token)',
        '        elif token == "(": ',
        '            stack.append(token)',
        '        elif token == ")":',
        '            while stack and stack[-1] != "(": postfix.append(stack.pop())',
        '            stack.pop()',
        '        else:',
        '            while stack and precedence(stack[-1]) >= precedence(token):',
        '                postfix.append(stack.pop())',
        '            stack.push(token)',
        '    while stack: postfix.append(stack.pop())',
        '    return "".join(postfix)'
      ]
    },
    exam_hash: {
      filename: 'Exams/Hash.py',
      lines: [
        '# Exams/Hash.py — ASCII Sum & Modulo Hash Function',
        'def hash(key, table_size):',
        '    hash_val = 0',
        '    for char in key:',
        '        hash_val += ord(char)',
        '    return hash_val % table_size',
        '',
        'if __name__ == "__main__":',
        '    print(hash("AB", 10))'
      ]
    },
    assign1_linkedlist: {
      filename: 'Exams/LinkedList/612037.py',
      lines: [
        '# Exams/LinkedList/612037.py — Singly Linked List',
        'class LinkedList:',
        '    def delete(self, item):',
        '        curr = self.head',
        '        prev = None',
        '        while curr and curr.student_id != item:',
        '            prev = curr',
        '            curr = curr.next',
        '        if not curr: return False',
        '        if not prev: self.head = curr.next',
        '        else: prev.next = curr.next',
        '        return True'
      ]
    }
  };

  // =========================================================================
  // PUBLIC API DISPATCHER
  // =========================================================================
  return {
    getStepsForExercise: function (exId) {
      if (exId === 'assign3_heap') return createHeapDefaultSteps();
      if (exId === 'lecture5_bst_delete') return createBstDefaultSteps();
      if (exId === 'exam_hash') return createHashSteps('HELLO', 10);
      if (exId === 'stack_postfix') return createStackSteps('(A + B) * C - D / E');
      if (exId === 'assign1_linkedlist') return createLinkedListSteps();
      if (exId === 'test1_queue') return createQueueSteps();
      if (exId === 'test2_sorting') return createSortingSteps();
      if (exId === 'assign4_dijkstra') return createDijkstraSteps();
      return createHeapDefaultSteps();
    },

    executeDynamicAction: function (exId, action, val) {
      if (exId === 'assign3_heap') {
        if (action === 'insert') return createHeapInsertSteps(val);
        if (action === 'delete') return createHeapDeleteMinSteps();
        if (action === 'search') return createHeapFindMinSteps();
        if (action === 'preset') return resetHeapToExamPreset();
        if (action === 'toggle_type') {
          heapType = heapType === 'min' ? 'max' : 'min';
          return createHeapDefaultSteps(`สลับโหมดเป็น Binary ${heapType === 'min' ? 'Min-Heap' : 'Max-Heap'}`);
        }
        if (action === 'clear') {
          setHeapState([0]);
          return createHeapDefaultSteps('ล้างข้อมูลในฮีปเรียบร้อย');
        }
        if (action === 'random') {
          const nums = [];
          for (let k = 0; k < 8; k++) nums.push(Math.floor(Math.random() * 80) + 10);
          setHeapState([0, ...nums]);
          return createHeapDefaultSteps('สุ่มชุดข้อมูลตัวเลขใหม่ 8 ค่า');
        }
      }

      if (exId === 'lecture5_bst_delete') {
        if (action === 'insert') return createDynamicBstInsertSteps(val);
        if (action === 'delete') return createDynamicBstDeleteSteps(val);
        if (action === 'preset') { initBstPreset(); return createBstDefaultSteps('รีเซ็ต BST ตามตัวอย่างข้อสอบ'); }
        if (action === 'clear') { bstRoot = null; return createBstDefaultSteps('ล้างข้อมูลต้นไม้ BST เรียบร้อย'); }
        if (action === 'random') {
          initBstPreset();
          return createBstDefaultSteps();
        }
      }

      if (exId === 'exam_hash') {
        if (action === 'insert' || action === 'search') return createHashSteps(val || 'HELLO', hashCapacity);
        if (action === 'preset') return resetHashTable();
        if (action === 'toggle_type') {
          hashStrategy = hashStrategy === 'chaining' ? 'linear_probing' : 'chaining';
          return createHashSteps(val || 'HELLO', hashCapacity);
        }
        if (action === 'clear') {
          hashBuckets = Array.from({ length: hashCapacity }, () => []);
          return createHashSteps('', hashCapacity);
        }
      }

      if (exId === 'stack_postfix') {
        if (action === 'insert' || action === 'search' || action === 'preset') {
          return createStackSteps(val || '(A + B) * C - D / E');
        }
      }

      return null;
    },

    getCodeSnippetForExercise: function (exId) {
      return EXAM_CODE_SNIPPETS[exId] || EXAM_CODE_SNIPPETS.assign3_heap;
    },

    renderVisualizer: function (container, exType, visualData) {
      if (!container || !visualData) return;
      if (exType === 'heap') renderHeap(container, visualData);
      else if (exType === 'bst') renderBst(container, visualData);
      else if (exType === 'hash') renderHash(container, visualData);
      else if (exType === 'stack') renderStack(container, visualData);
      else if (exType === 'linked_list') renderLinkedList(container, visualData);
      else if (exType === 'queue') renderQueue(container, visualData);
      else if (exType === 'sorting') renderSorting(container, visualData);
      else if (exType === 'dijkstra') renderDijkstra(container, visualData);
      else renderHeap(container, visualData);
    }
  };
})();
