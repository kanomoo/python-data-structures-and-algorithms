import re

with open('Wiki/dsa-interactive-studio.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Locate where QueueSimulator ends
split_marker = '  // =========================================================================\n  // HTML BUILDER FOR EMBEDDED WIKI STUDIO WIDGETS'
parts = code.split(split_marker)

if len(parts) != 2:
    print('ERROR: Split marker not found!')
    exit(1)

base_simulators = parts[0]

new_simulators = '''
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
      const cleanExpr = this.expr.replace(/\\s+/g, '');
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
        vars: { table_size: this.tableSize, strategy: this.strategy, collisions: 0 }
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
          vars: { key: k, h1: initialHash, h2: h2Val }
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
              vars: { key: k, slot, probe_count: probe, total_collisions: collisionCount }
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
              vars: { key: k, collided_at: slot, occupied_by: this.table[slot].key, probe_step: probe + 1 }
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
    }
  }
'''

new_builder = '''
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

        <!-- Debugger Stepper & Explanation Card -->
        <div class="studio-debugger-bar">
          <div class="studio-exp-box">
            <div class="studio-step-title">คำอธิบายขั้นตอน</div>
            <div class="studio-step-exp">พร้อมจำลองการทำงาน...</div>
          </div>
          <div class="studio-stepper-controls">
            <button id="${widgetId}-prev" class="studio-stepper-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'prev')" title="ย้อนกลับ">⏮️ ย้อนสเต็ป</button>
            <button id="${widgetId}-play" class="studio-stepper-btn play" onclick="window.DsaWikiStudio.act('${widgetId}', 'play')" title="เล่นอัตโนมัติ">▶ เล่น (Play)</button>
            <button id="${widgetId}-next" class="studio-stepper-btn" onclick="window.DsaWikiStudio.act('${widgetId}', 'next')" title="สเต็ปถัดไป">⏭️ สเต็ปถัดไป</button>
          </div>
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
      if (!targetHeading && h.textContent.includes(headingSearch.replace(/^[#\\s]+/, '').slice(0, 6))) {
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
'''

full_code = base_simulators + new_simulators + new_builder

with open('Wiki/dsa-interactive-studio.js', 'w', encoding='utf-8') as f:
    f.write(full_code)

print('Successfully generated full Wiki/dsa-interactive-studio.js! Size:', len(full_code))
