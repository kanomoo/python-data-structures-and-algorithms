/**
 * DSA Interactive Studio & Visualizer Engine for Wiki
 * Provides embedded interactive visualizers (Linked List, BST, Min-Heap, Queue, Hash, Sort)
 * with dynamic value inputs, step-by-step debugging, SVG animations, and live variable inspection.
 */

window.DsaWikiStudio = (function () {
  'use strict';

  // State registry for mounted widgets
  const widgetInstances = {};

  function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function renderCodeDebugger(container, codeLines, activeLine) {
    if (!container) return;
    const linesContainer = container.querySelector('.code-trace-lines');
    const lineBadge = container.querySelector('.active-code-line-num');
    
    if (lineBadge) {
      lineBadge.textContent = (activeLine && activeLine > 0) ? activeLine : '-';
    }

    if (linesContainer && codeLines) {
      const currentSig = codeLines.join('\n');
      if (linesContainer.dataset.sig !== currentSig) {
        linesContainer.dataset.sig = currentSig;
        let html = '';
        codeLines.forEach((line, idx) => {
          const lineNo = idx + 1;
          html += `<div class="code-trace-line" data-line="${lineNo}"><span class="line-num">${lineNo}</span><span class="line-text">${escapeHtml(line)}</span><span class="line-arrow">◀</span></div>`;
        });
        linesContainer.innerHTML = html;
      }

      const allLines = linesContainer.querySelectorAll('.code-trace-line');
      let activeElem = null;
      allLines.forEach(el => {
        const lineNo = parseInt(el.getAttribute('data-line'), 10);
        if (lineNo === activeLine) {
          el.classList.add('active');
          activeElem = el;
        } else {
          el.classList.remove('active');
        }
      });

      if (activeElem) {
        activeElem.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }
  }


  // =========================================================================
  // 1. LINKED LIST STUDIO (Singly & Doubly with Custom Value Input)
  // =========================================================================
  class LinkedListSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      this.mode = 'singly'; // 'singly' or 'doubly'
      this.nodes = [
        { id: '0x100', val: 10 },
        { id: '0x140', val: 20 },
        { id: '0x180', val: 30 }
      ];
      this.addressCounter = 0x200;
      this.steps = [];
      this.currentStep = 0;
      this.timer = null;
      this.isPlaying = false;
      this.codeLines = [
        'def insert_at(self, index, item):',
        '    new_node = Node(item)',
        '    if index == 0:',
        '        new_node.next = self.head; self.head = new_node; return',
        '    curr = self.head',
        '    for _ in range(index - 1): curr = curr.next',
        '    new_node.next = curr.next',
        '    curr.next = new_node',
        '',
        'def remove(self, target):',
        '    curr, prev = self.head, None',
        '    while curr and curr.data != target:',
        '        prev = curr; curr = curr.next',
        '    if prev is None: self.head = curr.next',
        '    else: prev.next = curr.next'
      ];
      this.initDefaultSteps();
    }

    nextAddr() {
      const addr = '0x' + this.addressCounter.toString(16).toUpperCase();
      this.addressCounter += 0x40;
      return addr;
    }

    initDefaultSteps() {
      this.steps = [{
        title: 'สถานะเริ่มต้น (Initial State)',
        explanation: `Linked List ปัจจุบันมี ${this.nodes.length} โหนด (head ชี้ที่ ${this.nodes[0] ? this.nodes[0].id : 'None'})`,
        nodes: JSON.parse(JSON.stringify(this.nodes)),
        currIdx: -1,
        prevIdx: -1,
        targetIdx: -1,
        deletedIdx: -1,
        headIdx: 0,
        vars: { head: this.nodes[0] ? this.nodes[0].id : 'None', size: this.nodes.length, curr: 'None', prev: 'None' }
      }];
      this.currentStep = 0;
    }

    insertHead(val) {
      this.pause();
      const newAddr = this.nextAddr();
      const newNode = { id: newAddr, val: Number(val) || val };
      const currentList = JSON.parse(JSON.stringify(this.nodes));

      this.steps = [
        {
          title: 'สเต็ป 1: สร้างโหนดใหม่ (Create Node)',
          explanation: `สร้างโหนดใหม่ new_node = Node(${newNode.val}) ที่หน่วยความจำ ${newAddr}`,
          nodes: [newNode, ...currentList],
          currIdx: 0,
          prevIdx: -1,
          headIdx: 1,
          vars: { new_node: newAddr, val: newNode.val, head: currentList[0] ? currentList[0].id : 'None' }
        },
        {
          title: 'สเต็ป 2: เชื่อมพอยน์เตอร์ new_node.next = head',
          explanation: `กำหนดให้ new_node.next ชี้ไปยังโหนดเดิมที่ตำแหน่ง head (${currentList[0] ? currentList[0].id : 'None'})`,
          nodes: [newNode, ...currentList],
          currIdx: 0,
          prevIdx: -1,
          headIdx: 1,
          vars: { 'new_node.next': currentList[0] ? currentList[0].id : 'None', head: currentList[0] ? currentList[0].id : 'None' }
        },
        {
          title: 'สเต็ป 3: อัปเดต head = new_node',
          explanation: `เลื่อนตัวแปร head ให้ชี้มายังโหนดใหม่ ${newAddr} สำเร็จ! ความยาว List เพิ่มเป็น ${currentList.length + 1}`,
          nodes: [newNode, ...currentList],
          currIdx: -1,
          prevIdx: -1,
          headIdx: 0,
          vars: { head: newAddr, size: currentList.length + 1 }
        }
      ];

      this.nodes.unshift(newNode);
      this.currentStep = 0;
      this.render();
    }

    insertTail(val) {
      this.pause();
      const newAddr = this.nextAddr();
      const newNode = { id: newAddr, val: Number(val) || val };
      const currentList = JSON.parse(JSON.stringify(this.nodes));
      this.steps = [];

      if (currentList.length === 0) {
        this.insertHead(val);
        return;
      }

      // Step: Start traversal
      this.steps.push({
        title: 'สเต็ป 1: ตั้งตัวชี้ curr = head เพื่อท่องหาจุดสิ้นสุด',
        explanation: `เริ่มตั้ง curr ที่ head (${currentList[0].id}) เตรียมวนลูป while curr.next is not None:`,
        nodes: JSON.parse(JSON.stringify(currentList)),
        currIdx: 0,
        prevIdx: -1,
        headIdx: 0,
        vars: { curr: currentList[0].id, head: currentList[0].id }
      });

      for (let i = 1; i < currentList.length; i++) {
        this.steps.push({
          title: `สเต็ป 2.${i}: เลื่อน curr = curr.next`,
          explanation: `โหนดที่ ${i - 1} (${currentList[i - 1].val}) ยังมี next -> ขยับ curr ไปที่โหนด ${i} (${currentList[i].id})`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: i,
          prevIdx: i - 1,
          headIdx: 0,
          vars: { curr: currentList[i].id, prev: currentList[i - 1].id }
        });
      }

      // Step: At tail, connect
      this.steps.push({
        title: 'สเต็ป 3: พบโหนดท้ายสุด สั่ง curr.next = new_node',
        explanation: `curr (${currentList[currentList.length - 1].id}) ไม่มี next แล้ว! เชื่อม curr.next = ${newAddr} (ค่า ${newNode.val})`,
        nodes: [...currentList, newNode],
        currIdx: currentList.length - 1,
        prevIdx: -1,
        headIdx: 0,
        vars: { 'curr.next': newAddr, new_node: newAddr, size: currentList.length + 1 }
      });

      this.nodes.push(newNode);
      this.currentStep = 0;
      this.render();
    }

    deleteVal(targetVal) {
      this.pause();
      const target = Number(targetVal) || targetVal;
      const currentList = JSON.parse(JSON.stringify(this.nodes));
      this.steps = [];

      if (currentList.length === 0) {
        this.steps.push({
          title: 'ล้มเหลว: List ว่างเปล่า',
          explanation: 'ไม่สามารถลบข้อมูลได้เนื่องจากไม่มีโหนดใน List (head = None)',
          nodes: [],
          currIdx: -1,
          prevIdx: -1,
          headIdx: -1,
          vars: { error: 'List is empty' }
        });
        this.currentStep = 0;
        this.render();
        return;
      }

      // Check if target is at Head
      if (currentList[0].val === target) {
        this.steps.push({
          title: 'สเต็ป 1: ตรวจพบว่าโหนดเป้าหมายอยู่ที่ Head',
          explanation: `head.val == ${target} -> ข้อมูลตรงกันตั้งแต่ตัวแรก!`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: 0,
          prevIdx: -1,
          targetIdx: 0,
          headIdx: 0,
          vars: { head: currentList[0].id, target }
        });

        this.steps.push({
          title: 'สเต็ป 2: เลื่อน head = head.next',
          explanation: `เลื่อน head ข้ามโหนดแรกไปยังโหนดถัดไป (${currentList[1] ? currentList[1].id : 'None'}) โหนดเดิมจะถูกลบออกจาก List`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: -1,
          prevIdx: -1,
          deletedIdx: 0,
          headIdx: 1,
          vars: { head: currentList[1] ? currentList[1].id : 'None', size: currentList.length - 1 }
        });

        currentList.shift();
        this.nodes = currentList;
        this.steps.push({
          title: 'สเต็ป 3: ลบสำเร็จ',
          explanation: `โหนดค่า ${target} ถูกปลดจากหน่วยความจำเรียบร้อยแล้ว`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: -1,
          prevIdx: -1,
          headIdx: 0,
          vars: { size: currentList.length }
        });

        this.currentStep = 0;
        this.render();
        return;
      }

      // Traverse to find node with prev and curr
      let foundIdx = -1;
      let prevIdx = -1;
      let currIdx = 0;

      this.steps.push({
        title: 'สเต็ป 1: เริ่มต้นท่องค้นหาด้วยตัวชี้คู่ (prev = None, curr = head)',
        explanation: `ตั้ง prev = None, curr = head (${currentList[0].id}) ตรวจสอบ curr.val == ${target}`,
        nodes: JSON.parse(JSON.stringify(currentList)),
        currIdx: 0,
        prevIdx: -1,
        headIdx: 0,
        vars: { prev: 'None', curr: currentList[0].id, target }
      });

      for (let i = 1; i < currentList.length; i++) {
        prevIdx = i - 1;
        currIdx = i;

        if (currentList[i].val === target) {
          foundIdx = i;
          this.steps.push({
            title: `สเต็ป ${i + 1}: 🎉 พบโหนดเป้าหมายที่ curr (index ${i})`,
            explanation: `curr.val == ${target} (${currentList[i].id}) ตรงกับค่าที่ต้องการลบ! โหนดก่อนหน้าคือ prev (${currentList[prevIdx].id})`,
            nodes: JSON.parse(JSON.stringify(currentList)),
            currIdx: currIdx,
            prevIdx: prevIdx,
            targetIdx: currIdx,
            headIdx: 0,
            vars: { prev: currentList[prevIdx].id, curr: currentList[currIdx].id, match: true }
          });
          break;
        } else {
          this.steps.push({
            title: `สเต็ป ${i + 1}: ข้อมูลไม่ตรง เลื่อน prev = curr, curr = curr.next`,
            explanation: `โหนดที่ ${i} (ค่า ${currentList[i].val}) != ${target} -> เลื่อนตัวชี้คู่ไปข้างหน้า`,
            nodes: JSON.parse(JSON.stringify(currentList)),
            currIdx: currIdx,
            prevIdx: prevIdx,
            headIdx: 0,
            vars: { prev: currentList[prevIdx].id, curr: currentList[currIdx].id, target }
          });
        }
      }

      if (foundIdx !== -1) {
        // Step: Bypass node
        this.steps.push({
          title: `สเต็ปสำคัญ: ปลดพอยน์เตอร์ prev.next = curr.next`,
          explanation: `สั่ง prev.next = curr.next -> โหนด ${currentList[prevIdx].id} จะชี้ข้ามไปยัง ${currentList[foundIdx + 1] ? currentList[foundIdx + 1].id : 'None'} ทำให้โหนด ${currentList[foundIdx].id} ถูกตัดออกจากสายโยง!`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: -1,
          prevIdx: prevIdx,
          deletedIdx: foundIdx,
          headIdx: 0,
          vars: { 'prev.next': currentList[foundIdx + 1] ? currentList[foundIdx + 1].id : 'None', deleted: currentList[foundIdx].id }
        });

        currentList.splice(foundIdx, 1);
        this.nodes = currentList;

        this.steps.push({
          title: 'ลบเสร็จสมบูรณ์',
          explanation: `การลบสำเร็จ ปัจจุบัน Linked List เหลือทั้งหมด ${currentList.length} โหนด`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: -1,
          prevIdx: -1,
          headIdx: 0,
          vars: { size: currentList.length, head: currentList[0] ? currentList[0].id : 'None' }
        });
      } else {
        this.steps.push({
          title: 'ไม่พบข้อมูลใน List',
          explanation: `ท่องค้นหาจนสุด List (curr is None) ไม่พบโหนดที่มีค่า ${target}`,
          nodes: JSON.parse(JSON.stringify(currentList)),
          currIdx: -1,
          prevIdx: -1,
          headIdx: 0,
          vars: { found: false, target }
        });
      }

      this.currentStep = 0;
      this.render();
    }

    reset() {
      this.pause();
      this.nodes = [
        { id: '0x100', val: 10 },
        { id: '0x140', val: 20 },
        { id: '0x180', val: 30 }
      ];
      this.addressCounter = 0x200;
      this.initDefaultSteps();
      this.render();
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      } else {
        this.pause();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    play() {
      if (this.isPlaying) {
        this.pause();
        return;
      }
      this.isPlaying = true;
      const playBtn = document.getElementById(`${this.containerId}-play`);
      if (playBtn) playBtn.innerHTML = '⏸ หยุด (Pause)';

      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1200);
    }

    pause() {
      this.isPlaying = false;
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
      const playBtn = document.getElementById(`${this.containerId}-play`);
      if (playBtn) playBtn.innerHTML = '▶ เล่น (Play)';
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];
      const nodes = step.nodes || [];

      // Update Step Counter & Explanation
      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      // Update Buttons
      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      // Render Variables Watch Table
      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows || '<tr><td colspan="2" style="text-align:center;color:var(--text-muted);">ไม่มีตัวแปร</td></tr>';
      }

      // Render Graphical Nodes
      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      if (nodes.length === 0) {
        canvasEl.innerHTML = '<div class="studio-empty">List ว่างเปล่า (head = None)</div>';
        return;
      }

      let nodesHtml = '<div class="studio-ll-chain">';
      nodes.forEach((node, idx) => {
        let isCurr = idx === step.currIdx;
        let isPrev = idx === step.prevIdx;
        let isTarget = idx === step.targetIdx;
        let isDeleted = idx === step.deletedIdx;
        let isHead = idx === step.headIdx && !isDeleted;

        let badges = [];
        if (isHead) badges.push('<span class="ll-badge head">HEAD</span>');
        if (isCurr) badges.push('<span class="ll-badge curr">CURR 📍</span>');
        if (isPrev) badges.push('<span class="ll-badge prev">PREV 📍</span>');
        if (isTarget) badges.push('<span class="ll-badge target">🎯 TARGET</span>');
        if (idx === nodes.length - 1 && !isDeleted) badges.push('<span class="ll-badge tail">TAIL</span>');

        let cardClass = 'studio-ll-node';
        if (isCurr) cardClass += ' highlight-curr';
        if (isPrev) cardClass += ' highlight-prev';
        if (isDeleted) cardClass += ' highlight-deleted';
        if (isTarget) cardClass += ' highlight-target';

        const isDoubly = this.mode === 'doubly';
        const prevAddr = idx > 0 ? nodes[idx - 1].id : 'None';
        const nextAddr = idx < nodes.length - 1 ? nodes[idx + 1].id : 'None';

        nodesHtml += `
          <div class="studio-ll-node-wrapper">
            <div class="studio-ll-badges">${badges.join(' ')}</div>
            <div class="${cardClass}">
              <div class="studio-node-addr">${node.id}</div>
              <div class="studio-node-body ${isDoubly ? 'is-doubly' : ''}">
                ${isDoubly ? `<div class="node-cell cell-prev" title="prev pointer">prev: ${prevAddr}</div>` : ''}
                <div class="node-cell cell-data" title="node data"><b>${node.val}</b></div>
                <div class="node-cell cell-next" title="next pointer">next: ${nextAddr}</div>
              </div>
            </div>
            ${idx < nodes.length - 1 ? `
              <div class="studio-ll-arrow ${isPrev && step.deletedIdx !== -1 ? 'is-bypassing' : ''}">
                ${isDoubly ? '⇄' : '➔'}
              </div>
            ` : `
              <div class="studio-ll-null">➔ <span class="null-pill">None</span></div>
            `}
          </div>
        `;
      });
      nodesHtml += '</div>';
      canvasEl.innerHTML = nodesHtml;
      renderCodeDebugger(container, this.codeLines, step.line || 1);
    }
  }

  // =========================================================================
  // 2. BINARY SEARCH TREE (BST) STUDIO
  // =========================================================================
  class BstSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      this.tree = null;
      this.steps = [];
      this.currentStep = 0;
      this.timer = null;
      this.isPlaying = false;
      this.codeLines = [
        'def insert(self, current, val):',
        '    if current is None: return Node(val)',
        '    if val < current.value:',
        '        current.left = self.insert(current.left, val)',
        '    elif val > current.value:',
        '        current.right = self.insert(current.right, val)',
        '    return current',
        '',
        'def delete(self, current, val):',
        '    if val < current.value: current.left = self.delete(current.left, val)',
        '    elif val > current.value: current.right = self.delete(current.right, val)',
        '    else:',
        '        if current.left is None: return current.right',
        '        if current.right is None: return current.left',
        '        succ = self.min_node(current.right) # Inorder Successor',
        '        current.value = succ.value',
        '        current.right = self.delete(current.right, succ.value)',
        '    return current'
      ];
      this.loadPreset();
    }

    loadPreset() {
      this.pause();
      this.tree = null;
      const initialVals = [50, 30, 70, 20, 40, 60, 80];
      initialVals.forEach(v => { this.tree = this._insertNode(this.tree, v); });
      this.steps = [{
        title: 'โครงสร้างเริ่มต้น (Initial BST Preset)',
        explanation: 'ต้นไม้ค้นหาแบบทวิภาค (BST) บรรจุ 7 โหนดตามกฎ: ซ้าย < พ่อ < ขวา',
        activeVal: null,
        path: [],
        treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
        vars: { root: 50, count: 7 }
      }];
      this.currentStep = 0;
      this.render();
    }

    _insertNode(root, val) {
      if (!root) return { val, left: null, right: null };
      if (val < root.val) root.left = this._insertNode(root.left, val);
      else if (val > root.val) root.right = this._insertNode(root.right, val);
      return root;
    }

    insert(val) {
      this.pause();
      const num = Number(val);
      if (isNaN(num)) return;

      this.steps = [];
      let curr = this.tree;
      let path = [];

      this.steps.push({
        title: `สเต็ป 1: เริ่มค้นหาตำแหน่งแทรกค่า ${num} จาก Root`,
        explanation: `เริ่มต้นตรวจสอบที่รากต้นไม้ (Root = ${this.tree ? this.tree.val : 'None'})`,
        activeVal: this.tree ? this.tree.val : null,
        path: [...path],
        treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
        vars: { insert_val: num, curr: this.tree ? this.tree.val : 'None' }
      });

      while (curr) {
        path.push(curr.val);
        if (num === curr.val) {
          this.steps.push({
            title: `พบค่าซ้ำ (${num})`,
            explanation: `ค่า ${num} มีอยู่ใน BST แล้ว (BST ปกติไม่เก็บค่าซ้ำ)`,
            activeVal: curr.val,
            path: [...path],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { status: 'Duplicate key' }
          });
          this.currentStep = 0;
          this.render();
          return;
        }

        if (num < curr.val) {
          this.steps.push({
            title: `${num} < ${curr.val} -> เลี้ยวซ้าย (Go Left)`,
            explanation: `ค่าที่ต้องการแทรก (${num}) น้อยกว่าโหนดปัจจุบัน (${curr.val}) ให้ลงไปยัง Subtree ด้านซ้าย`,
            activeVal: curr.left ? curr.left.val : null,
            path: [...path],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { curr: curr.val, dir: 'left', next: curr.left ? curr.left.val : 'Empty slot' }
          });
          if (!curr.left) break;
          curr = curr.left;
        } else {
          this.steps.push({
            title: `${num} > ${curr.val} -> เลี้ยวขวา (Go Right)`,
            explanation: `ค่าที่ต้องการแทรก (${num}) มากกว่าโหนดปัจจุบัน (${curr.val}) ให้ลงไปยัง Subtree ด้านขวา`,
            activeVal: curr.right ? curr.right.val : null,
            path: [...path],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { curr: curr.val, dir: 'right', next: curr.right ? curr.right.val : 'Empty slot' }
          });
          if (!curr.right) break;
          curr = curr.right;
        }
      }

      this.tree = this._insertNode(this.tree, num);

      this.steps.push({
        title: `สเต็ปสุดท้าย: สร้างโหนดใหม่สำเร็จ!`,
        explanation: `สร้าง Node(${num}) และเชื่อมต่อเข้ากับต้นไม้เรียบร้อย`,
        activeVal: num,
        path: [...path, num],
        treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
        vars: { inserted: num, status: 'Success' }
      });

      this.currentStep = 0;
      this.render();
    }

    search(val) {
      this.pause();
      const num = Number(val);
      if (isNaN(num)) return;

      this.steps = [];
      let curr = this.tree;
      let path = [];
      let found = false;

      while (curr) {
        path.push(curr.val);
        if (num === curr.val) {
          found = true;
          this.steps.push({
            title: `🎉 ค้นพบโหนดเป้าหมาย (${num})!`,
            explanation: `ค่า ${num} ตรงกับโหนดปัจจุบัน ค้นหาสำเร็จ!`,
            activeVal: curr.val,
            path: [...path],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { found: true, val: num, depth: path.length - 1 }
          });
          break;
        } else if (num < curr.val) {
          this.steps.push({
            title: `${num} < ${curr.val} -> ค้นหาต่อทางซ้าย`,
            explanation: `เป้าหมาย ${num} น้อยกว่า ${curr.val} -> เลื่อนตัวชี้ไปที่ curr.left`,
            activeVal: curr.val,
            path: [...path],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { curr: curr.val, target: num, dir: 'left' }
          });
          curr = curr.left;
        } else {
          this.steps.push({
            title: `${num} > ${curr.val} -> ค้นหาต่อทางขวา`,
            explanation: `เป้าหมาย ${num} มากกว่า ${curr.val} -> เลื่อนตัวชี้ไปที่ curr.right`,
            activeVal: curr.val,
            path: [...path],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { curr: curr.val, target: num, dir: 'right' }
          });
          curr = curr.right;
        }
      }

      if (!found) {
        this.steps.push({
          title: `ไม่พบข้อมูล (${num}) ในต้นไม้`,
          explanation: `ท่องค้นหาจนถึงปลายทาง (None) แล้ว ไม่พบค่า ${num}`,
          activeVal: null,
          path: [...path],
          treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
          vars: { found: false, target: num }
        });
      }

      this.currentStep = 0;
      this.render();
    }

    deleteNode(val) {
      this.pause();
      const num = Number(val);
      if (isNaN(num)) return;

      this.steps = [];
      this.steps.push({
        title: `เริ่มกระบวนการลบค่า ${num}`,
        explanation: `เริ่มต้นค้นหาโหนดที่มีค่า ${num} เพื่อจำแนกเป็น 3 กรณี (Case 1: ใบ, Case 2: ลูก 1 คน, Case 3: ลูก 2 คน)`,
        activeVal: num,
        path: [],
        treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
        vars: { target: num }
      });

      // Execute deletion and record steps
      this.tree = this._deleteRec(this.tree, num);

      this.steps.push({
        title: `การลบโหนด ${num} เสร็จสมบูรณ์`,
        explanation: `ปรับปรุงโครงสร้างต้นไม้ BST เรียบร้อย ยังคงรักษาคุณสมบัติ ซ้าย < พ่อ < ขวา`,
        activeVal: null,
        path: [],
        treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
        vars: { deleted: num, status: 'Success' }
      });

      this.currentStep = 0;
      this.render();
    }

    _deleteRec(root, val) {
      if (!root) return null;
      if (val < root.val) {
        root.left = this._deleteRec(root.left, val);
      } else if (val > root.val) {
        root.right = this._deleteRec(root.right, val);
      } else {
        // Node found!
        // Case 1: Leaf node (no children)
        if (!root.left && !root.right) {
          this.steps.push({
            title: `กรณีที่ 1: โหนดใบ (Leaf Node)`,
            explanation: `โหนด ${val} ไม่มีลูกทั้งซ้ายและขวา สามารถตัดทิ้ง (return None) ได้ทันที`,
            activeVal: root.val,
            path: [root.val],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { case: 'Case 1: Leaf', node: val }
          });
          return null;
        }
        // Case 2: One child
        if (!root.left) {
          this.steps.push({
            title: `กรณีที่ 2: มีลูกคนเดียว (ขวา)`,
            explanation: `โหนด ${val} มีเฉพาะลูกขวา (${root.right.val}) ยกเอาลูกขวาขึ้นมาแทนที่พ่อ`,
            activeVal: root.val,
            path: [root.val],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { case: 'Case 2: Single child', replacement: root.right.val }
          });
          return root.right;
        }
        if (!root.right) {
          this.steps.push({
            title: `กรณีที่ 2: มีลูกคนเดียว (ซ้าย)`,
            explanation: `โหนด ${val} มีเฉพาะลูกซ้าย (${root.left.val}) ยกเอาลูกซ้ายขึ้นมาแทนที่พ่อ`,
            activeVal: root.val,
            path: [root.val],
            treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
            vars: { case: 'Case 2: Single child', replacement: root.left.val }
          });
          return root.left;
        }
        // Case 3: Two children
        // Find Inorder Successor (min in right subtree)
        let succ = root.right;
        while (succ.left) succ = succ.left;

        this.steps.push({
          title: `กรณีที่ 3: มีลูกครบ 2 คน (Inorder Successor)`,
          explanation: `โหนด ${val} มีลูก 2 คน! ต้องหาโหนดที่ค่าน้อยที่สุดใน Subtree ขวา คือ Inorder Successor = ${succ.val} นำมาแทนที่ แล้วลบโหนด ${succ.val} ตัวล่างทิ้ง`,
          activeVal: root.val,
          path: [root.val, succ.val],
          treeSnapshot: JSON.parse(JSON.stringify(this.tree)),
          vars: { case: 'Case 3: Two children', successor: succ.val }
        });

        root.val = succ.val;
        root.right = this._deleteRec(root.right, succ.val);
      }
      return root;
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      } else {
        this.pause();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    play() {
      if (this.isPlaying) {
        this.pause();
        return;
      }
      this.isPlaying = true;
      const playBtn = document.getElementById(`${this.containerId}-play`);
      if (playBtn) playBtn.innerHTML = '⏸ หยุด (Pause)';

      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1200);
    }

    pause() {
      this.isPlaying = false;
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
      const playBtn = document.getElementById(`${this.containerId}-play`);
      if (playBtn) playBtn.innerHTML = '▶ เล่น (Play)';
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];

      // Update Header & Exp
      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      // Update Buttons
      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      // Variables Watch
      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows || '<tr><td colspan="2" style="text-align:center;color:var(--text-muted);">ไม่มีตัวแปร</td></tr>';
      }

      // Render Tree SVG
      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      const treeToRender = step.treeSnapshot || this.tree;
      if (!treeToRender) {
        canvasEl.innerHTML = '<div class="studio-empty">BST ว่างเปล่า (Root = None)</div>';
        return;
      }

      const svgWidth = 640;
      const svgHeight = 260;
      const nodesData = [];
      const edgesData = [];

      function layout(node, x, y, dx, level) {
        if (!node) return;
        nodesData.push({ val: node.val, x, y });
        if (node.left) {
          const childX = x - dx;
          const childY = y + 55;
          edgesData.push({ x1: x, y1: y, x2: childX, y2: childY });
          layout(node.left, childX, childY, dx / 2, level + 1);
        }
        if (node.right) {
          const childX = x + dx;
          const childY = y + 55;
          edgesData.push({ x1: x, y1: y, x2: childX, y2: childY });
          layout(node.right, childX, childY, dx / 2, level + 1);
        }
      }

      layout(treeToRender, svgWidth / 2, 35, 140, 1);

      let svgHtml = `<svg width="100%" height="${svgHeight}" viewBox="0 0 ${svgWidth} ${svgHeight}" class="studio-tree-svg">`;
      edgesData.forEach(e => {
        svgHtml += `<line x1="${e.x1}" y1="${e.y1}" x2="${e.x2}" y2="${e.y2}" stroke="rgba(255,255,255,0.2)" stroke-width="2.5" />`;
      });

      nodesData.forEach(n => {
        const isPath = (step.path || []).includes(n.val);
        const isActive = step.activeVal === n.val;
        let fill = '#1e293b';
        let stroke = '#6366f1';
        let textColor = '#f8fafc';

        if (isActive) {
          fill = '#f59e0b';
          stroke = '#fbbf24';
          textColor = '#0f172a';
        } else if (isPath) {
          fill = '#4f46e5';
          stroke = '#818cf8';
        }

        svgHtml += `
          <g class="studio-node-group">
            <circle cx="${n.x}" cy="${n.y}" r="18" fill="${fill}" stroke="${stroke}" stroke-width="2.5" />
            <text x="${n.x}" y="${n.y + 5}" fill="${textColor}" font-size="13" font-weight="700" text-anchor="middle">${n.val}</text>
          </g>
        `;
      });
      svgHtml += '</svg>';

      // Inorder traversal result
      const inorderVals = [];
      function getInorder(node) {
        if (!node) return;
        getInorder(node.left);
        inorderVals.push(node.val);
        getInorder(node.right);
      }
      getInorder(treeToRender);

      canvasEl.innerHTML = `
        ${svgHtml}
        <div class="studio-tree-footer">
          <span class="tree-trav-label">Inorder Traversal (Sorted):</span>
          <span class="tree-trav-val">[ ${inorderVals.join(', ')} ]</span>
        </div>
      `;
      renderCodeDebugger(container, this.codeLines, step.line || (step.activeVal ? (step.activeVal > 50 ? 6 : 4) : 1));
    }
  }

  // =========================================================================
  // 3. MIN-HEAP STUDIO (Dual View: Tree + 1-Indexed Array & Percolate Debugger)
  // =========================================================================
  class HeapSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      // Index 0 unused; 1-indexed heap
      this.array = [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32];
      this.currentSize = 10;
      this.steps = [];
      this.currentStep = 0;
      this.timer = null;
      this.isPlaying = false;
      this.codeLines = [
        'def insert(self, x):',
        '    self.currentSize += 1',
        '    hole = self.currentSize',
        '    while hole > 1 and x < self.array[hole // 2]:',
        '        self.array[hole] = self.array[hole // 2] # ดึง Parent ลงมา',
        '        hole //= 2',
        '    self.array[hole] = x # บรรจุค่าลงใน hole',
        '',
        'def delete_min(self):',
        '    min_item = self.array[1]',
        '    self.array[1] = self.array[self.currentSize]',
        '    self.currentSize -= 1',
        '    self._percolate_down(1)',
        '    return min_item'
      ];
      this.initDefaultSteps();
    }

    initDefaultSteps() {
      this.steps = [{
        title: 'สถานะเริ่มต้น (Initial Min-Heap Preset)',
        explanation: `Min-Heap ขนาด currentSize = ${this.currentSize} (Root อยู่ที่ index 1 = ${this.array[1]}) โดยเก็บใน 1-Indexed Array`,
        arr: [...this.array],
        size: this.currentSize,
        holeIdx: -1,
        parentIdx: -1,
        childIdx: -1,
        vars: { currentSize: this.currentSize, 'array[1] (Min)': this.array[1] }
      }];
      this.currentStep = 0;
    }

    insert(val) {
      this.pause();
      const x = Number(val);
      if (isNaN(x)) return;

      this.steps = [];
      let arr = [...this.array];
      let size = this.currentSize + 1;
      let hole = size;
      arr[hole] = x;

      this.steps.push({
        title: `สเต็ป 1: เพิ่มขนาด currentSize และวาง ${x} ไว้ที่ก้นฮีป`,
        explanation: `currentSize เพิ่มเป็น ${size} กำหนดช่องว่าง hole = ${size} บรรจุค่า ${x}`,
        arr: [...arr],
        size,
        holeIdx: hole,
        parentIdx: Math.floor(hole / 2),
        vars: { insert: x, hole, parent_idx: Math.floor(hole / 2), 'array[parent]': arr[Math.floor(hole / 2)] }
      });

      // Percolate Up loop
      while (hole > 1 && x < arr[Math.floor(hole / 2)]) {
        const parentIdx = Math.floor(hole / 2);
        const parentVal = arr[parentIdx];

        this.steps.push({
          title: `สเต็ป 2: ตรวจสอบ Percolate Up (${x} < พ่อ ${parentVal})`,
          explanation: `ค่าที่ใส่ (${x}) น้อยกว่าค่าพ่อที่ index ${parentIdx} (${parentVal}) จึงต้องเลื่อนพ่อลงมาที่ตำแหน่ง hole (${hole})`,
          arr: [...arr],
          size,
          holeIdx: hole,
          parentIdx: parentIdx,
          vars: { hole, parent_idx: parentIdx, 'x < parent': true }
        });

        arr[hole] = parentVal;
        hole = parentIdx;

        this.steps.push({
          title: `เลื่อนช่องว่าง hole ขึ้นไปที่ index ${hole}`,
          explanation: `ดึงพ่อลงมาเรียบร้อย ช่องว่าง hole เลื่อนขึ้นสู่ index ${hole}`,
          arr: [...arr],
          size,
          holeIdx: hole,
          parentIdx: Math.floor(hole / 2),
          vars: { new_hole: hole, next_parent: Math.floor(hole / 2) > 0 ? arr[Math.floor(hole / 2)] : 'Root' }
        });
      }

      arr[hole] = x;
      this.array = arr;
      this.currentSize = size;

      this.steps.push({
        title: `สเต็ปสุดท้าย: บรรจุค่า ${x} ลงในตำแหน่ง hole = ${hole}`,
        explanation: `คุณสมบัติ Min-Heap ถูกต้องสมบูรณ์ (พ่อ <= ลูก เสมอ)`,
        arr: [...arr],
        size,
        holeIdx: hole,
        parentIdx: -1,
        vars: { final_hole: hole, currentSize: size, 'array[1] (Min)': arr[1] }
      });

      this.currentStep = 0;
      this.render();
    }

    deleteMin() {
      this.pause();
      if (this.currentSize === 0) {
        this.steps = [{
          title: 'ล้มเหลว: Heap ว่างเปล่า',
          explanation: 'ไม่มีข้อมูลใน Heap (currentSize = 0)',
          arr: [null],
          size: 0,
          holeIdx: -1,
          vars: { error: 'Heap is empty' }
        }];
        this.currentStep = 0;
        this.render();
        return;
      }

      this.steps = [];
      let arr = [...this.array];
      const minItem = arr[1];
      const lastItem = arr[this.currentSize];

      this.steps.push({
        title: `สเต็ป 1: ดึงค่าน้อยที่สุดออกจาก Root (Min = ${minItem})`,
        explanation: `ดึง array[1] = ${minItem} ออกมาเป็นผลลัพธ์ และนำตัวสุดท้ายของ Heap (${lastItem}) มาเตรียม Percolate Down`,
        arr: [...arr],
        size: this.currentSize,
        holeIdx: 1,
        vars: { deletedMin: minItem, lastItem, currentSize: this.currentSize }
      });

      arr[1] = lastItem;
      const newSize = this.currentSize - 1;
      let hole = 1;

      // Percolate Down loop
      while (hole * 2 <= newSize) {
        let child = hole * 2;
        if (child !== newSize && arr[child + 1] < arr[child]) {
          child++; // Right child is smaller
        }

        if (arr[child] < lastItem) {
          const smallerChildVal = arr[child];
          this.steps.push({
            title: `สเต็ป 2: ตรวจสอบ Percolate Down (ลูกที่เล็กกว่า = ${smallerChildVal})`,
            explanation: `ลูกที่เล็กกว่าที่ index ${child} (${smallerChildVal}) เล็กกว่า ${lastItem} จึงดึงลูกขึ้นมาแทนที่ hole (${hole})`,
            arr: [...arr],
            size: newSize,
            holeIdx: hole,
            childIdx: child,
            vars: { hole, smaller_child_idx: child, child_val: smallerChildVal }
          });

          arr[hole] = arr[child];
          hole = child;
        } else {
          break;
        }
      }

      arr[hole] = lastItem;
      arr[this.currentSize] = null;
      this.array = arr.slice(0, newSize + 1);
      this.currentSize = newSize;

      this.steps.push({
        title: `สเต็ปสุดท้าย: วางค่า ${lastItem} ลงที่ตำแหน่ง hole = ${hole}`,
        explanation: `Percolate Down เสร็จสิ้น ปัจจุบัน Root ใหม่คือ ${this.array[1] || 'None'}`,
        arr: [...this.array],
        size: newSize,
        holeIdx: hole,
        vars: { 'new_array[1]': this.array[1] || 'None', currentSize: newSize }
      });

      this.currentStep = 0;
      this.render();
    }

    reset() {
      this.pause();
      this.array = [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32];
      this.currentSize = 10;
      this.initDefaultSteps();
      this.render();
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      } else {
        this.pause();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    play() {
      if (this.isPlaying) {
        this.pause();
        return;
      }
      this.isPlaying = true;
      const playBtn = document.getElementById(`${this.containerId}-play`);
      if (playBtn) playBtn.innerHTML = '⏸ หยุด (Pause)';

      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1200);
    }

    pause() {
      this.isPlaying = false;
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
      const playBtn = document.getElementById(`${this.containerId}-play`);
      if (playBtn) playBtn.innerHTML = '▶ เล่น (Play)';
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];
      const arr = step.arr || this.array;
      const size = step.size !== undefined ? step.size : this.currentSize;

      // Update Step Header & Exp
      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      // Buttons
      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      // Watch Table
      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows;
      }

      // Canvas Area: Dual View (Array + Tree)
      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      // 1. Array index representation
      let arrayHtml = '<div class="studio-heap-array-wrapper"><div class="studio-heap-array">';
      for (let i = 0; i <= Math.max(size, 10); i++) {
        const val = arr[i];
        const isHole = i === step.holeIdx;
        const isParent = i === step.parentIdx;
        const isChild = i === step.childIdx;
        const isUnused = i === 0 || i > size;

        let cellClass = 'heap-cell';
        if (isUnused) cellClass += ' is-unused';
        if (isHole) cellClass += ' is-hole';
        if (isParent) cellClass += ' is-parent';
        if (isChild) cellClass += ' is-child';

        arrayHtml += `
          <div class="${cellClass}">
            <span class="heap-cell-idx">${i}</span>
            <span class="heap-cell-val">${i === 0 ? '—' : (val !== undefined && val !== null ? val : '')}</span>
            ${isHole ? '<span class="heap-badge-marker">hole</span>' : ''}
            ${isParent ? '<span class="heap-badge-marker parent">parent</span>' : ''}
            ${isChild ? '<span class="heap-badge-marker child">child</span>' : ''}
          </div>
        `;
      }
      arrayHtml += '</div></div>';

      // 2. Binary Tree representation
      const svgWidth = 600;
      const svgHeight = 210;
      let svgHtml = `<svg width="100%" height="${svgHeight}" viewBox="0 0 ${svgWidth} ${svgHeight}" class="studio-tree-svg">`;

      const coords = {};
      const positions = [
        null,
        { x: 300, y: 30 }, // 1 (Root)
        { x: 160, y: 80 }, { x: 440, y: 80 }, // 2, 3
        { x: 90, y: 135 }, { x: 230, y: 135 }, { x: 370, y: 135 }, { x: 510, y: 135 }, // 4, 5, 6, 7
        { x: 55, y: 185 }, { x: 125, y: 185 }, { x: 195, y: 185 }, { x: 265, y: 185 } // 8, 9, 10, 11
      ];

      // Edges
      for (let i = 1; i <= size; i++) {
        const left = i * 2;
        const right = i * 2 + 1;
        const p = positions[i];
        if (!p) continue;

        if (left <= size && positions[left]) {
          svgHtml += `<line x1="${p.x}" y1="${p.y}" x2="${positions[left].x}" y2="${positions[left].y}" stroke="rgba(255,255,255,0.2)" stroke-width="2.5" />`;
        }
        if (right <= size && positions[right]) {
          svgHtml += `<line x1="${p.x}" y1="${p.y}" x2="${positions[right].x}" y2="${positions[right].y}" stroke="rgba(255,255,255,0.2)" stroke-width="2.5" />`;
        }
      }

      // Nodes
      for (let i = 1; i <= size; i++) {
        const p = positions[i];
        if (!p) continue;
        const val = arr[i];
        const isHole = i === step.holeIdx;
        const isParent = i === step.parentIdx;
        const isChild = i === step.childIdx;

        let fill = '#1e293b';
        let stroke = '#10b981';
        let textColor = '#f8fafc';

        if (isHole) {
          fill = '#f59e0b';
          stroke = '#fbbf24';
          textColor = '#0f172a';
        } else if (isParent) {
          fill = '#6366f1';
          stroke = '#818cf8';
        } else if (isChild) {
          fill = '#06b6d4';
          stroke = '#38bdf8';
        }

        svgHtml += `
          <g>
            <circle cx="${p.x}" cy="${p.y}" r="17" fill="${fill}" stroke="${stroke}" stroke-width="2.5" />
            <text x="${p.x}" y="${p.y + 5}" fill="${textColor}" font-size="12" font-weight="700" text-anchor="middle">${val !== null ? val : '?'}</text>
            <text x="${p.x}" y="${p.y - 20}" fill="var(--text-muted)" font-size="10" text-anchor="middle">[${i}]</text>
          </g>
        `;
      }
      svgHtml += '</svg>';

      canvasEl.innerHTML = arrayHtml + svgHtml;
      renderCodeDebugger(container, this.codeLines, step.line || (step.holeIdx > 1 ? 5 : (step.size < 10 ? 11 : 3)));
    }
  }

  // =========================================================================
  // 4. CIRCULAR ARRAY QUEUE STUDIO
  // =========================================================================
  class QueueSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      this.capacity = 6;
      this.arr = [10, 20, 30, 40, null, null];
      this.front = 0;
      this.rear = 3;
      this.size = 4;
      this.steps = [];
      this.currentStep = 0;
      this.initDefaultSteps();
    }

    initDefaultSteps() {
      this.steps = [{
        title: 'สถานะเริ่มต้น Circular Queue',
        explanation: `ขนาดความจุ capacity = 6, front = 0, rear = 3, size = 4`,
        arr: [...this.arr],
        front: this.front,
        rear: this.rear,
        size: this.size,
        vars: { front: this.front, rear: this.rear, size: this.size, capacity: this.capacity }
      }];
      this.currentStep = 0;
    }

    enqueue(val) {
      const x = Number(val) || val;
      if (this.size >= this.capacity) {
        this.steps = [{
          title: '⚠️ Queue เต็มแล้ว (Queue Full)',
          explanation: `ไม่สามารถ Enqueue ได้เนื่องจาก size (${this.size}) == capacity (${this.capacity})`,
          arr: [...this.arr],
          front: this.front,
          rear: this.rear,
          size: this.size,
          vars: { error: 'Overflow' }
        }];
        this.currentStep = 0;
        this.render();
        return;
      }

      this.steps = [];
      const newRear = (this.rear + 1) % this.capacity;

      this.steps.push({
        title: `สเต็ป 1: คำนวณ rear ใหม่ด้วย Modulo`,
        explanation: `คำนวณ rear = (rear + 1) % capacity = (${this.rear} + 1) % ${this.capacity} = ${newRear}`,
        arr: [...this.arr],
        front: this.front,
        rear: newRear,
        size: this.size,
        vars: { old_rear: this.rear, 'new_rear = (rear + 1) % 6': newRear }
      });

      this.arr[newRear] = x;
      this.rear = newRear;
      this.size++;

      this.steps.push({
        title: `สเต็ป 2: นำค่า ${x} บรรจุที่ตำแหน่ง rear = ${newRear}`,
        explanation: `เพิ่มขนาด size เป็น ${this.size} สำเร็จ`,
        arr: [...this.arr],
        front: this.front,
        rear: this.rear,
        size: this.size,
        vars: { front: this.front, rear: this.rear, size: this.size, item: x }
      });

      this.currentStep = 0;
      this.render();
    }

    dequeue() {
      if (this.size === 0) {
        this.steps = [{
          title: '⚠️ Queue ว่างเปล่า (Queue Empty)',
          explanation: `ไม่สามารถ Dequeue ได้เนื่องจากไม่มีข้อมูลใน Queue`,
          arr: [...this.arr],
          front: this.front,
          rear: this.rear,
          size: 0,
          vars: { error: 'Underflow' }
        }];
        this.currentStep = 0;
        this.render();
        return;
      }

      this.steps = [];
      const removed = this.arr[this.front];

      this.steps.push({
        title: `สเต็ป 1: ดึงข้อมูลที่หน้าคิว (front = ${this.front})`,
        explanation: `นำข้อมูลค่า ${removed} ออกจากช่อง front (${this.front})`,
        arr: [...this.arr],
        front: this.front,
        rear: this.rear,
        size: this.size,
        vars: { dequeued: removed, front: this.front }
      });

      this.arr[this.front] = null;
      const newFront = (this.front + 1) % this.capacity;
      this.front = newFront;
      this.size--;

      this.steps.push({
        title: `สเต็ป 2: ขยับ front ด้วย Modulo (front = (front + 1) % capacity)`,
        explanation: `เลื่อน front = (${(this.front - 1 + this.capacity) % this.capacity} + 1) % ${this.capacity} = ${newFront}`,
        arr: [...this.arr],
        front: this.front,
        rear: this.rear,
        size: this.size,
        vars: { dequeued: removed, new_front: this.front, size: this.size }
      });

      this.currentStep = 0;
      this.render();
    }

    reset() {
      this.arr = [10, 20, 30, 40, null, null];
      this.front = 0;
      this.rear = 3;
      this.size = 4;
      this.initDefaultSteps();
      this.render();
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];
      const arr = step.arr || this.arr;

      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      let slotsHtml = '<div class="studio-queue-slots">';
      for (let i = 0; i < this.capacity; i++) {
        const val = arr[i];
        const isFront = i === step.front && step.size > 0;
        const isRear = i === step.rear && step.size > 0;

        let badges = [];
        if (isFront) badges.push('<span class="q-badge front">FRONT</span>');
        if (isRear) badges.push('<span class="q-badge rear">REAR</span>');

        slotsHtml += `
          <div class="studio-queue-slot ${val !== null ? 'has-item' : 'is-empty'}">
            <div class="q-slot-badges">${badges.join(' ')}</div>
            <div class="q-slot-box">
              <span class="q-slot-val">${val !== null ? val : '—'}</span>
            </div>
            <span class="q-slot-idx">index: ${i}</span>
          </div>
        `;
      }
      slotsHtml += '</div>';

      canvasEl.innerHTML = slotsHtml;
      renderCodeDebugger(container, this.codeLines, step.line);
    }
  }


  // =========================================================================
  // 5. STACK & INFIX-TO-POSTFIX STUDIO
  // =========================================================================
  class StackInfixSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      this.expr = '(A + B) * (C - D)';
      this.steps = [];
      this.currentStep = 0;
      this.initInfixSteps(this.expr);
    }

    precedence(op) {
      if (op === '^') return 3;
      if (op === '*' || op === '/') return 2;
      if (op === '+' || op === '-') return 1;
      return 0;
    }

    initInfixSteps(expr) {
      this.expr = expr || '(A + B) * (C - D)';
      const cleanExpr = this.expr.replace(/\s+/g, '');
      const steps = [];
      const opStack = [];
      const output = [];

      steps.push({
        title: 'เริ่มต้นการแปลง Infix -> Postfix',
        explanation: `นิพจน์ตั้งต้น: "${this.expr}" | กฎ: Operand ส่งออกทันที, "(" เข้า Stack, Operator เทียบ Precedence`,
        token: 'START',
        action: 'เริ่มต้นการอ่าน',
        stack: [],
        output: [],
        vars: { expr: this.expr, stack: '[]', output: '""' }
      });

      for (let i = 0; i < cleanExpr.length; i++) {
        const ch = cleanExpr[i];

        if (/[A-Za-z0-9]/.test(ch)) {
          output.push(ch);
          steps.push({
            title: `อ่าน Operand: "${ch}"`,
            explanation: `ตัวถูกดำเนินการ "${ch}" ส่งออกไปยัง Postfix ทันทีโดยไม่ต้องผ่าน Stack`,
            token: ch,
            action: `Output "${ch}"`,
            stack: [...opStack],
            output: [...output],
            vars: { token: ch, action: 'Output directly', output: output.join(' ') }
          });
        } else if (ch === '(') {
          opStack.push(ch);
          steps.push({
            title: `อ่านวงเล็บเปิด: "("`,
            explanation: `พบวงเล็บเปิด "(" -> Push ลง Stack ทันทีเพื่อเริ่มขอบเขตวงเล็บใหม่`,
            token: ch,
            action: `Push "(" to Stack`,
            stack: [...opStack],
            output: [...output],
            vars: { token: ch, stack_top: '(', stack_size: opStack.length }
          });
        } else if (ch === ')') {
          steps.push({
            title: `อ่านวงเล็บปิด: ")"`,
            explanation: `พบวงเล็บปิด ")" -> Pop ตัวดำเนินการใน Stack ออกไปที่ Output จนกว่าจะเจอ "("`,
            token: ch,
            action: `Pop until "("`,
            stack: [...opStack],
            output: [...output],
            vars: { token: ch, action: 'Pop operators until (' }
          });

          while (opStack.length > 0 && opStack[opStack.length - 1] !== '(') {
            const popped = opStack.pop();
            output.push(popped);
            steps.push({
              title: `Pop ตัวดำเนินการ "${popped}" ในวงเล็บ`,
              explanation: `ดึง "${popped}" ออกจาก Stack ส่งไปต่อท้าย Output`,
              token: ch,
              action: `Pop "${popped}" -> Output`,
              stack: [...opStack],
              output: [...output],
              vars: { popped, output: output.join(' ') }
            });
          }

          if (opStack.length > 0 && opStack[opStack.length - 1] === '(') {
            opStack.pop(); // Discard '('
            steps.push({
              title: `ทิ้งวงเล็บเปิด "(" ออกจาก Stack`,
              explanation: `ดึง "(" ออกจาก Stack ปิดขอบเขตวงเล็บสมบูรณ์`,
              token: ch,
              action: `Discard "("`,
              stack: [...opStack],
              output: [...output],
              vars: { 'discarded': '(', stack_size: opStack.length }
            });
          }
        } else if ('+-*/^'.includes(ch)) {
          // While loop pop operators with >= precedence
          while (
            opStack.length > 0 &&
            opStack[opStack.length - 1] !== '(' &&
            this.precedence(opStack[opStack.length - 1]) >= this.precedence(ch)
          ) {
            const topOp = opStack[opStack.length - 1];
            const popped = opStack.pop();
            output.push(popped);
            steps.push({
              title: `Pop ตัวดำเนินการ "${popped}" (Precedence >= "${ch}")`,
              explanation: `ตัวบนสุดของ Stack (${topOp}) สำคัญ >= "${ch}" -> ต้อง Pop ออกไปก่อน!`,
              token: ch,
              action: `Pop "${popped}"`,
              stack: [...opStack],
              output: [...output],
              vars: { 'stack_top_precedence >= new': true, popped, output: output.join(' ') }
            });
          }

          opStack.push(ch);
          steps.push({
            title: `Push "${ch}" ลง Stack`,
            explanation: `Push ตัวดำเนินการ "${ch}" (Precedence = ${this.precedence(ch)}) ลงยอด Stack`,
            token: ch,
            action: `Push "${ch}" to Stack`,
            stack: [...opStack],
            output: [...output],
            vars: { pushed: ch, stack_top: ch, stack_size: opStack.length }
          });
        }
      }

      // Drain remaining
      while (opStack.length > 0) {
        const popped = opStack.pop();
        output.push(popped);
        steps.push({
          title: `Pop ตัวดำเนินการที่ค้างใน Stack: "${popped}"`,
          explanation: `อ่านนิพจน์จนหมดแล้ว ดึงตัวดำเนินการที่เหลือทั้งหมดใน Stack ออกสู่ Output`,
          token: 'EOF',
          action: `Pop remaining "${popped}"`,
          stack: [...opStack],
          output: [...output],
          vars: { popped, output: output.join(' ') }
        });
      }

      steps.push({
        title: `🎉 แปลงสำเร็จ! ผลลัพธ์ Postfix: ${output.join('')}`,
        explanation: `ผลลัพธ์นิพจน์ Postfix คือ: "${output.join(' ')}"`,
        token: 'DONE',
        action: 'สิ้นสุดการทำงาน',
        stack: [],
        output: [...output],
        vars: { final_postfix: output.join(''), length: output.length }
      });

      this.steps = steps;
      this.currentStep = 0;
      this.render();
    }

    convert(newExpr) {
      if (newExpr) this.expr = newExpr;
      this.initInfixSteps(this.expr);
    }

    reset() {
      this.convert('(A + B) * (C - D)');
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];

      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      let stackItemsHtml = '';
      if (step.stack && step.stack.length > 0) {
        for (let i = step.stack.length - 1; i >= 0; i--) {
          const isTop = i === step.stack.length - 1;
          stackItemsHtml += `
            <div class="studio-stack-item ${isTop ? 'is-top' : ''}">
              <span class="stk-val">${step.stack[i]}</span>
              ${isTop ? '<span class="stk-top-badge">TOP</span>' : ''}
            </div>
          `;
        }
      } else {
        stackItemsHtml = '<div class="studio-stack-empty">Stack ว่าง (Empty)</div>';
      }

      canvasEl.innerHTML = `
        <div class="studio-infix-view">
          <div class="infix-stack-column">
            <div class="infix-col-title">🥞 Operator Stack:</div>
            <div class="studio-stack-bucket">
              ${stackItemsHtml}
            </div>
          </div>
          <div class="infix-output-column">
            <div class="infix-col-title">📤 Postfix Output Stream:</div>
            <div class="studio-postfix-tape">
              ${(step.output || []).map(token => `<span class="tape-token">${token}</span>`).join('') || '<span class="tape-empty">(ยังไม่มี Output)</span>'}
            </div>
            <div class="infix-status-card">
              <div><b>Token ปัจจุบัน:</b> <span style="color:#f59e0b;font-weight:700;">${step.token}</span></div>
              <div><b>Action:</b> <span style="color:#38bdf8;">${step.action}</span></div>
            </div>
          </div>
        </div>
      `;
      renderCodeDebugger(container, this.codeLines, step.line || (step.token === '(' ? 5 : (step.token === ')' ? 7 : (step.action && step.action.includes('Output') ? 3 : 10))));
    }
  }

  // =========================================================================
  // 6. HASH TABLE STUDIO (Linear, Quadratic, Double Hashing)
  // =========================================================================
  class HashSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      this.tableSize = 11;
      this.strategy = 'double'; // 'linear', 'quadratic', 'double'
      this.keys = [25, 42, 96, 18, 77, 32];
      this.table = new Array(this.tableSize).fill(null);
      this.steps = [];
      this.currentStep = 0;
      this.codeLines = [
        'def insert_open_addressing(table, key, size):',
        '    h1 = key % size',
        '    step = 7 - (key % 7) if strategy == "double" else 1',
        '    for probe in range(size):',
        '        slot = (h1 + probe * step) % size',
        '        if table[slot] is None:',
        '            table[slot] = key',
        '            return True  # แทรกสำเร็จที่ช่อง slot',
        '        # Collision: ช่องถูกครอบครอง ตรวจสอบช่องถัดไป',
        '    return False  # ตารางเต็ม'
      ];
      this.runSimulation();
    }

    h1(k) { return k % this.tableSize; }
    h2(k) { return 7 - (k % 7); }

    runSimulation() {
      this.table = new Array(this.tableSize).fill(null);
      const steps = [];
      let collisionCount = 0;

      steps.push({
        title: 'เริ่มต้นตารางแฮช (Initial Hash Table)',
        explanation: `ขนาดตาราง M = ${this.tableSize} (ช่อง 0 ถึง ${this.tableSize - 1}) กลยุทธ์: ${this.strategy.toUpperCase()}`,
        table: [...this.table],
        activeSlot: -1,
        probeSequence: [],
        vars: { table_size: this.tableSize, strategy: this.strategy, collisions: 0 }, line: 1
      });

      for (let k of this.keys) {
        const initialHash = this.h1(k);
        const h2Val = this.h2(k);
        let probe = 0;
        let inserted = false;
        const probes = [];

        steps.push({
          title: `เริ่มแทรกคีย์ k = ${k}`,
          explanation: `คำนวณ h1(${k}) = ${k} % ${this.tableSize} = ${initialHash} ${this.strategy === 'double' ? `| h2(${k}) = 7 - (${k} % 7) = ${h2Val}` : ''}`,
          table: [...this.table],
          activeSlot: initialHash,
          probeSequence: [initialHash],
          vars: { key: k, h1: initialHash, h2: h2Val }, line: 2
        });

        while (probe < this.tableSize) {
          let slot;
          if (this.strategy === 'linear') slot = (initialHash + probe) % this.tableSize;
          else if (this.strategy === 'quadratic') slot = (initialHash + probe * probe) % this.tableSize;
          else slot = (initialHash + probe * h2Val) % this.tableSize;

          probes.push(slot);

          if (this.table[slot] === null) {
            this.table[slot] = { key: k, originalHash: initialHash, probes: probe };
            steps.push({
              title: `บรรจุคีย์ ${k} ที่ช่อง index ${slot} (Probe #${probe})`,
              explanation: `ช่อง ${slot} ว่างเปล่า! บรรจุคีย์ ${k} สำเร็จ (เกิดการชน ${probe} ครั้ง)`,
              table: [...this.table],
              activeSlot: slot,
              probeSequence: [...probes],
              vars: { key: k, slot, probe_count: probe, total_collisions: collisionCount }, line: 7
            });
            inserted = true;
            break;
          } else {
            collisionCount++;
            steps.push({
              title: `⚠️ เกิดการชนที่ช่อง index ${slot} (ชนกับคีย์ ${this.table[slot].key})`,
              explanation: `ช่อง ${slot} มีคีย์ ${this.table[slot].key} อยู่แล้ว! ทำการค้นหาช่องถัดไปด้วย ${this.strategy}`,
              table: [...this.table],
              activeSlot: slot,
              probeSequence: [...probes],
              vars: { key: k, collided_at: slot, occupied_by: this.table[slot].key, probe_step: probe + 1 }, line: 9
            });
            probe++;
          }
        }
      }

      steps.push({
        title: `🎉 แทรกครบทุกคีย์ (${this.keys.length} คีย์)`,
        explanation: `การแทรกเสร็จสิ้น ตารางมี ${this.keys.length} ข้อมูล (Load Factor = ${(this.keys.length / this.tableSize).toFixed(2)}) การชนสะสม = ${collisionCount} ครั้ง`,
        table: [...this.table],
        activeSlot: -1,
        probeSequence: [],
        vars: { total_keys: this.keys.length, load_factor: (this.keys.length / this.tableSize).toFixed(2), total_collisions: collisionCount }
      });

      this.steps = steps;
      this.currentStep = 0;
      this.render();
    }

    setStrategy(strat) {
      this.strategy = strat;
      this.runSimulation();
    }

    insertCustomKey(keyVal) {
      const k = Number(keyVal);
      if (!isNaN(k) && !this.keys.includes(k)) {
        this.keys.push(k);
        this.runSimulation();
      }
    }

    reset() {
      this.keys = [25, 42, 96, 18, 77, 32];
      this.strategy = 'double';
      this.runSimulation();
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];
      const table = step.table || this.table;

      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      let slotsHtml = '<div class="studio-hash-table-grid">';
      for (let i = 0; i < this.tableSize; i++) {
        const item = table[i];
        const isActive = i === step.activeSlot;
        const isProbed = (step.probeSequence || []).includes(i);

        let cardClass = 'studio-hash-slot';
        if (isActive) cardClass += ' is-active';
        else if (isProbed) cardClass += ' is-probed';
        if (item) cardClass += ' is-filled';

        slotsHtml += `
          <div class="${cardClass}">
            <div class="slot-idx-header">[ ${i} ]</div>
            <div class="slot-val-body">${item ? item.key : '<span class="empty-slot-dot">EMPTY</span>'}</div>
            ${item ? `<div class="slot-meta">h=${item.originalHash} | p=${item.probes}</div>` : ''}
          </div>
        `;
      }
      slotsHtml += '</div>';

      canvasEl.innerHTML = slotsHtml;
      renderCodeDebugger(container, this.codeLines, step.line);
    }
  }

  // =========================================================================
  // 7. SORTING ALGORITHMS STUDIO
  // =========================================================================
  class SortSimulator {
    constructor(containerId) {
      this.containerId = containerId;
      this.algorithm = 'bubble'; // 'bubble', 'selection', 'insertion'
      this.arr = [64, 34, 25, 12, 22, 11, 90];
      this.steps = [];
      this.currentStep = 0;
      this.codeLines = [
        'def bubble_sort(arr):',
        '    n = len(arr)',
        '    for i in range(n):',
        '        swapped = False',
        '        for j in range(0, n - i - 1):',
        '            if arr[j] > arr[j + 1]:',
        '                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap',
        '                swapped = True',
        '        if not swapped: break'
      ];
      this.runSimulation();
    }

    runSimulation() {
      const a = [...this.arr];
      const steps = [];
      let comparisons = 0;
      let swaps = 0;

      steps.push({
        title: `เริ่มต้น ${this.algorithm.toUpperCase()} SORT`,
        explanation: `อาร์เรย์เริ่มต้น [ ${a.join(', ')} ] ความยาว N = ${a.length}`,
        arr: [...a],
        compA: -1,
        compB: -1,
        sortedIdx: -1,
        vars: { comparisons: 0, swaps: 0, algorithm: this.algorithm }
      });

      if (this.algorithm === 'bubble') {
        const n = a.length;
        for (let i = 0; i < n - 1; i++) {
          for (let j = 0; j < n - i - 1; j++) {
            comparisons++;
            const doSwap = a[j] > a[j + 1];

            steps.push({
              title: `เปรียบเทียบ A[${j}] (${a[j]}) กับ A[${j + 1}] (${a[j + 1]})`,
              explanation: doSwap ? `${a[j]} > ${a[j + 1]} -> สลับตำแหน่ง (Swap)!` : `${a[j]} <= ${a[j + 1]} -> เรียงถูกต้องแล้ว ข้ามไป`,
              arr: [...a],
              compA: j,
              compB: j + 1,
              sortedIdx: n - i,
              vars: { comparisons, swaps, 'A[j] > A[j+1]': doSwap }
            });

            if (doSwap) {
              const tmp = a[j];
              a[j] = a[j + 1];
              a[j + 1] = tmp;
              swaps++;

              steps.push({
                title: `สลับตำแหน่งสำเร็จ: [${a[j]}, ${a[j + 1]}]`,
                explanation: `อาร์เรย์หลังการสลับ: [ ${a.join(', ')} ]`,
                arr: [...a],
                compA: j,
                compB: j + 1,
                sortedIdx: n - i,
                vars: { comparisons, swaps }
              });
            }
          }
        }
      } else if (this.algorithm === 'selection') {
        const n = a.length;
        for (let i = 0; i < n - 1; i++) {
          let minIdx = i;
          for (let j = i + 1; j < n; j++) {
            comparisons++;
            if (a[j] < a[minIdx]) minIdx = j;
            steps.push({
              title: `หาค่าน้อยสุดใน Pass ${i + 1}: เทียบ A[${j}] (${a[j]})`,
              explanation: `ค่าน้อยที่สุดปัจจุบันคือ index ${minIdx} (ค่า ${a[minIdx]})`,
              arr: [...a],
              compA: minIdx,
              compB: j,
              sortedIdx: i,
              vars: { pass: i + 1, current_min: a[minIdx], comparisons }
            });
          }
          if (minIdx !== i) {
            const tmp = a[i];
            a[i] = a[minIdx];
            a[minIdx] = tmp;
            swaps++;
          }
        }
      }

      steps.push({
        title: '🎉 เรียงลำดับเสร็จสิ้น!',
        explanation: `ผลลัพธ์ที่เรียงแล้ว: [ ${a.join(', ')} ] | เปรียบเทียบทั้งหมด: ${comparisons} ครั้ง, สลับ: ${swaps} ครั้ง`,
        arr: [...a],
        compA: -1,
        compB: -1,
        sortedIdx: a.length,
        vars: { sorted: true, total_comparisons: comparisons, total_swaps: swaps }
      });

      this.steps = steps;
      this.currentStep = 0;
      this.render();
    }

    setAlgo(algo) {
      this.algorithm = algo;
      this.runSimulation();
    }

    reset() {
      this.arr = [64, 34, 25, 12, 22, 11, 90];
      this.runSimulation();
    }

    stepNext() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
        this.render();
      }
    }

    stepPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.render();
      }
    }

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const step = this.steps[this.currentStep] || this.steps[0];
      const arr = step.arr || this.arr;

      const counterEl = container.querySelector('.studio-step-counter');
      if (counterEl) counterEl.textContent = `สเต็ป ${this.currentStep + 1} / ${this.steps.length}`;

      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;

      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(`${this.containerId}-prev`);
      const nextBtn = document.getElementById(`${this.containerId}-next`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += `<tr><td class="watch-k">${k}</td><td class="watch-v">${v}</td></tr>`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (!canvasEl) return;

      const maxVal = Math.max(...arr, 1);
      let barsHtml = '<div class="studio-sort-bars">';
      arr.forEach((val, idx) => {
        const heightPct = Math.round((val / maxVal) * 100);
        const isA = idx === step.compA;
        const isB = idx === step.compB;
        const isSorted = idx >= step.sortedIdx && step.sortedIdx !== -1;

        let barClass = 'sort-bar';
        if (isA) barClass += ' is-compa';
        if (isB) barClass += ' is-compb';
        if (isSorted) barClass += ' is-sorted';

        barsHtml += `
          <div class="sort-bar-col">
            <div class="${barClass}" style="height: ${Math.max(20, heightPct)}%;">
              <span class="bar-val">${val}</span>
            </div>
            <span class="bar-idx">[${idx}]</span>
          </div>
        `;
      });
      barsHtml += '</div>';

      canvasEl.innerHTML = barsHtml;
      renderCodeDebugger(container, this.codeLines, step.line || (step.compA >= 0 ? 6 : 4));
    }
  }

  // =========================================================================
  // HTML BUILDER FOR EMBEDDED WIKI STUDIO WIDGETS
  // =========================================================================
  function createStudioWidgetHtml(type, widgetId) {
    let title = '';
    let badge = '';
    let controlsHtml = '';

    if (type === 'linked-list') {
      title = '🔬 Interactive Linked List Studio (ห้องทดลองและตัวตรวจสอบพอยน์เตอร์)';
      badge = 'Chapter 3: Linked Lists';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>ค่าโหนด (Value):</label>
            <input type="text" id="${widgetId}-val" value="25" placeholder="ใส่ตัวเลขหรือข้อความ" style="width: 130px;" />
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'insertHead')">➕ แทรก Head</button>
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'insertTail')">➕ แทรก Tail</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'deleteVal')">🗑️ ลบค่านี้</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'bst') {
      title = '🌲 Interactive BST Studio (ห้องทดลองและตัวตรวจสอบต้นไม้ค้นหาทวิภาค)';
      badge = 'Chapter 5: Trees & BST';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>ตัวเลข (Number):</label>
            <input type="number" id="${widgetId}-val" value="45" style="width: 100px;" />
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'insert')">➕ แทรก (Insert)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'search')">🔍 ค้นหา (Search)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'delete')">🗑️ ลบ (Delete 3 Cases)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 โครงสร้างเดิม</button>
          </div>
        </div>
      `;
    } else if (type === 'heap') {
      title = '⚡ Interactive Min-Heap Studio (ตัวจำลองฮีปและดีบักเกอร์ Percolate Up/Down)';
      badge = 'Chapter 7: Binary Heap';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>ตัวเลข (Number):</label>
            <input type="number" id="${widgetId}-val" value="14" style="width: 100px;" />
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'insert')">➕ แทรก (Percolate Up)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'deleteMin')">🗑️ ดึงค่าต่ำสุด Delete Min</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต Preset</button>
          </div>
        </div>
      `;
    } else if (type === 'queue') {
      title = '🚶‍♂️ Interactive Circular Queue Studio (จำลองคิววงกลม Modulo Index)';
      badge = 'Chapter 4: Circular Queues';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>ข้อมูล (Item):</label>
            <input type="text" id="${widgetId}-val" value="50" style="width: 100px;" />
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'enqueue')">📥 Enqueue (เข้าคิว)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'dequeue')">📤 Dequeue (ออกจากคิว)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'stack-infix') {
      title = '🥞 Interactive Stack & Infix-to-Postfix Studio (ตัวแปลงนิพจน์ทีละสเต็ป)';
      badge = 'Chapter 4.1: Stacks';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>นิพจน์ Infix:</label>
            <input type="text" id="${widgetId}-val" value="(A + B) * (C - D)" style="width: 220px;" />
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'convertInfix')">⚡ แปลงนิพจน์ (Convert)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'loadExpr1')">Ex 1: A+B*C</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'loadExpr2')">Ex 2: A+B*C-D/E</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'hash') {
      title = '🔑 Interactive Hash Table Studio (จำลองการชน Linear, Quadratic, Double Hashing)';
      badge = 'Chapter 6: Hash Tables';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>กลยุทธ์แก้การชน:</label>
            <select id="${widgetId}-strat" onchange="window.DsaWikiStudio.act('${widgetId}', 'setStrategy')" style="background:#0f172a;color:#fff;padding:6px;border-radius:4px;border:1px solid #6366f1;">
              <option value="double" selected>Double Hashing (h2 = 7 - k%7)</option>
              <option value="linear">Linear Probing ((h + i) % M)</option>
              <option value="quadratic">Quadratic Probing ((h + i²) % M)</option>
            </select>
          </div>
          <div class="studio-input-group">
            <label>เพิ่มคีย์:</label>
            <input type="number" id="${widgetId}-val" value="53" style="width:80px;" />
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'insertHash')">➕ แทรกคีย์</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 คีย์ข้อสอบเดิม</button>
          </div>
        </div>
      `;
    } else if (type === 'sort') {
      title = '🔀 Interactive Sorting Studio (เปรียบเทียบขั้นตอนวิธีเรียงลำดับ)';
      badge = 'Chapter 8: Sorting';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-input-group">
            <label>อัลกอริทึม:</label>
            <select id="${widgetId}-algo" onchange="window.DsaWikiStudio.act('${widgetId}', 'setAlgo')" style="background:#0f172a;color:#fff;padding:6px;border-radius:4px;border:1px solid #6366f1;">
              <option value="bubble" selected>Bubble Sort O(N²)</option>
              <option value="selection">Selection Sort O(N²)</option>
            </select>
          </div>
          <div class="studio-btn-group">
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ตอาร์เรย์</button>
          </div>
        </div>
      `;
    }

    return `
      <div class="wiki-studio-card" id="${widgetId}">
        <div class="wiki-studio-header">
          <div class="studio-title-group">
            <span class="studio-badge">${badge}</span>
            <h3 class="studio-title">${title}</h3>
          </div>
          <div class="studio-step-counter">สเต็ป 1 / 1</div>
        </div>

        ${controlsHtml}

        <!-- Interactive Canvas Viewport -->
        <div class="studio-main-viewport">
          <div class="studio-canvas-area"></div>
        </div>

        <!-- Dual Code & Variable Debugger Deck -->
        <div class="studio-debugger-deck">
          <!-- Left Panel: Stepper, Status & Live Variables -->
          <div class="debugger-status-panel">
            <div class="studio-step-header">
              <div class="studio-step-title">คำอธิบายขั้นตอน</div>
              <div class="active-code-line-badge">▶ Line <span class="active-code-line-num">-</span></div>
            </div>
            <div class="studio-step-exp">พร้อมจำลองการทำงาน...</div>
            
            <div class="studio-stepper-controls">
              <button id="${widgetId}-prev" class="studio-stepper-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'prev')" title="ย้อนกลับ">⏮️ ย้อนสเต็ป</button>
              <button id="${widgetId}-play" class="studio-stepper-btn play" onclick="window.DsaWikiStudio.act('${widgetId}', 'play')" title="เล่นอัตโนมัติ">▶ เล่น (Play)</button>
              <button id="${widgetId}-next" class="studio-stepper-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'next')" title="สเต็ปถัดไป">⏭️ สเต็ปถัดไป</button>
            </div>

            <!-- Live Variables Inspector -->
            <div class="studio-inspector-footer">
              <div class="inspector-header">🔍 ตัวแปรขณะรัน (Live Variables Watch):</div>
              <table class="studio-watch-table">
                <thead>
                  <tr><th>ตัวแปร (Variable)</th><th>ค่าในหน่วยความจำ (Value)</th></tr>
                </thead>
                <tbody class="studio-watch-tbody">
                  <tr><td colspan="2" style="text-align:center;color:var(--text-muted);">ไม่มีตัวแปร</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Right Panel: Python Code Walkthrough with Active Line Highlighting -->
          <div class="debugger-code-panel">
            <div class="code-panel-header">
              <div class="code-title">
                <span>🐍</span>
                <span>Python Algorithm Code Debugger</span>
              </div>
              <span class="code-panel-badge">Step Debug</span>
            </div>
            <div class="code-trace-viewport">
              <div class="code-trace-lines"></div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  // Mount logic called by app.js when an article is loaded
  function mountWidgetsForDoc(docId, articleBody) {
    if (!articleBody) return;

    if (docId.startsWith('03.1')) {
      const widgetId = 'studio-widget-linked-list';
      mountWidgetAt(articleBody, 'linked-list', widgetId, '## ✂️ 3. ขั้นตอนการจัดการ Pointer');
      widgetInstances[widgetId] = new LinkedListSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('04.1')) {
      const widgetId = 'studio-widget-stack';
      mountWidgetAt(articleBody, 'stack-infix', widgetId, '## 🥞 1. Stack ADT');
      widgetInstances[widgetId] = new StackInfixSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('04.2')) {
      const widgetId = 'studio-widget-queue';
      mountWidgetAt(articleBody, 'queue', widgetId, '## 🏛️ 1. Queue ADT');
      widgetInstances[widgetId] = new QueueSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('05.1') || docId.startsWith('05.2') || docId.startsWith('05.3')) {
      const widgetId = 'studio-widget-bst';
      mountWidgetAt(articleBody, 'bst', widgetId, '## 🌲 2. อัลกอริทึม');
      widgetInstances[widgetId] = new BstSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('06.1')) {
      const widgetId = 'studio-widget-hash';
      mountWidgetAt(articleBody, 'hash', widgetId, '## 🏛️ 1. โครงสร้าง');
      widgetInstances[widgetId] = new HashSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('07.1')) {
      const widgetId = 'studio-widget-heap';
      mountWidgetAt(articleBody, 'heap', widgetId, '## 🏛️ 1. กายวิภาค');
      widgetInstances[widgetId] = new HeapSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('08.1')) {
      const widgetId = 'studio-widget-sort';
      mountWidgetAt(articleBody, 'sort', widgetId, '## 🏛️ 1. สรุปความเร็ว');
      widgetInstances[widgetId] = new SortSimulator(widgetId);
      widgetInstances[widgetId].render();
    }
  }

  function mountWidgetAt(articleBody, type, widgetId, headingSearch) {
    if (document.getElementById(widgetId)) return;

    const widgetHtml = createStudioWidgetHtml(type, widgetId);
    const headings = articleBody.querySelectorAll('h2');
    let targetHeading = null;

    headings.forEach(h => {
      if (!targetHeading && h.textContent.includes(headingSearch.replace(/^[#\s]+/, '').slice(0, 6))) {
        targetHeading = h;
      }
    });

    if (targetHeading && targetHeading.nextSibling) {
      const div = document.createElement('div');
      div.innerHTML = widgetHtml;
      targetHeading.parentNode.insertBefore(div.firstElementChild, targetHeading.nextSibling);
    } else {
      const div = document.createElement('div');
      div.innerHTML = widgetHtml;
      articleBody.insertBefore(div.firstElementChild, articleBody.firstChild);
    }
  }

  // Unified dispatcher for UI buttons
  function act(widgetId, action) {
    const inst = widgetInstances[widgetId];
    if (!inst) return;

    const valInput = document.getElementById(`${widgetId}-val`);
    const val = valInput ? valInput.value.trim() : '';

    if (action === 'insertHead' && inst.insertHead) inst.insertHead(val);
    else if (action === 'insertTail' && inst.insertTail) inst.insertTail(val);
    else if (action === 'deleteVal' && inst.deleteVal) inst.deleteVal(val);
    else if (action === 'insert' && inst.insert) inst.insert(val);
    else if (action === 'search' && inst.search) inst.search(val);
    else if (action === 'delete' && inst.deleteNode) inst.deleteNode(val);
    else if (action === 'deleteMin' && inst.deleteMin) inst.deleteMin();
    else if (action === 'enqueue' && inst.enqueue) inst.enqueue(val);
    else if (action === 'dequeue' && inst.dequeue) inst.dequeue();
    else if (action === 'convertInfix' && inst.convert) inst.convert(val);
    else if (action === 'loadExpr1' && inst.convert) { if (valInput) valInput.value = 'A + B * C'; inst.convert('A + B * C'); }
    else if (action === 'loadExpr2' && inst.convert) { if (valInput) valInput.value = 'A + B * C - D / E'; inst.convert('A + B * C - D / E'); }
    else if (action === 'insertHash' && inst.insertCustomKey) inst.insertCustomKey(val);
    else if (action === 'setStrategy' && inst.setStrategy) {
      const stratSel = document.getElementById(`${widgetId}-strat`);
      if (stratSel) inst.setStrategy(stratSel.value);
    }
    else if (action === 'setAlgo' && inst.setAlgo) {
      const algoSel = document.getElementById(`${widgetId}-algo`);
      if (algoSel) inst.setAlgo(algoSel.value);
    }
    else if (action === 'reset' && inst.reset) inst.reset();
    else if (action === 'next' && inst.stepNext) inst.stepNext();
    else if (action === 'prev' && inst.stepPrev) inst.stepPrev();
    else if (action === 'play' && inst.play) inst.play();
  }

  return {
    mountWidgetsForDoc,
    act
  };
})();
