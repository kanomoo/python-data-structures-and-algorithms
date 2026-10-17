# -*- coding: utf-8 -*-
"""
Module to generate HTML for Tab 0:
🎯 ชุดที่ 0: ข้อสอบเก็งตรงคำพูดอาจารย์ตั้งแต่วันแรกถึงวันสุดท้าย (Teacher's Spoken Words & Final Day Leaks - 7 ข้อ 70 คะแนน)
Anchored primarily on the final review lecture (Wednesday 7 October 2569) where Dr. Pradit opened Notepad at 11:54 AM.
Strictly separates:
1. Formal English Exam Statement + Exact Thai Translation + Teacher Spoken Warnings
2. Simulated Blank Answer Sheets / Empty Tables (NO SPOILERS)
3. Complete Step-by-Step Solutions in collapsible Solution Boxes
"""

def get_tab_set0_html():
    return r"""  <!-- ========================================================================= -->
  <!-- TAB 0: TEACHER'S SPOKEN WORDS & FINAL DAY LEAKS SUITE (ชุดที่ 0)           -->
  <!-- ========================================================================= -->
  <div id="tab-set0" class="tab-content active">
    <h1 class="section-heading" style="background: linear-gradient(135deg, #1e1b4b, #312e81); border-left: 6px solid #6366f1;">
      🎯 ชุดที่ 0: ข้อสอบเก็งตรงคำพูดอาจารย์ตั้งแต่วันแรกถึงวันสุดท้าย (Teacher's Spoken Words &amp; Final Day Leaks - 7 ข้อ 70 คะแนน)
    </h1>

    <!-- OFFICIAL EXAM RULES ANNOUNCED ON FINAL DAY -->
    <div class="rules-box" style="background:#eef2ff; border-left-color:#4f46e5; border-radius:0 10px 10px 0; margin-bottom:20px;">
      <div class="rules-title" style="color:#3730a3; font-size:15.5px; display:flex; align-items:center; gap:8px;">
        <span>🎙️</span> บันทึกคำพูดอาจารย์ ดร.ประดิษฐ์ พิทักษ์เสถียรกุล พิมพ์บน Notepad หน้าห้องเรียนวันสุดท้าย (7 ต.ค. 2569 เวลา 11:54 น.):
      </div>
      <div style="font-family:'JetBrains Mono', Consolas, monospace; background:#ffffff; border:1px solid #c7d2fe; padding:12px 16px; border-radius:6px; font-size:13px; color:#1e1b4b; line-height:1.6; margin-top:8px;">
        <strong>"แนวทางข้อสอบปลายภาค คะแนนในข้อสอบ 70 คะแนน หาร 2 เหลือ 35 คะแนน<br>
        เปิดตำรา ใช้เครื่องคิดเลขได้ ห้ามใช้โทรศัพท์มือถือทุกกรณี<br>
        1. Hashing<br>
        2. binary heap<br>
        3. insertion sort<br>
        4. selection sort/bubble sort<br>
        5. topological sort<br>
        6. unweighted shortest path<br>
        7. คำถามย่อยๆ หลายข้อ เช่น properties (โครงสร้างอะไรเอ่ยที่มี 2, 3 three properties two properties)<br>
        &nbsp;&nbsp;&nbsp;พวกที่มีการคำนวณใช้สูตรเปอร์เซนต์ what percentage of เป็นต้น how many"</strong>
      </div>
      <p style="margin:8px 0 0 0; font-size:13px; color:#4338ca;">
        ⚡ <em>คำแนะนำ: ชุดนี้จัดทำเป็นข้อสอบจริงแบบ "ไม่มีการเฉลยในตัวโจทย์" มีช่องตารางเปล่าจำลองกระดาษคำตอบให้ฝึกเขียนจริง และมีเฉลยละเอียดซ่อนอยู่ด้านล่างของแต่ละข้อ สามารถคลิกปุ่ม <strong>"👁️ ซ่อน/แสดงเฉลยทั้งหมด"</strong> เพื่อฝึกจับเวลาทำข้อสอบได้เสมือนจริง</em>
      </p>
    </div>

    <!-- QUICK NAV FOR TAB 0 -->
    <div class="nav-jump-bar" style="background:#e0e7ff;">
      <span class="nav-jump-label" style="color:#3730a3;">⚡ ทางลัดข้อสอบชุดที่ 0:</span>
      <a href="#set0-q1" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 1 Hashing</a>
      <a href="#set0-q2" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 2 Binary Heap (4 ตาราง)</a>
      <a href="#set0-q3" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 3 Insertion Sort</a>
      <a href="#set0-q4" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 4 Selection / Bubble Sort</a>
      <a href="#set0-q5" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 5 Topological Sort</a>
      <a href="#set0-q6" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 6 Shortest Path (Assignment 4)</a>
      <a href="#set0-q7" class="jump-pill" style="border-color:#6366f1; color:#4338ca;">ข้อ 7 คำถามย่อย Properties &amp; %</a>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 1: HASHING (EXACT REAL EXAM: TABLESIZE = 19, DOUBLE HASHING)    -->
    <!-- ========================================================================= -->
    <h2 id="set0-q1" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      ข้อ 1. Hashing &amp; Open Addressing (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: ข้อสอบปลายภาคจริง อ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล / โครงสร้างข้อมูลภาษา Python</div>

    <!-- PURE EXAM QUESTION STATEMENT (NO SPOILERS) -->
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-left:4px solid #4f46e5; border-radius:0 8px 8px 0; padding:16px 20px; margin:14px 0; font-size:15px; color:#1e293b; line-height:1.8;">
      <p style="margin:0 0 8px 0;">
        <strong>1. โครงสร้าง Hash Table ชนิด Open Addressing กำหนดวิธีการแก้การชนกันเป็นแบบ Double Hashing กำหนด TableSize ให้เป็น 19</strong><br>
        % ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่มากกว่า 75%
      </p>
      <p style="margin:0;">
        <strong>1.1 ให้นักศึกษาทำการ insert ข้อมูลจำนวน 8 ตัว ดังต่อไปนี้ เข้าไปใน HashTable ดังกล่าว โดยใช้วิธีการแก้การชนกันแบบ Double Hashing</strong><br>
        กำหนด $$f(i) = i \times (R - (X \bmod R))$$
        $$\mathbf{323, 17, 969, 868, 340, 370, 357, 391} \quad \text{รวม insert ทุกตัวเสร็จสิ้น [10 คะแนน]}$$
      </p>
    </div>

    <!-- BLANK SHEET FOR QUESTION 1 -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 1.1: ตารางแฮชขนาด 19 ช่อง (Hash Table Array ในภาษา Python)
      </div>
      <div style="overflow-x:auto;">
        <table style="width:100%; min-width:860px; border-collapse:collapse; text-align:center; font-size:12px; border:2px solid #334155;">
          <thead>
            <tr style="background:#1e293b; color:#ffffff;">
              <th style="padding:6px; border:1px solid #475569; width:75px;">Index</th>
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
              <th style="padding:6px; border:1px solid #475569;">[10]</th>
              <th style="padding:6px; border:1px solid #475569;">[11]</th>
              <th style="padding:6px; border:1px solid #475569;">[12]</th>
              <th style="padding:6px; border:1px solid #475569;">[13]</th>
              <th style="padding:6px; border:1px solid #475569;">[14]</th>
              <th style="padding:6px; border:1px solid #475569;">[15]</th>
              <th style="padding:6px; border:1px solid #475569;">[16]</th>
              <th style="padding:6px; border:1px solid #475569;">[17]</th>
              <th style="padding:6px; border:1px solid #475569;">[18]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding:10px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1;">Value</td>
              <td style="padding:10px 2px; border:1px solid #cbd5e1; height:36px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div style="margin-top:14px; font-size:13.5px; line-height:2.2; color:#1e293b;">
        <strong>พื้นที่คำนวณแสดงวิธีทำ / จำนวนการชนของแต่ละคีย์:</strong><br>
        • Key 323: .................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 17: ...................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 969: .................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 868: .................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 340: .................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 370: .................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 357: .................................................................................................... (ชน ............ ครั้ง)<br>
        • Key 391: .................................................................................................... (ชน ............ ครั้ง)<br>
        <strong>การชนรวมทั้งสิ้น:</strong> ............ ครั้ง
      </div>

      <div style="margin-top:12px; padding-top:10px; border-top:1px dashed #cbd5e1; font-size:13.5px; line-height:2.2; color:#1e293b;">
        <strong>1.2 คำถาม Rehashing (จากโจทย์ด้านบน):</strong><br>
        1) % ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่มากกว่า 75% ของขนาดตาราง 19 ช่อง คิดเป็นจำนวนข้อมูลกี่ตัว?<br>
        ตอบ: ต้องมีข้อมูลอย่างน้อย ............ ตัว (หากใส่ครบ 8 ตัวแล้ว จะต้องใส่เพิ่มอีก ............ ตัว จึงจะเกิด Rehashing)<br>
        2) ขนาดของตารางใหม่ (New TableSize) ในการ Rehash ต้องเลือกขนาดเท่าใด? (ตอบตัวเลขเต็ม)<br>
        ตอบ: New TableSize = ............
      </div>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 1 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดและหลักการคิดข้อ 1 (Double Hashing &amp; Rehashing Solution):</div>
      <p><strong>1. การหาค่าคงที่ $R$ และฟังก์ชันแฮชหลัก:</strong></p>
      <ul>
        <li><strong>การเลือกค่า $R$:</strong> ตามนิยาม Double Hashing ค่า $R$ ต้องเป็น <em>"จำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize ($R &lt; \text{TableSize}$)"</em><br>
          ตารางมีขนาด $\text{TableSize} = 19$ จำนวนเฉพาะที่น้อยกว่า 19 ได้แก่ $2, 3, 5, 7, 11, 13, 17$ &rarr; จึงได้ <strong style="color:#15803d;">$R = 17$</strong><br>
          <em>(⚠️ คำเตือนอาจารย์: ห้ามเลือก $R = 19$ เด็ดขาด เพราะ $R$ ต้องน้อยกว่า TableSize)</em>
        </li>
        <li><strong>ฟังก์ชันแฮชหลัก:</strong> $h_0(X) = X \bmod 19$</li>
        <li><strong>ฟังก์ชันคำนวณก้าว (Step Size):</strong> $\text{step}(X) = 17 - (X \bmod 17)$</li>
        <li><strong>ลำดับการตรวจสอบตำแหน่ง:</strong> $h_i(X) = (h_0(X) + i \times \text{step}(X)) \bmod 19$</li>
      </ul>

      <p><strong>2. ขั้นตอนการคำนวณและลำดับการชนทีละคีย์ (ตรงตามลายมือรุ่นพี่ในกระดาษข้อสอบ):</strong></p>
      <ul>
        <li><strong>Key 323:</strong>
          <ul>
            <li>$h_0(323) = 323 \bmod 19 = \mathbf{0}$ &rarr; ช่อง 0 ว่าง &rarr; ลง <strong>ช่อง 0</strong> (<strong style="color:#15803d;">ชน 0 ครั้ง</strong>)</li>
          </ul>
        </li>
        <li><strong>Key 17:</strong>
          <ul>
            <li>$h_0(17) = 17 \bmod 19 = \mathbf{17}$ &rarr; ช่อง 17 ว่าง &rarr; ลง <strong>ช่อง 17</strong> (<strong style="color:#15803d;">ชน 0 ครั้ง</strong>)</li>
          </ul>
        </li>
        <li><strong>Key 969:</strong>
          <ul>
            <li>$h_0(969) = 969 \bmod 19 = \mathbf{0}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 323 ที่ช่อง 0! (ชนครั้งที่ 1)</span></li>
            <li>คำนวณก้าว: $\text{step} = 17 - (969 \bmod 17) = 17 - 0 = \mathbf{17}$</li>
            <li>$i=1: (0 + 1 \times 17) \bmod 19 = \mathbf{17}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 17 ที่ช่อง 17! (ชนครั้งที่ 2)</span></li>
            <li>$i=2: (0 + 2 \times 17) \bmod 19 = 34 \bmod 19 = \mathbf{15}$ &rarr; ช่อง 15 ว่าง &rarr; ลง <strong>ช่อง 15</strong> (<strong style="color:#dc2626;">ชน 2 ครั้ง</strong>) *(ตรงกับเลข 2 เหนือ 969 ในลายมือรุ่นพี่)*</li>
          </ul>
        </li>
        <li><strong>Key 868:</strong>
          <ul>
            <li>$h_0(868) = 868 \bmod 19 = \mathbf{13}$ &rarr; ช่อง 13 ว่าง &rarr; ลง <strong>ช่อง 13</strong> (<strong style="color:#15803d;">ชน 0 ครั้ง</strong>)</li>
          </ul>
        </li>
        <li><strong>Key 340:</strong>
          <ul>
            <li>$h_0(340) = 340 \bmod 19 = \mathbf{17}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 17 ที่ช่อง 17! (ชนครั้งที่ 1)</span></li>
            <li>คำนวณก้าว: $\text{step} = 17 - (340 \bmod 17) = 17 - 0 = \mathbf{17}$</li>
            <li>$i=1: (17 + 1 \times 17) \bmod 19 = 34 \bmod 19 = \mathbf{15}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 969 ที่ช่อง 15! (ชนครั้งที่ 2)</span></li>
            <li>$i=2: (17 + 2 \times 17) \bmod 19 = 51 \bmod 19 = \mathbf{13}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 868 ที่ช่อง 13! (ชนครั้งที่ 3)</span></li>
            <li>$i=3: (17 + 3 \times 17) \bmod 19 = 68 \bmod 19 = \mathbf{11}$ &rarr; ช่อง 11 ว่าง &rarr; ลง <strong>ช่อง 11</strong> (<strong style="color:#dc2626;">ชน 3 ครั้ง</strong>) *(ตรงกับเลข 3 เหนือ 340 ในลายมือรุ่นพี่)*</li>
          </ul>
        </li>
        <li><strong>Key 370:</strong>
          <ul>
            <li>$h_0(370) = 370 \bmod 19 = \mathbf{9}$ &rarr; ช่อง 9 ว่าง &rarr; ลง <strong>ช่อง 9</strong> (<strong style="color:#15803d;">ชน 0 ครั้ง</strong>)</li>
          </ul>
        </li>
        <li><strong>Key 357:</strong>
          <ul>
            <li>$h_0(357) = 357 \bmod 19 = \mathbf{15}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 969 ที่ช่อง 15! (ชนครั้งที่ 1)</span></li>
            <li>คำนวณก้าว: $\text{step} = 17 - (357 \bmod 17) = 17 - 0 = \mathbf{17}$</li>
            <li>$i=1: (15 + 1 \times 17) \bmod 19 = 32 \bmod 19 = \mathbf{13}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 868 ที่ช่อง 13! (ชนครั้งที่ 2)</span></li>
            <li>$i=2: (15 + 2 \times 17) \bmod 19 = 49 \bmod 19 = \mathbf{11}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 340 ที่ช่อง 11! (ชนครั้งที่ 3)</span></li>
            <li>$i=3: (15 + 3 \times 17) \bmod 19 = 66 \bmod 19 = \mathbf{9}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 370 ที่ช่อง 9! (ชนครั้งที่ 4)</span></li>
            <li>$i=4: (15 + 4 \times 17) \bmod 19 = 83 \bmod 19 = \mathbf{7}$ &rarr; ช่อง 7 ว่าง &rarr; ลง <strong>ช่อง 7</strong> (<strong style="color:#dc2626;">ชน 4 ครั้ง</strong>) *(ตรงกับเลข 4 เหนือ 357 ในลายมือรุ่นพี่)*</li>
          </ul>
        </li>
        <li><strong>Key 391:</strong>
          <ul>
            <li>$h_0(391) = 391 \bmod 19 = \mathbf{11}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 340 ที่ช่อง 11! (ชนครั้งที่ 1)</span></li>
            <li>คำนวณก้าว: $\text{step} = 17 - (391 \bmod 17) = 17 - 0 = \mathbf{17}$</li>
            <li>$i=1: (11 + 1 \times 17) \bmod 19 = 28 \bmod 19 = \mathbf{9}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 370 ที่ช่อง 9! (ชนครั้งที่ 2)</span></li>
            <li>$i=2: (11 + 2 \times 17) \bmod 19 = 45 \bmod 19 = \mathbf{7}$ &rarr; <span style="color:#b91c1c; font-weight:bold;">ชนกับ 357 ที่ช่อง 7! (ชนครั้งที่ 3)</span></li>
            <li>$i=3: (11 + 3 \times 17) \bmod 19 = 62 \bmod 19 = \mathbf{5}$ &rarr; ช่อง 5 ว่าง &rarr; ลง <strong>ช่อง 5</strong> (<strong style="color:#dc2626;">ชน 3 ครั้ง</strong>) *(ตรงกับเลข 3 เหนือ 391 ในลายมือรุ่นพี่)*</li>
          </ul>
        </li>
      </ul>

      <p><strong>3. ตารางผลลัพธ์สุดท้าย 19 ช่อง (Final Hash Table Array):</strong></p>
      <div style="overflow-x:auto;">
        <table style="width:100%; min-width:860px; border-collapse:collapse; text-align:center; font-size:12px; border:1.5px solid #334155; margin:8px 0;">
          <tr style="background:#1e293b; color:white;"><th style="padding:4px;">Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th><th>[16]</th><th>[17]</th><th>[18]</th></tr>
          <tr style="background:#fff;"><td style="font-weight:bold; background:#f1f5f9;">Value</td><td style="font-weight:bold; color:#1e40af;">323</td><td>-</td><td>-</td><td>-</td><td>-</td><td style="font-weight:bold; color:#1e40af;">391</td><td>-</td><td style="font-weight:bold; color:#1e40af;">357</td><td>-</td><td style="font-weight:bold; color:#1e40af;">370</td><td>-</td><td style="font-weight:bold; color:#1e40af;">340</td><td>-</td><td style="font-weight:bold; color:#1e40af;">868</td><td>-</td><td style="font-weight:bold; color:#1e40af;">969</td><td>-</td><td style="font-weight:bold; color:#1e40af;">17</td><td>-</td></tr>
        </table>
      </div>

      <p><strong>4. สรุปคำตอบ 1.2:</strong><br>
        • <strong>การชนของแต่ละคีย์:</strong> 323 (0), 17 (0), 969 (2), 868 (0), 340 (3), 370 (0), 357 (4), 391 (3)<br>
        • <strong>การชนรวมทั้งสิ้น:</strong> $0 + 0 + 2 + 0 + 3 + 0 + 4 + 3 = \mathbf{12 \text{ ครั้ง}}$<br>
        • <strong>การคำนวณ Rehashing (&gt; 75%):</strong><br>
        &nbsp;&nbsp;&nbsp;&nbsp;- เกณฑ์ 75% ของ 19 ช่อง: $19 \times 0.75 = 14.25$ &rarr; ต้องมีข้อมูลมากกว่า 75% คือตั้งแต่ <strong>14 หรือ 15 ตัว</strong> ขึ้นไป *(ตรงตามที่รุ่นพี่ทดเลข 14 ไว้ในรูปข้อสอบ)*<br>
        &nbsp;&nbsp;&nbsp;&nbsp;- ปัจจุบันใส่ไปแล้ว 8 ตัว &rarr; <strong>ต้องใส่เพิ่มอีก $14 - 8 = \mathbf{6 \text{ ตัว}}$</strong> (หรือ $15 - 8 = 7$ ตัว)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;- <strong>ขนาดตารางใหม่ (New TableSize):</strong> $2 \times \text{TableSize} = 2 \times 19 = 38 \implies \text{NextPrime}(38) = \mathbf{41}$ (จำนวนเฉพาะที่น้อยที่สุดที่ $\ge 38$)
      </p>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 2: BINARY HEAP                                                   -->
    <!-- ========================================================================= -->
    <h2 id="set0-q2" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      Question 2: Binary Min-Heap 4 Vertical Tables &amp; Tracing (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 6, pp. 243-260 / สไลด์ Priority Queue หน้า 7-9 / คำพูดอาจารย์วันที่ 9 ก.ย. &amp; 7 ต.ค. 2569</div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#3b82f6; margin:10px 0;">
      <div class="rules-title" style="color:#1d4ed8;">🎙️ ถอดคำพูดอาจารย์จากห้องเรียน (คำสั่งวาดตารางแนวตั้ง 4 ตาราง &amp; deleteMin):</div>
      <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
        • <em>"ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Binary Heap เป็นแนวตั้ง 4 ตาราง เขียนหัวตารางด้วยว่า 2.1, 2.2 deleteMin, 2.3 Insert, 2.4 deleteMin... การตรวจยึดผลลัพธ์จากการทำงานของโปรแกรมเป็นหลัก ถ้าใส่ตามความรู้สึกจะผิด!"</em><br>
        • <em>"Index 0 เป็น sentinel ห้ามใส่ข้อมูล ถ้าเริ่มที่ 0 สูตรพ่อลูกจะวนกลับมาตัวเอง พังทันที! สูตร Left = 2i, Right = 2i+1, Parent = i//2 ใช้ floor division ปัดเศษทิ้งเสมอ"</em>
      </p>
    </div>

    <h3 class="question-title" style="border-left-color:#4f46e5; color:#3730a3;">
      <span>2. Binary Min-Heap 4 Vertical Array Stages (12 Keys, deleteMin, Insert 3, deleteMin)</span>
      <span class="score-badge" style="background:#e0e7ff; color:#3730a3;">Score: 10 Marks (1 + 2 + 2 + 3 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given an empty Binary Min-Heap stored in an array indexed from $1$ (where slot $0$ is unused / sentinel). You are given 12 keys:</p>
    $$\mathbf{64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20}$$
    <p>Write the resulting vertical array for each of the following 4 stages:</p>
    <ul>
      <li><strong>2.1:</strong> Insert all 12 keys sequentially. Write final result in Table 1 [1 คะแนน]</li>
      <li><strong>2.2 deleteMin:</strong> Perform <code>deleteMin()</code> 1 time. Write result in Table 2 [2 คะแนน]</li>
      <li><strong>2.3 Insert:</strong> Insert key <code>3</code> into the heap. Write result in Table 3 [2 คะแนน]</li>
      <li><strong>2.4 deleteMin:</strong> Perform <code>deleteMin()</code> again. Write final result in Table 4 [3 คะแนน]</li>
    </ul>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง อ.ประดิษฐ์):</strong><br>
      2. ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Binary Heap เป็นแนวตั้ง 4 ตาราง เพื่อรองรับข้อมูลตาม 2.1<br>
      2.1 จงใส่ข้อมูลตัวเลข <strong>64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20</strong> เข้าไปในตารางอะเรย์ เขียนเฉพาะผลลัพธ์สุดท้ายที่ Insert ข้อมูลเสร็จแล้วเท่านั้น ในตารางแรก [1 คะแนน]<br>
      2.2 ให้ทำการ deleteMin 1 ครั้ง แล้วเขียนผลลัพธ์ลงในตารางอะเรย์ ที่ 2 [2 คะแนน]<br>
      2.3 หลังจากนั้นให้ทำการ insert ข้อมูลตัวเลข 3 เข้าไป เขียนผลในตารางอะเรย์ ที่ 3 [2 คะแนน]<br>
      2.4 หลังจากนั้น ให้ทำการ deleteMin อีกครั้ง แล้วเขียนผลลัพธ์ลงในตารางอะเรย์ ที่ 4 [3 คะแนน]<br>
      <em>เขียนหัวตารางด้วยว่า 2.1 &nbsp; 2.2 deleteMin &nbsp; 2.3 Insert &nbsp; 2.4 deleteMin</em>
    </div>

    <!-- BLANK 4 VERTICAL TABLES -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 2: ตารางอะเรย์แนวตั้ง 4 ตาราง (ตามข้อสอบจริง)
      </div>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin:10px 0;">
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
          <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.1</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8; font-style:italic;">unused</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td></td></tr>
          </table>
        </div>
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
          <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.2 deleteMin</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8; font-style:italic;">unused</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td style="color:#cbd5e1;">-</td></tr>
          </table>
        </div>
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
          <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.3 Insert</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8; font-style:italic;">unused</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td></td></tr>
          </table>
        </div>
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #475569; border-radius:6px; overflow:hidden;">
          <div style="background:#1e293b; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.4 deleteMin</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9; color:#475569; font-weight:bold;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8; font-style:italic;">unused</td></tr>
            <tr><td>[1]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[3]</td><td></td></tr>
            <tr><td>[4]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[6]</td><td></td></tr>
            <tr><td>[7]</td><td></td></tr><tr><td>[8]</td><td></td></tr><tr><td>[9]</td><td></td></tr>
            <tr><td>[10]</td><td></td></tr><tr><td>[11]</td><td></td></tr><tr><td>[12]</td><td style="color:#cbd5e1;">-</td></tr>
          </table>
        </div>
      </div>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 2 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดและตารางคำตอบแนวตั้งทั้ง 4 ตาราง (Binary Heap Solution):</div>
      <p><strong>เฉลยค่าในตารางอาร์เรย์แนวตั้งทั้ง 4 ขั้นตอน:</strong></p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin:12px 0;">
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #cbd5e1; border-radius:6px; overflow:hidden;">
          <div style="background:#15803d; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.1 (Insert 12)</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">unused</td></tr>
            <tr><td>[1]</td><td style="font-weight:bold; color:#15803d;">1</td></tr>
            <tr><td>[2]</td><td style="font-weight:bold; color:#15803d;">6</td></tr>
            <tr><td>[3]</td><td style="font-weight:bold; color:#15803d;">2</td></tr>
            <tr><td>[4]</td><td style="font-weight:bold; color:#15803d;">10</td></tr>
            <tr><td>[5]</td><td style="font-weight:bold; color:#15803d;">8</td></tr>
            <tr><td>[6]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[7]</td><td style="font-weight:bold; color:#15803d;">5</td></tr>
            <tr><td>[8]</td><td style="font-weight:bold; color:#15803d;">64</td></tr>
            <tr><td>[9]</td><td style="font-weight:bold; color:#15803d;">14</td></tr>
            <tr><td>[10]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[11]</td><td style="font-weight:bold; color:#15803d;">15</td></tr>
            <tr><td>[12]</td><td style="font-weight:bold; color:#15803d;">24</td></tr>
          </table>
        </div>
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #cbd5e1; border-radius:6px; overflow:hidden;">
          <div style="background:#15803d; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.2 deleteMin</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">unused</td></tr>
            <tr><td>[1]</td><td style="font-weight:bold; color:#15803d;">2</td></tr>
            <tr><td>[2]</td><td style="font-weight:bold; color:#15803d;">6</td></tr>
            <tr><td>[3]</td><td style="font-weight:bold; color:#15803d;">5</td></tr>
            <tr><td>[4]</td><td style="font-weight:bold; color:#15803d;">10</td></tr>
            <tr><td>[5]</td><td style="font-weight:bold; color:#15803d;">8</td></tr>
            <tr><td>[6]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[7]</td><td style="font-weight:bold; color:#15803d;">24</td></tr>
            <tr><td>[8]</td><td style="font-weight:bold; color:#15803d;">64</td></tr>
            <tr><td>[9]</td><td style="font-weight:bold; color:#15803d;">14</td></tr>
            <tr><td>[10]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[11]</td><td style="font-weight:bold; color:#15803d;">15</td></tr>
            <tr><td>[12]</td><td style="color:#cbd5e1;">-</td></tr>
          </table>
        </div>
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #cbd5e1; border-radius:6px; overflow:hidden;">
          <div style="background:#15803d; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.3 Insert</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">unused</td></tr>
            <tr><td>[1]</td><td style="font-weight:bold; color:#15803d;">2</td></tr>
            <tr><td>[2]</td><td style="font-weight:bold; color:#15803d;">6</td></tr>
            <tr><td>[3]</td><td style="font-weight:bold; color:#15803d;">3</td></tr>
            <tr><td>[4]</td><td style="font-weight:bold; color:#15803d;">10</td></tr>
            <tr><td>[5]</td><td style="font-weight:bold; color:#15803d;">8</td></tr>
            <tr><td>[6]</td><td style="font-weight:bold; color:#15803d;">5</td></tr>
            <tr><td>[7]</td><td style="font-weight:bold; color:#15803d;">24</td></tr>
            <tr><td>[8]</td><td style="font-weight:bold; color:#15803d;">64</td></tr>
            <tr><td>[9]</td><td style="font-weight:bold; color:#15803d;">14</td></tr>
            <tr><td>[10]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[11]</td><td style="font-weight:bold; color:#15803d;">15</td></tr>
            <tr><td>[12]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
          </table>
        </div>
        <div style="flex:1; min-width:130px; max-width:160px; border:1.5px solid #cbd5e1; border-radius:6px; overflow:hidden;">
          <div style="background:#15803d; color:#fff; font-weight:bold; font-size:12px; padding:6px; text-align:center;">2.4 deleteMin</div>
          <table style="width:100%; border-collapse:collapse; text-align:center; font-size:11.5px;">
            <tr style="background:#f1f5f9;"><th>Index</th><th>Value</th></tr>
            <tr><td>[0]</td><td style="color:#94a3b8;">unused</td></tr>
            <tr><td>[1]</td><td style="font-weight:bold; color:#15803d;">3</td></tr>
            <tr><td>[2]</td><td style="font-weight:bold; color:#15803d;">6</td></tr>
            <tr><td>[3]</td><td style="font-weight:bold; color:#15803d;">5</td></tr>
            <tr><td>[4]</td><td style="font-weight:bold; color:#15803d;">10</td></tr>
            <tr><td>[5]</td><td style="font-weight:bold; color:#15803d;">8</td></tr>
            <tr><td>[6]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[7]</td><td style="font-weight:bold; color:#15803d;">24</td></tr>
            <tr><td>[8]</td><td style="font-weight:bold; color:#15803d;">64</td></tr>
            <tr><td>[9]</td><td style="font-weight:bold; color:#15803d;">14</td></tr>
            <tr><td>[10]</td><td style="font-weight:bold; color:#15803d;">20</td></tr>
            <tr><td>[11]</td><td style="font-weight:bold; color:#15803d;">15</td></tr>
            <tr><td>[12]</td><td style="color:#cbd5e1;">-</td></tr>
          </table>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 3: INSERTION SORT                                                -->
    <!-- ========================================================================= -->
    <h2 id="set0-q3" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      Question 3: Insertion Sort Tracing &amp; Position Moves (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7, pp. 281-285 / สไลด์ Insertion Sort / คำพูดอาจารย์วันที่ 16 ก.ย. &amp; 7 ต.ค. 2569</div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#3b82f6; margin:10px 0;">
      <div class="rules-title" style="color:#1d4ed8;">🎙️ ถอดคำพูดอาจารย์จากห้องเรียน (Worst Case &amp; นับรอบการเลื่อน):</div>
      <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
        • <em>"โจทย์จะให้ชุดตัวเลขมา ให้ไล่ทีละ Pass ถามว่าหลังจากจบ Pass p = 3 หรือ p = 6 อาร์เรย์มีค่าเป็นอย่างไร และมี Position Move กี่ครั้ง... ถ้าข้อมูลเป็น Worst Case เรียงจากมากไปน้อย สูตรคือ $N(N-1)/2$ ถ้าเรียงอยู่แล้วเป็น Best Case คือ 0 ครั้ง"</em>
      </p>
    </div>

    <h3 class="question-title" style="border-left-color:#4f46e5; color:#3730a3;">
      <span>3.1 Worst-Case Position Moves &amp; Pass Tracing</span>
      <span class="score-badge" style="background:#e0e7ff; color:#3730a3;">Score: 10 Marks (4 + 6 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given the input array of 12 elements for <code>insertionSort</code>:</p>
    $$\mathbf{61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2}$$
    <ol>
      <li>If an input array of 12 elements is given in <strong>Worst Case</strong> (descending order), how many total position moves will occur after insertionSort completes? [4 คะแนน]</li>
      <li>For the given 12 elements above, trace the algorithm and write the state of the array after <strong>Pass $p = 3$</strong> and after <strong>Pass $p = 6$</strong>, together with the number of Position Moves in each round. [6 คะแนน]</li>
    </ol>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง 2564 หน้า 2):</strong><br>
      3.1 ให้กำหนดข้อมูลเป็น input เริ่มต้นสำหรับการทำ insertionSort จำนวน 12 ตัว โดยเป็นข้อมูลแบบ Worst Case เมื่อทำเสร็จสิ้น เกิด position move รวมทั้งสิ้นกี่ครั้ง [4 คะแนน]<br>
      3.2 กำหนดข้อมูล input เริ่มต้น 12 ตัว: <strong>61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2</strong> ให้เขียนผลของการทำงานในรอบที่ $p = 3$ และ $p = 6$ พร้อมนับ Position Move ของทั้ง 2 รอบนี้ [6 คะแนน]
    </div>

    <!-- BLANK SHEET FOR QUESTION 3 -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 3: ตาราง Insertion Sort (Input, Pass p=3, Pass p=6)
      </div>
      <p style="margin:0 0 6px 0; font-size:14px;">
        3.1 ข้อมูลแบบ Worst Case 12 ตัว เกิด Position Move รวมทั้งสิ้น = ............ ครั้ง (เขียนตัวเลขเต็ม)
      </p>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px; border:2px solid #334155;">
        <thead>
          <tr style="background:#1e293b; color:white;">
            <th style="padding:6px; width:120px;">รอบ (Pass)</th>
            <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th>
            <th style="width:90px;">Moves</th>
          </tr>
        </thead>
        <tbody>
          <tr><td style="font-weight:bold; background:#f1f5f9;">เริ่มต้น (Input)</td><td>61</td><td>52</td><td>12</td><td>24</td><td>8</td><td>35</td><td>32</td><td>5</td><td>71</td><td>68</td><td>18</td><td>2</td><td>-</td></tr>
          <tr><td style="font-weight:bold; background:#f8fafc;">After p = 3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>......</td></tr>
          <tr><td style="font-weight:bold; background:#f8fafc;">After p = 6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>......</td></tr>
        </tbody>
      </table>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 3 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 3 (Insertion Sort Solution):</div>
      <p><strong>1. คำตอบข้อ 3.1:</strong><br>
        ข้อมูลแบบ Worst Case คือเรียงจากมากไปน้อย (เช่น 12, 11, 10, ..., 1)<br>
        สูตรคำนวณ: $\text{Moves} = \frac{N(N-1)}{2} = \frac{12 \times 11}{2} = \mathbf{66 \text{ ครั้ง}}$
      </p>
      <p><strong>2. คำตอบข้อ 3.2 การ Trace แต่ละรอบ:</strong></p>
      <ul>
        <li>$p=1$ (Key 52): 52 เลื่อนมาหน้า 61 (1 move) &rarr; <code>[52, 61, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]</code></li>
        <li>$p=2$ (Key 12): 12 เลื่อนมาหน้า 52 (2 moves) &rarr; <code>[12, 52, 61, 24, 8, 35, 32, 5, 71, 68, 18, 2]</code></li>
        <li>$p=3$ (Key 24): 24 แทรกระหว่าง 12 กับ 52 (2 moves: ผ่าน 61, 52)<br>
          &rarr; <strong>After p = 3: <code>[12, 24, 52, 61, 8, 35, 32, 5, 71, 68, 18, 2]</code></strong> (Moves รอบนี้ $= 2$, สะสม $= 5$)
        </li>
        <li>$p=4$ (Key 8): 8 เลื่อนมาหน้าสุด (4 moves) &rarr; <code>[8, 12, 24, 52, 61, 35, 32, 5, 71, 68, 18, 2]</code></li>
        <li>$p=5$ (Key 35): 35 แทรกระหว่าง 24 กับ 52 (2 moves) &rarr; <code>[8, 12, 24, 35, 52, 61, 32, 5, 71, 68, 18, 2]</code></li>
        <li>$p=6$ (Key 32): 32 แทรกระหว่าง 24 กับ 35 (3 moves: ผ่าน 61, 52, 35)<br>
          &rarr; <strong>After p = 6: <code>[8, 12, 24, 32, 35, 52, 61, 5, 71, 68, 18, 2]</code></strong> (Moves รอบนี้ $= 3$, สะสม $= 14$)
        </li>
      </ul>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 4: SELECTION SORT / BUBBLE SORT                                  -->
    <!-- ========================================================================= -->
    <h2 id="set0-q4" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      Question 4: Selection Sort หรือ Bubble Sort (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 / ชีต Test Program 2 / คำพูดอาจารย์วันที่ 16 ก.ย. &amp; 7 ต.ค. 2569</div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#3b82f6; margin:10px 0;">
      <div class="rules-title" style="color:#1d4ed8;">🎙️ ถอดคำพูดอาจารย์จากห้องเรียน:</div>
      <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
        • <em>"อาจารย์จะเลือกมา 1 ตัว ระหว่าง Selection Sort หรือ Bubble Sort ให้ชุดข้อมูลมาแล้ว Tracing ทีละรอบเหมือน Test Program 2 ที่ส่งไป... สำหรับ Bubble Sort จำนวนรอบทั้งหมดคือ $N-1$ รอบ และจำนวนการ Swap ทั้งหมดจะเท่ากับจำนวน Inversion ของข้อมูลพอดี!"</em>
      </p>
    </div>

    <h3 class="question-title" style="border-left-color:#4f46e5; color:#3730a3;">
      <span>4. Bubble Sort &amp; Selection Sort Tracing</span>
      <span class="score-badge" style="background:#e0e7ff; color:#3730a3;">Score: 10 Marks (10 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given the input array $A = [64, 34, 25, 12, 22, 11, 90]$ with $N = 7$ elements.</p>
    <ol>
      <li>For <strong>Bubble Sort</strong>:
        <ul>
          <li>What is the total number of passes required to sort the array?</li>
          <li>What is the total number of swaps executed when the algorithm terminates?</li>
          <li>Write the state of the array in Pass 1 at Step 4 (after comparing $A[3]$ and $A[4]$).</li>
          <li>Write the state of the array after Pass 1 completes.</li>
        </ul>
      </li>
      <li>For <strong>Selection Sort</strong>: Write the state of the array after Pass 1, Pass 2, and Pass 3.</li>
    </ol>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> กำหนดอาเรย์นำเข้า $A = [64, 34, 25, 12, 22, 11, 90]$ จำนวน $N = 7$ ตัว จงตอบคำถามเกี่ยวกับการ Trace ของ Bubble Sort และ Selection Sort
    </div>

    <!-- BLANK SHEET FOR QUESTION 4 -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 4: การแกะรอย Bubble Sort &amp; Selection Sort
      </div>
      <p style="margin:0; font-size:14px; line-height:2.2;">
        <strong>1. Bubble Sort:</strong><br>
        • จำนวน Pass ทั้งหมด = ............ รอบ<br>
        • จำนวนครั้งการ Swap ทั้งหมด = ............ ครั้ง<br>
        • สถานะ Array ใน Pass 1 ขั้นตอนที่ 4: [ ......, ......, ......, ......, ......, ......, ...... ]<br>
        • สถานะ Array หลังจบ Pass 1: [ ......, ......, ......, ......, ......, ......, ...... ]<br>
        <strong>2. Selection Sort:</strong><br>
        • After Pass 1: [ ......, ......, ......, ......, ......, ......, ...... ]<br>
        • After Pass 2: [ ......, ......, ......, ......, ......, ......, ...... ]<br>
        • After Pass 3: [ ......, ......, ......, ......, ......, ......, ...... ]
      </p>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 4 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 4 (Bubble Sort &amp; Selection Sort Solution):</div>
      <p><strong>1. เฉลย Bubble Sort:</strong></p>
      <ul>
        <li>จำนวน Pass ทั้งหมด $= N - 1 = 7 - 1 = \mathbf{6 \text{ รอบ}}$</li>
        <li>จำนวน Swap ทั้งหมด $=$ จำนวน Inversion $=\mathbf{14 \text{ ครั้ง}}$</li>
        <li>ใน Pass 1 Step 4 (เปรียบเทียบ 64 กับ 22 แล้ว swap) &rarr; ได้: <strong><code>[34, 25, 12, 22, 64, 11, 90]</code></strong></li>
        <li>หลังจบ Pass 1 (เลข 90 อยู่ขวาสุด) &rarr; ได้: <strong><code>[34, 25, 12, 22, 11, 64, 90]</code></strong></li>
      </ul>
      <p><strong>2. เฉลย Selection Sort:</strong></p>
      <ul>
        <li>เริ่มต้น: <code>[64, 34, 25, 12, 22, 11, 90]</code></li>
        <li>Pass 1: ค่าน้อยสุดคือ 11 (สลับกับ 64 ที่ index 0) &rarr; <strong><code>[11, 34, 25, 12, 22, 64, 90]</code></strong></li>
        <li>Pass 2: ค่าน้อยสุดในช่วงที่เหลือคือ 12 (สลับกับ 34 ที่ index 1) &rarr; <strong><code>[11, 12, 25, 34, 22, 64, 90]</code></strong></li>
        <li>Pass 3: ค่าน้อยสุดคือ 22 (สลับกับ 25 ที่ index 2) &rarr; <strong><code>[11, 12, 22, 34, 25, 64, 90]</code></strong></li>
      </ul>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 5: TOPOLOGICAL SORT                                              -->
    <!-- ========================================================================= -->
    <h2 id="set0-q5" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      Question 5: Topological Sort in Directed Acyclic Graph (DAG) (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9, pp. 363-368 / สไลด์บทที่ 10 Graph / คำพูดอาจารย์วันที่ 23 ก.ย. &amp; 7 ต.ค. 2569</div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#3b82f6; margin:10px 0;">
      <div class="rules-title" style="color:#1d4ed8;">🎙️ ถอดคำพูดอาจารย์จากห้องเรียน:</div>
      <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
        • <em>"โจทย์ Topological Sort จะให้กราฟ DAG มา 7 จุดยอด ให้นักศึกษาทำ 3 ข้อย่อย: (1) เขียนตาราง Indegree Array แสดงรอยขีดฆ่า (2) เขียนภาพ Queue แสดงข้อมูลหลังเสร็จสิ้นพร้อมชี้ตำแหน่ง front และ back ตาม Circular Queue บทที่ 3 (3) เขียน Topological Ordering ลำดับที่เป็นคำตอบ"</em>
      </p>
    </div>

    <h3 class="question-title" style="border-left-color:#4f46e5; color:#3730a3;">
      <span>5. Indegree Array, Queue State, and Topological Ordering</span>
      <span class="score-badge" style="background:#e0e7ff; color:#3730a3;">Score: 10 Marks (5 + 2 + 3 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given a Directed Acyclic Graph (DAG) with 7 vertices ($v_1, v_2, v_3, v_4, v_5, v_6, v_7$) defined by the following Adjacency List:</p>
    <ul>
      <li>$v_1 \to [v_2, v_3, v_4]$</li>
      <li>$v_2 \to [v_4, v_5]$</li>
      <li>$v_3 \to [v_6]$</li>
      <li>$v_4 \to [v_3, v_6, v_7]$</li>
      <li>$v_5 \to [v_4, v_7]$</li>
      <li>$v_6 \to []$ (no outgoing edges)</li>
      <li>$v_7 \to [v_6]$</li>
    </ul>
    <ol>
      <li>Show the step-by-step Indegree Array with crossed-out values as vertices are processed [5 คะแนน]</li>
      <li>Draw the state of the Queue (capacity 7) after algorithm terminates, specifying where <code>front</code> and <code>back</code> point [2 คะแนน]</li>
      <li>Write the final <strong>Topological Ordering</strong> sequence [3 คะแนน]</li>
    </ol>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริง 2564 หน้า 4):</strong><br>
      6. ให้นักศึกษาเขียนตารางอะเรย์ ชื่อ Indegree Array สำหรับประมวลผล Topological Sort กำหนดข้อมูลกราฟ DAG มี 7 Vertex<br>
      6.1 จงแสดงวิธีหา Topological Sort เขียนผลลัพธ์สุดท้ายของตาราง Indegree Array [5 คะแนน]<br>
      6.2 กำหนด Queue ขนาด 7 ช่อง จงเขียนภาพ Queue เพื่อแสดงข้อมูลหลังจากทำงานเสร็จ โดยเขียนตำแหน่งของ front และ back ด้วย [2 คะแนน]<br>
      6.3 เขียน Topological Ordering ที่เป็นคำตอบของกราฟนี้ [3 คะแนน]
    </div>

    <!-- BLANK SHEET FOR QUESTION 5 -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 5: ตาราง Indegree Array และ Queue
      </div>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px; border:2px solid #334155; margin-bottom:10px;">
        <thead>
          <tr style="background:#1e293b; color:white;">
            <th style="padding:6px; width:110px;">Vertex</th>
            <th>v1</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th><th>v6</th><th>v7</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f1f5f9; padding:8px;">Indegree (ขีดฆ่า)</td>
            <td style="height:35px;"></td><td></td><td></td><td></td><td></td><td></td><td></td>
          </tr>
        </tbody>
      </table>
      <p style="margin:0; font-size:14px; line-height:2.2;">
        <strong>Queue (ขนาด 7 ช่อง):</strong> front อยู่ที่ตำแหน่ง .......... &nbsp;|&nbsp; back อยู่ที่ตำแหน่ง ..........<br>
        <strong>Topological Ordering:</strong> .........................................................................................................................
      </p>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 5 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 5 (Topological Sort Solution):</div>
      <p><strong>1. การคำนวณ Indegree เริ่มต้น:</strong><br>
        • $v_1$: 0 &nbsp;|&nbsp; $v_2$: 1 (จาก $v_1$) &nbsp;|&nbsp; $v_3$: 2 (จาก $v_1, v_4$) &nbsp;|&nbsp; $v_4$: 3 (จาก $v_1, v_2, v_5$) &nbsp;|&nbsp; $v_5$: 1 (จาก $v_2$) &nbsp;|&nbsp; $v_6$: 3 (จาก $v_3, v_4, v_7$) &nbsp;|&nbsp; $v_7$: 2 (จาก $v_4, v_5$)
      </p>
      <p><strong>2. ขั้นตอนการทำงานและลำดับการลด Indegree:</strong></p>
      <ul>
        <li>เริ่มต้น: $Q = [v_1]$</li>
        <li>Dequeue $v_1$: ลด $v_2 (1 \to 0), v_3 (2 \to 1), v_4 (3 \to 2)$ &rarr; Enqueue $v_2 \implies Q = [v_2]$</li>
        <li>Dequeue $v_2$: ลด $v_4 (2 \to 1), v_5 (1 \to 0)$ &rarr; Enqueue $v_5 \implies Q = [v_5]$</li>
        <li>Dequeue $v_5$: ลด $v_4 (1 \to 0), v_7 (2 \to 1)$ &rarr; Enqueue $v_4 \implies Q = [v_4]$</li>
        <li>Dequeue $v_4$: ลด $v_3 (1 \to 0), v_6 (3 \to 2), v_7 (1 \to 0)$ &rarr; Enqueue $v_3, v_7 \implies Q = [v_3, v_7]$</li>
        <li>Dequeue $v_3$: ลด $v_6 (2 \to 1) \implies Q = [v_7]$</li>
        <li>Dequeue $v_7$: ลด $v_6 (1 \to 0)$ &rarr; Enqueue $v_6 \implies Q = [v_6]$</li>
        <li>Dequeue $v_6$: ไม่มีลูก &rarr; $Q = []$ เสร็จสิ้น</li>
      </ul>
      <p><strong>3. สรุปคำตอบ:</strong><br>
        • <strong>Indegree สุดท้าย:</strong> ทุก Vertex กลายเป็น 0 ทั้งหมด โดยมีรอยขีดฆ่าตามลำดับ<br>
        • <strong>Queue:</strong> front อยู่ที่ตำแหน่ง <strong>0</strong> (หรือตามฟังก์ชัน dequeue), back อยู่ที่ตำแหน่ง <strong>6</strong><br>
        • <strong>Topological Ordering:</strong> <strong style="color:#15803d; font-size:15px;">v1, v2, v5, v4, v3, v7, v6</strong>
      </p>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 6: UNWEIGHTED SHORTEST PATH                                      -->
    <!-- ========================================================================= -->
    <h2 id="set0-q6" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      Question 6: Unweighted Shortest Path (ถอดแบบ Assignment 4 วันสุดท้าย 100%) (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9, pp. 368-374 / Assignment 4 ฉบับจริงในห้องเรียน 7 ต.ค. 2569 / ไฟล์เสียง 20261007_092525.txt</div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#3b82f6; margin:10px 0;">
      <div class="rules-title" style="color:#1d4ed8;">🎙️ ถอดคำพูดอาจารย์จากห้องเรียน (ย้ำชัดในคาบสุดท้าย):</div>
      <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
        • <em>"ข้อ 6 เหมือน Assignment 4 ที่ทำวันนี้เป๊ะๆ! ให้กราฟมา แล้วให้ตาราง Known, Dist, Path และ Queue มา ให้คุณไล่ขีดฆ่าเติมค่าทีละสเต็ป แล้วตอบระยะทางและเส้นทาง... ลำดับเส้นทางห้ามเขียนลูกศร A -> B -> F ให้เขียนคั่นด้วยจุลภาค A, B, E, F ตามที่เน้นในห้องเรียน!"</em>
      </p>
    </div>

    <h3 class="question-title" style="border-left-color:#4f46e5; color:#3730a3;">
      <span>6. Adjacency List, Shortest Path Table, and Path Backtracking</span>
      <span class="score-badge" style="background:#e0e7ff; color:#3730a3;">Score: 10 Marks (3 + 5 + 2 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Given a directed unweighted graph with 7 vertices ($A, B, C, D, E, F, G$) from Assignment 4 with starting vertex <strong>Vertex A</strong>. The directed edges are: $A \to B, C$; $B \to G, E, C$; $C \to E, D$; $D \to F, A$; $E \to D, F$; $F \to \text{Ground}$; $G \to E$.</p>
    <ol>
      <li>Convert the graph into an <strong>Adjacency List</strong> representation [3 คะแนน]</li>
      <li>Fill the Shortest Path processing table with columns <code>Known</code>, <code>Dist</code> ($d_v$), and <code>Path</code> ($p_v$) showing crossed-out intermediate values [5 คะแนน]</li>
      <li>State the <strong>Shortest Path</strong> and the <strong>distance</strong> from $A$ to $F$ [2 คะแนน]</li>
    </ol>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ข้อความตามใบงาน Assignment 4 วันสุดท้าย):</strong><br>
      กำหนดกราฟมาให้ มี Vertex A, B, C, D, E, F, G ให้ vertex A เป็นจุดเริ่มต้น จงแสดงวิธีหาเส้นทางที่สั้นที่สุดจาก vertex A ไปยังทุกๆ vertex ในกราฟ<br>
      ข้อ 1. แปลงรูปกราฟให้เป็น Adjacency List (3 คะแนน)<br>
      ข้อ 2. อะเรย์สำหรับประมวลผล Shortest Path (Known, Dist, Path, Queue) สามารถขีดฆ่าเพื่อแสดงค่าที่เปลี่ยนไป (5 คะแนน)<br>
      ข้อ 3. จงหา Shortest Path และระยะทางจาก A ไปยัง F (2 คะแนน)
    </div>

    <!-- BLANK SHEET FOR QUESTION 6 -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 6: Adjacency List และตาราง Shortest Path
      </div>
      <p style="margin:0 0 4px 0; font-size:13.5px; font-weight:bold; color:#1e293b;">1. Adjacency List:</p>
      <div style="margin:0 0 12px 0; padding:12px 16px; background:#ffffff; border:1.5px solid #94a3b8; border-radius:6px; font-family:'JetBrains Mono', Consolas, monospace; font-size:13px; color:#0f172a; line-height:2.2;">
        <div><strong>A &rarr;</strong> ........................................................................................................................</div>
        <div><strong>B &rarr;</strong> ........................................................................................................................</div>
        <div><strong>C &rarr;</strong> ........................................................................................................................</div>
        <div><strong>D &rarr;</strong> ........................................................................................................................</div>
        <div><strong>E &rarr;</strong> ........................................................................................................................</div>
        <div><strong>F &rarr;</strong> ........................................................................................................................</div>
        <div><strong>G &rarr;</strong> ........................................................................................................................</div>
      </div>
      <p style="margin:0 0 4px 0; font-size:13.5px; font-weight:bold; color:#1e293b;">2. ตารางประมวลผล Shortest Path (จุดเริ่ม = A):</p>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px; border:2px solid #334155; margin-bottom:8px;">
        <thead>
          <tr style="background:#1e293b; color:white;">
            <th style="padding:5px; width:70px;">Vertex</th>
            <th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th>
          </tr>
        </thead>
        <tbody>
          <tr><td style="font-weight:bold; background:#f1f5f9; padding:6px;">Known</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
          <tr><td style="font-weight:bold; background:#f8fafc; padding:6px;">Dist (dv)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
          <tr><td style="font-weight:bold; background:#f1f5f9; padding:6px;">Path (pv)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        </tbody>
      </table>
      <p style="margin:0; font-size:14px; line-height:2.2;">
        <strong>Shortest Path จาก A ไป F คือ:</strong> ..................................................... &nbsp;|&nbsp; <strong>ระยะทาง (Distance) =</strong> ............
      </p>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 6 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 6 (Assignment 4 Solution):</div>
      <p><strong>1. เฉลย Adjacency List:</strong></p>
      <div style="margin:8px 0; padding:12px 16px; background:#0f172a; border:1px solid #334155; border-radius:6px; font-family:'JetBrains Mono', Consolas, monospace; font-size:13.5px; color:#38bdf8; line-height:1.9;">
        <div><strong style="color:#ffffff;">A</strong> &rarr; [ B ] &rarr; [ C ] &rarr; <span style="color:#f43f5e;">||</span></div>
        <div><strong style="color:#ffffff;">B</strong> &rarr; [ G ] &rarr; [ E ] &rarr; [ C ] &rarr; <span style="color:#f43f5e;">||</span></div>
        <div><strong style="color:#ffffff;">C</strong> &rarr; [ E ] &rarr; [ D ] &rarr; <span style="color:#f43f5e;">||</span></div>
        <div><strong style="color:#ffffff;">D</strong> &rarr; [ F ] &rarr; [ A ] &rarr; <span style="color:#f43f5e;">||</span></div>
        <div><strong style="color:#ffffff;">E</strong> &rarr; [ D ] &rarr; [ F ] &rarr; <span style="color:#f43f5e;">||</span></div>
        <div><strong style="color:#ffffff;">F</strong> &rarr; <span style="color:#f43f5e;">||</span> <span style="color:#94a3b8; font-size:12px;">(ไม่มีเส้นเชื่อมออกจาก F / Ground)</span></div>
        <div><strong style="color:#ffffff;">G</strong> &rarr; [ E ] &rarr; <span style="color:#f43f5e;">||</span></div>
      </div>
      <p><strong>2. ตารางสรุปผลลัพธ์สุดท้าย (Final Table):</strong></p>
      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px; border:1.5px solid #334155; margin:8px 0;">
        <tr style="background:#1e293b; color:white;"><th style="padding:5px;">Vertex</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th></tr>
        <tr style="background:#fff;"><td style="font-weight:bold; background:#f1f5f9;">Known</td><td><strong>T</strong></td><td><strong>T</strong></td><td><strong>T</strong></td><td><strong>T</strong></td><td><strong>T</strong></td><td><strong>T</strong></td><td><strong>T</strong></td></tr>
        <tr style="background:#f8fafc;"><td style="font-weight:bold; background:#e2e8f0;">Dist ($d_v$)</td><td><strong>0</strong></td><td><strong>1</strong></td><td><strong>1</strong></td><td><strong>2</strong></td><td><strong>2</strong></td><td><strong>3</strong></td><td><strong>2</strong></td></tr>
        <tr style="background:#fff;"><td style="font-weight:bold; background:#f1f5f9;">Path ($p_v$)</td><td><strong>0</strong></td><td><strong>A</strong></td><td><strong>A</strong></td><td><strong>C</strong></td><td><strong>B</strong></td><td><strong>E</strong></td><td><strong>B</strong></td></tr>
      </table>
      <p><strong>3. การหา Shortest Path จาก A ไปยัง F:</strong><br>
        • ตรวจสอบ Dist ของ $F \implies d_v = \mathbf{3}$<br>
        • Backtrack ย้อนกลับผ่านคอลัมน์ $p_v$: $F \leftarrow E \leftarrow B \leftarrow A$<br>
        • <strong>Shortest Path:</strong> <strong style="color:#15803d; font-size:15px;">A, B, E, F</strong> (ความยาว = 3 ขอบ)<br>
        <em>(⚠️ คำเตือนอาจารย์: เขียนคั่นด้วยจุลภาค A, B, E, F ห้ามเขียนลูกศร A -> B -> E -> F)</em>
      </p>
    </div>

    <!-- ========================================================================= -->
    <!-- QUESTION 7: PROPERTIES & PERCENTAGE CALCULATIONS                          -->
    <!-- ========================================================================= -->
    <h2 id="set0-q7" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">
      Question 7: คำถามย่อย Properties, Formulas &amp; Percentage Calculations (10 คะแนน)
    </h2>
    <div class="ref-tag">📖 อ้างอิง: ภาพหน้าจอ Notepad ของ อ.ประดิษฐ์ (IMG_20261007_120456_375.jpg) / คำพูดอาจารย์วันที่ 23 ก.ย. &amp; 7 ต.ค. 2569</div>

    <div class="rules-box" style="background:#eff6ff; border-left-color:#3b82f6; margin:10px 0;">
      <div class="rules-title" style="color:#1d4ed8;">🎙️ ถอดคำพูดอาจารย์จากห้องเรียน:</div>
      <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
        • <em>"ถาม Properties โครงสร้างอะไรมี 2 properties, 3 properties... พวกที่มีการคำนวณ ใช้สูตร เปอร์เซ็นต์ what percentage of, how many เช่น memory waste, เส้นเชื่อม complete graph, โหนดสูงสุดใน binary tree... ตอบเป็นตัวเลขเต็ม ห้ามติดสูตร ห้ามติดเลขยกกำลัง ถ้าติดสูตรได้ 0 ทันที!"</em>
      </p>
    </div>

    <h3 class="question-title" style="border-left-color:#4f46e5; color:#3730a3;">
      <span>7. Short Answers: Properties, RAM Waste %, Complete Graphs, and Heights</span>
      <span class="score-badge" style="background:#e0e7ff; color:#3730a3;">Score: 10 Marks (ข้อละ 1–2 คะแนน รวม 10 คะแนน)</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Answer the following concise theoretical and calculation questions precisely:</p>
    <ol>
      <li>Which data structure has strictly <strong>Two Fundamental Properties</strong>? What are they? [2 คะแนน]</li>
      <li>Which data structure has strictly <strong>Three Properties</strong>? [1 คะแนน]</li>
      <li>In an unweighted directed graph with 7 vertices and 12 directed edges stored as an <strong>Adjacency Matrix</strong> ($7 \times 7 = 49$ entries):
        <ul>
          <li>What percentage of memory entries are wasted as zeros (unused)?</li>
          <li>What percentage of entries actually hold real data? [2 คะแนน]</li>
        </ul>
      </li>
      <li>An <strong>Undirected Complete Graph</strong> has 16 vertices. How many total edges does it have? (Must answer as an exact integer, do NOT write formula!) [2 คะแนน]</li>
      <li>A <strong>Complete Binary Tree</strong> has height $h = 10$. What is the maximum number of nodes it can contain? (Must answer as an exact integer, do NOT write power expression!) [2 คะแนน]</li>
      <li>In Quicksort with Median-of-Three Partitioning, which elements are NOT included in the partition loop, and why? [1 คะแนน]</li>
    </ol>

    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย - ตามที่ อ.ประดิษฐ์ พิมพ์บน Notepad เป๊ะๆ):</strong><br>
      จงตอบคำถามย่อยต่อไปนี้ให้ถูกต้องและสมบูรณ์ (ข้อที่ตอบเป็นตัวเลข ต้องตอบเป็นตัวเลขจำนวนเต็ม ห้ามติดรูปสมการหรือเลขยกกำลัง)
    </div>

    <!-- BLANK SHEET FOR QUESTION 7 -->
    <div class="blank-sheet-box">
      <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
        📝 ช่องจำลองกระดาษคำตอบข้อ 7: เติมคำตอบสั้น
      </div>
      <p style="margin:0; font-size:14px; line-height:2.4;">
        7.1 โครงสร้างข้อมูลที่มี 2 Properties คือ ........................................................... โดยมี (1) ........................................................... และ (2) ...........................................................<br>
        7.2 โครงสร้างข้อมูลที่มี 3 Properties คือ ...........................................................<br>
        7.3 ใน Adjacency Matrix ขนาด $7 \times 7$ ที่มีเส้นเชื่อม 12 เส้น:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;• เปอร์เซ็นต์พื้นที่สูญเปล่า (Memory waste / Zeros) = ............ %<br>
        &nbsp;&nbsp;&nbsp;&nbsp;• เปอร์เซ็นต์พื้นที่ข้อมูลจริง (Data density) = ............ %<br>
        7.4 Complete Graph 16 จุดยอด มีเส้นเชื่อมทั้งหมด = ............ เส้น (ตอบตัวเลขเต็ม)<br>
        7.5 Complete Binary Tree สูง 10 ชั้น มีจำนวนโหนดมากที่สุด = ............ โหนด (ตอบตัวเลขเต็ม)<br>
        7.6 ใน Quicksort ข้อมูลที่ไม่ถูกนำไป partition คือ .........................................................................................................................
      </p>
    </div>

    <!-- COLLAPSIBLE SOLUTION BOX 7 -->
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดข้อ 7 (Properties &amp; Calculation Solutions):</div>
      <ul>
        <li><strong>7.1 โครงสร้างที่มี 2 Properties:</strong> คือ <strong>Binary Heap</strong> (Priority Queue)<br>
          (1) <em>Structure Property:</em> ต้องเป็น Complete Binary Tree (โหนดเรียงเต็มจากซ้ายไปขวาในชั้นล่างสุด)<br>
          (2) <em>Heap-Order Property:</em> ค่าของ Parent ต้องน้อยกว่าหรือเท่ากับลูกเสมอ สำหรับ Min-Heap ($Key(P) \le Key(X)$)
        </li>
        <li><strong>7.2 โครงสร้างที่มี 3 Properties:</strong> คือ <strong>AVL Tree</strong> (หรือ Red-Black Tree / B-Tree) โดยมี (1) Binary Tree Structure (2) Binary Search Tree Property ($Left < Root < Right$) (3) Height-Balance Property ($|\Delta h| \le 1$)</li>
        <li><strong>7.3 เปอร์เซ็นต์ Adjacency Matrix ($7 \times 7 = 49$ ช่อง, ข้อมูล 12 ช่อง):</strong><br>
          • <strong>Memory Waste (Zeros):</strong> $\frac{49 - 12}{49} \times 100\% = \frac{37}{49} \times 100\% = \mathbf{75.51\%}$<br>
          • <strong>Data Density:</strong> $\frac{12}{49} \times 100\% = \mathbf{24.48\%}$<br>
          <em>(เหตุผลที่อาจารย์ใช้สอนว่าทำไม Sparse Graph ต้องใช้ Adjacency List แทน Matrix)</em>
        </li>
        <li><strong>7.4 จำนวนเส้นเชื่อม Complete Graph 16 Vertices:</strong><br>
          $$E = \frac{V(V-1)}{2} = \frac{16 \times 15}{2} = \mathbf{120 \text{ เส้น}}$$
          <em>(ห้ามตอบ $16 \times 15 / 2$ ต้องตอบ 120 เท่านั้น)</em>
        </li>
        <li><strong>7.5 โหนดสูงสุดใน Binary Tree ความสูง $h = 10$:</strong><br>
          $$N_{\max} = 2^{h+1} - 1 = 2^{11} - 1 = 2048 - 1 = \mathbf{2047 \text{ โหนด}}$$
          <em>(ห้ามตอบ $2^{11}-1$ ต้องตอบ 2047 เท่านั้น)</em>
        </li>
        <li><strong>7.6 ข้อมูลใน Quicksort ที่ไม่ถูกนำไป Partition:</strong><br>
          คือ <strong>ข้อมูล 3 ตัวที่ทำ Median-of-Three</strong> ได้แก่ ตำแหน่ง <code>left</code>, <code>right</code>, และ <code>pivot</code> ที่เก็บไว้ที่ตำแหน่ง <code>right - 1</code> เพราะข้อมูลทั้ง 3 ตัวนี้ถูกเปรียบเทียบจัดเรียงล่วงหน้า และทำหน้าที่เป็นตัวกั้น (Sentinel guards) ป้องกัน pointer หลุดขอบอาร์เรย์แล้ว
        </li>
      </ul>
    </div>

  </div> <!-- END TAB 0 -->
"""
