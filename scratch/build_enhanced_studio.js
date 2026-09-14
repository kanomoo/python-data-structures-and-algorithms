const fs = require('fs');
const path = require('path');

const targetFile = path.join(__dirname, '..', 'Wiki', 'dsa-interactive-studio.js');
let content = fs.readFileSync(targetFile, 'utf8').replace(/\r\n/g, '\n');

// The new simulators code to be inserted before createStudioWidgetHtml
const newSimulatorsCode = `
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      if (counterEl) counterEl.textContent = \`สเต็ป \${this.currentStep + 1} / \${this.steps.length}\`;
      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;
      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(\`\${this.containerId}-prev\`);
      const nextBtn = document.getElementById(\`\${this.containerId}-next\`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += \`<tr><td class="watch-k">\${k}</td><td class="watch-v">\${v}</td></tr>\`;
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
          let svgHtml = \`<svg width="100%" height="\${svgH}" viewBox="0 0 \${svgW} \${svgH}">\`;

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

            svgHtml += \`
              <g>
                <text x="\${x + 35}" y="\${y - 12}" fill="\${stroke}" font-size="10" font-weight="700" font-family="JetBrains Mono" text-anchor="middle">\${badge ? '▼ ' + badge : n.addr}</text>
                <rect x="\${x}" y="\${y}" width="42" height="42" rx="6" fill="\${fill}" stroke="\${stroke}" stroke-width="2" />
                <text x="\${x + 21}" y="\${y + 26}" fill="#fff" font-size="16" font-weight="800" font-family="Chakra Petch" text-anchor="middle">\${n.val}</text>
                <rect x="\${x + 42}" y="\${y}" width="28" height="42" rx="0 6 6 0" fill="#0f172a" stroke="\${stroke}" stroke-width="2" />
                <circle cx="\${x + 56}" cy="\${y + 21}" r="4" fill="\${stroke}" />
              </g>
            \`;

            if (idx < nodes.length - 1) {
              const arrowX = x + 70;
              const targetX = startX + (idx + 1) * spacing;
              svgHtml += \`
                <line x1="\${arrowX}" y1="\${y + 21}" x2="\${targetX}" y2="\${y + 21}" stroke="\${stroke}" stroke-width="2" />
                <polygon points="\${targetX},\${y + 21} \${targetX - 7},\${y + 16} \${targetX - 7},\${y + 26}" fill="\${stroke}" />
              \`;
            } else {
              svgHtml += \`
                <line x1="\${x + 70}" y1="\${y + 21}" x2="\${x + 95}" y2="\${y + 21}" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3" />
                <text x="\${x + 105}" y="\${y + 25}" fill="#ef4444" font-size="11" font-family="JetBrains Mono" font-weight="700">None</text>
              \`;
            }
          });

          svgHtml += '</svg>';
          canvasEl.innerHTML = svgHtml;
        }
      }

      renderCodeDebugger(container, this.codeLines, step.line);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      if (counterEl) counterEl.textContent = \`สเต็ป \${this.currentStep + 1} / \${this.steps.length}\`;
      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;
      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(\`\${this.containerId}-prev\`);
      const nextBtn = document.getElementById(\`\${this.containerId}-next\`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += \`<tr><td class="watch-k">\${k}</td><td class="watch-v">\${v}</td></tr>\`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (canvasEl) {
        let html = '';
        if (step.isPathAlert) {
          html += \`
            <div class="studio-path-alert">
              <span class="studio-path-badge danger">⚠️ STRICT WARNING</span>
              <span><strong>ข้อควรระวังในห้องสอบ:</strong> ห้ามใส่ลูกศรเด็ดขาด! คำตอบต้องเป็น <code>A, B, E</code> เท่านั้น (ห้ามเขียน <code>A -&gt; B -&gt; E</code>)</span>
            </div>
          \`;
        }

        const svgW = 600;
        const svgH = 170;
        let svgHtml = \`<svg width="100%" height="\${svgH}" viewBox="0 0 \${svgW} \${svgH}">\`;

        if (step.tree) {
          const coords = {
            A: { x: 300, y: 30 },
            B: { x: 180, y: 85 },
            C: { x: 420, y: 85 },
            D: { x: 120, y: 140 },
            E: { x: 240, y: 140 },
            F: { x: 360, y: 140 },
            G: { x: 480, y: 140 }
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
                svgHtml += \`<line x1="\${pPos.x}" y1="\${pPos.y}" x2="\${cPos.x}" y2="\${cPos.y}" stroke="\${stroke}" stroke-width="\${w}" />\`;
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

            svgHtml += \`
              <g>
                <circle cx="\${pos.x}" cy="\${pos.y}" r="16" fill="\${fill}" stroke="\${stroke}" stroke-width="2.2" />
                <text x="\${pos.x}" y="\${pos.y + 5}" fill="\${txtColor}" font-weight="800" font-size="13" font-family="Chakra Petch" text-anchor="middle">\${key}</text>
              </g>
            \`;
          });
        }
        svgHtml += '</svg>';
        html += svgHtml;

        if (step.showArray) {
          html += \`
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
          \`;
        }

        canvasEl.innerHTML = html;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      if (counterEl) counterEl.textContent = \`สเต็ป \${this.currentStep + 1} / \${this.steps.length}\`;
      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;
      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(\`\${this.containerId}-prev\`);
      const nextBtn = document.getElementById(\`\${this.containerId}-next\`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += \`<tr><td class="watch-k">\${k}</td><td class="watch-v">\${v}</td></tr>\`;
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
            slotsHtml += \`<div class="\${cls}"><span class="slot-idx">[\${idx}]</span><span class="slot-val">\${displayVal}</span></div>\`;
          }
        });
        slotsHtml += '</div>';

        // Render Compact Tree Representation
        const svgW = 600;
        const svgH = 150;
        let svgHtml = \`<svg width="100%" height="\${svgH}" viewBox="0 0 \${svgW} \${svgH}">\`;
        const treeCoords = [
          null,
          { x: 300, y: 24 },
          { x: 180, y: 65 }, { x: 420, y: 65 },
          { x: 110, y: 110 }, { x: 230, y: 110 }, { x: 350, y: 110 }, { x: 470, y: 110 },
          { x: 70, y: 140 }, { x: 130, y: 140 }, { x: 190, y: 140 }, { x: 250, y: 140 }
        ];

        for (let i = 1; i <= Math.min(arr.length - 1, 11); i++) {
          const pIdx = Math.floor(i / 2);
          if (pIdx >= 1 && treeCoords[pIdx] && treeCoords[i]) {
            svgHtml += \`<line x1="\${treeCoords[pIdx].x}" y1="\${treeCoords[pIdx].y}" x2="\${treeCoords[i].x}" y2="\${treeCoords[i].y}" stroke="rgba(255,255,255,0.18)" stroke-width="1.8" />\`;
          }
        }

        for (let i = 1; i <= Math.min(arr.length - 1, 11); i++) {
          const pos = treeCoords[i];
          if (!pos) continue;
          const isHole = i === step.hole || arr[i] === 'HOLE';
          const fill = isHole ? 'rgba(245, 158, 11, 0.25)' : '#1e293b';
          const stroke = isHole ? '#f59e0b' : '#6366f1';
          const txt = isHole ? '?' : arr[i];
          svgHtml += \`
            <g>
              <circle cx="\${pos.x}" cy="\${pos.y}" r="14" fill="\${fill}" stroke="\${stroke}" stroke-width="2" />
              <text x="\${pos.x}" y="\${pos.y + 4}" fill="#fff" font-size="11" font-weight="700" font-family="Chakra Petch" text-anchor="middle">\${txt}</text>
              <text x="\${pos.x}" y="\${pos.y - 16}" fill="var(--text-muted)" font-size="9" font-family="JetBrains Mono" text-anchor="middle">[\${i}]</text>
            </g>
          \`;
        }
        svgHtml += '</svg>';

        canvasEl.innerHTML = svgHtml + slotsHtml;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      if (counterEl) counterEl.textContent = \`สเต็ป \${this.currentStep + 1} / \${this.steps.length}\`;
      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;
      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(\`\${this.containerId}-prev\`);
      const nextBtn = document.getElementById(\`\${this.containerId}-next\`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += \`<tr><td class="watch-k">\${k}</td><td class="watch-v">\${v}</td></tr>\`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (canvasEl) {
        const svgW = 600;
        const svgH = 180;
        const vPos = {
          V1: { x: 70, y: 90 },
          V2: { x: 200, y: 40 },
          V3: { x: 200, y: 140 },
          V4: { x: 330, y: 90 },
          V5: { x: 440, y: 40 },
          V6: { x: 530, y: 140 },
          V7: { x: 440, y: 140 }
        };

        const edges = [
          ['V1', 'V2'], ['V1', 'V4'],
          ['V2', 'V4'], ['V2', 'V5'],
          ['V3', 'V1'], ['V3', 'V6'],
          ['V4', 'V3'], ['V4', 'V5'], ['V4', 'V6'], ['V4', 'V7'],
          ['V5', 'V7'],
          ['V7', 'V6']
        ];

        let svgHtml = \`<svg width="100%" height="\${svgH}" viewBox="0 0 \${svgW} \${svgH}">\`;
        edges.forEach(([u, v]) => {
          const p1 = vPos[u], p2 = vPos[v];
          svgHtml += \`<line x1="\${p1.x}" y1="\${p1.y}" x2="\${p2.x}" y2="\${p2.y}" stroke="rgba(255,255,255,0.2)" stroke-width="1.6" />\`;
        });

        Object.keys(vPos).forEach(k => {
          const p = vPos[k];
          const info = (step.table && step.table[k]) || {};
          const isActive = step.activeV === k;
          let fill = '#1e293b';
          let stroke = '#6366f1';
          if (isActive) { fill = 'rgba(245, 158, 11, 0.3)'; stroke = '#f59e0b'; }
          else if (info.known) { fill = 'rgba(16, 185, 129, 0.2)'; stroke = '#10b981'; }

          svgHtml += \`
            <g>
              <circle cx="\${p.x}" cy="\${p.y}" r="17" fill="\${fill}" stroke="\${stroke}" stroke-width="2" />
              <text x="\${p.x}" y="\${p.y + 4}" fill="#fff" font-size="11" font-weight="800" font-family="Chakra Petch" text-anchor="middle">\${k}</text>
              <text x="\${p.x}" y="\${p.y - 20}" fill="var(--cyan)" font-size="9" font-family="JetBrains Mono" text-anchor="middle">d=\${info.dist !== undefined ? info.dist : '?'}</text>
            </g>
          \`;
        });
        svgHtml += '</svg>';

        let extraHtml = '';
        if (step.table && Object.keys(step.table).length > 0) {
          extraHtml += \`
            <table class="studio-bfs-table">
              <thead>
                <tr><th>Vertex</th><th>Known</th><th>$d_v$ (Dist)</th><th>$p_v$ (Path)</th></tr>
              </thead>
              <tbody>
          \`;
          Object.keys(step.table).forEach(vKey => {
            const row = step.table[vKey];
            const isKnown = row.known;
            extraHtml += \`
              <tr class="\${step.activeV === vKey ? 'is-active-row' : ''}">
                <td>\${vKey}</td>
                <td class="\${isKnown ? 'known-true' : 'known-false'}">\${isKnown ? 'True (T)' : 'False (F)'}</td>
                <td>\${row.dist}</td>
                <td>\${row.path || '0'}</td>
              </tr>
            \`;
          });
          extraHtml += '</tbody></table>';
        }

        canvasEl.innerHTML = svgHtml + extraHtml;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      if (counterEl) counterEl.textContent = \`สเต็ป \${this.currentStep + 1} / \${this.steps.length}\`;
      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;
      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(\`\${this.containerId}-prev\`);
      const nextBtn = document.getElementById(\`\${this.containerId}-next\`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += \`<tr><td class="watch-k">\${k}</td><td class="watch-v">\${v}</td></tr>\`;
        });
        watchTbody.innerHTML = rows;
      }

      const canvasEl = container.querySelector('.studio-canvas-area');
      if (canvasEl) {
        let html = '';
        if (step.isException) {
          html += \`
            <div class="studio-path-alert" style="background:rgba(239, 68, 68, 0.25);border-color:#ef4444;">
              <span class="studio-path-badge danger">🚨 EXCEPTION RAISED</span>
              <span><strong>เกิดข้อผิดพลาด:</strong> \${step.vars['🚨 Exception']} — "\${step.vars.message}"</span>
            </div>
          \`;
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

            html += \`
              <div class="\${cls}">
                \${isF ? '<span class="q-tag front-tag">FRONT</span>' : ''}
                \${isR ? '<span class="q-tag rear-tag">REAR</span>' : ''}
                <span class="q-val">\${val !== null ? val : '·'}</span>
                <span class="q-idx">[\${idx}]</span>
              </div>
            \`;
          });
          html += '</div>';
        } else if (step.arr) {
          const maxVal = Math.max(...step.arr, 1);
          html += '<div class="studio-sort-bars">';
          step.arr.forEach((val, idx) => {
            const heightPct = Math.round((val / maxVal) * 100);
            html += \`
              <div class="sort-bar-col">
                <div class="sort-bar is-sorted" style="height: \${Math.max(20, heightPct)}%;">
                  <span class="bar-val">\${val}</span>
                </div>
                <span class="bar-idx">[\${idx}]</span>
              </div>
            \`;
          });
          html += '</div>';
          if (step.moves !== undefined) {
            html += \`
              <div style="text-align:center;margin-top:10px;font-family:var(--font-mono);font-size:13px;color:#a5b4fc;">
                Position Moves สะสม: <strong style="color:#f59e0b;font-size:18px;">\${step.moves}</strong> Moves
              </div>
            \`;
          }
        }

        canvasEl.innerHTML = html;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
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
              title: \`รอบที่ \${count}: i = \${i}, j = \${j} (รันคำสั่ง print)\`,
              explanation: \`print("*") อยู่ในลูปในสุด (j) ทำให้พิมพ์ดาวทุกๆ รอบ รวมทั้งหมด 5 x 5 = 25 ครั้ง (O(N²))\`,
              line: 5,
              litI: i, litJ: j,
              vars: { n: 5, i: i, j: j, print_count: count, time_complexity: 'O(N²)' }
            });
          }
        }
      } else if (mode === 'indent_fixed_outside') {
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
            title: \`จบรอบลูป i = \${i} (พิมพ์ดาว 1 ดวง)\`,
            explanation: \`print("*") เยื้องอยู่นอกลูป j ทำให้พิมพ์ดาวเพียงรอบละ 1 ดวง รวมทั้งสิ้น 5 ครั้ง (O(N))\`,
            line: 6,
            litI: i, litJ: -1,
            vars: { n: 5, i: i, print_count: i + 1, time_complexity: 'O(N)' }
          });
        }
      } else if (mode === 'nested_matrix') {
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      const playBtn = document.getElementById(\`\${this.containerId}-play\`);
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
      if (counterEl) counterEl.textContent = \`สเต็ป \${this.currentStep + 1} / \${this.steps.length}\`;
      const titleEl = container.querySelector('.studio-step-title');
      if (titleEl) titleEl.textContent = step.title;
      const expEl = container.querySelector('.studio-step-exp');
      if (expEl) expEl.textContent = step.explanation;

      const prevBtn = document.getElementById(\`\${this.containerId}-prev\`);
      const nextBtn = document.getElementById(\`\${this.containerId}-next\`);
      if (prevBtn) prevBtn.disabled = this.currentStep === 0;
      if (nextBtn) nextBtn.disabled = this.currentStep === this.steps.length - 1;

      const watchTbody = container.querySelector('.studio-watch-tbody');
      if (watchTbody) {
        let rows = '';
        Object.entries(step.vars || {}).forEach(([k, v]) => {
          rows += \`<tr><td class="watch-k">\${k}</td><td class="watch-v">\${v}</td></tr>\`;
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
            gridHtml += \`<div class="\${cls}">*</div>\`;
          }
        }
        gridHtml += '</div>';
        canvasEl.innerHTML = gridHtml;
      }

      renderCodeDebugger(container, this.codeLines, step.line);
    }
  }
`;

// Now find where createStudioWidgetHtml starts
const createWidgetMarker = '// =========================================================================\n  // HTML BUILDER FOR EMBEDDED WIKI STUDIO WIDGETS';
if (!content.includes(createWidgetMarker)) {
  console.error('Could not find createStudioWidgetHtml marker!');
  process.exit(1);
}

// Replace and insert simulator classes
content = content.replace(createWidgetMarker, newSimulatorsCode + '\n  ' + createWidgetMarker);

// Now update createStudioWidgetHtml to handle the new widget types
const oldCreateStudioWidgetStart = 'function createStudioWidgetHtml(type, widgetId) {';
const newCreateStudioWidgetAdditions = `function createStudioWidgetHtml(type, widgetId) {
    let title = '';
    let badge = '';
    let controlsHtml = '';

    if (type === 'assign1-swap') {
      title = '🔗 Assignment 1 & Ch3: Singly Linked List Pointer Swap Studio';
      badge = 'Assign 1 / Lecture 3';
      controlsHtml = \`
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign1_p1')">🎓 สลับโหนด 1 และ 3 (รหัส 612037)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign1_p2')">📖 สลับโหนด 4 และ 2 (Lecture 3)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign1_p3')">⚠️ กับดัก add() (ผลลัพธ์กลับด้าน)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      \`;
    } else if (type === 'assign2-tree') {
      title = '🌲 Assignment 2 & Ch5: Tree Traversal Reconstruction & Strict Path Studio';
      badge = 'Assign 2 / Lecture 5';
      controlsHtml = \`
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign2_m1')">🌲 Post-order + In-order (Assign 2)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign2_m2')">🌿 Pre-order + In-order (Lecture 5)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign2_m3')">🎯 กฎลูกน้ำเคร่งครัด (Strict Comma Rule)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      \`;
    } else if (type === 'assign3-heap') {
      title = '⚡ Assignment 3 & Ch7: Min-Heap Hole Variable & Array Mapping Studio';
      badge = 'Assign 3 / Lecture 7';
      controlsHtml = \`
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign3_p1')">➕ แทรก 14 (ไล่ Hole: 11 → 5 → 2)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign3_p2')">🗑️ deleteMin() (Percolate Down)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign3_p3')">📦 ชุดข้อมูล 15 ค่า (Assignment 3)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      \`;
    } else if (type === 'assign4-graph') {
      title = '🕸️ Assignment 4 & Ch9: Graph BFS Shortest Path & Memory Optimization Studio';
      badge = 'Assign 4 / Lecture 9';
      controlsHtml = \`
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign4_p1')">🚀 BFS Shortest Path จาก V1 (7-Vertex)</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign4_p2')">💾 พิสูจน์ RAM สูญเปล่า 75.69%</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('\${widgetId}', 'assign4_p3')">🔢 Indegree (Topological Sort)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      \`;
    } else if (type === 'test-suite') {
      title = '🏛️ Test Program 1 & 2: Queue Over/Underflow & Sorting Move Tracing Studio';
      badge = 'Test 1 & 2 / Practical Exam';
      controlsHtml = \`
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'test_queue_over')">🚨 Queue(5) Overflow</button>
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'test_queue_under')">🚨 Queue(6) Underflow</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('\${widgetId}', 'test_modulo')">🔄 Circular Modulo</button>
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('\${widgetId}', 'test_sort_moves')">📊 Insertion Sort (นับ 9 Moves)</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'test_selection')">🔍 Selection Sort</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'test_bubble')">🫧 Bubble Sort</button>
          </div>
        </div>
      \`;
    } else if (type === 'bigo-indent') {
      title = '⚡ 0Exercises & Ch1: Python Indentation Traps & Big-O Loop Stepper';
      badge = '0Exercises / Lecture 1';
      controlsHtml = \`
        <div class="studio-control-row">
          <div class="studio-btn-group">
            <button class="studio-btn danger" onclick="window.DsaWikiStudio.act('\${widgetId}', 'bigo_bug')">❌ Bug: print("*") ใน Loop (O(N²) = 25 ครั้ง)</button>
            <button class="studio-btn primary" onclick="window.DsaWikiStudio.act('\${widgetId}', 'bigo_fixed')">✅ Fixed: print("*") นอก Loop (O(N) = 5 ครั้ง)</button>
            <button class="studio-btn info" onclick="window.DsaWikiStudio.act('\${widgetId}', 'bigo_matrix')">🧮 Nested Loop Triangle Matrix</button>
            <button class="studio-btn" onclick="window.DsaWikiStudio.act('\${widgetId}', 'reset')">🔄 รีเซ็ต</button>
          </div>
        </div>
      \`;
    } else `;

content = content.replace(oldCreateStudioWidgetStart, newCreateStudioWidgetAdditions);

// Update mountWidgetsForDoc to mount all assignments (12.1-12.6) and classroom examples (13.1-13.8)
const oldMountEnd = `    } else if (docId.startsWith('08.1')) {
      const widgetId = 'studio-widget-sort';
      mountWidgetAt(articleBody, 'sort', widgetId, '## 🏛️ 1. สรุปความเร็ว');
      widgetInstances[widgetId] = new SortSimulator(widgetId);
      widgetInstances[widgetId].render();
    }
  }`;

const newMountEnd = `    } else if (docId.startsWith('08.1')) {
      const widgetId = 'studio-widget-sort';
      mountWidgetAt(articleBody, 'sort', widgetId, '## 🏛️ 1. สรุปความเร็ว');
      widgetInstances[widgetId] = new SortSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.1') || docId.startsWith('13.1')) {
      const widgetId = 'studio-widget-assign1';
      mountWidgetAt(articleBody, 'assign1-swap', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign1PointerSwapSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.2') || docId.startsWith('13.3')) {
      const widgetId = 'studio-widget-assign2';
      mountWidgetAt(articleBody, 'assign2-tree', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign2TreeReconstructSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.3') || docId.startsWith('13.5')) {
      const widgetId = 'studio-widget-assign3';
      mountWidgetAt(articleBody, 'assign3-heap', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign3HeapSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.4') || docId.startsWith('13.7')) {
      const widgetId = 'studio-widget-assign4';
      mountWidgetAt(articleBody, 'assign4-graph', widgetId, '## 📌');
      widgetInstances[widgetId] = new Assign4GraphSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.5')) {
      const widgetId = 'studio-widget-test-suite';
      mountWidgetAt(articleBody, 'test-suite', widgetId, '## 📌');
      widgetInstances[widgetId] = new TestProgramSuiteSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.2')) {
      const widgetId = 'studio-widget-test-suite';
      mountWidgetAt(articleBody, 'test-suite', widgetId, '## 📌');
      widgetInstances[widgetId] = new TestProgramSuiteSimulator(widgetId, 'circular_modulo');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.4')) {
      const widgetId = 'studio-widget-hash';
      mountWidgetAt(articleBody, 'hash', widgetId, '## 📌');
      widgetInstances[widgetId] = new HashSimulator(widgetId);
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('13.6')) {
      const widgetId = 'studio-widget-test-suite';
      mountWidgetAt(articleBody, 'test-suite', widgetId, '## 📌');
      widgetInstances[widgetId] = new TestProgramSuiteSimulator(widgetId, 'insertion_moves');
      widgetInstances[widgetId].render();
    } else if (docId.startsWith('12.6') || docId.startsWith('13.8')) {
      const widgetId = 'studio-widget-bigo-indent';
      mountWidgetAt(articleBody, 'bigo-indent', widgetId, '## 📌');
      widgetInstances[widgetId] = new BigOExercisesSimulator(widgetId);
      widgetInstances[widgetId].render();
    }
  }`;

content = content.replace(oldMountEnd, newMountEnd);

// Update act dispatcher to handle new actions
const oldActReset = "else if (action === 'reset' && inst.reset) inst.reset();";
const newActDispatches = `
    else if (action === 'assign1_p1' && inst.loadPreset) inst.loadPreset('assign1');
    else if (action === 'assign1_p2' && inst.loadPreset) inst.loadPreset('lec3');
    else if (action === 'assign1_p3' && inst.loadPreset) inst.loadPreset('add_trap');
    else if (action === 'assign2_m1' && inst.loadMode) inst.loadMode('post_in');
    else if (action === 'assign2_m2' && inst.loadMode) inst.loadMode('pre_in');
    else if (action === 'assign2_m3' && inst.loadMode) inst.loadMode('strict_path');
    else if (action === 'assign3_p1' && inst.loadPreset) inst.loadPreset('insert14');
    else if (action === 'assign3_p2' && inst.loadPreset) inst.loadPreset('deleteMin');
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
    else if (action === 'reset' && inst.reset) inst.reset();`;

content = content.replace(oldActReset, newActDispatches);

fs.writeFileSync(targetFile, content, 'utf8');
console.log('Successfully updated Wiki/dsa-interactive-studio.js');
