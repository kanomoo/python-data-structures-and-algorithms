# -*- coding: utf-8 -*-
import sys

def update_tab1():
    filepath = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find boundaries
    start_anchor = '<h3 class="question-title">\n    <span>1.1 Double Hashing Table'
    end_anchor = '  <!-- QUESTION 2 -->'

    pos_start = content.find(start_anchor)
    pos_end = content.find(end_anchor)

    if pos_start == -1:
        print("ERROR: start_anchor not found")
        return
    if pos_end == -1:
        print("ERROR: end_anchor not found")
        return

    # Build replacement HTML
    replacement = r'''  <div class="rules-box" style="background:#eff6ff; border-left-color:#2563eb; margin:10px 0;">
    <div class="rules-title" style="color:#1e40af;">🎙️ คำสั่งและข้อกำหนดจากกระดาษข้อสอบจริงของ อ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล:</div>
    <p style="margin:2px 0; font-size:13.5px; color:#1e3a8a;">
      1. ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Hash Table (ใน 1 ช่อง มี <code>element</code> กับ <code>info</code>) กำหนด <strong>TableSize ให้เป็น 19</strong> คิดเปอร์เซ็นต์ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่ <strong>80%</strong><br>
      2. <strong>การนับการชน:</strong> <em>"การชนกันและแก้การชนกันในแต่ละครั้ง นับเป็น 1 ไม่ได้นับเป็น 2 ได้อธิบายไว้ในห้องเรียนแล้ว"</em> (ห้ามนำจำนวนก้าว + การชนมารวมกันเป็น 2 เด็ดขาด)<br>
      3. <strong>วิธีการคำนวณ:</strong> <em>"ไม่จำเป็นต้องไล่โปรแกรมเสมอไป นักศึกษาสามารถคำนวณตามสูตรก็ได้"</em>
    </p>
  </div>

  <h3 class="question-title">
    <span>1.1 Double Hashing Table &amp; Probe Calculations</span>
    <span class="score-badge">Score: 8 Marks (8 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Hash Table of size $\text{TableSize} = 19$ (indexed $0$ to $18$) using C++ Hash Table structure with fields <code>element</code> and <code>info</code> (where active slots are marked with <code>'A'</code> / <code>ACTIVE</code>). Rehashing is triggered when the table load reaches <strong>80%</strong>.</p>
  <p>Insert the sequence of 8 keys: $\mathbf{26, 45, 70, 85, 102, 123, 143, 155}$ into the Hash Table using Open Addressing with <strong>Double Hashing</strong> defined by:</p>
  $$\text{Primary Hash Function: } h_0(X) = X \bmod 19$$
  $$\text{Probe Formula: } h_i(X) = (h_0(X) + f(i)) \bmod 19 \quad \text{where } f(i) = i \times (R - (X \bmod R)) \quad \text{for } i = 0, 1, 2, \dots$$
  <p>Show all probe calculations ($h_0, h_1, h_2, \dots$) for each key and fill the resulting Hash Table with <code>element</code> and <code>info</code> fields.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - ข้อความตามกระดาษข้อสอบจริงปี 2564 หน้า 1 เป๊ะๆ):</strong><br>
    ให้นักศึกษาทำการ insert ข้อมูลจำนวน 8 ตัวต่อไปนี้ เข้าไปใน Hash Table ดังกล่าว ชนิด Open Addressing โดยใช้วิธีการแก้การชนกันแบบ Double Hashing กำหนด $f(i) = i \times (R - (x \bmod R))$<br>
    $$\mathbf{26 , 45 , 70 , 85 , 102 , 123 , 143 , 155} \quad \text{[รวม insert ทุกตัวเสร็จสิ้น 8 คะแนน]}$$
    โดยที่: 1) ไม่จำเป็นต้องไล่โปรแกรมเสมอไป นักศึกษาสามารถคำนวณตามสูตรก็ได้<br>
    2) การชนกันและแก้การชนกันในแต่ละครั้ง นับเป็น 1 ไม่ได้นับเป็น 2 ได้อธิบายไว้ในห้องเรียนแล้ว
  </div>

  <!-- DEDICATED CALLOUT BOX EXPLAINING WHERE 17 COMES FROM -->
  <div style="background:#fffbeb; border:2px solid #f59e0b; border-radius:8px; padding:14px 18px; margin:16px 0; box-shadow:0 1px 4px rgba(245,158,11,0.15);">
    <div style="font-weight:bold; font-size:15px; color:#b45309; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
      <span style="font-size:18px;">🔍</span> เฉลยที่มาของค่า $R = 17$ อย่างละเอียด: ทำไม $R$ ถึงต้องเป็น 17? (เลข 17 โผล่มาจากไหน?)
    </div>
    <div style="font-size:13.5px; color:#78350f; line-height:1.65;">
      <p style="margin:4px 0;">
        <strong>1. ในตัวข้อสอบพิมพ์จริง:</strong> อาจารย์ประดิษฐ์จะพิมพ์สูตรทั่วไปว่า $f(i) = i \times (R - (x \bmod R))$ โดย<strong>ไม่ได้ระบุเลข $R$ ในโจทย์</strong> เพราะต้องการวัดความรู้ทฤษฎีว่านักศึกษาเลือกค่า $R$ เป็นหรือไม่!
      </p>
      <p style="margin:4px 0;">
        <strong>2. ที่มาตามทฤษฎี (ตำรา Mark Allen Weiss บทที่ 5 หน้า 205):</strong> นิยามของ Double Hashing ระบุไว้ว่า:<br>
        <span style="font-family:Consolas, monospace; background:#fef3c7; padding:2px 6px; border-radius:4px; font-weight:bold;">
          "hash2(x) = R - (x mod R) with R a prime number strictly smaller than TableSize (R &lt; TableSize)"
        </span><br>
        นั่นคือ <strong>$R$ ต้องเป็นจำนวนเฉพาะ (Prime Number) ที่มีค่าน้อยกว่า TableSize อย่างเคร่งครัด ($R &lt; \text{TableSize}$)</strong>
      </p>
      <p style="margin:4px 0;">
        <strong>3. การคำนวณหาค่า $R$ ในข้อนี้:</strong><br>
        • ขนาดตารางในโจทย์คือ $\text{TableSize} = 19$<br>
        • จำนวนเฉพาะทั้งหมดที่น้อยกว่า 19 ได้แก่ $2, 3, 5, 7, 11, 13, \mathbf{17}$<br>
        • หลักการออกแบบ Double Hashing กำหนดให้เลือก<strong>จำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize</strong> เพื่อให้ก้าวเดินกระจายตัวได้ดีที่สุด จึงได้ว่า <strong>$R = 17$</strong>
      </p>
      <p style="margin:4px 0;">
        <strong>4. หลักฐานในเฉลยลายมือรุ่นพี่จริงปี 2564 (หน้า 7 และ 8 ของ PDF ข้อสอบจริง):</strong><br>
        ในกระดาษคำตอบลายมือรุ่นพี่ รุ่นพี่ทุกคนแทนค่า $R = 17$ ลงในสูตรการแก้การชนทุกตัวอย่างชัดเจน เช่น:<br>
        • $F_1(45) = 1 \times (17 - (45 \bmod 17)) = 1 \times (17 - 11) = 6$<br>
        • $F_1(70) = 1 \times (17 - (70 \bmod 17)) = 1 \times (17 - 2) = 15$<br>
        • $F_1(85) = 1 \times (17 - (85 \bmod 17)) = 1 \times (17 - 0) = 17$<br>
        • $F_2(85) = 2 \times (17 - (85 \bmod 17)) = 2 \times 17 = 34$
      </p>
      <p style="margin:4px 0;">
        <strong>5. ตารางเทียบค่า $R$ ตามขนาด TableSize ในข้อสอบปีก่อนๆ:</strong><br>
        • ถ้า $\text{TableSize} = 19 \implies R = \mathbf{17}$ (ข้อสอบจริงปี 2564 &amp; 2561)<br>
        • ถ้า $\text{TableSize} = 17 \implies R = \mathbf{13}$ (ข้อสอบเก่าหน้า 1 และ 14: เลือกรองลงมาคือ 13)<br>
        • ถ้า $\text{TableSize} = 13 \implies R = \mathbf{11}$<br>
        • ถ้า $\text{TableSize} = 11 \implies R = \mathbf{7}$ (⚠️ <em>ห้ามเลือก 11 เด็ดขาด เพราะ $R$ ต้องน้อยกว่า TableSize</em>)<br>
        • <em>คำเตือน:</em> หากเลือก $R = \text{TableSize}$ เมื่อข้อมูลมีค่าหารลงตัว จะได้ $hash_2 = R \equiv 0 \pmod{\text{TableSize}}$ ตำแหน่งจะไม่ขยับและเกิด Infinite Loop ทันที!
      </p>
    </div>
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">
      📝 ตารางจำลองกระดาษคำตอบข้อ 1.1: โครงสร้าง Hash Table ขนาด 19 ช่อง (ใน 1 ช่อง มี Element กับ Info ตามข้อสอบจริง)
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
            <td style="padding:6px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Element</td>
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
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a;">Info</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
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
            <td style="padding:6px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Element</td>
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
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a;">Info</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; height:24px;">&nbsp;</td>
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
            <td style="padding:7px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Element</td>
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
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a;">Info</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
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
            <td style="padding:7px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Element</td>
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
          <tr style="background:#f8fafc;">
            <td style="padding:6px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a;">Info</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; color:#cbd5e1;">-</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:bold; color:#15803d; background:#ecfdf5;">A</td>
            <td style="padding:6px 4px; border:1px solid #cbd5e1; background:#f1f5f9;">-</td>
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
'''

    new_content = content[:pos_start] + replacement + content[pos_end:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: generate_tab1.py Question 1 updated successfully!")

if __name__ == '__main__':
    update_tab1()
