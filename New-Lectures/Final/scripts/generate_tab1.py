# -*- coding: utf-8 -*-
"""
Module to generate HTML for Tab 1: Official Final Exam 2026 Suite
"""

def get_tab1_html():
    return r"""  <!-- ========================================================================= -->
  <!-- TAB 1: OFFICIAL FINAL EXAM 2026 SUITE (SET A)                           -->
  <!-- ========================================================================= -->
  <div id="tab-2026" class="tab-content active">
<h1 class="section-heading">🌟 ตอนที่ 1: ชุดข้อสอบปลายภาคฉบับจริงปี 2569 (Official Final Exam - 7 ข้อใหญ่ 70 คะแนน)</h1>

  <!-- QUICK NAV FOR TAB 1 -->
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


  <!-- QUESTION 1 -->
  <h2 id="q1" class="part-title">Question 1: Hashing &amp; Open Addressing (Double Hashing) (18 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (Hashing), pp. 195-212 / สไลด์ Hashing อ.ประดิษฐ์</div>

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (จุดระวังการนับชน &amp; ค่า R):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>การนับการชน:</strong> ให้นับเฉพาะจำนวนครั้งที่ตัวมันเองเกิดการชนจริง (เช่น ชน 1, 3, 3 ครั้ง) <em>ห้ามนำยอดรวมสะสมมาตอบผิด</em> และการชนรวมของตารางคือ 7 ครั้ง ไม่ใช่เอา ชน + แก้ = 14<br>
      • <strong>ค่าคงที่ R ใน Double Hashing:</strong> ต้องเลือกจำนวนเฉพาะที่มากที่สุดที่น้อยกว่าขนาดตาราง ($R < \text{TableSize}$) อย่างเคร่งครัด หากขนาดตารางเป็น 11 ต้องเลือก $R = 7$ (ห้ามเลือก 11 เด็ดขาด เพราะจะเกิด Infinite Loop)<br>
      • <strong>การ Rehash:</strong> ขนาดตารางใหม่ต้องเป็นจำนวนเฉพาะที่ $\ge 2 \times \text{TableSize}$ (ดูตารางเทียบด่วนใน Tab 4 หัวข้อ 13) และต้องกวาดอ่านข้อมูลจากช่อง 0 ลงไปช่องล่างสุด ห้ามอ่านตามลำดับโจทย์เดิม!
    </p>
  </div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำสั่งและข้อกำหนดจากกระดาษข้อสอบจริงของ อ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล:</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      1. ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Hash Table กำหนด <strong>TableSize ให้เป็น 19</strong> คิดเปอร์เซ็นต์ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่ <strong>80%</strong><br>
      2. <strong>การนับการชน:</strong> <em>"การชนกันและแก้การชนกันในแต่ละครั้ง นับเป็น 1 ไม่ได้นับเป็น 2 ได้อธิบายไว้ในห้องเรียนแล้ว"</em> (ห้ามนำจำนวนก้าว + การชนมารวมกันเป็น 2 เด็ดขาด)<br>
      3. <strong>วิธีการคำนวณ:</strong> <em>"ไม่จำเป็นต้องไล่โปรแกรมเสมอไป นักศึกษาสามารถคำนวณตามสูตรก็ได้"</em>
    </p>
  </div>

  <h3 class="question-title">
    <span>1.1 Double Hashing Table &amp; Probe Calculations</span>
    <span class="score-badge">Score: 8 Marks (8 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Hash Table of size $\text{TableSize} = 19$ (indexed $0$ to $18$) in Python. Rehashing is triggered when the table load reaches <strong>80%</strong>.</p>
  <p>Insert the sequence of 8 keys: $\mathbf{26, 45, 70, 85, 102, 123, 143, 155}$ into the Hash Table using Open Addressing with <strong>Double Hashing</strong> defined by:</p>
  $$\text{Probe Formula: } h_i(X) = (h_0(X) + f(i)) \bmod 19 \quad \text{where } f(i) = i \times (R - (X \bmod R)) \quad \text{for } i = 0, 1, 2, \dots$$
  <p>Fill the resulting Hash Table array and answer all sub-questions.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง):</strong><br>
    ให้นักศึกษาทำการ insert ข้อมูลจำนวน 8 ตัวต่อไปนี้ เข้าไปใน Hash Table ดังกล่าว ชนิด Open Addressing โดยใช้วิธีการแก้การชนกันแบบ Double Hashing กำหนด $f(i) = i \times (R - (x \bmod R))$<br>
    $$\mathbf{26 , 45 , 70 , 85 , 102 , 123 , 143 , 155} \quad \text{[รวม insert ทุกตัวเสร็จสิ้น 8 คะแนน]}$$
    โดยที่: 1) ไม่จำเป็นต้องไล่โปรแกรมเสมอไป นักศึกษาสามารถคำนวณตามสูตรก็ได้<br>
    2) การชนกันและแก้การชนกันในแต่ละครั้ง นับเป็น 1 ไม่ได้นับเป็น 2 ได้อธิบายไว้ในห้องเรียนแล้ว
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
      📝 ตารางจำลองกระดาษคำตอบข้อ 1.1: โครงสร้าง Hash Table ขนาด 19 ช่อง (Hash Table Array ในภาษา Python)
    </div>
    <div style="overflow-x:auto; margin:10px 0;">
      <table style="width:100%; border-collapse:collapse; text-align:center; font-family:'Segoe UI', Tahoma, sans-serif; font-size:12px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:5px; border:1px solid #475569; width:85px;">Slot / Index</th>
            <th style="padding:5px; border:1px solid #475569;">[0]</th>
            <th style="padding:5px; border:1px solid #475569;">[1]</th>
            <th style="padding:5px; border:1px solid #475569;">[2]</th>
            <th style="padding:5px; border:1px solid #475569;">[3]</th>
            <th style="padding:5px; border:1px solid #475569;">[4]</th>
            <th style="padding:5px; border:1px solid #475569;">[5]</th>
            <th style="padding:5px; border:1px solid #475569;">[6]</th>
            <th style="padding:5px; border:1px solid #475569;">[7]</th>
            <th style="padding:5px; border:1px solid #475569;">[8]</th>
            <th style="padding:5px; border:1px solid #475569;">[9]</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Value (Key)</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
          </tr>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:5px; border:1px solid #475569;">Slot / Index</th>
            <th style="padding:5px; border:1px solid #475569;">[10]</th>
            <th style="padding:5px; border:1px solid #475569;">[11]</th>
            <th style="padding:5px; border:1px solid #475569;">[12]</th>
            <th style="padding:5px; border:1px solid #475569;">[13]</th>
            <th style="padding:5px; border:1px solid #475569;">[14]</th>
            <th style="padding:5px; border:1px solid #475569;">[15]</th>
            <th style="padding:5px; border:1px solid #475569;">[16]</th>
            <th style="padding:5px; border:1px solid #475569;">[17]</th>
            <th style="padding:5px; border:1px solid #475569;">[18]</th>
            <th style="padding:5px; border:1px solid #475569; background:#475569;">-</th>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Value</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:30px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; background:#f1f5f9;">-</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- SUB-QUESTION 1.2 -->
  <h3 class="question-title">
    <span>1.2 ข้อมูลตัวใดชนมากที่สุด ชนกี่ครั้ง และที่ตำแหน่งใด / Key with Maximum Collisions</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน: 1 + 1 + 1)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Which key(s) experienced the maximum number of collisions during insertion? How many collisions did they experience, and at which cell locations?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง 2564 หน้า 1):</strong><br>
    ข้อมูลตัวใด ขณะใส่เข้าไปใน Hash Table แล้ว มีการชนกันและแก้การชนกันมากที่สุด (มีมากกว่า 1 ตัวก็ได้) และ ขณะใส่ข้อมูลตัวนั้น เกิดการชนกันกี่ครั้ง ที่ตำแหน่งใด
  </div>
  <div class="blank-sheet-box">
    <p style="margin:0; font-size:15px; line-height:2.2;">
      ข้อมูลตัวที่มีการชนกันและแก้การชนกันมากที่สุด คือ .................................................................... เกิดการชนกัน ............ ครั้ง ที่ตำแหน่ง ....................................................................
    </p>
  </div>

  <!-- SUB-QUESTION 1.3 -->
  <h3 class="question-title">
    <span>1.3 จำนวนการชนและแก้การชนรวมทั้งสิ้น / Total Cumulative Collisions</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> What is the total cumulative number of collisions and resolution steps that occurred during the insertion of all 8 keys?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง 2564 หน้า 1):</strong><br>
    หลังจากใส่ข้อมูลลงใน Hash Table ดังกล่าวครบทุกตัว ถามว่า มีการชนกันและแก้การชนกันรวมทั้งสิ้นกี่ครั้ง (การชนกันและแก้การชนกัน นับเป็น 1 ไม่ได้นับเป็น 2 ได้อธิบายไว้ในห้องเรียนแล้ว)
  </div>
  <div class="blank-sheet-box">
    <p style="margin:0; font-size:15px; line-height:2.2;">
      มีการชนกันและแก้การชนกันรวมทั้งสิ้น ............ ครั้ง
    </p>
  </div>

  <!-- SUB-QUESTION 1.4 -->
  <h3 class="question-title">
    <span>1.4 จำนวนข้อมูลที่ต้องใส่เพิ่มอีกกี่ตัว จึงจะเกิดการ Rehash / Threshold for Rehashing</span>
    <span class="score-badge">Score: 4 Marks (4 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> If the rehashing threshold is set at <strong>80%</strong> of $\text{TableSize} = 19$, how many additional keys must be inserted before rehashing occurs?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง 2564 หน้า 1):</strong><br>
    หลังจากใส่ข้อมูลลงใน Hash Table ดังกล่าวครบทุกตัว ถามว่า จะต้องใส่ข้อมูลเพิ่มอีกกี่ตัว จึงจะเกิดการ Rehash
  </div>
  <div class="blank-sheet-box">
    <p style="margin:0; font-size:15px; line-height:2.2;">
      จะต้องใส่ข้อมูลเพิ่มอีก ............ ตัว จึงจะเกิดการ Rehash
    </p>
  </div>

  <!-- SUB-QUESTION 1.5: WRAP AROUND -->
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
      ขนาดตารางเดิม = 19 &rarr; $2 \times 19 = 38$ &rarr; ขนาดตารางใหม่คือ <strong>............</strong> (ต้องเป็นจำนวนเฉพาะที่ &ge; 38)
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
      ร้อยละขณะมี 8 คีย์: $\lambda = \frac{8}{19} \times 100\% = $ ............ %<br>
      ร้อยละขณะมี 16 คีย์: $\lambda = \frac{16}{19} \times 100\% = $ ............ % (&gt; 80% เกิด Rehash)
    </p>
  </div>

  <!-- QUESTION 1 SOLUTIONS -->
  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. การคำนวณการชนและการแทรกทีละคีย์ (เทียบกับเฉลยลายมือรุ่นพี่หน้า 7–8 ใน PDF จริงเป๊ะๆ):</strong></p>
    <ul>
      <li><strong>Key 26:</strong> $h_0(26) = 26 \bmod 19 = \mathbf{7}$ &rarr; ช่อง 7 ว่าง &rarr; บรรจุลง <strong>ช่อง 7</strong> (Info: <code>A</code>, ชน 0 ครั้ง)</li>
      <li><strong>Key 45:</strong> $h_0(45) = 45 \bmod 19 = \mathbf{7}$ &rarr; <em>ชนกับ 26 ที่ช่อง 7!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $F_1 = 1 \times (17 - (45 \bmod 17)) = 1 \times (17 - 11) = 6$<br>
        $i=1: h_1(45) = (7 + 6) \bmod 19 = \mathbf{13}$ &rarr; ช่อง 13 ว่าง &rarr; บรรจุลง <strong>ช่อง 13</strong> (Info: <code>A</code>, ชน 1 ครั้ง)
      </li>
      <li><strong>Key 70:</strong> $h_0(70) = 70 \bmod 19 = \mathbf{13}$ &rarr; <em>ชนกับ 45 ที่ช่อง 13!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $F_1 = 1 \times (17 - (70 \bmod 17)) = 1 \times (17 - 2) = 15$<br>
        $i=1: h_1(70) = (13 + 15) \bmod 19 = 28 \bmod 19 = \mathbf{9}$ &rarr; ช่อง 9 ว่าง &rarr; บรรจุลง <strong>ช่อง 9</strong> (Info: <code>A</code>, ชน 1 ครั้ง)
      </li>
      <li><strong>Key 85:</strong> $h_0(85) = 85 \bmod 19 = \mathbf{9}$ &rarr; <em>ชนกับ 70 ที่ช่อง 9!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $F_1 = 1 \times (17 - (85 \bmod 17)) = 1 \times (17 - 0) = 17$<br>
        $i=1: h_1(85) = (9 + 17) \bmod 19 = 26 \bmod 19 = \mathbf{7}$ &rarr; <em>ชนกับ 26 ที่ช่อง 7!</em> (ชนครั้งที่ 2)<br>
        $F_2 = 2 \times (17 - (85 \bmod 17)) = 2 \times 17 = 34$<br>
        $i=2: h_2(85) = (9 + 34) \bmod 19 = 43 \bmod 19 = \mathbf{5}$ &rarr; ช่อง 5 ว่าง &rarr; บรรจุลง <strong>ช่อง 5</strong> (Info: <code>A</code>, ชน 2 ครั้ง)
      </li>
      <li><strong>Key 102:</strong> $h_0(102) = 102 \bmod 19 = \mathbf{7}$ &rarr; <em>ชนกับ 26 ที่ช่อง 7!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $F_1 = 1 \times (17 - (102 \bmod 17)) = 1 \times (17 - 0) = 17$<br>
        $i=1: h_1(102) = (7 + 17) \bmod 19 = 24 \bmod 19 = \mathbf{5}$ &rarr; <em>ชนกับ 85 ที่ช่อง 5!</em> (ชนครั้งที่ 2)<br>
        $F_2 = 2 \times (17 - (102 \bmod 17)) = 2 \times 17 = 34$<br>
        $i=2: h_2(102) = (7 + 34) \bmod 19 = 41 \bmod 19 = \mathbf{3}$ &rarr; ช่อง 3 ว่าง &rarr; บรรจุลง <strong>ช่อง 3</strong> (Info: <code>A</code>, ชน 2 ครั้ง)
      </li>
      <li><strong>Key 123:</strong> $h_0(123) = 123 \bmod 19 = \mathbf{9}$ &rarr; <em>ชนกับ 70 ที่ช่อง 9!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $F_1 = 1 \times (17 - (123 \bmod 17)) = 1 \times (17 - 4) = 13$<br>
        $i=1: h_1(123) = (9 + 13) \bmod 19 = 22 \bmod 19 = \mathbf{3}$ &rarr; <em>ชนกับ 102 ที่ช่อง 3!</em> (ชนครั้งที่ 2)<br>
        $F_2 = 2 \times (17 - (123 \bmod 17)) = 2 \times 13 = 26$<br>
        $i=2: h_2(123) = (9 + 26) \bmod 19 = 35 \bmod 19 = \mathbf{16}$ &rarr; ช่อง 16 ว่าง &rarr; บรรจุลง <strong>ช่อง 16</strong> (Info: <code>A</code>, ชน 2 ครั้ง)
      </li>
      <li><strong>Key 143:</strong> $h_0(143) = 143 \bmod 19 = \mathbf{10}$ &rarr; ช่อง 10 ว่าง &rarr; บรรจุลง <strong>ช่อง 10</strong> (Info: <code>A</code>, ชน 0 ครั้ง)</li>
      <li><strong>Key 155:</strong> $h_0(155) = 155 \bmod 19 = \mathbf{3}$ &rarr; <em>ชนกับ 102 ที่ช่อง 3!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $F_1 = 1 \times (17 - (155 \bmod 17)) = 1 \times (17 - 2) = 15$<br>
        $i=1: h_1(155) = (3 + 15) \bmod 19 = 18 \bmod 19 = \mathbf{18}$ &rarr; ช่อง 18 ว่าง &rarr; บรรจุลง <strong>ช่อง 18</strong> (Info: <code>A</code>, ชน 1 ครั้ง)
      </li>
    </ul>

    <div style="overflow-x:auto; margin:15px 0;">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
        📝 เฉลยตารางแฮชสมบูรณ์: แสดง Element, Info ('A') และประวัติการชน (Collisions) ตามแบบข้อสอบจริง
      </div>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-family:'Segoe UI', Tahoma, sans-serif; font-size:12.5px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:6px; border:1px solid #475569; width:95px;">Slot / Index</th>
            <th style="padding:6px; border:1px solid #475569;">[0]</th>
            <th style="padding:6px; border:1px solid #475569;">[1]</th>
            <th style="padding:6px; border:1px solid #475569;">[2]</th>
            <th style="padding:6px; border:1px solid #475569;">[3]</th>
            <th style="padding:6px; border:1px solid #475569;">[4]</th>
            <th style="padding:6px; border:1px solid #475569;">[5]</th>
            <th style="padding:6px; border:1px solid #475569;">[6]</th>
            <th style="padding:6px; border:1px solid #475569;">[7]</th>
            <th style="padding:6px; border:1px solid #475569;">[8]</th>
            <th style="padding:6px; border:1px solid #475569;">[9]</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:7px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Value (Key)</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">102</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">85</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">26</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">70</td>
          </tr>
          <tr style="background:#fff7ed;">
            <td style="padding:5px 4px; font-weight:bold; background:#ffedd5; border:1px solid #fed7aa; color:#9a3412; font-size:11px;">การชน (ชน N)</td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน 2 ครั้ง</span><br/><span style="font-size:9.5px; color:#64748b;">(ช่อง 7, 5)</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน 2 ครั้ง</span><br/><span style="font-size:9.5px; color:#64748b;">(ช่อง 9, 7)</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#15803d; font-size:11px;">ชน 0</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน 1 ครั้ง</span><br/><span style="font-size:9.5px; color:#64748b;">(ช่อง 13)</span></td>
          </tr>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:6px; border:1px solid #475569;">Slot / Index</th>
            <th style="padding:6px; border:1px solid #475569;">[10]</th>
            <th style="padding:6px; border:1px solid #475569;">[11]</th>
            <th style="padding:6px; border:1px solid #475569;">[12]</th>
            <th style="padding:6px; border:1px solid #475569;">[13]</th>
            <th style="padding:6px; border:1px solid #475569;">[14]</th>
            <th style="padding:6px; border:1px solid #475569;">[15]</th>
            <th style="padding:6px; border:1px solid #475569;">[16]</th>
            <th style="padding:6px; border:1px solid #475569;">[17]</th>
            <th style="padding:6px; border:1px solid #475569;">[18]</th>
            <th style="padding:6px; border:1px solid #475569; background:#475569;">-</th>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Value (Key)</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">143</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">45</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">123</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#1e40af; font-size:13.5px;">155</td>
            <td style="padding:7px 4px; border:1px solid #cbd5e1; background:#f1f5f9;">-</td>
          </tr>
          <tr style="background:#fff7ed;">
            <td style="padding:5px 4px; font-weight:bold; background:#ffedd5; border:1px solid #fed7aa; color:#9a3412; font-size:11px;">การชน (ชน N)</td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#15803d; font-size:11px;">ชน 0</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน 1 ครั้ง</span><br/><span style="font-size:9.5px; color:#64748b;">(ช่อง 7)</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน 2 ครั้ง</span><br/><span style="font-size:9.5px; color:#64748b;">(ช่อง 9, 3)</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="color:#cbd5e1;">-</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa;"><span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน 1 ครั้ง</span><br/><span style="font-size:9.5px; color:#64748b;">(ช่อง 3)</span></td>
            <td style="padding:5px 4px; border:1px solid #fed7aa; background:#f1f5f9;">-</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p><strong>สรุปคำตอบข้อ 1.2 - 1.4 ตรงตามเฉลยกระดาษข้อสอบจริง 2564:</strong></p>
    <ul>
      <li><strong>ข้อ 1.2 ข้อมูลตัวใดชนมากที่สุด ชนกี่ครั้ง และที่ตำแหน่งใด [3 คะแนน 1+1+1]:</strong><br>
        • ข้อมูลตัวที่มีการชนและแก้การชนมากที่สุด คือ <strong>85, 102, 123</strong> (มี 3 ตัว ตอบตัวใดตัวหนึ่งหรือทั้ง 3 ตัวก็ได้)<br>
        • เกิดการชนกันตัวละ <strong>2 ครั้ง</strong><br>
        • ที่ตำแหน่ง: <strong>85 ชนที่ช่อง 9 และ ช่อง 7</strong> | <strong>102 ชนที่ช่อง 7 และ ช่อง 5</strong> | <strong>123 ชนที่ช่อง 9 และ ช่อง 3</strong>
      </li>
      <li><strong>ข้อ 1.3 จำนวนการชนและแก้การชนรวมทั้งสิ้น [3 คะแนน]:</strong><br>
        คำนวณจากการชนของแต่ละคีย์: $0 (26) + 1 (45) + 1 (70) + 2 (85) + 2 (102) + 2 (123) + 0 (143) + 1 (155) = \mathbf{9 \text{ ครั้ง}}$<br>
        <em>(หมายเหตุ: กฎข้อสอบ อ.ประดิษฐ์ "การชนกันและแก้การชนกันในแต่ละครั้ง นับเป็น 1 ไม่ได้นับเป็น 2")</em>
      </li>
      <li><strong>ข้อ 1.4 จะต้องใส่ข้อมูลเพิ่มอีกกี่ตัว จึงจะเกิดการ Rehash [4 คะแนน]:</strong><br>
        เกณฑ์ Rehashing เมื่อตารางใกล้เต็มที่ <strong>80%</strong> ของ TableSize 19:<br>
        • <strong>วิธีคิดที่ 1 (ตามลายมือรุ่นพี่หน้า 8 ใน PDF จริงที่เขียนว่า $\frac{80 \times 19}{100} = 15.2 \implies \text{ตอบ 15}$):</strong><br>
          ตารางจะเริ่มเกิดการ Rehash เมื่อมีข้อมูลครบ <strong>15 ตัว</strong><br>
          ปัจจุบันใส่ไปแล้ว 8 ตัว &rarr; ดังนั้นจะต้องใส่ข้อมูลเพิ่มอีก $15 - 8 = \mathbf{7 \text{ ตัว}}$<br>
        • <strong>วิธีคิดที่ 2 (ตามเกณฑ์เชิงโปรแกรมแบบปัดขึ้น strictly &gt; 80%):</strong><br>
          $\frac{15}{19} = 78.95\% \le 80\%$ (ยังไม่ถึงเกณฑ์) &rarr; ข้อมูลตัวที่ทำให้เกิน 80% คือตัวที่ 16 ($\frac{16}{19} = 84.21\% &gt; 80\%$)<br>
          ดังนั้นจะต้องใส่ข้อมูลเพิ่มอีก $16 - 8 = \mathbf{8 \text{ ตัว}}$<br>
        <span style="color:#b45309; font-weight:bold;">💡 คำแนะนำในห้องสอบ: ให้เขียนกำกับว่า "หากคิด 80% ของ 19 คือ 15.2 ตัว: ต้องใส่อีก 7 ตัว (ถึง 15 ตัว) หรือหากคิดแบบปัดขึ้นเกิน 80% ต้องใส่อีก 8 ตัว (ถึง 16 ตัว)" จะได้คะแนนเต็มแน่นอน</span>
      </li>
      <li><strong>ข้อ 1.5 นิยาม Wrap Around:</strong> <em>"When the key was mapped to the last index of hash table, it go back to the first index of hash table by mod tablesize one more time."</em><br>
        (ภาษาไทย: เมื่อคีย์ถูกแม็ปไปถึงตำแหน่งท้ายของ hash table แล้ว ให้วนกลับมาตำแหน่งที่ 0 ใหม่ โดยการ mod tablesize อีกรอบหนึ่ง)</li>
      <li><strong>ข้อ 1.6 การเลือก New TableSize:</strong> <em>"Choose the smallest prime number but greater than or equal to double of the TableSize of the old Hash Table."</em><br>
        (เลือกจำนวนเฉพาะที่น้อยที่สุดแต่มากกว่าหรือเท่ากับ 2 เท่าของตารางเดิม &rarr; $2 \times 19 = 38$ &rarr; จำนวนเฉพาะถัดไปคือ <strong>41</strong>)</li>
      <li><strong>ข้อ 1.7 การเลือกค่า R:</strong> $R$ ต้องเป็นจำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize อย่างเคร่งครัด ($R &lt; \text{TableSize}$)<br>
        สำหรับ TableSize = 19 เลือก $R = 17$ | สำหรับ TableSize = 11 ต้องเลือก <strong>$R = 7$</strong> (ห้ามเลือก 11 เพราะจะทำให้ mod 11 ได้ 0 ซึ่งก้าวเดิน $hash_2 = 0$)</li>
      <li><strong>ข้อ 1.8 การคำนวณร้อยละ:</strong><br>
        • ปัจจุบัน 8 คีย์: $\lambda = \frac{8}{19} \times 100\% = \mathbf{42.11\%}$<br>
        • เมื่อเกิด Rehash (16 คีย์): $\lambda = \frac{16}{19} \times 100\% = \mathbf{84.21\%}$ (&gt; 80%)</li>
    </ul>
  </div>
  <!-- QUESTION 2 -->
  <h2 id="q2" class="part-title">Question 2: Priority Queue (Binary Min-Heap) (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 6 (Priority Queues), pp. 243-260 / สไลด์ Priority Queues อ.ประดิษฐ์ / ต้นฉบับข้อสอบจริงปี 2564 หน้า 1 (ข้อ 2.1–2.4)</div>

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำสั่งและข้อกำหนดจากกระดาษข้อสอบจริงของ อ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล:</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>โครงสร้างตาราง:</strong> <em>"ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Binary Heap เป็นแนวตั้ง 4 ตาราง เพื่อรองรับข้อมูลตาม 2.1"</em><br>
      • <strong>หัวตาราง:</strong> <em>"เขียนหัวตารางด้วย ว่า 2.1, 2.2 deleteMin, 2.3 Insert, 2.4 deleteMin"</em><br>
      • <strong>การตรวจยึดโปรแกรม:</strong> <em>"การดำเนินการนั้น ขอให้ใช้โปรแกรมตามที่เรียน เพราะหากใส่ตามความรู้สึกแล้ว อาจจะได้ผลลัพธ์ผิดพลาดได้ การตรวจยึดผลลัพธ์จากการทำงานของโปรแกรมเป็นหลัก"</em><br>
      • <strong>Index 0 Sentinel:</strong> อาร์เรย์ของ Heap เริ่มต้นที่ Index 1 เสมอ ช่อง 0 ห้ามใช้ใส่ <code>None</code> หรือ <code>unused</code>
    </p>
  </div>

  <h3 class="question-title">
    <span>2. Binary Min-Heap: Properties, 4-Stage Array Operations &amp; Tree Visualizations</span>
    <span class="score-badge">Score: 10 Marks (2 + 2 + 2 + 2 + 2 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Binary Min-Heap implemented as a 1-based array in Python (where index 0 is unused / <code>None</code>). You are given the sequence of 12 keys:</p>
  $$\mathbf{64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20}$$
  <p><strong>Sub-questions according to the official examination standards:</strong></p>
  <ol>
    <li><strong>2.1 Fundamental Properties:</strong> State the two fundamental properties (Structure Property &amp; Heap-Order Property) that govern a Binary Min-Heap [2 คะแนน]</li>
    <li><strong>2.2 Sequential Insertions:</strong> Insert all 12 keys into the Binary Heap. Write the resulting array into vertical table 1 [2 คะแนน]</li>
    <li><strong>2.3 First deleteMin:</strong> Perform <code>deleteMin()</code> 1 time and write the resulting array into vertical table 2 [2 คะแนน]</li>
    <li><strong>2.4 Key Insertion:</strong> Insert key <code>3</code> into the heap and write the resulting array into vertical table 3 [2 คะแนน]</li>
    <li><strong>2.5 Second deleteMin:</strong> Perform <code>deleteMin()</code> one more time and write the final resulting array into vertical table 4 [2 คะแนน]</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริงปี 2564 หน้า 1 เป๊ะๆ):</strong><br>
    2. ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Binary Heap เป็นแนวตั้ง 4 ตาราง เพื่อรองรับข้อมูลตาม 2.1<br>
    2.1. จงใส่ข้อมูลตัวเลขต่อไปนี้ <strong>64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20</strong> เข้าไปในตารางอะเรย์ดังกล่าว โดยให้เขียนเฉพาะผลลัพธ์สุดท้ายที่ Insert ข้อมูลเสร็จแล้วเท่านั้น ในตารางแรก [1 คะแนน]<br>
    2.2. ให้ทำการ deleteMin 1 ครั้ง แล้วเขียนผลลัพธ์ลงในตารางอะเรย์ ที่ 2 [2 คะแนน]<br>
    2.3. หลังจากนั้นให้ทำการ insert ข้อมูลตัวเลข 3 เข้าไปใน เขียนผลในตารางอะเรย์ ที่ 3 [2 คะแนน]<br>
    2.4. หลังจากนั้น ให้ทำการ deleteMin อีกครั้ง แล้วเขียนผลลัพธ์ลงในตารางอะเรย์ ที่ 4 [3 คะแนน]<br>
    <em>เขียนหัวตารางด้วย ว่า 2.1 &nbsp; 2.2 deleteMin &nbsp; 2.3 Insert &nbsp; 2.4 deleteMin</em>
  </div>

  <!-- BLANK VERTICAL TABLES SIMULATION -->
  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">
      📝 ช่องจำลองกระดาษคำตอบข้อ 2: ตารางอะเรย์แนวตั้ง 4 ตาราง (ตามข้อสอบจริง อ.ประดิษฐ์)
    </div>
    <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin:10px 0;">
      <!-- Table 1 -->
      <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
        <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.1</div>
        <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
          <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th style="padding:3px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:3px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[0]</td><td style="padding:3px; border:1px solid #e2e8f0; color:#94a3b8; font-style:italic;">unused</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[1]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[2]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[3]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[4]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[5]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[6]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[7]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[8]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[9]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[10]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[11]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[12]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
        </table>
      </div>
      <!-- Table 2 -->
      <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
        <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.2 deleteMin</div>
        <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
          <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th style="padding:3px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:3px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[0]</td><td style="padding:3px; border:1px solid #e2e8f0; color:#94a3b8; font-style:italic;">unused</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[1]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[2]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[3]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[4]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[5]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[6]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[7]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[8]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[9]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[10]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[11]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[12]</td><td style="padding:3px; border:1px solid #e2e8f0; color:#cbd5e1;">-</td></tr>
        </table>
      </div>
      <!-- Table 3 -->
      <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
        <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.3 Insert</div>
        <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
          <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th style="padding:3px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:3px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[0]</td><td style="padding:3px; border:1px solid #e2e8f0; color:#94a3b8; font-style:italic;">unused</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[1]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[2]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[3]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[4]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[5]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[6]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[7]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[8]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[9]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[10]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[11]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[12]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
        </table>
      </div>
      <!-- Table 4 -->
      <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
        <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.4 deleteMin</div>
        <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
          <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th style="padding:3px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:3px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[0]</td><td style="padding:3px; border:1px solid #e2e8f0; color:#94a3b8; font-style:italic;">unused</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[1]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[2]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[3]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[4]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[5]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[6]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[7]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[8]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[9]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[10]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[11]</td><td style="padding:3px; border:1px solid #e2e8f0;">&nbsp;</td></tr>
          <tr><td style="padding:3px; border:1px solid #e2e8f0; font-family:Consolas;">[12]</td><td style="padding:3px; border:1px solid #e2e8f0; color:#cbd5e1;">-</td></tr>
        </table>
      </div>
    </div>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <div class="theory-box">
      <strong>📌 1. คุณสมบัติพื้นฐาน 2 ประการของ Binary Min-Heap (Two Fundamental Properties):</strong>
      <ol>
        <li><strong>Structure Property (คุณสมบัติเชิงโครงสร้าง):</strong> ต้องเป็น Complete Binary Tree คือโหนดจะเต็มสมบูรณ์ทุกชั้น ยกเว้นชั้นล่างสุดที่เต็มหรือไม่เต็มก็ได้ แต่หากไม่เต็ม โหนดจะต้องบรรจุชิดจากซ้ายไปขวาอย่างต่อเนื่องเสมอ</li>
        <li><strong>Heap-Order Property (คุณสมบัติเชิงอันดับ):</strong> สำหรับโหนด $X$ ใดๆ ที่มี Parent คือ $P$ ค่าใน Parent จะต้องน้อยกว่าหรือเท่ากับค่าใน Child เสมอ ($\text{Key}(P) \le \text{Key}(X)$) ส่งผลให้โหนดที่มีค่าน้อยที่สุดจะอยู่ที่ Root เสมอ</li>
      </ol>
    </div>

    <p><strong>2. ผังต้นไม้ (Tree Diagrams) ครบทั้ง 4 ขั้นตอน:</strong></p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 270" width="100%" height="270" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="280" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Stage 1: Binary Min-Heap Tree หลังแทรกครบ 12 ตัว (Insert 12 Keys)</text>
  <line x1="270" y1="66" x2="140" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="270" y1="66" x2="400" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="75" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="205" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="335" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="465" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="45" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="105" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="175" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="235" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="335" y1="191" x2="305" y2="224" stroke="#475569" stroke-width="1.6"/>
  <circle cx="270" cy="50" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="270" y="55" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">1</text>
  <text x="288" y="42" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[1]</text>
  <circle cx="140" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="140" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">6</text>
  <text x="158" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[2]</text>
  <circle cx="400" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="400" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">2</text>
  <text x="418" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[3]</text>
  <circle cx="75" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="75" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">10</text>
  <text x="93" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[4]</text>
  <circle cx="205" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="205" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">8</text>
  <text x="223" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[5]</text>
  <circle cx="335" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="335" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="353" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[6]</text>
  <circle cx="465" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="465" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">5</text>
  <text x="483" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[7]</text>
  <circle cx="45" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="45" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">64</text>
  <text x="63" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[8]</text>
  <circle cx="105" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="105" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">14</text>
  <text x="123" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[9]</text>
  <circle cx="175" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="175" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="193" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[10]</text>
  <circle cx="235" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="235" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">15</text>
  <text x="253" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[11]</text>
  <circle cx="305" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="305" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">24</text>
  <text x="323" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[12]</text>
</svg></div>
      <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 270" width="100%" height="270" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="280" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Stage 2: Binary Min-Heap Tree หลัง deleteMin() ครั้งที่ 1</text>
  <line x1="270" y1="66" x2="140" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="270" y1="66" x2="400" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="75" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="205" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="335" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="465" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="45" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="105" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="175" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="235" y2="224" stroke="#475569" stroke-width="1.6"/>
  <circle cx="270" cy="50" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="270" y="55" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">2</text>
  <text x="288" y="42" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[1]</text>
  <circle cx="140" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="140" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">6</text>
  <text x="158" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[2]</text>
  <circle cx="400" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="400" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">5</text>
  <text x="418" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[3]</text>
  <circle cx="75" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="75" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">10</text>
  <text x="93" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[4]</text>
  <circle cx="205" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="205" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">8</text>
  <text x="223" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[5]</text>
  <circle cx="335" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="335" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="353" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[6]</text>
  <circle cx="465" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="465" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">24</text>
  <text x="483" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[7]</text>
  <circle cx="45" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="45" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">64</text>
  <text x="63" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[8]</text>
  <circle cx="105" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="105" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">14</text>
  <text x="123" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[9]</text>
  <circle cx="175" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="175" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="193" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[10]</text>
  <circle cx="235" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="235" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">15</text>
  <text x="253" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[11]</text>
</svg></div>
      <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 270" width="100%" height="270" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="280" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Stage 3: Binary Min-Heap Tree หลังแทรกเลข 3 (Insert 3)</text>
  <line x1="270" y1="66" x2="140" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="270" y1="66" x2="400" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="75" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="205" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="335" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="465" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="45" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="105" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="175" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="235" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="335" y1="191" x2="305" y2="224" stroke="#475569" stroke-width="1.6"/>
  <circle cx="270" cy="50" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="270" y="55" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">2</text>
  <text x="288" y="42" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[1]</text>
  <circle cx="140" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="140" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">6</text>
  <text x="158" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[2]</text>
  <circle cx="400" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="400" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">3</text>
  <text x="418" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[3]</text>
  <circle cx="75" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="75" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">10</text>
  <text x="93" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[4]</text>
  <circle cx="205" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="205" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">8</text>
  <text x="223" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[5]</text>
  <circle cx="335" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="335" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">5</text>
  <text x="353" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[6]</text>
  <circle cx="465" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="465" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">24</text>
  <text x="483" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[7]</text>
  <circle cx="45" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="45" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">64</text>
  <text x="63" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[8]</text>
  <circle cx="105" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="105" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">14</text>
  <text x="123" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[9]</text>
  <circle cx="175" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="175" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="193" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[10]</text>
  <circle cx="235" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="235" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">15</text>
  <text x="253" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[11]</text>
  <circle cx="305" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="305" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="323" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[12]</text>
</svg></div>
      <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 270" width="100%" height="270" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="280" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Stage 4: Binary Min-Heap Tree หลัง deleteMin() ครั้งที่ 2</text>
  <line x1="270" y1="66" x2="140" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="270" y1="66" x2="400" y2="94" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="75" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="140" y1="126" x2="205" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="335" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="400" y1="126" x2="465" y2="159" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="45" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="75" y1="191" x2="105" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="175" y2="224" stroke="#475569" stroke-width="1.6"/>
  <line x1="205" y1="191" x2="235" y2="224" stroke="#475569" stroke-width="1.6"/>
  <circle cx="270" cy="50" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="270" y="55" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">3</text>
  <text x="288" y="42" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[1]</text>
  <circle cx="140" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="140" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">6</text>
  <text x="158" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[2]</text>
  <circle cx="400" cy="110" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="400" y="115" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">5</text>
  <text x="418" y="102" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[3]</text>
  <circle cx="75" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="75" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">10</text>
  <text x="93" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[4]</text>
  <circle cx="205" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="205" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">8</text>
  <text x="223" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[5]</text>
  <circle cx="335" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="335" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="353" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[6]</text>
  <circle cx="465" cy="175" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="465" y="180" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">24</text>
  <text x="483" y="167" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[7]</text>
  <circle cx="45" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="45" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">64</text>
  <text x="63" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[8]</text>
  <circle cx="105" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="105" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">14</text>
  <text x="123" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[9]</text>
  <circle cx="175" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="175" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">20</text>
  <text x="193" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[10]</text>
  <circle cx="235" cy="240" r="16" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="235" y="245" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">15</text>
  <text x="253" y="232" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[11]</text>
</svg></div>
    </div>

    <p><strong>3. ตารางอาร์เรย์แนวตั้ง 4 ตาราง (Vertical Arrays Matching Exam Paper):</strong></p>
    <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; margin:16px 0;">
  <div style="flex:1; min-width:140px; max-width:200px; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
    <div style="background:#1e293b; color:#ffffff; padding:8px; font-size:12px; font-weight:bold; text-align:center;">2.1 (Insert 12 Keys)</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px;">
      <tr style="background:#f1f5f9; color:#64748b; font-weight:bold;"><th style="padding:4px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:4px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
      <tr style="background:#fafafa;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[0]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><span style="color:#94a3b8; font-style:italic;">unused</span></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[1]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">1</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[2]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">6</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[3]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">2</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[4]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">10</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[5]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">8</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[6]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[7]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">5</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[8]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">64</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[9]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">14</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[10]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[11]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">15</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[12]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">24</strong></td></tr>
    </table>
  </div>
  <div style="flex:1; min-width:140px; max-width:200px; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
    <div style="background:#1e293b; color:#ffffff; padding:8px; font-size:12px; font-weight:bold; text-align:center;">2.2 deleteMin</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px;">
      <tr style="background:#f1f5f9; color:#64748b; font-weight:bold;"><th style="padding:4px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:4px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
      <tr style="background:#fafafa;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[0]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><span style="color:#94a3b8; font-style:italic;">unused</span></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[1]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">2</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[2]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">6</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[3]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">5</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[4]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">10</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[5]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">8</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[6]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[7]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">24</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[8]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">64</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[9]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">14</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[10]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[11]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">15</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[12]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><span style="color:#cbd5e1;">-</span></td></tr>
    </table>
  </div>
  <div style="flex:1; min-width:140px; max-width:200px; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
    <div style="background:#1e293b; color:#ffffff; padding:8px; font-size:12px; font-weight:bold; text-align:center;">2.3 Insert</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px;">
      <tr style="background:#f1f5f9; color:#64748b; font-weight:bold;"><th style="padding:4px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:4px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
      <tr style="background:#fafafa;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[0]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><span style="color:#94a3b8; font-style:italic;">unused</span></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[1]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">2</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[2]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">6</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[3]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">3</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[4]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">10</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[5]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">8</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[6]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">5</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[7]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">24</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[8]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">64</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[9]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">14</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[10]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[11]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">15</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[12]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
    </table>
  </div>
  <div style="flex:1; min-width:140px; max-width:200px; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
    <div style="background:#1e293b; color:#ffffff; padding:8px; font-size:12px; font-weight:bold; text-align:center;">2.4 deleteMin</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px;">
      <tr style="background:#f1f5f9; color:#64748b; font-weight:bold;"><th style="padding:4px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:4px; border-bottom:1px solid #cbd5e1;">Value</th></tr>
      <tr style="background:#fafafa;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[0]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><span style="color:#94a3b8; font-style:italic;">unused</span></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[1]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">3</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[2]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">6</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[3]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">5</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[4]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">10</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[5]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">8</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[6]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[7]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">24</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[8]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">64</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[9]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">14</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[10]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">20</strong></td></tr>
      <tr style="background:#eff6ff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[11]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><strong style="color:#1e40af;">15</strong></td></tr>
      <tr style="background:#ffffff;"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[12]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;"><span style="color:#cbd5e1;">-</span></td></tr>
    </table>
  </div>
</div>
  </div>

  <!-- QUESTION 3 -->
    <!-- SUB-QUESTION 2.5: 15-KEY MIN-HEAP WORKSHEET -->
  <h3 class="question-title" style="background:#eff6ff; border-left-color:#2563eb; margin-top:25px;">
    <span>2.5 การสร้าง Binary Min-Heap 15 ตัว และการ deleteMin() [ถอดรหัสจากใบงานจริง 2569 ภาพที่ 1]</span>
    <span class="score-badge">Score: 8 Marks (8 คะแนน: 5 + 3)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Insert the following sequence of 15 integers into an initially empty Binary Min-Heap sequentially:</p>
  $$\mathbf{10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2}$$
  <p>Show the step-by-step tree insertion or array state up to 15 elements. Then perform one <code>deleteMin()</code> operation. Write the resulting array and show how the replacement element percolates down.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - จากใบงานจริงในห้องเรียน 2569 ภาพที่ 1):</strong> ให้นักศึกษาทำการ insert ข้อมูลจำนวน 15 ตัว: <strong>10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2</strong> เข้าไปใน Binary Min-Heap ว่าง และกรอกข้อมูลลงใน Array ขนาด 15 ช่อง จากนั้นให้ทำคำสั่ง <code>deleteMin()</code> 1 ครั้ง พร้อมเขียนผลลัพธ์ของ Array หลังการลบ
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#1e3a8a; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 2.5: อาร์เรย์ของ Binary Min-Heap ขนาด 15 ช่อง และหลัง deleteMin()</div>
    <table style="text-align:center; font-size:12px;">
      <thead>
        <tr style="background:#1e3a8a; color:white;">
          <th style="width:110px;">การทำงาน</th>
          <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th>
          <th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="font-weight:bold; background:#f1f5f9;">หลัง Insert 15 ตัว</td>
          <td style="color:#94a3b8;">-</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
        <tr>
          <td style="font-weight:bold; background:#fef2f2; color:#b91c1c;">หลัง deleteMin()</td>
          <td style="color:#94a3b8;">-</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#f1f5f9;">-</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดข้อ 2.5 (15-Key Min-Heap Insertion &amp; deleteMin Solution):</div>
    <p><strong>1. ลำดับการแทรกข้อมูลและ Percolate Up ทีละตัว:</strong></p>
    <ul>
      <li>Insert 10: <code>[-, 10]</code></li>
      <li>Insert 12: <code>[-, 10, 12]</code></li>
      <li>Insert 1: เลื่อน 10 ลงมา &rarr; <code>[-, 1, 12, 10]</code></li>
      <li>Insert 14: <code>[-, 1, 12, 10, 14]</code></li>
      <li>Insert 6: เลื่อน 12 ลงมา &rarr; <code>[-, 1, 6, 10, 14, 12]</code></li>
      <li>Insert 5: เลื่อน 10 ลงมา &rarr; <code>[-, 1, 6, 5, 14, 12, 10]</code></li>
      <li>Insert 8: <code>[-, 1, 6, 5, 14, 12, 10, 8]</code></li>
      <li>Insert 15: <code>[-, 1, 6, 5, 14, 12, 10, 8, 15]</code></li>
      <li>Insert 3: เลื่อน 14 &rarr; 6 ลงมา &rarr; <code>[-, 1, 3, 5, 6, 12, 10, 8, 15, 14]</code></li>
      <li>Insert 9: เลื่อน 12 ลงมา &rarr; <code>[-, 1, 3, 5, 6, 9, 10, 8, 15, 14, 12]</code></li>
      <li>Insert 7: เลื่อน 9 ลงมา &rarr; <code>[-, 1, 3, 5, 6, 7, 10, 8, 15, 14, 12, 9]</code></li>
      <li>Insert 4: เลื่อน 10 &rarr; 5 ลงมา &rarr; <code>[-, 1, 3, 4, 6, 7, 5, 8, 15, 14, 12, 9, 10]</code></li>
      <li>Insert 11: <code>[-, 1, 3, 4, 6, 7, 5, 8, 15, 14, 12, 9, 10, 11]</code></li>
      <li>Insert 13: <code>[-, 1, 3, 4, 6, 7, 5, 8, 15, 14, 12, 9, 10, 11, 13]</code></li>
      <li>Insert 2: อยู่ช่อง 15 &rarr; เทียบ Parent ช่อง 7 (ค่า 8): $2 < 8$ เลื่อน 8 ลงช่อง 15, hole=7 &rarr; เทียบ Parent ช่อง 3 (ค่า 4): $2 < 4$ เลื่อน 4 ลงช่อง 7, hole=3 &rarr; เทียบ Parent ช่อง 1 (ค่า 1): $2 < 1$ (False) จบการ Percolate วาง 2 ที่ช่อง 3!</li>
    </ul>

    <p><strong>ตารางอาร์เรย์หลังแทรกครบ 15 ตัว:</strong></p>
    <table style="text-align:center; font-size:12px;">
      <tr style="background:#1e3a8a; color:white;">
        <th>Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th>
      </tr>
      <tr>
        <td style="font-weight:bold; background:#f1f5f9;">Value</td>
        <td style="color:#94a3b8;">-</td><td><strong>1</strong></td><td><strong>3</strong></td><td><strong>2</strong></td><td><strong>6</strong></td><td><strong>7</strong></td><td><strong>5</strong></td><td><strong>4</strong></td><td><strong>15</strong></td><td><strong>14</strong></td><td><strong>12</strong></td><td><strong>9</strong></td><td><strong>10</strong></td><td><strong>11</strong></td><td><strong>13</strong></td><td><strong>8</strong></td>
      </tr>
    </table>

    <p><strong>2. ขั้นตอนการทำงานของ deleteMin():</strong></p>
    <ul>
      <li>ลบ Root (ค่า 1) ออกจากช่อง 1 &rarr; เกิด <code>hole = 1</code></li>
      <li>นำค่าตัวสุดท้ายท้ายแถวคือ <strong>8</strong> (จากช่อง 15) มาเตรียม Percolate Down</li>
      <li>เทียบลูกของ hole 1: ช่อง 2 (ค่า 3) และช่อง 3 (ค่า 2) &rarr; ลูกที่น้อยกว่าคือ <strong>2 (ช่อง 3)</strong> &rarr; $8 > 2$ ดึง 2 ขึ้นมาที่ช่อง 1, เลื่อน <code>hole = 3</code></li>
      <li>เทียบลูกของ hole 3: ช่อง 6 (ค่า 5) และช่อง 7 (ค่า 4) &rarr; ลูกที่น้อยกว่าคือ <strong>4 (ช่อง 7)</strong> &rarr; $8 > 4$ ดึง 4 ขึ้นมาที่ช่อง 3, เลื่อน <code>hole = 7</code></li>
      <li>เทียบลูกของ hole 7: มีเฉพาะลูกซ้ายช่อง 14 (ค่า 13) &rarr; $8 < 13$ (เงื่อนไขเป็นเท็จ) หยุดการ Percolate Down วาง <strong>8</strong> ลงที่ช่อง 7!</li>
    </ul>

    <p><strong>ตารางอาร์เรย์สุดท้ายหลัง deleteMin():</strong></p>
    <table style="text-align:center; font-size:12px;">
      <tr style="background:#b91c1c; color:white;">
        <th>Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th>
      </tr>
      <tr>
        <td style="font-weight:bold; background:#fef2f2;">Value</td>
        <td style="color:#94a3b8;">-</td><td><strong>2</strong></td><td><strong>3</strong></td><td><strong>4</strong></td><td><strong>6</strong></td><td><strong>7</strong></td><td><strong>5</strong></td><td><strong>8</strong></td><td><strong>15</strong></td><td><strong>14</strong></td><td><strong>12</strong></td><td><strong>9</strong></td><td><strong>10</strong></td><td><strong>11</strong></td><td><strong>13</strong></td><td style="background:#f1f5f9; color:#94a3b8;">-</td>
      </tr>
    </table>
  </div>


  <h2 id="q3" class="part-title">Question 3: Insertion Sort Tracing &amp; Position Moves (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 281-285 / สไลด์ Insertion Sort อ.ประดิษฐ์</div>

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (สูตรลัด 1 นาที vs 1 ชั่วโมง):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>Worst Case (ข้อมูลเรียงกลับทิศทาง):</strong> จำนวน Position Moves ทั้งหมดคือผลรวมอนุกรมเลขคณิต $\frac{N(N-1)}{2}$ เช่น $N=6 \implies 15$ ครั้ง, $N=8 \implies 28$ ครั้ง, $N=10 \implies 45$ ครั้ง มองอนุกรมให้ออกจะประหยัดเวลาทำข้อสอบได้เป็นชั่วโมง<br>
      • <strong>Best Case (ข้อมูลเรียงอยู่แล้ว):</strong> Position Moves $= 0$ ครั้ง, Time Complexity $= O(N)$
    </p>
  </div>

  <h3 class="question-title">
    <span>3.1 Tracing Array States &amp; Shifting Counts across Passes</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an array of 12 integers indexed from $0$ to $11$:</p>
  $$\mathbf{[9, 14, 2, 15, 6, 12, 1, 10, 5, 11, 7, 3]}$$
  <p>Execute the standard <code>insertionSort</code> algorithm from pass $P = 1$ to $P = 11$. For each pass, show the complete array state after insertion, the element being inserted, and the exact count of position moves (element shifts) that occurred.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดอาร์เรย์ขนาด 12 ช่อง (ดัชนี 0 ถึง 11) จงรัน Insertion Sort จากรอบ $P = 1$ ถึง $P = 11$ โดยแสดงสถานะของอาร์เรย์หลังจบรอบ, ตัวเลขที่ถูกนำมาแทรก (tmp), และจำนวนครั้งของการเลื่อนตำแหน่งข้อมูล (position moves)
  </div>

    <!-- SUB-QUESTION 3.2: SORTING CASES -->
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
      Average Case: $O(......)$ สูตรการย้ายตำแหน่ง: $\approx \frac{N(N-1)}{......}$ ครั้ง<br>
      Worst Case: $O(......)$ สูตรการย้ายตำแหน่ง: $\frac{N(N-1)}{......}$ ครั้ง (ข้อมูลเรียงจากมากไปน้อย)
    </p>
  </div>
<div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. สูตรคำนวณกรณีแย่ที่สุด (Worst-Case Formula):</strong></p>
    $$\text{Max Comparisons/Moves} = \frac{N(N-1)}{2} = \frac{12 \times 11}{2} = 66 \text{ ครั้ง}$$

    <p><strong>2. ตาราง Tracing ละเอียดครบทุก Pass (P = 1 ถึง 11):</strong></p>
    <table>
      <thead>
        <tr>
          <th>Pass (P)</th><th>tmp</th><th>Array Content [0 .. 11]</th><th>Moves</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Init</strong></td><td>-</td><td><code>[9, 14, 2, 15, 6, 12, 1, 10, 5, 11, 7, 3]</code></td><td>-</td></tr>
        <tr><td><strong>P = 1</strong></td><td>14</td><td><code>[9, 14, 2, 15, 6, 12, 1, 10, 5, 11, 7, 3]</code></td><td>0</td></tr>
        <tr><td><strong>P = 2</strong></td><td>2</td><td><code>[2, 9, 14, 15, 6, 12, 1, 10, 5, 11, 7, 3]</code></td><td>2</td></tr>
        <tr><td><strong>P = 3</strong></td><td>15</td><td><code>[2, 9, 14, 15, 6, 12, 1, 10, 5, 11, 7, 3]</code></td><td>0</td></tr>
        <tr><td><strong>P = 4</strong></td><td>6</td><td><code>[2, 6, 9, 14, 15, 12, 1, 10, 5, 11, 7, 3]</code></td><td>3</td></tr>
        <tr><td><strong>P = 5</strong></td><td>12</td><td><code>[2, 6, 9, 12, 14, 15, 1, 10, 5, 11, 7, 3]</code></td><td>2</td></tr>
        <tr><td><strong>P = 6</strong></td><td>1</td><td><code>[1, 2, 6, 9, 12, 14, 15, 10, 5, 11, 7, 3]</code></td><td>6</td></tr>
        <tr><td><strong>P = 7</strong></td><td>10</td><td><code>[1, 2, 6, 9, 10, 12, 14, 15, 5, 11, 7, 3]</code></td><td>3</td></tr>
        <tr><td><strong>P = 8</strong></td><td>5</td><td><code>[1, 2, 5, 6, 9, 10, 12, 14, 15, 11, 7, 3]</code></td><td>6</td></tr>
        <tr><td><strong>P = 9</strong></td><td>11</td><td><code>[1, 2, 5, 6, 9, 10, 11, 12, 14, 15, 7, 3]</code></td><td>3</td></tr>
        <tr><td><strong>P = 10</strong></td><td>7</td><td><code>[1, 2, 5, 6, 7, 9, 10, 11, 12, 14, 15, 3]</code></td><td>6</td></tr>
        <tr><td><strong>P = 11</strong></td><td>3</td><td><code>[1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15]</code></td><td>9</td></tr>
      </tbody>
    </table>
    <p><strong>จำนวนครั้งที่มีการขยับเลื่อนตำแหน่งรวม (Total Position Moves):</strong> $0+2+0+3+2+6+3+6+3+6+9 = \mathbf{40 \text{ ครั้ง}}$</p>
  </div>

  <!-- QUESTION 4 -->
  <h2 id="q4" class="part-title">Question 4: Selection Sort &amp; Bubble Sort Tracing (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 285-290 / สไลด์ Selection &amp; Bubble Sort อ.ประดิษฐ์</div>

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (สูตร Inversions &amp; จุดดัก Python):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>สูตรลัด Total Swaps ใน Bubble Sort:</strong> จำนวนครั้งการ Swap ทั้งหมดจะเท่ากับ <strong>จำนวน Inversions ในอาร์เรย์เริ่มต้น 100%</strong> นับตัวทางขวาที่น้อยกว่าทีละตัวแล้วจับบวกกัน ไม่ต้องรันลูป<br>
      • <strong>จุดเด่น Selection Sort:</strong> มีการ Swap ข้อมูลน้อยมากเพียง $O(N)$ ครั้ง (มากสุด $N-1$ ครั้ง) เหมาะมากกับหน่วยความจำที่เขียนซ้ำได้จำกัด<br>
      • <strong>กับดัก <code>range(0)</code>:</strong> ไม่ใช่ <code>None</code> และไม่ใช่ <code>[0]</code> แต่เป็น Empty Sequence Object ที่บันทึกเพียง metadata <code>start=0, stop=0, step=1</code>
    </p>
  </div>

  <h3 class="question-title">
    <span>4.1 Selection Sort &amp; 4.2 Bubble Sort Tracing (5 + 5 = 10 Marks)</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the input array $\mathbf{[64, 25, 12, 22, 11]}$.</p>
  <ol>
    <li>Show the state of the array after each pass of <strong>Selection Sort</strong> until fully sorted. State the min element identified and the swap made.</li>
    <li>Show the state of the array after each pass of <strong>Bubble Sort</strong> with early-termination flag checking.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดอาร์เรย์ $[64, 25, 12, 22, 11]$ จงแสดงผลลัพธ์ของอาร์เรย์ในแต่ละรอบเมื่อเรียงลำดับด้วย Selection Sort (ระบุค่าต่ำสุดที่พบและการสลับ) และแสดงผลลัพธ์แต่ละรอบเมื่อเรียงลำดับด้วย Bubble Sort
  </div>

    <!-- SUB-QUESTION 4.2: BUBBLE & SELECTION CASES -->
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
<div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. การทำงานของ Selection Sort:</strong></p>
    <ul>
      <li><strong>Initial:</strong> <code>[64, 25, 12, 22, 11]</code></li>
      <li><strong>Pass 1:</strong> Min ในช่วง index 0..4 คือ <code>11</code> (index 4) &rarr; สลับกับ index 0 (64) &rarr; <code>[11, 25, 12, 22, 64]</code></li>
      <li><strong>Pass 2:</strong> Min ในช่วง index 1..4 คือ <code>12</code> (index 2) &rarr; สลับกับ index 1 (25) &rarr; <code>[11, 12, 25, 22, 64]</code></li>
      <li><strong>Pass 3:</strong> Min ในช่วง index 2..4 คือ <code>22</code> (index 3) &rarr; สลับกับ index 2 (25) &rarr; <code>[11, 12, 22, 25, 64]</code></li>
      <li><strong>Pass 4:</strong> Min ในช่วง index 3..4 คือ <code>25</code> (index 3) &rarr; อยู่ถูกที่แล้ว ไม่ต้องสลับ &rarr; <code>[11, 12, 22, 25, 64]</code></li>
    </ul>

    <p><strong>2. การทำงานของ Bubble Sort (เปรียบเทียบคู่ติดกัน):</strong></p>
    <ul>
      <li><strong>Pass 1:</strong> ดัน 64 ไปท้ายสุด &rarr; <code>[25, 12, 22, 11, 64]</code> (เกิดการสลับ 4 ครั้ง)</li>
      <li><strong>Pass 2:</strong> ดัน 25 ไปตำแหน่งที่ 3 &rarr; <code>[12, 22, 11, 25, 64]</code> (เกิดการสลับ 2 ครั้ง)</li>
      <li><strong>Pass 3:</strong> ดัน 22 ไปตำแหน่งที่ 2 &rarr; <code>[12, 11, 22, 25, 64]</code> (เกิดการสลับ 1 ครั้ง)</li>
      <li><strong>Pass 4:</strong> สลับ 12 กับ 11 &rarr; <code>[11, 12, 22, 25, 64]</code> (เกิดการสลับ 1 ครั้ง)</li>
    </ul>
  </div>

  <!-- QUESTION 5 -->
  <h2 id="q5" class="part-title">Question 5: Topological Sort in DAG (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 367-374 / สไลด์ Topological Sort อ.ประดิษฐ์</div>

  <h3 class="question-title">
    <span>5.1 Indegree Array Tracing &amp; Topological Ordering (Strict Comma Output Rule)</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> A Directed Acyclic Graph (DAG) with <strong>7 vertices (1 to 7)</strong> is given by the diagram and Adjacency List below:</p>
  
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
    <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 340" width="100%" height="340" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <defs>
    <marker id="arrow-topo26" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="270" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#334155">Directed Acyclic Graph (DAG) [Lecture 10 &amp; Exam 2026 Q5]: |V|=7, |E|=12</text>
  <line x1="170.0" y1="60.0" x2="366.0" y2="60.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="138.0" y1="76.0" x2="74.4" y2="160.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="164.1" y1="74.1" x2="253.0" y2="163.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="375.9" y1="74.1" x2="287.0" y2="163.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="402.0" y1="76.0" x2="465.6" y2="160.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="72.0" y1="196.0" x2="135.6" y2="280.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="250.0" y1="180.0" x2="84.0" y2="180.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="255.9" y1="194.1" x2="167.0" y2="283.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="284.1" y1="194.1" x2="373.0" y2="283.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="460.0" y1="180.0" x2="294.0" y2="180.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="468.0" y1="196.0" x2="404.4" y2="280.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <line x1="370.0" y1="300.0" x2="174.0" y2="300.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>
  <circle cx="150" cy="60" r="20" fill="#dbeafe" stroke="#1d4ed8" stroke-width="3"/>
  <text x="150" y="65" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v1</text>
  <text x="150" y="34" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-weight="bold" fill="#1d4ed8">SOURCE</text>
  <circle cx="390" cy="60" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="390" y="65" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v2</text>
  <circle cx="60" cy="180" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="60" y="185" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v3</text>
  <circle cx="270" cy="180" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="270" y="185" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v4</text>
  <circle cx="480" cy="180" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="480" y="185" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v5</text>
  <circle cx="150" cy="300" r="20" fill="#fef2f2" stroke="#dc2626" stroke-width="3"/>
  <text x="150" y="305" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v6</text>
  <text x="150" y="332" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-weight="bold" fill="#dc2626">SINK</text>
  <circle cx="390" cy="300" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="390" y="305" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v7</text>
</svg></div>
    <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 370" width="100%" height="370" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <defs>
    <marker id="arrow-adj" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="280" y="26" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13.5" font-weight="bold" fill="#1e293b">Adjacency List: Directed Acyclic Graph (7 Vertices)</text>
  <text x="23" y="71" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">1</text>
  <rect x="35" y="50" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="50" x2="75" y2="82" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">1</text>
  <circle cx="85" cy="66" r="3" fill="#0284c7"/>
  <line x1="85" y1="66" x2="115" y2="66" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="51" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="51" x2="151" y2="81" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">2</text>
  <circle cx="161" cy="66" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="66" x2="191" y2="66" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="51" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="51" x2="227" y2="81" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">4</text>
  <circle cx="237" cy="66" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="66" x2="267" y2="66" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="267" y="51" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="303" y1="51" x2="303" y2="81" stroke="#334155" stroke-width="1.2"/>
  <text x="285" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">3</text>
  <circle cx="313" cy="66" r="2.8" fill="#0284c7"/>
  <line x1="313" y1="66" x2="337" y2="66" stroke="#334155" stroke-width="1.5"/>
  <line x1="337" y1="66" x2="337" y2="74" stroke="#334155" stroke-width="1.5"/>
  <line x1="328" y1="75" x2="346" y2="75" stroke="#334155" stroke-width="2"/>
  <line x1="331" y1="78" x2="343" y2="78" stroke="#334155" stroke-width="1.8"/>
  <line x1="334" y1="81" x2="340" y2="81" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="113" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">2</text>
  <rect x="35" y="92" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="92" x2="75" y2="124" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="113" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">2</text>
  <circle cx="85" cy="108" r="3" fill="#0284c7"/>
  <line x1="85" y1="108" x2="115" y2="108" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="93" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="93" x2="151" y2="123" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="113" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">4</text>
  <circle cx="161" cy="108" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="108" x2="191" y2="108" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="93" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="93" x2="227" y2="123" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="113" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">5</text>
  <circle cx="237" cy="108" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="108" x2="261" y2="108" stroke="#334155" stroke-width="1.5"/>
  <line x1="261" y1="108" x2="261" y2="116" stroke="#334155" stroke-width="1.5"/>
  <line x1="252" y1="117" x2="270" y2="117" stroke="#334155" stroke-width="2"/>
  <line x1="255" y1="120" x2="267" y2="120" stroke="#334155" stroke-width="1.8"/>
  <line x1="258" y1="123" x2="264" y2="123" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="155" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">3</text>
  <rect x="35" y="134" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="134" x2="75" y2="166" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="155" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">3</text>
  <circle cx="85" cy="150" r="3" fill="#0284c7"/>
  <line x1="85" y1="150" x2="115" y2="150" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="135" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="135" x2="151" y2="165" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="155" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">6</text>
  <circle cx="161" cy="150" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="150" x2="185" y2="150" stroke="#334155" stroke-width="1.5"/>
  <line x1="185" y1="150" x2="185" y2="158" stroke="#334155" stroke-width="1.5"/>
  <line x1="176" y1="159" x2="194" y2="159" stroke="#334155" stroke-width="2"/>
  <line x1="179" y1="162" x2="191" y2="162" stroke="#334155" stroke-width="1.8"/>
  <line x1="182" y1="165" x2="188" y2="165" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="197" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">4</text>
  <rect x="35" y="176" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="176" x2="75" y2="208" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">4</text>
  <circle cx="85" cy="192" r="3" fill="#0284c7"/>
  <line x1="85" y1="192" x2="115" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="177" x2="151" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">3</text>
  <circle cx="161" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="192" x2="191" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="177" x2="227" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">6</text>
  <circle cx="237" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="192" x2="267" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="267" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="303" y1="177" x2="303" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="285" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">7</text>
  <circle cx="313" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="313" y1="192" x2="337" y2="192" stroke="#334155" stroke-width="1.5"/>
  <line x1="337" y1="192" x2="337" y2="200" stroke="#334155" stroke-width="1.5"/>
  <line x1="328" y1="201" x2="346" y2="201" stroke="#334155" stroke-width="2"/>
  <line x1="331" y1="204" x2="343" y2="204" stroke="#334155" stroke-width="1.8"/>
  <line x1="334" y1="207" x2="340" y2="207" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="239" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">5</text>
  <rect x="35" y="218" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="218" x2="75" y2="250" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="239" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">5</text>
  <circle cx="85" cy="234" r="3" fill="#0284c7"/>
  <line x1="85" y1="234" x2="115" y2="234" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="219" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="219" x2="151" y2="249" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="239" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">4</text>
  <circle cx="161" cy="234" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="234" x2="191" y2="234" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="219" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="219" x2="227" y2="249" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="239" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">7</text>
  <circle cx="237" cy="234" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="234" x2="261" y2="234" stroke="#334155" stroke-width="1.5"/>
  <line x1="261" y1="234" x2="261" y2="242" stroke="#334155" stroke-width="1.5"/>
  <line x1="252" y1="243" x2="270" y2="243" stroke="#334155" stroke-width="2"/>
  <line x1="255" y1="246" x2="267" y2="246" stroke="#334155" stroke-width="1.8"/>
  <line x1="258" y1="249" x2="264" y2="249" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="281" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">6</text>
  <rect x="35" y="260" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="260" x2="75" y2="292" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="281" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">6</text>
  <circle cx="85" cy="276" r="3" fill="#0284c7"/>
  <path d="M 85 276 L 117 276 L 117 288" fill="none" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <line x1="108" y1="290" x2="126" y2="290" stroke="#334155" stroke-width="2"/>
  <line x1="111" y1="293" x2="123" y2="293" stroke="#334155" stroke-width="1.8"/>
  <line x1="114" y1="296" x2="120" y2="296" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="323" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">7</text>
  <rect x="35" y="302" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="302" x2="75" y2="334" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="323" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">7</text>
  <circle cx="85" cy="318" r="3" fill="#0284c7"/>
  <line x1="85" y1="318" x2="115" y2="318" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="303" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="303" x2="151" y2="333" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="323" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">6</text>
  <circle cx="161" cy="318" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="318" x2="185" y2="318" stroke="#334155" stroke-width="1.5"/>
  <line x1="185" y1="318" x2="185" y2="326" stroke="#334155" stroke-width="1.5"/>
  <line x1="176" y1="327" x2="194" y2="327" stroke="#334155" stroke-width="2"/>
  <line x1="179" y1="330" x2="191" y2="330" stroke="#334155" stroke-width="1.8"/>
  <line x1="182" y1="333" x2="188" y2="333" stroke="#334155" stroke-width="1.5"/>
</svg></div>
  </div>

  <ol>
    <li>Fill in the <strong>Indegree Array</strong> below across all 7 rounds of Kahn's Algorithm.</li>
    <li>Draw the resulting state of the <strong>Circular Queue</strong> (size 7) when the algorithm terminates. State <code>front</code> and <code>back</code> pointer values.</li>
    <li>Write the final <strong>Topological Ordering</strong> as a comma-separated list (e.g. <code>v1, v2, ...</code>). <strong>DO NOT USE ARROWS!</strong></li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดกราฟ DAG 7 จุดยอดตามภาพและ Adjacency List จงเติมตาราง Indegree Array ให้สมบูรณ์ครบ 7 รอบ, วาดภาพ Circular Queue เมื่อจบขั้นตอนพร้อมระบุ front และ back, และเขียนลำดับ Topological Ordering คั่นด้วยเครื่องหมายจุลภาคเท่านั้น (ห้ามใช้ลูกศร)
  </div>

  <div class="blank-sheet-box">
    <div style="margin:16px 0; font-family:'Segoe UI', Tahoma, sans-serif;">
  <div style="font-size:14px; font-weight:bold; color:#1e293b; margin-bottom:8px;">📝 ช่องจำลองกระดาษคำตอบ: ตาราง Indegree Array Tracing (ขนาด 7 จุดยอด)</div>
  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
    <div style="flex:3; min-width:480px; overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:8px 6px; border:1px solid #475569; width:85px;">Vertex (v)</th>
            <th style="padding:8px 6px; border:1px solid #475569;">เริ่มต้น (Init)</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 1</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 2</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 3</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 4</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 5</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 6</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 7</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v4</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v5</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v6</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v7</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#e0e7ff; font-weight:bold;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">Enqueue (v)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">&nbsp;</td>
          </tr>
          <tr style="background:#fee2e2; font-weight:bold;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">Dequeue (v)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">&nbsp;</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="flex:1; min-width:160px; max-width:200px;">
      <div style="font-size:13px; font-weight:bold; color:#1e293b; margin-bottom:6px; text-align:center;">📦 Vertical Queue (q)</div>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #475569;">
        <thead><tr style="background:#334155; color:#ffffff;"><th style="padding:6px; border:1px solid #475569; width:45px;">Index</th><th style="padding:6px; border:1px solid #475569;">Vertex</th></tr></thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[6]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[5]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[4]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[3]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[2]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[1]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[0]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div style="margin-top:14px; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:8px; padding:12px;">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">🔄 Horizontal Circular Queue Buffer &amp; Final Pointer Status:</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:10px;">
      <tr style="background:#334155; color:#ffffff; font-size:12px;"><th style="padding:5px;">Index</th><th style="padding:5px; border:1px solid #475569;">[0]</th><th style="padding:5px; border:1px solid #475569;">[1]</th><th style="padding:5px; border:1px solid #475569;">[2]</th><th style="padding:5px; border:1px solid #475569;">[3]</th><th style="padding:5px; border:1px solid #475569;">[4]</th><th style="padding:5px; border:1px solid #475569;">[5]</th><th style="padding:5px; border:1px solid #475569;">[6]</th></tr>
      <tr><td style="padding:6px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; font-size:12px;">q Value</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td></tr>
    </table>
    <div style="display:flex; justify-content:space-around; font-size:12.5px; color:#1e293b; background:#ffffff; padding:8px; border-radius:6px; border:1px solid #e2e8f0; flex-wrap:wrap; gap:10px;">
      <div>• <strong>front</strong> = <span style="color:#dc2626; font-weight:bold;">............</span> (สูตร: <code>(front+1)%7</code>)</div>
      <div>• <strong>back</strong> = <span style="color:#16a34a; font-weight:bold;">............</span> (สูตร: <code>(back+1)%7</code>)</div>
      <div>• <strong>currentSize</strong> = <span style="color:#2563eb; font-weight:bold;">............</span> (Empty)</div>
    </div>
    <div style="margin-top:10px; font-size:12.5px; background:#eff6ff; padding:10px; border-radius:6px; border:1px solid #bfdbfe;">
      <div><strong>ลำดับ Topological Order:</strong> <span style="color:#1d4ed8; font-weight:bold; font-size:14px;">............................................................</span></div>
      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ห้ามใส่ลูกศร <code>-&gt;</code> เด็ดขาด ให้คั่นด้วยเครื่องหมายจุลภาค <code>,</code> เท่านั้น หากใส่ลูกศรจะถูกปรับเป็น 0 คะแนน</div>
    </div>
  </div>
</div>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. ตารางค่า Indegree ทีละรอบ (Indegree Tracking Table):</strong></p>
    <div style="margin:16px 0; font-family:'Segoe UI', Tahoma, sans-serif;">
  <div style="font-size:14px; font-weight:bold; color:#1e293b; margin-bottom:8px;">📝 เฉลยตาราง Indegree Array Tracing ละเอียดครบ 7 รอบ</div>
  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
    <div style="flex:3; min-width:480px; overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:8px 6px; border:1px solid #475569; width:85px;">Vertex (v)</th>
            <th style="padding:8px 6px; border:1px solid #475569;">เริ่มต้น (Init)</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 1</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 2</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 3</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 4</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 5</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 6</th>
            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 7</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">1</del> <strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">2</del> 1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">1</del> <strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v4</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">3</del> 2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">2</del> 1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">1</del> <strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v5</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">1</del> <strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v6</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">3</del> 2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">2</del> 1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">1</del> <strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v7</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">2</del> 1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">1</del> <strong style="color:#15803d;">0</strong> (In Q)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">0 (dq)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">-</td>
          </tr>
          <tr style="background:#e0e7ff; font-weight:bold;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">Enqueue (v)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">5</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">4</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">3, 7</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">6</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">-</td>
          </tr>
          <tr style="background:#fee2e2; font-weight:bold;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">Dequeue (v)</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">-</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">5</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">4</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">7</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">6</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="flex:1; min-width:160px; max-width:200px;">
      <div style="font-size:13px; font-weight:bold; color:#1e293b; margin-bottom:6px; text-align:center;">📦 Vertical Queue (q)</div>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #475569;">
        <thead><tr style="background:#334155; color:#ffffff;"><th style="padding:6px; border:1px solid #475569; width:45px;">Index</th><th style="padding:6px; border:1px solid #475569;">Vertex</th></tr></thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[6]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">6</strong></td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[5]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">7</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[4]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">3</strong></td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[3]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">4</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[2]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">5</strong></td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[1]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">2</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[0]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">1</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div style="margin-top:14px; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:8px; padding:12px;">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">🔄 Horizontal Circular Queue Buffer &amp; Final Pointer Status:</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:10px;">
      <tr style="background:#334155; color:#ffffff; font-size:12px;"><th style="padding:5px;">Index</th><th style="padding:5px; border:1px solid #475569;">[0]</th><th style="padding:5px; border:1px solid #475569;">[1]</th><th style="padding:5px; border:1px solid #475569;">[2]</th><th style="padding:5px; border:1px solid #475569;">[3]</th><th style="padding:5px; border:1px solid #475569;">[4]</th><th style="padding:5px; border:1px solid #475569;">[5]</th><th style="padding:5px; border:1px solid #475569;">[6]</th></tr>
      <tr><td style="padding:6px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; font-size:12px;">q Value</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">1</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">2</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">5</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">4</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">3</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">7</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">6</strong></td></tr>
    </table>
    <div style="display:flex; justify-content:space-around; font-size:12.5px; color:#1e293b; background:#ffffff; padding:8px; border-radius:6px; border:1px solid #e2e8f0; flex-wrap:wrap; gap:10px;">
      <div>• <strong>front</strong> = <span style="color:#dc2626; font-weight:bold;">0</span> (สูตร: <code>(front+1)%7</code>)</div>
      <div>• <strong>back</strong> = <span style="color:#16a34a; font-weight:bold;">6</span> (สูตร: <code>(back+1)%7</code>)</div>
      <div>• <strong>currentSize</strong> = <span style="color:#2563eb; font-weight:bold;">0</span> (Empty)</div>
    </div>
    <div style="margin-top:10px; font-size:12.5px; background:#eff6ff; padding:10px; border-radius:6px; border:1px solid #bfdbfe;">
      <div><strong>ลำดับ Topological Order:</strong> <span style="color:#1d4ed8; font-weight:bold; font-size:14px;">1, 2, 5, 4, 3, 7, 6</span></div>
      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ห้ามใส่ลูกศร <code>-&gt;</code> เด็ดขาด ให้คั่นด้วยเครื่องหมายจุลภาค <code>,</code> เท่านั้น หากใส่ลูกศรจะถูกปรับเป็น 0 คะแนน</div>
    </div>
  </div>
</div>

    <p><strong>2. การทำงานของ Circular Queue (ขนาด 7 ช่อง, ดัชนี 0..6):</strong></p>
    <div style="max-width:560px; margin:14px 0;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="270" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <defs>
    <marker id="arrow-front" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
    <marker id="arrow-back" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#16a34a"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="240" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">สถานะ Circular Queue เมื่อจบขั้นตอน Topological Sort (front=0, back=6)</text>
  <rect x="55" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="79" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[0]</text>
  <text x="79" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">1</text>
  <line x1="79" y1="139" x2="79" y2="110" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-front)"/>
  <text x="79" y="153" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="11" font-weight="bold" fill="#dc2626">front=0</text>
  <rect x="103" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="127" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[1]</text>
  <text x="127" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">2</text>
  <rect x="151" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="175" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[2]</text>
  <text x="175" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">5</text>
  <rect x="199" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="223" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[3]</text>
  <text x="223" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">4</text>
  <rect x="247" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="271" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[4]</text>
  <text x="271" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">3</text>
  <rect x="295" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="319" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[5]</text>
  <text x="319" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">7</text>
  <rect x="343" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="367" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[6]</text>
  <text x="367" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">6</text>
  <line x1="367" y1="175" x2="367" y2="110" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow-back)"/>
  <text x="367" y="189" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="11" font-weight="bold" fill="#16a34a">back=6</text>
  <rect x="416" y="50" width="160" height="185" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" rx="6"/>
  <text x="428" y="72" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">สถานะพอยน์เตอร์จบลูป:</text>
  <text x="428" y="96" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#dc2626">front</tspan> = 0</text>
  <text x="428" y="118" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#16a34a">back</tspan> = 6</text>
  <text x="428" y="140" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#2563eb">currentSize</tspan> = 0</text>
  <line x1="426" y1="152" x2="566" y2="152" stroke="#e2e8f0" stroke-width="1"/>
  <text x="428" y="172" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" fill="#64748b">สูตร Enqueue:</text>
  <text x="428" y="188" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-family="Consolas" fill="#0f172a">back = (back+1)%7</text>
  <text x="428" y="208" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" fill="#64748b">สูตร Dequeue:</text>
  <text x="428" y="224" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-family="Consolas" fill="#0f172a">front = (front+1)%7</text>
</svg>
    </div>

    <p><strong>3. ผลลัพธ์ Topological Ordering:</strong></p>
    <p style="font-size:18px; font-weight:bold; color:#1e40af; text-align:center; background:#dbeafe; padding:12px; border-radius:8px;">
      1, 2, 5, 4, 3, 7, 6 &nbsp;&nbsp;<span style="font-size:14px; font-weight:normal; color:#475569;">(หรือ 1, 2, 5, 4, 7, 3, 6)</span>
    </p>
    <div class="alert-box">
      <strong>🚨 กับดักได้ 0 คะแนน:</strong> ห้ามเขียนลูกศร เช่น <code>1 -&gt; 2 -&gt; 5 -&gt; ...</code> ต้องเขียนคั่นด้วยจุลภาค <code>1, 2, 5, 4, 3, 7, 6</code> เท่านั้น!
    </div>
  </div>

  <!-- QUESTION 6 -->
  <h2 id="q6" class="part-title">Question 6: Unweighted Shortest Path (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 374-381 / สไลด์ Shortest Path อ.ประดิษฐ์</div>

  <h3 class="question-title">
    <span>6.1 BFS Processing Table, Shortest Path to v5 and v7 (With Strict Comma Output Rule)</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the directed graph $G = (V, E)$ with 7 vertices ($V = \{1, 2, 3, 4, 5, 6, 7\}$) defined by the diagram and Adjacency List below:</p>
  
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
    <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 340" width="100%" height="340" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <defs>
    <marker id="arrow-sp26" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="270" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#334155">Directed Graph G = (V, E) [Exam 2026 Question 6]: Source Vertex = 1, |E|=12</text>
  <line x1="170.0" y1="60.0" x2="366.0" y2="60.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="164.1" y1="74.1" x2="253.0" y2="163.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="375.9" y1="74.1" x2="287.0" y2="163.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="402.0" y1="76.0" x2="465.6" y2="160.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <path d="M 70 164 Q 95 105 134 70" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="72.0" y1="196.0" x2="135.6" y2="280.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="250.0" y1="180.0" x2="84.0" y2="180.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="290.0" y1="180.0" x2="456.0" y2="180.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="255.9" y1="194.1" x2="167.0" y2="283.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="284.1" y1="194.1" x2="373.0" y2="283.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="468.0" y1="196.0" x2="404.4" y2="280.8" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <line x1="370.0" y1="300.0" x2="174.0" y2="300.0" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>
  <circle cx="150" cy="60" r="20" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/>
  <text x="150" y="65" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v1</text>
  <text x="150" y="34" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-weight="bold" fill="#2563eb">SOURCE</text>
  <circle cx="390" cy="60" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="390" y="65" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v2</text>
  <circle cx="60" cy="180" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="60" y="185" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v3</text>
  <circle cx="270" cy="180" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="270" y="185" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v4</text>
  <circle cx="480" cy="180" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="480" y="185" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v5</text>
  <circle cx="150" cy="300" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="150" y="305" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v6</text>
  <circle cx="390" cy="300" r="20" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>
  <text x="390" y="305" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v7</text>
</svg></div>
    <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 370" width="100%" height="370" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <defs>
    <marker id="arrow-adj" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="280" y="26" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13.5" font-weight="bold" fill="#1e293b">Adjacency List: Directed Graph (Source = 1, 7 Vertices)</text>
  <text x="23" y="71" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">1</text>
  <rect x="35" y="50" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="50" x2="75" y2="82" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">1</text>
  <circle cx="85" cy="66" r="3" fill="#0284c7"/>
  <line x1="85" y1="66" x2="115" y2="66" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="51" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="51" x2="151" y2="81" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">2</text>
  <circle cx="161" cy="66" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="66" x2="191" y2="66" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="51" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="51" x2="227" y2="81" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="71" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">4</text>
  <circle cx="237" cy="66" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="66" x2="261" y2="66" stroke="#334155" stroke-width="1.5"/>
  <line x1="261" y1="66" x2="261" y2="74" stroke="#334155" stroke-width="1.5"/>
  <line x1="252" y1="75" x2="270" y2="75" stroke="#334155" stroke-width="2"/>
  <line x1="255" y1="78" x2="267" y2="78" stroke="#334155" stroke-width="1.8"/>
  <line x1="258" y1="81" x2="264" y2="81" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="113" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">2</text>
  <rect x="35" y="92" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="92" x2="75" y2="124" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="113" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">2</text>
  <circle cx="85" cy="108" r="3" fill="#0284c7"/>
  <line x1="85" y1="108" x2="115" y2="108" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="93" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="93" x2="151" y2="123" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="113" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">4</text>
  <circle cx="161" cy="108" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="108" x2="191" y2="108" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="93" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="93" x2="227" y2="123" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="113" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">5</text>
  <circle cx="237" cy="108" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="108" x2="261" y2="108" stroke="#334155" stroke-width="1.5"/>
  <line x1="261" y1="108" x2="261" y2="116" stroke="#334155" stroke-width="1.5"/>
  <line x1="252" y1="117" x2="270" y2="117" stroke="#334155" stroke-width="2"/>
  <line x1="255" y1="120" x2="267" y2="120" stroke="#334155" stroke-width="1.8"/>
  <line x1="258" y1="123" x2="264" y2="123" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="155" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">3</text>
  <rect x="35" y="134" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="134" x2="75" y2="166" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="155" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">3</text>
  <circle cx="85" cy="150" r="3" fill="#0284c7"/>
  <line x1="85" y1="150" x2="115" y2="150" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="135" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="135" x2="151" y2="165" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="155" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">1</text>
  <circle cx="161" cy="150" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="150" x2="191" y2="150" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="135" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="135" x2="227" y2="165" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="155" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">6</text>
  <circle cx="237" cy="150" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="150" x2="261" y2="150" stroke="#334155" stroke-width="1.5"/>
  <line x1="261" y1="150" x2="261" y2="158" stroke="#334155" stroke-width="1.5"/>
  <line x1="252" y1="159" x2="270" y2="159" stroke="#334155" stroke-width="2"/>
  <line x1="255" y1="162" x2="267" y2="162" stroke="#334155" stroke-width="1.8"/>
  <line x1="258" y1="165" x2="264" y2="165" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="197" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">4</text>
  <rect x="35" y="176" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="176" x2="75" y2="208" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">4</text>
  <circle cx="85" cy="192" r="3" fill="#0284c7"/>
  <line x1="85" y1="192" x2="115" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="177" x2="151" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">3</text>
  <circle cx="161" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="192" x2="191" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="191" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="227" y1="177" x2="227" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="209" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">5</text>
  <circle cx="237" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="237" y1="192" x2="267" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="267" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="303" y1="177" x2="303" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="285" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">6</text>
  <circle cx="313" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="313" y1="192" x2="343" y2="192" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="343" y="177" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="379" y1="177" x2="379" y2="207" stroke="#334155" stroke-width="1.2"/>
  <text x="361" y="197" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">7</text>
  <circle cx="389" cy="192" r="2.8" fill="#0284c7"/>
  <line x1="389" y1="192" x2="413" y2="192" stroke="#334155" stroke-width="1.5"/>
  <line x1="413" y1="192" x2="413" y2="200" stroke="#334155" stroke-width="1.5"/>
  <line x1="404" y1="201" x2="422" y2="201" stroke="#334155" stroke-width="2"/>
  <line x1="407" y1="204" x2="419" y2="204" stroke="#334155" stroke-width="1.8"/>
  <line x1="410" y1="207" x2="416" y2="207" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="239" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">5</text>
  <rect x="35" y="218" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="218" x2="75" y2="250" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="239" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">5</text>
  <circle cx="85" cy="234" r="3" fill="#0284c7"/>
  <line x1="85" y1="234" x2="115" y2="234" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="219" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="219" x2="151" y2="249" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="239" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">7</text>
  <circle cx="161" cy="234" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="234" x2="185" y2="234" stroke="#334155" stroke-width="1.5"/>
  <line x1="185" y1="234" x2="185" y2="242" stroke="#334155" stroke-width="1.5"/>
  <line x1="176" y1="243" x2="194" y2="243" stroke="#334155" stroke-width="2"/>
  <line x1="179" y1="246" x2="191" y2="246" stroke="#334155" stroke-width="1.8"/>
  <line x1="182" y1="249" x2="188" y2="249" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="281" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">6</text>
  <rect x="35" y="260" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="260" x2="75" y2="292" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="281" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">6</text>
  <circle cx="85" cy="276" r="3" fill="#0284c7"/>
  <path d="M 85 276 L 117 276 L 117 288" fill="none" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <line x1="108" y1="290" x2="126" y2="290" stroke="#334155" stroke-width="2"/>
  <line x1="111" y1="293" x2="123" y2="293" stroke="#334155" stroke-width="1.8"/>
  <line x1="114" y1="296" x2="120" y2="296" stroke="#334155" stroke-width="1.5"/>
  <text x="23" y="323" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">7</text>
  <rect x="35" y="302" width="60" height="32" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>
  <line x1="75" y1="302" x2="75" y2="334" stroke="#334155" stroke-width="1.2"/>
  <text x="55" y="323" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">7</text>
  <circle cx="85" cy="318" r="3" fill="#0284c7"/>
  <line x1="85" y1="318" x2="115" y2="318" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>
  <rect x="115" y="303" width="56" height="30" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>
  <line x1="151" y1="303" x2="151" y2="333" stroke="#334155" stroke-width="1.2"/>
  <text x="133" y="323" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">6</text>
  <circle cx="161" cy="318" r="2.8" fill="#0284c7"/>
  <line x1="161" y1="318" x2="185" y2="318" stroke="#334155" stroke-width="1.5"/>
  <line x1="185" y1="318" x2="185" y2="326" stroke="#334155" stroke-width="1.5"/>
  <line x1="176" y1="327" x2="194" y2="327" stroke="#334155" stroke-width="2"/>
  <line x1="179" y1="330" x2="191" y2="330" stroke="#334155" stroke-width="1.8"/>
  <line x1="182" y1="333" x2="188" y2="333" stroke="#334155" stroke-width="1.5"/>
</svg></div>
  </div>

  <ol>
    <li>Execute the Unweighted Shortest Path algorithm (BFS) using <strong>Source Vertex = 1</strong>. Complete the table tracking <code>Known</code>, $d_v$ (shortest distance), and $p_v$ (previous vertex) with Queue buffer alongside.</li>
    <li>State the shortest path and path length from vertex 1 to <strong>vertex 5</strong>.</li>
    <li>State the shortest path and path length from vertex 1 to <strong>vertex 7</strong>.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดกราฟระบุทิศทาง 7 จุดยอดตามภาพและ Adjacency List จงรันขั้นตอนวิธี Unweighted Shortest Path (BFS) โดยให้จุดยอด 1 เป็นจุดเริ่มต้น เติมตารางบันทึกสถานะ Known, dv, pv และคิว พร้อมระบุเส้นทางที่สั้นที่สุดพร้อมความยาวเส้นทางไปยังจุดยอด 5 และจุดยอด 7
  </div>

  <div class="blank-sheet-box">
    <div style="margin:16px 0; font-family:'Segoe UI', Tahoma, sans-serif;">
  <div style="font-size:14px; font-weight:bold; color:#1e293b; margin-bottom:8px;">📝 ช่องจำลองกระดาษคำตอบ: ตารางประมวลผล Shortest Path (Known, Dist, Path) (Source Vertex = 1)</div>
  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
    <div style="flex:2; min-width:320px;">
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:13px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:8px 6px; border:1px solid #475569; width:75px;">Vertex (v)</th>
            <th style="padding:8px 6px; border:1px solid #475569; width:85px;">Known</th>
            <th style="padding:8px 6px; border:1px solid #475569;">Dist (Dv)</th>
            <th style="padding:8px 6px; border:1px solid #475569;">Path (Pv)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#eff6ff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v4</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v5</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v6</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v7</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#e0e7ff; font-weight:bold;">
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#1e1b4b; text-align:left;" colspan="2">Enqueue Sequence:</td>
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#1e1b4b;" colspan="2">............................................................</td>
          </tr>
          <tr style="background:#fee2e2; font-weight:bold;">
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#991b1b; text-align:left;" colspan="2">Dequeue Sequence:</td>
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#991b1b;" colspan="2">............................................................</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="flex:1; min-width:170px; max-width:220px;">
      <div style="font-size:13px; font-weight:bold; color:#1e293b; margin-bottom:6px; text-align:center;">📦 Vertical Queue (q)</div>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #475569;">
        <thead><tr style="background:#334155; color:#ffffff;"><th style="padding:6px; border:1px solid #475569; width:45px;">Index</th><th style="padding:6px; border:1px solid #475569;">Vertex</th></tr></thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[6]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[5]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[4]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[3]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[2]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[1]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[0]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;">&nbsp;</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div style="margin-top:14px; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:8px; padding:12px;">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">🔄 Horizontal Circular Queue Buffer &amp; Final Pointer Status:</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:10px;">
      <tr style="background:#334155; color:#ffffff; font-size:12px;"><th style="padding:5px;">Index</th><th style="padding:5px; border:1px solid #475569;">[0]</th><th style="padding:5px; border:1px solid #475569;">[1]</th><th style="padding:5px; border:1px solid #475569;">[2]</th><th style="padding:5px; border:1px solid #475569;">[3]</th><th style="padding:5px; border:1px solid #475569;">[4]</th><th style="padding:5px; border:1px solid #475569;">[5]</th><th style="padding:5px; border:1px solid #475569;">[6]</th></tr>
      <tr><td style="padding:6px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; font-size:12px;">q Value</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">&nbsp;</td></tr>
    </table>
    <div style="display:flex; justify-content:space-around; font-size:12.5px; color:#1e293b; background:#ffffff; padding:8px; border-radius:6px; border:1px solid #e2e8f0; flex-wrap:wrap; gap:10px;">
      <div>• <strong>front</strong> = <span style="color:#dc2626; font-weight:bold;">............</span> (สูตร: <code>(front+1)%7</code>)</div>
      <div>• <strong>back</strong> = <span style="color:#16a34a; font-weight:bold;">............</span> (สูตร: <code>(back+1)%7</code>)</div>
      <div>• <strong>currentSize</strong> = <span style="color:#2563eb; font-weight:bold;">............</span> (Empty)</div>
    </div>
    <div style="margin-top:10px; font-size:12.5px; background:#eff6ff; padding:10px; border-radius:6px; border:1px solid #bfdbfe; line-height:1.7;">
      <div><strong>6.1 Shortest Path จาก 1 ไปยัง 5:</strong> ความยาวเส้นทาง = .............. edges, ลำดับคือ ............................................................</div>
      <div><strong>6.2 Shortest Path จาก 1 ไปยัง 7:</strong> ความยาวเส้นทาง = .............. edges, ลำดับคือ ............................................................</div>
      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ความยาวเส้นทางนับจำนวน Edge (ไม่ใช่ Node) และลำดับต้องคั่นด้วยเครื่องหมายจุลภาค <code>,</code> ห้ามใส่ลูกศร <code>-&gt;</code> เด็ดขาด!</div>
    </div>
  </div>
</div>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. ตารางประมวลผล Shortest Path (การขีดฆ่าอัปเดตตามลำดับ BFS):</strong></p>
    <div style="margin:16px 0; font-family:'Segoe UI', Tahoma, sans-serif;">
  <div style="font-size:14px; font-weight:bold; color:#1e293b; margin-bottom:8px;">📝 เฉลยละเอียดตารางประมวลผล Shortest Path (การขีดฆ่าอัปเดตตามลำดับ BFS) (Source Vertex = 1)</div>
  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
    <div style="flex:2; min-width:320px;">
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:13px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:#ffffff;">
            <th style="padding:8px 6px; border:1px solid #475569; width:75px;">Vertex (v)</th>
            <th style="padding:8px 6px; border:1px solid #475569; width:85px;">Known</th>
            <th style="padding:8px 6px; border:1px solid #475569;">Dist (Dv)</th>
            <th style="padding:8px 6px; border:1px solid #475569;">Path (Pv)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#eff6ff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v1</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">0</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">0</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v2</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">1</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v3</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v4</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">1</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v5</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">2</strong> (หรือ 4)</td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v6</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v7</td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong></td>
            <td style="padding:7px 6px; border:1px solid #cbd5e1;"><del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong> (หรือ 5)</td>
          </tr>
          <tr style="background:#e0e7ff; font-weight:bold;">
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#1e1b4b; text-align:left;" colspan="2">Enqueue Sequence:</td>
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#1e1b4b;" colspan="2">1, 2, 4, 5, 3, 6, 7</td>
          </tr>
          <tr style="background:#fee2e2; font-weight:bold;">
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#991b1b; text-align:left;" colspan="2">Dequeue Sequence:</td>
            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#991b1b;" colspan="2">1, 2, 4, 5, 3, 6, 7</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="flex:1; min-width:170px; max-width:220px;">
      <div style="font-size:13px; font-weight:bold; color:#1e293b; margin-bottom:6px; text-align:center;">📦 Vertical Queue (q)</div>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #475569;">
        <thead><tr style="background:#334155; color:#ffffff;"><th style="padding:6px; border:1px solid #475569; width:45px;">Index</th><th style="padding:6px; border:1px solid #475569;">Vertex</th></tr></thead>
        <tbody>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[6]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">7</strong></td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[5]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">6</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[4]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">3</strong></td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[3]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">5</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[2]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">4</strong></td>
          </tr>
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[1]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">2</strong></td>
          </tr>
          <tr style="background:#ffffff;">
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[0]</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1;"><strong style="color:#1e40af;">1</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div style="margin-top:14px; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:8px; padding:12px;">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">🔄 Horizontal Circular Queue Buffer &amp; Final Pointer Status:</div>
    <table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:10px;">
      <tr style="background:#334155; color:#ffffff; font-size:12px;"><th style="padding:5px;">Index</th><th style="padding:5px; border:1px solid #475569;">[0]</th><th style="padding:5px; border:1px solid #475569;">[1]</th><th style="padding:5px; border:1px solid #475569;">[2]</th><th style="padding:5px; border:1px solid #475569;">[3]</th><th style="padding:5px; border:1px solid #475569;">[4]</th><th style="padding:5px; border:1px solid #475569;">[5]</th><th style="padding:5px; border:1px solid #475569;">[6]</th></tr>
      <tr><td style="padding:6px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; font-size:12px;">q Value</td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">1</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">2</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">4</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">5</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">3</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">6</strong></td><td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;"><strong style="color:#1e40af;">7</strong></td></tr>
    </table>
    <div style="display:flex; justify-content:space-around; font-size:12.5px; color:#1e293b; background:#ffffff; padding:8px; border-radius:6px; border:1px solid #e2e8f0; flex-wrap:wrap; gap:10px;">
      <div>• <strong>front</strong> = <span style="color:#dc2626; font-weight:bold;">0</span> (สูตร: <code>(front+1)%7</code>)</div>
      <div>• <strong>back</strong> = <span style="color:#16a34a; font-weight:bold;">6</span> (สูตร: <code>(back+1)%7</code>)</div>
      <div>• <strong>currentSize</strong> = <span style="color:#2563eb; font-weight:bold;">0</span> (Empty)</div>
    </div>
    <div style="margin-top:10px; font-size:12.5px; background:#eff6ff; padding:10px; border-radius:6px; border:1px solid #bfdbfe; line-height:1.7;">
      <div><strong>6.1 Shortest Path จาก 1 ไปยัง 5:</strong> ความยาวเส้นทาง = <strong style="color:#1d4ed8;">2 edges</strong>, ลำดับคือ <strong style="color:#1d4ed8;">1, 2, 5</strong> (หรือ <strong style="color:#1d4ed8;">1, 4, 5</strong>)</div>
      <div><strong>6.2 Shortest Path จาก 1 ไปยัง 7:</strong> ความยาวเส้นทาง = <strong style="color:#1d4ed8;">2 edges</strong>, ลำดับคือ <strong style="color:#1d4ed8;">1, 4, 7</strong></div>
      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ความยาวเส้นทางนับจำนวน Edge (2 เส้น) และลำดับต้องคั่นด้วย <code>,</code> ห้ามเขียนลูกศร <code>-&gt;</code> หากเขียนลูกศรจะได้ 0 คะแนน</div>
    </div>
  </div>
</div>

    <p><strong>2. ผังจำลอง Circular Queue เมื่อจบขั้นตอน:</strong></p>
    <div style="max-width:560px; margin:14px 0;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="270" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
  <defs>
    <marker id="arrow-front" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#dc2626"/>
    </marker>
    <marker id="arrow-back" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#16a34a"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <text x="240" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">สถานะ Circular Queue เมื่อจบขั้นตอน Shortest Path (front=0, back=6)</text>
  <rect x="55" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="79" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[0]</text>
  <text x="79" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">1</text>
  <line x1="79" y1="139" x2="79" y2="110" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-front)"/>
  <text x="79" y="153" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="11" font-weight="bold" fill="#dc2626">front=0</text>
  <rect x="103" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="127" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[1]</text>
  <text x="127" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">2</text>
  <rect x="151" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="175" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[2]</text>
  <text x="175" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">4</text>
  <rect x="199" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="223" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[3]</text>
  <text x="223" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">5</text>
  <rect x="247" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="271" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[4]</text>
  <text x="271" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">3</text>
  <rect x="295" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="319" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[5]</text>
  <text x="319" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">6</text>
  <rect x="343" y="65" width="48" height="42" fill="#eff6ff" stroke="#475569" stroke-width="1.8"/>
  <text x="367" y="57" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[6]</text>
  <text x="367" y="91" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">7</text>
  <line x1="367" y1="175" x2="367" y2="110" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow-back)"/>
  <text x="367" y="189" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="11" font-weight="bold" fill="#16a34a">back=6</text>
  <rect x="416" y="50" width="160" height="185" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" rx="6"/>
  <text x="428" y="72" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">สถานะพอยน์เตอร์จบลูป:</text>
  <text x="428" y="96" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#dc2626">front</tspan> = 0</text>
  <text x="428" y="118" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#16a34a">back</tspan> = 6</text>
  <text x="428" y="140" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#2563eb">currentSize</tspan> = 0</text>
  <line x1="426" y1="152" x2="566" y2="152" stroke="#e2e8f0" stroke-width="1"/>
  <text x="428" y="172" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" fill="#64748b">สูตร Enqueue:</text>
  <text x="428" y="188" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-family="Consolas" fill="#0f172a">back = (back+1)%7</text>
  <text x="428" y="208" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" fill="#64748b">สูตร Dequeue:</text>
  <text x="428" y="224" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-family="Consolas" fill="#0f172a">front = (front+1)%7</text>
</svg>
    </div>

    <p><strong>3. คำตอบเส้นทางและระยะทาง (Strict Comma Notation):</strong></p>
    <ul>
      <li><strong>Shortest Path to Vertex 5:</strong> <strong style="color:#1e40af; font-size:16px;">1, 2, 5</strong> (หรือ <code>1, 4, 5</code>) &mdash; ความยาว (Length) = <strong>2</strong> (หรือ 2 เส้น)</li>
      <li><strong>Shortest Path to Vertex 7:</strong> <strong style="color:#1e40af; font-size:16px;">1, 4, 7</strong> &mdash; ความยาว (Length) = <strong>2</strong> (หรือ 2 เส้น)</li>
    </ul>

    <div class="alert-box">
      <strong>🚨 กับดักได้ 0 คะแนนขั้นวิกฤต (Zero-Mark Arrow Trap):</strong><br>
      อ.ประดิษฐ์ สั่งเน้นย้ำหลายรอบว่า <strong>ห้ามเขียนลูกศรเด็ดขาด!</strong> (เช่น ห้ามเขียน <code>1 -&gt; 4 -&gt; 5</code>) ใครเขียนลูกศรจะถูกปรับ <strong>0 คะแนนทันทีทั้งข้อ</strong>!<br>
      ต้องเขียนเป็นลำดับคั่นด้วยเครื่องหมายจุลภาคเท่านั้น เช่น <strong><code>1, 4, 5</code></strong><br>
      และหน่วยของความยาวตอบเป็นจำนวน <strong>"เส้น" (Edges)</strong> ห้ามตอบหน่วยนิ้วหรือเซนติเมตร
    </div>
  </div>

  <!-- QUESTION 7 -->
    <!-- SUB-QUESTION 6.2: WORKSHEET SOURCE VERTEX V3 -->
  <h3 class="question-title" style="background:#f0fdfa; border-left-color:#0d9488; margin-top:25px;">
    <span>6.2 การประมวลผล Shortest Path โดยมีจุดเริ่มต้นที่ $v_3$ (Source Vertex = 3) [ถอดรหัสจากใบงานจริง 2569 ภาพที่ 3]</span>
    <span class="score-badge" style="background:#ccfbf1; color:#0f766e;">Score: 10 Marks (10 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the same directed graph $G = (V, E)$ with 7 vertices. Now set the <strong>Source Vertex to $v_3$</strong> (Vertex 3). Execute the Breadth-First Search (BFS) Unweighted Shortest Path algorithm using the pseudo-code:</p>
  <pre><code>if w.dist == INFINITY :
    w.dist = v.dist + 1
    w.path = v
    q.enqueue (w)</code></pre>
  <p>Fill the processing table (Known, Dist, Path) and the Queue states. Then answer the exact questions from the worksheet:</p>
  <ul>
    <li>Write down the length and the shortest path from Vertex 3 to Vertex 5: <code>The length = ? The shortest path = ?</code></li>
    <li>Write down the length and the shortest path from Vertex 3 to Vertex 7: <code>The length = ? The shortest path = ?</code></li>
    <li>Write down the length and the shortest path from Vertex 4 to Vertex 5: <code>The length = ? The shortest path = ?</code></li>
  </ul>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - จากใบงานจริงในห้องเรียน 2569 ภาพที่ 3):</strong> กำหนดกราฟเดิม 7 โหนด แต่เปลี่ยน <strong>จุดเริ่มต้น (Source Vertex) เป็นโหนด $v_3$</strong> ให้นักศึกษาเติมตารางประมวลผล Shortest Path (Known, Dist, Path) และ Queue ให้สมบูรณ์ จากนั้นตอบคำถาม 3 ข้อย่อย:<br>
    1. จงหาเส้นทางที่สั้นที่สุดจาก $v_3$ ไป $v_5$ จากตารางที่คำนวณได้ และความยาวของเส้นทางนั้นเท่ากับเท่าไร?<br>
    2. จงหาเส้นทางที่สั้นที่สุดจาก $v_3$ ไป $v_7$ จากตารางที่คำนวณได้ และความยาวของเส้นทางนั้นเท่ากับเท่าไร?<br>
    3. เส้นทางที่สั้นที่สุดจาก $v_4$ ไป $v_5$ มีความยาวและเส้นทางคืออะไร?
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#0f766e; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 6.2: ตารางประมวลผล Shortest Path (Source = 3)</div>
    <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
      <div style="flex:2; min-width:280px;">
        <table style="text-align:center; font-size:12.5px;">
          <thead>
            <tr style="background:#0f766e; color:white;">
              <th>Vertex</th><th>Known</th><th>Dist ($d_v$)</th><th>Path ($p_v$)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>$v_1$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_2$</td><td></td><td></td><td></td></tr>
            <tr><td style="font-weight:bold; background:#f0fdfa;">$v_3$ (Src)</td><td></td><td></td><td></td></tr>
            <tr><td>$v_4$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_5$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_6$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_7$</td><td></td><td></td><td></td></tr>
          </tbody>
        </table>
      </div>
      <div style="flex:1; min-width:140px; max-width:180px;">
        <div style="font-size:12px; font-weight:bold; text-align:center; color:#0f766e; margin-bottom:4px;">Queue (q)</div>
        <table style="text-align:center; font-size:12px;">
          <tr style="background:#0f766e; color:white;"><th>Slot</th><th>Vertex</th></tr>
          <tr><td>[6]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[4]</td><td></td></tr>
          <tr><td>[3]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[1]</td><td></td></tr><tr><td>[0]</td><td></td></tr>
        </table>
        <div style="font-size:11px; margin-top:4px; text-align:center;">front = ? &nbsp; back = ?</div>
      </div>
    </div>

    <div style="margin-top:12px; font-size:13.5px; line-height:2; background:#f8fafc; padding:12px; border-radius:6px; border:1px solid #cbd5e1;">
      <div>• <strong>จาก $v_3$ ไป $v_5$:</strong> The length = ............ The shortest path = ............................................................</div>
      <div>• <strong>จาก $v_3$ ไป $v_7$:</strong> The length = ............ The shortest path = ............................................................</div>
      <div>• <strong>จาก $v_4$ ไป $v_5$:</strong> The length = ............ The shortest path = ............................................................</div>
    </div>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดข้อ 6.2 (Shortest Path from Source Vertex 3 Solution):</div>
    <p><strong>1. ลำดับการประมวลผล BFS และการอัปเดตตาราง:</strong></p>
    <ul>
      <li><strong>เริ่มต้น (Init):</strong> $v_3$ เป็น Source &rarr; $d(v_3) = \mathbf{0}, p(v_3) = \mathbf{0}$, โหนดอื่นๆ มี $d = \infty, p = 0$ ทั้งหมด &rarr; <code>q.enqueue(3)</code></li>
      <li><strong>รอบที่ 1 (Dequeue 3):</strong> Known[3] = True &rarr; โหนดติดกันของ 3 คือ <strong>1 และ 6</strong><br>
        • โหนด 1: $d(1) = \infty \implies d(1) = 0 + 1 = \mathbf{1}, p(1) = \mathbf{3}$ &rarr; <code>q.enqueue(1)</code><br>
        • โหนด 6: $d(6) = \infty \implies d(6) = 0 + 1 = \mathbf{1}, p(6) = \mathbf{3}$ &rarr; <code>q.enqueue(6)</code>
      </li>
      <li><strong>รอบที่ 2 (Dequeue 1):</strong> Known[1] = True &rarr; โหนดติดกันของ 1 คือ <strong>2 และ 4</strong><br>
        • โหนด 2: $d(2) = \infty \implies d(2) = 1 + 1 = \mathbf{2}, p(2) = \mathbf{1}$ &rarr; <code>q.enqueue(2)</code><br>
        • โหนด 4: $d(4) = \infty \implies d(4) = 1 + 1 = \mathbf{2}, p(4) = \mathbf{1}$ &rarr; <code>q.enqueue(4)</code>
      </li>
      <li><strong>รอบที่ 3 (Dequeue 6):</strong> Known[6] = True &rarr; โหนด 6 ไม่มีเส้นทางออก (Sink)</li>
      <li><strong>รอบที่ 4 (Dequeue 2):</strong> Known[2] = True &rarr; โหนดติดกันของ 2 คือ <strong>4 และ 5</strong><br>
        • โหนด 4: $d(4) = 2 \neq \infty$ (ไม่ทำอะไร)<br>
        • โหนด 5: $d(5) = \infty \implies d(5) = 2 + 1 = \mathbf{3}, p(5) = \mathbf{2}$ &rarr; <code>q.enqueue(5)</code>
      </li>
      <li><strong>รอบที่ 5 (Dequeue 4):</strong> Known[4] = True &rarr; โหนดติดกันของ 4 คือ <strong>3, 6, 5, 7</strong><br>
        • โหนด 3, 6, 5: มีค่า dist ไม่เป็น $\infty$ แล้ว<br>
        • โหนด 7: $d(7) = \infty \implies d(7) = 2 + 1 = \mathbf{3}, p(7) = \mathbf{4}$ &rarr; <code>q.enqueue(7)</code>
      </li>
      <li><strong>รอบที่ 6 (Dequeue 5):</strong> Known[5] = True &rarr; โหนดติดกันคือ 7 ($d(7)=3$ แล้ว ไม่ทำอะไร)</li>
      <li><strong>รอบที่ 7 (Dequeue 7):</strong> Known[7] = True &rarr; โหนดติดกันคือ 6 ($d(6)=1$ แล้ว ไม่ทำอะไร)</li>
    </ul>

    <p><strong>ตารางผลลัพธ์สุทธิ Shortest Path Table (Source = 3):</strong></p>
    <table style="text-align:center; font-size:13px;">
      <tr style="background:#0f766e; color:white;">
        <th>Vertex ($v$)</th><th>Known</th><th>Dist ($d_v$)</th><th>Path ($p_v$)</th><th>Shortest Path จาก $v_3$</th><th>ความยาว (Length)</th>
      </tr>
      <tr><td>$v_1$</td><td>T (1)</td><td>1</td><td>3</td><td><strong>$v_3, v_1$</strong></td><td>1 edge</td></tr>
      <tr><td>$v_2$</td><td>T (1)</td><td>2</td><td>1</td><td><strong>$v_3, v_1, v_2$</strong></td><td>2 edges</td></tr>
      <tr><td style="background:#f0fdfa; font-weight:bold;">$v_3$ (Src)</td><td>T (1)</td><td>0</td><td>0</td><td><strong>$v_3$</strong></td><td>0</td></tr>
      <tr><td>$v_4$</td><td>T (1)</td><td>2</td><td>1</td><td><strong>$v_3, v_1, v_4$</strong></td><td>2 edges</td></tr>
      <tr><td style="background:#fef9c3; font-weight:bold;">$v_5$</td><td>T (1)</td><td>3</td><td>2</td><td><strong>$v_3, v_1, v_2, v_5$</strong></td><td><strong>3 edges</strong></td></tr>
      <tr><td>$v_6$</td><td>T (1)</td><td>1</td><td>3</td><td><strong>$v_3, v_6$</strong></td><td>1 edge</td></tr>
      <tr><td style="background:#fef9c3; font-weight:bold;">$v_7$</td><td>T (1)</td><td>3</td><td>4</td><td><strong>$v_3, v_1, v_4, v_7$</strong></td><td><strong>3 edges</strong></td></tr>
    </table>

    <p><strong>2. คำตอบตรงตามคำถามในใบงานจริง (Image 3 Answers):</strong></p>
    <ul style="line-height:1.8;">
      <li><strong>ตอบคำถาม 1:</strong> The length of the shortest path from Vertex 3 to Vertex 5 = <strong>3</strong><br>
        The shortest path from Vertex 3 to Vertex 5 = <strong>$v_3, v_1, v_2, v_5$</strong> (ย้อนรอยจาก $v_5 \leftarrow p(5)=2 \leftarrow p(2)=1 \leftarrow p(1)=3$)
      </li>
      <li><strong>ตอบคำถาม 2:</strong> The length of the shortest path from Vertex 3 to Vertex 7 = <strong>3</strong><br>
        The shortest path from Vertex 3 to Vertex 7 = <strong>$v_3, v_1, v_4, v_7$</strong> (ย้อนรอยจาก $v_7 \leftarrow p(7)=4 \leftarrow p(4)=1 \leftarrow p(1)=3$)
      </li>
      <li><strong>ตอบคำถาม 3 (v4 ไป v5):</strong> จาก Adjacency List มีเส้นเชื่อมตรงจากโหนด 4 ไปโหนด 5<br>
        The length of shortest path from Vertex 4 to Vertex 5 = <strong>1</strong> | The shortest path = <strong>$v_4, v_5$</strong>
      </li>
    </ul>
  </div>


  <h2 id="q7" class="part-title">Question 7: Properties &amp; Theory Calculations (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิง: Weiss Chapters 4, 5, 6, 7, 9 / สไลด์สรุปเนื้อหา อ.ประดิษฐ์</div>

  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำเตือนอาจารย์ผู้สอนในห้องเรียน (จุดดัก 0 คะแนนข้อความบน Notepad):</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      • <strong>2 Properties vs 3 Properties:</strong> มี 2 คุณสมบัติคือ <strong>Binary Heap</strong> (Structure Property + Heap-Order Property), มี 3 คุณสมบัติคือ <strong>AVL Tree</strong> (BST Property + Height-Balanced Property + Node Structure)<br>
      • <strong>Complete Graph Edges:</strong> $E = \frac{V(V-1)}{2}$ เช่น $V=10 \implies 45$ เส้น <em>ห้ามตอบติดสูตร เช่น <code>10*(10-1)/2</code> หรือ <code>90/2</code> โดนหักเหลือ 0 คะแนนทันที ต้องกดเครื่องคิดเลขตอบตัวเลข 45</em><br>
      • <strong>Complete Binary Tree Nodes:</strong> ที่ความสูง $H=10$ โหนดต่ำสุด $= 1,024$ โหนดสูงสุด $= 2,047$ <em>ห้ามตอบเป็นเลขยกกำลัง $2^{10}$ หรือ $2^{11}-1$ เด็ดขาด โดน 0 ทันที</em>
    </p>
  </div>

  <h3 class="question-title">
    <span>7.1 Data Structure Properties, Ideal Hash, Memory Waste &amp; Tree Formulas</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Answer the following sub-questions thoroughly:</p>
  <ol>
    <li>Which data structures are governed by <strong>2 properties</strong>? Which are governed by <strong>3 properties</strong>? State each property clearly.</li>
    <li>State 3 ideal theoretical properties of Hash Functions. Which one is impossible in practice, and why (2 reasons)?</li>
    <li>In a directed graph with $|V| = 7$ vertices and $|E| = 12$ edges stored as a $7 \times 7$ Adjacency Matrix:
      <ul>
        <li>What percentage of memory entries are actively used (contain 1)?</li>
        <li>What percentage of memory entries are wasted (contain 0)?</li>
      </ul>
    </li>
    <li>How many edges are in a Complete Graph $K_{16}$? (Calculate as an exact integer).</li>
    <li>A Complete Binary Tree has height $H = 10$. What are the minimum and maximum possible number of nodes?</li>
    <li>State the 1-based array formulas for finding the Parent, Left Child, and Right Child of node at index $i$ in a Binary Heap.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> ตอบคำถามเชิงทฤษฎีและการคำนวณ: โครงสร้างใดมี 2 คุณสมบัติ/3 คุณสมบัติ, คุณสมบัติในอุดมคติของ Hash Function, เปอร์เซ็นต์ความสูญเสียในหน่วยความจำของ Adjacency Matrix, จำนวนเส้นใน Complete Graph $K_{16}$, จำนวนโหนดต่ำสุดและสูงสุดของ Complete Binary Tree สูง 10, และสูตร Parent/Left/Right Child ในอาร์เรย์ฮีป
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <ol>
      <li><strong>โครงสร้างข้อมูลที่มี 2 คุณสมบัติ:</strong><br>
        • <strong>Binary Min-Heap:</strong> (1) Structure Property (Complete Binary Tree), (2) Heap-Order Property (Parent &le; Children)<br>
        • <strong>AVL Tree:</strong> (1) Binary Search Tree Property, (2) Balance Property ($|h_L - h_R| \le 1$)<br>
        <strong>โครงสร้างข้อมูลที่มี 3 คุณสมบัติ:</strong><br>
        • <strong>Hashing:</strong> (1) Deterministic, (2) Uniform Distribution, (3) Fast Computation / Range Matching
      </li>
      <li><strong>คุณสมบัติในอุดมคติของ Hash Function 3 ข้อ:</strong><br>
        1. คำนวณง่ายและรวดเร็ว ($O(1)$)<br>
        2. กระจายคีย์ได้สม่ำเสมอทั่วทุกช่องในตาราง (Uniform Distribution)<br>
        3. คีย์ที่ต่างกันต้องได้ค่าดัชนีต่างกัน (One-to-One Mapping หรือ Perfect Hashing)<br>
        <strong>ข้อที่เป็นไปไม่ได้ในทางปฏิบัติ:</strong> <strong>ข้อ 3 (One-to-One Mapping)</strong><br>
        <em>สาเหตุ 2 ประการ:</em><br>
        (1) ขนาดของ Key Space มีค่าเป็นอนันต์หรือใหญ่กว่าขนาด TableSize มาก ($|K| \gg \text{TableSize}$)<br>
        (2) กฎช่องนกพิราบ (Pigeonhole Principle): เมื่อจำนวนคีย์มากกว่าจำนวนช่อง ย่อมเกิด Collision อย่างหลีกเลี่ยงไม่ได้
      </li>
      <li><strong>การคำนวณร้อยละความสูญเสียใน RAM (Adjacency Matrix $7 \times 7$):</strong><br>
        • พื้นที่ทั้งหมดในตาราง: $7 \times 7 = \mathbf{49 \text{ ช่อง}}$<br>
        • ช่องที่เป็น 1 (Used): $\frac{12}{49} \times 100 \approx \mathbf{24.48\%}$<br>
        • ช่องที่เป็น 0 (Wasted): $\frac{37}{49} \times 100 \approx \mathbf{75.52\%}$ (สูญเปล่าในหน่วยความจำ)
      </li>
      <li><strong>จำนวนเส้นเชื่อมใน Complete Graph $K_{16}$:</strong><br>
        $$\text{Edges} = \frac{N(N-1)}{2} = \frac{16 \times 15}{2} = \frac{240}{2} = \mathbf{120 \text{ เส้น}}$$
      </li>
      <li><strong>จำนวนโหนดของ Complete Binary Tree สูง $H = 10$:</strong><br>
        • น้อยที่สุด (Minimum Nodes): $2^H = 2^{10} = \mathbf{1,024 \text{ โหนด}}$ (หรือ $H+1 = 11$ หากเป็นโหนดแบบ Binary Tree ทั่วไป)<br>
        • มากที่สุด (Maximum Nodes): $2^{H+1} - 1 = 2^{11} - 1 = 2,048 - 1 = \mathbf{2,047 \text{ โหนด}}$
      </li>
      <li><strong>สูตรการคำนวณตำแหน่งใน 1-Based Array Binary Heap:</strong><br>
        • $\text{Parent}(i) = \lfloor i / 2 \rfloor$ (หรือ <code>i // 2</code> ใน Python)<br>
        • $\text{Left Child}(i) = 2 \times i$<br>
        • $\text{Right Child}(i) = 2 \times i + 1$
      </li>
    </ol>
  </div>

  <!-- ========================================================================= -->
  <!-- PART 2: INTERVIEW & WHITEBOARD SECRETS                                    -->
  
  </div> <!-- END TAB 1 -->
"""
