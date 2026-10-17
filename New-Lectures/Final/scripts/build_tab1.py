# -*- coding: utf-8 -*-
"""
Builder to generate generate_tab1.py from existing raw Tab 1,
injecting textbook citations, quick jump bar, and new sub-questions:
- Q1: 1.5 Wrap Around, 1.6 How to choose new TableSize, 1.7 How to choose R, 1.8 Load factor %
- Q3: 3.2 Best/Average/Worst case in Insertion Sort
- Q4: 4.2 Best/Average/Worst case in Bubble/Selection Sort
"""

import re

with open(r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "🌟 ตอนที่ 1:"
end_marker = "🎯 ตอนที่ 2:"
start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

h1_start = text.rfind("<h1", 0, start_idx)
h1_end = text.rfind("<!-- ======", 0, end_idx)

tab1_content = text[h1_start:h1_end]

# 1. Wrap in Tab 1 container and Quick Jump Bar
quick_nav = """  <!-- QUICK NAV FOR TAB 1 -->
  <div class="nav-jump-bar">
    <span class="nav-jump-label">⚡ ทางลัดข้อสอบชุด 2569:</span>
    <a href="#q1" class="jump-pill">ข้อ 1 Hashing &amp; Open Addressing</a>
    <a href="#q2" class="jump-pill">ข้อ 2 Binary Min-Heap (Array &amp; hole)</a>
    <a href="#q3" class="jump-pill">ข้อ 3 Insertion Sort Tracing</a>
    <a href="#q4" class="jump-pill">ข้อ 4 Selection &amp; Bubble Sort</a>
    <a href="#q5" class="jump-pill">ข้อ 5 Topological Sort in DAG</a>
    <a href="#q6" class="jump-pill">ข้อ 6 Unweighted Shortest Path</a>
    <a href="#q7" class="jump-pill">ข้อ 7 Properties &amp; Theory Calculations</a>
  </div>
"""

# Insert quick_nav right after the h1 heading
h1_close = tab1_content.find("</h1>") + 5
tab1_content = tab1_content[:h1_close] + "\n\n" + quick_nav + tab1_content[h1_close:]

# 2. Add Reference Citations
citations = {
    '<h2 id="q1" class="part-title">': '<h2 id="q1" class="part-title">Question 1: Hashing &amp; Open Addressing (Double Hashing) (18 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (Hashing), pp. 195-212 / สไลด์ Hashing อ.ประดิษฐ์</div>',
    '<h2 id="q2" class="part-title">': '<h2 id="q2" class="part-title">Question 2: Priority Queue (Binary Min-Heap) (10 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 6 (Priority Queues), pp. 243-260 / สไลด์ Priority Queues อ.ประดิษฐ์ ภาพที่ 7-9</div>',
    '<h2 id="q3" class="part-title">': '<h2 id="q3" class="part-title">Question 3: Insertion Sort Tracing &amp; Position Moves (10 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 281-285 / สไลด์ Insertion Sort อ.ประดิษฐ์</div>',
    '<h2 id="q4" class="part-title">': '<h2 id="q4" class="part-title">Question 4: Selection Sort &amp; Bubble Sort Tracing (10 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 285-290 / สไลด์ Selection &amp; Bubble Sort อ.ประดิษฐ์</div>',
    '<h2 id="q5" class="part-title">': '<h2 id="q5" class="part-title">Question 5: Topological Sort in DAG (10 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 367-374 / สไลด์ Topological Sort อ.ประดิษฐ์</div>',
    '<h2 id="q6" class="part-title">': '<h2 id="q6" class="part-title">Question 6: Unweighted Shortest Path (10 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 374-381 / สไลด์ Shortest Path อ.ประดิษฐ์</div>',
    '<h2 id="q7" class="part-title">': '<h2 id="q7" class="part-title">Question 7: Properties &amp; Theory Calculations (10 คะแนน)</h2>\n  <div class="ref-tag">📖 อ้างอิง: Weiss Chapters 4, 5, 6, 7, 9 / สไลด์สรุปเนื้อหา อ.ประดิษฐ์</div>'
}

for old_h, new_h in citations.items():
    # Replace the entire h2 line
    m = re.search(re.escape(old_h[:-1]) + r'[^>]*>', tab1_content)
    if m:
        orig = tab1_content[m.start():tab1_content.find("</h2>", m.start()) + 5]
        tab1_content = tab1_content.replace(orig, new_h, 1)

# 3. Add Sub-questions 1.5, 1.6, 1.7, 1.8 in Question 1
q1_extras = """  <!-- SUB-QUESTION 1.5: WRAP AROUND -->
  <h3 class="question-title">
    <span>1.5 หลักการ Wrap Around ใน Hashing &amp; Circular Queue / Wrap Around Principle</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Define the <strong>Wrap Around</strong> principle in Open Addressing Hashing and explain the mathematical reason why <code>mod TableSize</code> is used.</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> จงอธิบายหลักการ <strong>Wrap Around</strong> ในการทำ Hashing ตามนิยามภาษาอังกฤษและหลักการทางคณิตศาสตร์ที่อาจารย์เน้นในห้องเรียน
  </div>
  <div class="blank-sheet-box compact">
    <p style="margin:0; font-size:14px; line-height:2;">
      นิยามภาษาอังกฤษ: "When the key was mapped to the last index of hash table, ...................................................................."<br>
      คำอธิบายภาษาไทย: เมื่อการค้นหาหรือก้าวเดินคำนวณตำแหน่งโพรบเกินช่องสุดท้ายของตาราง ให้วนกลับมาที่ .............................. โดยการ .................................................... อีกรอบหนึ่ง
    </p>
  </div>

  <!-- SUB-QUESTION 1.6: HOW TO CHOOSE NEW TABLESIZE -->
  <h3 class="question-title">
    <span>1.6 การเลือกขนาดตารางใหม่เมื่อทำ Rehashing / How to Choose a New TableSize is...</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> State the rule for <em>"How to choose a new TableSize is..."</em>. For $\text{OldTableSize} = 19$, calculate the exact new TableSize.</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> จงเขียนนิยามภาษาอังกฤษและสูตรการเลือก New TableSize สำหรับการทำ Rehashing และหากขนาดตารางเดิมคือ <strong>19</strong> ช่อง ขนาดตารางใหม่ที่ถูกต้องคือเท่าใด?
  </div>
  <div class="blank-sheet-box compact">
    <p style="margin:0; font-size:14px; line-height:2;">
      หลักการตามสไลด์: "How to choose a new TableSize is ....................................................................................................."<br>
      ขนาดตารางเดิม = 19 &rarr; $2 \\times 19 = 38$ &rarr; ขนาดตารางใหม่คือ <strong>............</strong> (ต้องเป็นจำนวนเฉพาะที่ &ge; 38)
    </p>
  </div>

  <!-- SUB-QUESTION 1.7: HOW TO CHOOSE R -->
  <h3 class="question-title">
    <span>1.7 การเลือกค่า R ในสูตร Double Hashing / How to Choose R for Double Hashing</span>
    <span class="score-badge">Score: 2 Marks (2 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> What are the strict mathematical conditions for choosing parameter $R$ in $hash_2(X) = R - (X \bmod R)$? If TableSize is <strong>11</strong>, what is $R$?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> เงื่อนไขการเลือกค่า $R$ ในสูตร Double Hashing มีอะไรบ้าง? และหาก TableSize เป็น <strong>11</strong> จะต้องเลือกค่า $R$ เป็นเท่าใด (ห้ามเลือก 11 เพราะเหตุใด)?
  </div>
  <div class="blank-sheet-box compact">
    <p style="margin:0; font-size:14px; line-height:2;">
      เงื่อนไขของค่า R: (1) ต้องเป็น .................................................... (2) ต้องมีค่า .................................................... TableSize<br>
      สำหรับ TableSize = 11 จะต้องเลือกค่า $R =$ ............ (ห้ามเลือก 11 เด็ดขาด เพราะ ....................................................)
    </p>
  </div>

  <!-- SUB-QUESTION 1.8: LOAD FACTOR PERCENTAGE -->
  <h3 class="question-title">
    <span>1.8 การคำนวณร้อยละข้อมูลในตาราง / Load Factor Percentage Calculation</span>
    <span class="score-badge">Score: 2 Marks (2 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> What is the current load factor percentage ($\lambda$) of the Hash Table with 8 keys? What percentage triggers Rehashing (> 80%)?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> จงคำนวณร้อยละข้อมูลในตาราง (Load Factor $\lambda$) ขณะที่มี 8 คีย์ และร้อยละเมื่อมีข้อมูลครบ 16 คีย์ที่ทำให้เกิดการ Rehash
  </div>
  <div class="blank-sheet-box compact">
    <p style="margin:0; font-size:14px; line-height:2;">
      ร้อยละขณะมี 8 คีย์: $\\lambda = \\frac{8}{19} \\times 100\\% = $ ............ %<br>
      ร้อยละขณะมี 16 คีย์: $\\lambda = \\frac{16}{19} \\times 100\\% = $ ............ % (&gt; 80% เกิด Rehash)
    </p>
  </div>
"""

# Insert before Question 1 solution box
target_q1_sol = '<div class="solution-box">'
idx_q1_sol = tab1_content.find(target_q1_sol)
tab1_content = tab1_content[:idx_q1_sol] + q1_extras + tab1_content[idx_q1_sol:]

# Add solutions for 1.5 - 1.8 into Question 1 solution box
sol1_add = """      <li><strong>ข้อ 1.5 นิยาม Wrap Around:</strong> <em>"When the key was mapped to the last index of hash table, it go back to the first index of hash table by mod tablesize one more time."</em><br>
        (ภาษาไทย: เมื่อคีย์ถูกแม็ปไปถึงตำแหน่งท้ายของ hash table แล้ว ให้วนกลับมาตำแหน่งที่ 0 ใหม่ โดยการ mod tablesize อีกรอบหนึ่ง)</li>
      <li><strong>ข้อ 1.6 การเลือก New TableSize:</strong> <em>"Choose the smallest prime number but greater than or equal to double of the TableSize of the old Hash Table."</em><br>
        (เลือกจำนวนเฉพาะที่น้อยที่สุดแต่มากกว่าหรือเท่ากับ 2 เท่าของตารางเดิม &rarr; $2 \\times 19 = 38$ &rarr; จำนวนเฉพาะถัดไปคือ <strong>41</strong>)</li>
      <li><strong>ข้อ 1.7 การเลือกค่า R:</strong> $R$ ต้องเป็นจำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize อย่างเคร่งครัด ($R &lt; \\text{TableSize}$)<br>
        สำหรับ TableSize = 19 เลือก $R = 17$ | สำหรับ TableSize = 11 ต้องเลือก <strong>$R = 7$</strong> (ห้ามเลือก 11 เพราะจะทำให้ mod 11 ได้ 0 ซึ่งก้าวเดิน $hash_2 = 0$)</li>
      <li><strong>ข้อ 1.8 การคำนวณร้อยละ:</strong><br>
        • ปัจจุบัน 8 คีย์: $\\lambda = \\frac{8}{19} \\times 100\\% = \mathbf{42.11\\%}$<br>
        • เมื่อเกิด Rehash (16 คีย์): $\\lambda = \\frac{16}{19} \\times 100\\% = \mathbf{84.21\\%}$ (&gt; 80%)</li>
    </ul>"""

tab1_content = tab1_content.replace("</ul>\n  </div>\n\n  <!-- QUESTION 2 -->", sol1_add + "\n  </div>\n\n  <!-- QUESTION 2 -->")

# 4. In Question 3, add 3.2 Worst/Average/Best case
q3_extras = """  <!-- SUB-QUESTION 3.2: SORTING CASES -->
  <h3 class="question-title">
    <span>3.2 วิเคราะห์ Worst-Case, Average-Case และ Best-Case ของ Insertion Sort</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Compare the Best-Case, Average-Case, and Worst-Case time complexities of Insertion Sort. State the exact formula for position moves for each case.</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> จงเปรียบเทียบ Time Complexity และสูตรการคำนวณจำนวนครั้งการย้ายตำแหน่ง (Position Moves) ของ Insertion Sort ทั้ง 3 กรณี: Best Case, Average Case, และ Worst Case
  </div>
  <div class="blank-sheet-box compact">
    <p style="margin:0; font-size:14px; line-height:2;">
      Best Case: $O(......)$ สูตรการย้ายตำแหน่ง: ...... ครั้ง (ข้อมูลเรียงลำดับอยู่แล้ว)<br>
      Average Case: $O(......)$ สูตรการย้ายตำแหน่ง: $\\approx \\frac{N(N-1)}{......}$ ครั้ง<br>
      Worst Case: $O(......)$ สูตรการย้ายตำแหน่ง: $\\frac{N(N-1)}{......}$ ครั้ง (ข้อมูลเรียงจากมากไปน้อย)
    </p>
  </div>
"""

# Insert before Question 3 solution box
idx_q3 = tab1_content.find('<h2 id="q3"')
idx_q3_sol = tab1_content.find('<div class="solution-box">', idx_q3)
tab1_content = tab1_content[:idx_q3_sol] + q3_extras + tab1_content[idx_q3_sol:]

# Add 3.2 solution into Question 3 solution box
sol3_add = """    <p><strong>3.2 สรุปกรณีทั้ง 3 ของ Insertion Sort:</strong></p>
    <ul>
      <li><strong>Best Case:</strong> $O(N)$ เมื่อข้อมูลเรียงจากน้อยไปมากอยู่แล้ว เกิดการเปรียบเทียบ $N-1$ ครั้ง และ Position Move = <strong>0 ครั้ง</strong> (ไม่ต้องเลื่อนสมาชิกตัวอื่นเลย)</li>
      <li><strong>Average Case:</strong> $O(N^2)$ เมื่อข้อมูลเป็น Random Permutation เฉลี่ยแต่ละตัวต้องเลื่อนถอยหลังครึ่งหนึ่ง เกิด Move $\\approx \\frac{N(N-1)}{4}$ ครั้ง</li>
      <li><strong>Worst Case:</strong> $O(N^2)$ เมื่อข้อมูลเรียงกลับหลังจากมากไปน้อย ทุกตัวต้องเลื่อนถอยหลังจนสุด เกิด Move $= \\frac{N(N-1)}{2}$ ครั้ง ($N=10 \\implies 45$ ครั้ง)</li>
    </ul>
"""

tab1_content = tab1_content.replace('<div class="solution-title">💡 เฉลยละเอียดข้อ 3 (Complete Insertion Sort Solution):</div>', '<div class="solution-title">💡 เฉลยละเอียดข้อ 3 (Complete Insertion Sort Solution):</div>\n' + sol3_add)

# 5. In Question 4, add 4.2 Swaps = Inversions & Cases
q4_extras = """  <!-- SUB-QUESTION 4.2: BUBBLE & SELECTION CASES -->
  <h3 class="question-title">
    <span>4.2 ความสัมพันธ์ Swaps = Inversions และการเปรียบเทียบเคส Bubble &amp; Selection Sort</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Why is the number of swaps in Bubble Sort strictly equal to the number of inversions? Compare the comparisons and swaps of Selection Sort with Bubble Sort.</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> เหตุใดจำนวนครั้งการสลับที่ (Swaps) ของ Bubble Sort จึงเท่ากับจำนวน Inversions เสมอ? และเปรียบเทียบจำนวนการเปรียบเทียบและการสลับของ Selection Sort กับ Bubble Sort
  </div>
  <div class="blank-sheet-box compact">
    <p style="margin:0; font-size:14px; line-height:2;">
      ความสัมพันธ์ Swaps กับ Inversions: เพราะการสลับของข้อมูลที่ติดกัน 1 ครั้ง จะลดจำนวน Inversion ลงได้ ............ คู่<br>
      Selection Sort Comparisons: มีค่าเท่ากับ ........................................ เสมอทุกกรณี ไม่ว่าข้อมูลจะเรียงแบบใด<br>
      Selection Sort Swaps: เกิดขึ้นอย่างมากที่สุด ........................................ ครั้ง เหมาะสำหรับกรณีที่การเขียนข้อมูลลงหน่วยความจำมีต้นทุนสูง
    </p>
  </div>
"""

idx_q4 = tab1_content.find('<h2 id="q4"')
idx_q4_sol = tab1_content.find('<div class="solution-box">', idx_q4)
tab1_content = tab1_content[:idx_q4_sol] + q4_extras + tab1_content[idx_q4_sol:]

sol4_add = """    <p><strong>4.2 สรุปทฤษฎี Bubble Sort &amp; Selection Sort:</strong></p>
    <ul>
      <li><strong>Bubble Sort Swaps = Inversions:</strong> เพราะการสลับข้อมูลที่อยู่ติดกัน 1 ครั้ง สามารถกำจัดคู่ที่สลับลำดับกัน (Inversion) ได้ทีละ <strong>1 คู่พอดี</strong> ดังนั้นจำนวน Swaps จึงเท่ากับจำนวน Inversions ในอาร์เรย์เริ่มต้นเสมอ</li>
      <li><strong>Selection Sort Comparisons:</strong> ทำการเปรียบเทียบ $\\frac{N(N-1)}{2}$ ครั้ง <strong>เท่ากันเสมอในทุกกรณี</strong> (Best, Average, Worst) เพราะต้องสแกนหาตัวน้อยที่สุดจนสุดอาร์เรย์เสมอ</li>
      <li><strong>Selection Sort Swaps:</strong> เกิดการสลับอย่างมากที่สุดเพียง $N-1$ ครั้ง ทำให้ Selection Sort มีจำนวนการเขียนหน่วยความจำน้อยที่สุด เหมาะกับหน่วยความจำประเภท Flash หรือ EEPROM ที่การเขียนมีราคาแพง</li>
    </ul>
"""

tab1_content = tab1_content.replace('<div class="solution-title">💡 เฉลยละเอียดข้อ 4 (Selection &amp; Bubble Sort Tracing):</div>', '<div class="solution-title">💡 เฉลยละเอียดข้อ 4 (Selection &amp; Bubble Sort Tracing):</div>\n' + sol4_add)

# Wrap inside <div id="tab-2026" class="tab-content active"> ... </div>
final_tab1_html = '  <!-- ========================================================================= -->\n' + \
                  '  <!-- TAB 1: OFFICIAL FINAL EXAM 2026 SUITE (SET A)                           -->\n' + \
                  '  <!-- ========================================================================= -->\n' + \
                  '  <div id="tab-2026" class="tab-content active">\n' + \
                  tab1_content + \
                  '\n  </div> <!-- END TAB 1 -->\n'

# Write to generate_tab1.py
with open(r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py", "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""\nModule to generate HTML for Tab 1: Official Final Exam 2026 Suite\n"""\n\ndef get_tab1_html():\n    return """' + final_tab1_html + '"""\n')

print("generate_tab1.py generated successfully!")
