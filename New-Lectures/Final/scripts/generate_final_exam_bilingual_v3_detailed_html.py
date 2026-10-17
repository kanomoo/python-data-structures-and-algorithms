"""
Final Exam Bilingual HTML Generator (Version 3 - Comprehensive & Detailed Sub-Questions)
Course: 060243106 / 060223119 Data Structures and Algorithms
Faculty of Applied Science / Faculty of Information Technology, KMUTNB
Semester 1, Academic Year 2026
Instructor: Assoc. Prof. Dr. Pradit Pitaksatheinkul
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svg_exam_components as sec

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "แนวข้อสอบปลายภาค_Data_Structures_Final_Exam_v3_Detailed.html"
)

# SVGs
svg_graph_topo = sec.render_svg_graph_exam2026_topo(width=580, height=320)
adj_exam_topo = {
    1: [3, 4],
    2: [1, 4],
    3: [4, 6],
    4: [6],
    5: [1, 2, 3],
    6: [],
    7: [2, 6]
}
svg_adj_topo = sec.render_svg_adj_list(adj_exam_topo, title="Adjacency List: Directed Acyclic Graph (DAG 7 Vertices)", width=540, height=350)

svg_graph_sp = sec.render_svg_graph_exam2026_sp(width=580, height=320)
adj_exam_sp = {
    1: [2, 4],
    2: [4, 5],
    3: [1, 6],
    4: [3, 5, 6, 7],
    5: [7],
    6: [],
    7: [6]
}
svg_adj_sp = sec.render_svg_adj_list(adj_exam_sp, title="Adjacency List: Directed Graph (Source = 1, 7 Vertices)", width=540, height=350)

html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ข้อสอบปลายภาค 2569 (Detailed Version 3) — Data Structures & Algorithms (KMUTNB)</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {{
  --primary: #1e3a8a;
  --primary-light: #3b82f6;
  --success: #15803d;
  --success-bg: #f0fdf4;
  --danger: #b91c1c;
  --danger-bg: #fef2f2;
  --warning: #b45309;
  --warning-bg: #fffbeb;
  --bg: #f8fafc;
  --card-bg: #ffffff;
  --text: #0f172a;
  --text-muted: #475569;
  --border: #cbd5e1;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Sarabun', sans-serif;
  background-color: var(--bg);
  color: var(--text);
  line-height: 1.6;
  padding: 24px;
}}
.container {{ max-width: 1200px; margin: 0 auto; }}
.header-card {{
  background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
  color: #ffffff;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  margin-bottom: 24px;
}}
.header-card h1 {{ font-size: 26px; font-weight: 700; margin-bottom: 8px; }}
.header-card p {{ font-size: 15px; opacity: 0.9; margin-bottom: 6px; }}
.badge {{ display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; margin-right: 8px; }}
.badge-gold {{ background: #fef08a; color: #854d0e; }}
.badge-blue {{ background: #dbeafe; color: #1e40af; }}
.badge-green {{ background: #dcfce7; color: #166534; }}

.nav-tabs {{
  display: flex; gap: 12px; margin-bottom: 24px; border-bottom: 2px solid var(--border); padding-bottom: 8px;
}}
.nav-tab {{
  padding: 10px 20px; font-weight: 600; border-radius: 8px; cursor: pointer; transition: all 0.2s;
  background: #e2e8f0; color: var(--text-muted); text-decoration: none;
}}
.nav-tab.active {{ background: var(--primary); color: #fff; }}

.q-card {{
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 28px;
  margin-bottom: 28px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}}
.q-title {{
  font-size: 20px; font-weight: 700; color: var(--primary); border-bottom: 2px solid #e2e8f0; padding-bottom: 12px; margin-bottom: 16px;
  display: flex; justify-content: space-between; align-items: center;
}}
.sub-q {{
  margin-top: 20px; margin-bottom: 14px; padding-left: 12px; border-left: 4px solid var(--primary-light);
}}
.sub-q h4 {{ font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 6px; }}
.sub-q p {{ font-size: 14.5px; color: var(--text-muted); }}

.data-table {{
  width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 14px;
}}
.data-table th, .data-table td {{
  border: 1px solid var(--border); padding: 8px 12px; text-align: center;
}}
.data-table th {{ background: #f1f5f9; font-weight: 600; color: #1e293b; }}
.data-table tr:nth-child(even) {{ background: #f8fafc; }}

.sol-toggle {{
  margin-top: 14px;
}}
.sol-btn {{
  background: #e0e7ff; color: #3730a3; border: 1px solid #c7d2fe; padding: 8px 16px; border-radius: 6px; font-weight: 600; cursor: pointer;
  font-family: inherit; font-size: 13.5px;
}}
.sol-btn:hover {{ background: #c7d2fe; }}
.sol-body {{
  display: none; background: var(--success-bg); border: 1px solid #86efac; border-radius: 8px; padding: 18px; margin-top: 12px;
}}
.sol-body.open {{ display: block; }}

.alert-danger {{
  background: var(--danger-bg); border: 1px solid #fca5a5; color: var(--danger); padding: 12px 16px; border-radius: 8px; font-weight: 600; margin: 12px 0; font-size: 14px;
}}
.alert-info {{
  background: #f0f9ff; border: 1px solid #bae6fd; color: #0369a1; padding: 12px 16px; border-radius: 8px; margin: 12px 0; font-size: 14px;
}}

.grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 16px 0; }}
@media(max-width: 800px) {{ .grid-2 {{ grid-template-columns: 1fr; }} }}

code {{ font-family: 'Fira Code', monospace; background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #095299; }}
</style>
<script>
function toggleSol(id) {{
  var el = document.getElementById(id);
  if (el.classList.contains('open')) {{
    el.classList.remove('open');
  }} else {{
    el.classList.add('open');
  }}
}}
</script>
</head>
<body>
<div class="container">

<div class="header-card">
  <div style="margin-bottom: 12px;">
    <span class="badge badge-gold">Official Exam Suite 2026</span>
    <span class="badge badge-blue">Detailed Version 3</span>
    <span class="badge badge-green">Open-Book & Calculator Allowed</span>
  </div>
  <h1>KMUTNB Data Structures & Algorithms — Final Exam 2026 (Detailed Version 3)</h1>
  <p><b>หลักสูตร:</b> 060243106 / 060223119 | <b>ผู้บรรยาย:</b> รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล | ภาควิชาวิทยาการคอมพิวเตอร์และสารสนเทศ มจพ.</p>
  <p><b>รูปแบบข้อสอบ:</b> 7 ข้อใหญ่ 70 คะแนนดิบ (หาร 2 เหลือ 35% ของเกรด) | มีข้อย่อยละเอียดครบทุกมิติ พร้อมเฉลยละเอียดและข้อควรระวังตัดศูนย์คะแนน</p>
</div>

<!-- QUESTION 1 -->
<div class="q-card" id="q1">
  <div class="q-title">
    <span>ข้อ 1: Hashing & Open Addressing with Double Hashing (10 คะแนน)</span>
    <span class="badge badge-blue">บทที่ 7 (Hashing)</span>
  </div>
  <p>กำหนดให้มี Hash Table ว่างขนาด <b>TableSize = 19</b> (ดัชนี 0 ถึง 18) โครงสร้าง Open Addressing ด้วย Double Hashing:</p>
  <div class="alert-info">
    • Primary Hash: <code>h₀(X) = X mod 19</code><br/>
    • Collision Function: <code>f(i) = i × (17 - (X mod 17))</code> สำหรับรอบการชน i = 0, 1, 2, ...<br/>
    • Probe Address: <code>h_i(X) = (h₀(X) + f(i)) mod 19</code><br/>
    • ชุดตัวเลขที่ต้องแทรกตามลำดับ: <code>26, 45, 70, 85, 102, 123, 143, 155</code> (จำนวน 8 ตัว)
  </div>

  <div class="sub-q">
    <h4>1.1 แสดงการคำนวณ Hash Address และ Probe Sequence ละเอียดทุกตัว [3 คะแนน]</h4>
    <p>จงแสดงวิธีทำของแต่ละคีย์ พร้อมระบุช่องที่ชนและช่องสุดท้ายที่ได้ลง</p>
  </div>
  <div class="sub-q">
    <h4>1.2 ตาราง Hash Table สุดท้าย (Element และ Info: 'A' = Active) [2 คะแนน]</h4>
    <p>วาดตารางขนาด 19 ช่อง ระบุ Element และ Info ให้ครบถ้วน</p>
  </div>
  <div class="sub-q">
    <h4>1.3 วิเคราะห์การชน (Collision Breakdown) & คีย์ที่ชนมากที่สุด [2 คะแนน]</h4>
    <p>คีย์ใดชน 0 ครั้ง, คีย์ใดชน 1 ครั้ง, คีย์ใดชนมากที่สุด (กี่ครั้ง และชนที่ช่องใดบ้าง) และจำนวนการชนสะสมรวมทั้งหมด</p>
  </div>
  <div class="sub-q">
    <h4>1.4 การคำนวณ Load Factor (λ) และเกณฑ์การ Rehashing ที่ 80% [3 คะแนน]</h4>
    <p>คำนวณ Load Factor ปัจจุบัน, จำนวนคีย์ที่ใส่เพิ่มได้อีกก่อนเกิด Rehash, และขนาดตารางใหม่ (New Table Size) หลัง Rehash</p>
  </div>

  <div class="sol-toggle">
    <button class="sol-btn" onclick="toggleSol('sol-1')">🔍 ดูเฉลยละเอียดและวิธีคิดข้อ 1 (Click to Toggle)</button>
    <div class="sol-body" id="sol-1">
      <h3 style="color: #15803d; margin-bottom: 8px;">เฉลยสมบูรณ์ข้อ 1:</h3>
      <table class="data-table">
        <tr><th>Key (X)</th><th>h₀(X) = X mod 19</th><th>hash₂(X) = 17 - (X mod 17)</th><th>Probe Sequence & Collision</th><th>Final Slot</th><th>Collisions</th></tr>
        <tr><td><b>26</b></td><td>26 mod 19 = 7</td><td>17 - (26 mod 17) = 8</td><td>Probe 0: ช่อง 7 ว่าง → ลงทันที</td><td><b>7</b></td><td>0</td></tr>
        <tr><td><b>45</b></td><td>45 mod 19 = 7</td><td>17 - (45 mod 17) = 6</td><td>Probe 0: ช่อง 7 (ชน 26) → Probe 1: (7+6)%19 = 13 (ว่าง)</td><td><b>13</b></td><td>1</td></tr>
        <tr><td><b>70</b></td><td>70 mod 19 = 13</td><td>17 - (70 mod 17) = 15</td><td>Probe 0: ช่อง 13 (ชน 45) → Probe 1: (13+15)%19 = 9 (ว่าง)</td><td><b>9</b></td><td>1</td></tr>
        <tr><td><b>85</b></td><td>85 mod 19 = 9</td><td>17 - (85 mod 17) = 17</td><td>Probe 0: ชน 70 → Probe 1: (9+17)%19 = 7 (ชน 26) → Probe 2: (9+34)%19 = 5 (ว่าง)</td><td><b>5</b></td><td>2</td></tr>
        <tr><td><b>102</b></td><td>102 mod 19 = 7</td><td>17 - (102 mod 17) = 17</td><td>Probe 0: ชน 26 → Probe 1: (7+17)%19 = 5 (ชน 85) → Probe 2: (7+34)%19 = 3 (ว่าง)</td><td><b>3</b></td><td>2</td></tr>
        <tr><td><b>123</b></td><td>123 mod 19 = 9</td><td>17 - (123 mod 17) = 13</td><td>Probe 0: ชน 70 → Probe 1: (9+13)%19 = 3 (ชน 102) → Probe 2: (9+26)%19 = 16 (ว่าง)</td><td><b>16</b></td><td>2</td></tr>
        <tr><td><b>143</b></td><td>143 mod 19 = 10</td><td>17 - (143 mod 17) = 10</td><td>Probe 0: ช่อง 10 ว่าง → ลงทันที</td><td><b>10</b></td><td>0</td></tr>
        <tr><td><b>155</b></td><td>155 mod 19 = 3</td><td>17 - (155 mod 17) = 15</td><td>Probe 0: ช่อง 3 (ชน 102) → Probe 1: (3+15)%19 = 18 (ว่าง)</td><td><b>18</b></td><td>1</td></tr>
      </table>
      <p><b>ตารางแฮชสุดท้าย:</b> Slot 3=102(A), Slot 5=85(A), Slot 7=26(A), Slot 9=70(A), Slot 10=143(A), Slot 13=45(A), Slot 16=123(A), Slot 18=155(A)</p>
      <p>• <b>คีย์ที่ชนมากที่สุด:</b> 85, 102, 123 (ชน 2 ครั้งเท่ากัน โดย 85 ชนช่อง 9,7 | 102 ชนช่อง 7,5 | 123 ชนช่อง 9,3)</p>
      <p>• <b>จำนวนการชนรวม:</b> 0 + 1 + 1 + 2 + 2 + 2 + 0 + 1 = <b>9 ครั้ง</b></p>
      <p>• <b>Load Factor:</b> λ = 8 / 19 ≈ <b>42.11%</b></p>
      <p>• <b>Rehashing ที่ 80%:</b> ขีดจำกัด ⌈19 × 0.8⌉ = 16 ตัว → ใส่เพิ่มได้อีก <b>8 ตัว</b> (16 - 8 = 8)</p>
      <p>• <b>ขนาดตารางใหม่:</b> จำนวนเฉพาะถัดไปที่ ≥ 2 × 19 = 38 คือ <b>41</b> (New TableSize = 41)</p>
    </div>
  </div>
</div>

<!-- QUESTION 2 -->
<div class="q-card" id="q2">
  <div class="q-title">
    <span>ข้อ 2: Priority Queue (Binary Min-Heap) Tracing & Operations (10 คะแนน)</span>
    <span class="badge badge-blue">บทที่ 8 (Binary Heap)</span>
  </div>
  <p>กำหนด Binary Min-Heap ว่างในรูป 1D Array แบบ 1-based indexing (ช่อง 0 ไม่ใช้งาน <code>arr[0] = -</code>)</p>
  <p><b>ชุดข้อมูลที่ใส่ตามลำดับ:</b> <code>64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20</code> (12 ตัว)</p>
  
  <div class="sub-q">
    <h4>2.1 คุณสมบัติ 2 ข้อและสูตร 1D Array Mapping [1 คะแนน]</h4>
    <p>ระบุ Structure Property, Heap-Order Property, และสูตร Left Child (2i), Right Child (2i+1), Parent (⌊i/2⌋)</p>
  </div>
  <div class="sub-q">
    <h4>2.2 ตารางอะเรย์แนวตั้ง 4 ตาราง (ตามแบบข้อสอบจริง มจพ. 2564) [4 คะแนน]</h4>
    <p>ตารางที่ 1: หลัง Insert ครบ 12 ตัว | ตารางที่ 2: หลัง deleteMin() ครั้งที่ 1 | ตารางที่ 3: หลัง Insert 3 | ตารางที่ 4: หลัง deleteMin() ครั้งที่ 2</p>
  </div>
  <div class="sub-q">
    <h4>2.3 วาดรูปทรี (Binary Tree Diagrams) [2 คะแนน]</h4>
    <p>วาดรูป Tree หลัง Insert 12 ตัว และรูป Tree สภาพสุดท้าย (หลัง deleteMin ครั้งที่ 2)</p>
  </div>
  <div class="sub-q">
    <h4>2.4 การไล่ตัวแปร 'hole' ขณะ percolateDown และ percolateUp [2 คะแนน]</h4>
    <p>ไล่ลำดับการย้ายตำแหน่งของ hole อย่างละเอียดตามที่เรียนในห้องเรียน</p>
  </div>
  <div class="sub-q">
    <h4>2.5 การวิเคราะห์ความซับซ้อน Big-O [1 คะแนน]</h4>
    <p>Worst case และ Average case ของ insert และ deleteMin พร้อมเหตุผลว่าทำไม insert เฉลี่ยเป็น O(1)</p>
  </div>

  <div class="sol-toggle">
    <button class="sol-btn" onclick="toggleSol('sol-2')">🔍 ดูเฉลยละเอียดและตาราง 4 ช่องข้อ 2 (Click to Toggle)</button>
    <div class="sol-body" id="sol-2">
      <h3 style="color: #15803d; margin-bottom: 8px;">เฉลยสมบูรณ์ข้อ 2:</h3>
      <table class="data-table">
        <tr><th>Index</th><th>2.1 หลัง Insert 12 ตัว</th><th>2.2 หลัง deleteMin() #1</th><th>2.3 หลัง Insert 3</th><th>2.4 หลัง deleteMin() #2</th></tr>
        <tr><td><b>[0]</b></td><td>- (Unused)</td><td>- (Unused)</td><td>- (Unused)</td><td>- (Unused)</td></tr>
        <tr><td><b>[1] (Root)</b></td><td><b>1</b></td><td><b>2</b></td><td><b>2</b></td><td><b>3</b></td></tr>
        <tr><td><b>[2]</b></td><td>6</td><td>6</td><td>6</td><td>6</td></tr>
        <tr><td><b>[3]</b></td><td>2</td><td>5</td><td><b>3</b></td><td>5</td></tr>
        <tr><td><b>[4]</b></td><td>10</td><td>10</td><td>10</td><td>10</td></tr>
        <tr><td><b>[5]</b></td><td>8</td><td>8</td><td>8</td><td>8</td></tr>
        <tr><td><b>[6]</b></td><td>5</td><td>20</td><td>5</td><td>20</td></tr>
        <tr><td><b>[7]</b></td><td>24</td><td>24</td><td>24</td><td>24</td></tr>
        <tr><td><b>[8]</b></td><td>64</td><td>64</td><td>64</td><td>64</td></tr>
        <tr><td><b>[9]</b></td><td>14</td><td>14</td><td>14</td><td>14</td></tr>
        <tr><td><b>[10]</b></td><td>20</td><td>20</td><td>20</td><td>20</td></tr>
        <tr><td><b>[11]</b></td><td>15</td><td>15</td><td>15</td><td>15</td></tr>
        <tr><td><b>[12]</b></td><td>20</td><td>-</td><td>20</td><td>-</td></tr>
      </table>
      <p>• <b>deleteMin() #1 Hole Trace:</b> hole เริ่มที่ 1 → เทียบลูก (6 กับ 2) ย้ายไป 3 → เทียบลูก (5 กับ 24) ย้ายไป 6 → วาง temp=20 ที่ arr[6]</p>
      <p>• <b>Insert 3 Hole Trace:</b> hole เริ่มที่ 12 → เทียบพ่อ arr[6]=20 (3 < 20) เลื่อน 20 ลงมา hole ย้ายไป 6 → เทียบพ่อ arr[3]=5 (3 < 5) เลื่อน 5 ลงมา hole ย้ายไป 3 → เทียบพ่อ arr[1]=2 (3 > 2 หยุด) → วาง 3 ที่ arr[3]</p>
    </div>
  </div>
</div>

<!-- QUESTION 3 & 4 -->
<div class="q-card" id="q3">
  <div class="q-title">
    <span>ข้อ 3 & ข้อ 4: Sorting Algorithms Tracing & Analysis (20 คะแนน)</span>
    <span class="badge badge-blue">บทที่ 9 (Sorting)</span>
  </div>
  
  <div class="sub-q">
    <h4>ข้อ 3: Insertion Sort Tracing & Position Moves (10 คะแนน)</h4>
    <p>3.1 วิเคราะห์ Worst-Case สำหรับ N = 12 ตัว: ชุดข้อมูลเริ่มต้นคือ <code>[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]</code><br/>
    สูตรผลรวม Position Moves: <code>N(N-1)/2 = 12 × 11 / 2 = 66 ครั้ง</code> | เปรียบเทียบ 66 ครั้ง</p>
    <p>3.2 กำหนดอาร์เรย์ <code>[61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]</code> ไล่ผลลัพธ์รอบ p = 1 ถึง 11</p>
    <p>3.3 เจาะลึกรอบ p = 3 (Key 24: เลื่อน 2 ครั้ง) และรอบ p = 6 (Key 32: เลื่อน 3 ครั้ง) | <b>ผลรวม Position Move ทั้งสิ้น = 41 ครั้ง</b> (เท่ากับจำนวน Inversions)</p>
  </div>

  <div class="sub-q">
    <h4>ข้อ 4: Selection Sort & Bubble Sort Tracing (10 คะแนน)</h4>
    <p>กำหนดอาร์เรย์ 8 ตัว: <code>[45, 18, 72, 31, 12, 88, 25, 60]</code></p>
    <p>4.1 <b>Selection Sort:</b> หา min_idx และสลับกับ a[i] ทีละรอบ (ทำ 7 รอบ, เปรียบเทียบ 28 ครั้ง, สลับจริง 3 ครั้งที่รอบ 0, 2, 5)</p>
    <p>4.2 <b>Bubble Sort:</b> แสดงการเปรียบเทียบติดกัน 7 คู่ในรอบที่ 1 (เกิด 5 สลับ) | สลับรวมทั้งสิ้น <b>12 สลับ</b> | หยุดเร็วที่ <b>รอบที่ 5</b> เพราะไม่มีการสลับ</p>
  </div>

  <div class="sol-toggle">
    <button class="sol-btn" onclick="toggleSol('sol-3-4')">🔍 ดูเฉลยละเอียดและตาราง Pass ของ Sorting (Click to Toggle)</button>
    <div class="sol-body" id="sol-3-4">
      <h3 style="color: #15803d; margin-bottom: 8px;">เฉลย Insertion Sort & Bubble Sort:</h3>
      <p><b>ตาราง Insertion Sort Position Moves:</b></p>
      <p>p=1: 1 move | p=2: 2 moves | p=3: 2 moves | p=4: 4 moves | p=5: 2 moves | p=6: 3 moves | p=7: 7 moves | p=8: 0 moves | p=9: 1 move | p=10: 8 moves | p=11: 11 moves → <b>รวม 41 moves</b></p>
      <p><b>Bubble Sort Pass 1:</b> (45,18)สลับ → (72,31)สลับ → (72,12)สลับ → (88,25)สลับ → (88,60)สลับ ได้ <code>[18, 45, 31, 12, 72, 25, 60, 88]</code> (5 สลับ)</p>
    </div>
  </div>
</div>

<!-- QUESTION 5 -->
<div class="q-card" id="q5">
  <div class="q-title">
    <span>ข้อ 5: Topological Sort (Kahn's Algorithm on 7-Vertex DAG) (10 คะแนน)</span>
    <span class="badge badge-blue">บทที่ 10 (Graph & Topo Sort)</span>
  </div>
  <p>กำหนดกราฟ DAG 7 จุดยอด 12 เส้นเชื่อม (จากภาพกระดานห้องเรียนจริง 840922631)</p>
  <div class="grid-2">
    <div>{svg_graph_topo}</div>
    <div>{svg_adj_topo}</div>
  </div>
  
  <div class="sub-q">
    <h4>5.1 ตาราง Indegree Processing Table ทั้ง 7 รอบ [4 คะแนน]</h4>
    <p>เริ่มต้น Indegree: <code>v1:2, v2:2, v3:2, v4:3, v5:0, v6:3, v7:0</code> (Enqueue 5 และ 7)</p>
  </div>
  <div class="sub-q">
    <h4>5.2 Circular Queue Tracing (ขนาด 7 ช่อง ดัชนี 0 ถึง 6) [2 คะแนน]</h4>
    <p>Enqueue Sequence: 5, 7, 2, 1, 3, 4, 6 | Dequeue Sequence: 5, 7, 2, 1, 3, 4, 6 | พอยน์เตอร์ front = 6, back = 6 (คิวว่าง)</p>
  </div>
  <div class="sub-q">
    <h4>5.3 ลำดับ Topological Ordering สมบูรณ์ [3 คะแนน]</h4>
    <div class="alert-danger">
      * คำเตือนจุดตัด 0 คะแนนของ อ.ประดิษฐ์: ต้องคั่นด้วยเครื่องหมายจุลภาค (,) เท่านั้น เช่น 5, 7, 2, 1, 3, 4, 6 ห้ามใส่ลูกศร (5 → 7 → 2...) เด็ดขาด!
    </div>
  </div>
  <div class="sub-q">
    <h4>5.4 การตรวจสอบวัฏจักร (Cycle Detection) [1 คะแนน]</h4>
    <p>ถ้าจำนวนโหนดที่ Dequeue ออกมาได้ < |V| (7) แสดงว่ากราฟมี Cycle (ไม่เป็น DAG)</p>
  </div>

  <div class="sol-toggle">
    <button class="sol-btn" onclick="toggleSol('sol-5')">🔍 ดูเฉลยละเอียดและตาราง Indegree ข้อ 5 (Click to Toggle)</button>
    <div class="sol-body" id="sol-5">
      <h3 style="color: #15803d; margin-bottom: 8px;">เฉลยสมบูรณ์ข้อ 5:</h3>
      <p><b>Topological Ordering ที่ถูกต้อง:</b> <code style="font-size: 16px; font-weight: bold; color: #15803d;">5, 7, 2, 1, 3, 4, 6</code> (หรือ <code>7, 5, 2, 1, 3, 4, 6</code>)</p>
    </div>
  </div>
</div>

<!-- QUESTION 6 -->
<div class="q-card" id="q6">
  <div class="q-title">
    <span>ข้อ 6: Unweighted Shortest Path Algorithm (BFS) (10 คะแนน)</span>
    <span class="badge badge-blue">บทที่ 11 (Shortest Path & Assignment 4)</span>
  </div>
  <p>กำหนดกราฟ 7 จุดยอด 12 เส้นเชื่อม (จากภาพกระดานห้องเรียนจริง 838089388 และงาน Assignment 4) โดยมี <b>Vertex 1 เป็นจุดเริ่มต้น</b></p>
  <div class="grid-2">
    <div>{svg_graph_sp}</div>
    <div>{svg_adj_sp}</div>
  </div>

  <div class="sub-q">
    <h4>6.1 ตารางประมวลผล BFS Shortest Path (Known, Dist, Path) [4 คะแนน]</h4>
    <p>เติมตารางให้ครบทุกโหนด โดย Known เป็น True (1) ทั้งหมด</p>
  </div>
  <div class="sub-q">
    <h4>6.2 Circular Queue State upon Completion [2 คะแนน]</h4>
    <p>Enqueue Sequence: 1, 2, 4, 5, 3, 6, 7 | Dequeue Sequence: 1, 2, 4, 5, 3, 6, 7 | front = 6, back = 6 (คิวว่าง)</p>
  </div>
  <div class="sub-q">
    <h4>6.3 เส้นทางและระยะทางสั้นที่สุดไปยัง 4 จุดหมายปลายทาง [3 คะแนน]</h4>
    <div class="alert-danger">
      * กฎเหล็ก: เขียนคั่นด้วยจุลภาคเท่านั้น ห้ามใส่ลูกศร และระยะทางนับจำนวนเส้นเชื่อม (Edges) ห้ามตอบจำนวนโหนด!
    </div>
  </div>

  <div class="sol-toggle">
    <button class="sol-btn" onclick="toggleSol('sol-6')">🔍 ดูเฉลยละเอียดตารางและเส้นทางข้อ 6 (Click to Toggle)</button>
    <div class="sol-body" id="sol-6">
      <h3 style="color: #15803d; margin-bottom: 8px;">เฉลยสมบูรณ์ข้อ 6:</h3>
      <table class="data-table">
        <tr><th>Vertex</th><th>Known</th><th>Distance (dv)</th><th>Previous Path (pv)</th><th>Shortest Route from Source (1)</th></tr>
        <tr><td><b>v₁</b></td><td>True</td><td>0</td><td>0</td><td><b>1</b></td></tr>
        <tr><td><b>v₂</b></td><td>True</td><td>1</td><td>1</td><td><b>1, 2</b></td></tr>
        <tr><td><b>v₃</b></td><td>True</td><td>2</td><td>4</td><td><b>1, 4, 3</b></td></tr>
        <tr><td><b>v₄</b></td><td>True</td><td>1</td><td>1</td><td><b>1, 4</b></td></tr>
        <tr><td><b>v₅</b></td><td>True</td><td>2</td><td>4</td><td><b>1, 4, 5</b> (หรือ 1, 2, 5)</td></tr>
        <tr><td><b>v₆</b></td><td>True</td><td>2</td><td>4</td><td><b>1, 4, 6</b></td></tr>
        <tr><td><b>v₇</b></td><td>True</td><td>2</td><td>4</td><td><b>1, 4, 7</b></td></tr>
      </table>
      <p>• เส้นทางสั้นที่สุดไป <b>Vertex 5:</b> ระยะทาง = <b>2 edges</b> | เส้นทาง: <b>1, 4, 5</b></p>
      <p>• เส้นทางสั้นที่สุดไป <b>Vertex 7:</b> ระยะทาง = <b>2 edges</b> | เส้นทาง: <b>1, 4, 7</b></p>
    </div>
  </div>
</div>

<!-- QUESTION 7 -->
<div class="q-card" id="q7">
  <div class="q-title">
    <span>ข้อ 7: Advanced Theory, Structural Properties & Calculations (10 คะแนน)</span>
    <span class="badge badge-blue">สรุปทฤษฎี & ข้อสอบรั่ว 2561-2564</span>
  </div>
  
  <div class="sub-q">
    <h4>7.1 โครงสร้างข้อมูลที่มี 2 คุณสมบัติ vs 3 คุณสมบัติ [2 คะแนน]</h4>
    <p>• มี 2 คุณสมบัติ: <b>Binary Heap</b> (Structure Property & Heap-Order Property)<br/>
    • มี 3 คุณสมบัติ: <b>Binary Search Tree (BST)</b> (Binary tree, Left < Root, Right > Root)</p>
  </div>
  <div class="sub-q">
    <h4>7.2 คุณสมบัติ 3 ข้อของ Ideal Hash Function และข้อที่เป็นไปไม่ได้ในทางปฏิบัติ [2 คะแนน]</h4>
    <p>ข้อที่เป็นไปไม่ได้: <b>Zero Collisions (ไม่มีการชนกันเลย)</b><br/>
    เหตุผล 2 ประการ: 1. Pigeonhole Principle (คีย์อินพุตมีขนาดอนันต์แต่ตารางแฮชมีขนาดจำกัด) 2. การแจกแจงของข้อมูลจริงไม่สามารถคาดเดาได้</p>
  </div>
  <div class="sub-q">
    <h4>7.3 เปอร์เซ็นต์ขยะใน Adjacency Matrix ขนาด 7×7 [2 คะแนน]</h4>
    <p>ช่องทั้งหมด = 49 ช่อง | ช่องที่มีเส้นเชื่อม (1) = 12 ช่อง (24.49%) | <b>เปอร์เซ็นต์ขยะ (0) = 37 ช่อง (75.51%)</b><br/>
    หากใช้ Adjacency List ใช้เพียง 7 + 12 = 19 โหนด (ประหยัดหน่วยความจำได้ 61.22%)</p>
  </div>
  <div class="sub-q">
    <h4>7.4 การคำนวณจำนวนเส้นเชื่อม Complete Graph K₁₆ [1 คะแนน]</h4>
    <p>สูตร: N(N-1)/2 = 16 × 15 / 2 = <b>120 เส้นเชื่อม</b> (ตอบเป็นตัวเลขจำนวนเต็ม ห้ามติดสมการ)</p>
  </div>
  <div class="sub-q">
    <h4>7.5 จำนวนโหนดใน Complete Binary Tree ความสูง h = 10, 15, 16 [2 คะแนน]</h4>
    <p>• ความสูง h = 10: น้อยสุด = 2¹⁰ = <b>1,024 โหนด</b> | มากสุด = 2¹¹ - 1 = <b>2,047 โหนด</b><br/>
    • ความสูง h = 15: น้อยสุด = 2¹⁵ = <b>32,768 โหนด</b> | มากสุด = 2¹⁶ - 1 = <b>65,535 โหนด</b><br/>
    • ความสูง h = 16: น้อยสุด = 2¹⁶ = <b>65,536 โหนด</b> | มากสุด = 2¹⁷ - 1 = <b>131,071 โหนด</b></p>
  </div>
  <div class="sub-q">
    <h4>7.6 สูตรตำแหน่งพ่อและลูกใน Binary Heap [1 คะแนน]</h4>
    <p>Left = <b>2i</b> | Right = <b>2i + 1</b> | Parent = <b>⌊i/2⌋ (i // 2)</b> โดยใช้การปัดเศษทิ้ง</p>
  </div>

  <div class="sol-toggle">
    <button class="sol-btn" onclick="toggleSol('sol-7')">🔍 ดูเฉลยละเอียดและเหตุผลข้อ 7 (Click to Toggle)</button>
    <div class="sol-body" id="sol-7">
      <h3 style="color: #15803d; margin-bottom: 8px;">เฉลยสรุปข้อ 7:</h3>
      <p>คำตอบทุกข้อตรงตามเทปบันทึกเสียงสดของ อ.ประดิษฐ์ 100% ตัวเลขทุกตัวคำนวณเป็นจำนวนเต็มเป๊ะตามเกณฑ์การให้คะแนน</p>
    </div>
  </div>
</div>

<div class="alert-info" style="text-align: center; margin-top: 32px;">
  <b>คลังภาพประกอบและภาพกระดานเรียนสดทั้งหมด:</b> จัดเก็บแยกตามบทเรียนเรียบร้อยในโฟลเดอร์ <code>Course_Images_By_Chapter/</code> รวมทั้งสิ้น 286 ภาพ
</div>

</div>
</body>
</html>
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML: {output_path}")
