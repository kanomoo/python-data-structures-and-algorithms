# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive DSA Lab visualizer engine for Wiki/app.js
covering all 48 diagrams with 100% precision, zero mermaid dependencies,
and world-class SVG and HTML layouts matching DsaLab standards.
"""
import sys, json, re

def get_engine_code():
    return r'''  // ==========================================================================
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

  function buildNativeDsaVisual(code, docId) {
    const clean = code.trim();
    const lower = clean.toLowerCase();

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

    // -------------------------------------------------------------
    // 1. MASTER DSA KNOWLEDGE MAP (Index)
    // -------------------------------------------------------------
    if (lower.includes('knowledge map') || (lower.includes('linear data structures') && lower.includes('hierarchical structures'))) {
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

    // -------------------------------------------------------------
    // 2. ADT VS DATA STRUCTURE (Chapter 01.1 & 02.1)
    // -------------------------------------------------------------
    if (lower.includes('adt vs data structure') || (lower.includes('abstract data type') && lower.includes('interface') && lower.includes('implementation')) || (lower.includes('adt_concept') && lower.includes('ds_impl'))) {
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

    // -------------------------------------------------------------
    // 3. ASYMPTOTIC NOTATION (Big-O, Big-Omega, Big-Theta) (Chapter 01.1)
    // -------------------------------------------------------------
    if (lower.includes('asymptotic notation') || (lower.includes('big-o') && lower.includes('big-omega') && lower.includes('big-theta'))) {
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

    // -------------------------------------------------------------
    // 4. BIG-O GROWTH RATE HIERARCHY (Chapter 01.1)
    // -------------------------------------------------------------
    if (lower.includes('growth rate') || lower.includes('อัตราการเติบโต') || (lower.includes('o(1)') && lower.includes('o(log n)') && lower.includes('o(n^2)'))) {
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

    // -------------------------------------------------------------
    // 5. PYTHON MEMORY REFERENCE MODEL (Chapter 02.1)
    // -------------------------------------------------------------
    if (lower.includes('ตัวแปรและการอ้างอิงหน่วยความจำ') || (lower.includes('var_a') && lower.includes('var_b') && lower.includes('obj_list'))) {
      return {
        title: '🐍 Python Memory Reference Model (Pointer & Identity in Heap)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:220px 80px 1fr;align-items:center;gap:14px;">
              <div style="background:#181a26;border:1px solid #334155;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#fbbf24;font-weight:700;margin-bottom:8px;">Variable Stack (Name Tag)</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#e2e8f0;display:flex;flex-direction:column;gap:8px;">
                  <div style="padding:6px 10px;background:#20222c;border-radius:6px;border-left:3px solid #4fd1e8;">list_a (0x7f90)</div>
                  <div style="padding:6px 10px;background:#20222c;border-radius:6px;border-left:3px solid #4fd1e8;">list_b = list_a</div>
                </div>
              </div>
              <div style="text-align:center;color:#4fd1e8;font-size:24px;">➔<br/>➔</div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:18px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;margin-bottom:4px;">Shared Heap Memory Object (@ 0x7f90)</div>
                <div style="font-size:12px;color:#94a3b8;margin-bottom:10px;">id(list_a) == id(list_b) is True</div>
                <div style="display:flex;gap:8px;">
                  <div class="dsa-heap-cell" style="width:44px;height:44px;border-color:#4fd1e8;"><span class="cell-val">10</span></div>
                  <div class="dsa-heap-cell" style="width:44px;height:44px;border-color:#4fd1e8;"><span class="cell-val">20</span></div>
                  <div class="dsa-heap-cell" style="width:44px;height:44px;border-color:#4fd1e8;"><span class="cell-val">30</span></div>
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 ใน Python ตัวแปรไม่ใช่กล่องใส่ข้อมูล แต่เป็น "ป้ายชื่อ (Reference)" ที่ชี้ไปยัง Object ก้อนเดียวกันใน Heap Memory</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 6. OOP 4 PILLARS (Chapter 02.1)
    // -------------------------------------------------------------
    if (lower.includes('หลักการ oop 4 ประการ') || (lower.includes('encapsulation') && lower.includes('abstraction') && lower.includes('inheritance') && lower.includes('polymorphism'))) {
      return {
        title: '🏛️ The 4 Pillars of Object-Oriented Programming (OOP Architecture)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:14px;">
              <div style="background:#181a26;border:1px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:6px;">1. Encapsulation</div>
                <div style="font-size:13px;color:#c7cad6;">การห่อหุ้มข้อมูลและเมธอดไว้ด้วยกัน ซ่อนแอตทริบิวต์ภายในด้วย Private Prefix (<code>__data</code>)</div>
              </div>
              <div style="background:#181a26;border:1px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#f59e0b;font-weight:700;font-size:15px;margin-bottom:6px;">2. Abstraction</div>
                <div style="font-size:13px;color:#c7cad6;">การคัดแยกความซับซ้อน แสดงเฉพาะอินเทอร์เฟซที่จำเป็นต่อการใช้งานภายนอก</div>
              </div>
              <div style="background:#181a26;border:1px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:15px;margin-bottom:6px;">3. Inheritance</div>
                <div style="font-size:13px;color:#c7cad6;">การสืบทอดคุณสมบัติจาก Parent Class มายัง Child Class เพื่อลดโค้ดซ้ำซ้อน</div>
              </div>
              <div style="background:#181a26;border:1px solid #b794f6;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#b794f6;font-weight:700;font-size:15px;margin-bottom:6px;">4. Polymorphism</div>
                <div style="font-size:13px;color:#c7cad6;">การมีหลายรูปแบบ เมธอดชื่อเดียวกันในคลาสลูกสามารถทำงานแตกต่างกันได้ (Method Overriding)</div>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 7. OOP CLASS DIAGRAM (Student & Person) (Chapter 02.1)
    // -------------------------------------------------------------
    if (lower.includes('classdiagram') || (lower.includes('student') && lower.includes('person') && lower.includes('gpa'))) {
      return {
        title: '🐍 Python OOP Class & Object Architecture (Inheritance & Static Member)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;justify-content:center;gap:30px;flex-wrap:wrap;align-items:center;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;width:260px;overflow:hidden;">
                <div style="background:rgba(79,209,232,0.15);padding:10px 14px;font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;text-align:center;">Class: Person</div>
                <div style="padding:12px 14px;font-family:'JetBrains Mono',monospace;font-size:12px;color:#c7cad6;border-bottom:1px solid #334155;">
                  + name: str<br/>
                  + age: int
                </div>
                <div style="padding:12px 14px;font-family:'JetBrains Mono',monospace;font-size:12px;color:#4fd1e8;">
                  + get_info(): str
                </div>
              </div>
              <div style="font-size:24px;color:#fbbf24;">▲<br/><span style="font-size:11px;color:#94a3b8;">Inherits</span></div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:12px;width:280px;overflow:hidden;">
                <div style="background:rgba(16,185,129,0.15);padding:10px 14px;font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;text-align:center;">Class: Student (Subclass)</div>
                <div style="padding:12px 14px;font-family:'JetBrains Mono',monospace;font-size:12px;color:#c7cad6;border-bottom:1px solid #334155;">
                  <u>$school_name: str = "KMUTT"</u><br/>
                  + student_id: str<br/>
                  + gpa: float
                </div>
                <div style="padding:12px 14px;font-family:'JetBrains Mono',monospace;font-size:12px;color:#10b981;">
                  + calculate_grade(): str<br/>
                  + get_info(): str (Overridden)
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 <code>school_name</code> มีขีดเส้นใต้หมายถึง <b>Class Attribute (Static Member)</b> ที่ทุก instance ของ Student ใช้งานหน่วยความจำร่วมกัน</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 8. SINGLY LINKED LIST (Chapter 03.1)
    // -------------------------------------------------------------
    if ((lower.includes('singly linked list') && lower.includes('node 1')) || (lower.includes('head') && lower.includes('data: 10') && lower.includes('0x240'))) {
      return {
        title: '🔗 Singly Linked List Memory Model (โครงสร้างพอยน์เตอร์ในหน่วยความจำ)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:12px;overflow-x:auto;padding:12px 4px;">
              <div style="background:#0f172a;border:2px solid #fbbf24;color:#fbbf24;padding:8px 14px;border-radius:8px;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:13px;flex-shrink:0;">
                📍 HEAD<br/><span style="font-size:10px;color:#94a3b8;">0x100</span>
              </div>
              <span style="color:#4fd1e8;font-size:20px;">➔</span>
              <div style="display:flex;border:2px solid #4fd1e8;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;box-shadow:0 0 14px rgba(79,209,232,0.15);">
                <div style="padding:12px 16px;border-right:1px solid #334155;text-align:center;">
                  <div style="font-size:10px;color:#94a3b8;">DATA</div>
                  <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;font-size:16px;color:#fff;">10</div>
                </div>
                <div style="padding:12px 14px;background:rgba(79,209,232,0.08);text-align:center;">
                  <div style="font-size:10px;color:#4fd1e8;">NEXT</div>
                  <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#38bdf8;">0x240</div>
                </div>
              </div>
              <span style="color:#4fd1e8;font-size:20px;">➔</span>
              <div style="display:flex;border:2px solid #4fd1e8;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:12px 16px;border-right:1px solid #334155;text-align:center;">
                  <div style="font-size:10px;color:#94a3b8;">DATA</div>
                  <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;font-size:16px;color:#fff;">20</div>
                </div>
                <div style="padding:12px 14px;background:rgba(79,209,232,0.08);text-align:center;">
                  <div style="font-size:10px;color:#4fd1e8;">NEXT</div>
                  <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#38bdf8;">0x380</div>
                </div>
              </div>
              <span style="color:#4fd1e8;font-size:20px;">➔</span>
              <div style="display:flex;border:2px solid #4fd1e8;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:12px 16px;border-right:1px solid #334155;text-align:center;">
                  <div style="font-size:10px;color:#94a3b8;">DATA</div>
                  <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;font-size:16px;color:#fff;">30</div>
                </div>
                <div style="padding:12px 14px;background:rgba(239,68,68,0.1);text-align:center;">
                  <div style="font-size:10px;color:#f87171;">NEXT</div>
                  <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#fca5a5;">None</div>
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 แต่ละโหนดถูกเก็บกระจัดกระจายใน RAM เชื่อมโยงกันด้วย <code>node.next</code> โหนดสุดท้ายชี้ไปยัง <b>None (NULL)</b></span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 9. DOUBLY LINKED LIST (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('doubly linked list') || (lower.includes('dp1') && lower.includes('dn1') && lower.includes('dp2'))) {
      return {
        title: '🔗 Doubly Linked List Model (แบบจำลองเชื่อมโยงสองทิศทาง)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:12px;overflow-x:auto;padding:12px 4px;">
              <div style="display:flex;border:2px solid #b794f6;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:10px 12px;background:rgba(239,68,68,0.1);font-family:'JetBrains Mono',monospace;font-size:11px;color:#fca5a5;">prev: None</div>
                <div style="padding:10px 16px;border-left:1px solid #334155;border-right:1px solid #334155;font-family:'Chakra Petch',sans-serif;font-weight:700;color:#fff;font-size:16px;">10</div>
                <div style="padding:10px 12px;background:rgba(79,209,232,0.1);font-family:'JetBrains Mono',monospace;font-size:11px;color:#38bdf8;">next: 0x240</div>
              </div>
              <span style="color:#b794f6;font-size:20px;font-weight:700;">⇄</span>
              <div style="display:flex;border:2px solid #b794f6;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:10px 12px;background:rgba(79,209,232,0.1);font-family:'JetBrains Mono',monospace;font-size:11px;color:#38bdf8;">prev: 0x100</div>
                <div style="padding:10px 16px;border-left:1px solid #334155;border-right:1px solid #334155;font-family:'Chakra Petch',sans-serif;font-weight:700;color:#fff;font-size:16px;">20</div>
                <div style="padding:10px 12px;background:rgba(79,209,232,0.1);font-family:'JetBrains Mono',monospace;font-size:11px;color:#38bdf8;">next: 0x380</div>
              </div>
              <span style="color:#b794f6;font-size:20px;font-weight:700;">⇄</span>
              <div style="display:flex;border:2px solid #b794f6;border-radius:10px;overflow:hidden;background:#181a26;flex-shrink:0;">
                <div style="padding:10px 12px;background:rgba(79,209,232,0.1);font-family:'JetBrains Mono',monospace;font-size:11px;color:#38bdf8;">prev: 0x240</div>
                <div style="padding:10px 16px;border-left:1px solid #334155;border-right:1px solid #334155;font-family:'Chakra Petch',sans-serif;font-weight:700;color:#fff;font-size:16px;">30</div>
                <div style="padding:10px 12px;background:rgba(239,68,68,0.1);font-family:'JetBrains Mono',monospace;font-size:11px;color:#fca5a5;">next: None</div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 มีพอยน์เตอร์ 2 ทาง (<code>prev</code> และ <code>next</code>) ทำให้สามารถย้อนกลับ (Reverse Traversal) และลบโหนดได้ในเวลา O(1) เมื่อมี Pointer ชี้ที่ตัวมัน</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 10. CIRCULAR LINKED LIST (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('circular linked list') || (lower.includes('chead') && lower.includes('วนกลับมาชี้ node 1'))) {
      return {
        title: '🔄 Circular Linked List Architecture (โหนดท้ายวนกลับมาชี้ Head)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 620 180" style="width:100%;max-width:620px;">
              ${svgDefs}
              <!-- Nodes -->
              <rect x="130" y="30" width="90" height="50" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="175" y="55" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Node 1 (10)</text>

              <rect x="280" y="30" width="90" height="50" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="325" y="55" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Node 2 (20)</text>

              <rect x="430" y="30" width="90" height="50" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="475" y="55" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Node 3 (30)</text>

              <!-- Forward Arrows -->
              <line x1="20" y1="55" x2="120" y2="55" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#dsa-arrow-amber)" />
              <text x="65" y="44" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">📍 HEAD</text>

              <line x1="220" y1="55" x2="270" y2="55" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="370" y1="55" x2="420" y2="55" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />

              <!-- Circular Loopback Path -->
              <path d="M 475 80 C 475 140, 175 140, 175 90" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="5 5" marker-end="url(#dsa-arrow-emerald)" />
              <text x="325" y="145" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" text-anchor="middle">🔄 next วนลูปกลับมาชี้ Node 1 (ไม่มี None)</text>
            </svg>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 11. INSERT AT HEAD (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('insert at head') || (lower.includes('new_node(5)') && lower.includes('beforeinsert'))) {
      return {
        title: '⚡ Linked List: การแทรกโหนดหน้าสุด (Insert at Head in O(1))',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:16px;">
              <div style="background:#181a26;border:1px solid #334155;border-radius:10px;padding:14px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#fbbf24;font-weight:700;font-size:14px;margin-bottom:8px;">1. สถานะเดิมก่อนแทรก</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#e2e8f0;">
                  head ➔ [10] ➔ [20] ➔ None
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:14px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:14px;margin-bottom:8px;">2. เชื่อมโยง new_node.next</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#e2e8f0;">
                  new_node(5).next = self.head<br/>
                  <span style="color:#34d399;">[5] ➔ [10]</span>
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:14px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:14px;margin-bottom:8px;">3. สลับตำแหน่ง head</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#e2e8f0;">
                  self.head = new_node<br/>
                  <span style="color:#38bdf8;">head ➔ [5] ➔ [10] ➔ [20]</span>
                </div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚡ ใช้เวลาเพียง <b>O(1)</b> เพราะไม่ต้องวนลูป ไม่ว่าใน List จะมีข้อมูล 10 ตัวหรือ 1,000,000 ตัวก็เสร็จทันที!</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 12. DELETE MIDDLE NODE BYPASS (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('การลบโหนดตรงกลาง') || (lower.includes('prev.next = curr.next') && lower.includes('n_20b'))) {
      return {
        title: '✂️ Linked List: การลบโหนดเป้าหมาย (Pointer Bypass Removal)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 640 200" style="width:100%;max-width:640px;">
              ${svgDefs}
              <!-- Nodes -->
              <rect x="80" y="50" width="90" height="44" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="125" y="77" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Node 10</text>
              <text x="125" y="32" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">prev</text>

              <!-- Node 20 (Target) -->
              <rect x="260" y="50" width="90" height="44" rx="8" fill="rgba(239,68,68,0.15)" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 4" />
              <text x="305" y="77" fill="#f87171" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Node 20 ❌</text>
              <text x="305" y="32" fill="#ef4444" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">curr (Delete!)</text>

              <rect x="440" y="50" width="90" height="44" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="485" y="77" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Node 30</text>
              <text x="485" y="32" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">curr.next</text>

              <!-- Normal connections -->
              <line x1="170" y1="72" x2="250" y2="72" stroke="#475569" stroke-width="2" stroke-dasharray="3 3" />
              <line x1="350" y1="72" x2="430" y2="72" stroke="#475569" stroke-width="2" stroke-dasharray="3 3" />

              <!-- Bypass Curved Arrow -->
              <path d="M 125 94 C 125 170, 485 170, 485 100" fill="none" stroke="#10b981" stroke-width="3" marker-end="url(#dsa-arrow-emerald)" />
              <text x="305" y="160" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">prev.next = curr.next (ชี้ข้ามตัด Node 20)</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🗑️ เมื่อไม่มีใครชี้ไปยัง Node 20 แล้ว ระบบ Garbage Collector ของ Python จะเคลียร์หน่วยความจำทิ้งให้อัตโนมัติ</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 13. DOUBLY LINKED LIST INSERT (4-STEP POINTER RELINK) (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('การปรับเปลี่ยนพอยน์เตอร์ 4 สเต็ปของ doubly') || (lower.includes('curr.next = new_node') && lower.includes('new_node.prev = curr'))) {
      return {
        title: '⚡ Doubly Linked List: ลำดับการต่อพอยน์เตอร์ 4 สเต็ป (Four-Step Relink)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:12px;">
              <div style="background:#181a26;border-left:3.5px solid #4fd1e8;padding:12px 14px;border-radius:8px;">
                <span style="color:#4fd1e8;font-weight:700;font-family:'JetBrains Mono',monospace;">Step 1:</span>
                <code style="color:#fff;display:block;margin-top:4px;">new_node.next = curr.next</code>
                <span style="font-size:11.5px;color:#94a3b8;">ต่อลูกศรไปข้างหน้าของโหนดใหม่ก่อน เพื่อไม่ให้หลุดสาย</span>
              </div>
              <div style="background:#181a26;border-left:3.5px solid #fbbf24;padding:12px 14px;border-radius:8px;">
                <span style="color:#fbbf24;font-weight:700;font-family:'JetBrains Mono',monospace;">Step 2:</span>
                <code style="color:#fff;display:block;margin-top:4px;">new_node.prev = curr</code>
                <span style="font-size:11.5px;color:#94a3b8;">ต่อลูกศรย้อนกลับของโหนดใหม่มาชี้ที่โหนดปัจจุบัน</span>
              </div>
              <div style="background:#181a26;border-left:3.5px solid #10b981;padding:12px 14px;border-radius:8px;">
                <span style="color:#10b981;font-weight:700;font-family:'JetBrains Mono',monospace;">Step 3:</span>
                <code style="color:#fff;display:block;margin-top:4px;">curr.next.prev = new_node</code>
                <span style="font-size:11.5px;color:#94a3b8;">ให้โหนดตัวถัดไปชี้พอยน์เตอร์ prev ย้อนกลับมาหาโหนดใหม่</span>
              </div>
              <div style="background:#181a26;border-left:3.5px solid #b794f6;padding:12px 14px;border-radius:8px;">
                <span style="color:#b794f6;font-weight:700;font-family:'JetBrains Mono',monospace;">Step 4:</span>
                <code style="color:#fff;display:block;margin-top:4px;">curr.next = new_node</code>
                <span style="font-size:11.5px;color:#94a3b8;">คำสั่งสุดท้าย: อัปเดต next ของ curr ให้มาชี้โหนดใหม่</span>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 14. LINKED LIST TRAVERSAL TRACE 7->1->2->3->6->0 (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('h["head"]') && lower.includes('n6["[7]"]') && lower.includes('n1["[0]"]')) {
      return {
        title: '🔍 Linked List Traversal Trace: [7] ➔ [1] ➔ [2] ➔ [3] ➔ [6] ➔ [0]',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;align-items:center;gap:10px;overflow-x:auto;padding:10px 4px;">
              <span style="color:#fbbf24;font-weight:700;font-family:'JetBrains Mono',monospace;">head ➔</span>
              <div class="dsa-heap-cell" style="width:48px;height:48px;border-color:#4fd1e8;"><span class="cell-val">7</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell" style="width:48px;height:48px;border-color:#4fd1e8;"><span class="cell-val">1</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell" style="width:48px;height:48px;border-color:#4fd1e8;"><span class="cell-val">2</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell" style="width:48px;height:48px;border-color:#4fd1e8;"><span class="cell-val">3</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell" style="width:48px;height:48px;border-color:#4fd1e8;"><span class="cell-val">6</span></div>
              <span style="color:#4fd1e8;">➔</span>
              <div class="dsa-heap-cell" style="width:48px;height:48px;border-color:#4fd1e8;"><span class="cell-val">0</span></div>
              <span style="color:#ef4444;">➔ None</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 15. NODE POINTER SWAPPING (Chapter 03.1)
    // -------------------------------------------------------------
    if (lower.includes('เป้าหมายหลังสลับ: 1 -> 4 -> 3 -> 2 -> 5') || (lower.includes('node 4') && lower.includes('node 2') && lower.includes('node 5') && lower.includes('node 1 (head)'))) {
      return {
        title: '✂️ Linked List Node Pointer Swapping (สลับตำแหน่ง Node 2 และ Node 4)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:flex;flex-direction:column;gap:14px;">
              <div style="background:#181a26;border:1px solid #334155;border-radius:10px;padding:12px 16px;">
                <span style="color:#94a3b8;font-size:12px;font-weight:700;">ก่อนสลับ:</span>
                <div style="font-family:'JetBrains Mono',monospace;font-size:14px;color:#e2e8f0;margin-top:4px;">
                  1 ➔ <span style="color:#f59e0b;font-weight:700;">[2]</span> ➔ 3 ➔ <span style="color:#4fd1e8;font-weight:700;">[4]</span> ➔ 5
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:12px 16px;">
                <span style="color:#10b981;font-size:12px;font-weight:700;">หลังสลับพอยน์เตอร์สำเร็จ (โดยไม่คัดลอก Data):</span>
                <div style="font-family:'JetBrains Mono',monospace;font-size:14px;color:#e2e8f0;margin-top:4px;">
                  1 ➔ <span style="color:#4fd1e8;font-weight:700;">[4]</span> ➔ 3 ➔ <span style="color:#f59e0b;font-weight:700;">[2]</span> ➔ 5
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 16. STACK ADT LIFO CANISTER (Chapter 04.1)
    // -------------------------------------------------------------
    if (lower.includes('stack_ops') || (lower.includes('push(30)') && lower.includes('topnode') && lower.includes('botnode'))) {
      return {
        title: '🥞 Stack ADT Memory Model: LIFO (Last-In First-Out) Canister',
        topicHash: '#stack',
        html: `
          <div class="dsa-native-wrap" style="display:flex;justify-content:center;gap:30px;align-items:center;flex-wrap:wrap;">
            <div style="width:180px;background:#0d1117;border:2.5px solid #4fd1e8;border-top:none;border-radius:0 0 16px 16px;padding:16px 12px;box-shadow:0 0 20px rgba(79,209,232,0.15);">
              <div style="text-align:center;font-size:11px;color:#fbbf24;font-family:'JetBrains Mono',monospace;margin-bottom:8px;">▲ TOP (เข้า/ออก)</div>
              <div style="display:flex;flex-direction:column;gap:8px;">
                <div style="background:#1e293b;border:1.5px solid #f59e0b;border-radius:8px;padding:10px;text-align:center;font-weight:700;color:#fff;box-shadow:0 0 10px rgba(245,158,11,0.2);">[ 30 ] TOP</div>
                <div style="background:#1e293b;border:1px solid #4fd1e8;border-radius:8px;padding:10px;text-align:center;font-weight:700;color:#cbd5e1;">[ 20 ]</div>
                <div style="background:#191c28;border:1px solid #64748b;border-radius:8px;padding:10px;text-align:center;font-weight:700;color:#94a3b8;">[ 10 ] BOTTOM</div>
              </div>
            </div>
            <div style="display:flex;flex-direction:column;gap:12px;font-size:13px;max-width:320px;">
              <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.3);padding:10px 16px;border-radius:8px;color:#34d399;">
                📥 <b>push(x)</b>: ใส่ข้อมูลลงบนสุดของ Stack (O(1))
              </div>
              <div style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);padding:10px 16px;border-radius:8px;color:#fca5a5;">
                📤 <b>pop()</b>: ดึงข้อมูลบนสุด (Top) ออกมาก่อนเสมอ (O(1))
              </div>
              <div style="background:rgba(79,209,232,0.12);border:1px solid rgba(79,209,232,0.3);padding:10px 16px;border-radius:8px;color:#4fd1e8;">
                👀 <b>peek()</b>: ส่องดูค่าบนสุดโดยไม่นำออก (O(1))
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 17. TREE TERMINOLOGY (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('root: a (depth=0, height=2)') || (lower.includes('b (internal node)') && lower.includes('d (leaf, depth=2)'))) {
      return {
        title: '🌲 Tree Terminology Architecture: Root, Internal Nodes, Leaves & Depth/Height Levels',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 540 240" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="40" x2="160" y2="110" stroke="#334155" stroke-width="2.5" />
              <line x1="270" y1="40" x2="380" y2="110" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="110" x2="100" y2="180" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="110" x2="220" y2="180" stroke="#334155" stroke-width="2.5" />
              <line x1="380" y1="110" x2="420" y2="180" stroke="#334155" stroke-width="2.5" />

              <!-- Level Guidelines -->
              <text x="30" y="45" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11">Depth 0</text>
              <text x="30" y="115" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11">Depth 1</text>
              <text x="30" y="185" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11">Depth 2</text>

              <!-- Node A (Root) -->
              <circle cx="270" cy="40" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="270" y="46" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="16" font-weight="700" text-anchor="middle">A</text>
              <text x="270" y="14" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Root (Height=2)</text>

              <!-- Nodes B & C (Internal) -->
              <circle cx="160" cy="110" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="115" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">B</text>

              <circle cx="380" cy="110" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="380" y="115" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="15" font-weight="700" text-anchor="middle">C</text>

              <!-- Nodes D, E, F (Leaves) -->
              <circle cx="100" cy="180" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="100" y="185" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">D</text>

              <circle cx="220" cy="180" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="220" y="185" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">E</text>

              <circle cx="420" cy="180" r="18" fill="#181a26" stroke="#10b981" stroke-width="2" />
              <text x="420" y="185" fill="#fff" font-family="'Chakra Petch', sans-serif" font-size="14" font-weight="700" text-anchor="middle">F</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 <b>Leaf Node</b> (โหนดใบ D, E, F) คือโหนดที่ไม่มีลูกเลย (Degree=0) | <b>Internal Node</b> คือโหนดที่มีลูกอย่างน้อย 1 ตัว</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 18. FULL VS COMPLETE BINARY TREE (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('full binary tree') && lower.includes('complete binary tree')) {
      return {
        title: '🌴 Structural Comparison: Full Binary Tree vs Complete Binary Tree',
        topicHash: '#heap',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:8px;text-align:center;">
                  Full Binary Tree
                </div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:12px;text-align:center;">ทุกโหนดมีลูก 0 หรือ 2 ตัวเท่านั้น (ห้ามมีลูก 1 ตัว)</div>
                <svg viewBox="0 0 240 140" style="width:100%;">
                  <line x1="120" y1="20" x2="60" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="120" y1="20" x2="180" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="60" y1="70" x2="30" y2="120" stroke="#334155" stroke-width="2" />
                  <line x1="60" y1="70" x2="90" y2="120" stroke="#334155" stroke-width="2" />
                  <circle cx="120" cy="20" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="120" y="24" fill="#fff" font-size="11" text-anchor="middle">A</text>
                  <circle cx="60" cy="70" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="60" y="74" fill="#fff" font-size="11" text-anchor="middle">B</text>
                  <circle cx="180" cy="70" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="180" y="74" fill="#fff" font-size="11" text-anchor="middle">C</text>
                  <circle cx="30" cy="120" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="30" y="124" fill="#fff" font-size="10" text-anchor="middle">D</text>
                  <circle cx="90" cy="120" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="90" y="124" fill="#fff" font-size="10" text-anchor="middle">E</text>
                </svg>
              </div>

              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#f59e0b;font-weight:700;font-size:15px;margin-bottom:8px;text-align:center;">
                  Complete Binary Tree
                </div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:12px;text-align:center;">ทุกชั้นเต็มแน่น ชั้นสุดท้ายเติมชิดซ้ายเสมอ (ใช้ทำ Heap!)</div>
                <svg viewBox="0 0 240 140" style="width:100%;">
                  <line x1="120" y1="20" x2="60" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="120" y1="20" x2="180" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="60" y1="70" x2="30" y2="120" stroke="#334155" stroke-width="2" />
                  <line x1="60" y1="70" x2="90" y2="120" stroke="#334155" stroke-width="2" />
                  <line x1="180" y1="70" x2="150" y2="120" stroke="#334155" stroke-width="2" />
                  <circle cx="120" cy="20" r="14" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="120" y="24" fill="#fff" font-size="11" text-anchor="middle">A</text>
                  <circle cx="60" cy="70" r="14" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="60" y="74" fill="#fff" font-size="11" text-anchor="middle">B</text>
                  <circle cx="180" cy="70" r="14" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="180" y="74" fill="#fff" font-size="11" text-anchor="middle">C</text>
                  <circle cx="30" cy="120" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="30" y="124" fill="#fff" font-size="10" text-anchor="middle">D</text>
                  <circle cx="90" cy="120" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="90" y="124" fill="#fff" font-size="10" text-anchor="middle">E</text>
                  <circle cx="150" cy="120" r="12" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="150" y="124" fill="#fff" font-size="10" text-anchor="middle">F</text>
                </svg>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 19. TREE TRAVERSALS 4 TYPES (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('การท่องไปในต้นไม้ 4 รูปแบบ') || (lower.includes('preorder: root') && lower.includes('inorder: left') && lower.includes('postorder: left'))) {
      return {
        title: '🔄 Tree Traversals Taxonomy: DFS (Pre, In, Post) vs BFS (Level-Order)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;">
              <div style="background:#181a26;border-left:3.5px solid #4fd1e8;padding:12px 14px;border-radius:8px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;">1. Preorder Traversal</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#fff;font-size:13px;margin:4px 0;">Root ➔ Left ➔ Right</div>
                <span style="font-size:11.5px;color:#94a3b8;">แวะ Root ก่อนใคร ใช้ทำ Clone ต้นไม้ หรือบันทึกโครงสร้าง</span>
              </div>
              <div style="background:#181a26;border-left:3.5px solid #10b981;padding:12px 14px;border-radius:8px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;">2. Inorder Traversal</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#fff;font-size:13px;margin:4px 0;">Left ➔ Root ➔ Right</div>
                <span style="font-size:11.5px;color:#94a3b8;">สำหรับ BST จะได้ข้อมูลเรียงจากน้อยไปมาก (Sorted Order) 100%!</span>
              </div>
              <div style="background:#181a26;border-left:3.5px solid #b794f6;padding:12px 14px;border-radius:8px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#b794f6;">3. Postorder Traversal</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#fff;font-size:13px;margin:4px 0;">Left ➔ Right ➔ Root</div>
                <span style="font-size:11.5px;color:#94a3b8;">แวะลูกให้ครบก่อนแวะแม่ ใช้คำนวณพื้นที่โฟลเดอร์ หรือลบต้นไม้</span>
              </div>
              <div style="background:#181a26;border-left:3.5px solid #f59e0b;padding:12px 14px;border-radius:8px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;">4. Level-Order Traversal</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#fff;font-size:13px;margin:4px 0;">Level 0 ➔ Level 1 ➔ ...</div>
                <span style="font-size:11.5px;color:#94a3b8;">ใช้ Queue (FIFO) ท่องทีละชั้นความกว้างจากซ้ายไปขวา</span>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 20. TREE PATH NOTATION QUESTION A->E->J->P (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('node a (root)') && lower.includes('node e') && lower.includes('node j') && lower.includes('node p')) {
      return {
        title: '🎯 Tree Path Notation: เส้นทางจาก Root A ไปยัง Leaf P (A ➔ E ➔ J ➔ P)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 540 220" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="30" x2="200" y2="90" stroke="#334155" stroke-width="2" />
              <line x1="270" y1="30" x2="320" y2="90" stroke="#f59e0b" stroke-width="3" />
              <line x1="320" y1="90" x2="360" y2="150" stroke="#f59e0b" stroke-width="3" />
              <line x1="360" y1="150" x2="340" y2="200" stroke="#f59e0b" stroke-width="3" />
              <line x1="360" y1="150" x2="400" y2="200" stroke="#334155" stroke-width="2" />

              <circle cx="270" cy="30" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="270" y="34" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">A</text>
              <circle cx="320" cy="90" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="320" y="94" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">E</text>
              <circle cx="360" cy="150" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="360" y="154" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">J</text>
              <circle cx="340" cy="200" r="16" fill="#10b981" stroke="#10b981" stroke-width="2.5" filter="url(#dsa-glow-emerald)" /><text x="340" y="204" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">P</text>
              <circle cx="400" cy="200" r="14" fill="#181a26" stroke="#64748b" stroke-width="1.5" /><text x="400" y="204" fill="#fff" font-size="11" text-anchor="middle">Q</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 Path Definition: ลำดับโหนดที่เชื่อมต่อกันจาก A ถึง P = <code>[A, E, J, P]</code> มีความยาว (Length) = 3 ขอบ</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 21. TREE TRAVERSALS ON 10, 3, 19, 8, 5, 15, 24 (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('10 (root)') && lower.includes('n19["19"]') && lower.includes('n15["15"]') && lower.includes('n24["24"]')) {
      return {
        title: '🌲 Tree Traversals Tracing: ตัวอย่างการท่องโหนด 10, 3, 19, 8, 5, 15, 24',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 520 220" style="width:100%;max-width:520px;">
              ${svgDefs}
              <line x1="260" y1="36" x2="160" y2="100" stroke="#334155" stroke-width="2.2" />
              <line x1="260" y1="36" x2="360" y2="100" stroke="#334155" stroke-width="2.2" />
              <line x1="160" y1="100" x2="110" y2="165" stroke="#334155" stroke-width="2.2" />
              <line x1="160" y1="100" x2="210" y2="165" stroke="#334155" stroke-width="2.2" />
              <line x1="360" y1="100" x2="310" y2="165" stroke="#334155" stroke-width="2.2" />
              <line x1="360" y1="100" x2="410" y2="165" stroke="#334155" stroke-width="2.2" />

              <circle cx="260" cy="36" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="260" y="41" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">10</text>
              <circle cx="160" cy="100" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="160" y="105" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <circle cx="360" cy="100" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="360" y="105" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">19</text>
              <circle cx="110" cy="165" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="110" y="169" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">8</text>
              <circle cx="210" cy="165" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="210" y="169" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">5</text>
              <circle cx="310" cy="165" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="310" y="169" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">15</text>
              <circle cx="410" cy="165" r="16" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="410" y="169" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">24</text>
            </svg>
            <div style="margin-top:14px;display:flex;flex-direction:column;gap:6px;font-family:'JetBrains Mono',monospace;font-size:12.5px;">
              <div>• <b>Preorder (Root-L-R)</b>: <span style="color:#4fd1e8;">10, 3, 8, 5, 19, 15, 24</span></div>
              <div>• <b>Inorder (L-Root-R)</b>: <span style="color:#10b981;">8, 3, 5, 10, 15, 19, 24</span></div>
              <div>• <b>Postorder (L-R-Root)</b>: <span style="color:#b794f6;">8, 5, 3, 15, 24, 19, 10</span></div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 22. SKEWED TREE 1->6->7->8 (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('t1["1 (root)"]') && lower.includes('t6["6"]') && lower.includes('t7["7"]') && lower.includes('t8["8"]')) {
      return {
        title: '🌴 Skewed Binary Tree Analysis (ต้นไม้เอนขวา Root 1 ➔ 6 ➔ 7 ➔ 8)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 380 220" style="width:100%;max-width:380px;">
              ${svgDefs}
              <line x1="80" y1="40" x2="160" y2="90" stroke="#f59e0b" stroke-width="2.5" />
              <line x1="160" y1="90" x2="240" y2="140" stroke="#f59e0b" stroke-width="2.5" />
              <line x1="240" y1="140" x2="190" y2="190" stroke="#4fd1e8" stroke-width="2.5" />

              <circle cx="80" cy="40" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="80" y="44" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">1</text>
              <circle cx="160" cy="90" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="160" y="94" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">6</text>
              <circle cx="240" cy="140" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="240" y="144" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">7</text>
              <circle cx="190" cy="190" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="190" y="194" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">8</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">⚠️ Skewed Tree ทำให้ประสิทธิภาพการค้นหาถดถอยจาก O(log N) กลายเป็น O(N) เทียบเท่า Linked List</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 23. ARITHMETIC EXPRESSION TREE (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('plusroot["+ (root กลาง)"]') || (lower.includes('subleft["+"]') && lower.includes('mulbc["*"]') && lower.includes('plusdef["+"]'))) {
      return {
        title: '🧮 Binary Expression Tree: (a + b * c) + ((d * e + f) * g)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 540 240" style="width:100%;max-width:540px;">
              ${svgDefs}
              <line x1="270" y1="36" x2="160" y2="90" stroke="#334155" stroke-width="2.2" />
              <line x1="270" y1="36" x2="380" y2="90" stroke="#334155" stroke-width="2.2" />
              <line x1="160" y1="90" x2="110" y2="150" stroke="#334155" stroke-width="2.2" />
              <line x1="160" y1="90" x2="200" y2="150" stroke="#334155" stroke-width="2.2" />
              <line x1="200" y1="150" x2="175" y2="200" stroke="#334155" stroke-width="2.2" />
              <line x1="200" y1="150" x2="225" y2="200" stroke="#334155" stroke-width="2.2" />

              <line x1="380" y1="90" x2="330" y2="150" stroke="#334155" stroke-width="2.2" />
              <line x1="380" y1="90" x2="430" y2="150" stroke="#334155" stroke-width="2.2" />
              <line x1="330" y1="150" x2="300" y2="200" stroke="#334155" stroke-width="2.2" />
              <line x1="330" y1="150" x2="355" y2="200" stroke="#334155" stroke-width="2.2" />

              <!-- Operators (Gold) -->
              <circle cx="270" cy="36" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="270" y="41" fill="#fbbf24" font-weight="700" font-size="16" text-anchor="middle">+</text>
              <circle cx="160" cy="90" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="160" y="95" fill="#fbbf24" font-weight="700" font-size="15" text-anchor="middle">+</text>
              <circle cx="380" cy="90" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="380" y="95" fill="#fbbf24" font-weight="700" font-size="15" text-anchor="middle">*</text>
              <circle cx="200" cy="150" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="200" y="155" fill="#fbbf24" font-weight="700" font-size="15" text-anchor="middle">*</text>
              <circle cx="330" cy="150" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="330" y="155" fill="#fbbf24" font-weight="700" font-size="15" text-anchor="middle">+</text>

              <!-- Operands (Cyan Leaves) -->
              <circle cx="110" cy="150" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="110" y="154" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">a</text>
              <circle cx="175" cy="200" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="175" y="204" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">b</text>
              <circle cx="225" cy="200" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="225" y="204" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">c</text>
              <circle cx="430" cy="150" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="430" y="154" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">g</text>
              <circle cx="355" cy="200" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="355" y="204" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">f</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">📌 การท่อง Inorder จะได้นิพจน์ Infix ดั้งเดิม ส่วนการท่อง Postorder จะได้นิพจน์ Postfix พร้อมคำนวณผ่าน Stack ทันที!</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 24. SMALL BINARY TREE ROOT 2 -> 3, 3 -> (2, 0) (Chapter 05.1)
    // -------------------------------------------------------------
    if (lower.includes('r2["2 (root)"]') && lower.includes('l3["3"]') && lower.includes('rr0["0"]')) {
      return {
        title: '🌲 Binary Tree Structure: Root 2 with Subtrees',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 360 180" style="width:100%;max-width:360px;">
              ${svgDefs}
              <line x1="180" y1="36" x2="110" y2="90" stroke="#334155" stroke-width="2.2" />
              <line x1="180" y1="36" x2="250" y2="90" stroke="#334155" stroke-width="2.2" />
              <line x1="250" y1="90" x2="210" y2="145" stroke="#334155" stroke-width="2.2" />
              <line x1="250" y1="90" x2="290" y2="145" stroke="#334155" stroke-width="2.2" />

              <circle cx="180" cy="36" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="180" y="41" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">2</text>
              <circle cx="110" cy="90" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="110" y="95" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <circle cx="250" cy="90" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="250" y="95" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <circle cx="210" cy="145" r="15" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="210" y="149" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">2</text>
              <circle cx="290" cy="145" r="15" fill="#181a26" stroke="#10b981" stroke-width="1.8" /><text x="290" y="149" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">0</text>
            </svg>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 25. GOLDEN BST RULE (Chapter 05.2)
    // -------------------------------------------------------------
    if (lower.includes('คุณสมบัติของ bst') || (lower.includes('left_subtree') && lower.includes('golden bst rule'))) {
      return {
        title: '🌲 Binary Search Tree (BST) The Golden Rule: Left < Root < Right',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 520 180" style="width:100%;max-width:520px;">
              ${svgDefs}
              <line x1="260" y1="40" x2="140" y2="110" stroke="#4fd1e8" stroke-width="2.5" />
              <line x1="260" y1="40" x2="380" y2="110" stroke="#10b981" stroke-width="2.5" />

              <circle cx="260" cy="40" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="260" y="45" fill="#fff" font-weight="700" font-size="15" text-anchor="middle">Root X</text>

              <rect x="60" y="95" width="160" height="50" rx="10" fill="rgba(79,209,232,0.12)" stroke="#4fd1e8" stroke-width="2" />
              <text x="140" y="118" fill="#38bdf8" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">Left Subtree</text>
              <text x="140" y="134" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="11" text-anchor="middle">ทุกค่าน้อยกว่า X (&lt; X)</text>

              <rect x="300" y="95" width="160" height="50" rx="10" fill="rgba(16,185,129,0.12)" stroke="#10b981" stroke-width="2" />
              <text x="380" y="118" fill="#34d399" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">Right Subtree</text>
              <text x="380" y="134" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="11" text-anchor="middle">ทุกค่ามากกว่า X (&gt; X)</text>
            </svg>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 26 & 27. BST INSERT 5 TRACE (Chapter 05.2)
    // -------------------------------------------------------------
    if (lower.includes('แทรกใหม่รอบที่ 3') || lower.includes('n5["5 (โหนดใหม่)"]') || (lower.includes('n6["6 (root)"]') && lower.includes('n2["2"]') && lower.includes('n8["8"]') && lower.includes('n4["4"]'))) {
      const isPostInsert = lower.includes('แทรกใหม่รอบที่ 3') || lower.includes('โหนดใหม่');
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
                <!-- Newly Inserted Node 5 -->
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

    // -------------------------------------------------------------
    // 28. BST 3 DELETION CASES (Chapter 05.3)
    // -------------------------------------------------------------
    if (lower.includes('เจาะลึก 3 กรณีการลบโหนด') || (lower.includes('case 1: leaf') && lower.includes('case 2: one child') && lower.includes('case 3: two children'))) {
      return {
        title: '✂️ BST Deletion: สรุปภาพรวม 3 กรณีการลบโหนด (Leaf, One Child, Two Children)',
        topicHash: '#bst',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:16px;">
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#10b981;font-size:15px;margin-bottom:6px;">Case 1: Leaf Node</div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:10px;">มีลูก 0 ตัว (โหนดใบ)</div>
                <div style="background:rgba(16,185,129,0.1);padding:10px;border-radius:6px;font-size:13px;color:#e2e8f0;">
                  ตัดโหนดใบออกได้ทันทีโดยสั่งให้ Pointer แม่ชี้เป็น <b>None</b>
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#4fd1e8;font-size:15px;margin-bottom:6px;">Case 2: One Child</div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:10px;">มีลูกเพียงข้างเดียว (ซ้ายหรือขวา)</div>
                <div style="background:rgba(79,209,232,0.1);padding:10px;border-radius:6px;font-size:13px;color:#e2e8f0;">
                  Bypass ข้าม: ดึงโหนดลูกขึ้นมาต่อกับโหนดแม่แทนตำแหน่งเดิมทันที
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f59e0b;font-size:15px;margin-bottom:6px;">Case 3: Two Children</div>
                <div style="font-size:12.5px;color:#94a3b8;margin-bottom:10px;">มีลูกครบทั้งสองข้าง!</div>
                <div style="background:rgba(245,158,11,0.1);padding:10px;border-radius:6px;font-size:13px;color:#e2e8f0;">
                  หา <b>Inorder Successor</b> (ค่าน้อยสุดในกิ่งขวา) คัดลอกค่ามาทับ แล้วลบโหนด Successor เดิมออก
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 29, 30, 31, 32. BST CASE 3 DELETION EXECUTION (Chapter 05.3)
    // -------------------------------------------------------------
    if (lower.includes('successor candidate') || lower.includes('successor ถูกยกขึ้นมาแทน 2') || (lower.includes('n3_new') && lower.includes('n6["6 (root)"]'))) {
      const isFinal = lower.includes('n3_new') || lower.includes('สำเร็จ');
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

    // -------------------------------------------------------------
    // 33. OPEN ADDRESSING STRATEGIES (Chapter 06.1)
    // -------------------------------------------------------------
    if (lower.includes('open addressing strategies') || (lower.includes('linear probing') && lower.includes('quadratic probing') && lower.includes('double hashing'))) {
      return {
        title: '🔑 Open Addressing: กลยุทธ์การแก้การชน 3 รูปแบบ (Linear, Quadratic, Double Hashing)',
        topicHash: '#hash',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:16px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;">1. Linear Probing</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#fbbf24;margin:8px 0;">h(k, i) = (h(k) + i) mod M</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">ขยับทีละ 1 ช่องถัดไป (+1, +2, +3...) ข้อเสียคือเกิด <b>Primary Clustering</b> เกาะกลุ่มเป็นก้อน</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#f59e0b;font-weight:700;font-size:15px;">2. Quadratic Probing</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#fbbf24;margin:8px 0;">h(k, i) = (h(k) + i²) mod M</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">กระโดดด้วยกำลังสอง (+1, +4, +9, +16...) แก้ Primary Cluster ได้ แต่ต้องให้ตารางขนาด Prime และ λ ≤ 0.5</p>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:15px;">3. Double Hashing</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:12.5px;color:#fbbf24;margin:8px 0;">h(k, i) = (h₁(k) + i·h₂(k)) mod M</div>
                <p style="font-size:12.5px;color:#c7cad6;margin:0;">ใช้ฟังก์ชันแฮชตัวที่สอง h₂(k) กำหนดขนาดการกระโดด กระจายตัวสม่ำเสมอที่สุด ไม่มีปัญหา Clustering</p>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 34 & 35 & 47. BINARY MIN-HEAP & ARRAY INDEXING (Chapter 07.1 & 11.6)
    // -------------------------------------------------------------
    if (lower.includes('h13') || (lower.includes('13') && lower.includes('21') && lower.includes('16') && (lower.includes('68') || lower.includes('31')))) {
      const isTraceInsert = lower.includes('hole') || lower.includes('candidate hole') || lower.includes('insert 14');
      return {
        title: isTraceInsert
          ? '⚡ Binary Min-Heap Architecture: 10 Nodes + Slot [11] Candidate Hole (Insert 14 Tracing)'
          : '⚡ Binary Min-Heap: Complete Binary Tree & 1-Based Array Indexing',
        topicHash: '#heap',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 720 280" style="width:100%;max-width:720px;">
              ${svgDefs}
              <line x1="360" y1="36" x2="190" y2="100" stroke="#334155" stroke-width="2.5" />
              <line x1="360" y1="36" x2="530" y2="100" stroke="#334155" stroke-width="2.5" />
              <line x1="190" y1="100" x2="105" y2="165" stroke="#334155" stroke-width="2.5" />
              <line x1="190" y1="100" x2="275" y2="165" stroke="#334155" stroke-width="2.5" />
              <line x1="530" y1="100" x2="445" y2="165" stroke="#334155" stroke-width="2.5" />
              <line x1="530" y1="100" x2="615" y2="165" stroke="#334155" stroke-width="2.5" />
              <line x1="105" y1="165" x2="65" y2="230" stroke="#334155" stroke-width="2.5" />
              <line x1="105" y1="165" x2="145" y2="230" stroke="#334155" stroke-width="2.5" />
              <line x1="275" y1="165" x2="235" y2="230" stroke="#334155" stroke-width="2.5" />
              ${isTraceInsert ? '<line x1="275" y1="165" x2="315" y2="230" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4" />' : ''}

              <!-- Root 13 [1] -->
              <circle cx="360" cy="36" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="360" y="41" fill="#fff" font-weight="700" font-size="15" text-anchor="middle">13</text>
              <text x="360" y="14" fill="#fbbf24" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">[1] Root</text>

              <!-- Level 1: 21 [2], 16 [3] -->
              <circle cx="190" cy="100" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="190" y="105" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">21</text>
              <text x="190" y="76" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[2]</text>

              <circle cx="530" cy="100" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" />
              <text x="530" y="105" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">16</text>
              <text x="530" y="76" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[3]</text>

              <!-- Level 2 -->
              <circle cx="105" cy="165" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="105" y="170" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">24</text>
              <text x="105" y="142" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[4]</text>

              <circle cx="275" cy="165" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="275" y="170" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">31</text>
              <text x="275" y="142" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[5]</text>

              <circle cx="445" cy="165" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="445" y="170" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">19</text>
              <text x="445" y="142" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[6]</text>

              <circle cx="615" cy="165" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="615" y="170" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">68</text>
              <text x="615" y="142" fill="#94a3b8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[7]</text>

              <!-- Level 3 -->
              <circle cx="65" cy="230" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="65" y="234" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">65</text>
              <circle cx="145" cy="230" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="145" y="234" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">26</text>
              <circle cx="235" cy="230" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="235" y="234" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">32</text>

              ${isTraceInsert ? `
                <circle cx="315" cy="230" r="18" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4 4" filter="url(#dsa-glow-amber)" />
                <text x="315" y="235" fill="#fbbf24" font-weight="800" font-size="13" text-anchor="middle">14?</text>
                <text x="315" y="258" fill="#fbbf24" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">[11] Hole</text>
              ` : ''}
            </svg>

            <!-- 1-Based Memory Array Representation -->
            <div class="dsa-heap-array-row" style="margin-top:16px;">
              <div class="dsa-heap-cell"><span class="cell-idx">[0]</span><span class="cell-val" style="color:#64748b;">-</span></div>
              <div class="dsa-heap-cell root-cell"><span class="cell-idx">[1] Root</span><span class="cell-val">13</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[2]</span><span class="cell-val">21</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[3]</span><span class="cell-val">16</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[4]</span><span class="cell-val">24</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[5]</span><span class="cell-val">31</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[6]</span><span class="cell-val">19</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[7]</span><span class="cell-val">68</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[8]</span><span class="cell-val">65</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[9]</span><span class="cell-val">26</span></div>
              <div class="dsa-heap-cell"><span class="cell-idx">[10]</span><span class="cell-val">32</span></div>
              ${isTraceInsert ? '<div class="dsa-heap-cell" style="border-color:#f59e0b;background:rgba(245,158,11,0.12);border-style:dashed;"><span class="cell-idx" style="color:#fbbf24;">[11] Hole</span><span class="cell-val" style="color:#fbbf24;">14?</span></div>' : ''}
            </div>

            <div class="dsa-heap-formulas">
              <span>Parent(i) = ⌊i/2⌋</span>
              <span>Left(i) = 2 × i</span>
              <span>Right(i) = 2 × i + 1</span>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 36. 5 SORTING ALGORITHMS TAXONOMY (Chapter 08.1)
    // -------------------------------------------------------------
    if (lower.includes('sorting algorithms') && lower.includes('bubblesort') && lower.includes('mergesort')) {
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

    // -------------------------------------------------------------
    // 37 & 40. GRAPH REPRESENTATION (DIRECTED & UNDIRECTED) (Chapter 09.1)
    // -------------------------------------------------------------
    if (lower.includes('directed graph') || lower.includes('digraph') || (lower.includes('a --- b') && lower.includes('c --- d'))) {
      const isDirected = lower.includes('directed') || lower.includes('digraph');
      return {
        title: isDirected
          ? '🕸️ Directed Graph (Digraph) Architecture Model'
          : '🕸️ Undirected Graph Architecture Model (Cycle A-B-C-D)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 400 180" style="width:100%;max-width:400px;">
              ${svgDefs}
              ${isDirected ? `
                <line x1="120" y1="50" x2="260" y2="50" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <line x1="120" y1="50" x2="190" y2="130" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <line x1="260" y1="50" x2="190" y2="130" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <circle cx="120" cy="50" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" filter="url(#dsa-glow-cyan)" /><text x="120" y="55" fill="#fff" font-weight="700" text-anchor="middle">A</text>
                <circle cx="260" cy="50" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" filter="url(#dsa-glow-cyan)" /><text x="260" y="55" fill="#fff" font-weight="700" text-anchor="middle">B</text>
                <circle cx="190" cy="130" r="20" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" filter="url(#dsa-glow-amber)" /><text x="190" y="135" fill="#fff" font-weight="700" text-anchor="middle">C</text>
              ` : `
                <line x1="120" y1="50" x2="260" y2="50" stroke="#4fd1e8" stroke-width="2.5" />
                <line x1="260" y1="50" x2="260" y2="140" stroke="#4fd1e8" stroke-width="2.5" />
                <line x1="260" y1="140" x2="120" y2="140" stroke="#4fd1e8" stroke-width="2.5" />
                <line x1="120" y1="140" x2="120" y2="50" stroke="#4fd1e8" stroke-width="2.5" />
                <circle cx="120" cy="50" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="120" y="55" fill="#fff" font-weight="700" text-anchor="middle">A</text>
                <circle cx="260" cy="50" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="260" y="55" fill="#fff" font-weight="700" text-anchor="middle">B</text>
                <circle cx="260" cy="140" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="260" y="145" fill="#fff" font-weight="700" text-anchor="middle">C</text>
                <circle cx="120" cy="140" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="120" y="145" fill="#fff" font-weight="700" text-anchor="middle">D</text>
              `}
            </svg>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 38. BFS VS DFS TRAVERSALS (Chapter 09.1)
    // -------------------------------------------------------------
    if (lower.includes('graph traversals: bfs vs dfs') || (lower.includes('breadth-first search') && lower.includes('depth-first search'))) {
      return {
        title: '🔄 Graph Traversals: BFS (Queue) vs DFS (Stack / Recursion)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;margin-bottom:8px;">
                  1. Breadth-First Search (BFS)
                </div>
                <div style="font-size:13px;color:#c7cad6;line-height:1.6;">
                  • <b>Data Structure</b>: ใช้ <b>Queue (FIFO)</b><br/>
                  • <b>พฤติกรรม</b>: ท่องกระจายเป็นวงคลื่นทีละระดับความกว้าง<br/>
                  • <b>การประยุกต์ใช้</b>: หา Shortest Path ใน Unweighted Graph, ระดับ Level ในโครงสร้างเครือข่าย
                </div>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:12px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#f59e0b;font-weight:700;font-size:15px;margin-bottom:8px;">
                  2. Depth-First Search (DFS)
                </div>
                <div style="font-size:13px;color:#c7cad6;line-height:1.6;">
                  • <b>Data Structure</b>: ใช้ <b>Stack (LIFO)</b> หรือ Call Stack Recursion<br/>
                  • <b>พฤติกรรม</b>: ดำดิ่งลงไปให้สุดกิ่งแล้วค่อยย้อนกลับ (Backtracking)<br/>
                  • <b>การประยุกต์ใช้</b>: ตรวจจับ Cycle ในกราฟ, Topological Sort, หา Connected Components
                </div>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 39 & 41. TOPOLOGICAL SORT (Chapter 09.1)
    // -------------------------------------------------------------
    if (lower.includes('topological sort') || lower.includes('cs101') || lower.includes('v1["v1 (in=0)"]')) {
      const isCoursePrereq = lower.includes('cs101');
      return {
        title: isCoursePrereq
          ? '🔀 Topological Sort: แบบจำลองเงื่อนไขวิชาบังคับก่อน (Course Prerequisite DAG)'
          : '🔀 Topological Sort: 7-Node DAG & Indegree Array Tracing',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            ${isCoursePrereq ? `
              <svg viewBox="0 0 540 180" style="width:100%;max-width:540px;">
                ${svgDefs}
                <line x1="140" y1="60" x2="270" y2="60" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <line x1="140" y1="60" x2="270" y2="120" stroke="#4fd1e8" stroke-width="2.5" marker-end="url(#dsa-arrow-cyan)" />
                <line x1="390" y1="60" x2="450" y2="90" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" />
                <line x1="390" y1="120" x2="450" y2="90" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" />

                <rect x="20" y="38" width="120" height="44" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                <text x="80" y="65" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">CS101 (In=0)</text>

                <rect x="270" y="38" width="120" height="44" rx="8" fill="#181a26" stroke="#fbbf24" stroke-width="2" />
                <text x="330" y="65" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">CS102 (In=1)</text>

                <rect x="270" y="98" width="120" height="44" rx="8" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
                <text x="330" y="125" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">Math101 (In=0)</text>

                <rect x="450" y="68" width="120" height="44" rx="8" fill="#181a26" stroke="#10b981" stroke-width="2.5" filter="url(#dsa-glow-emerald)" />
                <text x="510" y="95" fill="#34d399" font-family="'Chakra Petch',sans-serif" font-weight="800" font-size="13" text-anchor="middle">CS201 (In=2)</text>
              </svg>
            ` : `
              <div style="background:#181a26;border:1px solid #334155;border-radius:10px;padding:16px;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#fbbf24;font-weight:700;font-size:15px;margin-bottom:8px;">ลำดับ Topological Sort ที่ถูกต้อง:</div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:14px;color:#34d399;font-weight:700;">
                  v1 ➔ v2 ➔ v4 ➔ v3 ➔ v5 ➔ v7 ➔ v6
                </div>
                <div style="font-size:12.5px;color:#94a3b8;margin-top:8px;">อัลกอริทึมเริ่มจากโหนดที่มี Indegree = 0 (v1) ใส่ลงใน Queue จากนั้นดึงออกมา ตัดเส้นเชื่อมออก และลด Indegree ของเพื่อนบ้านลงทีละ 1</div>
              </div>
            `}
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 42 & 43 & 44 & 48. SHORTEST PATH & DIJKSTRA (Chapter 10.1 & 11.6)
    // -------------------------------------------------------------
    if (lower.includes('dijkstra') || lower.includes('shortestpath') || lower.includes('adjacencylist') || lower.includes('v1((v1)) -- 2 --> v2((v2))')) {
      const isExamGraph = lower.includes('v1((v1)) -- 2 --> v2((v2))') || lower.includes('part 5: ขั้นตอนวิธีวิถีสั้นสุด');
      return {
        title: isExamGraph
          ? '🚀 Dijkstra Shortest Path: กราฟถ่วงน้ำหนักข้อสอบปลายภาค (Source: v1 ➔ Target: v5)'
          : '🗺️ Shortest Path & Dijkstra Algorithm Flow Architecture (O((V + E) log V))',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 580 260" style="width:100%;max-width:580px;">
              ${svgDefs}
              <!-- Graph Edges with Weights -->
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

              <!-- Vertices -->
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

    // -------------------------------------------------------------
    // 45. FINAL EXAM 5 TRAPS MINDMAP (Chapter 11.6)
    // -------------------------------------------------------------
    if (lower.includes('กับดักข้อสอบปลายภาค') || (lower.includes('mindmap') && lower.includes('trap 1'))) {
      return {
        title: '🚨 5 กับดักข้อสอบปลายภาคและจุดเน้นคะแนนจากอาจารย์ (Classroom Traps)',
        topicHash: '',
        html: `
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:14px;">
              <div style="background:#181a26;border-left:4px solid #ef4444;border-radius:8px;padding:14px;">
                <div style="color:#f87171;font-weight:700;font-size:14px;">⚠️ Trap 1: การนับ Collision</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-top:6px;"><b>ห้ามนับรอบ Resolve รวม!</b> ถ้าชน 7 ครั้งแล้วแก้ 7 ครั้ง ต้องตอบว่าชน 7 ครั้ง (ตอบ 14 = 0 คะแนนทันที)</div>
              </div>
              <div style="background:#181a26;border-left:4px solid #f59e0b;border-radius:8px;padding:14px;">
                <div style="color:#fbbf24;font-weight:700;font-size:14px;">⚠️ Trap 2: Modulo Wrap-Around</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-top:6px;">สูตร Probing ต้องใส่ <code>% TableSize</code> ทุกสเต็ป เช่น (9 + 1) mod 10 = 0 เพื่อให้วนลูปกลับมาต้นตารางได้</div>
              </div>
              <div style="background:#181a26;border-left:4px solid #4fd1e8;border-radius:8px;padding:14px;">
                <div style="color:#38bdf8;font-weight:700;font-size:14px;">⚠️ Trap 3: พารามิเตอร์ R ใน Double Hashing</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-top:6px;">R คือ Prime สูงสุดที่ &lt; TableSize (เช่น ขนาด 10 ใช้ R=7, ขนาด 16 ใช้ R=13) <b>ห้ามจำตายตัวว่าเป็น 7</b></div>
              </div>
              <div style="background:#181a26;border-left:4px solid #10b981;border-radius:8px;padding:14px;">
                <div style="color:#34d399;font-weight:700;font-size:14px;">⚠️ Trap 4: สูตร Rehashing</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-top:6px;">เมื่อ Load Factor เกินกำหนด ตารางใหม่ต้องเป็น <b>จำนวนเฉพาะตัวแรกที่มากกว่า 2 × TableSize เดิม</b></div>
              </div>
              <div style="background:#181a26;border-left:4px solid #b794f6;border-radius:8px;padding:14px;">
                <div style="color:#c084fc;font-weight:700;font-size:14px;">⚠️ Trap 5: 1-Based Heap Index</div>
                <div style="font-size:12.5px;color:#c7cad6;margin-top:6px;">Root ของ Binary Heap เริ่มต้นที่ <b>Index 1</b> (Index 0 เว้นว่าง) สูตร Parent = ⌊i/2⌋ ปัดเศษทิ้งเสมอ!</div>
              </div>
            </div>
          </div>
        `
      };
    }

    // -------------------------------------------------------------
    // 46. LINEAR PROBING COLLISION COUNT TRAP (Chapter 11.6)
    // -------------------------------------------------------------
    if (lower.includes('hash_simulation') || (lower.includes('89 mod 10 = 9') && lower.includes('49 mod 10 = 9') && lower.includes('58 mod 10 = 8'))) {
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

    // -------------------------------------------------------------
    // UNIVERSAL FALLBACK: HIGH-FIDELITY DSA LAB SVG ENGINE
    // -------------------------------------------------------------
    return generateGenericDsaLabVisual(code, getArchitectureTitle(code));
  }
'''

print('Generated engine length:', len(get_engine_code()))
