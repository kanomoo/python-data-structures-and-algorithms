# -*- coding: utf-8 -*-
import sys

def update_tab1_q2():
    filepath = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find boundaries
    start_anchor = '<h2 id="q2" class="part-title">Question 2: Priority Queue (Binary Min-Heap) (10 คะแนน)</h2>'
    end_anchor = '<div class="solution-box">\n    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>'

    pos_start = content.find(start_anchor)
    pos_end = content.find(end_anchor)

    if pos_start == -1 or pos_end == -1:
        print("ERROR: markers not found")
        return

    replacement = r'''<h2 id="q2" class="part-title">Question 2: Priority Queue (Binary Min-Heap) (10 คะแนน)</h2>
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
    <span>2. Binary Heap 4 Vertical Arrays (Insertions, deleteMin, Insert, deleteMin)</span>
    <span class="score-badge">Score: 10 Marks (1 + 2 + 2 + 3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Binary Min-Heap implemented as a 1-based array (where index 0 is unused / sentinel). You are given the sequence of 12 keys:</p>
  $$\mathbf{64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20}$$
  <p><strong>Sub-questions according to the official exam paper:</strong></p>
  <ul>
    <li><strong>2.1:</strong> Insert the 12 keys into the Binary Heap. Write <em>only the final resulting array</em> into vertical table 1 [1 คะแนน]</li>
    <li><strong>2.2:</strong> Perform <code>deleteMin()</code> 1 time and write the resulting array into vertical table 2 [2 คะแนน]</li>
    <li><strong>2.3:</strong> Insert key <code>3</code> into the heap and write the resulting array into vertical table 3 [2 คะแนน]</li>
    <li><strong>2.4:</strong> Perform <code>deleteMin()</code> one more time and write the final resulting array into vertical table 4 [3 คะแนน]</li>
  </ul>

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
'''

    new_content = content[:pos_start] + replacement + content[pos_end:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: generate_tab1.py Question 2 updated successfully!")

if __name__ == '__main__':
    update_tab1_q2()
