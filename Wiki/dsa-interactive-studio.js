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

  function renderQaPanel(container, qa) {
    if (!container || !qa) return;
    const qEl = container.querySelector('.qa-question-text');
    const aEl = container.querySelector('.qa-answer-text');
    const dEl = container.querySelector('.qa-danger-text');
    if (qEl) qEl.innerHTML = qa.question || '-';
    if (aEl) aEl.innerHTML = qa.answer || '-';
    if (dEl) dEl.innerHTML = qa.danger || '-';
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

      if (activeElem && linesContainer) {
        const topDiff = activeElem.offsetTop - linesContainer.offsetTop;
        linesContainer.scrollTop = topDiff - (linesContainer.clientHeight / 2);
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
      renderQaPanel(container, this.qa);
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
      this.tableSize = 10;
      this.strategy = 'linear'; // 'linear', 'quadratic', 'double'
      this.keys = [89, 18, 49, 58, 69];
      this.table = new Array(this.tableSize).fill(null);
      this.steps = [];
      this.currentStep = 0;
      this.qa = {
        question: 'โจทย์ข้อสอบปลายภาค ข้อที่ 1: แทรกข้อมูล [89, 18, 49, 58, 69] ลงใน Hash Table ขนาด 10 ด้วย Linear Probing จงหาตำแหน่งของแต่ละคีย์และผลรวมการชนทั้งหมด',
        answer: '<strong>ตำแหน่งในตาราง:</strong> ช่อง 0: 49, ช่อง 1: 58, ช่อง 2: 69, ช่อง 8: 18, ช่อง 9: 89<br><strong>การชนแต่ละตัว:</strong> 49(ชน 1 ครั้ง), 58(ชน 3 ครั้ง), 69(ชน 3 ครั้ง)<br><strong>ผลรวมการชนทั้งหมด:</strong> <code>7 ครั้ง</code>',
        danger: '<strong>จุดตัด 0 คะแนน:</strong> 1. ห้ามตอบ 14 ครั้งเด็ดขาด (ตอบ 14 = 0 ทันที) 2. คีย์ 58 ลงช่อง 1 ห้ามตอบช่อง 6! 3. คีย์ 49 ทำ Wrap Around วนกลับไปช่อง 0'
      };
      this.codeLines = [
        'def insert_open_addressing(table, key, size):',
        '    h1 = key % size',
        '    step = (7 - (key % 7)) if strategy == "double" else 1',
        '    for probe in range(size):',
        '        slot = (h1 + (probe if strategy != "quadratic" else probe**2) * step) % size',
        '        if table[slot] is None:',
        '            table[slot] = key',
        '            return True  # แทรกสำเร็จที่ช่อง slot',
        '        # Collision: ช่องถูกครอบครอง ตรวจสอบช่องถัดไป (Wrap Around)',
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
            let specialNote = '';
            if (k === 49 && slot === 0) specialNote = ' [Wrap Around: วนกลับหัวมาช่อง 0 ด้วยการ mod TableSize อีกรอบ]';
            if (k === 58 && slot === 1) specialNote = ' [คำเตือนอาจารย์: คีย์ 58 ลงช่อง 1 ชน 3 ครั้ง ห้ามตอบช่อง 6 เด็ดขาด!]';
            if (k === 69 && slot === 2) specialNote = ' [คีย์ 69 ลงช่อง 2 ชน 3 ครั้ง]';

            steps.push({
              title: `บรรจุคีย์ ${k} ที่ช่อง index ${slot} (Probe #${probe})`,
              explanation: `ช่อง ${slot} ว่างเปล่า! บรรจุคีย์ ${k} สำเร็จ (เกิดการชนและแก้การชน ${probe} ครั้ง)${specialNote}`,
              table: [...this.table],
              activeSlot: slot,
              probeSequence: [...probes],
              vars: { key: k, slot, probe_count: probe, total_collisions: collisionCount }, line: 7
            });
            inserted = true;
            break;
          } else {
            collisionCount++;
            let collDetail = `ช่อง ${slot} มีคีย์ ${this.table[slot].key} อยู่แล้ว!`;
            if (k === 58 && slot === 0) collDetail += ' (58 ชนกับ 49 ที่ช่อง 0 หลัง Wrap Around)';
            steps.push({
              title: `⚠️ เกิดการชนที่ช่อง index ${slot} (ชนกับคีย์ ${this.table[slot].key})`,
              explanation: `${collDetail} ทำการคำนวณหาช่องถัดไปด้วยกลยุทธ์ ${this.strategy.toUpperCase()}`,
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
        title: `🎉 แทรกครบทุกคีย์ (${this.keys.length} คีย์) — สรุปข้อสอบปลายภาค ข้อที่ 1`,
        explanation: `การแทรกเสร็จสิ้น! ผลรวมการชนทั้งหมด = ${collisionCount} ครั้ง [49(1) + 58(3) + 69(3)] *** กฎเหล็กตรวจข้อสอบ ดร.ประดิษฐ์: ห้ามตอบ 14 ครั้งเด็ดขาด! ตอบ 14 ได้ 0 คะแนนทันที ***`,
        table: [...this.table],
        activeSlot: -1,
        probeSequence: [],
        vars: { total_keys: this.keys.length, load_factor: (this.keys.length / this.tableSize).toFixed(2), total_collisions: `${collisionCount} ครั้ง (ห้ามตอบ 14!)` }
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
      this.keys = [89, 18, 49, 58, 69];
      this.strategy = 'linear';
      this.tableSize = 10;
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
      renderQaPanel(container, this.qa);
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
  // 8. ASSIGNMENT 1 & CH3: POINTER SWAP SIMULATOR
  // =========================================================================
  class Assign1PointerSwapSimulator {
    constructor(containerId, preset = 'assign1') {
      this.containerId = containerId;
      this.preset = preset;
      this.steps = [];
      this.currentStep = 0;
      this.isPlaying = false;
      this.timer = null;
      this.codeLines = [];
      this.loadPreset(this.preset);
    }

    loadPreset(preset) {
      this.pause();
      this.preset = preset;
      this.steps = [];
      this.currentStep = 0;

      if (preset === 'assign1') {
        this.qa = {
          question: 'สลับโหนดค่า 1 และโหนดค่า 3 ใน Singly Linked List ที่สร้างจากรหัสนักศึกษา 612037 โดยย้ายเฉพาะ Pointer เท่านั้น (ห้ามแตะ Data) ลิสต์ผลลัพธ์คืออะไร?',
          answer: '<strong>คำสั่งสลับ Pointer:</strong><br><code>prev_x.next = curr_y</code> (โหนด 6 ชี้ไป 3)<br><code>prev_y.next = curr_x</code> (โหนด 0 ชี้ไป 1)<br><code>curr_x.next, curr_y.next = curr_y.next, curr_x.next</code><br><strong>ผลลัพธ์สุดท้าย:</strong> <code>6 -> 3 -> 2 -> 0 -> 1 -> 7</code>',
          danger: '<strong>ข้อควรระวัง:</strong> ห้ามสลับ <code>curr_x.data, curr_y.data = curr_y.data, curr_x.data</code> เด็ดขาด! อาจารย์ให้ 0 คะแนนทันทีเพราะผิดหลักการจัดการ Pointer'
        };
        this.codeLines = [
          'def swap_nodes(head, x, y):',
          '    if x == y: return head',
          '    prev_x, curr_x = None, head',
          '    while curr_x and curr_x.data != x:',
          '        prev_x, curr_x = curr_x, curr_x.next',
          '    prev_y, curr_y = None, head',
          '    while curr_y and curr_y.data != y:',
          '        prev_y, curr_y = curr_y, curr_y.next',
          '    if not curr_x or not curr_y: return head',
          '    if prev_x: prev_x.next = curr_y',
          '    else: head = curr_y',
          '    if prev_y: prev_y.next = curr_x',
          '    else: head = curr_x',
          '    curr_x.next, curr_y.next = curr_y.next, curr_x.next',
          '    return head'
        ];

        this.steps = [
          {
            title: 'สถานะเริ่มต้น: รายการเชื่อมโยงจากรหัสนักศึกษา (612037)',
            explanation: 'Linked List เริ่มต้น: 6 -> 1 -> 2 -> 0 -> 3 -> 7 โดยต้องการสลับโหนดค่า 1 (x) และโหนดค่า 3 (y) ผ่านการปรับ Pointer เท่านั้น (ห้ามสลับ Data)',
            line: 1,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 1, addr: '0x140' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 3, addr: '0x200' }, { val: 7, addr: '0x240' }
            ],
            currX: null, prevX: null, currY: null, prevY: null,
            vars: { x: 1, y: 3, prev_x: 'None', curr_x: '0x100 (6)', prev_y: 'None', curr_y: '0x100 (6)', head: '0x100 (6)' }
          },
          {
            title: 'ขั้นตอนที่ 1: ค้นหาตำแหน่งโหนด x (ค่า 1)',
            explanation: 'วนลูปตรวจสอบจนเจอ curr_x.data == 1: พบที่ address 0x140 โดยมี prev_x ชี้อยู่ที่ 0x100 (โหนด 6)',
            line: 5,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 1, addr: '0x140' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 3, addr: '0x200' }, { val: 7, addr: '0x240' }
            ],
            currX: '0x140', prevX: '0x100', currY: null, prevY: null,
            vars: { x: 1, y: 3, prev_x: '0x100 (6)', curr_x: '0x140 (1)', prev_y: 'None', curr_y: 'None' }
          },
          {
            title: 'ขั้นตอนที่ 2: ค้นหาตำแหน่งโหนด y (ค่า 3)',
            explanation: 'วนลูปตรวจสอบจนเจอ curr_y.data == 3: พบที่ address 0x200 โดยมี prev_y ชี้อยู่ที่ 0x1C0 (โหนด 0)',
            line: 8,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 1, addr: '0x140' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 3, addr: '0x200' }, { val: 7, addr: '0x240' }
            ],
            currX: '0x140', prevX: '0x100', currY: '0x200', prevY: '0x1C0',
            vars: { x: 1, y: 3, prev_x: '0x100 (6)', curr_x: '0x140 (1)', prev_y: '0x1C0 (0)', curr_y: '0x200 (3)' }
          },
          {
            title: 'ขั้นตอนที่ 3: ปรับ Pointer ของโหนดก่อนหน้า x (prev_x.next = curr_y)',
            explanation: 'prev_x (โหนด 6) ปรับ pointer .next ให้เปลี่ยนมาชี้ที่ curr_y (โหนด 3 ที่ 0x200) แทน',
            line: 10,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 1, addr: '0x140' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 3, addr: '0x200' }, { val: 7, addr: '0x240' }
            ],
            currX: '0x140', prevX: '0x100', currY: '0x200', prevY: '0x1C0',
            vars: { 'prev_x.next': '0x200 (3)', prev_y: '0x1C0 (0)', curr_x: '0x140 (1)', curr_y: '0x200 (3)' }
          },
          {
            title: 'ขั้นตอนที่ 4: ปรับ Pointer ของโหนดก่อนหน้า y (prev_y.next = curr_x)',
            explanation: 'prev_y (โหนด 0) ปรับ pointer .next ให้เปลี่ยนมาชี้ที่ curr_x (โหนด 1 ที่ 0x140) แทน',
            line: 12,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 1, addr: '0x140' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 3, addr: '0x200' }, { val: 7, addr: '0x240' }
            ],
            currX: '0x140', prevX: '0x100', currY: '0x200', prevY: '0x1C0',
            vars: { 'prev_x.next': '0x200 (3)', 'prev_y.next': '0x140 (1)', curr_x: '0x140 (1)', curr_y: '0x200 (3)' }
          },
          {
            title: 'ขั้นตอนที่ 5: สลับ .next ของ curr_x และ curr_y',
            explanation: 'curr_x.next สลับกับ curr_y.next: โหนด 1 เปลี่ยนมาชี้ที่ 7 (0x240) และโหนด 3 เปลี่ยนมาชี้ที่ 2 (0x180)',
            line: 14,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 3, addr: '0x200' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 1, addr: '0x140' }, { val: 7, addr: '0x240' }
            ],
            currX: '0x140', prevX: '0x100', currY: '0x200', prevY: '0x1C0',
            vars: { 'curr_x.next': '0x240 (7)', 'curr_y.next': '0x180 (2)', status: 'สลับ Pointer สำเร็จ!' }
          },
          {
            title: 'ขั้นตอนที่ 6: สลับสำเร็จสมบูรณ์ (ผลลัพธ์: 6 -> 3 -> 2 -> 0 -> 1 -> 7)',
            explanation: 'การสลับสำเร็จโดยไม่ต้องย้ายหน่วยความจำหรือคัดลอก Data ใดๆ ทั้งสิ้น: ลิสต์ใหม่คือ 6 -> 3 -> 2 -> 0 -> 1 -> 7',
            line: 15,
            nodes: [
              { val: 6, addr: '0x100' }, { val: 3, addr: '0x200' }, { val: 2, addr: '0x180' },
              { val: 0, addr: '0x1C0' }, { val: 1, addr: '0x140' }, { val: 7, addr: '0x240' }
            ],
            currX: null, prevX: null, currY: null, prevY: null,
            vars: { head: '0x100 (6)', result_order: '[6, 3, 2, 0, 1, 7]', time_complexity: 'O(N)', space_complexity: 'O(1)' }
          }
        ];
      } else if (preset === 'lec3') {
        this.qa = {
          question: 'ใน Lecture 3 จงสลับโหนด 4 และ 2 ในลิสต์ 1 -> 4 -> 3 -> 2 -> 5 เพื่อให้เรียงลำดับอย่างถูกต้อง',
          answer: '<strong>คำสั่งสลับ Pointer:</strong> ปรับ <code>prev_x.next = curr_y</code> (1 ชี้ 2), <code>prev_y.next = curr_x</code> (3 ชี้ 4) และสลับ .next ปลายทาง<br><strong>ผลลัพธ์สุดท้าย:</strong> <code>1 -> 2 -> 3 -> 4 -> 5</code> (Sorted)',
          danger: '<strong>ข้อควรระวัง:</strong> ต้องระบุและจำตัวแปร <code>prev_x</code> และ <code>prev_y</code> ไว้ล่วงหน้าเสมอ มิฉะนั้นจะไม่สามารถต่อสาย Pointer ย้อนกลับได้'
        };
        this.codeLines = [
          'def swap_nodes(head, x, y):',
          '    # สลับโหนด 4 และ 2 ใน 1 -> 4 -> 3 -> 2 -> 5',
          '    prev_x, curr_x = find_node(head, x)',
          '    prev_y, curr_y = find_node(head, y)',
          '    prev_x.next = curr_y',
          '    prev_y.next = curr_x',
          '    curr_x.next, curr_y.next = curr_y.next, curr_x.next',
          '    return head'
        ];
        this.steps = [
          {
            title: 'สถานะเริ่มต้น (Lecture 3 Example)',
            explanation: 'รายการเริ่มต้น: 1 -> 4 -> 3 -> 2 -> 5 ต้องการสลับโหนด 4 และ 2 เพื่อให้เรียงลำดับสมบูรณ์',
            line: 1,
            nodes: [
              { val: 1, addr: '0x100' }, { val: 4, addr: '0x140' }, { val: 3, addr: '0x180' },
              { val: 2, addr: '0x1C0' }, { val: 5, addr: '0x200' }
            ],
            vars: { x: 4, y: 2, head: '0x100 (1)' }
          },
          {
            title: 'ค้นพบตำแหน่ง x = 4 และ y = 2',
            explanation: 'prev_x = โหนด 1 (0x100), curr_x = โหนด 4 (0x140) และ prev_y = โหนด 3 (0x180), curr_y = โหนด 2 (0x1C0)',
            line: 3,
            nodes: [
              { val: 1, addr: '0x100' }, { val: 4, addr: '0x140' }, { val: 3, addr: '0x180' },
              { val: 2, addr: '0x1C0' }, { val: 5, addr: '0x200' }
            ],
            currX: '0x140', prevX: '0x100', currY: '0x1C0', prevY: '0x180',
            vars: { prev_x: '0x100 (1)', curr_x: '0x140 (4)', prev_y: '0x180 (3)', curr_y: '0x1C0 (2)' }
          },
          {
            title: 'ย้าย Pointer: prev_x.next = curr_y และ prev_y.next = curr_x',
            explanation: 'โหนด 1 เปลี่ยนมาชี้ที่ 2 (0x1C0) และโหนด 3 เปลี่ยนมาชี้ที่ 4 (0x140)',
            line: 5,
            nodes: [
              { val: 1, addr: '0x100' }, { val: 2, addr: '0x1C0' }, { val: 3, addr: '0x180' },
              { val: 4, addr: '0x140' }, { val: 5, addr: '0x200' }
            ],
            currX: '0x140', prevX: '0x100', currY: '0x1C0', prevY: '0x180',
            vars: { 'prev_x.next': '0x1C0 (2)', 'prev_y.next': '0x140 (4)' }
          },
          {
            title: 'สลับ .next ของ curr_x และ curr_y',
            explanation: 'โหนด 4 เปลี่ยนมาชี้ที่ 5 (0x200) และโหนด 2 เปลี่ยนมาชี้ที่ 3 (0x180) -> เรียงลำดับถูกต้อง 1 -> 2 -> 3 -> 4 -> 5',
            line: 7,
            nodes: [
              { val: 1, addr: '0x100' }, { val: 2, addr: '0x1C0' }, { val: 3, addr: '0x180' },
              { val: 4, addr: '0x140' }, { val: 5, addr: '0x200' }
            ],
            vars: { result: '1 -> 2 -> 3 -> 4 -> 5 (เรียงลำดับเรียบร้อย!)' }
          }
        ];
      } else if (preset === 'add_trap') {
        this.qa = {
          question: 'ถ้าเรียกเมธอด add() ที่เขียนแบบแทรกที่หัว นำเข้าเลข 1, 2, 3, 4, 5 ตามลำดับ ผลลัพธ์ในลิสต์คืออะไร? และทำไมจึงได้ 0 คะแนน?',
          answer: '<strong>ผลลัพธ์ในลิสต์:</strong> <code>5 -> 4 -> 3 -> 2 -> 1</code> (ลำดับกลับทิศทางกลายเป็น Descending Order!)',
          danger: '<strong>กับดักคะแนน 0:</strong> ข้อสอบสั่งให้เก็บ 1 ถึง 5 แบบเรียงลำดับ แต่การแทรกที่ Head เสมอทำให้ข้อมูลที่ใส่ทีหลังกลายเป็นตัวหน้าสุด (พฤติกรรม LIFO เหมือน Stack) ต้องแก้โดยแทรกที่ Tail หรือใช้ <code>append()</code>'
        };
        this.codeLines = [
          'def add(self, data):',
          '    new_node = Node(data)',
          '    new_node.next = self.head  # แทรกที่หัวเสมอ',
          '    self.head = new_node      # head อัปเดตชี้โหนดใหม่'
        ];
        this.steps = [
          {
            title: 'จุดเริ่มต้น: รายการว่างเปล่า (head = None)',
            explanation: 'ต้องการเก็บข้อมูล 1, 2, 3, 4, 5 แต่ใช้เมธอด add() ที่เขียนแบบแทรกที่หัว',
            line: 1,
            nodes: [],
            vars: { head: 'None', size: 0 }
          },
          {
            title: 'เรียก add(1)',
            explanation: 'สร้างโหนด 1 -> head ชี้ที่โหนด 1',
            line: 4,
            nodes: [{ val: 1, addr: '0x100' }],
            vars: { head: '0x100 (1)', list_preview: '1 -> None' }
          },
          {
            title: 'เรียก add(2)',
            explanation: 'สร้างโหนด 2 -> new_node.next = head (1) -> head ชี้ที่ 2',
            line: 4,
            nodes: [{ val: 2, addr: '0x140' }, { val: 1, addr: '0x100' }],
            vars: { head: '0x140 (2)', list_preview: '2 -> 1 -> None' }
          },
          {
            title: 'เรียก add(3), add(4), add(5)',
            explanation: '⚠️ กับดักที่พบบ่อยในข้อสอบ! ผลลัพธ์สุดท้ายกลับด้านกลายเป็น 5 -> 4 -> 3 -> 2 -> 1 แทนที่จะเป็น 1 -> 2 -> 3 -> 4 -> 5',
            line: 4,
            nodes: [
              { val: 5, addr: '0x200' }, { val: 4, addr: '0x1C0' }, { val: 3, addr: '0x180' },
              { val: 2, addr: '0x140' }, { val: 1, addr: '0x100' }
            ],
            vars: { head: '0x200 (5)', warning: 'ผลลัพธ์กลับทิศ (Reversed Order!)', solution: 'ต้องแทรกที่ Tail หรือใช้ append()' }
          }
        ];
      }

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
      if (playBtn) playBtn.innerHTML = '⏸️ หยุด (Pause)';
      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1300);
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

    reset() {
      this.pause();
      this.currentStep = 0;
      this.render();
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
      if (canvasEl) {
        const nodes = step.nodes || [];
        if (nodes.length === 0) {
          canvasEl.innerHTML = '<div class="studio-empty">รายการว่างเปล่า (head = None)</div>';
        } else {
          const svgW = 760;
          const svgH = 150;
          const startX = 40;
          const spacing = Math.min(115, Math.floor((svgW - 80) / nodes.length));
          let svgHtml = `<svg width="100%" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}">`;

          nodes.forEach((n, idx) => {
            const x = startX + idx * spacing;
            const y = 50;
            const isCurrX = step.currX === n.addr;
            const isCurrY = step.currY === n.addr;
            const isPrevX = step.prevX === n.addr;
            const isPrevY = step.prevY === n.addr;

            let stroke = '#6366f1';
            let fill = '#1e293b';
            let badge = '';

            if (isCurrX) { stroke = '#f59e0b'; fill = 'rgba(245, 158, 11, 0.2)'; badge = 'curr_x'; }
            else if (isCurrY) { stroke = '#06b6d4'; fill = 'rgba(6, 182, 212, 0.2)'; badge = 'curr_y'; }
            else if (isPrevX) { stroke = '#a855f7'; fill = 'rgba(168, 85, 247, 0.2)'; badge = 'prev_x'; }
            else if (isPrevY) { stroke = '#3b82f6'; fill = 'rgba(59, 130, 246, 0.2)'; badge = 'prev_y'; }

            svgHtml += `
              <g>
                <text x="${x + 35}" y="${y - 12}" fill="${stroke}" font-size="10" font-weight="700" font-family="JetBrains Mono" text-anchor="middle">${badge ? '▼ ' + badge : n.addr}</text>
                <rect x="${x}" y="${y}" width="42" height="42" rx="6" fill="${fill}" stroke="${stroke}" stroke-width="2" />
                <text x="${x + 21}" y="${y + 26}" fill="#fff" font-size="16" font-weight="800" font-family="Chakra Petch" text-anchor="middle">${n.val}</text>
                <rect x="${x + 42}" y="${y}" width="28" height="42" rx="4" fill="#0f172a" stroke="${stroke}" stroke-width="2" />
                <circle cx="${x + 56}" cy="${y + 21}" r="4" fill="${stroke}" />
              </g>
            `;

            if (idx < nodes.length - 1) {
              const arrowX = x + 70;
              const targetX = startX + (idx + 1) * spacing;
              svgHtml += `
                <line x1="${arrowX}" y1="${y + 21}" x2="${targetX}" y2="${y + 21}" stroke="${stroke}" stroke-width="2" />
                <polygon points="${targetX},${y + 21} ${targetX - 7},${y + 16} ${targetX - 7},${y + 26}" fill="${stroke}" />
              `;
            } else {
              svgHtml += `
                <line x1="${x + 70}" y1="${y + 21}" x2="${x + 95}" y2="${y + 21}" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3" />
                <text x="${x + 105}" y="${y + 25}" fill="#ef4444" font-size="11" font-family="JetBrains Mono" font-weight="700">None</text>
              `;
            }
          });

          svgHtml += '</svg>';
          canvasEl.innerHTML = svgHtml;
        }
      }

      renderCodeDebugger(container, this.codeLines, step.line);
      renderQaPanel(container, this.qa);
    }
  }

  // =========================================================================
  // 9. ASSIGNMENT 2 & CH5: TREE RECONSTRUCTION & STRICT PATH SIMULATOR
  // =========================================================================
  class Assign2TreeReconstructSimulator {
    constructor(containerId, mode = 'post_in') {
      this.containerId = containerId;
      this.mode = mode;
      this.steps = [];
      this.currentStep = 0;
      this.isPlaying = false;
      this.timer = null;
      this.codeLines = [];
      this.loadMode(this.mode);
    }

    loadMode(mode) {
      this.pause();
      this.mode = mode;
      this.steps = [];
      this.currentStep = 0;

      this.codeLines = [
        'def build_tree_post_in(inorder, postorder):',
        '    if not inorder or not postorder: return None',
        '    root_val = postorder.pop()  # ตัวสุดท้ายของ Post-order คือ Root',
        '    root = TreeNode(root_val)',
        '    idx = inorder.index(root_val)  # แบ่ง In-order เป็นซ้าย/ขวา',
        '    root.right = build_tree_post_in(inorder[idx+1:], postorder)',
        '    root.left = build_tree_post_in(inorder[:idx], postorder)',
        '    return root',
        '',
        'def strict_path_search(root, target, path=[]):',
        '    path.append(root.val)',
        '    if root.val == target: return ", ".join(path)  # กฎลูกน้ำเคร่งครัด!',
        '    return strict_path_search(root.left, target, path) or ...'
      ];

      if (mode === 'post_in') {
        this.qa = {
          question: 'สร้าง Binary Tree จาก In-order [D, B, E, A, F, C, G] และ Post-order [D, E, B, F, G, C, A] จงระบุ Root, ผล Pre-order Traversal และ Array 1-Based',
          answer: '<strong>Root หลัก:</strong> คือโหนด <code>A</code> (ตัวสุดท้ายของ Post-order)<br><strong>ผล Pre-order Traversal:</strong> <code>A, B, D, E, C, F, G</code><br><strong>ตาราง Array 1-Based:</strong> [1]=A, [2]=B, [3]=C, [4]=D, [5]=E, [6]=F, [7]=G',
          danger: '<strong>ข้อควรระวัง:</strong> ตัวสุดท้ายของ Post-order คือ Root เสมอ จากนั้นนำ Root ไปตัดแบ่ง In-order เป็นฝั่งซ้าย [D, B, E] และฝั่งขวา [F, C, G]'
        };
        this.steps = [
          {
            title: 'สถานะเริ่มต้น: กำหนดลำดับ In-order และ Post-order (Assignment 2)',
            explanation: 'In-order: [D, B, E, A, F, C, G] | Post-order: [D, E, B, F, G, C, A] -> เตรียมสร้างทวิภาคต้นไม้',
            line: 1,
            tree: null,
            inorderStr: 'D, B, E, A, F, C, G',
            postorderStr: 'D, E, B, F, G, C, A',
            vars: { root: 'None', inorder: '[D, B, E, A, F, C, G]', postorder: '[D, E, B, F, G, C, A]' }
          },
          {
            title: 'ขั้นตอนที่ 1: ดึง Root หลักตัวแรก (Post-order ตัวท้ายสุด = A)',
            explanation: 'pop() ค่าตัวสุดท้ายของ Post-order ได้ A เป็น Root -> ค้นหา A ใน In-order พบที่ตำแหน่ง index 3',
            line: 3,
            tree: { val: 'A', left: null, right: null },
            inorderStr: '[D, B, E] <== A ==> [F, C, G]',
            vars: { root_val: 'A', in_index: 3, left_inorder: '[D, B, E]', right_inorder: '[F, C, G]' }
          },
          {
            title: 'ขั้นตอนที่ 2: สร้าง Subtree ด้านขวา (Pop ได้ C)',
            explanation: 'Post-order ถัดมาคือ C -> C เป็น Root ของ Subtree ขวา -> แบ่ง In-order [F, C, G] ได้ Left: F, Right: G',
            line: 6,
            tree: { val: 'A', left: null, right: { val: 'C', left: { val: 'F' }, right: { val: 'G' } } },
            vars: { right_child: 'C', c_left: 'F', c_right: 'G' }
          },
          {
            title: 'ขั้นตอนที่ 3: สร้าง Subtree ด้านซ้าย (Pop ได้ B)',
            explanation: 'Post-order ถัดมาคือ B -> B เป็น Root ของ Subtree ซ้าย -> แบ่ง In-order [D, B, E] ได้ Left: D, Right: E',
            line: 7,
            tree: {
              val: 'A',
              left: { val: 'B', left: { val: 'D' }, right: { val: 'E' } },
              right: { val: 'C', left: { val: 'F' }, right: { val: 'G' } }
            },
            vars: { left_child: 'B', b_left: 'D', b_right: 'E', status: 'โครงสร้างต้นไม้สมบูรณ์' }
          },
          {
            title: 'ขั้นตอนที่ 4: การแทนค่าลง Array 1-Based Indexing',
            explanation: 'Root อยู่ index [1] = A, ลูกซ้าย 2i = [2] (B), ลูกขวา 2i+1 = [3] (C), ลูกของ B = [4] (D), [5] (E), ลูกของ C = [6] (F), [7] (G)',
            line: 8,
            tree: {
              val: 'A',
              left: { val: 'B', left: { val: 'D' }, right: { val: 'E' } },
              right: { val: 'C', left: { val: 'F' }, right: { val: 'G' } }
            },
            showArray: true,
            vars: { '[1] Root': 'A', '[2] Left': 'B', '[3] Right': 'C', '[4..7] Leaves': 'D, E, F, G' }
          }
        ];
      } else if (mode === 'pre_in') {
        this.qa = {
          question: 'สร้าง Binary Tree จาก Pre-order [A, B, D, E, C, F, G] และ In-order [D, B, E, A, F, C, G]',
          answer: '<strong>Root:</strong> คือโหนด <code>A</code> (ตัวแรกของ Pre-order) มี Subtree ซ้ายคือ B และ Subtree ขวาคือ C',
          danger: '<strong>ข้อควรระวัง:</strong> ใน Pre-order โหนด Root จะอยู่ตัวแรกสุด ต่างจาก Post-order ที่ Root อยู่ตัวสุดท้าย'
        };
        this.steps = [
          {
            title: 'สร้าง Tree จาก Pre-order และ In-order (Lecture 5)',
            explanation: 'Pre-order: [A, B, D, E, C, F, G] | In-order: [D, B, E, A, F, C, G] -> ตัวแรกของ Pre-order คือ Root (A)',
            line: 1,
            tree: { val: 'A', left: null, right: null },
            vars: { root: 'A', preorder_first: 'A', status: 'แยกซ้ายขวาที่ In-order index 3' }
          },
          {
            title: 'สร้างโหนดสมบูรณ์จาก Pre-order',
            explanation: 'สร้างลูกซ้าย B และลูกขวา C พร้อมทั้งโหนดใบ D, E, F, G สมบูรณ์',
            line: 8,
            tree: {
              val: 'A',
              left: { val: 'B', left: { val: 'D' }, right: { val: 'E' } },
              right: { val: 'C', left: { val: 'F' }, right: { val: 'G' } }
            },
            vars: { status: 'Reconstructed successfully' }
          }
        ];
      } else if (mode === 'strict_path') {
        this.qa = {
          question: 'จงเขียนเส้นทาง (Path) จาก Root A ไปยังโหนดใบ E และโหนด Q ตามกฎระเบียบของอาจารย์ประดิษฐ์',
          answer: '<strong>คำตอบที่ถูกต้อง 100%:</strong> <code>A, B, E</code> และ <code>A, E, J, Q</code> (คั่นด้วยเครื่องหมายจุลภาค/ลูกน้ำเท่านั้น)',
          danger: '🚨 <strong>กฎเหล็กของอาจารย์:</strong> ห้ามใส่ลูกศร <code>A -> B -> E</code> หรือ <code>A -> E -> J -> Q</code> เด็ดขาด! อาจารย์ประกาศชัดเจนว่าหากมีลูกศรจะหักคะแนนข้อนั้นทันที 100%!'
        };
        this.steps = [
          {
            title: 'ค้นหาเส้นทางไปหาโหนด E ตามกฎ Comma-Separated',
            explanation: 'เดินทางจาก Root A -> เลี้ยวซ้ายไป B -> เลี้ยวขวาไป E',
            line: 11,
            tree: {
              val: 'A',
              left: { val: 'B', left: { val: 'D' }, right: { val: 'E' } },
              right: { val: 'C', left: { val: 'F' }, right: { val: 'G' } }
            },
            highlightPath: ['A', 'B', 'E'],
            vars: { current_node: 'E', path_nodes: '[A, B, E]' }
          },
          {
            title: '⚠️ ตรวจสอบรูปแบบคำตอบ: กฎลูกน้ำเคร่งครัด (Strict Comma Rule)',
            explanation: 'อาจารย์กำหนดชัดเจน: ต้องคั่นด้วยลูกน้ำเท่านั้น "A, B, E" — หากใส่ลูกศร "A -> B -> E" จะถูกหักคะแนน 100%!',
            line: 12,
            tree: {
              val: 'A',
              left: { val: 'B', left: { val: 'D' }, right: { val: 'E' } },
              right: { val: 'C', left: { val: 'F' }, right: { val: 'G' } }
            },
            highlightPath: ['A', 'B', 'E'],
            isPathAlert: true,
            vars: { '✅ รูปแบบถูกต้อง': 'A, B, E', '❌ รูปแบบที่ถูกหัก 100%': 'A -> B -> E' }
          }
        ];
      }

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
      if (playBtn) playBtn.innerHTML = '⏸️ หยุด (Pause)';
      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1400);
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

    reset() {
      this.pause();
      this.currentStep = 0;
      this.render();
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
      if (canvasEl) {
        let html = '';
        if (step.isPathAlert) {
          html += `
            <div class="studio-path-alert">
              <span class="studio-path-badge danger">⚠️ STRICT WARNING</span>
              <span><strong>ข้อควรระวังในห้องสอบ:</strong> ห้ามใส่ลูกศรเด็ดขาด! คำตอบต้องเป็น <code>A, B, E</code> เท่านั้น (ห้ามเขียน <code>A -&gt; B -&gt; E</code>)</span>
            </div>
          `;
        }

        const svgW = 700;
        const svgH = 190;
        let svgHtml = `<svg width="100%" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}">`;

        if (step.tree) {
          const coords = {
            A: { x: 350, y: 35 },
            B: { x: 210, y: 90 },
            C: { x: 490, y: 90 },
            D: { x: 140, y: 155 },
            E: { x: 280, y: 155 },
            F: { x: 420, y: 155 },
            G: { x: 560, y: 155 }
          };

          const edges = [
            ['A', 'B'], ['A', 'C'],
            ['B', 'D'], ['B', 'E'],
            ['C', 'F'], ['C', 'G']
          ];

          edges.forEach(([p, c]) => {
            if (step.tree.left || step.tree.right) {
              const pPos = coords[p];
              const cPos = coords[c];
              if (pPos && cPos) {
                const isPath = (step.highlightPath || []).includes(p) && (step.highlightPath || []).includes(c);
                const stroke = isPath ? '#10b981' : 'rgba(255,255,255,0.2)';
                const w = isPath ? 3 : 1.8;
                svgHtml += `<line x1="${pPos.x}" y1="${pPos.y}" x2="${cPos.x}" y2="${cPos.y}" stroke="${stroke}" stroke-width="${w}" />`;
              }
            }
          });

          Object.keys(coords).forEach(key => {
            const pos = coords[key];
            const isPath = (step.highlightPath || []).includes(key);
            let fill = '#1e293b';
            let stroke = '#6366f1';
            let txtColor = '#fff';

            if (isPath) {
              fill = '#10b981';
              stroke = '#34d399';
              txtColor = '#000';
            }

            svgHtml += `
              <g>
                <circle cx="${pos.x}" cy="${pos.y}" r="16" fill="${fill}" stroke="${stroke}" stroke-width="2.2" />
                <text x="${pos.x}" y="${pos.y + 5}" fill="${txtColor}" font-weight="800" font-size="13" font-family="Chakra Petch" text-anchor="middle">${key}</text>
              </g>
            `;
          });
        }
        svgHtml += '</svg>';
        html += svgHtml;

        if (step.showArray) {
          html += `
            <div class="studio-heap-slots" style="justify-content:center;margin-top:8px;">
              <div class="studio-heap-slot is-sentinel"><span class="slot-idx">[0]</span><span class="slot-val">-</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[1]</span><span class="slot-val">A</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[2]</span><span class="slot-val">B</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[3]</span><span class="slot-val">C</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[4]</span><span class="slot-val">D</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[5]</span><span class="slot-val">E</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[6]</span><span class="slot-val">F</span></div>
              <div class="studio-heap-slot"><span class="slot-idx">[7]</span><span class="slot-val">G</span></div>
            </div>
          `;
        }

        canvasEl.innerHTML = html;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
      renderQaPanel(container, this.qa);
    }
  }

  // =========================================================================
  // 10. ASSIGNMENT 3 & CH7: MIN-HEAP HOLE VARIABLE SIMULATOR
  // =========================================================================
  class Assign3HeapSimulator {
    constructor(containerId, preset = 'insert14') {
      this.containerId = containerId;
      this.preset = preset;
      this.steps = [];
      this.currentStep = 0;
      this.isPlaying = false;
      this.timer = null;
      this.codeLines = [];
      this.loadPreset(this.preset);
    }

    loadPreset(preset) {
      this.pause();
      this.preset = preset;
      this.steps = [];
      this.currentStep = 0;

      if (preset === 'insert14') {
        this.qa = {
          question: 'แทรกค่า 14 ลงใน Min-Heap [Sentinel, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32] จงเขียนลำดับการเปลี่ยนแปลงของตัวแปร hole และอาร์เรย์ผลลัพธ์',
          answer: '<strong>ลำดับตัวแปร hole:</strong> <code>hole = 11 → hole = 5 → hole = 2</code> (เลื่อน 3 จังหวะ)<br><strong>ตำแหน่งสุดท้ายของ 14:</strong> อยู่ที่ Index <code>[2]</code><br><strong>อาร์เรย์ผลลัพธ์:</strong> <code>[-, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31]</code>',
          danger: '<strong>ข้อควรระวัง:</strong> สูตรหาโหนดพ่อคือ <code>hole // 2</code> และ Index [0] ต้องคง Sentinel (-∞) ไว้เสมอ'
        };
        this.codeLines = [
          'def insert(self, x):',
          '    self.current_size += 1',
          '    hole = self.current_size  # เริ่มสร้างช่องว่างที่ท้ายอาร์เรย์',
          '    # Percolate Up: เปรียบเทียบกับโหนดพ่อ (hole // 2)',
          '    while hole > 1 and x < self.heap[hole // 2]:',
          '        self.heap[hole] = self.heap[hole // 2]  # ดึงพ่อลงมา',
          '        hole = hole // 2                        # เลื่อน hole ขึ้น',
          '    self.heap[hole] = x  # วางค่า x ลงในช่องว่างที่ถูกต้อง'
        ];

        this.steps = [
          {
            title: 'สถานะเริ่มต้น: Min-Heap ขนาด 10 ตัว พร้อม Sentinel ที่ index 0',
            explanation: 'Array: [Sentinel, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32] ต้องการแทรกค่า 14 ลงใน Heap',
            line: 1,
            heap: [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32],
            hole: -1,
            vars: { 'array[0]': '-∞ (Sentinel)', current_size: 10, target_x: 14, hole: 'None' }
          },
          {
            title: 'ขั้นตอนที่ 1: เพิ่มขนาด current_size = 11 และสร้าง hole = 11',
            explanation: 'ขยายขนาดอาร์เรย์ สร้างช่องว่าง hole อยู่ที่ตำแหน่ง index 11 (ลูกซ้ายของโหนดที่ index 5)',
            line: 3,
            heap: [null, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32, 'HOLE'],
            hole: 11,
            vars: { hole: 11, parent_idx: '11 // 2 = 5', parent_val: 31, 'x < parent': '14 < 31 (จริง!)' }
          },
          {
            title: 'ขั้นตอนที่ 2: Percolate Up รอบที่ 1 (ดึง 31 ลงมา, hole เลื่อนไป index 5)',
            explanation: 'เนื่องจาก 14 < 31 ผิดกฎ Min-Heap จึงดึง 31 ลงมาที่ index 11 แล้วขยับ hole ขึ้นไปอยู่ที่ index 5',
            line: 6,
            heap: [null, 13, 21, 16, 24, 'HOLE', 19, 68, 65, 26, 32, 31],
            hole: 5,
            vars: { hole: 5, parent_idx: '5 // 2 = 2', parent_val: 21, 'x < parent': '14 < 21 (จริง!)' }
          },
          {
            title: 'ขั้นตอนที่ 3: Percolate Up รอบที่ 2 (ดึง 21 ลงมา, hole เลื่อนไป index 2)',
            explanation: 'เนื่องจาก 14 < 21 จึงดึง 21 ลงมาที่ index 5 แล้วขยับ hole ขึ้นไปอยู่ที่ index 2',
            line: 6,
            heap: [null, 13, 'HOLE', 16, 24, 21, 19, 68, 65, 26, 32, 31],
            hole: 2,
            vars: { hole: 2, parent_idx: '2 // 2 = 1', parent_val: 13, 'x < parent': '14 < 13 (เท็จ!)' }
          },
          {
            title: 'ขั้นตอนที่ 4: หยุดการ Percolate Up (14 ไม่น้อยกว่า Root 13)',
            explanation: 'เมื่อเปรียบเทียบกับพ่อ index 1 (ค่า 13) พบว่า 14 > 13 จึงหยุดวนลูป และวาง 14 ลงใน hole ที่ index 2',
            line: 8,
            heap: [null, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31],
            hole: -1,
            vars: { 'heap[2]': 14, status: 'แทรกสำเร็จสมบูรณ์', final_size: 11 }
          }
        ];
      } else if (preset === 'deleteMin') {
        this.qa = {
          question: 'ทำคำสั่ง deleteMin() บน Min-Heap จงระบุค่าที่ถูกส่งกลับ (Returned value) และโหนดใดจะขึ้นมาแทนที่ Root',
          answer: '<strong>ค่าที่ถูกส่งกลับ (Min Value):</strong> <code>13</code><br><strong>โหนดที่ขึ้นมาแทนที่ Root:</strong> คือโหนด <code>14</code> (เปรียบเทียบลูกซ้าย 14 กับลูกขวา 16 ดึงตัวเล็กกว่าขึ้นมา)',
          danger: '<strong>ข้อควรระวัง:</strong> การ Percolate Down ต้องเปรียบเทียบลูกทั้งสองข้างเสมอแล้วเลือก <strong>ลูกที่มีค่าน้อยกว่า</strong> ขึ้นมาแทนที่'
        };
        this.codeLines = [
          'def delete_min(self):',
          '    min_val = self.heap[1]  # ค่าต่ำสุดอยู่ที่ Root',
          '    last_val = self.heap.pop()',
          '    hole = 1',
          '    # Percolate Down: เปรียบเทียบกับลูกที่เล็กกว่า',
          '    while hole * 2 <= len(self.heap) - 1:',
          '        child = hole * 2',
          '        if child != len(self.heap) - 1 and self.heap[child+1] < self.heap[child]: child += 1',
          '        if last_val > self.heap[child]: self.heap[hole] = self.heap[child]; hole = child',
          '        else: break',
          '    self.heap[hole] = last_val; return min_val'
        ];
        this.steps = [
          {
            title: 'สถานะก่อน deleteMin: ดึง Root (13) ออก',
            explanation: 'ดึงค่าต่ำสุด 13 ออกจาก Root นำตัวสุดท้าย (31) มาเตรียม Percolate Down จาก hole = 1',
            line: 2,
            heap: [null, 'HOLE', 14, 16, 24, 21, 19, 68, 65, 26, 32],
            hole: 1,
            vars: { min_val: 13, last_val: 31, hole: 1 }
          },
          {
            title: 'Percolate Down: ดึงลูกที่เล็กกว่า (14) ขึ้นมาแทน',
            explanation: 'เปรียบเทียบลูกซ้าย (14) กับลูกขวา (16) -> 14 เล็กกว่า -> ดึง 14 ขึ้นไปที่ Root, hole เลื่อนลงไป index 2',
            line: 8,
            heap: [null, 14, 'HOLE', 16, 24, 21, 19, 68, 65, 26, 32],
            hole: 2,
            vars: { 'heap[1]': 14, hole: 2, smaller_child: 14 }
          },
          {
            title: 'Percolate Down รอบ 2: ดึงลูกที่เล็กกว่า (21) ขึ้นมาแทน',
            explanation: 'เปรียบเทียบลูกของ index 2 คือ 24 และ 21 -> 21 เล็กกว่า -> ดึง 21 ขึ้นมา, hole เลื่อนไป index 5',
            line: 8,
            heap: [null, 14, 21, 16, 24, 'HOLE', 19, 68, 65, 26, 32],
            hole: 5,
            vars: { 'heap[2]': 21, hole: 5, smaller_child: 21 }
          },
          {
            title: 'วาง last_val (31) ลงใน hole index 5',
            explanation: 'เนื่องจาก index 5 ไม่มีลูกแล้ว จึงวาง 31 ลงในช่องว่าง index 5 เสร็จสิ้นการ deleteMin',
            line: 11,
            heap: [null, 14, 21, 16, 24, 31, 19, 68, 65, 26, 32],
            hole: -1,
            vars: { 'heap[5]': 31, status: 'deleteMin สำเร็จ', returned_min: 13 }
          }
        ];
      } else if (preset === 'assign3_15') {
        this.qa = {
          question: 'แทรกข้อมูล 15 ค่าของ Assignment 3 [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2] ค่าต่ำสุดที่อยู่ที่ Root คืออะไร?',
          answer: '<strong>ค่าต่ำสุดที่ Root (Index 1):</strong> คือเลข <code>1</code> เสมอตามนิยาม Min-Heap Order Property',
          danger: '<strong>ข้อสังเกต:</strong> หากสร้างด้วย <code>build_heap()</code> (Percolate Down จาก N//2) จะใช้เวลาเพียง O(N) รวดเร็วกว่าการแทรกทีละตัว O(N log N)'
        };
        this.codeLines = [
          '# ชุดข้อมูล Assignment 3 (15 ค่า):',
          '# [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]',
          'def build_heap(arr):',
          '    heap = [float("-inf")] + arr',
          '    # ทำ Percolate Down จาก N//2 ลงมาถึง 1'
        ];
        this.steps = [
          {
            title: 'ชุดข้อมูล Assignment 3 ทั้ง 15 ค่า',
            explanation: 'ข้อมูล: 10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2 -> ค่าต่ำสุดคือ 1 จะอยู่ที่ Root index 1 เสมอ',
            line: 3,
            heap: [null, 1, 3, 2, 6, 7, 4, 8, 15, 14, 12, 9, 10, 11, 13, 5],
            hole: -1,
            vars: { root: 1, min_element: 1, total_elements: 15, height: 'floor(log2(15)) = 3' }
          }
        ];
      } else if (preset === 'deleteMin3') {
        this.qa = {
          question: 'โจทย์ข้อสอบปลายภาคจริง (10 คะแนนเต็ม): ทำ deleteMin() 3 ครั้งติดต่อกันบน Min-Heap [-, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31] จงเขียนอาร์เรย์ผลลัพธ์หลังจบแต่ละครั้ง',
          answer: '<strong>ครั้งที่ 1 (ลบ 13):</strong> <code>[-, 14, 21, 16, 24, 31, 19, 68, 65, 26, 32]</code><br><strong>ครั้งที่ 2 (ลบ 14):</strong> <code>[-, 16, 21, 19, 24, 31, 32, 68, 65, 26]</code><br><strong>ครั้งที่ 3 (ลบ 16 - คำตอบสุดท้ายข้อสอบ):</strong> <code>[-, 19, 21, 26, 24, 31, 32, 68, 65]</code>',
          danger: '<strong>กฎเหล็กข้อสอบ 10 คะแนน:</strong> 1. เมธอด deleteMin() ไม่มี Parameter ห้ามเขียน deleteMin(13) เด็ดขาด (ได้ 0 ทันที) 2. ช่อง Index 0 ต้องเว้นว่างไว้เสมอ 3. เทคนิคทำเร็วใน 5 นาทีคือวาดรูป Tree สลับค่าก่อนแล้วค่อยถอดเป็น Array!'
        };
        this.codeLines = [
          '# ข้อสอบปลายภาค: ทำ deleteMin() 3 ครั้งติดต่อกัน (10 คะแนน)',
          'min1 = myHeap.deleteMin()  # ครั้งที่ 1: ดึง 13 ออก, temp = 31, new root = 14',
          'min2 = myHeap.deleteMin()  # ครั้งที่ 2: ดึง 14 ออก, temp = 32, new root = 16',
          'min3 = myHeap.deleteMin()  # ครั้งที่ 3: ดึง 16 ออก, temp = 26, new root = 19'
        ];
        this.steps = [
          {
            title: 'สถานะก่อนทำข้อสอบ: Min-Heap 11 สมาชิก (หลังแทรก 14)',
            explanation: 'Array: [-, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31] พร้อมทำ deleteMin() 3 ครั้งติดต่อกัน',
            line: 1,
            heap: [null, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31],
            hole: -1,
            vars: { current_size: 11, root_min: 13, target_ops: 'deleteMin 3 ครั้งรวด (ข้อสอบ 10 คะแนน)' }
          },
          {
            title: 'DeleteMin ครั้งที่ 1: ดึง Root (13) ออก, temp = 31, hole = 1',
            explanation: 'ดึง 13 ออก ขนาดยุบเหลือ 10 -> เลือกลูกตัวน้อยกว่า (14 vs 16) ดึง 14 ขึ้นแทนราก -> เลือกลูกของช่อง 2 (24 vs 21) ดึง 21 ขึ้น -> วาง 31 ที่ช่อง 5',
            line: 2,
            heap: [null, 14, 21, 16, 24, 31, 19, 68, 65, 26, 32],
            hole: 5,
            vars: { returned_min: 13, temp: 31, new_root: 14, current_size: 10, 'array_round1': '[-, 14, 21, 16, 24, 31, 19, 68, 65, 26, 32]' }
          },
          {
            title: 'DeleteMin ครั้งที่ 2: ดึง Root (14) ออก, temp = 32, hole = 1',
            explanation: 'ดึง 14 ออก ขนาดยุบเหลือ 9 -> เลือกลูกตัวน้อยกว่า (21 vs 16) ดึง 16 ขึ้นแทนราก -> เลือกลูกของช่อง 3 (19 vs 68) ดึง 19 ขึ้น -> วาง 32 ที่ช่อง 6',
            line: 3,
            heap: [null, 16, 21, 19, 24, 31, 32, 68, 65, 26],
            hole: 6,
            vars: { returned_min: 14, temp: 32, new_root: 16, current_size: 9, 'array_round2': '[-, 16, 21, 19, 24, 31, 32, 68, 65, 26]' }
          },
          {
            title: 'DeleteMin ครั้งที่ 3 (คำตอบสุดท้ายข้อสอบ!): ดึง Root (16) ออก, temp = 26',
            explanation: 'ดึง 16 ออก ขนาดยุบเหลือ 8 -> เลือกลูกตัวน้อยกว่า (21 vs 19) ดึง 19 ขึ้นแทนราก -> เปรียบเทียบกับลูกช่อง 6 (32) พบว่า 26 < 32 หยุด! วาง 26 ที่ช่อง 3',
            line: 4,
            heap: [null, 19, 21, 26, 24, 31, 32, 68, 65],
            hole: 3,
            vars: { returned_min: 16, temp: 26, final_root: 19, current_size: 8, 'final_answer_array': '[-, 19, 21, 26, 24, 31, 32, 68, 65]' }
          }
        ];
      }

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
      if (playBtn) playBtn.innerHTML = '⏸️ หยุด (Pause)';
      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1400);
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

    reset() {
      this.pause();
      this.currentStep = 0;
      this.render();
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
      if (canvasEl) {
        let slotsHtml = '<div class="studio-heap-slots">';
        const arr = step.heap || [];
        arr.forEach((val, idx) => {
          if (idx === 0) {
            slotsHtml += '<div class="studio-heap-slot is-sentinel"><span class="slot-idx">[0]</span><span class="slot-val">-∞</span></div>';
          } else {
            const isHole = idx === step.hole || val === 'HOLE';
            const cls = isHole ? 'studio-heap-slot is-hole' : 'studio-heap-slot';
            const displayVal = isHole ? '?' : (val !== null ? val : '·');
            slotsHtml += `<div class="${cls}"><span class="slot-idx">[${idx}]</span><span class="slot-val">${displayVal}</span></div>`;
          }
        });
        slotsHtml += '</div>';

        // Render Compact Tree Representation
        const svgW = 760;
        const svgH = 240;
        let svgHtml = `<svg width="100%" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}">`;
        const treeCoords = [
          null,
          { x: 380, y: 30 },
          { x: 210, y: 85 }, { x: 550, y: 85 },
          { x: 125, y: 145 }, { x: 295, y: 145 }, { x: 465, y: 145 }, { x: 635, y: 145 },
          { x: 75, y: 205 }, { x: 175, y: 205 }, { x: 245, y: 205 }, { x: 345, y: 205 }
        ];

        for (let i = 1; i <= Math.min(arr.length - 1, 11); i++) {
          const pIdx = Math.floor(i / 2);
          if (pIdx >= 1 && treeCoords[pIdx] && treeCoords[i]) {
            svgHtml += `<line x1="${treeCoords[pIdx].x}" y1="${treeCoords[pIdx].y}" x2="${treeCoords[i].x}" y2="${treeCoords[i].y}" stroke="rgba(255,255,255,0.18)" stroke-width="1.8" />`;
          }
        }

        for (let i = 1; i <= Math.min(arr.length - 1, 11); i++) {
          const pos = treeCoords[i];
          if (!pos) continue;
          const isHole = i === step.hole || arr[i] === 'HOLE';
          const fill = isHole ? 'rgba(245, 158, 11, 0.25)' : '#1e293b';
          const stroke = isHole ? '#f59e0b' : '#6366f1';
          const txt = isHole ? '?' : arr[i];
          svgHtml += `
            <g>
              <circle cx="${pos.x}" cy="${pos.y}" r="14" fill="${fill}" stroke="${stroke}" stroke-width="2" />
              <text x="${pos.x}" y="${pos.y + 4}" fill="#fff" font-size="11" font-weight="700" font-family="Chakra Petch" text-anchor="middle">${txt}</text>
              <text x="${pos.x}" y="${pos.y - 16}" fill="var(--text-muted)" font-size="9" font-family="JetBrains Mono" text-anchor="middle">[${i}]</text>
            </g>
          `;
        }
        svgHtml += '</svg>';

        canvasEl.innerHTML = svgHtml + slotsHtml;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
      renderQaPanel(container, this.qa);
    }
  }

  // =========================================================================
  // 11. ASSIGNMENT 4 & CH9: GRAPH BFS SHORTEST PATH SIMULATOR
  // =========================================================================
  class Assign4GraphSimulator {
    constructor(containerId, preset = 'bfs') {
      this.containerId = containerId;
      this.preset = preset;
      this.steps = [];
      this.currentStep = 0;
      this.isPlaying = false;
      this.timer = null;
      this.codeLines = [];
      this.loadPreset(this.preset);
    }

    loadPreset(preset) {
      this.pause();
      this.preset = preset;
      this.steps = [];
      this.currentStep = 0;

      this.codeLines = [
        'def unweighted_shortest_path(graph, start):',
        '    table = {v: {"known": False, "dist": float("inf"), "path": None} for v in graph}',
        '    table[start]["dist"] = 0',
        '    queue = [start]',
        '    while queue:',
        '        curr = queue.pop(0)',
        '        table[curr]["known"] = True',
        '        for neighbor in graph[curr]:',
        '            if table[neighbor]["dist"] == float("inf"):',
        '                table[neighbor]["dist"] = table[curr]["dist"] + 1',
        '                table[neighbor]["path"] = curr',
        '                queue.append(neighbor)',
        '    return table'
      ];

      if (preset === 'bfs') {
        this.qa = {
          question: 'จากกราฟระบุทิศทาง 7 จุดยอด (V1..V7) จงหา Shortest Path จาก V1 ไปยัง V7 พร้อมระยะทางสั้นสุด และตารางสถานะสุดท้าย',
          answer: '<strong>Shortest Path ไปยัง V7:</strong> <code>V1 -> V4 -> V7</code><br><strong>ระยะทางสั้นสุด (d_v7):</strong> <code>2</code> Edges<br><strong>ตารางสถานะ:</strong> V1(T,0,0), V2(T,1,V1), V3(T,2,V4), V4(T,1,V1), V5(T,2,V2), V6(T,2,V4), V7(T,2,V4)',
          danger: '<strong>ข้อควรระวัง:</strong> ในคอลัมน์ p_v ต้องบันทึกจุดยอดก่อนหน้าที่ทำให้เกิดระยะทางสั้นที่สุดเท่านั้น'
        };
        this.steps = [
          {
            title: 'เริ่มต้นการค้นหา BFS Shortest Path จาก V1 (Digraph 7 จุดยอด)',
            explanation: 'กราฟ Assignment 4 มี 7 จุดยอด (V1..V7) และ 12 เส้นเชื่อมระบุทิศทาง: กำหนด start = V1, dist[V1] = 0, Queue = [V1]',
            line: 4,
            activeV: 'V1',
            queue: ['V1'],
            table: {
              V1: { known: false, dist: 0, path: 0 },
              V2: { known: false, dist: '∞', path: 0 },
              V3: { known: false, dist: '∞', path: 0 },
              V4: { known: false, dist: '∞', path: 0 },
              V5: { known: false, dist: '∞', path: 0 },
              V6: { known: false, dist: '∞', path: 0 },
              V7: { known: false, dist: '∞', path: 0 }
            },
            vars: { curr: 'V1', queue: '[V1]', dist_v1: 0 }
          },
          {
            title: 'สเต็ป 1: Dequeue V1 -> อัปเดต Known = True, ตรวจสอบเพื่อนบ้าน V2, V4',
            explanation: 'V1 เชื่อมไปยัง V2 และ V4 -> ตั้งค่า dist[V2]=1, path=V1 และ dist[V4]=1, path=V1 -> Enqueue V2, V4',
            line: 7,
            activeV: 'V1',
            queue: ['V2', 'V4'],
            table: {
              V1: { known: true, dist: 0, path: 0 },
              V2: { known: false, dist: 1, path: 'V1' },
              V3: { known: false, dist: '∞', path: 0 },
              V4: { known: false, dist: 1, path: 'V1' },
              V5: { known: false, dist: '∞', path: 0 },
              V6: { known: false, dist: '∞', path: 0 },
              V7: { known: false, dist: '∞', path: 0 }
            },
            vars: { curr: 'V1', queue: '[V2, V4]', neighbors: 'V2 (d=1), V4 (d=1)' }
          },
          {
            title: 'สเต็ป 2: Dequeue V2 -> ตรวจสอบเพื่อนบ้าน V4, V5',
            explanation: 'V2 มีเส้นทางไป V4 (ระยะ 1 อยู่แล้ว) และ V5 -> ตั้ง dist[V5]=2, path=V2 -> Enqueue V5',
            line: 7,
            activeV: 'V2',
            queue: ['V4', 'V5'],
            table: {
              V1: { known: true, dist: 0, path: 0 },
              V2: { known: true, dist: 1, path: 'V1' },
              V3: { known: false, dist: '∞', path: 0 },
              V4: { known: false, dist: 1, path: 'V1' },
              V5: { known: false, dist: 2, path: 'V2' },
              V6: { known: false, dist: '∞', path: 0 },
              V7: { known: false, dist: '∞', path: 0 }
            },
            vars: { curr: 'V2', queue: '[V4, V5]', relaxed: 'V5 (d=2)' }
          },
          {
            title: 'สเต็ป 3: Dequeue V4 -> ตรวจสอบเพื่อนบ้าน V3, V5, V6, V7',
            explanation: 'V4 มีเส้นเชื่อมกระจาย 4 ทาง: ปรับ dist[V3]=2, dist[V6]=2, dist[V7]=2 (path=V4 ทั้งหมด!) -> Enqueue V3, V6, V7',
            line: 11,
            activeV: 'V4',
            queue: ['V5', 'V3', 'V6', 'V7'],
            table: {
              V1: { known: true, dist: 0, path: 0 },
              V2: { known: true, dist: 1, path: 'V1' },
              V3: { known: false, dist: 2, path: 'V4' },
              V4: { known: true, dist: 1, path: 'V1' },
              V5: { known: false, dist: 2, path: 'V2' },
              V6: { known: false, dist: 2, path: 'V4' },
              V7: { known: false, dist: 2, path: 'V4' }
            },
            vars: { curr: 'V4', queue: '[V5, V3, V6, V7]', path_to_v7: 'V1 -> V4 -> V7 (Dist=2)' }
          },
          {
            title: 'สเต็ป 4: Dequeue จุดยอดที่เหลือ (V5, V3, V6, V7)',
            explanation: 'ทุกจุดยอดถูกมาร์ก Known = True ครบถ้วน ได้ Shortest Path ไปยังทุกโหนดอย่างสมบูรณ์',
            line: 13,
            activeV: 'V7',
            queue: [],
            table: {
              V1: { known: true, dist: 0, path: 0 },
              V2: { known: true, dist: 1, path: 'V1' },
              V3: { known: true, dist: 2, path: 'V4' },
              V4: { known: true, dist: 1, path: 'V1' },
              V5: { known: true, dist: 2, path: 'V2' },
              V6: { known: true, dist: 2, path: 'V4' },
              V7: { known: true, dist: 2, path: 'V4' }
            },
            vars: { final_path_v7: 'V1 -> V4 -> V7', min_distance: 2, complexity: 'O(|V| + |E|)' }
          }
        ];
      } else if (preset === 'ram_waste') {
        this.qa = {
          question: 'จงแสดงวิธีคำนวณความสูญเปล่าของหน่วยความจำ (Memory Waste) เมื่อเก็บกราฟ 7 จุดยอด 12 เส้นเชื่อมด้วย Adjacency Matrix',
          answer: '<strong>จำนวนช่องทั้งหมด:</strong> 7 x 7 = 49 ช่อง<br><strong>ช่องที่มีเส้นเชื่อมจริง (1):</strong> 12 ช่อง<br><strong>ช่องว่างที่สูญเปล่า (0):</strong> 49 - 12 = 37 ช่อง<br><strong>คิดเป็นความสูญเปล่า:</strong> (37 / 49) x 100% = <strong>75.51%</strong> (≈ 75.69%)',
          danger: '<strong>ข้อสรุปในข้อสอบ:</strong> กราฟที่มีเส้นเชื่อมน้อย (Sparse Graph) ไม่ควรใช้ Adjacency Matrix ให้เปลี่ยนไปใช้ Adjacency List แทน'
        };
        this.steps = [
          {
            title: 'เปรียบเทียบความคุ้มค่าหน่วยความจำ: Adjacency Matrix vs Adjacency List',
            explanation: 'กราฟ 7 จุดยอดมีขนาด Matrix = 7 x 7 = 49 ช่อง แต่มีเส้นเชื่อมจริงเพียง 12 เส้น -> เกิดความสูญเปล่าหน่วยความจำสูงถึง 75.51%!',
            line: 2,
            activeV: null,
            queue: [],
            table: {},
            vars: { total_cells: '7 x 7 = 49', edges_used: 12, empty_cells: 37, 'memory_waste_%': '75.51%', solution: 'ควรใช้ Adjacency List' }
          }
        ];
      } else if (preset === 'topological') {
        this.qa = {
          question: 'จงระบุ In-degree ของจุดยอดทุกตัว และอธิบายหลักการเริ่มต้นทำ Topological Sort',
          answer: '<strong>In-degrees:</strong> V1: 1, V2: 1, V3: 1, V4: 2, V5: 2, V6: 3, V7: 2<br><strong>หลักการ:</strong> นำจุดยอดที่มี In-degree = 0 ใส่ลงใน Queue เพื่อเป็นจุดเริ่มต้นกระบวนการ',
          danger: '<strong>ข้อควรระวัง:</strong> หากกราฟมี Cycle (วงรอบ) จะไม่มีจุดยอดใดที่มี In-degree = 0 และไม่สามารถทำ Topological Sort ได้'
        };
        this.steps = [
          {
            title: 'ตาราง Indegree สำหรับ Topological Sort (Lecture 9 / Assign 4)',
            explanation: 'นับจำนวน In-degree ของแต่ละโหนด: V1=1, V2=1, V3=1, V4=2, V5=2, V6=3, V7=2 -> จุดยอดที่มี In-degree = 0 สามารถเริ่มทำก่อนได้',
            line: 1,
            activeV: null,
            queue: [],
            table: {},
            vars: { 'In-degree V1': 1, 'In-degree V2': 1, 'In-degree V3': 1, 'In-degree V4': 2, 'In-degree V5': 2, 'In-degree V6': 3, 'In-degree V7': 2 }
          }
        ];
      }

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
      if (playBtn) playBtn.innerHTML = '⏸️ หยุด (Pause)';
      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1500);
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

    reset() {
      this.pause();
      this.currentStep = 0;
      this.render();
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
      if (canvasEl) {
        const svgW = 740;
        const svgH = 210;
        const vPos = {
          V1: { x: 75, y: 105 },
          V2: { x: 210, y: 45 },
          V3: { x: 210, y: 165 },
          V4: { x: 360, y: 105 },
          V5: { x: 510, y: 45 },
          V6: { x: 660, y: 105 },
          V7: { x: 510, y: 165 }
        };

        const edges = [
          ['V1', 'V2'], ['V1', 'V4'],
          ['V2', 'V4'], ['V2', 'V5'],
          ['V3', 'V1'], ['V3', 'V6'],
          ['V4', 'V3'], ['V4', 'V5'], ['V4', 'V6'], ['V4', 'V7'],
          ['V5', 'V7'],
          ['V7', 'V6']
        ];

        let svgHtml = `<svg width="100%" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}">`;
        edges.forEach(([u, v]) => {
          const p1 = vPos[u], p2 = vPos[v];
          svgHtml += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="rgba(255,255,255,0.2)" stroke-width="1.6" />`;
        });

        Object.keys(vPos).forEach(k => {
          const p = vPos[k];
          const info = (step.table && step.table[k]) || {};
          const isActive = step.activeV === k;
          let fill = '#1e293b';
          let stroke = '#6366f1';
          if (isActive) { fill = 'rgba(245, 158, 11, 0.3)'; stroke = '#f59e0b'; }
          else if (info.known) { fill = 'rgba(16, 185, 129, 0.2)'; stroke = '#10b981'; }

          svgHtml += `
            <g>
              <circle cx="${p.x}" cy="${p.y}" r="17" fill="${fill}" stroke="${stroke}" stroke-width="2" />
              <text x="${p.x}" y="${p.y + 4}" fill="#fff" font-size="11" font-weight="800" font-family="Chakra Petch" text-anchor="middle">${k}</text>
              <text x="${p.x}" y="${p.y - 20}" fill="var(--cyan)" font-size="9" font-family="JetBrains Mono" text-anchor="middle">d=${info.dist !== undefined ? info.dist : '?'}</text>
            </g>
          `;
        });
        svgHtml += '</svg>';

        let extraHtml = '';
        if (step.table && Object.keys(step.table).length > 0) {
          extraHtml += `
            <table class="studio-bfs-table">
              <thead>
                <tr><th>Vertex</th><th>Known</th><th>$d_v$ (Dist)</th><th>$p_v$ (Path)</th></tr>
              </thead>
              <tbody>
          `;
          Object.keys(step.table).forEach(vKey => {
            const row = step.table[vKey];
            const isKnown = row.known;
            extraHtml += `
              <tr class="${step.activeV === vKey ? 'is-active-row' : ''}">
                <td>${vKey}</td>
                <td class="${isKnown ? 'known-true' : 'known-false'}">${isKnown ? 'True (T)' : 'False (F)'}</td>
                <td>${row.dist}</td>
                <td>${row.path || '0'}</td>
              </tr>
            `;
          });
          extraHtml += '</tbody></table>';
        }

        canvasEl.innerHTML = svgHtml + extraHtml;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
      renderQaPanel(container, this.qa);
    }
  }

  // =========================================================================
  // 12. TEST PROGRAM 1 & 2: QUEUE & SORTING SUITE SIMULATOR
  // =========================================================================
  class TestProgramSuiteSimulator {
    constructor(containerId, mode = 'queue_overflow') {
      this.containerId = containerId;
      this.mode = mode;
      this.steps = [];
      this.currentStep = 0;
      this.isPlaying = false;
      this.timer = null;
      this.codeLines = [];
      this.loadMode(this.mode);
    }

    loadMode(mode) {
      this.pause();
      this.mode = mode;
      this.steps = [];
      this.currentStep = 0;

      if (mode === 'queue_overflow') {
        this.qa = {
          question: 'ใน program.py กำหนด Queue(5) แล้วเรียก enqueue() 7 ครั้งติดต่อกัน จะเกิดอะไรขึ้นในครั้งที่ 6?',
          answer: '<strong>ผลลัพธ์:</strong> เกิดข้อผิดพลาด <code>QueueOverflowException: Queue is full!</code> ในการ Enqueue ครั้งที่ 6 เพราะ count == capacity (5 == 5)',
          danger: '<strong>ข้อควรระวัง:</strong> ต้องเขียนดักจับด้วย <code>try ... except QueueOverflowException</code> เพื่อไม่ให้โปรแกรมหยุดทำงาน'
        };
        this.codeLines = [
          'class Queue:',
          '    def __init__(self, capacity=5):',
          '        self.capacity = capacity',
          '        self.items = [None] * capacity',
          '        self.front = self.rear = self.count = 0',
          '    def enqueue(self, item):',
          '        if self.count == self.capacity:',
          '            raise QueueOverflowException("Queue is full!")',
          '        self.items[self.rear] = item',
          '        self.rear = (self.rear + 1) % self.capacity',
          '        self.count += 1'
        ];
        this.steps = [
          {
            title: 'สร้าง Queue(5) ว่างเปล่า (program.py Test 1)',
            explanation: 'กำหนด capacity = 5 ช่อง (items = [None, None, None, None, None]), front = 0, rear = 0, count = 0',
            line: 5,
            items: [null, null, null, null, null], front: 0, rear: 0, count: 0,
            vars: { capacity: 5, count: 0, front: 0, rear: 0, status: 'Empty' }
          },
          {
            title: 'Enqueue(10), Enqueue(20), Enqueue(30), Enqueue(40)',
            explanation: 'นำข้อมูลเข้าคิว 4 ตัว: items = [10, 20, 30, 40, None], rear = 4, count = 4',
            line: 9,
            items: [10, 20, 30, 40, null], front: 0, rear: 4, count: 4,
            vars: { capacity: 5, count: 4, front: 0, rear: 4, status: 'Normal' }
          },
          {
            title: 'Enqueue(50) -> คิวเต็มพอดี (Full)',
            explanation: 'items = [10, 20, 30, 40, 50], rear วน modulo กลับไปที่ (4+1)%5 = 0, count = 5 เต็มความจุ!',
            line: 10,
            items: [10, 20, 30, 40, 50], front: 0, rear: 0, count: 5,
            vars: { capacity: 5, count: 5, front: 0, rear: 0, status: 'FULL' }
          },
          {
            title: '⚠️ Enqueue(60) ตัวที่ 6 -> ตรวจสอบ self.count == self.capacity',
            explanation: 'เนื่องจาก count (5) == capacity (5) ทำให้เข้าเงื่อนไขบรรทัดที่ 7 -> พ่น QueueOverflowException("Queue is full!") ทันที!',
            line: 8,
            items: [10, 20, 30, 40, 50], front: 0, rear: 0, count: 5, isException: true,
            vars: { '🚨 Exception': 'QueueOverflowException', message: 'Queue is full!', line: 8 }
          }
        ];
      } else if (mode === 'queue_underflow') {
        this.qa = {
          question: 'ใน program.py กำหนด Queue(6) แล้วเรียก dequeue() 7 ครั้ง จะเกิดอะไรขึ้นในครั้งที่ 7?',
          answer: '<strong>ผลลัพธ์:</strong> เกิดข้อผิดพลาด <code>QueueUnderflowException: Queue is empty!</code> ในการ Dequeue ครั้งที่ 7 เพราะ count == 0',
          danger: '<strong>ข้อควรระวัง:</strong> ก่อนเรียก dequeue() ควรตรวจสอบด้วย <code>is_empty()</code> เสมอ'
        };
        this.codeLines = [
          '    def dequeue(self):',
          '        if self.count == 0:',
          '            raise QueueUnderflowException("Queue is empty!")',
          '        val = self.items[self.front]',
          '        self.items[self.front] = None',
          '        self.front = (self.front + 1) % self.capacity',
          '        self.count -= 1',
          '        return val'
        ];
        this.steps = [
          {
            title: 'Dequeue ตัวที่ 1 ถึง 6 จนหมดคิว',
            explanation: 'ดึงข้อมูลออก 6 ครั้งติดต่อกันจน count ลดลงเหลือ 0 คิวว่างเปล่าสมบูรณ์',
            line: 7,
            items: [null, null, null, null, null, null], front: 0, rear: 0, count: 0,
            vars: { count: 0, status: 'คิวว่าง (Empty)' }
          },
          {
            title: '⚠️ Dequeue ครั้งที่ 7 -> เกิด QueueUnderflowException',
            explanation: 'ตรวจพบ self.count == 0 ในบรรทัดที่ 2 -> ยกเว้นข้อผิดพลาด QueueUnderflowException("Queue is empty!") ตามโจทย์ Test 1',
            line: 3,
            items: [null, null, null, null, null, null], front: 0, rear: 0, count: 0, isException: true,
            vars: { '🚨 Exception': 'QueueUnderflowException', message: 'Queue is empty!' }
          }
        ];
      } else if (mode === 'insertion_moves') {
        this.qa = {
          question: 'ใน Test Program 2 นำอาร์เรย์ [29, 10, 14, 37, 13] มาเรียงด้วย Insertion Sort จงนับจำนวน Position Moves รวมทั้งหมด และแจกแจงแต่ละ Pass',
          answer: '<strong>ผลรวม Position Moves ทั้งหมด = 9 ครั้ง</strong><br>• Pass 1 (i=1, key=10): เลื่อน 29 (+1), วาง 10 (+1) = <strong>2 Moves</strong><br>• Pass 2 (i=2, key=14): เลื่อน 29 (+1), วาง 14 (+1) = <strong>2 Moves</strong><br>• Pass 3 (i=3, key=37): ไม่เลื่อน (+0), วาง 37 (+1) = <strong>1 Move</strong><br>• Pass 4 (i=4, key=13): เลื่อน 37, 29, 14 (+3), วาง 13 (+1) = <strong>4 Moves</strong><br><strong>รวม:</strong> 2 + 2 + 1 + 4 = <strong>9 Moves</strong>',
          danger: '⚠️ <strong>เกณฑ์ตรวจของอาจารย์ประดิษฐ์:</strong> ให้นับทั้งการเลื่อนสมาชิกไปทางขวา (Shift) และนับจังหวะนำ key วางลงในช่องว่างด้วย! จึงได้ 9 Moves ตรงตามเฉลย'
        };
        this.codeLines = [
          'def insertion_sort(arr):',
          '    total_moves = 0',
          '    for i in range(1, len(arr)):',
          '        key = arr[i]',
          '        j = i - 1',
          '        while j >= 0 and arr[j] > key:',
          '            arr[j + 1] = arr[j]  # Move 1: เลื่อนสมาชิก (+1)',
          '            total_moves += 1; j -= 1',
          '        arr[j + 1] = key          # Move 2: วาง key (+1)',
          '        total_moves += 1',
          '    return total_moves'
        ];
        this.steps = [
          {
            title: 'สถานะเริ่มต้น: อาร์เรย์ [29, 10, 14, 37, 13] (Test Program 2)',
            explanation: 'โจทย์สอบกำหนดให้นับจำนวน Position Move ทั้งหมด (นับทั้งการเลื่อนช่อง และการวาง key ลงช่อง)',
            line: 2,
            arr: [29, 10, 14, 37, 13], moves: 0,
            vars: { array: '[29, 10, 14, 37, 13]', total_moves: 0 }
          },
          {
            title: 'Pass 1 (i=1): key = 10 -> เลื่อน 29 ขวา (+1), วาง 10 (+1) = 2 Moves',
            explanation: 'เปรียบเทียบ 10 กับ 29 -> เลื่อน 29 ไป index 1 แล้ววาง 10 ที่ index 0: อาร์เรย์เป็น [10, 29, 14, 37, 13]',
            line: 9,
            arr: [10, 29, 14, 37, 13], moves: 2,
            vars: { key: 10, pass_moves: 2, total_moves: 2 }
          },
          {
            title: 'Pass 2 (i=2): key = 14 -> เลื่อน 29 ขวา (+1), วาง 14 (+1) = 2 Moves',
            explanation: 'เปรียบเทียบ 14 กับ 29 -> เลื่อน 29 แล้ววาง 14 ที่ index 1: อาร์เรย์เป็น [10, 14, 29, 37, 13]',
            line: 9,
            arr: [10, 14, 29, 37, 13], moves: 4,
            vars: { key: 14, pass_moves: 2, total_moves: 4 }
          },
          {
            title: 'Pass 3 (i=3): key = 37 -> ไม่ต้องเลื่อน, วาง 37 (+1) = 1 Move',
            explanation: '37 มากกว่า 29 อยู่แล้ว ไม่มีการเลื่อนสมาชิก วาง 37 ตำแหน่งเดิม: อาร์เรย์เป็น [10, 14, 29, 37, 13]',
            line: 9,
            arr: [10, 14, 29, 37, 13], moves: 5,
            vars: { key: 37, pass_moves: 1, total_moves: 5 }
          },
          {
            title: 'Pass 4 (i=4): key = 13 -> เลื่อน 37, 29, 14 (+3), วาง 13 (+1) = 4 Moves',
            explanation: '13 น้อยกว่า 37, 29, 14 เลื่อนทั้ง 3 ตัวไปทางขวา แล้ววาง 13 ที่ index 1: รวมสเต็ปนี้ได้ 4 Moves',
            line: 9,
            arr: [10, 13, 14, 29, 37], moves: 9,
            vars: { key: 13, pass_moves: 4, total_moves: 9, status: 'เรียงเสร็จสมบูรณ์!' }
          },
          {
            title: 'สรุปเฉลยข้อสอบ Test Program 2: นับ Position Move ทั้งหมด = 9 Moves',
            explanation: 'Pass 1 (2) + Pass 2 (2) + Pass 3 (1) + Pass 4 (4) = 9 Moves ตรงกับเฉลยข้อสอบอย่างสมบูรณ์แบบ!',
            line: 11,
            arr: [10, 13, 14, 29, 37], moves: 9,
            vars: { final_moves: 9, formula: 'Pass1(2) + Pass2(2) + Pass3(1) + Pass4(4) = 9' }
          }
        ];
      } else if (mode === 'circular_modulo') {
        this.qa = {
          question: 'จงเขียนสูตรการเลื่อน Front และ Rear ใน Circular Queue แบบไม่ล้น Buffer',
          answer: '<strong>สูตรเลื่อน Rear:</strong> <code>rear = (rear + 1) % capacity</code><br><strong>สูตรเลื่อน Front:</strong> <code>front = (front + 1) % capacity</code>',
          danger: '<strong>ข้อควรระวัง:</strong> ห้ามใช้ <code>rear += 1</code> เดี่ยวๆ เพราะเมื่อถึงช่องสุดท้ายจะเกิด <code>IndexError</code>'
        };
        this.codeLines = [
          '# Circular Modulo Wrap-Around Formula:',
          'rear = (rear + 1) % capacity',
          'front = (front + 1) % capacity'
        ];
        this.steps = [
          {
            title: 'สูตร Modulo Wrap-Around ในคิววงกลม',
            explanation: 'เมื่อ rear หรือ front เดินทางถึง index สุดท้าย (capacity - 1) ตัวถัดไปจะถูกวนกลับไปที่ index 0 อัตโนมัติด้วย % capacity',
            line: 2,
            items: [10, 20, 30, 40, 50], front: 2, rear: 1, count: 4,
            vars: { formula: '(index + 1) % 5', '4 + 1 % 5': 0 }
          }
        ];
      }

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
      if (playBtn) playBtn.innerHTML = '⏸️ หยุด (Pause)';
      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 1400);
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

    reset() {
      this.pause();
      this.currentStep = 0;
      this.render();
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
      if (canvasEl) {
        let html = '';
        if (step.isException) {
          html += `
            <div class="studio-path-alert" style="background:rgba(239, 68, 68, 0.25);border-color:#ef4444;">
              <span class="studio-path-badge danger">🚨 EXCEPTION RAISED</span>
              <span><strong>เกิดข้อผิดพลาด:</strong> ${step.vars['🚨 Exception']} — "${step.vars.message}"</span>
            </div>
          `;
        }

        if (step.items) {
          html += '<div class="studio-queue-tape">';
          step.items.forEach((val, idx) => {
            const isF = idx === step.front && step.count > 0;
            const isR = idx === step.rear;
            let cls = 'studio-queue-slot';
            if (isF) cls += ' is-front';
            if (isR) cls += ' is-rear';
            if (val === null) cls += ' is-empty';

            html += `
              <div class="${cls}">
                ${isF ? '<span class="q-tag front-tag">FRONT</span>' : ''}
                ${isR ? '<span class="q-tag rear-tag">REAR</span>' : ''}
                <span class="q-val">${val !== null ? val : '·'}</span>
                <span class="q-idx">[${idx}]</span>
              </div>
            `;
          });
          html += '</div>';
        } else if (step.arr) {
          const maxVal = Math.max(...step.arr, 1);
          html += '<div class="studio-sort-bars">';
          step.arr.forEach((val, idx) => {
            const heightPct = Math.round((val / maxVal) * 100);
            html += `
              <div class="sort-bar-col">
                <div class="sort-bar is-sorted" style="height: ${Math.max(20, heightPct)}%;">
                  <span class="bar-val">${val}</span>
                </div>
                <span class="bar-idx">[${idx}]</span>
              </div>
            `;
          });
          html += '</div>';
          if (step.moves !== undefined) {
            html += `
              <div style="text-align:center;margin-top:10px;font-family:var(--font-mono);font-size:13px;color:#a5b4fc;">
                Position Moves สะสม: <strong style="color:#f59e0b;font-size:18px;">${step.moves}</strong> Moves
              </div>
            `;
          }
        }

        canvasEl.innerHTML = html;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
      renderQaPanel(container, this.qa);
    }
  }

  // =========================================================================
  // 13. 0EXERCISES & CH1: BIG-O & INDENTATION SIMULATOR
  // =========================================================================
  class BigOExercisesSimulator {
    constructor(containerId, mode = 'indent_bug_inside') {
      this.containerId = containerId;
      this.mode = mode;
      this.steps = [];
      this.currentStep = 0;
      this.isPlaying = false;
      this.timer = null;
      this.codeLines = [];
      this.loadMode(this.mode);
    }

    loadMode(mode) {
      this.pause();
      this.mode = mode;
      this.steps = [];
      this.currentStep = 0;

      if (mode === 'indent_bug_inside') {
        this.qa = {
          question: 'ในฟังก์ชัน function(n) ถ้าคำสั่ง print("*") เยื้องอยู่ในลูป j จะพิมพ์ดาวกี่ดวงเมื่อ n=5? ความซับซ้อน Big-O คือเท่าใด?',
          answer: '<strong>จำนวนดาวที่พิมพ์:</strong> <strong>25 ดวง</strong> (5 x 5 = 25)<br><strong>ความซับซ้อน Time Complexity:</strong> <code>O(N²)</code>',
          danger: '<strong>กับดักคะแนน 0:</strong> เกิดจากการกด Tab เกิน 1 ครั้ง ทำให้คำสั่งถูกดึงเข้าไปในลูปด้านในโดยไม่รู้ตัว'
        };
        this.codeLines = [
          '# Case A: print("*") เยื้องเข้าไปในลูป j (Bug ยอดฮิต!)',
          'def function_bug(n=5):',
          '    for i in range(n):',
          '        for j in range(n):',
          '            print("*")  # รัน n * n = 25 ครั้ง! O(n^2)'
        ];
        this.steps = [];
        let count = 0;
        for (let i = 0; i < 5; i++) {
          for (let j = 0; j < 5; j++) {
            count++;
            this.steps.push({
              title: `รอบที่ ${count}: i = ${i}, j = ${j} (รันคำสั่ง print)`,
              explanation: `print("*") อยู่ในลูปในสุด (j) ทำให้พิมพ์ดาวทุกๆ รอบ รวมทั้งหมด 5 x 5 = 25 ครั้ง (O(N²))`,
              line: 5,
              litI: i, litJ: j,
              vars: { n: 5, i: i, j: j, print_count: count, time_complexity: 'O(N²)' }
            });
          }
        }
      } else if (mode === 'indent_fixed_outside') {
        this.qa = {
          question: 'หากแก้ Indentation ให้คำสั่ง print("*") ถอยออกมาอยู่นอกลูป j จะพิมพ์ดาวกี่ดวงเมื่อ n=5? ความซับซ้อน Big-O คือเท่าใด?',
          answer: '<strong>จำนวนดาวที่พิมพ์:</strong> <strong>5 ดวง</strong> เท่านั้น (พิมพ์เพียงรอบละ 1 ดวงตอนจบลูป j แต่ละแถว)<br><strong>ความซับซ้อน Time Complexity:</strong> <code>O(N)</code>',
          danger: '<strong>ข้อสังเกต:</strong> การเปลี่ยน Indentation เพียง 4 เคาะ สามารถเปลี่ยนความเร็วของโปรแกรมจาก O(N²) เป็น O(N) ได้ทันที'
        };
        this.codeLines = [
          '# Case B: print("*") เยื้องออกมานอกลูป j (ที่ถูกต้อง)',
          'def function_fixed(n=5):',
          '    for i in range(n):',
          '        for j in range(n):',
          '            pass',
          '        print("*")      # รันเพียง n = 5 ครั้ง! O(n)'
        ];
        this.steps = [];
        for (let i = 0; i < 5; i++) {
          this.steps.push({
            title: `จบรอบลูป i = ${i} (พิมพ์ดาว 1 ดวง)`,
            explanation: `print("*") เยื้องอยู่นอกลูป j ทำให้พิมพ์ดาวเพียงรอบละ 1 ดวง รวมทั้งสิ้น 5 ครั้ง (O(N))`,
            line: 6,
            litI: i, litJ: -1,
            vars: { n: 5, i: i, print_count: i + 1, time_complexity: 'O(N)' }
          });
        }
      } else if (mode === 'nested_matrix') {
        this.qa = {
          question: 'Nested Loop สามเหลี่ยม j = range(i, n) มีจำนวนรอบการทำงานทั้งหมดกี่รอบ?',
          answer: '<strong>สูตรจำนวนรอบ:</strong> N(N+1)/2 = 5(6)/2 = <strong>15 รอบ</strong> (5 + 4 + 3 + 2 + 1)<br><strong>ความซับซ้อน:</strong> ยังคงเป็น <code>O(N²)</code>',
          danger: '<strong>ข้อควรจำ:</strong> แม้จำนวนรอบจะลดลงครึ่งหนึ่ง แต่ในทาง Big-O ค่าสัมประสิทธิ์ 1/2 จะถูกตัดทิ้ง คงเหลือ O(N²)'
        };
        this.codeLines = [
          'def triangle_loop(n=5):',
          '    for i in range(n):',
          '        for j in range(i, n):',
          '            count += 1  # n(n+1)/2 = 15 รอบ'
        ];
        this.steps = [
          {
            title: 'Nested Loop สามเหลี่ยม j = range(i, n)',
            explanation: 'จำนวนรอบทั้งหมดคือ 5 + 4 + 3 + 2 + 1 = 15 รอบ (ยังคงเป็น O(N²))',
            line: 4,
            litI: 2, litJ: 3,
            vars: { formula: 'N(N+1)/2', total_rounds: 15, complexity: 'O(N²)' }
          }
        ];
      }

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
      if (playBtn) playBtn.innerHTML = '⏸️ หยุด (Pause)';
      this.timer = setInterval(() => {
        if (this.currentStep < this.steps.length - 1) {
          this.stepNext();
        } else {
          this.pause();
        }
      }, 500);
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

    reset() {
      this.pause();
      this.currentStep = 0;
      this.render();
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
      if (canvasEl) {
        let gridHtml = '<div class="studio-matrix-grid">';
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 5; c++) {
            let cls = 'studio-matrix-cell';
            if (this.mode === 'indent_bug_inside') {
              if (r < step.litI || (r === step.litI && c <= step.litJ)) cls += ' cell-done';
              if (r === step.litI && c === step.litJ) cls += ' cell-lit';
            } else if (this.mode === 'indent_fixed_outside') {
              if (r <= step.litI && c === 4) cls += ' cell-done';
            }
            gridHtml += `<div class="${cls}">*</div>`;
          }
        }
        gridHtml += '</div>';
        canvasEl.innerHTML = gridHtml;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
      renderQaPanel(container, this.qa);
    }
  }

  // =========================================================================
  // HTML BUILDER FOR EMBEDDED WIKI STUDIO WIDGETS
  // =========================================================================
  function createStudioWidgetHtml(type, widgetId) {
    let title = '';
    let badge = '';
    let controlsHtml = '';

    if (type === 'assign1-swap') {
      title = '🔗 Assignment 1 & Ch3: Singly Linked List Pointer Swap Studio';
      badge = 'Assign 1 / Lecture 3';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign1_p1')">🎓 สลับโหนด 1 และ 3 (รหัส 612037)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign1_p2')">📖 สลับโหนด 4 และ 2 (Lecture 3)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign1_p3')">⚠️ กับดัก add() (ผลลัพธ์กลับด้าน)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'assign2-tree') {
      title = '🌲 Assignment 2 & Ch5: Tree Traversal Reconstruction & Strict Path Studio';
      badge = 'Assign 2 / Lecture 5';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign2_m1')">🌲 Post-order + In-order (Assign 2)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign2_m2')">🌿 Pre-order + In-order (Lecture 5)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign2_m3')">🎯 กฎลูกน้ำเคร่งครัด (Strict Comma Rule)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'assign3-heap') {
      title = '⚡ Assignment 3 & Ch7: Min-Heap Hole Variable & Array Mapping Studio';
      badge = 'Assign 3 / Lecture 7';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign3_p1')">➕ แทรก 14 (ไล่ Hole: 11 → 5 → 2)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign3_p2')">🗑️ deleteMin() (Percolate Down)</button>
            <button class="studio-btn warning" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign3_p4')">🎯 ข้อสอบปลายภาค: deleteMin 3 ครั้งรวด (10 คะแนน)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign3_p3')">📦 ชุดข้อมูล 15 ค่า (Assignment 3)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'assign4-graph') {
      title = '🕸️ Assignment 4 & Ch9: Graph BFS Shortest Path & Memory Optimization Studio';
      badge = 'Assign 4 / Lecture 9';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign4_p1')">🚀 BFS Shortest Path จาก V1 (7-Vertex)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign4_p2')">💾 พิสูจน์ RAM สูญเปล่า 75.69%</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'assign4_p3')">🔢 Indegree (Topological Sort)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      `;
    } else if (type === 'test-suite') {
      title = '🏛️ Test Program 1 & 2: Queue Over/Underflow & Sorting Move Tracing Studio';
      badge = 'Test 1 & 2 / Practical Exam';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'test_queue_over')">🚨 Queue(5) Overflow</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'test_queue_under')">🚨 Queue(6) Underflow</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'test_modulo')">🔄 Circular Modulo</button>
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'test_sort_moves')">📊 Insertion Sort (นับ 9 Moves)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'test_selection')">🔍 Selection Sort</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'test_bubble')">🫧 Bubble Sort</button>
          </div>
        </div>
      `;
    } else if (type === 'bigo-indent') {
      title = '⚡ 0Exercises & Ch1: Python Indentation Traps & Big-O Loop Stepper';
      badge = '0Exercises / Lecture 1';
      controlsHtml = `
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('${widgetId}', 'bigo_bug')">❌ Bug: print("*") ใน Loop (O(N²) = 25 ครั้ง)</button>
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('${widgetId}', 'bigo_fixed')">✅ Fixed: print("*") นอก Loop (O(N) = 5 ครั้ง)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('${widgetId}', 'bigo_matrix')">🧮 Nested Loop Triangle Matrix</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'reset')">🔄 รีเซ็ต</button>
        </div>
      `;
    } else if (type === 'linked-list') {
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

        <!-- Official Exam Q&A Solution Panel -->
        <div class="studio-qa-solution-panel">
          <div class="qa-header">
            <span class="qa-icon">🎯</span>
            <span class="qa-title">โจทย์คำถามและเฉลยคำตอบสำหรับส่งอาจารย์ (Official Exam Q&A Solution)</span>
            <span class="qa-badge">คำตอบฉบับสมบูรณ์</span>
          </div>
          <div class="qa-content">
            <div class="qa-question-box">
              <div class="qa-lbl">📌 คำถามในห้องเรียน / ข้อสอบ:</div>
              <div class="qa-text qa-question-text">พร้อมตอบคำถาม...</div>
            </div>
            <div class="qa-answer-box">
              <div class="qa-lbl">🏆 เฉลยคำตอบที่ถูกต้อง (Official Final Answer):</div>
              <div class="qa-text qa-answer-text">พร้อมแสดงเฉลย...</div>
            </div>
            <div class="qa-danger-box">
              <div class="qa-lbl">⚠️ จุดที่ต้องระวัง (Zero-Point Danger / Trap):</div>
              <div class="qa-text qa-danger-text">จุดที่อาจารย์หักคะแนน...</div>
            </div>
          </div>
        </div>

        <!-- Dual Code & Variable Debugger Deck -->
        <div class="studio-debugger-deck">
          <!-- Left Panel: Stepper, Status & Live Variables -->
          <div class="debugger-status-panel">
            <div class="studio-step-header">
              <div class="studio-step-title">คำอธิบายขั้นตอน</div>
              <div class="active-code-line-badge">▶ Line <span class="active-code-line-num">-</span></div>
            </div>
            <div class="studio-stepper-controls">
              <button id="${widgetId}-prev" class="studio-stepper-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'prev')" title="ย้อนกลับ">⏮️ ย้อนสเต็ป</button>
              <button id="${widgetId}-play" class="studio-stepper-btn play" onclick="window.DsaWikiStudio.act('${widgetId}', 'play')" title="เล่นอัตโนมัติ">▶ เล่น (Play)</button>
              <button id="${widgetId}-next" class="studio-stepper-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'next')" title="สเต็ปถัดไป">⏭️ สเต็ปถัดไป</button>
            </div>
            <div class="studio-step-exp">พร้อมจำลองการทำงาน...</div>

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
    } else if (docId.startsWith('12.1')) {
      const widgetId = 'studio-widget-assign1';
      mountWidgetAt(articleBody, 'assign1-swap', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign1PointerSwapSimulator(widgetId, 'assign1');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.2')) {
      const widgetId = 'studio-widget-assign2';
      mountWidgetAt(articleBody, 'assign2-tree', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign2TreeReconstructSimulator(widgetId, 'post_in');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.3')) {
      const widgetId = 'studio-widget-assign3';
      mountWidgetAt(articleBody, 'assign3-heap', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign3HeapSimulator(widgetId, 'insert14');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.4')) {
      const widgetId = 'studio-widget-assign4';
      mountWidgetAt(articleBody, 'assign4-graph', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign4GraphSimulator(widgetId, 'bfs');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.5')) {
      const widgetId = 'studio-widget-test-suite';
      mountWidgetAt(articleBody, 'test-suite', widgetId, '## 📌');
      widgetInstances[widgetId] = new TestProgramSuiteSimulator(widgetId, 'insertion_moves');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.6')) {
      const widgetId = 'studio-widget-bigo-indent';
      mountWidgetAt(articleBody, 'bigo-indent', widgetId, '## 📌');
      widgetInstances[widgetId] = new BigOExercisesSimulator(widgetId, 'indent_bug_inside');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.1')) {
      const widgetId = 'studio-widget-assign1';
      mountWidgetAt(articleBody, 'assign1-swap', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign1PointerSwapSimulator(widgetId, 'lec3');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.2')) {
      const widgetId = 'studio-widget-stack';
      mountWidgetAt(articleBody, 'stack-infix', widgetId, '## 📌');
      widgetInstances[widgetId] = new StackInfixSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.3')) {
      const widgetId = 'studio-widget-test-suite';
      mountWidgetAt(articleBody, 'test-suite', widgetId, '## 📌');
      widgetInstances[widgetId] = new TestProgramSuiteSimulator(widgetId, 'circular_modulo');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.4')) {
      const widgetId = 'studio-widget-assign2';
      mountWidgetAt(articleBody, 'assign2-tree', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign2TreeReconstructSimulator(widgetId, 'strict_path');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.5')) {
      const widgetId = 'studio-widget-bst';
      mountWidgetAt(articleBody, 'bst', widgetId, '## 📌');
      widgetInstances[widgetId] = new BstSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.6')) {
      const widgetId = 'studio-widget-assign3';
      mountWidgetAt(articleBody, 'assign3-heap', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign3HeapSimulator(widgetId, 'insert14');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.7')) {
      const widgetId = 'studio-widget-test-suite';
      mountWidgetAt(articleBody, 'test-suite', widgetId, '## 📌');
      widgetInstances[widgetId] = new TestProgramSuiteSimulator(widgetId, 'insertion_moves');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.8')) {
      const widgetId = 'studio-widget-assign4';
      mountWidgetAt(articleBody, 'assign4-graph', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign4GraphSimulator(widgetId, 'bfs');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('11.7')) {
      const widgetIdHash = 'studio-widget-hash-11-7';
      mountWidgetAt(articleBody, 'hash', widgetIdHash, '## 🔑 ข้อสอบข้อที่ 1');
      widgetInstances[widgetIdHash] = new HashSimulator(widgetIdHash);
      widgetInstances[widgetIdHash].render();

      const widgetIdHeap = 'studio-widget-heap-11-7';
      mountWidgetAt(articleBody, 'assign3-heap', widgetIdHeap, '## ⚡ ข้อสอบข้อที่ 3');
      widgetInstances[widgetIdHeap] = new Assign3HeapSimulator(widgetIdHeap, 'deleteMin3');
      widgetInstances[widgetIdHeap].render();
    } else if (docId.startsWith('14.1')) {
      const widgetId = 'studio-widget-hash-14-1';
      mountWidgetAt(articleBody, 'hash', widgetId, '## 🎮');
      widgetInstances[widgetId] = new HashSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('14.2')) {
      const widgetId = 'studio-widget-heap-14-2';
      mountWidgetAt(articleBody, 'heap', widgetId, '## 🎮');
      widgetInstances[widgetId] = new HeapSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('14.3')) {
      const widgetId = 'studio-widget-heap-14-3';
      mountWidgetAt(articleBody, 'heap', widgetId, '## 🏛️ 1');
      widgetInstances[widgetId] = new HeapSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('14.4')) {
      const widgetId = 'studio-widget-heap-14-4';
      mountWidgetAt(articleBody, 'assign3-heap', widgetId, '## 🎮');
      widgetInstances[widgetId] = new Assign3HeapSimulator(widgetId, 'deleteMin3');
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
    
    else if (action === 'assign1_p1' && inst.loadPreset) inst.loadPreset('assign1');
    else if (action === 'assign1_p2' && inst.loadPreset) inst.loadPreset('lec3');
    else if (action === 'assign1_p3' && inst.loadPreset) inst.loadPreset('add_trap');
    else if (action === 'assign2_m1' && inst.loadMode) inst.loadMode('post_in');
    else if (action === 'assign2_m2' && inst.loadMode) inst.loadMode('pre_in');
    else if (action === 'assign2_m3' && inst.loadMode) inst.loadMode('strict_path');
    else if (action === 'assign3_p1' && inst.loadPreset) inst.loadPreset('insert14');
    else if (action === 'assign3_p2' && inst.loadPreset) inst.loadPreset('deleteMin');
    else if (action === 'assign3_p4' && inst.loadPreset) inst.loadPreset('deleteMin3');
    else if (action === 'assign3_p3' && inst.loadPreset) inst.loadPreset('assign3_15');
    else if (action === 'assign4_p1' && inst.loadPreset) inst.loadPreset('bfs');
    else if (action === 'assign4_p2' && inst.loadPreset) inst.loadPreset('ram_waste');
    else if (action === 'assign4_p3' && inst.loadPreset) inst.loadPreset('topological');
    else if (action === 'test_queue_over' && inst.loadMode) inst.loadMode('queue_overflow');
    else if (action === 'test_queue_under' && inst.loadMode) inst.loadMode('queue_underflow');
    else if (action === 'test_modulo' && inst.loadMode) inst.loadMode('circular_modulo');
    else if (action === 'test_sort_moves' && inst.loadMode) inst.loadMode('insertion_moves');
    else if (action === 'test_selection' && inst.loadMode) inst.loadMode('selection_sort');
    else if (action === 'test_bubble' && inst.loadMode) inst.loadMode('bubble_sort');
    else if (action === 'bigo_bug' && inst.loadMode) inst.loadMode('indent_bug_inside');
    else if (action === 'bigo_fixed' && inst.loadMode) inst.loadMode('indent_fixed_outside');
    else if (action === 'bigo_matrix' && inst.loadMode) inst.loadMode('nested_matrix');
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
