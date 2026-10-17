# -*- coding: utf-8 -*-
"""
Module to generate HTML for Tab 2:
🏛️ ชุดที่ 2: ข้อสอบจริงย้อนหลังปี 2564 & 2561 (Real Past Exams 2564 & 2561 Suite)
Adheres strictly to the extracted text and images of past exams from Assoc. Prof. Dr. Pradit Pitaksatheinkul.
Includes both English statement and Thai translation, official blanks, and complete detailed solutions.
"""

def get_tab2_html():
    return r"""
  <!-- ========================================================================= -->
  <!-- TAB 2: REAL PAST FINAL EXAMS 2564 & 2561 SUITE                            -->
  <!-- ========================================================================= -->
  <div id="tab-past" class="tab-content">
    <h1 class="section-heading past-heading">
      🏛️ ชุดที่ 2: ข้อสอบปลายภาคฉบับจริงย้อนหลังปี 2564 &amp; 2561 (Real Past Exams Suite - รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล)
    </h1>

    <div class="rules-box" style="border-left-color:#0d9488; background:#f0fdfa;">
      <div class="rules-title" style="color:#0f766e;">📌 ข้อมูลเกี่ยวกับชุดข้อสอบจริงย้อนหลังปี 2564 และ 2561:</div>
      <p style="margin:4px 0; font-size:13.5px;">
        รวบรวมและถอดรหัสจากต้นฉบับข้อสอบจริงปี 2564 (ฉบับ 5 หน้า 7 ข้อ 80 คะแนน) และข้อสอบจริงปี 2561 พร้อมลายมือเฉลยของรุ่นพี่และสไลด์ประกอบการสอนของอาจารย์ ครอบคลุมทั้งตารางแนวนอน 19 ช่อง (Active 'A'), ตารางแนวตั้ง 4 ตารางของ Heap, การเขียนโปรแกรมแก้ Insertion Sort ให้นับ Position Moves, การ Trace Quicksort 17 ตัวด้วย Cutoff = 3, ตาราง Indegree ของ DAG, และตาราง BFS ของ Unweighted Shortest Path
      </p>
    </div>

    <!-- QUICK NAV FOR TAB 2 -->
    <div class="nav-jump-bar">
      <span class="nav-jump-label">⚡ ทางลัดข้อสอบชุดย้อนหลัง:</span>
      <a href="#past-q1" class="jump-pill alt">ข้อ 1 Hashing 2561/2564</a>
      <a href="#past-q2" class="jump-pill alt">ข้อ 2 Binary Min-Heap (4 ตารางแนวตั้ง + Tracing hole)</a>
      <a href="#past-q3" class="jump-pill alt">ข้อ 3 Insertion Sort (Worst Case &amp; แก้โปรแกรมนับ Move)</a>
      <a href="#past-q4" class="jump-pill alt">ข้อ 4 Quicksort 17 ตัว &amp; Bubble Inversions</a>
      <a href="#past-q5" class="jump-pill alt">ข้อ 5 Topological Sort (Indegree Array &amp; Queue)</a>
      <a href="#past-q6" class="jump-pill alt">ข้อ 6 Unweighted Shortest Path</a>
      <a href="#past-q7" class="jump-pill alt">ข้อ 7 ทฤษฎีข้อเขียน 2564/2561</a>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 1: HASHING (PAST EXAMS 2561 & 2564)                              -->
    <!-- ========================================================================= -->
    <h2 id="past-q1" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 1 (Past Exams): Hashing &amp; Open Addressing (Double Hashing 2561 &amp; 2564) (18 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (Hashing), pp. 195-208 / ข้อสอบจริงปี 2561 หน้า 1-3 &amp; ข้อสอบจริงปี 2564 หน้า 1, 6, 14</div>

    <h3 class="question-title past-q">
      <span>1.1 Double Hashing Table (8 Keys, TableSize = 19, Rehash &gt; 75%) [ข้อสอบจริงปี 2561 หน้า 1]</span>
      <span class="score-badge past-badge">Score: 10 Marks (10 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given an empty Hash Table of size $\text{TableSize} = 19$ (indexed from $0$ to $18$) in Python using Open Addressing with <strong>Double Hashing</strong> where probe step function is defined as $f(i) = i \times \text{hash}_2(X)$. Rehashing is triggered when the load factor strictly exceeds <strong>75%</strong>.</p>
    <p>Insert the following 8 keys sequentially into the hash table:</p>
    $$\mathbf{323, 17, 969, 868, 340, 370, 357, 391}$$
    <p>Show the step-by-step probe calculations for each key, determine the appropriate prime constant $R$, and fill the resulting Hash Table array in Python (empty slots remain <code>None</code>).</p>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2561 หน้า 1):</strong> โครงสร้าง Hash Table ชนิด Open Addressing กำหนดวิธีการแก้การชนกันเป็นแบบ Double Hashing กำหนด TableSize ให้เป็น 19 คิดเปอร์เซ็นต์ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่มากกว่า 75% ให้นักศึกษาทำการ insert ข้อมูลจำนวน 8 ตัว ดังต่อไปนี้: <strong>323, 17, 969, 868, 340, 370, 357, 391</strong> เข้าไปใน HashTable ดังกล่าว โดยแสดงวิธีคิดการคำนวณการชนและการแก้การชน และนำตัวเลขมาใส่ในตาราง Hash Table ในภาษา Python (ช่องว่างเก็บ None)
    </div>

    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#0f766e; margin-bottom:6px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 1.1: ตารางแฮชขนาด 19 ช่อง (ดัชนี 0 ถึง 18 พร้อมฟิลด์ Element และ Info ตามข้อสอบจริง)
      </div>
      <table style="text-align:center; font-size:12px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:95px; text-align:center;">Slot</th>
            <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Value (Key)</td>
            <td style="height:32px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          </tr>
        </tbody>
      </table>
      <table style="text-align:center; font-size:12px; margin-top:8px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:95px; text-align:center;">Slot</th>
            <th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th><th>[16]</th><th>[17]</th><th>[18]</th><th style="background:#475569;">-</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Value (Key)</td>
            <td style="height:32px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#f1f5f9;">-</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="question-title past-q">
      <span>1.2 จำนวนการชนและแก้การชนทั้งสิ้น / Total Collisions [ข้อสอบจริงปี 2561 หน้า 3]</span>
      <span class="score-badge past-badge">Score: 4 Marks (4 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> After inserting all 8 keys into the Hash Table, how many total collisions and collision resolution steps occurred?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2561 หน้า 3 ข้อ 1.2):</strong> หลังจากใส่ข้อมูลลงใน Hash Table ดังกล่าว ครบทุกตัว ถามว่า เกิดการชนกันและแก้การชนกันทั้งสิ้นกี่ครั้ง?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14.5px;">ตอบ เกิดการชนกันและแก้การชนกันทั้งสิ้น ............ ครั้ง</p>
    </div>

    <h3 class="question-title past-q">
      <span>1.3 จำนวนข้อมูลที่ต้องใส่เพิ่มจนเกิด Rehashing / Additional Keys for Rehashing [ข้อสอบจริงปี 2561 หน้า 3]</span>
      <span class="score-badge past-badge">Score: 4 Marks (4 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> If Rehashing is triggered when the load factor strictly exceeds <strong>75%</strong> of $\text{TableSize} = 19$, how many <em>additional</em> keys must be inserted before rehashing occurs?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2561 หน้า 3 ข้อ 1.3):</strong> หลังจากใส่ข้อมูลลงใน Hash Table ดังกล่าวครบทุกตัว ต้องใส่ข้อมูลเพิ่มอย่างน้อยกี่ตัวถึงจะมีการ Rehashing?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14.5px;">ตอบ ต้องใส่ข้อมูลเพิ่มอีกอย่างน้อย ............ ตัว ถึงจะเกิดการ Rehashing</p>
    </div>

        <h3 class="question-title past-q">
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
        ตารางเดิมขนาด 19 &rarr; $2 \times 19 = 38$ &rarr; ขนาดตารางใหม่ (New TableSize) คือ <strong>............</strong>
      </p>
    </div>

    <h3 class="question-title past-q">
      <span>1.6 กฎการเลือกค่า R ในสูตร Double Hashing (How to choose constant R)</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> State the rule for choosing the prime constant $R$ in Double Hashing. What value of $R$ is chosen when $\text{TableSize} = 19$? If $\text{TableSize} = 11$, what value of $R$ must be chosen and why?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> จงระบุกฎเกณฑ์ในการเลือกค่าคงที่ $R$ ใน Double Hashing, สำหรับ TableSize = 19 จะได้ค่า $R$ เป็นเท่าใด? และหากตารางมีขนาด 11 ช่อง จะต้องเลือกค่า $R$ เป็นเท่าใด เพราะเหตุใด?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        เกณฑ์การเลือกค่า R: $R$ ต้องเป็นจำนวนเฉพาะที่ .................................................................... กับ TableSize<br>
        สำหรับ TableSize = 19 จะได้ค่า $R =$ ............ | สำหรับ TableSize = 11 จะต้องเลือก $R =$ ............ (เพราะ ....................................................)
      </p>
    </div>

    <h3 class="question-title past-q">
      <span>1.7 การคำนวณร้อยละข้อมูลในตาราง (Load Factor Percentage &lambda;)</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Calculate the load factor percentage ($\lambda$) of the Hash Table after inserting the 8 keys. What percentage is reached when the threshold triggers Rehashing?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> จงคำนวณร้อยละความจุข้อมูล (Load Factor $\lambda$) หลังจากใส่ข้อมูลครบ 8 ตัว และร้อยละเมื่อใส่ครบจนเกิดการ Rehash (&gt; 75%)
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        ความจุข้อมูลปัจจุบัน (8 คีย์): $\lambda = \frac{8}{19} \times 100\% = $ ............ %<br>
        ความจุข้อมูล ณ จุดที่เกิด Rehash (15 คีย์): $\lambda = \frac{15}{19} \times 100\% = $ ............ % (&gt; 75%)
      </p>
    </div>

<!-- QUESTION 1 PAST SOLUTIONS -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดและวิธีคำนวณทีละขั้นตอน (Complete Past Exam 2561 Solution):</div>
      <p><strong>สูตรก้าวเดิน:</strong> $s(X) = 17 - (X \bmod 17)$, ฟังก์ชันหลัก: $h_0(X) = X \bmod 19$</p>
      <ul>
        <li><strong>Key 323:</strong> $h_0(323) = 323 \bmod 19 = \mathbf{0}$ &rarr; ช่อง 0 ว่าง &rarr; บรรจุลง <strong>ช่อง 0</strong> (Info: A, ชน 0 ครั้ง) [ก้าวเดิน $s=17-(323\bmod 17)=17-0=17$]</li>
        <li><strong>Key 17:</strong> $h_0(17) = 17 \bmod 19 = \mathbf{17}$ &rarr; ช่อง 17 ว่าง &rarr; บรรจุลง <strong>ช่อง 17</strong> (Info: A, ชน 0 ครั้ง) [ก้าวเดิน $s=17-0=17$]</li>
        <li><strong>Key 969:</strong> $h_0(969) = 969 \bmod 19 = \mathbf{0}$ &rarr; <em>ชนกับ 323 ที่ช่อง 0!</em> (ชนครั้งที่ 1)<br>
          ก้าวเดิน $s = 17 - (969 \bmod 17) = 17 - 0 = \mathbf{17}$<br>
          $h_1(969) = (0 + 1 \times 17) \bmod 19 = \mathbf{17}$ &rarr; <em>ชนกับ 17 ที่ช่อง 17!</em> (ชนครั้งที่ 2)<br>
          $h_2(969) = (0 + 2 \times 17) \bmod 19 = 34 \bmod 19 = \mathbf{15}$ &rarr; ช่อง 15 ว่าง! บรรจุลง <strong>ช่อง 15</strong> (Info: A, ชน 2 ครั้ง)
        </li>
        <li><strong>Key 868:</strong> $h_0(868) = 868 \bmod 19 = \mathbf{13}$ &rarr; ช่อง 13 ว่าง &rarr; บรรจุลง <strong>ช่อง 13</strong> (Info: A, ชน 0 ครั้ง) [ก้าวเดิน $s=17-(868\bmod 17)=17-1=16$]</li>
        <li><strong>Key 340:</strong> $h_0(340) = 340 \bmod 19 = \mathbf{17}$ &rarr; <em>ชนกับ 17 ที่ช่อง 17!</em> (ชนครั้งที่ 1)<br>
          ก้าวเดิน $s = 17 - (340 \bmod 17) = 17 - 0 = \mathbf{17}$<br>
          $h_1(340) = (17 + 17) \bmod 19 = 34 \bmod 19 = \mathbf{15}$ &rarr; <em>ชนกับ 969 ที่ช่อง 15!</em> (ชนครั้งที่ 2)<br>
          $h_2(340) = (17 + 34) \bmod 19 = 51 \bmod 19 = \mathbf{13}$ &rarr; <em>ชนกับ 868 ที่ช่อง 13!</em> (ชนครั้งที่ 3)<br>
          $h_3(340) = (17 + 51) \bmod 19 = 68 \bmod 19 = \mathbf{11}$ &rarr; ช่อง 11 ว่าง! บรรจุลง <strong>ช่อง 11</strong> (Info: A, ชน 3 ครั้ง)
        </li>
        <li><strong>Key 370:</strong> $h_0(370) = 370 \bmod 19 = \mathbf{9}$ &rarr; ช่อง 9 ว่าง &rarr; บรรจุลง <strong>ช่อง 9</strong> (Info: A, ชน 0 ครั้ง) [ก้าวเดิน $s=17-(370\bmod 17)=17-13=4$]</li>
        <li><strong>Key 357:</strong> $h_0(357) = 357 \bmod 19 = \mathbf{15}$ &rarr; <em>ชนกับ 969 ที่ช่อง 15!</em> (ชนครั้งที่ 1)<br>
          ก้าวเดิน $s = 17 - (357 \bmod 17) = 17 - 0 = \mathbf{17}$<br>
          $h_1(357) = (15 + 17) \bmod 19 = 32 \bmod 19 = \mathbf{13}$ &rarr; <em>ชนกับ 868 ที่ช่อง 13!</em> (ชนครั้งที่ 2)<br>
          $h_2(357) = (15 + 34) \bmod 19 = 49 \bmod 19 = \mathbf{11}$ &rarr; <em>ชนกับ 340 ที่ช่อง 11!</em> (ชนครั้งที่ 3)<br>
          $h_3(357) = (15 + 51) \bmod 19 = 66 \bmod 19 = \mathbf{9}$ &rarr; <em>ชนกับ 370 ที่ช่อง 9!</em> (ชนครั้งที่ 4)<br>
          $h_4(357) = (15 + 68) \bmod 19 = 83 \bmod 19 = \mathbf{7}$ &rarr; ช่อง 7 ว่าง! บรรจุลง <strong>ช่อง 7</strong> (Info: A, ชน 4 ครั้ง)
        </li>
        <li><strong>Key 391:</strong> $h_0(391) = 391 \bmod 19 = \mathbf{11}$ &rarr; <em>ชนกับ 340 ที่ช่อง 11!</em> (ชนครั้งที่ 1)<br>
          ก้าวเดิน $s = 17 - (391 \bmod 17) = 17 - 0 = \mathbf{17}$<br>
          $h_1(391) = (11 + 17) \bmod 19 = 28 \bmod 19 = \mathbf{9}$ &rarr; <em>ชนกับ 370 ที่ช่อง 9!</em> (ชนครั้งที่ 2)<br>
          $h_2(391) = (11 + 34) \bmod 19 = 45 \bmod 19 = \mathbf{7}$ &rarr; <em>ชนกับ 357 ที่ช่อง 7!</em> (ชนครั้งที่ 3)<br>
          $h_3(391) = (11 + 51) \bmod 19 = 62 \bmod 19 = \mathbf{5}$ &rarr; ช่อง 5 ว่าง! บรรจุลง <strong>ช่อง 5</strong> (Info: A, ชน 3 ครั้ง)
        </li>
      </ul>

      <p><strong>สรุปผลตาราง Hash Table สุดท้าย:</strong></p>
      <ul>
        <li>ช่อง 0 = <strong>323</strong> (A) | ช่อง 5 = <strong>391</strong> (A) | ช่อง 7 = <strong>357</strong> (A) | ช่อง 9 = <strong>370</strong> (A) | ช่อง 11 = <strong>340</strong> (A) | ช่อง 13 = <strong>868</strong> (A) | ช่อง 15 = <strong>969</strong> (A) | ช่อง 17 = <strong>17</strong> (A)</li>
        <li>ช่องว่างอื่นๆ (1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18) = ว่าง (EMPTY)</li>
      </ul>

      <p><strong>คำตอบข้อย่อย:</strong></p>
      <ul>
        <li><strong>ข้อ 1.2:</strong> จำนวนการชนกันทั้งสิ้น = $0 + 0 + 2 + 0 + 3 + 0 + 4 + 3 = \mathbf{12}$ ครั้ง (Key ที่ชนมากที่สุดคือ <strong>357</strong> ชน 4 ครั้ง ที่ช่อง 15, 13, 11, 9)</li>
        <li><strong>ข้อ 1.3:</strong> เกณฑ์ Rehashing คือ Load Factor เกิน 75% ของ TableSize 19:<br>
          $19 \times 0.75 = 14.25 \implies$ ต้องมีข้อมูลมากกว่า 14.25 ตัว คืออย่างน้อย <strong>15 ตัว</strong><br>
          ขณะนี้ใส่ไปแล้ว 8 ตัว &rarr; ดังนั้นต้องใส่ข้อมูลเพิ่มอีกอย่างน้อย $15 - 8 = \mathbf{7}$ ตัว จึงจะเกิดการ Rehashing
        </li>
      </ul>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 2: BINARY HEAP (PAST EXAMS 2564 & 2561 & LECTURE TRACE)          -->
    <!-- ========================================================================= -->
    <h2 id="past-q2" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 2 (Past Exams): Priority Queue (Binary Min-Heap) 4 Vertical Arrays &amp; Tracing (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 6 (Heaps), pp. 244-255 / ข้อสอบจริงปี 2564 หน้า 6 &amp; สไลด์ อ.ประดิษฐ์ สัปดาห์ที่ 10</div>

    <h3 class="question-title past-q">
      <span>2.1 Four Vertical Arrays Simulation (12 Keys, deleteMin, insert 3, deleteMin) [ข้อสอบจริงปี 2564 หน้า 6]</span>
      <span class="score-badge past-badge">Score: 8 Marks (8 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Draw 4 vertical array tables representing the Binary Min-Heap state according to the following 4 phases:</p>
    <ul>
      <li><strong>2.1.1:</strong> Insert the following 12 keys sequentially into an empty Min-Heap: <code>64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20</code> (Show the final array state in Table 1).</li>
      <li><strong>2.1.2:</strong> Perform <code>deleteMin()</code> once. Write the resulting array in Table 2.</li>
      <li><strong>2.1.3:</strong> Insert key <code>3</code>. Write the resulting array in Table 3.</li>
      <li><strong>2.1.4:</strong> Perform <code>deleteMin()</code> once more. Write the resulting array in Table 4.</li>
    </ul>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2564 หน้า 6 ข้อ 2):</strong> ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Binary Heap เป็นแนวตั้ง 4 ตาราง เพื่อรองรับข้อมูล:<br>
      2.1 จงใส่ข้อมูลตัวเลขต่อไปนี้: <strong>64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20</strong> เข้าไปในตารางอะเรย์ โดยเขียนเฉพาะผลลัพธ์สุดท้ายที่ Insert ข้อมูลเสร็จแล้วเท่านั้น ในตารางแรก<br>
      2.2 ให้ทำการ deleteMin 1 ครั้ง แล้วเขียนผลลัพธ์ลงในตารางอะเรย์ ที่ 2<br>
      2.3 หลังจากนั้นให้ทำการ insert ข้อมูลตัวเลข 3 เข้าไป เขียนผลในตารางอะเรย์ ที่ 3<br>
      2.4 หลังจากนั้น ให้ทำการ deleteMin อีกครั้ง แล้วเขียนผลลัพธ์ลงในตารางอะเรย์ ที่ 4
    </div>

    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#0f766e; margin-bottom:8px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 2.1: ตารางอะเรย์แนวตั้ง 4 ชุด (ดัชนี 0 ถึง 12 ตามมาตรฐานข้อสอบจริงปี 2564)
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px; text-align:center;">
        <div>
          <div style="background:#0f766e; color:white; padding:4px; font-weight:bold; font-size:12px; border-radius:4px 4px 0 0;">ตารางที่ 1: Insert 12 ตัว</div>
          <table style="margin:0; font-size:12px;">
            <tr><th style="width:50px;">Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">- (เว้นว่าง)</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td></td></tr>
          </table>
        </div>
        <div>
          <div style="background:#0f766e; color:white; padding:4px; font-weight:bold; font-size:12px; border-radius:4px 4px 0 0;">ตารางที่ 2: deleteMin() ครั้งที่ 1</div>
          <table style="margin:0; font-size:12px;">
            <tr><th style="width:50px;">Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">- (เว้นว่าง)</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td style="background:#f1f5f9;">-</td></tr>
          </table>
        </div>
        <div>
          <div style="background:#0f766e; color:white; padding:4px; font-weight:bold; font-size:12px; border-radius:4px 4px 0 0;">ตารางที่ 3: insert(3)</div>
          <table style="margin:0; font-size:12px;">
            <tr><th style="width:50px;">Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">- (เว้นว่าง)</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td></td></tr>
          </table>
        </div>
        <div>
          <div style="background:#0f766e; color:white; padding:4px; font-weight:bold; font-size:12px; border-radius:4px 4px 0 0;">ตารางที่ 4: deleteMin() ครั้งที่ 2</div>
          <table style="margin:0; font-size:12px;">
            <tr><th style="width:50px;">Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">- (เว้นว่าง)</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td style="background:#f1f5f9;">-</td></tr>
          </table>
        </div>
      </div>
    </div>

    <!-- SUB-QUESTION 2.2: LECTURE SLIDE TRACE HOLE -->
    <h3 class="question-title past-q">
      <span>2.2 Tracing insert(14) with Variable 'hole' &amp; if-else Condition [โจทย์สไลด์ห้องเรียน 2569 ภาพที่ 7, 8, 9]</span>
      <span class="score-badge past-badge">Score: 4 Marks (4 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given an existing <code>BinaryHeap</code> instance variable named <code>myheap</code> containing 10 elements stored in an array indexed from 1 to 10:</p>
    $$\text{Array: } [-, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32]$$
    <p>Write the statements in the main program to insert the value <code>14</code> into <code>myheap</code>. Then trace the step-by-step execution of the <code>insert()</code> member function. For each iteration, specify:</p>
    <ul>
      <li>The value of the variable <code>hole</code></li>
      <li>The exact comparison performed in the <code>if-else</code> condition</li>
    </ul>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - จากสไลด์ห้องเรียน อ.ประดิษฐ์ ภาพที่ 7, 8, 9):</strong> กำหนดตัวแปรอ็อบเจกต์ BinaryHeap ชื่อ <code>myheap</code> มีข้อมูล 10 ตัวดังรูป ให้เขียนประโยคคำสั่งในฟังก์ชัน main ในการแทรกค่า <code>14</code> เข้าไปใน myheap จากนั้นให้ Trace ขั้นตอนการทำงานของฟังก์ชัน <code>insert()</code> ทีละขั้นตอน โดยในแต่ละรอบระบุค่าของตัวแปร <code>hole</code> และเงื่อนไขการเปรียบเทียบที่เกิดขึ้นจริงในเงื่อนไข <code>if-else</code>
    </div>

    <div class="blank-sheet-box">
      <p style="margin:0 0 8px 0; font-weight:bold;">📝 คำสั่งในฟังก์ชัน main:</p>
      <pre style="margin:0 0 10px 0; background:#f8fafc; color:#0f172a; border:1px solid #cbd5e1;"><code>// เขียนคำสั่งเรียก insert 14 ลงใน myheap:
........................................................................................................................</code></pre>
      <p style="margin:0 0 8px 0; font-weight:bold;">📝 ตารางบันทึกการ Trace ตัวแปร hole และเงื่อนไขเปรียบเทียบ:</p>
      <table style="font-size:12.5px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:100px;">Iteration / รอบ</th>
            <th style="width:140px;">ค่าของตัวแปร hole</th>
            <th>เงื่อนไขการเปรียบเทียบใน if-else</th>
            <th>ผลลัพธ์การทำงานในรอบนั้น</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>รอบที่ 1</td><td></td><td></td><td></td></tr>
          <tr><td>รอบที่ 2</td><td></td><td></td><td></td></tr>
          <tr><td>รอบที่ 3</td><td></td><td></td><td></td></tr>
        </tbody>
      </table>
    </div>

    <!-- QUESTION 2 SOLUTIONS -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 2 (Complete Binary Heap Solutions):</div>
      <p><strong>เฉลย 2.1 ตาราง 4 ชุด:</strong></p>
      <ul>
        <li><strong>ตารางที่ 1 (Insert 12 keys):</strong> <code>[-, 1, 6, 2, 10, 8, 5, 24, 64, 14, 20, 15, 20]</code></li>
        <li><strong>ตารางที่ 2 (deleteMin ครั้งที่ 1):</strong> ลบ 1 นำ 20 ท้ายแถวมา Percolate Down &rarr; <code>[-, 2, 6, 5, 10, 8, 20, 24, 64, 14, 20, 15]</code></li>
        <li><strong>ตารางที่ 3 (insert 3):</strong> เปิดช่อง 12 ใส่ 3 แล้ว Percolate Up &rarr; <code>[-, 2, 6, 3, 10, 8, 5, 24, 64, 14, 20, 15, 20]</code></li>
        <li><strong>ตารางที่ 4 (deleteMin ครั้งที่ 2):</strong> ลบ 2 นำ 20 ท้ายแถวมา Percolate Down &rarr; <code>[-, 3, 6, 5, 10, 8, 20, 24, 64, 14, 20, 15]</code></li>
      </ul>

      <p><strong>เฉลย 2.2 การ Trace insert(14) ด้วยตัวแปร hole (ตามสไลด์ อ.ประดิษฐ์):</strong></p>
      <p><strong>ประโยคคำสั่งใน main:</strong> <code>myheap.insert(14)</code></p>
      <table style="font-size:13px;">
        <tr style="background:#f0fdf4;">
          <th>รอบ (Iteration)</th><th>ค่า hole</th><th>การเปรียบเทียบใน if-else</th><th>การทำงาน</th>
        </tr>
        <tr>
          <td>เริ่มต้น</td><td><code>hole = 11</code></td><td>(เปิดช่องว่างท้ายอาร์เรย์ที่ currentSize + 1)</td><td>เตรียมแทรก $X = 14$</td>
        </tr>
        <tr>
          <td>รอบที่ 1</td><td><code>hole = 11</code></td><td><code>if (14 &lt; array[11 // 2])</code> &rarr; <code>if (14 &lt; array[5])</code> &rarr; <strong><code>14 &lt; 31</code> (True)</strong></td><td>เลื่อนค่า 31 ลงมาที่ช่อง 11: <code>array[11] = 31</code> แล้วเลื่อน <code>hole = 5</code></td>
        </tr>
        <tr>
          <td>รอบที่ 2</td><td><code>hole = 5</code></td><td><code>if (14 &lt; array[5 // 2])</code> &rarr; <code>if (14 &lt; array[2])</code> &rarr; <strong><code>14 &lt; 21</code> (True)</strong></td><td>เลื่อนค่า 21 ลงมาที่ช่อง 5: <code>array[5] = 21</code> แล้วเลื่อน <code>hole = 2</code></td>
        </tr>
        <tr>
          <td>รอบที่ 3</td><td><code>hole = 2</code></td><td><code>if (14 &lt; array[2 // 2])</code> &rarr; <code>if (14 &lt; array[1])</code> &rarr; <strong><code>14 &lt; 13</code> (False)</strong></td><td>เงื่อนไขเป็นเท็จ! สิ้นสุดลูป Percolate Up ใส่ 14 ลงที่ <code>array[2] = 14</code></td>
        </tr>
      </table>
      <p><strong>ผลลัพธ์อาร์เรย์สุดท้าย:</strong> <code>[-, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31]</code></p>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 3: INSERTION SORT (PAST EXAMS 2564 & 2561)                       -->
    <!-- ========================================================================= -->
    <h2 id="past-q3" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 3 (Past Exams): Insertion Sort Worst Case &amp; Modified Program (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 281-285 / ข้อสอบจริงปี 2564 หน้า 9 &amp; ข้อสอบจริงปี 2561 หน้า 8</div>

    <h3 class="question-title past-q">
      <span>3.1 Worst-Case Formula &amp; Position Moves [ข้อสอบจริงปี 2564 หน้า 9 ข้อ 3.1]</span>
      <span class="score-badge past-badge">Score: 4 Marks (4 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given an initial input array of $N = 12$ elements arranged in <strong>Worst-Case</strong> order (strictly reverse/descending order). After <code>insertionSort</code> completes sorting the elements in ascending order, how many total <strong>Position Moves</strong> occurred?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2564 หน้า 9 ข้อ 3.1):</strong> ให้กำหนดข้อมูลเป็น input เริ่มต้นสำหรับการทำ insertionSort จำนวน 12 ตัว โดยเป็นข้อมูลแบบ Worst Case โดยเขียนตัวเลขข้อมูล input เริ่มต้นลงในตาราง เมื่อทำ insertionSort เสร็จสิ้นแล้ว ถามว่า เกิด position move รวมทั้งสิ้นกี่ครั้ง?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14.5px;">ข้อมูล Worst Case 12 ตัว: ........................................................................................ เกิด Position Move รวมทั้งสิ้น ............ ครั้ง</p>
    </div>

    <h3 class="question-title past-q">
      <span>3.2 Tracing Pass p=3 and p=6 [ข้อสอบจริงปี 2564 หน้า 9 ข้อ 3.2]</span>
      <span class="score-badge past-badge">Score: 6 Marks (6 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given the initial input array of $N = 12$ elements: <code>61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2</code>. Write the exact array states after pass $p = 3$ and after pass $p = 6$, specifying the number of position moves and the value of variable $j$ for each pass.</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2564 หน้า 9 ข้อ 3.2):</strong> กำหนดข้อมูล input เริ่มต้นสำหรับการทำ insertionSort 12 ตัว: <strong>61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2</strong> ให้เขียนผลของการทำงานในรอบที่ $p = 3$ และ $p = 6$ พร้อมนับ Position Move ของทั้ง 2 รอบนี้ และระบุค่าของตัวแปร $j$
    </div>
    <div class="blank-sheet-box">
      <table style="font-size:12.5px; text-align:center;">
        <tr style="background:#0f766e; color:white;">
          <th style="width:110px;">รอบ (Pass)</th>
          <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th>
          <th style="width:90px;">Moves</th><th style="width:70px;">ค่า $j$</th>
        </tr>
        <tr><td>เริ่มต้น</td><td>61</td><td>52</td><td>12</td><td>24</td><td>8</td><td>35</td><td>32</td><td>5</td><td>71</td><td>68</td><td>18</td><td>2</td><td>-</td><td>-</td></tr>
        <tr><td>หลัง $p=3$</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>หลัง $p=6$</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>

    <h3 class="question-title past-q">
      <span>3.3 แก้โปรแกรม Insertion Sort ให้นับ Position Moves [ข้อสอบจริงปี 2561 หน้า 8]</span>
      <span class="score-badge past-badge">Score: 4 Marks (4 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Modify the textbook <code>insertionSort</code> function from Chapter 7 to count and output the position moves for each pass and the total position moves.</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2561 หน้า 8 ข้อ 3.3):</strong> จาก insertion sort ในบทที่ 7 ต้องแก้โปรแกรมอย่างไร จึงจะสามารถนับการเลื่อนตำแหน่งของข้อมูลได้ (Position Move ของแต่ละรอบ) ให้เขียน Function Insertion Sort ที่ได้แก้ไขแล้วทั้ง Function
    </div>
    <div class="blank-sheet-box">
      <pre style="margin:0; background:#f8fafc; color:#0f172a; border:1px solid #cbd5e1;"><code>def insertion_sort(a):
    # จงเขียนโค้ดฟังก์ชันภาษา Python ที่แก้ไขเพื่อนับและพิมพ์ Position Moves แต่ละรอบ (p) และยอดรวมทั้งหมด:
    ....................................................................................................
    ....................................................................................................
    ....................................................................................................</code></pre>
    </div>

    <!-- QUESTION 3 SOLUTIONS -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 3 (Insertion Sort Tracing &amp; Code Solutions):</div>
      <p><strong>3.4 สรุปกรณีทั้ง 3 ของ Insertion Sort:</strong></p>
      <ul>
        <li><strong>Best Case:</strong> $O(N)$ เมื่อข้อมูลเรียงจากน้อยไปมากอยู่แล้ว เกิดการเปรียบเทียบ $N-1$ ครั้ง และ Position Move = <strong>0 ครั้ง</strong> (ไม่ต้องเลื่อนสมาชิกตัวอื่นเลย)</li>
        <li><strong>Average Case:</strong> $O(N^2)$ เมื่อข้อมูลเป็น Random Permutation เฉลี่ยแต่ละตัวต้องเลื่อนถอยหลังครึ่งหนึ่ง เกิด Move $\approx \frac{N(N-1)}{4}$ ครั้ง</li>
        <li><strong>Worst Case:</strong> $O(N^2)$ เมื่อข้อมูลเรียงกลับหลังจากมากไปน้อย ทุกตัวต้องเลื่อนถอยหลังจนสุด เกิด Move $= \frac{N(N-1)}{2}$ ครั้ง ($N=12 \implies 66$ ครั้ง)</li>
      </ul>

      <p><strong>3.1 Worst Case:</strong> กำหนดข้อมูลเรียงจากมากไปน้อย เช่น <code>12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1</code><br>
        สูตรคำนวณจำนวนครั้งเลื่อนตำแหน่ง: $\frac{N(N-1)}{2} = \frac{12 \times 11}{2} = \mathbf{66}$ ครั้ง
      </p>
      <p><strong>3.2 ผลการ Tracing:</strong></p>
      <ul>
        <li><strong>หลังรอบ $p=3$ ($X = 24$):</strong> อาร์เรย์กลายเป็น <code>[12, 24, 52, 61, 8, 35, 32, 5, 71, 68, 18, 2]</code> | เลื่อนตำแหน่ง = <strong>2 ครั้ง</strong> | ค่า $j = \mathbf{1}$</li>
        <li><strong>หลังรอบ $p=6$ ($X = 32$):</strong> อาร์เรย์กลายเป็น <code>[8, 12, 24, 32, 35, 52, 61, 5, 71, 68, 18, 2]</code> | เลื่อนตำแหน่ง = <strong>3 ครั้ง</strong> | ค่า $j = \mathbf{3}$</li>
      </ul>
      <p><strong>3.3 ฟังก์ชันที่แก้ไขแล้ว (Python - ตรงตามโค้ดในห้องเรียน Exams/InsertionSort.py):</strong></p>
      <pre><code>def insertion_sort(a):
    total = 0
    print("Original: ", a, "Position Move")
    for p in range(1, len(a)):
        tmp = a[p]
        j = p
        swap = 0
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
            swap += 1
        a[j] = tmp
        total += swap
        print(f"After p = {p}", a, swap)
    print(f"Result : {a}")
    print(f"Total Moves: {total}")

# (หมายเหตุ: ในข้อสอบเก่า C++ ปี 2564 ใช้ template <class Comparable> void insertionSort(vector<Comparable>& a))</code></pre>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 4: QUICKSORT & BUBBLE SORT (PAST 2564 & 2026 CLASSROOM)          -->
    <!-- ========================================================================= -->
        <h3 class="question-title past-q">
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
        Average Case: $O(......)$ สูตรการย้ายตำแหน่ง: $\approx \frac{N(N-1)}{......}$ ครั้ง<br>
        Worst Case: $O(......)$ สูตรการย้ายตำแหน่ง: $\frac{N(N-1)}{......}$ ครั้ง (ข้อมูลเรียงจากมากไปน้อย)
      </p>
    </div>

<h2 id="past-q4" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 4 (Past Exams): Quicksort 17 Keys (Cutoff=3) &amp; Bubble Sort Inversions (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Quicksort), pp. 302-315 / ข้อสอบจริงปี 2564 หน้า 9 &amp; ใบงานห้องเรียน 2569 ภาพที่ 10</div>

    <h3 class="question-title past-q">
      <span>4.1 Quicksort Tracing with 17 Elements &amp; Cutoff = 3 [ข้อสอบจริงปี 2564 หน้า 9 ข้อ 4]</span>
      <span class="score-badge past-badge">Score: 10 Marks (10 คะแนน: 7 + 3)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given an initial input of 17 elements to <code>quicksort</code> using Median-of-Three partitioning and $\text{Cutoff} = 3$:</p>
    $$\mathbf{81, 198, 157, 145, 123, 109, 93, 5, 76, 64, 42, 33, 21, 12, 201, 57, 89}$$
    <ul>
      <li><strong>4.1.1:</strong> What is Pivot #3? Write the entire array of 17 elements after Pivot #3 finishes.</li>
      <li><strong>4.1.2:</strong> While Pivot #1 is active, after the partitioning step finishes but before restoring the pivot, what is the value stored in array slot $a[i]$?</li>
      <li><strong>4.1.3:</strong> How many total times is <code>insertionSort</code> invoked throughout the complete sorting of all 17 elements?</li>
    </ul>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2564 หน้า 9 ข้อ 4):</strong> กำหนดข้อมูลเป็น input ให้กับฟังก์ชัน quicksort จำนวน 17 ตัว: <strong>81, 198, 157, 145, 123, 109, 93, 5, 76, 64, 42, 33, 21, 12, 201, 57, 89</strong> กำหนดตัวเลข Cutoff เท่ากับ 3 เมื่อทำงานฟังก์ชัน quicksort โดยเรียงข้อมูลจากน้อยไปมาก<br>
      4.1 จงเขียนข้อมูลในตัวแปร Object a ทั้ง 17 ตัว หลังจากใช้ pivot ตัวที่ 3 ทำงานเสร็จแล้ว และระบุว่า pivot ตัวที่ 3 คืออะไร?<br>
      4.2 ขณะที่ pivot ตัวที่ 1 ทำงานอยู่ ค่าในอะเรย์ตำแหน่งที่ $i$ ชี้อยู่หลังจากทำ partition เสร็จแล้ว ก่อนจะนำ pivot คืนที่ มีค่าเท่าไร?<br>
      4.3 มีการทำงานฟังก์ชัน insertionsort รวมทั้งสิ้นกี่ครั้ง?
    </div>

    <div class="blank-sheet-box">
      <p style="margin:0 0 6px 0; font-size:14px;"><strong>4.1.1 Pivot ตัวที่ 3 คือ:</strong> .................... สภาพอาร์เรย์ทั้ง 17 ตัวหลังใช้ Pivot ตัวที่ 3 เสร็จ:</p>
      <table style="text-align:center; font-size:11.5px;">
        <tr style="background:#0f766e; color:white;">
          <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th><th>[16]</th>
        </tr>
        <tr>
          <td style="height:28px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
      </table>
      <p style="margin:8px 0 4px 0; font-size:14px;"><strong>4.1.2 ค่าในอะเรย์ตำแหน่งที่ $i$ ชี้อยู่หลัง partition ของ Pivot ตัวที่ 1 คือ:</strong> ....................</p>
      <p style="margin:4px 0 0 0; font-size:14px;"><strong>4.1.3 จำนวนครั้งที่เรียกใช้ฟังก์ชัน insertionsort รวมทั้งสิ้น:</strong> .................... ครั้ง</p>
    </div>

    <h3 class="question-title past-q">
      <span>4.2 Bubble Sort Tracing &amp; Inversions Count [ใบงานห้องเรียน 2569 ภาพที่ 10]</span>
      <span class="score-badge past-badge">Score: 6 Marks (6 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given the array <code>[64, 34, 25, 12, 22, 11, 90]</code>. Trace Bubble Sort execution: How many passes? How many swaps in Pass 1? What is the total number of swaps from start to finish?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ใบงานห้องเรียน 2569 ภาพที่ 10):</strong> กำหนดอาร์เรย์ <code>[64, 34, 25, 12, 22, 11, 90]</code> จง Trace การทำงานของ Bubble Sort:<br>
      - ลูปชั้นนอก (Passes) หมุนกี่รอบ? (ตอบ $7-1 = 6$ รอบ)<br>
      - สภาพอาร์เรย์หลังจบ Pass 1 เป็นอย่างไร? และเกิดการ Swap ใน Pass 1 กี่ครั้ง?<br>
      - เกิดการ Swap รวมทั้งสิ้นกี่ครั้งตลอดการทำงาน? (แสดงการนับ Inversions)
    </div>
    <div class="blank-sheet-box">
      <p style="margin:0; font-size:14.5px; line-height:2;">
        จำนวน Passes = $7 - 1 = $ ............ รอบ | สภาพอาร์เรย์หลัง Pass 1: [ ................................................................ ]<br>
        จำนวน Swap ใน Pass 1 = ............ ครั้ง | จำนวน Swap รวมทั้งสิ้น = ............ ครั้ง (= Inversions)
      </p>
    </div>

    <!-- QUESTION 4 SOLUTIONS -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 4 (Quicksort &amp; Bubble Sort Solutions):</div>
      <p><strong>เฉลย 4.1 Quicksort 17 ตัว (Cutoff = 3):</strong></p>
      <ul>
        <li><strong>Pivot 1:</strong> $\text{Median-3 of } a[0]=81, a[8]=76, a[16]=89 \implies \mathbf{81}$. หลัง Partition หยุดที่ $i=8, j=7$ ค่าใน $a[i]$ ก่อนคืน Pivot คือ <strong>93</strong>! นำ 81 วางลงที่ $a[8]$</li>
        <li><strong>Pivot 2:</strong> ช่วงซ้าย $0..7$ $\implies \text{Median-3 of } 76, 33, 5 \implies \mathbf{33}$. วางที่ $a[3]$</li>
        <li><strong>Pivot 3:</strong> ช่วงย่อย $4..7$ (เพราะช่วง $0..2$ มีขนาด $3 \le \text{cutoff}$ จึงทำ insertion sort) &rarr; $\text{Median-3 of } 42, 64, 76 \implies \mathbf{64}$.</li>
        <li><strong>สภาพอาร์เรย์ทั้ง 17 ตัวหลัง Pivot 3:</strong><br>
          <code>[5, 12, 21, 33, 42, 57, 64, 76, 81, 109, 123, 145, 157, 198, 201, 93, 89]</code>
        </li>
        <li><strong>4.1.2:</strong> ค่าที่ $a[i]$ ก่อนคืน pivot 1 คือ <strong>93</strong></li>
        <li><strong>4.1.3:</strong> จำนวนครั้งที่เรียก <code>insertionSort</code> รวมทั้งสิ้น = <strong>6 ครั้ง</strong></li>
      </ul>
      <p><strong>เฉลย 4.2 Bubble Sort:</strong></p>
      <ul>
        <li>จำนวน Passes = $7 - 1 = \mathbf{6}$ รอบ</li>
        <li>Step 4 เปรียบเทียบ $(64, 22) \implies$ อาร์เรย์คือ <code>[34, 25, 12, 22, 64, 11, 90]</code></li>
        <li>สภาพอาร์เรย์หลังจบ Pass 1: <code>[34, 25, 12, 22, 11, 64, 90]</code> (Swap ไป <strong>5 ครั้ง</strong>)</li>
        <li>จำนวน Swap รวมทั้งสิ้น = จำนวน Inversions = $5 + 4 + 3 + 1 + 1 + 0 = \mathbf{14}$ ครั้ง</li>
      </ul>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 5: TOPOLOGICAL SORT (PAST EXAMS 2564 & 2561)                     -->
    <!-- ========================================================================= -->
    <h2 id="past-q5" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 5 (Past Exams): Topological Sort in DAG (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 355-364 / ข้อสอบจริงปี 2564 หน้า 12 &amp; ข้อสอบจริงปี 2561 หน้า 10</div>

    <p><strong>Question Statement (EN):</strong> Given a Directed Acyclic Graph (DAG) with 7 vertices defined by the following Adjacency List:</p>
    <ul>
      <li>$v_1 \to v_4, v_2, v_3, v_6$</li>
      <li>$v_2 \to v_3, v_4, v_5, v_6$</li>
      <li>$v_3 \to v_4, v_5$</li>
      <li>$v_4 \to v_6, v_5$</li>
      <li>$v_5 \to v_6$</li>
      <li>$v_6 \to \text{(none)}$</li>
      <li>$v_7 \to v_1, v_6$</li>
    </ul>
    <p>Find the Topological Sort using an Indegree table across all rounds and a Circular Queue of size 7 (indices 0..6). Specify the final <code>front</code> and <code>back</code> pointers, and write the final Topological Ordering.</p>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2564 หน้า 12 &amp; ปี 2561 หน้า 10 ข้อ 6):</strong> กำหนดข้อมูลของกราฟ DAG อันหนึ่งเป็น Adjacency List มี 7 Vertex ดังกำหนด จงแสดงวิธีหา Topological Sort เขียนผลลัพธ์ของตาราง Indegree Array ทุกรอบ และเขียนภาพ Queue ขนาด 7 ช่อง ระบุตำแหน่ง front และ back เมื่อเสร็จสิ้น พร้อมเขียน Topological Ordering
    </div>

    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#0f766e; margin-bottom:6px;">📝 ตาราง Indegree Array:</div>
      <table style="text-align:center; font-size:12.5px;">
        <tr style="background:#0f766e; color:white;">
          <th>Vertex</th><th>In-degree เริ่มต้น</th><th>รอบที่ 1</th><th>รอบที่ 2</th><th>รอบที่ 3</th><th>รอบที่ 4</th><th>รอบที่ 5</th><th>รอบที่ 6</th><th>รอบที่ 7</th>
        </tr>
        <tr><td>$v_1$</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_2$</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_3$</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_4$</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_5$</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_6$</td><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_7$</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      </table>
      <p style="margin:8px 0 0 0; font-size:14px;"><strong>ตำแหน่ง Queue:</strong> front อยู่ที่ .......... back อยู่ที่ .......... | <strong>Topological Ordering:</strong> ................................................................</p>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 5 (Topological Sort Solution):</div>
      <ul>
        <li><strong>ลำดับการ Enqueue &amp; Dequeue:</strong>
          <ul>
            <li>รอบที่ 1: $v_7$ (Indegree 0) &rarr; Enqueue $v_7$, Dequeue $v_7$ &rarr; ลด Indegree ของ $v_1$ เหลือ 0</li>
            <li>รอบที่ 2: $v_1$ (Indegree 0) &rarr; Enqueue $v_1$, Dequeue $v_1$ &rarr; ลด Indegree ของ $v_2$ เหลือ 0</li>
            <li>รอบที่ 3: $v_2$ (Indegree 0) &rarr; Enqueue $v_2$, Dequeue $v_2$ &rarr; ลด Indegree ของ $v_3$ เหลือ 0</li>
            <li>รอบที่ 4: $v_3$ (Indegree 0) &rarr; Enqueue $v_3$, Dequeue $v_3$ &rarr; ลด Indegree ของ $v_4$ เหลือ 0</li>
            <li>รอบที่ 5: $v_4$ (Indegree 0) &rarr; Enqueue $v_4$, Dequeue $v_4$ &rarr; ลด Indegree ของ $v_5$ เหลือ 0</li>
            <li>รอบที่ 6: $v_5$ (Indegree 0) &rarr; Enqueue $v_5$, Dequeue $v_5$ &rarr; ลด Indegree ของ $v_6$ เหลือ 0</li>
            <li>รอบที่ 7: $v_6$ (Indegree 0) &rarr; Enqueue $v_6$, Dequeue $v_6$</li>
          </ul>
        </li>
        <li><strong>ตำแหน่ง Queue เมื่อจบการทำงาน:</strong> <code>front = 0</code>, <code>back = 6</code></li>
        <li><strong>Topological Ordering (เขียนคั่นด้วย Comma เท่านั้น ห้ามใส่ลูกศร):</strong> <strong><code>7, 1, 2, 3, 4, 5, 6</code></strong></li>
      </ul>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 6: UNWEIGHTED SHORTEST PATH (PAST EXAMS 2564 & 2561)             -->
    <!-- ========================================================================= -->
    <h2 id="past-q6" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 6 (Past Exams): Unweighted Shortest Path (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 365-375 / ข้อสอบจริงปี 2564 หน้า 10 &amp; ข้อสอบจริงปี 2561 หน้า 10</div>

    <p><strong>Question Statement (EN):</strong> Find the Unweighted Shortest Path starting from <strong>Vertex 1</strong> (or Vertex 4). Fill the BFS table tracking <code>Known</code>, $d_v$, and $p_v$. Write the shortest path strictly separated by commas and state the path length in edges.</p>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2564 หน้า 10 ข้อ 5):</strong> จงหา Shortest Path แบบ Unweighted โดยมี Vertex 1 เป็นจุดเริ่มต้น ให้นักศึกษาเขียนตารางอะเรย์ผลลัพธ์สุดท้ายที่แสดง Known, Dv และ Pv ทำทุก vertex โดย Known เป็น True หรือ 1 ทั้งหมดแล้ว และเขียนภาพของ Queue แสดง front และ back
    </div>

    <div class="blank-sheet-box">
      <table style="text-align:center; font-size:12.5px;">
        <tr style="background:#0f766e; color:white;">
          <th>Vertex $v$</th><th>Known (True / 1)</th><th>Dist $d_v$</th><th>Path $p_v$</th><th>Shortest Path from $v_1$ (คั่นด้วย Comma)</th><th>Length (Edges)</th>
        </tr>
        <tr><td>$v_1$</td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_2$</td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_3$</td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_4$</td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_5$</td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_6$</td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><td>$v_7$</td><td></td><td></td><td></td><td></td><td></td></tr>
      </table>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 6 (Shortest Path Solution):</div>
      <table style="font-size:13px; text-align:center;">
        <tr style="background:#f0fdf4;">
          <th>Vertex $v$</th><th>Known</th><th>$d_v$</th><th>$p_v$</th><th>Shortest Path (Comma เท่านั้น ห้ามใส่ลูกศร)</th><th>Path Length (เส้น)</th>
        </tr>
        <tr><td>$v_1$</td><td>1 (True)</td><td>0</td><td>0</td><td><strong>1</strong></td><td>0 เส้น</td></tr>
        <tr><td>$v_2$</td><td>1 (True)</td><td>1</td><td>1</td><td><strong>1, 2</strong></td><td>1 เส้น</td></tr>
        <tr><td>$v_3$</td><td>1 (True)</td><td>1</td><td>1</td><td><strong>1, 3</strong></td><td>1 เส้น</td></tr>
        <tr><td>$v_4$</td><td>1 (True)</td><td>1</td><td>1</td><td><strong>1, 4</strong></td><td>1 เส้น</td></tr>
        <tr><td>$v_5$</td><td>1 (True)</td><td>2</td><td>4</td><td><strong>1, 4, 5</strong></td><td>2 เส้น</td></tr>
        <tr><td>$v_6$</td><td>1 (True)</td><td>1</td><td>1</td><td><strong>1, 6</strong></td><td>1 เส้น</td></tr>
        <tr><td>$v_7$</td><td>1 (True)</td><td>&infin;</td><td>0</td><td><strong>ไม่มีวิถีเดินถึง (No path)</strong></td><td>&infin;</td></tr>
      </table>
      <p style="margin-top:8px;">⚠️ <strong>จุดตัดคะแนนเป็น 0:</strong> วิถีต้องเขียนคั่นด้วย Comma เช่น <code>1, 4, 5</code> ห้ามเขียน <code>1 -&gt; 4 -&gt; 5</code> เด็ดขาด!</p>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 7: PAST EXAMS WRITTEN THEORY QUESTIONS                           -->
    <!-- ========================================================================= -->
    <h2 id="past-q7" class="part-title" style="color:#0f766e; border-bottom-color:#99f6e4;">
      Question 7 (Past Exams): Theory &amp; Short Answer Questions (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapters 5, 6, 7, 9 / ข้อสอบจริงปี 2564 หน้า 13 &amp; ข้อสอบจริงปี 2561 หน้า 15</div>

    <h3 class="question-title past-q">
      <span>7.1 คุณสมบัติ 3 ประการของ Hash Function ในอุดมคติ [ข้อสอบจริงปี 2564 หน้า 13 ข้อ 7.1]</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> คุณสมบัติของ hash function ตามทฤษฎีในทางอุดมคติ มี 3 ข้อ คืออะไร? ข้อใดเป็นไปไม่ได้ในทางปฏิบัติ ด้วยเหตุผล 2 ประการคืออะไร?
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <ol>
        <li>คำนวณได้ง่ายและรวดเร็ว ($O(1)$) (Simple and fast to compute)</li>
        <li>กระจายคีย์ลงในช่องตารางอย่างสม่ำเสมอทั่วถึง (Equally and uniformly distributed)</li>
        <li>รับประกันว่าข้อมูลที่ต่างกัน ต้องได้ตำแหน่งช่องที่ไม่ซ้ำกันเลย ไม่เกิดการชน (No collisions)</li>
      </ol>
      <p><strong>ข้อที่เป็นไปไม่ได้:</strong> ข้อ 3 (และข้อ 2 ในทางสมบูรณ์แบบ) เนื่องจากเหตุผล 2 ประการ:</p>
      <ul>
        <li><strong>1. กฎรังนกพิราบ (Pigeonhole Principle):</strong> จำนวนคีย์ที่เป็นไปได้ในจักรวาลข้อมูล ($|U|$) มีมากกว่าขนาดตารางแฮช ($M$) อย่างมหาศาล ($|U| \gg M$) เมื่อนกพิราบมีมากกว่ารัง ย่อมต้องมีรังที่นกมากกว่า 1 ตัวอยู่ร่วมกันเสมอ</li>
        <li><strong>2. การเกาะกลุ่มของข้อมูลจริง (Key Clustering):</strong> ข้อมูลจริงในโลกไม่ได้สุ่มมาแบบ Uniform Random แต่มักมีแพทเทิร์นหรือกระจุกตัว</li>
      </ul>
    </div>

    <h3 class="question-title past-q">
      <span>7.2 การกำหนดค่าใน HashTable: Python List vs Struct C++ [ข้อสอบประวัติศาสตร์ปี 2564 หน้า 13 ข้อ 7.2]</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย &amp; บริบทเปรียบเทียบ):</strong> ในข้อสอบปี 2564 (C++) ข้อสอบถามประโยคคำสั่งเพื่อใช้แทนฟังก์ชัน <code>HashEntry(x, ACTIVE)</code> ในคำสั่ง <code>array[currentPos] = HashEntry(x, ACTIVE);</code><br>
      จงอธิบายความแตกต่างระหว่างการเก็บข้อมูลในตารางแฮชภาษา C++ ปี 2564 กับภาษา Python ในหลักสูตรปัจจุบัน 2569 ของ อ.ประดิษฐ์
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดและเปรียบเทียบเชิงสถาปัตยกรรม:</div>
      <p><strong>1. ในภาษา Python (หลักสูตรปัจจุบัน 2569 อ.ประดิษฐ์):</strong></p>
      <ul>
        <li>ตารางแฮชถูกสร้างเป็น 1D List ธรรมดา เช่น <code>self.table = [None] * TableSize</code></li>
        <li>ช่องว่างจะเก็บค่า <code>None</code></li>
        <li>เมื่อทำการแทรกข้อมูล จะบันทึกค่าลงช่องตรงๆ: <code>self.table[currentPos] = x</code> (ไม่มี struct <code>info</code> หรือสถานะ <code>'A'</code> มาเกะกะ)</li>
      </ul>
      <p><strong>2. ในภาษา C++ (ข้อสอบเก่าประวัติศาสตร์ปี 2564):</strong></p>
      <ul>
        <li>ใช้ Struct ซ้อนเรียกว่า <code>HashEntry</code> มี 2 ฟิลด์คือ <code>element</code> และ <code>info</code> (ACTIVE, EMPTY, DELETED)</li>
        <li>คำสั่งที่ใช้แทน Constructor <code>HashEntry(x, ACTIVE)</code> คือ:<br>
          <code>array[ currentPos ].element = x;</code><br>
          <code>array[ currentPos ].info = ACTIVE;</code>
        </li>
      </ul>
    </div>

    <h3 class="question-title past-q">
      <span>7.3 ข้อมูลใน Quicksort ที่ไม่ถูกนำไป Partition [ข้อสอบจริงปี 2564 หน้า 13 ข้อ 7.3]</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> ในการทำ Quick Sort ขั้นตอนการทำ Partitioning แต่ละรอบนั้น พบว่ามีข้อมูลบางตัวที่ไม่ได้นำไปทำ Partition ด้วย ถามว่ามีข้อมูลตัวใดใน array ที่ไม่ได้ถูกทำ Partition เพราะเหตุผลใด?
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <p>ข้อมูลที่ไม่ได้นำไปทำ Partition มี <strong>3 ตัว</strong> ได้แก่:</p>
      <ol>
        <li><strong>ข้อมูลที่ตำแหน่งซ้ายสุด (<code>array[left]</code>):</strong> เพราะจากการทำ Median-of-Three ข้อมูลตัวนี้มีค่าน้อยกว่าหรือเท่ากับ Pivot เรียบร้อยแล้ว จึงทำหน้าที่เป็น <em>Sentinel (ตัวคุมขอบ)</em> ทางซ้ายโดยอัตโนมัติ</li>
        <li><strong>ข้อมูลที่ตำแหน่งขวาสุด (<code>array[right]</code>):</strong> เพราะมีค่ามากกว่าหรือเท่ากับ Pivot เรียบร้อยแล้ว ทำหน้าที่เป็น Sentinel ทางขวา</li>
        <li><strong>ตัว Pivot เอง (ที่ถูกซ่อนไว้ที่ <code>array[right - 1]</code>):</strong> ถูกนำไปพักไว้ชั่วคราว เพื่อไม่ให้ถูกสลับไปมาระหว่างการ Partition และจะนำกลับมาใส่ที่ตำแหน่ง $i$ หลังเสร็จสิ้น</li>
      </ol>
    </div>

    <h3 class="question-title past-q">
      <span>7.4 Complete Binary Tree สูง 10 ชั้น และ 16 ชั้น มีโหนดอย่างน้อยและอย่างมากกี่โหนด [ข้อสอบปี 2564 &amp; 2561]</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> Complete Binary Tree ที่มีความสูง $h=10$ และ $h=16$ จะมีจำนวน node อย่างน้อยที่สุดและอย่างมากที่สุดกี่โหนด? ตอบเป็นตัวเลขจำนวนเต็มเท่านั้น ห้ามติดเลขยกกำลัง
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <p>สูตรความสูง $h$ (นับ Root สูง 0): อย่างน้อย $= 2^h$ โหนด, อย่างมาก $= 2^{h+1} - 1$ โหนด</p>
      <ul>
        <li><strong>ความสูง $h = 10$:</strong>
          <ul>
            <li>อย่างน้อย $= 2^{10} = \mathbf{1,024}$ โหนด</li>
            <li>อย่างมาก $= 2^{11} - 1 = 2048 - 1 = \mathbf{2,047}$ โหนด</li>
          </ul>
        </li>
        <li><strong>ความสูง $h = 16$:</strong>
          <ul>
            <li>อย่างน้อย $= 2^{16} = \mathbf{65,536}$ โหนด</li>
            <li>อย่างมาก $= 2^{17} - 1 = 131072 - 1 = \mathbf{131,071}$ โหนด</li>
          </ul>
        </li>
      </ul>
      <p>⚠️ <em>กับดัก: ตอบติดรูปเลขยกกำลัง เช่น $2^{10}$ ได้ 0 คะแนนทันที ต้องคำนวณเป็นตัวเลขจำนวนเต็ม!</em></p>
    </div>

    <h3 class="question-title past-q">
      <span>7.5 Complete Graph ไม่มีทิศทาง 10 โหนด และ 16 โหนด มีเส้นเชื่อมกี่เส้น [ข้อสอบปี 2564 &amp; 2561]</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> Complete Graph แบบไม่มีทิศทาง (Undirected Complete Graph) ที่มีจำนวนโหนด 10 โหนด และ 16 โหนด จะมีเส้นเชื่อมทั้งหมดกี่เส้น? ตอบเป็นตัวเลขจำนวนเต็มเท่านั้น ห้ามติดสมการ
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <p>สูตรจำนวนเส้นเชื่อม: $\frac{V(V-1)}{2}$ เส้น</p>
      <ul>
        <li>สำหรับ $V = 10$ โหนด: $\frac{10 \times 9}{2} = \mathbf{45}$ เส้น</li>
        <li>สำหรับ $V = 16$ โหนด: $\frac{16 \times 15}{2} = \mathbf{120}$ เส้น</li>
      </ul>
      <p>⚠️ <em>กับดัก: ตอบติดรูปสูตร $10(9)/2$ หรือ $16(15)/2$ ได้ 0 คะแนนทันที ต้องตอบ 45 หรือ 120 เท่านั้น!</em></p>
    </div>

      <h3 class="question-title past-q">
      <span>7.6 การคำนวณร้อยละความสูญเสียในหน่วยความจำของ Adjacency Matrix [สไลด์ Graph อ.ประดิษฐ์]</span>
      <span class="score-badge past-badge">Score: 3 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> กราฟมีทิศทางที่มี 7 โหนด และมีเส้นเชื่อม 12 เส้น หากจัดเก็บด้วย Adjacency Matrix ขนาด $7 \times 7$ จงคำนวณร้อยละของพื้นที่หน่วยความจำที่ถูกใช้งานจริง (Used %) และร้อยละที่สูญเปล่า (Wasted %)
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <p>พื้นที่ทั้งหมดใน Matrix: $7 \times 7 = \mathbf{49}$ ช่อง</p>
      <ul>
        <li><strong>พื้นที่ใช้งานจริง (มีเส้นเชื่อม Edge = 1):</strong> $\frac{12}{49} \times 100\% = \mathbf{24.49\%}$</li>
        <li><strong>พื้นที่สูญเปล่า (เป็น 0 ไม่มีเส้นเชื่อม):</strong> $\frac{49 - 12}{49} \times 100\% = \frac{37}{49} \times 100\% = \mathbf{75.51\%}$</li>
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
            <li><strong>AVL Tree:</strong> (1) Binary Search Tree Property, (2) Balance Property ($|h_L - h_R| \le 1$)</li>
          </ul>
        </li>
        <li><strong>มี 3 คุณสมบัติ (Three Properties):</strong>
          <ul>
            <li><strong>Ideal Hash Function:</strong> (1) Simple and fast to compute ($O(1)$), (2) Uniformly distributed (กระจายสม่ำเสมอทั่วตาราง), (3) No collisions (One-to-One mapping - ซึ่งเป็นไปไม่ได้จริงเพราะ Pigeonhole Principle)</li>
          </ul>
        </li>
      </ul>
    </div>
  </div> <!-- END TAB 2 -->
"""

if __name__ == "__main__":
    print("generate_tab2.py compiled successfully!")
