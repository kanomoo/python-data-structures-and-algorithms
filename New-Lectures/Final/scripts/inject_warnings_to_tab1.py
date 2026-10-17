# -*- coding: utf-8 -*-
"""
Script to inject teacher warnings into Question 2, 3, 4, 7 in generate_tab1.py
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Question 2 Warning
q2_marker = r"""  <h2 id="q2" class="part-title">Question 2: Priority Queue (Binary Min-Heap) (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 6 (Priority Queues), pp. 243-260 / สไลด์ Priority Queues อ.ประดิษฐ์ ภาพที่ 7-9</div>"""

q2_warn = q2_marker + r"""

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (จุดดัก 0 คะแนนใน Binary Heap):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>Index 0 Sentinel:</strong> อาร์เรย์ของ Heap ต้องเริ่มที่ Index 1 เสมอ ช่อง 0 เว้นว่างใส่ <code>None</code> หากนำ Root ไปไว้ที่ 0 สูตรพ่อลูก $2i$ จะวนกลับมาที่ตัวเอง<br>
      • <strong>Floor Division (//):</strong> การหา Parent ของโหนด $i$ ต้องใช้ $\lfloor i / 2 \rfloor$ ปัดเศษทิ้ง (เช่น โหนด 7 ได้ $7 // 2 = 3$ ห้ามปัดขึ้นเป็น 4 เด็ดขาด)<br>
      • <strong>DeleteMin:</strong> การบ้านในห้องเรียนให้อาจารย์ทำ 1 ครั้ง แต่ในข้อสอบปลายภาคอาจารย์จะออก <strong>deleteMin 3 ครั้งติดต่อกัน!</strong> ให้นำ Root ออก แล้วดึงตัวท้ายสุดมาแทนที่ แล้ว Percolate Down โดยสลับกับลูกตัวที่น้อยกว่าเสมอ
    </p>
  </div>"""

# 3. Question 3 Warning
q3_marker = r"""  <h2 id="q3" class="part-title">Question 3: Insertion Sort Tracing &amp; Position Moves (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 281-285 / สไลด์ Insertion Sort อ.ประดิษฐ์</div>"""

q3_warn = q3_marker + r"""

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (สูตรลัด 1 นาที vs 1 ชั่วโมง):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>Worst Case (ข้อมูลเรียงกลับทิศทาง):</strong> จำนวน Position Moves ทั้งหมดคือผลรวมอนุกรมเลขคณิต $\frac{N(N-1)}{2}$ เช่น $N=6 \implies 15$ ครั้ง, $N=8 \implies 28$ ครั้ง, $N=10 \implies 45$ ครั้ง มองอนุกรมให้ออกจะประหยัดเวลาทำข้อสอบได้เป็นชั่วโมง<br>
      • <strong>Best Case (ข้อมูลเรียงอยู่แล้ว):</strong> Position Moves $= 0$ ครั้ง, Time Complexity $= O(N)$
    </p>
  </div>"""

# 4. Question 4 Warning
q4_marker = r"""  <h2 id="q4" class="part-title">Question 4: Selection Sort &amp; Bubble Sort Tracing (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 285-290 / สไลด์ Selection &amp; Bubble Sort อ.ประดิษฐ์</div>"""

q4_warn = q4_marker + r"""

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (สูตร Inversions &amp; จุดดัก Python):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>สูตรลัด Total Swaps ใน Bubble Sort:</strong> จำนวนครั้งการ Swap ทั้งหมดจะเท่ากับ <strong>จำนวน Inversions ในอาร์เรย์เริ่มต้น 100%</strong> นับตัวทางขวาที่น้อยกว่าทีละตัวแล้วจับบวกกัน ไม่ต้องรันลูป<br>
      • <strong>จุดเด่น Selection Sort:</strong> มีการ Swap ข้อมูลน้อยมากเพียง $O(N)$ ครั้ง (มากสุด $N-1$ ครั้ง) เหมาะมากกับหน่วยความจำที่เขียนซ้ำได้จำกัด<br>
      • <strong>กับดัก <code>range(0)</code>:</strong> ไม่ใช่ <code>None</code> และไม่ใช่ <code>[0]</code> แต่เป็น Empty Sequence Object ที่บันทึกเพียง metadata <code>start=0, stop=0, step=1</code>
    </p>
  </div>"""

# 5. Question 7 Warning
q7_marker = r"""  <h2 id="q7" class="part-title">Question 7: Properties &amp; Theory Calculations (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapters 4, 5, 6, 7, 9 / สไลด์สรุปเนื้อหา อ.ประดิษฐ์</div>"""

q7_warn = q7_marker + r"""

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (จุดดัก 0 คะแนนข้อความบน Notepad):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>2 Properties vs 3 Properties:</strong> มี 2 คุณสมบัติคือ <strong>Binary Heap</strong> (Structure Property + Heap-Order Property), มี 3 คุณสมบัติคือ <strong>AVL Tree</strong> (BST Property + Height-Balanced Property + Node Structure)<br>
      • <strong>Complete Graph Edges:</strong> $E = \frac{V(V-1)}{2}$ เช่น $V=10 \implies 45$ เส้น <em>ห้ามตอบติดสูตร เช่น <code>10*(10-1)/2</code> หรือ <code>90/2</code> โดนหักเหลือ 0 คะแนนทันที ต้องกดเครื่องคิดเลขตอบตัวเลข 45</em><br>
      • <strong>Complete Binary Tree Nodes:</strong> ที่ความสูง $H=10$ โหนดต่ำสุด $= 1,024$ โหนดสูงสุด $= 2,047$ <em>ห้ามตอบเป็นเลขยกกำลัง $2^{10}$ หรือ $2^{11}-1$ เด็ดขาด โดน 0 ทันที</em>
    </p>
  </div>"""

for name, marker, repl in [("Q2", q2_marker, q2_warn),
                           ("Q3", q3_marker, q3_warn),
                           ("Q4", q4_marker, q4_warn),
                           ("Q7", q7_marker, q7_warn)]:
    if marker in text:
        text = text.replace(marker, repl)
        print(f"{name} warning injected successfully!")
    else:
        print(f"Warning: {name} marker not found!")

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"generate_tab1.py updated! Total chars: {len(text)}")
