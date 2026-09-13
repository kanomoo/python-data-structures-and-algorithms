# -*- coding: utf-8 -*-
"""
Generates scratch/perfect_engine.js containing the full buildNativeDsaVisual function
with all 48 dedicated high-fidelity DSA visual models.
"""
import sys, io, json

def generate_perfect_engine():
    # We will write the complete JS function
    js_code = r'''  // ==========================================================================
  // DSA Lab Studio Native Visual Architecture Engine (100% Zero Mermaid Dependency)
  // Maps all 48 textbook & exam diagrams to world-class pedagogical SVG/HTML models
  // ==========================================================================

  function getArchitectureTitle(code) {
    const lower = code.toLowerCase();
    if (lower.includes('knowledge map')) return '🗺️ DSA Curriculum Architecture & Master Knowledge Map';
    if (lower.includes('dijkstra') || lower.includes('shortest')) return '🗺️ Shortest Path & Dijkstra Algorithm Flow Architecture';
    if (lower.includes('topological')) return '🔀 Topological Sort & Dependency DAG Model';
    if (lower.includes('traversal') || lower.includes('bfs') || lower.includes('dfs')) return '🕸️ Graph Traversals (BFS vs DFS) Architecture';
    if (lower.includes('big-o') || lower.includes('growth') || lower.includes('asymptotic')) return '📈 Big-O & Complexity Hierarchy Model';
    if (lower.includes('adt') || lower.includes('abstract data type')) return '🏛️ Abstract Data Type (ADT) vs Data Structure Architecture';
    if (lower.includes('linked list') || lower.includes('singly') || lower.includes('doubly') || lower.includes('circular')) return '🔗 Linked List Pointer & Memory Model';
    if (lower.includes('heap') || lower.includes('priority queue')) return '⚡ Binary Heap Complete Tree Architecture';
    if (lower.includes('bst') || lower.includes('binary search tree')) return '🌲 Binary Search Tree (BST) Architecture';
    if (lower.includes('tree')) return '🌴 Tree Terminology & Structure Model';
    if (lower.includes('stack')) return '🥞 Stack ADT Memory Model: LIFO Canister';
    if (lower.includes('queue')) return '🚶 Queue FIFO Conveyor Architecture';
    if (lower.includes('hash') || lower.includes('collision')) return '🔑 Hash Table & Collision Architecture';
    if (lower.includes('sort')) return '🔀 Sorting Algorithm Workflow';
    if (lower.includes('trap')) return '🚨 Final Exam Traps & Core Insights';
    return '🔬 แบบจำลองโครงสร้างสถาปัตยกรรม (DSA Studio Architecture)';
  }

  function buildNativeDsaVisual(code, docId, inDocIdx) {
    const clean = code.trim();
    const lower = clean.toLowerCase();
    const dId = docId || '';

    // Standard Reusable SVG Defs
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
        <marker id="dsa-arrow-emerald" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M 0 1 L 7 4 L 0 7 z" fill="#10b981" />
        </marker>
      </defs>
    `;

    // =========================================================================
    // 1. MASTER DSA KNOWLEDGE MAP (Index)
    // =========================================================================
    if (dId === 'Index' || (inDocIdx === 1 && dId === 'Index') || (lower.includes('root["📚 data structures') && lower.includes('m1["01'))) {
      return {
        title: '🗺️ DSA Curriculum Architecture & Master Knowledge Map',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:16px;margin-bottom:16px;">
              <div class="dsa-card" style="border-left:4px solid #4fd1e8;background:#181a26;padding:16px;border-radius:10px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;margin-bottom:8px;">1. Linear Structures</div>
                <div style="font-size:13px;color:#c7cad6;line-height:1.6;">
                  • <b>Array & Dynamic Array</b>: O(1) Access, O(N) Insert<br/>
                  • <b>Singly & Doubly Linked List</b>: O(1) Head Op, O(N) Search<br/>
                  • <b>Stack (LIFO)</b>: push, pop, infix-to-postfix<br/>
                  • <b>Queue (FIFO)</b>: enqueue, dequeue, circular buffer
                </div>
              </div>
              <div class="dsa-card" style="border-left:4px solid #f59e0b;background:#181a26;padding:16px;border-radius:10px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:15px;margin-bottom:8px;">2. Trees & Hierarchies</div>
                <div style="font-size:13px;color:#c7cad6;line-height:1.6;">
                  • <b>Binary Search Tree (BST)</b>: Left &lt; Root &lt; Right<br/>
                  • <b>BST Deletion</b>: Case 1 (Leaf), Case 2 (1 Child), Case 3 (2 Children)<br/>
                  • <b>Binary Heap</b>: Min/Max Heap, Complete Tree, 1-based array<br/>
                  • <b>Percolate Up & Down</b>: O(log N)
                </div>
              </div>
              <div class="dsa-card" style="border-left:4px solid #10b981;background:#181a26;padding:16px;border-radius:10px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;margin-bottom:8px;">3. Direct Access & Hashing</div>
                <div style="font-size:13px;color:#c7cad6;line-height:1.6;">
                  • <b>Hash Function</b>: h(k) = k mod M<br/>
                  • <b>Separate Chaining</b>: Linked buckets, Load factor λ<br/>
                  • <b>Open Addressing</b>: Linear, Quadratic, Double Hashing<br/>
                  • <b>Average Complexity</b>: O(1) Insert / Search / Delete
                </div>
              </div>
              <div class="dsa-card" style="border-left:4px solid #b794f6;background:#181a26;padding:16px;border-radius:10px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#b794f6;font-size:15px;margin-bottom:8px;">4. Graphs & Algorithms</div>
                <div style="font-size:13px;color:#c7cad6;line-height:1.6;">
                  • <b>Representations</b>: Adjacency Matrix vs Adjacency List<br/>
                  • <b>Traversals</b>: BFS (Queue) vs DFS (Stack / Recursion)<br/>
                  • <b>Topological Sort</b>: Indegree array & DAGs<br/>
                  • <b>Dijkstra's Algorithm</b>: Greedy Shortest Path O((V+E) log V)
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 สถาปัตยกรรมครอบคลุมทั้ง 4 เสาหลักของวิชา Data Structures & Algorithms พร้อมโหมดทดลอง Interactive ทุกหัวข้อ</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 2. ADT VS DATA STRUCTURE (Chapter 01.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('01.1') && inDocIdx === 1) || (lower.includes('abstract data type') && lower.includes('what to do')) || (lower.includes('data structure a') && lower.includes('data structure b'))) {
      return {
        title: '🏛️ Abstract Data Type (ADT) vs Physical Data Structure Architecture',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 60px 1fr;gap:12px;align-items:center;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:18px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:8px;">🏛️ Abstract Data Type (ADT)</div>
                <div style="font-size:13px;color:#94a3b8;margin-bottom:10px;"><b>"What it does"</b> — นิยามและพฤติกรรมภายนอก (User View)</div>
                <div style="background:rgba(79,209,232,0.1);padding:10px;border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#e2e8f0;">
                  • insert(x)<br/>
                  • delete(x)<br/>
                  • search(x)<br/>
                  • isEmpty()
                </div>
              </div>
              <div style="text-align:center;font-size:24px;color:#fbbf24;">➔<br/><span style="font-size:10px;color:#94a3b8;">Implements</span></div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:12px;padding:18px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:15px;margin-bottom:8px;">⚙️ Physical Data Structure</div>
                <div style="font-size:13px;color:#94a3b8;margin-bottom:10px;"><b>"How it works"</b> — การจัดสรรหน่วยความจำจริง (Hardware View)</div>
                <div style="background:rgba(16,185,129,0.1);padding:10px;border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#e2e8f0;">
                  • Contiguous Array Memory<br/>
                  • Pointer Linked Nodes<br/>
                  • Hash Buckets + Probing<br/>
                  • Complete Binary Heap
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">💡 หัวใจสำคัญ: ผู้ใช้งานสนใจเพียง ADT (Method Name & Return Value) ส่วนผู้พัฒนาต้องเลือก Data Structure ที่ให้ Big-O ที่ดีที่สุด</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 3. ASYMPTOTIC NOTATIONS (Chapter 01.1 - Diagram 2)
    // =========================================================================
    if ((dId.includes('01.1') && inDocIdx === 2) || (lower.includes('o_notation') && lower.includes('omega_notation') && lower.includes('theta_notation'))) {
      return {
        title: '📈 Asymptotic Notations: Big-O, Big-Omega, Big-Theta',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:14px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:16px;">O(g(N)) — Big-O</div>
                <div style="font-size:12.5px;color:#38bdf8;font-weight:600;margin:4px 0 8px;">Upper Bound (ขอบเขตบน)</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">ใช้บอก <b>Worst-Case</b> เวลาทำงานจริงไม่มีทางแย่ไปกว่าอัตรานี้: f(N) ≤ c·g(N)</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:16px;">Ω(g(N)) — Big-Omega</div>
                <div style="font-size:12.5px;color:#fbbf24;font-weight:600;margin:4px 0 8px;">Lower Bound (ขอบเขตล่าง)</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">ใช้บอก <b>Best-Case</b> เวลาทำงานจริงไม่มีทางเร็วกว่าขอบเขตนี้: f(N) ≥ c·g(N)</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:16px;">Θ(g(N)) — Big-Theta</div>
                <div style="font-size:12.5px;color:#34d399;font-weight:600;margin:4px 0 8px;">Tight Bound (ขอบเขตรัดกุม)</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">เมื่อ Upper Bound และ Lower Bound ขนาบเท่ากันพอดี: c₁·g(N) ≤ f(N) ≤ c₂·g(N)</p>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 4. BIG-O GROWTH RATE SPECTRUM (Chapter 01.1 - Diagram 3)
    // =========================================================================
    if ((dId.includes('01.1') && inDocIdx === 3) || (lower.includes('o1["o(1)') && lower.includes('ologn') && lower.includes('on["o(n)'))) {
      return {
        title: '🚀 Big-O Growth Rate Spectrum (ลำดับความเร็วจากเร็วสุดไปช้าสุด)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;flex-direction:column;gap:8px;">
              <div style="display:grid;grid-template-columns:120px 1fr 140px;align-items:center;background:#181a26;padding:10px 16px;border-radius:8px;border-left:4px solid #10b981;">
                <span style="font-family:'JetBrains Mono',monospace;font-weight:700;color:#10b981;font-size:15px;">O(1)</span>
                <span style="font-size:13px;color:#e2e8f0;">Constant Time — เร็วคงที่ เช่น เข้าถึง Index อาร์เรย์ หรือ Hash Lookup</span>
                <span style="font-size:11.5px;color:#34d399;font-weight:700;text-align:right;">⚡ ยอดเยี่ยม (Instant)</span>
              </div>
              <div style="display:grid;grid-template-columns:120px 1fr 140px;align-items:center;background:#181a26;padding:10px 16px;border-radius:8px;border-left:4px solid #4fd1e8;">
                <span style="font-family:'JetBrains Mono',monospace;font-weight:700;color:#4fd1e8;font-size:15px;">O(log N)</span>
                <span style="font-size:13px;color:#e2e8f0;">Logarithmic Time — ตัดปัญหาลงทีละครึ่ง เช่น Binary Search, Heap Ops</span>
                <span style="font-size:11.5px;color:#38bdf8;font-weight:700;text-align:right;">💎 ดีเยี่ยม (Sub-linear)</span>
              </div>
              <div style="display:grid;grid-template-columns:120px 1fr 140px;align-items:center;background:#181a26;padding:10px 16px;border-radius:8px;border-left:4px solid #3b82f6;">
                <span style="font-family:'JetBrains Mono',monospace;font-weight:700;color:#60a5fa;font-size:15px;">O(N)</span>
                <span style="font-size:13px;color:#e2e8f0;">Linear Time — แปรผันตรงกับขนาด N เช่น Linear Search, Traversal</span>
                <span style="font-size:11.5px;color:#93c5fd;font-weight:700;text-align:right;">👍 ปานกลาง (Fair)</span>
              </div>
              <div style="display:grid;grid-template-columns:120px 1fr 140px;align-items:center;background:#181a26;padding:10px 16px;border-radius:8px;border-left:4px solid #b794f6;">
                <span style="font-family:'JetBrains Mono',monospace;font-weight:700;color:#c084fc;font-size:15px;">O(N log N)</span>
                <span style="font-size:13px;color:#e2e8f0;">Linearithmic Time — อัลกอริทึมเรียงข้อมูลที่ดีที่สุด เช่น Merge Sort, Quick Sort</span>
                <span style="font-size:11.5px;color:#d8b4fe;font-weight:700;text-align:right;">⚖️ ยอมรับได้ (Optimal)</span>
              </div>
              <div style="display:grid;grid-template-columns:120px 1fr 140px;align-items:center;background:#181a26;padding:10px 16px;border-radius:8px;border-left:4px solid #f59e0b;">
                <span style="font-family:'JetBrains Mono',monospace;font-weight:700;color:#fbbf24;font-size:15px;">O(N²)</span>
                <span style="font-size:13px;color:#e2e8f0;">Quadratic Time — Nested Loops สองชั้น เช่น Bubble Sort, Selection Sort</span>
                <span style="font-size:11.5px;color:#fde68a;font-weight:700;text-align:right;">⚠️ ช้ามาก (Quadratic)</span>
              </div>
              <div style="display:grid;grid-template-columns:120px 1fr 140px;align-items:center;background:#181a26;padding:10px 16px;border-radius:8px;border-left:4px solid #ef4444;">
                <span style="font-family:'JetBrains Mono',monospace;font-weight:700;color:#f87171;font-size:15px;">O(2ᴺ)</span>
                <span style="font-size:13px;color:#e2e8f0;">Exponential Time — Recursive Fibonacci หรือ Brute Force หน่วงระเบิด</span>
                <span style="font-size:11.5px;color:#fca5a5;font-weight:700;text-align:right;">❌ แย่ที่สุด (Explosive)</span>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 5. PYTHON MEMORY REFERENCE MODEL (Chapter 02.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('02.1') && inDocIdx === 1) || (lower.includes('pylist object') || (lower.includes('vara') && lower.includes('listobj')))) {
      return {
        title: '🐍 Python Memory Reference Model (Pointer & Identity in Heap)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 60px 1.4fr 60px 1fr;gap:12px;align-items:center;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;">Variable: a</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#94a3b8;font-size:12px;margin-top:4px;">Reference Pointer</div>
                <div style="color:#38bdf8;font-size:11px;font-family:'JetBrains Mono',monospace;margin-top:6px;">➔ 0x7f8a</div>
              </div>
              <div style="text-align:center;font-size:24px;color:#38bdf8;">➔</div>
              <div style="background:#181a26;border:2px solid #10b981;border-radius:12px;padding:18px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:16px;">PyList Object in Heap</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#34d399;font-size:11.5px;margin-bottom:10px;">Memory Address: 0x7f8a</div>
                <div style="display:flex;gap:8px;justify-content:center;align-items:center;">
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#10b981;"><span class="cell-val">1</span></div>
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#10b981;"><span class="cell-val">2</span></div>
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#10b981;"><span class="cell-val">3</span></div>
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#f59e0b;background:rgba(245,158,11,0.15);"><span class="cell-val" style="color:#fbbf24;">4</span></div>
                </div>
                <div style="font-size:11px;color:#94a3b8;margin-top:8px;font-family:'JetBrains Mono',monospace;">b.append(4) แก้ไขที่อ็อบเจกต์นี้</div>
              </div>
              <div style="text-align:center;font-size:24px;color:#38bdf8;">🠔</div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;">Variable: b (b = a)</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#94a3b8;font-size:12px;margin-top:4px;">Reference Pointer</div>
                <div style="color:#38bdf8;font-size:11px;font-family:'JetBrains Mono',monospace;margin-top:6px;">➔ 0x7f8a</div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">💡 Python Reference Rule: ตัวแปร <code>b = a</code> ไม่ได้สร้าง List สำเนาใหม่ แต่แชร์พอยน์เตอร์ชี้ไปที่ Heap Object <code>0x7f8a</code> ตัวเดียวกัน เมื่อสั่ง <code>b.append(4)</code> ตัวแปร <code>a</code> จึงเห็น <code>[1, 2, 3, 4]</code> เช่นกัน!</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 6. OOP 4 PILLARS (Chapter 02.1 - Diagram 2)
    // =========================================================================
    if ((dId.includes('02.1') && inDocIdx === 2) || (lower.includes('4 pillars of oop') || (lower.includes('encapsulation') && lower.includes('polymorphism') && lower.includes('inheritance')))) {
      return {
        title: '🏛️ The 4 Pillars of Object-Oriented Programming (OOP Architecture)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:14px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;">1. Encapsulation</div>
                <div style="font-size:12.5px;color:#94a3b8;margin:4px 0 8px;">การห่อหุ้มและซ่อนข้อมูล</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">ใช้ Prefix <code>_</code> หรือ <code>__</code> เพื่อซ่อนตัวแปรภายใน และเข้าถึงผ่าน Getter/Setter ป้องกันข้อมูลเพี้ยน</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;">2. Abstraction</div>
                <div style="font-size:12.5px;color:#94a3b8;margin:4px 0 8px;">การซ่อนรายละเอียดซับซ้อน</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">เปิดเผยเฉพาะ Method ที่จำเป็น เช่น <code>push()</code> โดยผู้ใช้ไม่ต้องรู้โครงสร้าง Pointer ภายใน</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:15px;">3. Inheritance</div>
                <div style="font-size:12.5px;color:#94a3b8;margin:4px 0 8px;">การสืบทอดคุณสมบัติ</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">คลาสลูกรับถ่ายทอด Attribute และ Method จากคลาสแม่ผ่าน <code>super().__init__()</code> ลดโค้ดซ้ำซ้อน</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #b794f6;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#b794f6;font-size:15px;">4. Polymorphism</div>
                <div style="font-size:12.5px;color:#94a3b8;margin:4px 0 8px;">พหุรูปร่าง (Overriding)</div>
                <p style="font-size:13px;color:#c7cad6;margin:0;">Method ชื่อเดียวกันแต่มีพฤติกรรมเฉพาะตามคลาส เช่น <code>__str__</code> หรือ <code>area()</code></p>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 7. OOP CLASS DIAGRAM (Chapter 02.1 - Diagram 3)
    // =========================================================================
    if ((dId.includes('02.1') && inDocIdx === 3) || (lower.includes('class person') && lower.includes('class student'))) {
      return {
        title: '🐍 Python OOP Class & Object Architecture (Inheritance & Static Member)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 50px 1fr;gap:12px;align-items:center;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;margin-bottom:8px;">Base Class: Person</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#c7cad6;line-height:1.7;">
                  - __name: String<br/>
                  - __age: int<br/>
                  + setName(name)<br/>
                  + getName(): String<br/>
                  + toString(): String
                </div>
              </div>
              <div style="text-align:center;font-size:24px;color:#fbbf24;">▲<br/><span style="font-size:10px;color:#94a3b8;">Extends</span></div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;margin-bottom:8px;">Derived Class: Student</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#c7cad6;line-height:1.7;">
                  - __gpa: float<br/>
                  + setGpa(gpa)<br/>
                  + getGpa(): float<br/>
                  + toString(): Override!
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 8. SINGLY LINKED LIST (Chapter 03.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 1) || (lower.includes('p1["next: 0x240"]') && lower.includes('head = 0x100'))) {
      return {
        title: '🔗 Singly Linked List Memory Model (โครงสร้างพอยน์เตอร์ในหน่วยความจำ)',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:12px;overflow-x:auto;padding:16px 4px;">
              <div style="background:#181a26;border:2px dashed #f59e0b;padding:12px 16px;border-radius:10px;text-align:center;flex-shrink:0;">
                <div style="color:#f59e0b;font-weight:700;font-size:12px;">📍 head Pointer</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#fff;font-size:15px;font-weight:700;">0x100</div>
              </div>
              <div style="font-size:22px;color:#38bdf8;">➔</div>
              <!-- Node 1 -->
              <div style="display:flex;border:2px solid #4fd1e8;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;box-shadow:0 0 15px rgba(79,209,232,0.15);">
                <div style="padding:14px 20px;border-right:1px solid #334155;text-align:center;">
                  <div style="font-size:11px;color:#94a3b8;">data</div>
                  <div style="font-family:'Chakra Petch',sans-serif;font-size:18px;font-weight:700;color:#fff;">10</div>
                </div>
                <div style="padding:14px 16px;background:rgba(79,209,232,0.1);text-align:center;">
                  <div style="font-size:11px;color:#38bdf8;">next</div>
                  <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#4fd1e8;font-weight:600;">0x240</div>
                </div>
              </div>
              <div style="font-size:22px;color:#38bdf8;">➔</div>
              <!-- Node 2 -->
              <div style="display:flex;border:2px solid #4fd1e8;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:14px 20px;border-right:1px solid #334155;text-align:center;">
                  <div style="font-size:11px;color:#94a3b8;">data</div>
                  <div style="font-family:'Chakra Petch',sans-serif;font-size:18px;font-weight:700;color:#fff;">20</div>
                </div>
                <div style="padding:14px 16px;background:rgba(79,209,232,0.1);text-align:center;">
                  <div style="font-size:11px;color:#38bdf8;">next</div>
                  <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#4fd1e8;font-weight:600;">0x380</div>
                </div>
              </div>
              <div style="font-size:22px;color:#38bdf8;">➔</div>
              <!-- Node 3 -->
              <div style="display:flex;border:2px solid #4fd1e8;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:14px 20px;border-right:1px solid #334155;text-align:center;">
                  <div style="font-size:11px;color:#94a3b8;">data</div>
                  <div style="font-family:'Chakra Petch',sans-serif;font-size:18px;font-weight:700;color:#fff;">30</div>
                </div>
                <div style="padding:14px 16px;background:rgba(239,68,68,0.1);text-align:center;">
                  <div style="font-size:11px;color:#f87171;">next</div>
                  <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#ef4444;font-weight:700;">None</div>
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 แต่ละ Node ไม่จำเป็นต้องอยู่ติดกันใน Memory เพราะใช้ <code>next</code> ในการเชื่อมโยงหากัน</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 9. DOUBLY LINKED LIST (Chapter 03.1 - Diagram 2)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 2) || (lower.includes('dp1["prev: none"]') && lower.includes('dd1["data: 10"]'))) {
      return {
        title: '🔗 Doubly Linked List Model (แบบจำลองเชื่อมโยงสองทิศทาง)',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:8px;overflow-x:auto;padding:16px 4px;">
              <div style="display:flex;border:2px solid #10b981;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:12px;background:rgba(239,68,68,0.1);color:#ef4444;font-family:'JetBrains Mono',monospace;font-size:12px;">prev: None</div>
                <div style="padding:12px 18px;border-left:1px solid #334155;border-right:1px solid #334155;font-weight:700;font-size:16px;color:#fff;">10</div>
                <div style="padding:12px;background:rgba(16,185,129,0.1);color:#10b981;font-family:'JetBrains Mono',monospace;font-size:12px;">next: 0x240</div>
              </div>
              <div style="font-size:20px;color:#34d399;">⇄</div>
              <div style="display:flex;border:2px solid #10b981;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:12px;background:rgba(16,185,129,0.1);color:#10b981;font-family:'JetBrains Mono',monospace;font-size:12px;">prev: 0x100</div>
                <div style="padding:12px 18px;border-left:1px solid #334155;border-right:1px solid #334155;font-weight:700;font-size:16px;color:#fff;">20</div>
                <div style="padding:12px;background:rgba(16,185,129,0.1);color:#10b981;font-family:'JetBrains Mono',monospace;font-size:12px;">next: 0x380</div>
              </div>
              <div style="font-size:20px;color:#34d399;">⇄</div>
              <div style="display:flex;border:2px solid #10b981;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:12px;background:rgba(16,185,129,0.1);color:#10b981;font-family:'JetBrains Mono',monospace;font-size:12px;">prev: 0x240</div>
                <div style="padding:12px 18px;border-left:1px solid #334155;border-right:1px solid #334155;font-weight:700;font-size:16px;color:#fff;">30</div>
                <div style="padding:12px;background:rgba(239,68,68,0.1);color:#ef4444;font-family:'JetBrains Mono',monospace;font-size:12px;">next: None</div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚡ DLL เดินหน้าและถอยหลังได้ใน O(1) แต่ใช้ Memory เพิ่มขึ้นสำหรับ <code>prev</code> pointer</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 10. CIRCULAR LINKED LIST (Chapter 03.1 - Diagram 3)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 3) || (lower.includes('chead["📍 head"]') && lower.includes('cn1'))) {
      return {
        title: '🔄 Circular Linked List Architecture (โหนดท้ายวนกลับมาชี้ Head)',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="position:relative;background:#181a26;border-radius:12px;padding:24px;border:1px solid #334155;">
              <div style="display:flex;justify-content:center;gap:36px;align-items:center;">
                <div style="border:2px solid #4fd1e8;border-radius:10px;padding:12px 18px;background:#20222c;text-align:center;">
                  <div style="font-size:10px;color:#4fd1e8;font-weight:700;">HEAD (0x100)</div>
                  <div style="font-size:16px;font-weight:700;color:#fff;">Node 1 [10]</div>
                </div>
                <div style="font-size:22px;color:#4fd1e8;">➔</div>
                <div style="border:2px solid #4fd1e8;border-radius:10px;padding:12px 18px;background:#20222c;text-align:center;">
                  <div style="font-size:10px;color:#94a3b8;">NODE (0x240)</div>
                  <div style="font-size:16px;font-weight:700;color:#fff;">Node 2 [20]</div>
                </div>
                <div style="font-size:22px;color:#4fd1e8;">➔</div>
                <div style="border:2px solid #4fd1e8;border-radius:10px;padding:12px 18px;background:#20222c;text-align:center;">
                  <div style="font-size:10px;color:#f59e0b;font-weight:700;">TAIL (0x380)</div>
                  <div style="font-size:16px;font-weight:700;color:#fff;">Node 3 [30]</div>
                </div>
              </div>
              <div style="margin-top:16px;padding:8px;background:rgba(245,158,11,0.1);border:1px dashed #f59e0b;border-radius:8px;text-align:center;font-size:12.5px;color:#fbbf24;">
                🔄 Loop Back: <code>tail.next = head</code> (วนลูปกลับมาชี้ Node 1 โดยไม่มี None ตลอดสาย)
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 11. INSERT AT HEAD (Chapter 03.1 - Diagram 4)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 4) || (lower.includes('beforeinsert') && lower.includes('stepconnect') && lower.includes('new_node(5)'))) {
      return {
        title: '⚡ Linked List: การแทรกโหนดหน้าสุด (Insert at Head in O(1))',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1.5px solid #334155;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#fbbf24;margin-bottom:8px;">สเต็ป 1: เชื่อม new_node.next = head</div>
                <div style="display:flex;align-items:center;gap:8px;">
                  <div class="dsa-heap-cell" style="border-color:#10b981;background:rgba(16,185,129,0.1);"><span class="cell-val">new(5)</span></div>
                  <div style="color:#10b981;font-weight:700;">➔</div>
                  <div class="dsa-heap-cell"><span class="cell-val">head[10]</span></div>
                  <div style="color:#64748b;">➔</div>
                  <div class="dsa-heap-cell"><span class="cell-val">[20]</span></div>
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#34d399;margin-bottom:8px;">สเต็ป 2: ย้าย head = new_node</div>
                <div style="display:flex;align-items:center;gap:8px;">
                  <div class="dsa-heap-cell root-cell"><span class="cell-idx">head</span><span class="cell-val">5</span></div>
                  <div style="color:#10b981;font-weight:700;">➔</div>
                  <div class="dsa-heap-cell"><span class="cell-val">10</span></div>
                  <div style="color:#10b981;font-weight:700;">➔</div>
                  <div class="dsa-heap-cell"><span class="cell-val">20</span></div>
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚠️ ข้อควรระวังในห้องสอบ: ห้ามสั่ง <code>head = new_node</code> ก่อนเชื่อม <code>new_node.next = head</code> เด็ดขาด มิฉะนั้นโหนดเดิมจะหลุดหายทั้งยวง!</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 12. DELETE MIDDLE NODE BYPASS (Chapter 03.1 - Diagram 5)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 5) || (lower.includes('prev.next = curr.next') && lower.includes('node(20) [target!]'))) {
      return {
        title: '✂️ Linked List: การลบโหนดเป้าหมาย (Pointer Bypass Removal)',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;justify-content:center;gap:12px;padding:16px 0;">
              <div class="dsa-heap-cell" style="border-color:#4fd1e8;"><span class="cell-idx">prev</span><span class="cell-val">10</span></div>
              <div style="font-size:24px;color:#10b981;font-weight:700;">═════ ข้าม ═════➔</div>
              <div class="dsa-heap-cell" style="border-color:#ef4444;background:rgba(239,68,68,0.15);opacity:0.45;"><span class="cell-idx">curr (ลบ)</span><span class="cell-val">20 ❌</span></div>
              <div style="font-size:20px;color:#64748b;">➔</div>
              <div class="dsa-heap-cell" style="border-color:#4fd1e8;"><span class="cell-idx">curr.next</span><span class="cell-val">30</span></div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">✂️ ทำงานเพียง 1 บรรทัด: <code>prev.next = curr.next</code> ทำให้ Node 20 หลุดจากการอ้างอิงและถูก Python Garbage Collector เก็บกวาดอัตโนมัติ</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 13. DOUBLY LINKED LIST INSERT (4-STEP) (Chapter 03.1 - Diagram 6)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 6) || (lower.includes('การปรับเปลี่ยนพอยน์เตอร์ 4 สเต็ป') || (lower.includes('curr.next.prev = new_node') && lower.includes('new_node.prev = curr')))) {
      return {
        title: '🔗 Doubly Linked List: ปรับเปลี่ยนพอยน์เตอร์ 4 สเต็ปอย่างปลอดภัย',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:12px;">
              <div style="background:#181a26;border-left:4px solid #4fd1e8;padding:12px;border-radius:8px;">
                <b style="color:#4fd1e8;">สเต็ป 1:</b> <code>new_node.next = curr.next</code><br/>
                <span style="font-size:12px;color:#94a3b8;">ต่อขาหน้าของโหนดใหม่ไปหาโหนดถัดไป</span>
              </div>
              <div style="background:#181a26;border-left:4px solid #10b981;padding:12px;border-radius:8px;">
                <b style="color:#10b981;">สเต็ป 2:</b> <code>new_node.prev = curr</code><br/>
                <span style="font-size:12px;color:#94a3b8;">ต่อขาหลังของโหนดใหม่กลับมาหา curr</span>
              </div>
              <div style="background:#181a26;border-left:4px solid #f59e0b;padding:12px;border-radius:8px;">
                <b style="color:#f59e0b;">สเต็ป 3:</b> <code>curr.next.prev = new_node</code><br/>
                <span style="font-size:12px;color:#94a3b8;">ให้โหนดถัดไปหันกลับมาชี้ที่ new_node</span>
              </div>
              <div style="background:#181a26;border-left:4px solid #b794f6;padding:12px;border-radius:8px;">
                <b style="color:#b794f6;">สเต็ป 4:</b> <code>curr.next = new_node</code><br/>
                <span style="font-size:12px;color:#94a3b8;">ให้ curr หันไปชี้ new_node เป็นอันเสร็จสมบูรณ์</span>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 14. LINKED LIST TRAVERSAL TRACE 7->1->2->3->6->0 (Chapter 03.1 - Diagram 7)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 7) || (lower.includes('n6["[7]"]') && lower.includes('n2["[1]"]') && lower.includes('n1["[0]"]'))) {
      return {
        title: '🔍 Linked List Traversal Trace: [7] ➔ [1] ➔ [2] ➔ [3] ➔ [6] ➔ [0]',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:8px;overflow-x:auto;padding:14px 4px;">
              <div class="dsa-heap-cell root-cell"><span class="cell-idx">head</span><span class="cell-val">7</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">1</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">2</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">3</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">6</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">0</span></div>
              <span style="color:#ef4444;">➔</span>
              <span style="font-family:'JetBrains Mono',monospace;color:#ef4444;font-weight:700;">None</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 15. NODE POINTER SWAPPING (Chapter 03.1 - Diagram 8)
    // =========================================================================
    if ((dId.includes('03.1') && inDocIdx === 8) || (lower.includes('1 -> 4 -> 3 -> 2 -> 5') || (lower.includes('node 1 (head)') && lower.includes('node 4') && lower.includes('node 3')))) {
      return {
        title: '✂️ Linked List Node Pointer Swapping (สลับตำแหน่ง Node 2 และ Node 4)',
        topicHash: '#list',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:10px;justify-content:center;padding:16px 0;">
              <div class="dsa-heap-cell root-cell"><span class="cell-idx">head</span><span class="cell-val">Node 1</span></div>
              <span style="color:#10b981;font-weight:700;">➔</span>
              <div class="dsa-heap-cell" style="border-color:#10b981;background:rgba(16,185,129,0.15);"><span class="cell-idx">สลับ</span><span class="cell-val">Node 4</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">Node 3</span></div>
              <span style="color:#f59e0b;font-weight:700;">➔</span>
              <div class="dsa-heap-cell" style="border-color:#f59e0b;background:rgba(245,158,11,0.15);"><span class="cell-idx">สลับ</span><span class="cell-val">Node 2</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell"><span class="cell-val">Node 5</span></div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 การสลับโหนดจริงโดยไม่สลับข้อมูล (Value Swap) ต้องปรับ Pointer ทั้งหมด 4 เส้นรอบโหนดที่เกี่ยวข้อง</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 16. STACK ADT LIFO CANISTER (Chapter 04.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('04.1') && inDocIdx === 1) || (lower.includes('stack_ops') || (lower.includes('pushop["📥 push(30)"]') && lower.includes('topnode')))) {
      return {
        title: '🥞 Stack ADT Memory Model: LIFO (Last-In First-Out) Canister',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap" style="display:grid;grid-template-columns:220px 1fr;gap:24px;align-items:center;">
            <!-- Canister Visual -->
            <div style="background:#13151f;border:2px solid #3b82f6;border-top:none;border-radius:0 0 16px 16px;padding:12px;display:flex;flex-direction:column;gap:8px;box-shadow:0 8px 25px rgba(59,130,246,0.2);">
              <div style="border:2px solid #34d399;border-radius:8px;padding:12px;background:#064e3b;color:#fff;font-weight:700;text-align:center;position:relative;">
                [ 30 ]
                <span style="position:absolute;right:-70px;top:10px;font-size:11px;color:#34d399;font-weight:700;">◀ TOP</span>
              </div>
              <div style="border:1.5px solid #4fd1e8;border-radius:8px;padding:12px;background:#181a26;color:#e2e8f0;font-weight:600;text-align:center;">
                [ 20 ]
              </div>
              <div style="border:1.5px solid #4fd1e8;border-radius:8px;padding:12px;background:#181a26;color:#e2e8f0;font-weight:600;text-align:center;position:relative;">
                [ 10 ]
                <span style="position:absolute;right:-90px;top:10px;font-size:11px;color:#94a3b8;">◀ BOTTOM</span>
              </div>
            </div>
            <!-- Explanations -->
            <div style="display:flex;flex-direction:column;gap:12px;">
              <div style="background:#181a26;padding:12px 16px;border-radius:8px;border-left:4px solid #10b981;">
                <b style="color:#10b981;">📥 push(x):</b> บรรจุข้อมูลลงที่ด้านบนสุด (Top) ในเวลา O(1)
              </div>
              <div style="background:#181a26;padding:12px 16px;border-radius:8px;border-left:4px solid #ef4444;">
                <b style="color:#f87171;">📤 pop():</b> ดึงข้อมูลตัวบนสุดออกมาก่อนเสมอ (LIFO) ในเวลา O(1)
              </div>
              <div style="background:#181a26;padding:12px 16px;border-radius:8px;border-left:4px solid #4fd1e8;">
                <b style="color:#38bdf8;">👀 peek() / top():</b> ส่องดูข้อมูลตัวบนสุดโดยไม่ต้องดึงออก ในเวลา O(1)
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 17. TREE TERMINOLOGY (Chapter 05.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 1) || (lower.includes('root: a (depth=0') && lower.includes('b (internal node)'))) {
      return {
        title: '🌲 Tree Terminology Architecture: Root, Internal Nodes, Leaves & Depth/Height Levels',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 540 220" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="40" x2="160" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="40" x2="380" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="110" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="210" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="105" x2="430" y2="170" stroke="#334155" stroke-width="2.5" />

              <circle cx="270" cy="40" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="45" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="15" text-anchor="middle">A</text>
              <text x="350" y="45" fill="#fbbf24" font-family="'JetBrains Mono',monospace" font-size="11">Root (Depth=0, Height=2)</text>

              <circle cx="160" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="110" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="14" text-anchor="middle">B</text>

              <circle cx="380" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="380" y="110" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="14" text-anchor="middle">C</text>
              <text x="440" y="110" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="11">Internal Nodes</text>

              <circle cx="110" cy="170" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="110" y="174" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">D</text>

              <circle cx="210" cy="170" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="210" y="174" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">E</text>

              <circle cx="430" cy="170" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="430" y="174" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">F</text>
              <text x="490" y="174" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="11">Leaves (Depth=2)</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 นิยาม: Depth วัดจากบนลงล่าง (Root Depth=0) ส่วน Height วัดจากล่างขึ้นบน (Leaf Height=0, Tree Height=2)</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 18. FULL VS COMPLETE BINARY TREE (Chapter 05.1 - Diagram 2)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 2) || (lower.includes('full binary tree') && lower.includes('complete binary tree'))) {
      return {
        title: '🌴 Structural Comparison: Full Binary Tree vs Complete Binary Tree',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:8px;">1. Full Binary Tree</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-bottom:12px;">ทุก Node ต้องมีลูก <b>0 หรือ 2 ตัวเท่านั้น</b> (ห้ามมีลูกเดี่ยว 1 ตัว)</div>
                <svg viewBox="0 0 240 140" style="width:100%;max-width:240px;margin:0 auto;display:block;">
                  <line x1="120" y1="20" x2="70" y2="65" stroke="#334155" stroke-width="2" />
                  <line x1="120" y1="20" x2="170" y2="65" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="65" x2="45" y2="110" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="65" x2="95" y2="110" stroke="#334155" stroke-width="2" />
                  <circle cx="120" cy="20" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="120" y="24" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">A</text>
                  <circle cx="70" cy="65" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="70" y="69" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">B</text>
                  <circle cx="170" cy="65" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="170" y="69" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">C</text>
                  <circle cx="45" cy="110" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="45" y="114" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">D</text>
                  <circle cx="95" cy="110" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="95" y="114" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">E</text>
                </svg>
              </div>

              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:15px;margin-bottom:8px;">2. Complete Binary Tree</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-bottom:12px;">เต็มทุกชั้น และชั้นสุดท้ายต้อง <b>เรียงชิดซ้ายสุดเสมอ</b> (โครงสร้างของ Heap)</div>
                <svg viewBox="0 0 240 140" style="width:100%;max-width:240px;margin:0 auto;display:block;">
                  <line x1="120" y1="20" x2="70" y2="65" stroke="#334155" stroke-width="2" />
                  <line x1="120" y1="20" x2="170" y2="65" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="65" x2="45" y2="110" stroke="#334155" stroke-width="2" />
                  <line x1="70" y1="65" x2="95" y2="110" stroke="#334155" stroke-width="2" />
                  <line x1="170" y1="65" x2="145" y2="110" stroke="#334155" stroke-width="2" />
                  <circle cx="120" cy="20" r="14" fill="#181a26" stroke="#10b981" stroke-width="2" /><text x="120" y="24" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">A</text>
                  <circle cx="70" cy="65" r="14" fill="#181a26" stroke="#10b981" stroke-width="2" /><text x="70" y="69" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">B</text>
                  <circle cx="170" cy="65" r="14" fill="#181a26" stroke="#10b981" stroke-width="2" /><text x="170" y="69" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">C</text>
                  <circle cx="45" cy="110" r="12" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="45" y="114" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">D</text>
                  <circle cx="95" cy="110" r="12" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="95" y="114" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">E</text>
                  <circle cx="145" cy="110" r="12" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="145" y="114" fill="#fff" font-size="10" font-weight="700" text-anchor="middle">F</text>
                </svg>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 19. TREE TRAVERSALS 4 TYPES (Chapter 05.1 - Diagram 3)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 3) || (lower.includes('tree traversals') && lower.includes('preorder: root') && lower.includes('inorder: left'))) {
      return {
        title: '🔄 Tree Traversals Taxonomy: DFS (Pre, In, Post) vs BFS (Level-Order)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:14px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;">1. Preorder (NLR)</div>
                <div style="font-size:13px;color:#38bdf8;font-weight:600;margin:4px 0 8px;">Root ➔ Left ➔ Right</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">แวะ Root ก่อนใคร นิยมใช้ทำ Deep Clone ต้นไม้ หรือสร้าง Prefix Expression</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;">2. Inorder (LNR)</div>
                <div style="font-size:13px;color:#34d399;font-weight:600;margin:4px 0 8px;">Left ➔ Root ➔ Right</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">เมื่อท่อง BST จะได้ลำดับตัวเลข <b>เรียงจากน้อยไปมาก (Sorted)</b> เสมอ!</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:15px;">3. Postorder (LRN)</div>
                <div style="font-size:13px;color:#fbbf24;font-weight:600;margin:4px 0 8px;">Left ➔ Right ➔ Root</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">เคลียร์ลูกทั้งสองข้างก่อนแม่ นิยมใช้ลบต้นไม้จากล่างขึ้นบน หรือคำนวณพื้นที่โฟลเดอร์</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #b794f6;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#b794f6;font-size:15px;">4. Level-Order (BFS)</div>
                <div style="font-size:13px;color:#c084fc;font-weight:600;margin:4px 0 8px;">ทีละชั้นจากบนลงล่าง</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">ใช้ Queue (FIFO) เก็บโหนด ท่องทีละระดับความลึกจากซ้ายไปขวา</p>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 20. TREE PATH NOTATION QUESTION A->E->J->P (Chapter 05.1 - Diagram 4)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 4) || (lower.includes('node a (root)') && lower.includes('node p') && lower.includes('node e'))) {
      return {
        title: '🎯 Tree Path Notation: เส้นทางจาก Root A ไปยัง Leaf P (A ➔ E ➔ J ➔ P)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;justify-content:center;gap:12px;padding:16px 0;">
              <div class="dsa-heap-cell root-cell"><span class="cell-idx">Root</span><span class="cell-val">A</span></div>
              <span style="color:#34d399;font-size:22px;font-weight:700;">➔</span>
              <div class="dsa-heap-cell" style="border-color:#34d399;"><span class="cell-idx">Level 1</span><span class="cell-val">E</span></div>
              <span style="color:#34d399;font-size:22px;font-weight:700;">➔</span>
              <div class="dsa-heap-cell" style="border-color:#34d399;"><span class="cell-idx">Level 2</span><span class="cell-val">J</span></div>
              <span style="color:#34d399;font-size:22px;font-weight:700;">➔</span>
              <div class="dsa-heap-cell" style="border-color:#34d399;background:rgba(16,185,129,0.2);"><span class="cell-idx">Leaf (Target)</span><span class="cell-val">P ⭐</span></div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 Path Length = 3 Edges (จำนวนเส้นเชื่อมระหว่าง Root ถึง P คือ 3)</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 21. TREE TRAVERSALS ON 10, 3, 19, 8, 5, 15, 24 (Chapter 05.1 - Diagram 5)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 5) || (lower.includes('n10["10 (root)"]') && lower.includes('n19["19"]') && lower.includes('n24["24"]'))) {
      return {
        title: '🌲 Tree Traversals Tracing: ตัวอย่างการท่องโหนด 10, 3, 19, 8, 5, 15, 24',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 520 180" style="width:100%;max-width:520px;">
              ${svgDefs}
              <line x1="260" y1="36" x2="160" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="260" y1="36" x2="360" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="85" x2="110" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="85" x2="210" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="360" y1="85" x2="310" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="360" y1="85" x2="410" y2="135" stroke="#334155" stroke-width="2.5" />

              <circle cx="260" cy="36" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="260" y="41" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">10</text>
              <circle cx="160" cy="85" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="160" y="90" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <circle cx="360" cy="85" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="360" y="90" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">19</text>
              <circle cx="110" cy="135" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="110" y="139" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">8</text>
              <circle cx="210" cy="135" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="210" y="139" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">5</text>
              <circle cx="310" cy="135" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="310" y="139" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">15</text>
              <circle cx="410" cy="135" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="410" y="139" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">24</text>
            </svg>
            <div style="margin-top:12px;background:#181a26;border-radius:8px;padding:10px 14px;font-size:12.5px;line-height:1.7;">
              • <b>Preorder (NLR):</b> 10, 3, 8, 5, 19, 15, 24<br/>
              • <b>Inorder (LNR):</b> 8, 3, 5, 10, 15, 19, 24<br/>
              • <b>Postorder (LRN):</b> 8, 5, 3, 15, 24, 19, 10
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 22. SKEWED TREE 1->6->7->8 (Chapter 05.1 - Diagram 6)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 6) || (lower.includes('t1["1 (root)"]') && lower.includes('t6["6"]') && lower.includes('t8["8"]'))) {
      return {
        title: '🌴 Skewed Binary Tree Analysis (ต้นไม้เอนขวา Root 1 ➔ 6 ➔ 7 ➔ 8)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;justify-content:center;gap:12px;padding:16px 0;">
              <div class="dsa-heap-cell root-cell"><span class="cell-idx">Root</span><span class="cell-val">1</span></div>
              <span style="color:#ef4444;font-weight:700;">➔ (ขวา)</span>
              <div class="dsa-heap-cell"><span class="cell-val">6</span></div>
              <span style="color:#ef4444;font-weight:700;">➔ (ขวา)</span>
              <div class="dsa-heap-cell"><span class="cell-val">7</span></div>
              <span style="color:#ef4444;font-weight:700;">➔ (ซ้าย)</span>
              <div class="dsa-heap-cell"><span class="cell-val">8</span></div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚠️ Degenerate (Skewed) Tree กลายสภาพเสมือน Linked List ทำให้ความเร็วค้นหาตกฮวบจาก O(log N) ไปเป็น O(N) Worst-Case!</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 23. ARITHMETIC EXPRESSION TREE (Chapter 05.1 - Diagram 7)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 7) || (lower.includes('plusroot["+ (root กลาง)"]') || (lower.includes('mulbc["*"]') && lower.includes('subleft["+"]')))) {
      return {
        title: '🧮 Binary Expression Tree: (a + b * c) + ((d * e + f) * g)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="text-align:center;padding:14px;background:#181a26;border-radius:10px;margin-bottom:12px;font-family:'JetBrains Mono',monospace;font-size:15px;color:#38bdf8;">
              นิพจน์คณิตศาสตร์: <b>(a + (b * c)) + (((d * e) + f) * g)</b>
            </div>
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:12px;font-size:12.5px;">
              <div style="background:#181a26;padding:10px;border-radius:8px;border-left:3px solid #4fd1e8;">
                <b>Prefix (Preorder):</b><br/>+ + a * b c * + * d e f g
              </div>
              <div style="background:#181a26;padding:10px;border-radius:8px;border-left:3px solid #10b981;">
                <b>Infix (Inorder):</b><br/>a + b * c + d * e + f * g
              </div>
              <div style="background:#181a26;padding:10px;border-radius:8px;border-left:3px solid #f59e0b;">
                <b>Postfix (Postorder):</b><br/>a b c * + d e * f + g * +
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 24. SMALL BINARY TREE ROOT 2 -> 3, 3 -> (2, 0) (Chapter 05.1 - Diagram 8)
    // =========================================================================
    if ((dId.includes('05.1') && inDocIdx === 8) || (lower.includes('r2["2 (root)"]') && lower.includes('l3["3"]') && lower.includes('rr0["0"]'))) {
      return {
        title: '🌲 Binary Tree Structure: Root 2 with Subtrees',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 420 160" style="width:100%;max-width:420px;">
              ${svgDefs}
              <line x1="210" y1="30" x2="130" y2="80" stroke="#334155" stroke-width="2.5" />
              <line x1="210" y1="30" x2="290" y2="80" stroke="#334155" stroke-width="2.5" />
              <line x1="290" y1="80" x2="250" y2="130" stroke="#334155" stroke-width="2.5" />
              <line x1="290" y1="80" x2="330" y2="130" stroke="#334155" stroke-width="2.5" />

              <circle cx="210" cy="30" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="210" y="35" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">2</text>
              <circle cx="130" cy="80" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="130" y="84" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <circle cx="290" cy="80" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="290" y="84" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <circle cx="250" cy="130" r="14" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="250" y="134" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">2</text>
              <circle cx="330" cy="130" r="14" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="330" y="134" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">0</text>
            </svg>
          </div>
        `
      };
    }

    // =========================================================================
    // 25. GOLDEN BST RULE (Chapter 05.2 - Diagram 1)
    // =========================================================================
    if ((dId.includes('05.2') && inDocIdx === 1) || (lower.includes('4 < 6') && lower.includes('7 > 6') && lower.includes('3 < 4'))) {
      return {
        title: '🌲 Binary Search Tree (BST) The Golden Rule: Left < Root < Right',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 560 230" style="width:100%;max-width:560px;">
              ${svgDefs}
              <line x1="280" y1="36" x2="160" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="280" y1="36" x2="400" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="85" x2="100" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="85" x2="220" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="100" y1="135" x2="60" y2="185" stroke="#334155" stroke-width="2.5" />
              <line x1="60" y1="185" x2="30" y2="215" stroke="#334155" stroke-width="2.5" />

              <circle cx="280" cy="36" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="280" y="41" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="15" text-anchor="middle">6</text>
              <text x="280" y="14" fill="#f59e0b" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">Root</text>

              <circle cx="160" cy="85" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="90" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="14" text-anchor="middle">4</text>
              <text x="160" y="65" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">4 &lt; 6 (ซ้าย)</text>

              <circle cx="400" cy="85" r="20" fill="#181a26" stroke="#10b981" stroke-width="2.2" filter="url(#dsa-glow-emerald)" />
              <text x="400" y="90" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="14" text-anchor="middle">7</text>
              <text x="400" y="65" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">7 &gt; 6 (ขวา)</text>

              <circle cx="100" cy="135" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="100" y="140" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <text x="100" y="115" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">3 &lt; 4</text>

              <circle cx="220" cy="135" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="220" y="140" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">5</text>
              <text x="220" y="115" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">5 &gt; 4</text>

              <circle cx="60" cy="185" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="60" y="189" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="12" text-anchor="middle">2</text>

              <circle cx="30" cy="215" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.5" />
              <text x="30" y="219" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="11" text-anchor="middle">1</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🌲 กฎทองคำของ BST: ทุกโหนดในกิ่งซ้ายต้องน้อยกว่า Root (&lt; Root) และทุกโหนดในกิ่งขวาต้องมากกว่า Root (&gt; Root) ตลอดทั้งโครงสร้าง</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 26 & 27. BST INSERT 5 TRACE (Chapter 05.2 - Diagrams 2 & 3)
    // =========================================================================
    if ((dId.includes('05.2') && (inDocIdx === 2 || inDocIdx === 3)) || (lower.includes('แทรกใหม่รอบที่ 3') || lower.includes('n5["5 (โหนดใหม่)"]') || (lower.includes('n6["6 (root)"]') && lower.includes('n2["2"]') && lower.includes('n4["4"]')))) {
      const isPostInsert = inDocIdx === 3 || lower.includes('แทรกใหม่รอบที่ 3') || lower.includes('โหนดใหม่');
      return {
        title: isPostInsert
          ? '🌲 Binary Search Tree: การแทรกเลข 5 สำเร็จที่รอบ 3 (Insertion Tracing)'
          : '🌲 Binary Search Tree: โครงสร้างก่อนแทรกเลข 5 (Candidate Tree)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 540 280" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="42" x2="160" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="42" x2="380" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="100" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="105" x2="220" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="220" y1="170" x2="180" y2="235" stroke="#334155" stroke-width="2.5" />
              ${isPostInsert ? '<line x1="220" y1="170" x2="260" y2="235" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 4" />' : ''}

              <circle cx="270" cy="42" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="47" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">6</text>
              <text x="270" y="16" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Root</text>

              <circle cx="160" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="110" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">2</text>
              ${isPostInsert ? '<text x="160" y="78" fill="#4fd1e8" font-family="\'JetBrains Mono\', monospace" font-size="9.5" text-anchor="middle">5 &lt; 6 (L)</text>' : ''}

              <circle cx="380" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="380" y="110" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">8</text>

              <circle cx="100" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="100" y="175" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">1</text>

              <circle cx="220" cy="170" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" />
              <text x="220" y="175" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">4</text>
              ${isPostInsert ? '<text x="220" y="142" fill="#f59e0b" font-family="\'JetBrains Mono\', monospace" font-size="9.5" text-anchor="middle">5 &gt; 2 (R)</text>' : ''}

              <circle cx="180" cy="235" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="180" y="240" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">3</text>

              ${isPostInsert ? `
                <circle cx="260" cy="235" r="20" fill="#064e3b" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" />
                <text x="260" y="240" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="800" text-anchor="middle">5</text>
                <text x="260" y="270" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" text-anchor="middle">✨ โหนดใหม่</text>
              ` : ''}
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">
                ${isPostInsert ? '🎯 Round 1: 5 &lt; 6 (ซ้าย) ➔ Round 2: 5 &gt; 2 (ขวา) ➔ Round 3: 5 &gt; 4 (ขวาว่าง ➔ แทรก 5 สำเร็จ!)' : '📌 เตรียมแทรกค่า 5: จะเปรียบเทียบจาก Root 6 ➔ 2 ➔ 4 เพื่อหาตำแหน่งใบที่ว่าง'}
              </span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 28. BST 3 DELETION CASES (Chapter 05.3 - Diagram 1)
    // =========================================================================
    if ((dId.includes('05.3') && inDocIdx === 1) || (lower.includes('checkchild') && lower.includes('case 1: leaf'))) {
      return {
        title: '✂️ BST Deletion: สรุปภาพรวม 3 กรณีการลบโหนด (Leaf, Single Child, Two Children)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:16px;">
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;margin-bottom:6px;">Case 1: Leaf Node</div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:10px;">0 Child (ไม่มีลูกเลย)</div>
                <div style="background:rgba(16,185,129,0.1);padding:10px;border-radius:6px;font-size:13px;color:#e2e8f0;">
                  ตัดโหนดใบออกได้ทันทีโดยสั่งให้ Pointer แม่ชี้เป็น <b>None</b>
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;margin-bottom:6px;">Case 2: Single Child</div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:10px;">1 Child (มีลูกข้างเดียว ซ้ายหรือขวา)</div>
                <div style="background:rgba(79,209,232,0.1);padding:10px;border-radius:6px;font-size:13px;color:#e2e8f0;">
                  Bypass ข้าม: ดึงโหนดลูกขึ้นมาต่อกับโหนดแม่แทนตำแหน่งเดิมทันที
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:15px;margin-bottom:6px;">Case 3: Two Children</div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:10px;">2 Children (มีลูกครบสองข้าง)</div>
                <div style="background:rgba(245,158,11,0.1);padding:10px;border-radius:6px;font-size:13px;color:#e2e8f0;">
                  หา <b>Inorder Successor</b> (ค่าน้อยสุดในกิ่งขวา) คัดลอกค่ามาทับ แล้วลบโหนด Successor เดิมออก
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 29. BST DELETION CASE 1 LEAF NODE (Chapter 05.3 - Diagram 2)
    // =========================================================================
    if ((dId.includes('05.3') && inDocIdx === 2) || (lower.includes('beforedelete') && lower.includes('afterdelete') && lower.includes('ก๊อปปี้ 5 มาแทน'))) {
      return {
        title: '✂️ BST Deletion Case 1: การลบโหนดและกระบวนการแทนที่ด้วย Successor (Before vs After)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1px solid #334155;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f87171;font-size:14px;margin-bottom:8px;">1. ก่อนลบ: โหนด 4 ต้องการลบ (เป้าหมาย)</div>
                <svg viewBox="0 0 260 170" style="width:100%;max-width:260px;">
                  <line x1="130" y1="26" x2="65" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="130" y1="26" x2="195" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="65" y1="70" x2="35" y2="120" stroke="#334155" stroke-width="2" />
                  <line x1="65" y1="70" x2="95" y2="120" stroke="#334155" stroke-width="2" />
                  <circle cx="130" cy="26" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="130" y="30" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">6</text>
                  <circle cx="65" cy="70" r="17" fill="rgba(239,68,68,0.25)" stroke="#ef4444" stroke-width="2.5" /><text x="65" y="74" fill="#fca5a5" font-size="12" font-weight="700" text-anchor="middle">4 ✂️</text>
                  <circle cx="195" cy="70" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="195" y="74" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">7</text>
                  <circle cx="35" cy="120" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="35" y="124" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="95" cy="120" r="14" fill="#064e3b" stroke="#10b981" stroke-width="2" /><text x="95" y="124" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">5 ⭐</text>
                </svg>
                <div style="font-size:11.5px;color:#94a3b8;margin-top:6px;">Inorder Successor คือ 5 (ค่าน้อยสุดในกิ่งขวา)</div>
              </div>
              <div style="background:#181a26;border:1px solid #10b981;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#34d399;font-size:14px;margin-bottom:8px;">2. หลังลบ: นำ Successor 5 มาแทนตำแหน่ง 4</div>
                <svg viewBox="0 0 260 170" style="width:100%;max-width:260px;">
                  <line x1="130" y1="26" x2="65" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="130" y1="26" x2="195" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="65" y1="70" x2="35" y2="120" stroke="#334155" stroke-width="2" />
                  <circle cx="130" cy="26" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="130" y="30" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">6</text>
                  <circle cx="65" cy="70" r="17" fill="#064e3b" stroke="#10b981" stroke-width="2.5" /><text x="65" y="74" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">5</text>
                  <circle cx="195" cy="70" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="195" y="74" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">7</text>
                  <circle cx="35" cy="120" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="35" y="124" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">3</text>
                </svg>
                <div style="font-size:11.5px;color:#34d399;margin-top:6px;">ก๊อปปี้ค่า 5 มาแทน แล้วลบโหนดใบ 5 เดิมทิ้ง (Case 1)</div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 30. BST DELETION CASE 2 SINGLE CHILD (Chapter 05.3 - Diagram 3)
    // =========================================================================
    if ((dId.includes('05.3') && inDocIdx === 3) || (lower.includes('4 (โหนดที่ต้องการลบ)') && lower.includes('3 (ลูกซ้าย)'))) {
      return {
        title: '✂️ BST Deletion Case 2: ลบโหนดที่มีลูกเดี่ยว (Single Child Bypass Pointer)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 480 220" style="width:100%;max-width:480px;">
              ${svgDefs}
              <line x1="240" y1="36" x2="150" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="240" y1="36" x2="330" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="150" y1="85" x2="100" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="150" y1="85" x2="200" y2="135" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 4" />
              <line x1="200" y1="135" x2="160" y2="185" stroke="#334155" stroke-width="2" />
              <path d="M 150 100 Q 130 150 160 175" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" stroke-dasharray="4 4" />

              <circle cx="240" cy="36" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="240" y="41" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">6</text>
              <circle cx="330" cy="85" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="330" y="90" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">8</text>
              <circle cx="150" cy="85" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="150" y="90" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">2</text>
              <circle cx="100" cy="135" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="100" y="139" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">1</text>

              <circle cx="200" cy="135" r="18" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="2.5" />
              <text x="200" y="140" fill="#f87171" font-weight="700" font-size="13" text-anchor="middle">4 ✂️</text>

              <circle cx="160" cy="185" r="18" fill="#064e3b" stroke="#10b981" stroke-width="2.5" filter="url(#dsa-glow-emerald)" />
              <text x="160" y="190" fill="#34d399" font-weight="800" font-size="13" text-anchor="middle">3</text>
              <text x="160" y="212" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">ลูกเดี่ยว (Bypassed)</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">✂️ Case 2 (Single Child): ลบโหนด 4 ที่มีลูกซ้ายคือ 3 เพียงตัวเดียว ให้พอยน์เตอร์ขวาของโหนด 2 ชี้ข้าม (Bypass) ไปที่โหนด 3 ทันที</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 31 & 32. BST CASE 3 TWO CHILDREN (Chapter 05.3 - Diagrams 4 & 5)
    // =========================================================================
    if ((dId.includes('05.3') && (inDocIdx === 4 || inDocIdx === 5)) || (lower.includes('successor candidate') || lower.includes('successor ถูกยกขึ้นมาแทน 2') || (lower.includes('n3_new') && lower.includes('n6["6 (root)"]')))) {
      const isFinal = inDocIdx === 5 || lower.includes('n3_new') || lower.includes('สำเร็จ');
      return {
        title: isFinal
          ? '🎉 BST Case 3 Success: ยก Inorder Successor (3) ขึ้นมาแทนตำแหน่ง 2 สำเร็จ 100%'
          : '🔍 BST Case 3: ขั้นตอนค้นหา Inorder Successor (ค่าน้อยที่สุดในกิ่งขวา min_node(node.right))',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 540 260" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="36" x2="160" y2="95" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="36" x2="380" y2="95" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="95" x2="110" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="95" x2="220" y2="160" stroke="#334155" stroke-width="2.5" />
              <line x1="220" y1="160" x2="260" y2="220" stroke="#334155" stroke-width="2.5" />

              <circle cx="270" cy="36" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="270" y="41" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">6</text>
              <circle cx="380" cy="95" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="380" y="100" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">8</text>
              <circle cx="110" cy="160" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="110" y="164" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">1</text>

              ${isFinal ? `
                <circle cx="160" cy="95" r="22" fill="#064e3b" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" />
                <text x="160" y="100" fill="#fff" font-weight="800" font-size="16" text-anchor="middle">3</text>
                <text x="160" y="68" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">Successor Promoted</text>
                <circle cx="220" cy="160" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="220" y="165" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">5</text>
                <circle cx="260" cy="220" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="260" y="224" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">4</text>
              ` : `
                <circle cx="160" cy="95" r="20" fill="rgba(239,68,68,0.15)" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 4" />
                <text x="160" y="100" fill="#f87171" font-weight="700" font-size="14" text-anchor="middle">2 ❌</text>
                <circle cx="220" cy="160" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="220" y="165" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">5</text>
                <circle cx="260" cy="220" r="20" fill="#181a26" stroke="#10b981" stroke-width="2.8" filter="url(#dsa-glow-emerald)" />
                <text x="260" y="225" fill="#34d399" font-weight="800" font-size="14" text-anchor="middle">3 ⭐</text>
                <text x="260" y="252" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">Inorder Successor</text>
              `}
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">
                ${isFinal ? '🎉 ลบโหนด 2 สำเร็จ: ค่า 3 ขึ้นมาเป็นรากของซับทรีย์ซ้าย คงกฎ BST Left &lt; Root &lt; Right อย่างสมบูรณ์' : '🔍 Inorder Successor คือค่าน้อยที่สุดในกิ่งขวาของโหนดที่ต้องการลบ (เดินขวา 1 ก้าวแล้วเดินซ้ายสุดสาย)'}
              </span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 33. OPEN ADDRESSING STRATEGIES (Chapter 06.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('06.1') && inDocIdx === 1) || (lower.includes('open addressing strategies') || (lower.includes('primary clustering') && lower.includes('double hashing')))) {
      return {
        title: '🔑 Open Addressing: กลยุทธ์การแก้การชน 3 รูปแบบ (Linear, Quadratic, Double Hashing)',
        topicHash: '#hash',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:16px;">
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:15px;margin-bottom:6px;">1. Linear Probing</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#fbbf24;margin-bottom:8px;">h(k, i) = (h(k) + i) mod M</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.5;">
                  เดินหน้าทีละ 1 ช่องถัดไปเสมอ<br/>
                  <b style="color:#ef4444;">ข้อเสีย:</b> เกิด <b>Primary Clustering</b> (ข้อมูลเกาะกันเป็นแถวยาว ยิ่งชนยิ่งช้า)
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;margin-bottom:6px;">2. Quadratic Probing</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#38bdf8;margin-bottom:8px;">h(k, i) = (h(k) + i²) mod M</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.5;">
                  ก้าวกระโดดด้วยกำลังสอง (+1, +4, +9, ...)<br/>
                  <b style="color:#34d399;">ข้อดี:</b> แก้ Primary Clustering ได้<br/>
                  <span style="color:#94a3b8;">แต่อาจเกิด Secondary Clustering</span>
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;margin-bottom:6px;">3. Double Hashing</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#34d399;margin-bottom:8px;">h(k, i) = (h₁(k) + i · h₂(k)) mod M</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.5;">
                  ใช้ 2 ฟังก์ชันแฮช ระยะก้าวขึ้นกับค่า Key<br/>
                  <b style="color:#34d399;">ยอดเยี่ยมที่สุด:</b> ขจัด Clustering ทั้งปวงได้อย่างหมดจด!
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 34 & 35 & 47. BINARY MIN-HEAP & ARRAY INDEXING (Chapter 07.1 & 11.6)
    // =========================================================================
    if ((dId.includes('07.1') && (inDocIdx === 1 || inDocIdx === 2)) || (dId.includes('11.6') && inDocIdx === 3) || (lower.includes('h13["[1] 13 (root)"]') || lower.includes('root["13 (min-heap root') || (lower.includes('n1["[1] 13"]') && lower.includes('n10["[10] 32"]')))) {
      const isSimple = (dId.includes('07.1') && inDocIdx === 1) || lower.includes('root["13 (min-heap root');
      return {
        title: isSimple
          ? '⚡ Binary Min-Heap: Complete Binary Tree Invariant (Root ≤ Children)'
          : '⚡ Binary Min-Heap: Complete Binary Tree & 1-Based Array Indexing',
        topicHash: '#heap',
        html: `
          <div class="dsa-native-heap-wrap">
            <svg viewBox="0 0 760 300" style="width:100%;max-width:760px;">
              ${svgDefs}
              <!-- Branches -->
              <line x1="380" y1="40" x2="200" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="40" x2="560" y2="105" stroke="#334155" stroke-width="2.5" />
              <line x1="200" y1="105" x2="110" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="200" y1="105" x2="290" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="560" y1="105" x2="470" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="560" y1="105" x2="650" y2="170" stroke="#334155" stroke-width="2.5" />
              <line x1="110" y1="170" x2="70" y2="235" stroke="#334155" stroke-width="2.5" />
              <line x1="110" y1="170" x2="150" y2="235" stroke="#334155" stroke-width="2.5" />
              <line x1="290" y1="170" x2="250" y2="235" stroke="#334155" stroke-width="2.5" />

              <!-- Nodes -->
              <circle cx="380" cy="40" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" /><text x="380" y="45" fill="#fff" font-weight="800" font-size="15" text-anchor="middle">13</text><text x="380" y="15" fill="#f59e0b" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">[1] Root</text>
              <circle cx="200" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="200" y="110" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">21</text><text x="200" y="80" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">[2]</text>
              <circle cx="560" cy="105" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="560" y="110" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">16</text><text x="560" y="80" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">[3]</text>
              <circle cx="110" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="110" y="174" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">24</text><text x="110" y="148" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[4]</text>
              <circle cx="290" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="290" y="174" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">31</text><text x="290" y="148" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[5]</text>
              <circle cx="470" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="470" y="174" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">19</text><text x="470" y="148" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[6]</text>
              <circle cx="650" cy="170" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="650" y="174" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">68</text><text x="650" y="148" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[7]</text>
              <circle cx="70" cy="235" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="70" y="239" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">65</text><text x="70" y="215" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="8.5" text-anchor="middle">[8]</text>
              <circle cx="150" cy="235" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="150" y="239" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">26</text><text x="150" y="215" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="8.5" text-anchor="middle">[9]</text>
              <circle cx="250" cy="235" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="250" y="239" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">32</text><text x="250" y="215" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="8.5" text-anchor="middle">[10]</text>
            </svg>

            <!-- Array Indexing Bar -->
            <div style="margin-top:14px;">
              <div style="font-size:12px;font-weight:700;color:#a5b4fc;margin-bottom:6px;font-family:'Chakra Petch',sans-serif;">
                📦 1-Based Array Memory Layout:
              </div>
              <div style="display:flex;gap:4px;overflow-x:auto;padding-bottom:6px;">
                <div class="dsa-heap-cell" style="opacity:0.35;"><span class="cell-idx">[0]</span><span class="cell-val">-</span></div>
                <div class="dsa-heap-cell root-cell"><span class="cell-idx">[1]</span><span class="cell-val">13</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[2]</span><span class="cell-val">21</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[3]</span><span class="cell-val">16</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[4]</span><span class="cell-val">24</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[5]</span><span class="cell-val">31</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[6]</span><span class="cell-val">19</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[7]</span><span class="cell-val">68</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[8]</span><span class="cell-val">65</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[9]</span><span class="cell-val">26</span></div>
                <div class="dsa-heap-cell"><span class="cell-idx">[10]</span><span class="cell-val">32</span></div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚡ สูตรคำนวณ 1-Based Array: ลูกซ้าย = <code>2 * i</code> | ลูกขวา = <code>2 * i + 1</code> | โหนดพ่อ = <code>i // 2</code> รวดเร็วระดับ O(1) โดยไม่ต้องพึ่งพอยน์เตอร์</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 36. 5 SORTING ALGORITHMS TAXONOMY (Chapter 08.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('08.1') && inDocIdx === 1) || (lower.includes('sorting algorithms') && (lower.includes('bubble sort') || lower.includes('simplesorts')))) {
      return {
        title: '🔀 Sorting Algorithms Taxonomy: Elementary O(N²) vs Divide-and-Conquer O(N log N)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#f59e0b;font-weight:700;font-size:15px;margin-bottom:10px;">
                  1. Elementary Sorts: O(N²)
                </div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:#c7cad6;">
                  <div style="background:#20222c;padding:8px 12px;border-radius:6px;border-left:3px solid #f59e0b;">
                    <b>Bubble Sort</b>: สลับคู่ที่ติดกัน ลอยตัวมากสุดไปขวาสุด (O(N) Best เมื่อเกือบเรียง)
                  </div>
                  <div style="background:#20222c;padding:8px 12px;border-radius:6px;border-left:3px solid #f59e0b;">
                    <b>Selection Sort</b>: หาค่าน้อยสุดมาสลับกับตำแหน่งแรกเสมอ (ทำ N-1 รอบเสมอ)
                  </div>
                  <div style="background:#20222c;padding:8px 12px;border-radius:6px;border-left:3px solid #f59e0b;">
                    <b>Insertion Sort</b>: หยิบทีละตัวแล้วแทรกในส่วนที่เรียงแล้ว (มีประสิทธิภาพสูงกับ N ขนาดเล็ก)
                  </div>
                </div>
              </div>

              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:15px;margin-bottom:10px;">
                  2. Divide-and-Conquer: O(N log N)
                </div>
                <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:#c7cad6;">
                  <div style="background:#20222c;padding:8px 12px;border-radius:6px;border-left:3px solid #10b981;">
                    <b>Merge Sort</b>: แบ่งครึ่งซ้ายขวาแล้วผสานกลับ (Stable 100%, ใช้ Extra Space O(N))
                  </div>
                  <div style="background:#20222c;padding:8px 12px;border-radius:6px;border-left:3px solid #10b981;">
                    <b>Quick Sort</b>: เลือก Pivot แบ่งพาร์ติชัน (In-place, เร็วที่สุดในทางปฏิบัติ Worst O(N²))
                  </div>
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 37 & 40. GRAPH REPRESENTATION (DIRECTED & UNDIRECTED) (Chapter 09.1 - Diagrams 1 & 4)
    // =========================================================================
    if ((dId.includes('09.1') && (inDocIdx === 1 || inDocIdx === 4)) || (lower.includes('subgraph digraph') || (lower.includes('a --- b') && lower.includes('b --- c')))) {
      const isDirected = inDocIdx === 1 || lower.includes('digraph') || lower.includes('-->');
      return {
        title: isDirected
          ? '🕸️ Directed Graph (Digraph) Architecture Model'
          : '🕸️ Undirected Graph Architecture Model (Cycle A-B-C-D)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 460 180" style="width:100%;max-width:460px;">
              ${svgDefs}
              ${isDirected ? `
                <line x1="120" y1="60" x2="240" y2="60" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <line x1="120" y1="60" x2="180" y2="130" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <line x1="240" y1="60" x2="180" y2="130" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <circle cx="120" cy="60" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="120" y="65" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">A</text>
                <circle cx="240" cy="60" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="240" y="65" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">B</text>
                <circle cx="180" cy="130" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="180" y="135" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">C</text>
              ` : `
                <line x1="140" y1="40" x2="280" y2="40" stroke="#10b981" stroke-width="2.5" />
                <line x1="280" y1="40" x2="280" y2="140" stroke="#10b981" stroke-width="2.5" />
                <line x1="280" y1="140" x2="140" y2="140" stroke="#10b981" stroke-width="2.5" />
                <line x1="140" y1="140" x2="140" y2="40" stroke="#10b981" stroke-width="2.5" />
                <circle cx="140" cy="40" r="18" fill="#181a26" stroke="#10b981" stroke-width="2.2" /><text x="140" y="45" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">A</text>
                <circle cx="280" cy="40" r="18" fill="#181a26" stroke="#10b981" stroke-width="2.2" /><text x="280" y="45" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">B</text>
                <circle cx="280" cy="140" r="18" fill="#181a26" stroke="#10b981" stroke-width="2.2" /><text x="280" y="145" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">C</text>
                <circle cx="140" cy="140" r="18" fill="#181a26" stroke="#10b981" stroke-width="2.2" /><text x="140" y="145" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">D</text>
              `}
            </svg>
          </div>
        `
      };
    }

    // =========================================================================
    // 38. BFS VS DFS TRAVERSALS (Chapter 09.1 - Diagram 2)
    // =========================================================================
    if ((dId.includes('09.1') && inDocIdx === 2) || (lower.includes('graph traversals') && lower.includes('queueused') && lower.includes('stackused'))) {
      return {
        title: '🔄 Graph Traversals: BFS (Queue) vs DFS (Stack / Recursion)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:8px;">1. Breadth-First Search (BFS)</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.6;">
                  • <b>Data Structure:</b> ใช้ <b>Queue (FIFO)</b><br/>
                  • <b>พฤติกรรม:</b> กระจายตัวสำรวจทีละระดับชั้นความกว้าง (Level-by-level)<br/>
                  • <b>ประโยชน์:</b> หา Shortest Path ในกราฟที่น้ำหนักทุกเส้นเท่ากัน (Unweighted) ได้สมบูรณ์แบบ
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#f59e0b;font-weight:700;font-size:15px;margin-bottom:8px;">2. Depth-First Search (DFS)</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.6;">
                  • <b>Data Structure:</b> ใช้ <b>Stack (LIFO)</b> หรือ Call Stack Recursion<br/>
                  • <b>พฤติกรรม:</b> พุ่งเจาะลึกลงไปตามกิ่งจนสุดสายก่อนย้อนกลับ (Backtracking)<br/>
                  • <b>ประโยชน์:</b> ตรวจจับ Cycle, หา Connected Components และ Topological Sort
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 39 & 41. TOPOLOGICAL SORT (Chapter 09.1 - Diagrams 3 & 5)
    // =========================================================================
    if ((dId.includes('09.1') && (inDocIdx === 3 || inDocIdx === 5)) || (lower.includes('cs101') && lower.includes('cs201')) || (lower.includes('v1["v1 (in=0)"]') && lower.includes('v7["v7"]'))) {
      const isCourseDAG = inDocIdx === 3 || lower.includes('cs101');
      return {
        title: isCourseDAG
          ? '🔀 Topological Sort: แบบจำลองเงื่อนไขวิชาบังคับก่อน (Course Prerequisite DAG)'
          : '🔀 Topological Sort: 7-Node DAG & Indegree Array Tracing',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 560 180" style="width:100%;max-width:560px;">
              ${svgDefs}
              <line x1="80" y1="60" x2="220" y2="60" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="80" y1="60" x2="220" y2="120" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="220" y1="60" x2="380" y2="90" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="220" y1="120" x2="380" y2="90" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />

              <circle cx="80" cy="60" r="22" fill="#181a26" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" />
              <text x="80" y="65" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">${isCourseDAG ? 'CS101' : 'v1'}</text>
              <text x="80" y="32" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">In=0 (เริ่ม)</text>

              <circle cx="220" cy="60" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="220" y="65" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">${isCourseDAG ? 'CS102' : 'v2'}</text>

              <circle cx="220" cy="120" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="220" y="125" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">${isCourseDAG ? 'Math' : 'v3'}</text>

              <circle cx="380" cy="90" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" />
              <text x="380" y="95" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">${isCourseDAG ? 'CS201' : 'v4'}</text>
              <text x="380" y="125" fill="#fbbf24" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">In=2 (รอ 2 ตัว)</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 กฎเหล็ก: Topological Sort ทำได้เฉพาะบน <b>DAG (Directed Acyclic Graph)</b> เท่านั้น หากกราฟมี Cycle จะไม่สามารถจัดลำดับได้</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 42. SHORTEST PATH OVERVIEW (Chapter 10.1 - Diagram 1)
    // =========================================================================
    if ((dId.includes('10.1') && inDocIdx === 1) || (lower.includes('shortestpathalg') && lower.includes('unweighted') && lower.includes('dijkstra_alg'))) {
      return {
        title: '🗺️ Shortest Path Algorithms Overview: Unweighted (BFS) vs Weighted (Dijkstra)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:8px;">1. Unweighted Shortest Path</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.6;">
                  • <b>Algorithm:</b> ใช้ <b>BFS (Breadth-First Search)</b><br/>
                  • <b>ความซับซ้อน:</b> <b>O(V + E)</b> เร็วที่สุดและประหยัดที่สุด<br/>
                  • <b>แนวคิด:</b> ทุก Edge มีค่าใช้จ่ายเท่ากับ 1 ขยายวงออกไปทีละชั้น
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:15px;margin-bottom:8px;">2. Weighted Shortest Path (Dijkstra)</div>
                <div style="font-size:12.5px;color:#c7cad6;line-height:1.6;">
                  • <b>Algorithm:</b> <b>Dijkstra's Algorithm</b> ร่วมกับ Min-Heap<br/>
                  • <b>ความซับซ้อน:</b> <b>O((V + E) log V)</b><br/>
                  • <b>เงื่อนไข:</b> น้ำหนักทุกเส้นต้องไม่ติดลบ (w ≥ 0)
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 43. DIJKSTRA STATE MACHINE FLOWCHART (Chapter 10.1 - Diagram 2)
    // =========================================================================
    if ((dId.includes('10.1') && inDocIdx === 2) || (lower.includes('dist[source]=0') && lower.includes('relaxation'))) {
      return {
        title: '🗺️ Dijkstra Algorithm State Machine: กระบวนการทำงาน 5 ขั้นตอน',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:10px;align-items:stretch;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#4fd1e8;font-weight:700;font-size:13px;margin-bottom:4px;">1. Initialize</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">dist[src]=0<br/>dist[v]=∞<br/>visited=set()<br/>push (0, src) เข้า PQ</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#f59e0b;font-weight:700;font-size:13px;margin-bottom:4px;">2. Pop Min</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">ดึงโหนด u ที่มีค่า dist[u] น้อยสุดออกจาก Min-Heap</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #b794f6;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#b794f6;font-weight:700;font-size:13px;margin-bottom:4px;">3. Visited Check</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">ถ้า u เคยแวะแล้ว ➔ ข้าม<br/>ถ้ายังไม่แวะ ➔ เพิ่ม u เข้า visited set</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#10b981;font-weight:700;font-size:13px;margin-bottom:4px;">4. Relaxation</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">สำหรับเพื่อนบ้าน v:<br/>ถ้า dist[u]+w &lt; dist[v]:<br/>dist[v] = dist[u]+w<br/>push (dist[v], v)</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #38bdf8;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#38bdf8;font-weight:700;font-size:13px;margin-bottom:4px;">5. Terminate</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">ทำซ้ำจน Priority Queue ว่างเปล่า<br/>ได้ตาราง Shortest Path ครบทุกโหนด</div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🗺️ Dijkstra State Machine: ใช้หลักการ Greedy ร่วมกับ Min-Heap ให้ความเร็ว O((V + E) log V) สำหรับกราฟถ่วงน้ำหนักบวกทุกเส้น</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 44. DIJKSTRA 7-VERTEX GRAPH MODEL (Chapter 10.1 - Diagram 3)
    // =========================================================================
    if ((dId.includes('10.1') && inDocIdx === 3) || (lower.includes('v3["v3 (start)"]') && lower.includes('v1["v1"]'))) {
      return {
        title: '🗺️ Shortest Path: กราฟ 7 โหนดพร้อมเส้นทางเชื่อมต่อ (Start ที่ v3)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 620 280" style="width:100%;max-width:620px;">
              ${svgDefs}
              <line x1="160" y1="60" x2="300" y2="60" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="160" y1="60" x2="230" y2="150" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="300" y1="60" x2="230" y2="150" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="300" y1="60" x2="450" y2="60" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="80" y1="150" x2="160" y2="60" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" />
              <line x1="80" y1="150" x2="230" y2="240" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" />
              <line x1="230" y1="150" x2="80" y2="150" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="230" y1="150" x2="230" y2="240" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="230" y1="150" x2="450" y2="60" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="230" y1="150" x2="390" y2="210" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="450" y1="60" x2="390" y2="210" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="390" y1="210" x2="230" y2="240" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />

              <circle cx="160" cy="60" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="160" y="65" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v1</text>
              <circle cx="300" cy="60" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="300" y="65" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v2</text>
              <circle cx="80" cy="150" r="22" fill="#064e3b" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" /><text x="80" y="155" fill="#fff" font-weight="800" font-size="14" text-anchor="middle">v3</text>
              <text x="80" y="122" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">Start (v3)</text>
              <circle cx="230" cy="150" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="230" y="155" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v4</text>
              <circle cx="450" cy="60" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="450" y="65" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v5</text>
              <circle cx="230" cy="240" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="230" y="245" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v6</text>
              <circle cx="390" cy="210" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="390" y="215" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v7</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🗺️ กราฟ 7 โหนดพร้อมเส้นทางเชื่อมต่อ (Start ที่ v3): Dijkstra จะสำรวจเพื่อนบ้าน (v1 และ v6) แล้วอัปเดตระยะทางที่สั้นที่สุดตามลำดับ Priority Queue</span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 45. FINAL EXAM 5 TRAPS MINDMAP (Chapter 11.6 - Diagram 1)
    // =========================================================================
    if ((dId.includes('11.6') && inDocIdx === 1) || (lower.includes('กับดักข้อสอบปลายภาค') || (lower.includes('mindmap') && lower.includes('trap 1')))) {
      return {
        title: '🚨 5 กับดักข้อสอบปลายภาคและจุดเน้นคะแนนจากอาจารย์ (Classroom Traps)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:14px;">
              <div style="background:#181a26;border:1.5px solid #ef4444;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f87171;font-size:15px;margin-bottom:6px;">Trap 1: การนับ Collision</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;line-height:1.6;">
                  ห้ามนับรอบ Resolve รวม! ชน 7 ครั้ง แก้ 7 ครั้ง ตอบ <b>7 ครั้ง</b> เท่านั้น ตอบ 14 ได้ 0 คะแนนทันที
                </p>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#fbbf24;font-size:15px;margin-bottom:6px;">Trap 2: Wrap Around Modulo</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;line-height:1.6;">
                  สูตร Probing ต้องใส่ <code>mod TableSize</code> เสมอ เช่น <code>(h + i²) mod TableSize</code> ห้ามลืม!
                </p>
              </div>
              <div style="background:#181a26;border:1.5px solid #b794f6;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#c084fc;font-size:15px;margin-bottom:6px;">Trap 3: พารามิเตอร์ R ใน Double Hash</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;line-height:1.6;">
                  สูตรก้าวคือ <code>h₂(k) = R - (k mod R)</code> โดยที่ <b>R ต้องเป็น Prime ที่น้อยกว่า TableSize</b>
                </p>
              </div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#38bdf8;font-size:15px;margin-bottom:6px;">Trap 4: 1-Based Heap Array</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;line-height:1.6;">
                  ข้อสอบอาจารย์ใช้ช่อง <code>[0]</code> เป็นตัวว่าง Root เริ่มที่ Index 1 เสมอ: ซ้าย <code>2*i</code>, ขวา <code>2*i+1</code>
                </p>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#34d399;font-size:15px;margin-bottom:6px;">Trap 5: Dijkstra Tracing</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;line-height:1.6;">
                  ต้องแสดงตารางคอลัมน์ <b>v, Known, d_v, p_v</b> ครบทุกสเต็ป และเลือกโหนด d_v น้อยสุดในแถวที่ยังไม่ Known เสมอ
                </p>
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 46. LINEAR PROBING COLLISION COUNT TRAP (Chapter 11.6 - Diagram 2)
    // =========================================================================
    if ((dId.includes('11.6') && inDocIdx === 2) || (lower.includes('hash_simulation') || (lower.includes('89 mod 10 = 9') && lower.includes('49 mod 10 = 9') && lower.includes('58 mod 10 = 8')))) {
      return {
        title: '🔑 Final Exam Simulation: การนับจำนวน Collision ที่ถูกต้อง (Total = 7 Collisions)',
        topicHash: '#hash',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;gap:6px;overflow-x:auto;padding:12px 2px;">
              <div class="dsa-heap-cell" style="border-color:#10b981;"><span class="cell-idx">[0]</span><span class="cell-val">49</span></div>
              <div class="dsa-heap-cell" style="border-color:#10b981;"><span class="cell-idx">[1]</span><span class="cell-val">58</span></div>
              <div class="dsa-heap-cell" style="border-color:#10b981;"><span class="cell-idx">[2]</span><span class="cell-val">69</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[3]</span><span class="cell-val" style="color:#64748b;">-</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[4]</span><span class="cell-val" style="color:#64748b;">-</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[5]</span><span class="cell-val" style="color:#64748b;">-</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[6]</span><span class="cell-val" style="color:#64748b;">-</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[7]</span><span class="cell-val" style="color:#64748b;">-</span></div>
              <div class="dsa-heap-cell" style="border-color:#4fd1e8;"><span class="cell-idx">[8]</span><span class="cell-val">18</span></div>
              <div class="dsa-heap-cell root-cell"><span class="cell-idx">[9]</span><span class="cell-val">89</span></div>
            </div>
            <div style="margin-top:14px;background:#181a26;border:1px solid #334155;border-radius:10px;padding:14px;font-size:13px;line-height:1.7;">
              • แทรก 89: 89 mod 10 = 9 (ว่าง) ➔ <b>ชน 0 ครั้ง</b><br/>
              • แทรก 18: 18 mod 10 = 8 (ว่าง) ➔ <b>ชน 0 ครั้ง</b><br/>
              • แทรก 49: 49 mod 10 = 9 (ชน 89) ➔ วนไปช่อง 0 ว่าง ➔ <b>ชน 1 ครั้ง</b><br/>
              • แทรก 58: 58 mod 10 = 8 (ชน 18, ชน 89 ที่ช่อง 9, ชน 49 ที่ช่อง 0) ➔ ลงช่อง 1 ➔ <b>ชน 3 ครั้ง</b><br/>
              • แทรก 69: 69 mod 10 = 9 (ชน 89 ที่ช่อง 9, ชน 49 ที่ช่อง 0, ชน 58 ที่ช่อง 1) ➔ ลงช่อง 2 ➔ <b>ชน 3 ครั้ง</b><br/>
              <div style="margin-top:8px;padding-top:8px;border-top:1px dashed #334155;font-weight:700;color:#34d399;font-size:14px;">
                🎯 สรุปผลรวมจำนวนครั้งที่เกิด Collision = 0 + 0 + 1 + 3 + 3 = 7 ครั้งบริบูรณ์!
              </div>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // 48. FINAL EXAM DIJKSTRA GRAPH TRACING (Chapter 11.6 - Diagram 4)
    // =========================================================================
    if ((dId.includes('11.6') && inDocIdx === 4) || (lower.includes('v1((v1)) -- 2 --> v2((v2))') || (lower.includes('v1((v1))') && lower.includes('v4((v4))') && lower.includes('v5((v5))')))) {
      return {
        title: '🚀 Dijkstra Shortest Path: กราฟถ่วงน้ำหนักข้อสอบปลายภาค (Source: v1 ➔ Target: v5)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 580 260" style="width:100%;max-width:580px;">
              ${svgDefs}
              <line x1="80" y1="130" x2="200" y2="60" stroke="#34d399" stroke-width="3" marker-end="url(#dsa-arrow-emerald)" />
              <text x="135" y="85" fill="#34d399" font-family="'JetBrains Mono',monospace" font-weight="700" font-size="12">w=2</text>

              <line x1="80" y1="130" x2="240" y2="180" stroke="#334155" stroke-width="2" />
              <text x="150" y="165" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="11">w=4</text>

              <line x1="200" y1="60" x2="240" y2="180" stroke="#34d399" stroke-width="3" marker-end="url(#dsa-arrow-emerald)" />
              <text x="228" y="120" fill="#34d399" font-family="'JetBrains Mono',monospace" font-weight="700" font-size="12">w=3</text>

              <line x1="240" y1="180" x2="380" y2="200" stroke="#34d399" stroke-width="3" marker-end="url(#dsa-arrow-emerald)" />
              <text x="310" y="200" fill="#34d399" font-family="'JetBrains Mono',monospace" font-weight="700" font-size="12">w=2</text>

              <line x1="380" y1="200" x2="480" y2="130" stroke="#34d399" stroke-width="3" marker-end="url(#dsa-arrow-emerald)" />
              <text x="440" y="175" fill="#34d399" font-family="'JetBrains Mono',monospace" font-weight="700" font-size="12">w=5</text>

              <line x1="200" y1="60" x2="480" y2="130" stroke="#334155" stroke-width="1.8" stroke-dasharray="4 4" />
              <text x="340" y="85" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="11">w=10</text>

              <circle cx="80" cy="130" r="22" fill="#064e3b" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" />
              <text x="80" y="135" fill="#fff" font-weight="800" font-size="14" text-anchor="middle">v1</text>
              <text x="80" y="100" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">Start (dist=0)</text>

              <circle cx="200" cy="60" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="200" y="65" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">v2</text>
              <circle cx="240" cy="180" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="240" y="185" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">v4</text>
              <circle cx="380" cy="200" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="380" y="205" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">v3</text>

              <circle cx="480" cy="130" r="22" fill="#831843" stroke="#f43f5e" stroke-width="3" filter="url(#dsa-glow-red)" />
              <text x="480" y="135" fill="#fff" font-weight="800" font-size="14" text-anchor="middle">v5</text>
              <text x="480" y="100" fill="#fda4af" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">Dest (dist=12)</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.4);color:#34d399;">
                🎯 เส้นทางที่สั้นที่สุด: <b>v1 ➔ v2 ➔ v4 ➔ v3 ➔ v5</b> รวมระยะทางต่ำสุด = <b>2 + 3 + 2 + 5 = 12</b> (ชนะเส้นตรง v2 ➔ v5 ที่มี cost 10)
              </span>
            </div>
          </div>
        `
      };
    }

    // =========================================================================
    // UNIVERSAL FALLBACK: HIGH-FIDELITY DSA LAB SVG ENGINE
    // =========================================================================
    return generateGenericDsaLabVisual(code, getArchitectureTitle(code));
  }
'''

    with open('scratch/perfect_engine.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
    print("scratch/perfect_engine.js written successfully.")

if __name__ == '__main__':
    generate_perfect_engine()
