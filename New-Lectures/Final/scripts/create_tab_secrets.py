# -*- coding: utf-8 -*-
"""
Script to create generate_tab_secrets.py containing the full 7-question exam suite
derived from teacher's secret voice leaks, in-class verbal warnings, and weird phrases
from Day 1 to the final lecture.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

content = r'''# -*- coding: utf-8 -*-
"""
Module to generate HTML for Tab 2: Teacher's Secret Warnings & Leaked Exam Suite (Set Secret)
Derived from verbatim audio transcripts, in-class projector leaks, and teacher warnings (Day 1 - Final Day)
"""

def get_tab_secrets_html():
    return r"""  <!-- ========================================================================= -->
  <!-- TAB: TEACHER'S SECRET WARNINGS & LEAKED EXAM SUITE (70 MARKS / HARVED TO 35)-->
  <!-- ========================================================================= -->
  <div id="tab-secrets" class="tab-content">
  <h1 class="section-heading" style="background: linear-gradient(135deg, #4f46e5, #312e81);">🎙️ ชุดที่ 2: แบบฝึกหัดเก็งคำพูดลับ &amp; กับดักจับผิด 0 คะแนน (Teacher's Secret Warnings &amp; Leaked Traps Suite - 7 ข้อใหญ่ 70 คะแนน)</h1>

  <!-- QUICK NAV FOR TAB SECRETS -->
  <div class="nav-jump-bar" style="border-left-color: #6366f1;">
    <span class="nav-jump-label" style="color: #4338ca;">⚡ ทางลัดข้อสอบชุดคำพูดลับอาจารย์:</span>
    <a href="#sec-q1" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 1 Hashing ชน 58 / กฎอ่านตาราง Rehash</a>
    <a href="#sec-q2" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 2 Heap DeleteMin 3 ครั้ง / Parent //</a>
    <a href="#sec-q3" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 3 Insertion Sort สูตร 1 นาที vs 1 ชม.</a>
    <a href="#sec-q4" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 4 Bubble &amp; Selection ใบงานจริง / range(0)</a>
    <a href="#sec-q5" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 5 Topological Sort ดักลูกศร vs จุลภาค</a>
    <a href="#sec-q6" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 6 Shortest Path Assignment 4 / Null Graph</a>
    <a href="#sec-q7" class="jump-pill" style="border-color:#818cf8; color:#3730a3;">ข้อ 7 รวมคำถามย่อยบน Notepad &amp; % RAM</a>
  </div>

  <div class="rules-box" style="background:#eef2ff; border-left-color:#6366f1;">
    <div class="rules-title" style="color:#3730a3;">🎙️ ที่มาและความสำคัญของข้อสอบชุดที่ 2 (Teacher's Secret Warnings Intelligence):</div>
    <p style="margin:4px 0; font-size:13.5px; color:#1e1b4b;">
      ข้อสอบชุดนี้สร้างขึ้นจากการแกะรอย <strong>ไฟล์เสียงบันทึกการสอนคำต่อคำ (Verbatim Transcripts) ตั้งแต่วันแรกถึงวันสุดท้าย</strong> รวมทั้งภาพถ่ายหน้าจอโปรเจกเตอร์ที่อาจารย์เปิดโปรแกรม Notepad ฉายขึ้นจอเวลา 11:54 น. ในคาบเรียนสุดท้าย โดยเน้นเจาะลึก <strong>"คำพูดลับที่อาจารย์แอบบอกหน้าห้อง", "จุดที่อาจารย์พูดแปลกๆ หรือพูดเตือนให้ระวัง", และ "กฎเหล็กที่ทำให้นิสิตได้ 0 คะแนนทันที"</strong> ซึ่งไม่เคยมีในสรุปทั่วไป!
    </p>
  </div>

  <!-- ========================================================================= -->
  <!-- QUESTION 1: HASHING & TEACHER SECRET TRAPS -->
  <!-- ========================================================================= -->
  <h2 id="sec-q1" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 1: Hashing, Collision Count Trap, and Rehashing Order (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงเสียงบรรยาย: 20260902_091736.aac (นาที 09:26, 10:10, 10:50) | ภาพกระดานสไลด์: IMG_20260826_120134, IMG_20260902_092629, IMG_20260902_105026</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>1.1 Linear Probing Collision Count Trap (อย่าตอบ 6!)</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 4 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty hash table of size $\text{TableSize} = 10$ using <strong>Linear Probing</strong> with hash function $h(k) = k \bmod 10$ and probe sequence formula:</p>
  $$h_i(k) = (h(k) + i) \bmod 10 \quad \text{for } i = 0, 1, 2, \dots$$
  <p>Insert the key sequence $\mathbf{\{89, 18, 49, 58, 69\}}$ sequentially into the table.</p>
  <ol type="a">
    <li>Fill the final 10-slot hash table array (indices 0 to 9).</li>
    <li>How many collisions occurred specifically during the insertion of key <strong>58</strong>? (Explain why answering 6 is strictly incorrect).</li>
    <li>What is the TOTAL number of collisions/probe resolutions for the entire sequence? (Explain why answering 14 is incorrect).</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดลับอาจารย์):</strong> กำหนดตารางแฮชว่างขนาด 10 ช่อง (ดัชนี 0 ถึง 9) ใช้วิธี Linear Probing โดย $h_i(k) = (k \bmod 10 + i) \bmod 10$ จงแทรกข้อมูล $89, 18, 49, 58, 69$ ตามลำดับ<br>
    <strong>🎙️ คำพูดจริงของอาจารย์ในห้องเรียน:</strong> <em>"จำนวนครั้งการชนของ 58 อย่าตอบว่า 6 นะครับ! ให้นับเฉพาะการชนของตัวมันเอง คือ ชน 18 (index 8), ชน 89 (index 9), ชน 49 (index 0) รวมชน 3 ครั้ง แล้วลงที่ช่องว่าง index 1... และจำนวนการชนรวมของตารางคือ 7 ครั้ง ไม่ใช่เอา ชน 7 + แก้ 7 = 14 ครั้งเด็ดขาด!"</em>
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 1.1: ตารางแฮชขนาด 10 ช่อง (ดัชนี 0 ถึง 9)</div>
    <table class="blank-table">
      <thead>
        <tr>
          <th>Slot</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="font-weight:bold; background:#f8fafc;">Key</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
      </tbody>
    </table>
    <div class="handwriting-line" style="margin-top:10px;">คำตอบข้อ b) จำนวนการชนของคีย์ 58: ................... ครั้ง เพราะ ..........................................................................................</div>
    <div class="handwriting-line">คำตอบข้อ c) จำนวนการชนรวมทั้งสิ้นของตาราง: ................... ครั้ง เพราะ ....................................................................................</div>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียดและวิเคราะห์จุดดัก 0 คะแนน (Solution 1.1)</summary>
    <div class="solution-box">
      <p><strong>ขั้นตอนการคำนวณทีละคีย์:</strong></p>
      <ul>
        <li><strong>ใส่ 89:</strong> $89 \bmod 10 = 9$ &rarr; ช่อง 9 ว่าง &rarr; <strong>ลงช่อง 9</strong> (ชน 0 ครั้ง)</li>
        <li><strong>ใส่ 18:</strong> $18 \bmod 10 = 8$ &rarr; ช่อง 8 ว่าง &rarr; <strong>ลงช่อง 8</strong> (ชน 0 ครั้ง)</li>
        <li><strong>ใส่ 49:</strong> $h(49) = 9$ &rarr; ชน 89 ที่ช่อง 9 ($i=0$) &rarr; $i=1: (9+1)\%10 = 0$ ว่าง &rarr; <strong>ลงช่อง 0</strong> (ชน 1 ครั้ง)</li>
        <li><strong>ใส่ 58:</strong> $h(58) = 8$ &rarr; ชน 18 ที่ช่อง 8 ($i=0$) &rarr; $i=1: (8+1)\%10 = 9$ ชน 89 &rarr; $i=2: (8+2)\%10 = 0$ ชน 49 &rarr; $i=3: (8+3)\%10 = 1$ ว่าง &rarr; <strong>ลงช่อง 1</strong> (ชน 3 ครั้ง)</li>
        <li><strong>ใส่ 69:</strong> $h(69) = 9$ &rarr; ชนช่อง 9, ชนช่อง 0, ชนช่อง 1 &rarr; $i=3: (9+3)\%10 = 2$ ว่าง &rarr; <strong>ลงช่อง 2</strong> (ชน 3 ครั้ง)</li>
      </ul>
      <p><strong>ตารางผลลัพธ์สุดท้าย:</strong></p>
      <table class="blank-table" style="max-width:650px;">
        <tr style="background:#f1f5f9;">
          <th>ดัชนี</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th>
        </tr>
        <tr>
          <td><strong>ข้อมูล</strong></td>
          <td style="color:#2563eb; font-weight:bold;">49</td>
          <td style="color:#b45309; font-weight:bold;">58</td>
          <td style="color:#15803d; font-weight:bold;">69</td>
          <td style="color:#94a3b8;">-</td><td style="color:#94a3b8;">-</td><td style="color:#94a3b8;">-</td><td style="color:#94a3b8;">-</td><td style="color:#94a3b8;">-</td>
          <td style="color:#1e293b; font-weight:bold;">18</td>
          <td style="color:#1e293b; font-weight:bold;">89</td>
        </tr>
      </table>
      <div class="note-box" style="margin-top:8px;">
        🚨 <strong>จุดเฉลยคำพูดอาจารย์:</strong>
        <br>• ข้อ b: คีย์ 58 ชน <strong>3 ครั้ง</strong> (ชนช่อง 8, 9, 0) <em>ห้ามตอบ 6 เด็ดขาด</em> เพราะเลข 6 มาจากการที่นิสิตเอายอดรวมสะสมก่อนหน้ามามั่ว
        <br>• ข้อ c: จำนวนการชนรวม $= 0 + 0 + 1 + 3 + 3 = \mathbf{7 \text{ ครั้ง}}$ <em>ห้ามตอบ 14</em> เพราะการชนกับการแก้การชนนับเป็นรอบเดียวกัน
      </div>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>1.2 Double Hashing $R$-Choice Trap &amp; Zero-Step Disaster</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 3 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> In Double Hashing with secondary hash function $h_2(k) = R - (k \bmod R)$ and table size $\text{TableSize} = 11$:</p>
  <ol type="a">
    <li>What is the exact integer value of $R$?</li>
    <li>Explain why $R$ <strong>CANNOT</strong> be chosen as $11$, even though $11$ is a prime number. What disastrous runtime error happens if $R = 11$ when hashing a multiple of 11 (e.g., $k = 22$)?</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดลับอาจารย์):</strong> สำหรับ Double Hashing ที่มีขนาดตาราง 11 ช่อง ($M = 11$) และสูตร $h_2(k) = R - (k \bmod R)$<br>
    <strong>🎙️ คำพูดจริงของอาจารย์ในห้องเรียน:</strong> <em>"นิยามบอกว่า R คือจำนวนเฉพาะที่มากที่สุด แต่ต้องน้อยกว่า TableSize อย่างเด็ดขาด (less than) ห้ามเท่ากับ 11 นะครับ! ถ้าใครตอบ R = 11 แล้วเจอเลขอย่าง 22 หรือ 33 ลองคิดดู: 22 mod 11 ได้ 0 ทำให้ก้าวเดิน R - 0 = 11 mod 11 กลายเป็น 0 ก้าว ตกช่องเดิมตลอดกาล เกิด Infinite Loop ติดลูปไม่รู้จบ โปรแกรมค้างทันที!"</em>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 1.2)</summary>
    <div class="solution-box">
      <p><strong>คำตอบ:</strong></p>
      <ul>
        <li><strong>ข้อ a) ค่าของ $R$:</strong> $\mathbf{R = 7}$ (จำนวนเฉพาะที่มากที่สุดที่ $R < 11$ คือ 7)</li>
        <li><strong>ข้อ b) สาเหตุที่ห้ามเลือก $R = 11$:</strong> เพราะหากเลือก $R = 11$ เมื่อข้อมูลมีค่าที่เป็นพหุคูณของ 11 (เช่น $k = 22, 33, 44$) จะได้ $k \bmod 11 = 0$ ส่งผลให้ $h_2(k) = 11 - 0 = 11$ เมื่อนำไปคูณกับ $i$ ในการขยับ Probe:
        $$h_i(k) = (h_0(k) + i \times 11) \bmod 11 = (h_0(k) + 0) \bmod 11 = h_0(k)$$
        ระยะก้าวจะมีค่าเป็น <strong>0 (Zero Step)</strong> ทำให้โพรบตกที่ช่องเดิมซ้ำซาก เกิด <strong>Infinite Loop (วนลูปไม่รู้จบ)</strong> จนโปรแกรมแฮงก์!</li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>1.3 Rehashing Order-of-Reading Trap (กฎอ่านจากบนลงล่าง)</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 3 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> An old hash table of size $7$ contains the following keys in its slots: Slot 0: `6`, Slot 1: `15`, Slot 3: `24`, Slot 6: `13`. When inserting a new key `23`, the load factor exceeds 70%, triggering a <strong>Rehashing</strong> operation.</p>
  <ol type="a">
    <li>What is the new table size $\text{TableSize}_{\text{new}}$? Show the rule.</li>
    <li><strong>CRUCIAL EXAM RULE:</strong> In what exact sequential order must elements be extracted from the old table and inserted into the new table? (Show why reading from original input $\{13, 15, 24, 6\}$ results in 0 score).</li>
    <li>Fill the new hash table of size 17 using $h(k) = k \bmod 17$ and Linear Probing.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; กับดัก 0 คะแนน):</strong> ตารางเดิมขนาด 7 ช่อง มีข้อมูล ช่อง 0: 6, ช่อง 1: 15, ช่อง 3: 24, ช่อง 6: 13 เมื่อแทรก 23 ตารางเกินเกณฑ์ 70% จึงต้อง Rehash<br>
    <strong>🚨 กับดักที่ทำให้นิสิตได้ 0 คะแนนมากที่สุด:</strong> เวลาดึงข้อมูลจากตารางเดิมเข้าตารางใหม่ <strong>ต้องกวาดอ่านตามลำดับช่องในตารางเดิมจากบนลงล่าง (Index 0, 1, 2, ...) คือ 6, 15, 24, 13 แล้วตามด้วย 23</strong> ห้ามดึงตามลำดับโจทย์เดิม (13, 15, 24, 6) เด็ดขาด เพราะในหน่วยความจำจริง คอมพิวเตอร์ไม่รู้ประวัติการ Insert ในอดีต มีแต่อาร์เรย์ปัจจุบัน!
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 1.3)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a) ขนาดตารางใหม่:</strong> $2 \times 7 = 14$ &rarr; จำนวนเฉพาะที่น้อยที่สุดที่ $\ge 14$ คือ $\mathbf{17}$ ($\text{TableSize}_{\text{new}} = 17$)</li>
        <li><strong>ข้อ b) ลำดับการอ่านข้อมูล:</strong> ต้องอ่านจากช่อง 0 ลงไปช่อง 6 ได้ลำดับ: $\mathbf{6, 15, 24, 13}$ แล้วตามด้วยตัวใหม่ $\mathbf{23}$ (หากอ่าน $13, 15, 24, 6$ อาจารย์ปรับเป็น 0 คะแนนทันที)</li>
        <li><strong>ข้อ c) การคำนวณใส่ตารางใหม่ขนาด 17 ($x \bmod 17$):</strong>
          <br>• <strong>6:</strong> $6 \bmod 17 = 6$ &rarr; <strong>ลงช่อง 6</strong>
          <br>• <strong>15:</strong> $15 \bmod 17 = 15$ &rarr; <strong>ลงช่อง 15</strong>
          <br>• <strong>24:</strong> $24 \bmod 17 = 7$ &rarr; <strong>ลงช่อง 7</strong>
          <br>• <strong>13:</strong> $13 \bmod 17 = 13$ &rarr; <strong>ลงช่อง 13</strong>
          <br>• <strong>23:</strong> $23 \bmod 17 = 6$ &rarr; ชนกับ 6 ที่ช่อง 6 &rarr; $(6+1)\%17 = 7$ ชนกับ 24 &rarr; $(6+2)\%17 = 8$ ว่าง &rarr; <strong>ลงช่อง 8</strong>
        </li>
      </ul>
      <p><strong>ผลลัพธ์ในตารางใหม่ 17 ช่อง:</strong> ช่อง 6: `6`, ช่อง 7: `24`, ช่อง 8: `23`, ช่อง 13: `13`, ช่อง 15: `15` (ช่องอื่นๆ ว่าง)</p>
    </div>
  </details>

  <!-- ========================================================================= -->
  <!-- QUESTION 2: BINARY HEAP & 3 CONSECUTIVE DELETEMIN -->
  <!-- ========================================================================= -->
  <h2 id="sec-q2" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 2: Binary Min-Heap — Leaked 3-Consecutive DeleteMin &amp; Python Traps (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงเสียงบรรยาย: dsa20260909_092303.aac (นาที 09:41-11:57), 20260909_103704.aac | ภาพกระดานสไลด์: IMG_20260909_094140, IMG_20260909_110606, IMG_20260909_115719</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>2.1 Floor Division `//` and Sentinel Index 0 Rule</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 2 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> In the Python implementation of class `BinaryHeap`:</p>
  <pre style="background:#1e1e2e; color:#cdd6f4; padding:10px; border-radius:6px; font-family:'JetBrains Mono', Consolas, monospace; font-size:12.5px;">self.array = [None] * (capacity + 1)</pre>
  <ol type="a">
    <li>Why must Index 0 be reserved as a sentinel (`None`) instead of storing the Root node? What happens mathematically to formula $2i$ if $\text{Root}$ is placed at index 0?</li>
    <li>When finding the Parent of a node at index 7: Explain why in Python we must write `7 // 2 = 3` and why calculating `7 / 2 = 3.5` and rounding up to 4 results in 0 score.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดอาจารย์):</strong> ในการสร้างคลาส BinaryHeap ในภาษา Python ทำไมช่อง 0 ต้องใส่ `None` และการหา Parent ของโหนดที่ 7 ทำไมต้องตัดเศษทิ้ง `7 // 2 = 3` ปัดเป็น 4 ผิดทันที?
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 2.1)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a):</strong> หากใส่ Root ที่ Index 0 สูตรลูกซ้าย $2i$ จะกลายเป็น $2 \times 0 = 0$ ซึ่งวนกลับมาที่ตัวเอง ทำให้ความสัมพันธ์พังทลายทันที จึงต้องเว้นช่อง 0 ไว้เพื่อให้ Root เริ่มที่ Index 1 เสมอ ($2 \times 1 = 2, 2 \times 1 + 1 = 3$)</li>
        <li><strong>ข้อ b):</strong> โหนดดัชนี 7 เป็นลูกขวาของโหนด 3 สูตร Parent ทางคณิตศาสตร์คือ $\lfloor i / 2 \rfloor$ (ปัดเศษทิ้ง) ได้ $7 // 2 = \mathbf{3}$ หากนิสิตปัดเศษขึ้นเป็น 4 จะได้โหนด 4 ซึ่งผิดโครงสร้างครอบครัวและได้ 0 คะแนนทันที</li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>2.2 🚨 THE LEAKED FINAL EXAM PROBLEM: Three Consecutive `deleteMin()` Operations</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 8 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the following 11-element Binary Min-Heap stored in a 1D Python Array (index 1 to 11):</p>
  <table class="blank-table" style="max-width:700px; margin:8px 0;">
    <tr style="background:#1e293b; color:#fff;">
      <th>Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th>
    </tr>
    <tr>
      <td><strong>Value</strong></td>
      <td style="color:#94a3b8;">None</td><td>13</td><td>14</td><td>16</td><td>24</td><td>21</td><td>19</td><td>68</td><td>65</td><td>26</td><td>32</td><td>31</td>
    </tr>
  </table>
  <p>Execute <strong>THREE consecutive `deleteMin()`</strong> operations on this heap. For each operation, specify:</p>
  <ol>
    <li>The minimum element deleted and returned.</li>
    <li>The path of the `hole` moving down during Percolate Down (showing comparisons with smaller child).</li>
    <li>The resulting array state after that `deleteMin()`.</li>
  </ol>
  <p>Fill the final resulting array into the answer boxes below.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดรั่วจากอาจารย์):</strong> กำหนด Binary Min-Heap เริ่มต้น 11 สมาชิก จงแสดงการทำ <code>deleteMin()</code> <strong>ติดต่อกัน 3 ครั้ง!</strong><br>
    <strong>🎙️ คำพูดจริงของอาจารย์ในห้องเรียน (9 ก.ย. 2569 เวลา 11:57 น.):</strong> <em>"การบ้านในคาบ อาจารย์ให้ทำ deleteMin แค่ 1 ครั้ง แต่ในข้อสอบปลายภาคจริง 10 คะแนน อาจารย์จะออก deleteMin 3 ครั้งติดต่อกัน! ใครมัวไล่โค้ดทีละบรรทัดทำไม่ทันแน่นอน ให้วาดรูป Tree บนกระดาษทด ดึง Root ออก เอาตัวล่างขวามาแทน แล้วสลับกับลูกตัวที่น้อยกว่าลงไป ทำ 3 รอบ แล้วแปลงกลับเป็น Array มาเขียนลงช่องคำตอบ!"</em>
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 2.2: สถานะ Array หลังจบ `deleteMin()` ครั้งที่ 3 (ขนาดเหลือ 8 สมาชิก)</div>
    <table class="blank-table">
      <thead>
        <tr>
          <th>Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="font-weight:bold; background:#f8fafc;">Value</td>
          <td style="background:#e2e8f0; color:#64748b;">None</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          <td style="background:#f1f5f9; color:#cbd5e1;">-</td>
          <td style="background:#f1f5f9; color:#cbd5e1;">-</td>
          <td style="background:#f1f5f9; color:#cbd5e1;">-</td>
        </tr>
      </tbody>
    </table>
    <div class="handwriting-line" style="margin-top:10px;">Root ที่ถูกลบออก: ครั้งที่ 1 = ..........., ครั้งที่ 2 = ..........., ครั้งที่ 3 = ...........</div>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียดการลบ 3 ครั้งติดต่อกัน (Solution 2.2)</summary>
    <div class="solution-box">
      <p><strong>เริ่มต้น:</strong> Array ขนาด 11 ตัว: `[-, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31]`</p>

      <p><strong>🔹 การทำ `deleteMin()` ครั้งที่ 1:</strong></p>
      <ul>
        <li><strong>ลบ Root:</strong> นำ `13` ออก, ตัวท้ายสุดคือ `temp = 31` (ช่อง 11 ตัดทิ้ง, ขนาดเหลือ 10)</li>
        <li><strong>Percolate Down:</strong> หลุมอยู่ที่ 1
          <br>&bull; รอบ 1: ลูกของ 1 คือ 2 (ค่า 14) และ 3 (ค่า 16) &rarr; เลือกลูกน้อยคือ 14 &rarr; $14 < 31$ จริง &rarr; 14 ขึ้นมาที่ช่อง 1, หลุมเลื่อนไปช่อง 2
          <br>&bull; รอบ 2: ลูกของ 2 คือ 4 (ค่า 24) และ 5 (ค่า 21) &rarr; เลือกลูกน้อยคือ 21 &rarr; $21 < 31$ จริง &rarr; 21 ขึ้นมาที่ช่อง 2, หลุมเลื่อนไปช่อง 5
          <br>&bull; รอบ 3: ลูกของ 5 คือ 10 (ค่า 32, ไม่มีลูกขวา) &rarr; $32 < 31$ เท็จ &rarr; หยุดลูป!
          <br>&bull; นำ `temp = 31` ใส่ช่อง 5
        </li>
        <li><strong>Array หลังครั้งที่ 1 (ขนาด 10):</strong> <code>[-, 14, 21, 16, 24, 31, 19, 68, 65, 26, 32]</code> (ส่งคืน 13)</li>
      </ul>

      <p><strong>🔹 การทำ `deleteMin()` ครั้งที่ 2:</strong></p>
      <ul>
        <li><strong>ลบ Root:</strong> นำ `14` ออก, ตัวท้ายสุดคือ `temp = 32` (ช่อง 10 ตัดทิ้ง, ขนาดเหลือ 9)</li>
        <li><strong>Percolate Down:</strong> หลุมอยู่ที่ 1
          <br>&bull; รอบ 1: ลูกของ 1 คือ 2 (ค่า 21) และ 3 (ค่า 16) &rarr; เลือกลูกน้อยคือ 16 &rarr; $16 < 32$ จริง &rarr; 16 ขึ้นมาที่ช่อง 1, หลุมเลื่อนไปช่อง 3
          <br>&bull; รอบ 2: ลูกของ 3 คือ 6 (ค่า 19) และ 7 (ค่า 68) &rarr; เลือกลูกน้อยคือ 19 &rarr; $19 < 32$ จริง &rarr; 19 ขึ้นมาที่ช่อง 3, หลุมเลื่อนไปช่อง 6
          <br>&bull; รอบ 3: ลูกของ 6 คือ $2 \times 6 = 12 > 9$ (ไม่มีลูก) &rarr; หลุดลูป!
          <br>&bull; นำ `temp = 32` ใส่ช่อง 6
        </li>
        <li><strong>Array หลังครั้งที่ 2 (ขนาด 9):</strong> <code>[-, 16, 21, 19, 24, 31, 32, 68, 65, 26]</code> (ส่งคืน 14)</li>
      </ul>

      <p><strong>🔹 การทำ `deleteMin()` ครั้งที่ 3:</strong></p>
      <ul>
        <li><strong>ลบ Root:</strong> นำ `16` ออก, ตัวท้ายสุดคือ `temp = 26` (ช่อง 9 ตัดทิ้ง, ขนาดเหลือ 8)</li>
        <li><strong>Percolate Down:</strong> หลุมอยู่ที่ 1
          <br>&bull; รอบ 1: ลูกของ 1 คือ 2 (ค่า 21) และ 3 (ค่า 19) &rarr; เลือกลูกน้อยคือ 19 &rarr; $19 < 26$ จริง &rarr; 19 ขึ้นมาที่ช่อง 1, หลุมเลื่อนไปช่อง 3
          <br>&bull; รอบ 2: ลูกของ 3 คือ 6 (ค่า 32) และ 7 (ค่า 68) &rarr; เลือกลูกน้อยคือ 32 &rarr; $32 < 26$ เท็จ &rarr; หยุดลูปทันที!
          <br>&bull; นำ `temp = 26` ใส่ช่อง 3
        </li>
        <li><strong>Array หลังครั้งที่ 3 (ขนาด 8 - คำตอบสุดท้าย):</strong>
          <br><code style="font-size:14px; font-weight:bold; color:#15803d;">[-, 19, 21, 26, 24, 31, 32, 68, 65]</code> (ส่งคืน 16)
        </li>
      </ul>
    </div>
  </details>

  <!-- ========================================================================= -->
  <!-- QUESTION 3: INSERTION SORT & 1-MINUTE ARITHMETIC SHORTCUT -->
  <!-- ========================================================================= -->
  <h2 id="sec-q3" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 3: Insertion Sort Tracing &amp; The 1-Minute Arithmetic Shortcut (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงเสียงบรรยาย: 20260916_092007.aac (นาที 09:48-10:20) | ภาพกระดาน: IMG_20260916_094820, IMG_20260916_095318, IMG_20260916_095816</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>3.1 Step-by-Step Pass Tracing on Original Array</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 5 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the initial array: $\mathbf{[34, 8, 64, 51, 32, 21]}$ ($N = 6$). Trace the execution of <strong>Insertion Sort</strong> for each pass $p = 1, 2, 3, 4, 5$. Fill the table with the value of `temp`, the number of Position Moves in each pass, and the array state after each pass.</p>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">📝 ตารางจำลองคำตอบข้อ 3.1: Insertion Sort Tracing</div>
    <table class="blank-table">
      <thead>
        <tr>
          <th>Pass ($p$)</th><th>`temp`</th><th>Position Moves</th><th>Array State After Pass</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Original</td><td>-</td><td>-</td><td>[34, 8, 64, 51, 32, 21]</td></tr>
        <tr><td>$p = 1$</td><td></td><td></td><td></td></tr>
        <tr><td>$p = 2$</td><td></td><td></td><td></td></tr>
        <tr><td>$p = 3$</td><td></td><td></td><td></td></tr>
        <tr><td>$p = 4$</td><td></td><td></td><td></td></tr>
        <tr><td>$p = 5$</td><td></td><td></td><td></td></tr>
      </tbody>
    </table>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยตาราง Trace (Solution 3.1)</summary>
    <div class="solution-box">
      <table class="blank-table">
        <tr style="background:#f1f5f9;">
          <th>Pass ($p$)</th><th>`temp`</th><th>Position Moves</th><th>Array State After Pass</th>
        </tr>
        <tr><td>Original</td><td>-</td><td>-</td><td>[34, 8, 64, 51, 32, 21]</td></tr>
        <tr><td><strong>p = 1</strong></td><td>8</td><td><strong>1</strong> (34 เลื่อนขวา)</td><td>[8, 34, 64, 51, 32, 21]</td></tr>
        <tr><td><strong>p = 2</strong></td><td>64</td><td><strong>0</strong> (64 &gt; 34 ไม่เลื่อน)</td><td>[8, 34, 64, 51, 32, 21]</td></tr>
        <tr><td><strong>p = 3</strong></td><td>51</td><td><strong>1</strong> (64 เลื่อนขวา)</td><td>[8, 34, 51, 64, 32, 21]</td></tr>
        <tr><td><strong>p = 4</strong></td><td>32</td><td><strong>3</strong> (64, 51, 34 เลื่อนขวา)</td><td>[8, 32, 34, 51, 64, 21]</td></tr>
        <tr><td><strong>p = 5</strong></td><td>21</td><td><strong>4</strong> (64, 51, 34, 32 เลื่อน)</td><td>[8, 21, 32, 34, 51, 64]</td></tr>
      </table>
      <p style="margin-top:6px;"><strong>รวมจำนวน Position Moves ตลอดการทำงาน:</strong> $1 + 0 + 1 + 3 + 4 = \mathbf{9 \text{ ครั้ง}}$</p>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>3.2 🎙️ The 1-Minute vs 1-Hour Arithmetic Series Shortcut</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 5 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Suppose the input array is sorted in <strong>Reverse Order (Worst Case)</strong>:</p>
  $$\mathbf{[64, 51, 34, 32, 21, 8]} \quad (N = 6)$$
  <ol type="a">
    <li>What is the total number of Position Moves? Write the closed-form arithmetic series formula and calculate the exact numerical result.</li>
    <li>If the exam provides a reverse-sorted array of size $\mathbf{N = 8}$, how many total Position Moves occur?</li>
    <li>If the exam provides a reverse-sorted array of size $\mathbf{N = 10}$, how many total Position Moves occur?</li>
    <li>What is the total number of Position Moves in the <strong>Best Case</strong> (array already in ascending order)? What is its Time Complexity?</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดอาจารย์):</strong> หากข้อมูลเรียงกลับทิศทาง (มากไปหาน้อย - Worst Case) จงคำนวณจำนวน Position Moves ของ $N=6, N=8, N=10$<br>
    <strong>🎙️ คำพูดจริงของอาจารย์ในห้องเรียน:</strong> <em>"คนที่มองอนุกรมออก จะใช้เวลาทำข้อสอบข้อนี้เพียง 1 นาที แต่คนที่ไม่รู้นั่งไล่โปรแกรมทีละรอบจะเสียเวลาไปเกือบ 1 ชั่วโมงเต็ม! สูตรคือ $1 + 2 + 3 + ... + (N-1) = \frac{N(N-1)}{2}$ ถ้า 6 ตัวคือ 15 ครั้ง, ถ้า 8 ตัวคือ 28 ครั้ง, ถ้า 10 ตัวคือ 45 ครั้ง!"</em>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 3.2)</summary>
    <div class="solution-box">
      <p><strong>เฉลยสูตรลัด 1 นาที:</strong></p>
      <ul>
        <li><strong>ข้อ a) สำหรับ $N = 6$:</strong>
          $$\text{Moves} = 1 + 2 + 3 + 4 + 5 = \frac{6 \times (6 - 1)}{2} = \frac{30}{2} = \mathbf{15 \text{ ครั้ง}}$$
        </li>
        <li><strong>ข้อ b) สำหรับ $N = 8$:</strong>
          $$\text{Moves} = \frac{8 \times 7}{2} = \frac{56}{2} = \mathbf{28 \text{ ครั้ง}}$$
        </li>
        <li><strong>ข้อ c) สำหรับ $N = 10$:</strong>
          $$\text{Moves} = \frac{10 \times 9}{2} = \frac{90}{2} = \mathbf{45 \text{ ครั้ง}}$$
        </li>
        <li><strong>ข้อ d) กรณี Best Case:</strong> Position Moves $= \mathbf{0 \text{ ครั้ง}}$ (ไม่มีการเลื่อนเลย), Time Complexity $= \mathbf{O(N)}$</li>
      </ul>
    </div>
  </details>

  <!-- ========================================================================= -->
  <!-- QUESTION 4: BUBBLE & SELECTION SORT & RANGE(0) TRAP -->
  <!-- ========================================================================= -->
  <h2 id="sec-q4" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 4: Bubble Sort Quiz Breakdown &amp; The `range(0)` Python Trap (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงเสียงบรรยาย: 20260916_092007.aac (นาที 10:20-11:29) | ภาพใบงานจริง: IMG_20260916_112712 (ใบงานนักศึกษา ภาภวินท์ ฐิติชยานันท์)</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>4.1 In-Class Quiz Bubble Sort 5-Subquestion Analysis</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 6 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the initial array from the in-class assignment: $\mathbf{[64, 34, 25, 12, 22, 11, 90]}$ ($N = 7$). Answer the 5 questions exactly as tested in class:</p>
  <ol>
    <li>What is the total number of passes required to complete the algorithm?</li>
    <li>Calculate the <strong>Total Number of Swaps</strong> using <strong>Inversion Counting Theory</strong> without tracing loops. (Show individual inversion counts for each number).</li>
    <li>What is the array state in <strong>Pass 1 at Step 4</strong> (after comparing 64 and 22)?</li>
    <li>What is the array state immediately after <strong>Pass 1 completes</strong>?</li>
    <li>How many swaps occurred during <strong>Pass 1</strong>?</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> ข้อสอบจากใบงานจริงในห้องเรียน อาร์เรย์ `[64, 34, 25, 12, 22, 11, 90]` จงตอบคำถาม 5 ข้อย่อย โดยข้อ 2 ให้ใช้ทฤษฎีการนับ Inversion
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด 5 ข้อย่อย (Solution 4.1)</summary>
    <div class="solution-box">
      <p><strong>เฉลยทั้ง 5 ข้อย่อย:</strong></p>
      <ol>
        <li><strong>จำนวน Pass ทั้งหมด:</strong> $N - 1 = 7 - 1 = \mathbf{6 \text{ passes}}$</li>
        <li><strong>จำนวน Swap ทั้งหมดด้วยทฤษฎีนับ Inversion:</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 64: (34, 25, 12, 22, 11) &rarr; <strong>5 ตัว</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 34: (25, 12, 22, 11) &rarr; <strong>4 ตัว</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 25: (12, 22, 11) &rarr; <strong>3 ตัว</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 12: (11) &rarr; <strong>1 ตัว</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 22: (11) &rarr; <strong>1 ตัว</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 11: ไม่มี &rarr; <strong>0 ตัว</strong>
          <br>• นับตัวทางขวาที่น้อยกว่า 90: ไม่มี &rarr; <strong>0 ตัว</strong>
          <br>&rArr; <strong>Total Swaps</strong> $= 5 + 4 + 3 + 1 + 1 + 0 + 0 = \mathbf{14 \text{ swaps}}$ (ตรงกับการ Trace 100%)
        </li>
        <li><strong>สถานะ Array ใน Pass 1 ขั้นตอนย่อยที่ 4:</strong> <code>[34, 25, 12, 64, 22, 11, 90]</code></li>
        <li><strong>สถานะ Array เมื่อจบ Pass 1:</strong> <code>[34, 25, 12, 22, 11, 64, 90]</code> (เลข 90 ลอยไปขวาสุด)</li>
        <li><strong>จำนวนการสลับ (Swaps) ใน Pass 1:</strong> <strong>5 ครั้ง</strong></li>
      </ol>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>4.2 Selection Sort vs Bubble Sort Swap Trade-off &amp; Python `range(0)` Trap</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 4 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong></p>
  <ol type="a">
    <li>Why is <strong>Selection Sort</strong> preferred over Bubble Sort when writing to memory (swapping elements) is extremely expensive? What is the maximum number of swaps in Selection Sort vs Bubble Sort for $N$ elements?</li>
    <li><strong>Teacher's Python Trap:</strong> Does `range(0)` evaluate to `None` or `[0]`? Explain its true data type, metadata (`start`, `stop`, `step`), and why its memory allocation differs fundamentally from `[]` (empty list).</li>
  </ol>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 4.2)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a):</strong> เพราะ Selection Sort ทำการ Swap มากที่สุดเพียง <strong>$N - 1$ ครั้ง ($O(N)$ swaps)</strong> (สลับรอบละ 1 ครั้งเท่านั้น) ในขณะที่ Bubble Sort อาจต้อง Swap มากถึง <strong>$\frac{N(N-1)}{2}$ ครั้ง ($O(N^2)$ swaps)</strong> ดังนั้นเมื่อต้นทุนการเขียนหน่วยความจำสูง (เช่น Flash memory หรือ EEPROM) Selection Sort จึงมีประสิทธิภาพเหนือกว่าอย่างมาก</li>
        <li><strong>ข้อ b) จุดดัก `range(0)`:</strong> `range(0)` <strong>ไม่ใช่ `None` และไม่ใช่ `[0]`</strong> แต่เป็น <strong>Empty Sequence Object</strong> ของคลาส `range` ซึ่งเก็บเพียง Metadata 3 ค่าคือ `start = 0, stop = 0, step = 1` โดยไม่จองเนื้อที่ใน Heap Memory ต่างจาก `[]` (Empty List) ที่ระบบต้องทำการ Allocate List Header Object จริงในหน่วยความจำ</li>
      </ul>
    </div>
  </details>

  <!-- ========================================================================= -->
  <!-- QUESTION 5: TOPOLOGICAL SORT & ARROW VS COMMA TRAP -->
  <!-- ========================================================================= -->
  <h2 id="sec-q5" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 5: Topological Sort — Ground Null $\perp$, Indegree Table &amp; Comma Rule (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงเสียงบรรยาย: 20260923_091645.aac, 20261007_092525.aac | ภาพใบงานจริง: IMG_20261017_010732, IMG_20261017_010659, IMG_20261017_010740</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>5.1 Adjacency List with Ground Terminator $\perp$ and Full Indegree Trace</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the DAG with 7 vertices ($v_1$ to $v_7$) and edges: $(v_1, v_2), (v_1, v_3), (v_1, v_4), (v_2, v_4), (v_2, v_5), (v_3, v_6), (v_4, v_3), (v_4, v_6), (v_4, v_7), (v_5, v_4), (v_5, v_7), (v_7, v_6)$.</p>
  <ol type="a">
    <li>Draw the Adjacency List for the graph. Explain what the electrical ground symbol $\mathbf{\perp}$ (or `-||`) at the end of each linked list represents.</li>
    <li>Fill the Indegree Reduction Table across Initial and Rounds 1 to 7 with strikethroughs of reduced indegrees.</li>
    <li>Trace the vertical Queue $Q$ indexed from `[6]` down to `[0]` with `Front` and `Back` pointers, and loop variables $V=$ and $W=$.</li>
    <li><strong>CRITICAL GRADING RULE:</strong> Write the final Topological Order. Explain why writing arrows ($v_1 \to v_2 \to \dots$) results in an <strong>immediate 0 score</strong>, while comma separation ($v_1, v_2, \dots$) receives full marks.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดอาจารย์):</strong> จงแปลง DAG เป็น Adjacency List เติมตาราง Indegree ครบ 7 รอบ ไล่คิวแนวตั้ง และเขียนคำตอบ Topological Order<br>
    <strong>🚨 คำพูดเตือนสติของอาจารย์:</strong> <em>"การเขียนคำตอบ ให้คั่นด้วยเครื่องหมายจุลภาคเท่านั้น ห้ามเขียนหัวลูกศรเด็ดขาด! เพราะในนิยามคณิตศาสตร์ระบุเป็น Sequence of vertices การเขียนลูกศรจะกลายเป็นการเขียน Edge ซึ่งผิดนิยามและโดนปรับ 0 ทันที!"</em>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 5.1)</summary>
    <div class="solution-box">
      <p><strong>ข้อ a) Adjacency List พร้อมสัญลักษณ์ $\perp$ (Null Ground Terminator):</strong></p>
      <pre style="background:#0f172a; color:#f8fafc; padding:10px; border-radius:6px; font-family:'JetBrains Mono', Consolas, monospace; font-size:13px;">
Index [1] -> [ 2 ] -> [ 3 ] -> [ 4 ] -> ⟂
Index [2] -> [ 4 ] -> [ 5 ] -> ⟂
Index [3] -> [ 6 ] -> ⟂
Index [4] -> [ 3 ] -> [ 6 ] -> [ 7 ] -> ⟂
Index [5] -> [ 4 ] -> [ 7 ] -> ⟂
Index [6] -> ⟂
Index [7] -> [ 6 ] -> ⟂</pre>
      <p><em>สัญลักษณ์ $\perp$ หมายถึง Ground / NULL Pointer บ่งบอกจุดสิ้นสุดของ Linked List ในแถวนั้นๆ</em></p>

      <p><strong>ข้อ b) ตาราง Indegree ครบ 7 รอบ:</strong></p>
      <table class="blank-table">
        <tr style="background:#f1f5f9;">
          <th>Vertex</th><th>เริ่มต้น</th><th>รอบ 1</th><th>รอบ 2</th><th>รอบ 3</th><th>รอบ 4</th><th>รอบ 5</th><th>รอบ 6</th><th>รอบ 7</th>
        </tr>
        <tr><td><strong>v1</strong></td><td>0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
        <tr><td><strong>v2</strong></td><td>1</td><td><del>1</del> <strong>0</strong></td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
        <tr><td><strong>v3</strong></td><td>2</td><td><del>2</del> 1</td><td>1</td><td>1</td><td><del>1</del> <strong>0</strong></td><td>-</td><td>-</td><td>-</td></tr>
        <tr><td><strong>v4</strong></td><td>3</td><td><del>3</del> 2</td><td><del>2</del> 1</td><td><del>1</del> <strong>0</strong></td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
        <tr><td><strong>v5</strong></td><td>1</td><td>1</td><td><del>1</del> <strong>0</strong></td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
        <tr><td><strong>v6</strong></td><td>3</td><td>3</td><td>3</td><td>3</td><td><del>3</del> 2</td><td><del>2</del> 1</td><td>1</td><td><del>1</del> <strong>0</strong></td></tr>
        <tr><td><strong>v7</strong></td><td>2</td><td>2</td><td>2</td><td><del>2</del> 1</td><td><del>1</del> <strong>0</strong></td><td>-</td><td>-</td><td>-</td></tr>
      </table>

      <p><strong>ข้อ c) ลำดับการประมวลผล Queue และตัวแปรลูป:</strong></p>
      <ul>
        <li>รอบ 1: Dequeue $V = v_1$, เพื่อนบ้าน $W \in \{v_2, v_3, v_4\}$ &rarr; $v_2$ indegree $= 0$ &rarr; Enqueue $v_2$</li>
        <li>รอบ 2: Dequeue $V = v_2$, เพื่อนบ้าน $W \in \{v_4, v_5\}$ &rarr; $v_5$ indegree $= 0$ &rarr; Enqueue $v_5$</li>
        <li>รอบ 3: Dequeue $V = v_5$, เพื่อนบ้าน $W \in \{v_4, v_7\}$ &rarr; $v_4$ indegree $= 0$ &rarr; Enqueue $v_4$</li>
        <li>รอบ 4: Dequeue $V = v_4$, เพื่อนบ้าน $W \in \{v_3, v_6, v_7\}$ &rarr; $v_3, v_7$ indegree $= 0$ &rarr; Enqueue $v_3, v_7$</li>
        <li>รอบ 5: Dequeue $V = v_3$, เพื่อนบ้าน $W \in \{v_6\}$ (indegree v6 เหลือ 1)</li>
        <li>รอบ 6: Dequeue $V = v_7$, เพื่อนบ้าน $W \in \{v_6\}$ &rarr; $v_6$ indegree $= 0$ &rarr; Enqueue $v_6$</li>
        <li>รอบ 7: Dequeue $V = v_6$, ไม่มีเพื่อนบ้าน &rarr; จบการทำงาน</li>
      </ul>

      <p><strong>ข้อ d) ผลลัพธ์ Topological Order ที่ถูกต้องตามกฎ:</strong></p>
      <div class="note-box" style="border-left-color:#15803d; background:#f0fdf4;">
        ✅ <strong>คำตอบที่ได้คะแนนเต็ม:</strong> <span style="font-size:15px; font-weight:bold; color:#15803d;">v1, v2, v5, v4, v3, v7, v6</span> (หรือใส่ในวงเล็บ `(v1, v2, v5, v4, v3, v7, v6)`)
        <br>❌ <strong>คำตอบที่ได้ 0 คะแนน:</strong> <code>v1 -> v2 -> v5 -> v4 -> v3 -> v7 -> v6</code> (ห้ามใส่หัวลูกศรเด็ดขาด!)
      </div>
    </div>
  </details>

  <!-- ========================================================================= -->
  <!-- QUESTION 6: UNWEIGHTED SHORTEST PATH & ASSIGNMENT 4 -->
  <!-- ========================================================================= -->
  <h2 id="sec-q6" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 6: Unweighted Shortest Path — Assignment 4 &amp; The Null Graph Trap (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงเสียงบรรยาย: 20261007_092525.aac (Assignment 4) | ภาพถ่ายจริง: IMG_20261007_114532, IMG_20260923_103822</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>6.1 Assignment 4 Full Table Trace (Source = Vertex A)</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 7 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the directed graph from <strong>Assignment 4</strong> with vertices $A, B, C, D, E, F, G$ and start vertex $\mathbf{A}$. Edges: $A \to B, C; B \to G, E, C; C \to E, D; D \to F, A; E \to D, F; F \to \perp; G \to E$.</p>
  <p>Fill the processing table with columns `Known`, `Dist (dv)`, and `Path (pv)` (initial distance: $0$ for start vertex, $999/\infty$ for others). Show all strikethroughs and trace the Queue state.</p>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 6.1: ตารางประมวลผล Shortest Path (เริ่มต้น A)</div>
    <table class="blank-table">
      <thead>
        <tr>
          <th>Vertex</th><th>Known (T/F)</th><th>Dist ($d_v$)</th><th>Path ($p_v$)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>A</strong></td><td></td><td></td><td></td></tr>
        <tr><td><strong>B</strong></td><td></td><td></td><td></td></tr>
        <tr><td><strong>C</strong></td><td></td><td></td><td></td></tr>
        <tr><td><strong>D</strong></td><td></td><td></td><td></td></tr>
        <tr><td><strong>E</strong></td><td></td><td></td><td></td></tr>
        <tr><td><strong>F</strong></td><td></td><td></td><td></td></tr>
        <tr><td><strong>G</strong></td><td></td><td></td><td></td></tr>
      </tbody>
    </table>
    <div class="handwriting-line" style="margin-top:10px;">Shortest path from A to F: Length = ..........., Path = ............................................................</div>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด Assignment 4 (Solution 6.1)</summary>
    <div class="solution-box">
      <p><strong>ตารางเฉลยสมบูรณ์พร้อมรอยขีดฆ่า:</strong></p>
      <table class="blank-table">
        <tr style="background:#f1f5f9;">
          <th>Vertex</th><th>Known</th><th>Dist ($d_v$)</th><th>Path ($p_v$)</th><th>การเปลี่ยนค่า</th>
        </tr>
        <tr><td><strong>A</strong></td><td><strong>T</strong></td><td><strong>0</strong></td><td><strong>0</strong></td><td>$F \to T, 999 \to 0$</td></tr>
        <tr><td><strong>B</strong></td><td><strong>T</strong></td><td><strong>1</strong></td><td><strong>A</strong></td><td>$F \to T, 999 \to 1, 0 \to A$</td></tr>
        <tr><td><strong>C</strong></td><td><strong>T</strong></td><td><strong>1</strong></td><td><strong>A</strong></td><td>$F \to T, 999 \to 1, 0 \to A$</td></tr>
        <tr><td><strong>D</strong></td><td><strong>T</strong></td><td><strong>2</strong></td><td><strong>C</strong></td><td>$F \to T, 999 \to 2, 0 \to C$</td></tr>
        <tr><td><strong>E</strong></td><td><strong>T</strong></td><td><strong>2</strong></td><td><strong>B</strong></td><td>$F \to T, 999 \to 2, 0 \to B$</td></tr>
        <tr><td><strong>F</strong></td><td><strong>T</strong></td><td><strong>3</strong></td><td><strong>E</strong></td><td>$F \to T, 999 \to 3, 0 \to E$ (หรือ D)</td></tr>
        <tr><td><strong>G</strong></td><td><strong>T</strong></td><td><strong>2</strong></td><td><strong>B</strong></td><td>$F \to T, 999 \to 2, 0 \to B$</td></tr>
      </table>
      <p><strong>ผลการค้นหาเส้นทาง $A \to F$:</strong></p>
      <ul>
        <li>ความยาว (Length) $= \mathbf{3 \text{ เส้น}}$</li>
        <li>เส้นทางที่ถูกต้อง: <span style="font-weight:bold; color:#15803d;">A, B, E, F</span> (หรือ <code>(A, B, E, F)</code> หรือ <code>A, C, D, F</code>)</li>
        <li>🚨 <strong>ห้ามเขียน:</strong> <code>A -> B -> E -> F</code> (โดน 0 คะแนน)</li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>6.2 The Null Graph Trick Question (ข้อสอบลวงเรื่องกราฟว่าง)</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 3 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Consider a Null Graph (Empty Graph) defined mathematically as $G = (\emptyset, \emptyset)$ where $V = \{\}$ and $E = \{\}$. What is the Shortest Path from Vertex $A$ to Vertex $C$ in this graph? State the exact required response.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดอาจารย์):</strong> กำหนดกราฟว่าง $V = \{\}, E = \{\}$ จงเขียน Path จาก $A$ ไปยัง $C$<br>
    <strong>🎙️ คำพูดจริงของอาจารย์ในห้องเรียน (23 ก.ย. 2569 เวลา 10:38 น.):</strong> <em>"มีรุ่นพี่ปีก่อนๆ ไปตอบ A, C หรือไปตอบว่า Length = 0 อาจารย์ให้ 0 คะแนนทันทีครับ! เพราะในกราฟว่าง มันไม่มี Vertex A และไม่มี Vertex C เลย แล้วมันจะมี Path ได้ยังไง! ต้องตอบว่า 'ไม่มี Path จาก A ไป C เนื่องจากไม่มีโหนดดังกล่าวในกราฟ' ถึงจะได้คะแนน!"</em>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 6.2)</summary>
    <div class="solution-box">
      <p><strong>คำตอบที่ถูกต้อง:</strong></p>
      <div class="note-box" style="border-left-color:#2563eb; background:#eff6ff;">
        <strong>"ไม่มี Path จาก $A$ ไปยัง $C$ เนื่องจากในกราฟไม่มี Vertex $A$ และไม่มี Vertex $C$"</strong>
        <br>(<em>"No path exists from A to C because neither vertex exists in the graph."</em>)
      </div>
      <p>❌ <strong>คำตอบที่ได้ 0 คะแนน:</strong> ตอบว่า $A, C$ หรือตอบว่า Length = 0 หรือเว้นว่างไว้</p>
    </div>
  </details>

  <!-- ========================================================================= -->
  <!-- QUESTION 7: RAPID-FIRE TEACHER SECRET TRAPS -->
  <!-- ========================================================================= -->
  <h2 id="sec-q7" class="part-title" style="color:#3730a3; border-bottom-color:#c7d2fe;">Question 7: Rapid-Fire Teacher Secret Traps, Properties &amp; Percentages (10 คะแนน)</h2>
  <div class="ref-tag">📖 อ้างอิงข้อความจริงบนจอโปรเจกเตอร์ Notepad: IMG_20261007_120456_375.jpg | เสียงบรรยาย 7 ต.ค. 2569 (นาที 02:28:00)</div>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3;">
    <span>7.1 โครงสร้างข้อมูลอะไรเอ่ยที่มี 2, 3 Properties? (Two &amp; Three Properties)</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 2 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Answer the exact questions typed in Notepad by the professor:</p>
  <ol type="a">
    <li>What data structure has <strong>TWO properties</strong>? Name the structure and state both properties.</li>
    <li>What data structure has <strong>THREE properties</strong>? Name the structure and state all three properties.</li>
  </ol>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 7.1)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a) โครงสร้างที่มี 2 Properties:</strong> คือ <strong>Binary Heap</strong>
          <br>1. <strong>Structure Property:</strong> ต้องเป็น Complete Binary Tree (บรรจุเต็มทุกระดับ ยกเว้นระดับล่างสุดที่ชิดซ้าย)
          <br>2. <strong>Heap-Order Property:</strong> สำหรับ Min-Heap ค่าของพ่อแม่ต้องน้อยกว่าหรือเท่ากับลูกเสมอ ($\text{Parent} \le \text{Children}$)
        </li>
        <li><strong>ข้อ b) โครงสร้างที่มี 3 Properties:</strong> คือ <strong>AVL Tree</strong> (หรือ Red-Black Tree / B-Tree)
          <br>1. <strong>Binary Search Tree Property:</strong> โหนดซ้ายน้อยกว่าราก โหนดขวามากกว่าราก
          <br>2. <strong>Height-Balanced Property:</strong> ความสูงของต้นไม้ย่อยซ้ายและขวาต่างกันไม่เกิน 1 ($|\Delta h| = |h_L - h_R| \le 1$)
          <br>3. <strong>Binary Tree Node Property:</strong> แต่ละโหนดมีลูกได้ไม่เกิน 2 คน
        </li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>7.2 การคำนวณร้อยละความสูญเสียใน RAM (RAM Waste Percentage in Adjacency Matrix)</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 2 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> A directed graph has $|V| = 7$ vertices and $|E| = 12$ edges. When represented as an Adjacency Matrix:</p>
  <ol type="a">
    <li>What percentage of memory space is actively used (value = 1)?</li>
    <li>What percentage of memory space is completely wasted (zeros)?</li>
    <li>If represented as an Adjacency List for $|V| = 10, |E| = 20$, how many memory units are required compared to an Adjacency Matrix? What percentage of memory is saved?</li>
  </ol>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 7.2)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a) พื้นที่ใช้งานจริง (Value = 1):</strong>
          $$\frac{|E|}{|V|^2} \times 100\% = \frac{12}{7 \times 7} \times 100\% = \frac{12}{49} \times 100\% = \mathbf{24.48\%}$$
        </li>
        <li><strong>ข้อ b) พื้นที่สูญเปล่า (Zeros):</strong>
          $$\frac{|V|^2 - |E|}{|V|^2} \times 100\% = \frac{49 - 12}{49} \times 100\% = \frac{37}{49} \times 100\% = \mathbf{75.51\%}$$
        </li>
        <li><strong>ข้อ c) สำหรับ $|V|=10, |E|=20$:</strong>
          <br>&bull; Adjacency Matrix ใช้: $|V|^2 = 10 \times 10 = \mathbf{100 \text{ ช่อง}}$
          <br>&bull; Adjacency List ใช้: $|V| + |E| = 10 + 20 = \mathbf{30 \text{ ช่อง}}$
          <br>&bull; ประหยัดหน่วยความจำได้: $\frac{100 - 30}{100} \times 100\% = \mathbf{70\%}$
        </li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>7.3 Complete Graph Edges &amp; The Strict "No-Formula" Evaluation Rule</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 2 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong></p>
  <ol type="a">
    <li>How many edges are in an <strong>Undirected Complete Graph</strong> with $V = 10$? (Why does answering `10*(10-1)/2` result in an <strong>immediate 0 score</strong>?).</li>
    <li>How many edges are in an Undirected Complete Graph with $V = 16$?</li>
    <li>How many edges are in a <strong>Directed Complete Graph</strong> with $V = 10$?</li>
  </ol>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 7.3)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a) Undirected Complete Graph $V=10$:</strong>
          $$E = \frac{V(V-1)}{2} = \frac{10 \times 9}{2} = \mathbf{45 \text{ เส้น}}$$
          🚨 <strong>คำเตือนอาจารย์:</strong> ต้องตอบตัวเลขจำนวนเต็ม <strong>45</strong> หรือ <strong>45 เส้น</strong> ห้ามตอบติดสูตร <code>10*(10-1)/2</code> หรือ <code>90/2</code> เด็ดขาด ใครตอบติดสูตรโดนตัดเหลือ 0 ทันที!
        </li>
        <li><strong>ข้อ b) สำหรับ $V=16$:</strong>
          $$E = \frac{16 \times 15}{2} = 8 \times 15 = \mathbf{120 \text{ เส้น}}$$
        </li>
        <li><strong>ข้อ c) Directed Complete Graph $V=10$:</strong>
          $$E = V(V-1) = 10 \times 9 = \mathbf{90 \text{ เส้น}}$$
        </li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>7.4 Complete Binary Tree Node Limits &amp; "Do NOT Answer Powers of 2" Rule</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 2 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> In a Complete Binary Tree of height $H = 10$ (where Root is at height 0):</p>
  <ol type="a">
    <li>What is the <strong>minimum number of nodes</strong> ($N_{\min}$)?</li>
    <li>What is the <strong>maximum number of nodes</strong> ($N_{\max}$)?</li>
    <li>Explain why writing your answer as $2^{10}$ or $2^{11}-1$ results in a <strong>0 score</strong>.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย &amp; คำพูดอาจารย์):</strong> จงหาจำนวนโหนดอย่างน้อยและอย่างมากของ Complete Binary Tree ที่ความสูง 10<br>
    <strong>🎙️ คำพูดจริงของอาจารย์ในห้องเรียน:</strong> <em>"เวลาตอบ อย่าติดในรูปเลขยกกำลังนะครับ! คุณจะต้องตอบเป็นตัวเลขจำนวนเต็มของโหนด ถ้าตอบมาเป็นเลขยกกำลังอย่างนี้ ไม่ได้คะแนน! คุณเรียนไอที 2^10 = 1024, 2^11 - 1 = 2047 โหนด คิดเลขไม่ยากเลย!"</em>
  </div>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 7.4)</summary>
    <div class="solution-box">
      <p><strong>เฉลย:</strong></p>
      <ul>
        <li><strong>ข้อ a) จำนวนโหนดอย่างน้อย:</strong>
          $$N_{\min} = 2^H = 2^{10} = \mathbf{1,024 \text{ โหนด}}$$
        </li>
        <li><strong>ข้อ b) จำนวนโหนดอย่างมาก:</strong>
          $$N_{\max} = 2^{H+1} - 1 = 2^{11} - 1 = 2048 - 1 = \mathbf{2,047 \text{ โหนด}}$$
        </li>
        <li><strong>ข้อ c) สาเหตุที่ห้ามตอบเลขยกกำลัง:</strong> เพราะอาจารย์ต้องการวัดผลว่านักศึกษาสามารถคำนวณและประเมินขนาดจริงของหน่วยความจำได้หรือไม่ การตอบ $2^{10}$ ถือว่ายังคำนวณไม่สำเร็จและไม่ปฏิบัติตามคำสั่งการตรวจข้อสอบ</li>
      </ul>
    </div>
  </details>

  <h3 class="question-title" style="border-left-color:#6366f1; color:#3730a3; margin-top:20px;">
    <span>7.5 Circular Queue Simulation with Internal Array &amp; Pointers</span>
    <span class="score-badge" style="background:#ede9fe; color:#4338ca;">Score: 2 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an existing circular queue of capacity 5 implemented using a 1D array, containing the initial elements `[20, 40, 50, 60]`. The following operations are executed sequentially: `dequeue()`, `dequeue()`, `enqueue(10)`, `dequeue()`, `enqueue(30)`.</p>
  <ol type="a">
    <li>What elements remain in the queue in logical FIFO order?</li>
    <li>What are the final values of the pointers `Front` and `Back`?</li>
    <li>Show the exact internal array state (`self.the_array`).</li>
  </ol>

  <details class="solution-details">
    <summary class="solution-summary">💡 คลิกเพื่อดูเฉลยละเอียด (Solution 7.5)</summary>
    <div class="solution-box">
      <p><strong>การ Trace ทีละขั้นตอน:</strong></p>
      <ul>
        <li>เริ่มต้น: `[20, 40, 50, 60]` &rarr; `Front = 0, Back = 3`</li>
        <li>`dequeue()` &rarr; นำ 20 ออก &rarr; `Front = 1`</li>
        <li>`dequeue()` &rarr; นำ 40 ออก &rarr; `Front = 2`</li>
        <li>`enqueue(10)` &rarr; `Back = (3 + 1) % 5 = 4` &rarr; ช่อง 4 ใส่ 10</li>
        <li>`dequeue()` &rarr; นำ 50 ออก &rarr; `Front = 3`</li>
        <li>`enqueue(30)` &rarr; `Back = (4 + 1) % 5 = 0` (Wrap Around!) &rarr; ช่อง 0 ใส่ 30</li>
      </ul>
      <p><strong>คำตอบ:</strong></p>
      <ul>
        <li><strong>ข้อ a) สมาชิกที่เหลือในคิวตามลำดับ FIFO:</strong> <span style="font-weight:bold; color:#15803d;">[60, 10, 30]</span></li>
        <li><strong>ข้อ b) สถานะ Pointer:</strong> `Front = 3`, `Back = 0` (คิวมีขนาด `CurrentSize = 3`)</li>
        <li><strong>ข้อ c) สถานะ Array ภายใน (`self.the_array`):</strong>
          <table class="blank-table" style="max-width:400px; margin:6px 0;">
            <tr style="background:#f1f5f9;"><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th></tr>
            <tr>
              <td style="font-weight:bold; color:#2563eb;">30</td>
              <td style="color:#94a3b8;">None</td>
              <td style="color:#94a3b8;">None</td>
              <td style="font-weight:bold; color:#2563eb;">60</td>
              <td style="font-weight:bold; color:#2563eb;">10</td>
            </tr>
          </table>
        </li>
      </ul>
    </div>
  </details>

  </div> <!-- END TAB SECRETS -->
"""
'''

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab_secrets.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"generate_tab_secrets.py written successfully! Total bytes: {len(content)}")
