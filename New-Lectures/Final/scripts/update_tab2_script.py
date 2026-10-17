# -*- coding: utf-8 -*-
"""
Script to update generate_tab2.py by injecting sub-questions:
- Q1: 1.4 Wrap Around, 1.5 How to choose new TableSize is..., 1.6 How to choose R, 1.7 Load factor %
- Q3: 3.4 Best-case, Average-case, Worst-case in Insertion Sort
- Q7: 7.6 RAM Waste % in Adjacency Matrix, 7.7 Two & Three Properties
"""

import os

tab2_path = r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab2.py"

with open(tab2_path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. In Question 1, add 1.4 - 1.7 before '<!-- QUESTION 1 PAST SOLUTIONS -->'
q1_extras = """    <h3 class="question-title past-q">
      <span>1.4 หลักการ Wrap Around ใน Hashing &amp; Circular Array [ข้อเขียนสไลด์ อ.ประดิษฐ์]</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Explain the exact definition and mechanics of the <strong>Wrap Around</strong> principle in Open Addressing Hashing as stated in the lecture slides.</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> จงอธิบายหลักการ <strong>Wrap Around</strong> ในการทำ Hashing ตามนิยามภาษาอังกฤษและหลักการทางคณิตศาสตร์ที่อาจารย์สอนในห้องเรียน
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        นิยามภาษาอังกฤษ: "When the key was mapped to the last index of hash table, ...................................................................."<br>
        หลักการทางคณิตศาสตร์: อาศัยการนำตำแหน่งโพรบมาทำ .................................................................... อีกรอบหนึ่ง
      </p>
    </div>

    <h3 class="question-title past-q">
      <span>1.5 การเลือกขนาดตารางใหม่เมื่อทำ Rehashing (How to choose a new TableSize is...)</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> State the exact principle of <em>"How to choose a new TableSize is..."</em>. If the old TableSize is <strong>19</strong>, what is the exact new TableSize?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> จงเขียนนิยามและหลักการเลือก New TableSize สำหรับการทำ Rehashing และหากขนาดตารางเดิมคือ <strong>19</strong> ช่อง ขนาดตารางใหม่ที่ต้องเลือกคือเท่าใด?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        หลักการเลือก New TableSize: ........................................................................................................................<br>
        ตารางเดิมขนาด 19 &rarr; $2 \\times 19 = 38$ &rarr; ขนาดตารางใหม่ (New TableSize) คือ <strong>............</strong>
      </p>
    </div>

    <h3 class="question-title past-q">
      <span>1.6 การเลือกค่า R ในสูตร Double Hashing (How to choose R for Double Hashing)</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Why is $R = 17$ chosen for $\\text{TableSize} = 19$? If the TableSize was <strong>11</strong>, what value of $R$ must be chosen?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> เหตุใดในโจทย์ข้อนี้จึงเลือก $R = 17$ เมื่อ TableSize = 19? และหากตารางแฮชมีขนาด <strong>11</strong> ช่อง จะต้องเลือกค่า $R$ เป็นเท่าใด เพราะเหตุใด?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        เกณฑ์การเลือกค่า R: $R$ ต้องเป็นจำนวนเฉพาะที่ .................................................................... กับ TableSize<br>
        สำหรับ TableSize = 11 จะต้องเลือก $R =$ ............ (ห้ามเลือก 11 เด็ดขาด เพราะ ....................................................)
      </p>
    </div>

    <h3 class="question-title past-q">
      <span>1.7 การคำนวณร้อยละข้อมูลในตาราง (Load Factor Percentage &lambda;)</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Calculate the load factor percentage ($\\lambda$) of the Hash Table after inserting the 8 keys. What percentage is reached when the threshold triggers Rehashing?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> จงคำนวณร้อยละความจุข้อมูล (Load Factor $\\lambda$) หลังจากใส่ข้อมูลครบ 8 ตัว และร้อยละเมื่อใส่ครบจนเกิดการ Rehash (&gt; 75%)
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        ความจุข้อมูลปัจจุบัน (8 คีย์): $\\lambda = \\frac{8}{19} \\times 100\\% = $ ............ %<br>
        ความจุข้อมูล ณ จุดที่เกิด Rehash (15 คีย์): $\\lambda = \\frac{15}{19} \\times 100\\% = $ ............ % (&gt; 75%)
      </p>
    </div>

"""

if "1.4 หลักการ Wrap Around ใน Hashing" not in c:
    c = c.replace("<!-- QUESTION 1 PAST SOLUTIONS -->", q1_extras + "<!-- QUESTION 1 PAST SOLUTIONS -->")

# Update solutions of Q1
sol1_old = """      <p><strong>คำตอบข้อย่อย:</strong></p>
      <ul>
        <li><strong>ข้อ 1.2:</strong> จำนวนการชนกันทั้งสิ้น = $0 + 0 + 2 + 0 + 3 + 0 + 4 + 3 = \mathbf{12}$ ครั้ง (Key ที่ชนมากที่สุดคือ <strong>357</strong> ชน 4 ครั้ง ที่ช่อง 15, 13, 11, 9)</li>
        <li><strong>ข้อ 1.3:</strong> เกณฑ์ Rehashing คือ Load Factor เกิน 75% ของ TableSize 19:<br>
          $19 \times 0.75 = 14.25 \implies$ ต้องมีข้อมูลมากกว่า 14.25 ตัว คืออย่างน้อย <strong>15 ตัว</strong><br>
          ขณะนี้ใส่ไปแล้ว 8 ตัว &rarr; ดังนั้นต้องใส่ข้อมูลเพิ่มอีกอย่างน้อย $15 - 8 = \mathbf{7}$ ตัว จึงจะเกิดการ Rehashing
        </li>
      </ul>"""

sol1_new = """      <p><strong>คำตอบข้อย่อย:</strong></p>
      <ul>
        <li><strong>ข้อ 1.2:</strong> จำนวนการชนกันทั้งสิ้น = $0 + 0 + 2 + 0 + 3 + 0 + 4 + 3 = \mathbf{12}$ ครั้ง (Key ที่ชนมากที่สุดคือ <strong>357</strong> ชน 4 ครั้ง ที่ช่อง 15, 13, 11, 9)</li>
        <li><strong>ข้อ 1.3:</strong> เกณฑ์ Rehashing คือ Load Factor เกิน 75% ของ TableSize 19:<br>
          $19 \\times 0.75 = 14.25 \\implies$ ต้องมีข้อมูลมากกว่า 14.25 ตัว คืออย่างน้อย <strong>15 ตัว</strong><br>
          ขณะนี้ใส่ไปแล้ว 8 ตัว &rarr; ดังนั้นต้องใส่ข้อมูลเพิ่มอีกอย่างน้อย $15 - 8 = \mathbf{7}$ ตัว จึงจะเกิดการ Rehashing
        </li>
        <li><strong>ข้อ 1.4 นิยาม Wrap Around:</strong> <em>"When the key was mapped to the last index of hash table, it go back to the first index of hash table by mod tablesize one more time."</em><br>
          (ภาษาไทย: เมื่อคีย์ถูกแม็ปไปถึงตำแหน่งท้ายของ hash table แล้ว ให้วนกลับมาตำแหน่งที่ 0 ใหม่ โดยการ mod tablesize อีกรอบหนึ่ง)</li>
        <li><strong>ข้อ 1.5 การเลือก New TableSize:</strong> <em>"Choose the smallest prime number but greater than or equal to double of the TableSize of the old Hash Table."</em><br>
          (เลือกจำนวนเฉพาะที่น้อยที่สุดแต่มากกว่าหรือเท่ากับ 2 เท่าของตารางเดิม &rarr; $2 \\times 19 = 38$ &rarr; จำนวนเฉพาะถัดไปคือ <strong>41</strong>)</li>
        <li><strong>ข้อ 1.6 การเลือกค่า R:</strong> $R$ ต้องเป็นจำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize อย่างเคร่งครัด ($R &lt; \\text{TableSize}$)<br>
          สำหรับ TableSize = 19 เลือก $R = 17$ | สำหรับ TableSize = 11 ต้องเลือก <strong>$R = 7$</strong> (ห้ามเลือก 11 เพราะจะทำให้ mod 11 ได้ 0 ซึ่งก้าวเดิน $hash_2 = 0$)</li>
        <li><strong>ข้อ 1.7 การคำนวณร้อยละ:</strong><br>
          • ปัจจุบัน 8 คีย์: $\\lambda = \\frac{8}{19} \\times 100\\% = \mathbf{42.11\\%}$<br>
          • เมื่อเกิด Rehash (15 คีย์): $\\lambda = \\frac{15}{19} \\times 100\\% = \mathbf{78.95\\%}$ (&gt; 75%)</li>
      </ul>"""

if sol1_old in c:
    c = c.replace(sol1_old, sol1_new)

# 2. In Question 3, add 3.4
q3_extra = """    <h3 class="question-title past-q">
      <span>3.4 วิเคราะห์ Worst Case, Average Case และ Best Case ของ Insertion Sort</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
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

if "3.4 วิเคราะห์ Worst Case" not in c:
    c = c.replace('<h2 id="past-q4"', q3_extra + '<h2 id="past-q4"')

# Update solutions of Q3
sol3_target = '<div class="solution-title">💡 เฉลยละเอียดข้อ 3 (Insertion Sort Tracing &amp; Code Solutions):</div>'
sol3_extra = """      <p><strong>3.4 สรุปกรณีทั้ง 3 ของ Insertion Sort:</strong></p>
      <ul>
        <li><strong>Best Case:</strong> $O(N)$ เมื่อข้อมูลเรียงจากน้อยไปมากอยู่แล้ว เกิดการเปรียบเทียบ $N-1$ ครั้ง และ Position Move = <strong>0 ครั้ง</strong> (ไม่ต้องเลื่อนสมาชิกตัวอื่นเลย)</li>
        <li><strong>Average Case:</strong> $O(N^2)$ เมื่อข้อมูลเป็น Random Permutation เฉลี่ยแต่ละตัวต้องเลื่อนถอยหลังครึ่งหนึ่ง เกิด Move $\\approx \\frac{N(N-1)}{4}$ ครั้ง</li>
        <li><strong>Worst Case:</strong> $O(N^2)$ เมื่อข้อมูลเรียงกลับหลังจากมากไปน้อย ทุกตัวต้องเลื่อนถอยหลังจนสุด เกิด Move $= \\frac{N(N-1)}{2}$ ครั้ง ($N=12 \\implies 66$ ครั้ง)</li>
      </ul>
"""

if "3.4 สรุปกรณีทั้ง 3 ของ Insertion Sort" not in c and sol3_target in c:
    c = c.replace(sol3_target, sol3_target + "\n" + sol3_extra)

# 3. In Question 7, add 7.6 and 7.7
q7_extra = """    <h3 class="question-title past-q">
      <span>7.6 การคำนวณร้อยละความสูญเสียในหน่วยความจำของ Adjacency Matrix [สไลด์ Graph อ.ประดิษฐ์]</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> กราฟมีทิศทางที่มี 7 โหนด และมีเส้นเชื่อม 12 เส้น หากจัดเก็บด้วย Adjacency Matrix ขนาด $7 \\times 7$ จงคำนวณร้อยละของพื้นที่หน่วยความจำที่ถูกใช้งานจริง (Used %) และร้อยละที่สูญเปล่า (Wasted %)
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <p>พื้นที่ทั้งหมดใน Matrix: $7 \\times 7 = \mathbf{49}$ ช่อง</p>
      <ul>
        <li><strong>พื้นที่ใช้งานจริง (มีเส้นเชื่อม Edge = 1):</strong> $\\frac{12}{49} \\times 100\\% = \mathbf{24.49\\%}$</li>
        <li><strong>พื้นที่สูญเปล่า (เป็น 0 ไม่มีเส้นเชื่อม):</strong> $\\frac{49 - 12}{49} \\times 100\\% = \\frac{37}{49} \\times 100\\% = \mathbf{75.51\\%}$</li>
      </ul>
    </div>

    <h3 class="question-title past-q">
      <span>7.7 คุณสมบัติ 2 ประการ และ 3 ประการ ของโครงสร้างข้อมูล (Two &amp; Three Properties)</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> โครงสร้างข้อมูลใดบ้างที่มีกฎหรือคุณสมบัติบังคับ 2 ประการ (Two Properties)? และโครงสร้างข้อมูลใดที่มีคุณสมบัติ 3 ประการ (Three Properties)? จงระบุชื่อและบอกคุณสมบัติแต่ละข้อ
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <ul>
        <li><strong>มี 2 คุณสมบัติ (Two Properties):</strong>
          <ul>
            <li><strong>Binary Min-Heap:</strong> (1) Structure Property (ต้องเป็น Complete Binary Tree), (2) Heap-Order Property (Parent &le; Children เสมอ)</li>
            <li><strong>Tree ในกราฟ:</strong> (1) Connected (ทุกโหนดเชื่อมโยงถึงกัน), (2) Acyclic (ไม่มีวงรอบ cycle เลย)</li>
            <li><strong>AVL Tree:</strong> (1) Binary Search Tree Property, (2) Balance Property ($|h_L - h_R| \\le 1$)</li>
          </ul>
        </li>
        <li><strong>มี 3 คุณสมบัติ (Three Properties):</strong>
          <ul>
            <li><strong>Ideal Hash Function:</strong> (1) Simple and fast to compute ($O(1)$), (2) Uniformly distributed (กระจายสม่ำเสมอทั่วตาราง), (3) No collisions (One-to-One mapping - ซึ่งเป็นไปไม่ได้จริงเพราะ Pigeonhole Principle)</li>
          </ul>
        </li>
      </ul>
    </div>
"""

if "7.6 การคำนวณร้อยละความสูญเสีย" not in c:
    c = c.replace("</div> <!-- END TAB 2 -->", q7_extra + "  </div> <!-- END TAB 2 -->")

with open(tab2_path, "w", encoding="utf-8") as f:
    f.write(c)

print("generate_tab2.py updated successfully!")
