r"""
Interactive Web Application Generator for Final Exam 2026 Set B
Course: 060243106 / 060223119 Data Structures and Algorithms, KMUTNB
Instructor: Assoc. Prof. Dr. Pradit Pitaksatheinkul
Outputs: C:/Project/python-data-structures-and-algorithms/New-Lectures/Final/แนวข้อสอบปลายภาค_Data_Structures_Final_Exam_Set_B.html
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_OUT = os.path.join(BASE_DIR, "แนวข้อสอบปลายภาค_Data_Structures_Final_Exam_Set_B.html")

html_content = r"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ข้อสอบปลายภาค 2569 (ชุดซ้อมมือ Set B) — Data Structures & Algorithms (KMUTNB)</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {
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
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Sarabun', sans-serif;
  background-color: var(--bg);
  color: var(--text);
  line-height: 1.6;
  padding: 20px 10px;
}
.container {
  max-width: 1100px;
  margin: 0 auto;
}
/* Header */
.exam-header {
  background: linear-gradient(135deg, #1e3a8a, #0f172a);
  color: #ffffff;
  border-radius: 14px;
  padding: 28px 24px;
  margin-bottom: 24px;
  box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.25);
  position: relative;
  overflow: hidden;
}
.exam-header h1 {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 8px;
}
.exam-header .meta-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 13.5px;
  color: #cbd5e1;
  margin-top: 12px;
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.15);
}
.badge-danger { background: #ef4444; color: #fff; }
.badge-success { background: #22c55e; color: #fff; }
.badge-warning { background: #f59e0b; color: #fff; }

/* Action Bar */
.action-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 24px;
  align-items: center;
  justify-content: space-between;
}
.btn-group {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  font-size: 14px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s ease;
}
.btn-primary {
  background-color: var(--primary);
  color: #ffffff;
}
.btn-primary:hover {
  background-color: #1d4ed8;
  transform: translateY(-1px);
}
.btn-success {
  background-color: var(--success);
  color: #ffffff;
}
.btn-success:hover {
  background-color: #166534;
  transform: translateY(-1px);
}
.btn-outline {
  background-color: #ffffff;
  color: var(--text);
  border: 1px solid var(--border);
}
.btn-outline:hover {
  background-color: #f1f5f9;
}

/* Nav Tabs */
.nav-tabs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 8px;
  margin-bottom: 20px;
}
.tab-btn {
  padding: 8px 16px;
  border-radius: 8px;
  background: #e2e8f0;
  color: #334155;
  font-size: 13.5px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
}
.tab-btn.active, .tab-btn:hover {
  background: var(--primary);
  color: #ffffff;
}

/* Card */
.card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 12px;
}
.card-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--primary);
}
.card-score {
  font-size: 14px;
  font-weight: 700;
  background: #dbeafe;
  color: var(--primary);
  padding: 4px 10px;
  border-radius: 6px;
}

/* Problem Details */
.problem-box {
  background: #f8fafc;
  border-left: 4px solid var(--primary-light);
  padding: 14px 18px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 16px;
  font-size: 14px;
}
.code-block {
  font-family: 'Fira Code', monospace;
  background: #0f172a;
  color: #f8fafc;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 13px;
  margin: 10px 0;
  overflow-x: auto;
}

/* Tables */
.table-wrapper {
  overflow-x: auto;
  margin: 16px 0;
}
table.exam-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: center;
}
table.exam-table th {
  background-color: #e2e8f0;
  color: #0f172a;
  font-weight: 700;
  padding: 8px 10px;
  border: 1px solid var(--border);
}
table.exam-table td {
  padding: 8px 10px;
  border: 1px solid var(--border);
}
.highlight-ans {
  background-color: var(--success-bg);
  color: var(--success);
  font-weight: 700;
}
.strikethrough {
  text-decoration: line-through;
  color: #94a3b8;
  margin-right: 6px;
}

/* Solution Accordion */
.solution-box {
  margin-top: 18px;
  background-color: var(--success-bg);
  border: 1.5px solid #bbf7d0;
  border-radius: 10px;
  overflow: hidden;
}
.solution-header {
  padding: 12px 18px;
  background: #dcfce7;
  color: #166534;
  font-weight: 700;
  font-size: 14.5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}
.solution-body {
  padding: 16px 18px;
  font-size: 13.5px;
  color: #14532d;
  display: none;
}
.solution-box.open .solution-body {
  display: block;
}

/* Alerts */
.alert {
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 13px;
  margin: 12px 0;
  display: flex;
  gap: 10px;
  align-items: flex-start;
}
.alert-danger {
  background-color: var(--danger-bg);
  border: 1px solid #fecaca;
  color: var(--danger);
}
.alert-warning {
  background-color: var(--warning-bg);
  border: 1px solid #fed7aa;
  color: var(--warning);
}

/* Interactive Checker */
.checker-box {
  background: #f1f5f9;
  border: 1px dashed var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  margin: 12px 0;
  font-size: 13.5px;
}
.checker-row {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-top: 6px;
  flex-wrap: wrap;
}
.input-text {
  padding: 6px 12px;
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 13px;
  font-family: inherit;
  width: 220px;
}
.btn-sm {
  padding: 6px 14px;
  font-size: 12.5px;
  border-radius: 6px;
}
.feedback-msg {
  font-weight: 700;
  font-size: 13px;
}
.img-center {
  display: block;
  margin: 16px auto;
  max-width: 100%;
  border-radius: 8px;
  border: 1px solid var(--border);
}
</style>
</head>
<body>

<div class="container">

  <!-- Header -->
  <header class="exam-header">
    <h1>🏛️ ข้อสอบปลายภาค 2569 (ชุดซ้อมมือ Set B — ฉบับสมบูรณ์ 7 ข้อ 70 คะแนน)</h1>
    <p style="font-size: 15px; color: #e2e8f0;">060243106 / 060223119 Data Structures and Algorithms — คณะเทคโนโลยีและการจัดการอุตสาหกรรม มจพ.</p>
    <div class="meta-bar">
      <span>👨‍🏫 <b>ผู้ออกข้อสอบ:</b> รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล</span>
      <span>⏱️ <b>เวลาสอบ:</b> 3 ชั่วโมงเต็ม</span>
      <span>🎯 <b>คะแนน:</b> 70 คะแนน (หาร 2 เหลือ 35 คะแนน)</span>
    </div>
    <div class="meta-bar" style="margin-top: 10px;">
      <span class="badge badge-success">📖 Open Book เปิดตำราได้</span>
      <span class="badge badge-warning">🔢 ใช้เครื่องคิดเลขได้</span>
      <span class="badge badge-danger">📵 ห้ามใช้โทรศัพท์มือถือทุกกรณี</span>
    </div>
  </header>

  <!-- Download & Action Bar -->
  <div class="action-bar">
    <div class="btn-group">
      <a href="Final_Exam_2026_Set_B_Paper.pdf" target="_blank" class="btn btn-primary">
        📄 ดาวน์โหลด "ใบข้อสอบเปล่าสำหรับพิมพ์เขียน (PDF)"
      </a>
      <a href="Final_Exam_2026_Set_B_Master_Solutions.pdf" target="_blank" class="btn btn-success">
        🏆 ดาวน์โหลด "ชุดเฉลยสมบูรณ์พร้อมวิธีคิดและจุดดัก (PDF)"
      </a>
    </div>
    <div>
      <button class="btn btn-outline" onclick="toggleAllSolutions()">👁️ เปิด / ปิดเฉลยทุกข้อ</button>
    </div>
  </div>

  <!-- Navigation Filters -->
  <div class="nav-tabs">
    <button class="tab-btn active" onclick="filterQuestion('all')">ทั้งหมด (All 7 Questions)</button>
    <button class="tab-btn" onclick="filterQuestion('q1')">ข้อ 1: Hashing</button>
    <button class="tab-btn" onclick="filterQuestion('q2')">ข้อ 2: Binary Heap</button>
    <button class="tab-btn" onclick="filterQuestion('q3')">ข้อ 3: Insertion Sort</button>
    <button class="tab-btn" onclick="filterQuestion('q4')">ข้อ 4: Selection Sort</button>
    <button class="tab-btn" onclick="filterQuestion('q5')">ข้อ 5: Topological Sort</button>
    <button class="tab-btn" onclick="filterQuestion('q6')">ข้อ 6: Shortest Path</button>
    <button class="tab-btn" onclick="filterQuestion('q7')">ข้อ 7: ทฤษฎี &amp; คุณสมบัติ &amp; %</button>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 1: HASHING -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q1">
    <div class="card-header">
      <div class="card-title">ข้อ 1: Hashing &amp; Open Addressing with Double Hashing</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b> กำหนดตารางแฮชชนิด Open Addressing ขนาด <b>TableSize = 13</b> (ดัชนี 0 ถึง 12)<br/>
      ฟังก์ชันแฮชหลัก: <code>h₀(x) = x mod 13</code><br/>
      การแก้การชน: <b>Double Hashing</b> กำหนดสูตร: <code>hᵢ(x) = (h₀(x) + f(i)) mod 13</code> โดย <code>f(i) = i × (11 - (x mod 11))</code> (ค่า R = 11 ซึ่งเป็นจำนวนเฉพาะที่มากที่สุดที่น้อยกว่า 13)<br/>
      นำชุดข้อมูล 6 ตัวใส่ลงในตารางตามลำดับ: <b>[ 43, 17, 82, 95, 35, 160 ]</b>
    </div>

    <!-- Interactive Checker -->
    <div class="checker-box">
      <b>🎯 ซ้อมตอบ:</b> เกิดการชนและแก้การชนรวมทั้งสิ้นกี่ครั้ง?
      <div class="checker-row">
        <input type="number" id="ans_q1_collisions" class="input-text" placeholder="กรอกตัวเลขจำนวนครั้ง...">
        <button class="btn btn-primary btn-sm" onclick="checkQ1()">ตรวจคำตอบ</button>
        <span id="feedback_q1" class="feedback-msg"></span>
      </div>
    </div>

    <div class="alert alert-danger">
      <div>
        <b>🚨 คำเตือนจุดดัก 0 คะแนนจาก อ.ประดิษฐ์:</b><br/>
        การนับจำนวนครั้งการชน ให้นับเฉพาะจำนวนครั้งที่เกิดการกระทบเพื่อหาช่องว่างใหม่สะสมรวมกัน <b>ห้ามนับแยก "ชน 6 แก้ 6 แล้วตอบ 12 ครั้ง" เด็ดขาด!</b> ถ้าตอบ 12 จะได้ 0 คะแนนทันที
      </div>
    </div>

    <!-- Solution Accordion -->
    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยขั้นตอนการ Trace ตาราง และคำนวณ Load Factor (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <div class="table-wrapper">
          <table class="exam-table">
            <thead>
              <tr>
                <th>Key (x)</th>
                <th>h₀(x) = x mod 13</th>
                <th>Double Hashing &amp; f(i) Calculation</th>
                <th>ช่องที่ลงได้</th>
                <th>จำนวนครั้งที่ชน</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>43</b></td>
                <td>43 mod 13 = 4</td>
                <td>ช่อง 4 ว่าง ➔ ลงได้ทันที</td>
                <td class="highlight-ans">ช่อง 4</td>
                <td>0</td>
              </tr>
              <tr>
                <td><b>17</b></td>
                <td>17 mod 13 = 4</td>
                <td><b>ชนช่อง 4!</b> f(1) = 1 × (11 - (17 mod 11)) = 5 ➔ h₁ = (4 + 5) mod 13 = 9</td>
                <td class="highlight-ans">ช่อง 9</td>
                <td>1</td>
              </tr>
              <tr>
                <td><b>82</b></td>
                <td>82 mod 13 = 4</td>
                <td><b>ชนช่อง 4!</b> f(1) = 1 × (11 - (82 mod 11)) = 6 ➔ h₁ = (4 + 6) mod 13 = 10</td>
                <td class="highlight-ans">ช่อง 10</td>
                <td>1</td>
              </tr>
              <tr>
                <td><b>95</b></td>
                <td>95 mod 13 = 4</td>
                <td><b>ชนช่อง 4!</b> f(1) = 1 × (11 - (95 mod 11)) = 4 ➔ h₁ = (4 + 4) mod 13 = 8</td>
                <td class="highlight-ans">ช่อง 8</td>
                <td>1</td>
              </tr>
              <tr>
                <td><b>35</b></td>
                <td>35 mod 13 = 9</td>
                <td><b>ชนช่อง 9!</b> f(1) = 1 × (11 - (35 mod 11)) = 9 ➔ h₁ = (9 + 9) mod 13 = 18 mod 13 = 5</td>
                <td class="highlight-ans">ช่อง 5</td>
                <td>1</td>
              </tr>
              <tr>
                <td><b>160</b></td>
                <td>160 mod 13 = 4</td>
                <td><b>ชนช่อง 4!</b> h₁ = 9 ➔ <b>ชนช่อง 9 (ชนครั้งที่ 2)!</b> f(2) = 2 × 5 = 10 ➔ h₂ = (4 + 10) mod 13 = 1</td>
                <td class="highlight-ans">ช่อง 1</td>
                <td><b>2</b></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p><b>ตารางแฮชสุดท้าย:</b> Index 1: <code>160 (A)</code>, Index 4: <code>43 (A)</code>, Index 5: <code>35 (A)</code>, Index 8: <code>95 (A)</code>, Index 9: <code>17 (A)</code>, Index 10: <code>82 (A)</code></p>
        <ul style="margin-left: 20px; margin-top: 8px;">
          <li><b>ตัวเลขที่ชนมากที่สุด:</b> <b>160</b> (ชน 2 ครั้ง ที่ช่อง 4 และช่อง 9)</li>
          <li><b>เกิดการชนและแก้การชนรวม:</b> 0 + 1 + 1 + 1 + 1 + 2 = <b>6 ครั้ง</b></li>
          <li><b>Load Factor Percentage:</b> λ = (6 / 13) × 100% = <b>46.15%</b></li>
          <li><b>เกณฑ์ Rehashing ที่ 70%:</b> 13 × 0.70 = 9.1 ➔ ต้องมี 10 ตัว ปัจจุบันมี 6 ตัว ➔ <b>ต้องใส่เพิ่มอีก 4 ตัว</b></li>
          <li><b>ขนาดตารางใหม่:</b> จำนวนเฉพาะตัวแรกที่มากกว่า 2 × 13 (26) ➔ ตอบ <b>TableSize = 29</b></li>
          <li><b>นิยาม Wrap-Around:</b> <i>"เมื่อตำแหน่ง Index ที่คำนวณได้หลุดเลยช่องสุดท้ายของตาราง จะวนกลับมาเริ่มต้นที่ช่อง 0 ใหม่ด้วยการ mod TableSize อีก 1 รอบ"</i></li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 2: BINARY MIN-HEAP -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q2">
    <div class="card-header">
      <div class="card-title">ข้อ 2: Binary Min-Heap (Array Representation &amp; Operations)</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b> กำหนดชุดข้อมูล 10 ตัว: <b>[ 65, 30, 48, 15, 22, 10, 50, 18, 25, 8 ]</b><br/>
      ให้จำลองการเก็บข้อมูลในอาร์เรย์ 1 มิติ (ดัชนีเริ่มต้นที่ 1, ช่อง 0 เป็น None / ไม่ใช้งาน) ผ่าน 4 ขั้นตอน:
      1) Insert ข้อมูลทั้ง 10 ตัว &nbsp; 2) ทำ deleteMin() ครั้งที่ 1 &nbsp; 3) Insert ค่า 12 &nbsp; 4) ทำ deleteMin() อีกครั้ง
    </div>

    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยสถานะอาร์เรย์ทั้ง 4 ตาราง และสูตรพ่อลูก (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <p><b>1. อาร์เรย์หลัง Insert ข้อมูล 10 ตัว (Percolate Up):</b></p>
        <div class="code-block">Index:   [ 0     1   2   3   4   5   6   7   8   9  10 ]
Element: [ None  8  10  15  22  18  48  50  65  25  30 ]</div>

        <p><b>2. อาร์เรย์หลัง deleteMin() ครั้งที่ 1 (ดึง 8 ออก, นำ 30 มา Percolate Down):</b></p>
        <div class="code-block">Index:   [ 0     1   2   3   4   5   6   7   8   9 ]
Element: [ None 10  18  15  22  30  48  50  65  25 ]</div>

        <p><b>3. อาร์เรย์หลัง Insert 12 (ใส่ 12 ที่ช่อง 10 แล้ว Percolate Up):</b></p>
        <div class="code-block">Index:   [ 0     1   2   3   4   5   6   7   8   9  10 ]
Element: [ None 10  12  15  22  18  48  50  65  25  30 ]</div>

        <p><b>4. อาร์เรย์หลัง deleteMin() ครั้งที่ 2 (ดึง 10 ออก, นำ 30 มา Percolate Down):</b></p>
        <div class="code-block">Index:   [ 0     1   2   3   4   5   6   7   8   9 ]
Element: [ None 12  18  15  22  30  48  50  65  25 ]</div>

        <div class="alert alert-warning">
          <b>📌 สูตรและกฎสำคัญของอาจารย์:</b><br/>
          • Left Child = <code>2i</code>, Right Child = <code>2i + 1</code>, Parent = <code>⌊i / 2⌋</code> (Python ใช้ <code>i // 2</code>)<br/>
          • <b>กฎการตัดเศษทิ้ง:</b> การหาตำแหน่ง Parent ต้องตัดเศษทิ้งเสมอ เช่น ตำแหน่งที่ 7 ➔ 7/2 = 3.5 ➔ ได้ช่อง <b>3</b> (ห้ามปัดขึ้นเด็ดขาด!)<br/>
          • <b>เงื่อนไขโค้ดใน Percolate Down:</b> <code>if child != self.current_size and self.heap[child + 1] &lt; self.heap[child]: child += 1</code>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 3: INSERTION SORT -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q3">
    <div class="card-header">
      <div class="card-title">ข้อ 3: Insertion Sort Tracing &amp; Position Moves</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b><br/>
      1) คำนวณ Worst-Case และ Best-Case Moves ของข้อมูล 10 ตัว<br/>
      2) กำหนดอาร์เรย์ 10 ตัว: <b>[ 54, 38, 16, 27, 10, 62, 45, 9, 70, 31 ]</b> จง Trace อาร์เรย์ในรอบ <b>p = 3</b> และ <b>p = 6</b> พร้อมนับ Position Moves<br/>
      3) อธิบายการดัดแปลงโค้ด Insertion Sort เพื่อให้นับจำนวนการเลื่อนตำแหน่งได้
    </div>

    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยการวิเคราะห์และ Tracing ทีละรอบ (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <ul style="margin-left: 20px;">
          <li><b>Worst-Case Input:</b> ข้อมูลที่เรียงลำดับจาก <b>มากไปน้อย</b> (เช่น [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ])</li>
          <li><b>จำนวน Moves ใน Worst-Case:</b> N(N - 1) / 2 = (10 × 9) / 2 = <b>45 ครั้ง</b></li>
          <li><b>จำนวน Moves ใน Best-Case:</b> <b>0 ครั้ง</b> (ข้อมูลเรียงอยู่แล้ว ไม่เกิดการ Shift)</li>
        </ul>
        <div class="table-wrapper">
          <table class="exam-table">
            <thead>
              <tr>
                <th>Pass (p)</th>
                <th>Key Element</th>
                <th>ตัวเลขที่ถูกเลื่อน (Position Moves)</th>
                <th>สถานะอาร์เรย์หลังจบรอบ p</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>p = 3</b></td>
                <td>27</td>
                <td>เลื่อน 54 และ 38 ไปทางขวา (<b>2 moves</b>)</td>
                <td class="highlight-ans">[ 16, 27, 38, 54, 10, 62, 45, 9, 70, 31 ]</td>
              </tr>
              <tr>
                <td><b>p = 6</b></td>
                <td>45</td>
                <td>เลื่อน 62 และ 54 ไปทางขวา (<b>2 moves</b>)</td>
                <td class="highlight-ans">[ 10, 16, 27, 38, 45, 54, 62, 9, 70, 31 ]</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p><b>การดัดแปลงโค้ด:</b> ใส่คำสั่ง <code>total_moves += 1</code> ไว้ในลูป <code>while (j &gt;= 0 and arr[j] &gt; key)</code> ตรงบรรทัดที่ทำการเลื่อนค่า <code>arr[j + 1] = arr[j]</code></p>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 4: SELECTION SORT -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q4">
    <div class="card-header">
      <div class="card-title">ข้อ 4: Selection Sort Tracing (รูปแบบใบงาน Test Program 2)</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b> กำหนดอาร์เรย์ 7 ตัว: <b>[ 64, 25, 12, 38, 11, 49, 20 ]</b> จงแสดงวิธีทำของฟังก์ชัน selection_sort() ใน Round 1, 2, 3, 4 ตามรูปแบบในห้องเรียน
    </div>

    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยขั้นตอนการ Trace แบบฟอร์มใบงาน (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <p><b>Round 1:</b></p>
        <ul style="margin-left: 20px;">
          <li>1. Find minimum: จากอาร์เรย์ที่ยังไม่เรียง [ 64, 25, 12, 38, 11, 49, 20 ] ค่าน้อยสุดคือ <b>11</b> ที่ index <b>4</b></li>
          <li>2. Swap: สลับ 11 กับตัวแรกของส่วนที่ยังไม่เรียง (64)<br/>
              • Before swap: [ 64, 25, 12, 38, 11, 49, 20 ]<br/>
              • After swap: &nbsp;<b>[ 11, 25, 12, 38, 64, 49, 20 ]</b></li>
          <li>3. Result: จัดเรียงแล้ว 1 ตัว [ 11 ]. ส่วนที่ยังไม่เรียงคือ [ 25, 12, 38, 64, 49, 20 ]</li>
        </ul>
        <p style="margin-top: 8px;"><b>Round 2:</b></p>
        <ul style="margin-left: 20px;">
          <li>1. Find minimum: จากอาร์เรย์ที่ยังไม่เรียง [ 25, 12, 38, 64, 49, 20 ] ค่าน้อยสุดคือ <b>12</b> ที่ index <b>2</b></li>
          <li>2. Swap: สลับ 12 กับ 25 ➔ After swap: <b>[ 11, 12, 25, 38, 64, 49, 20 ]</b></li>
          <li>3. Result: จัดเรียงแล้ว 2 ตัว [ 11, 12 ]. ส่วนที่ยังไม่เรียงคือ [ 25, 38, 64, 49, 20 ]</li>
        </ul>
        <p style="margin-top: 8px;"><b>Round 3:</b></p>
        <ul style="margin-left: 20px;">
          <li>1. Find minimum: จากอาร์เรย์ที่ยังไม่เรียง [ 25, 38, 64, 49, 20 ] ค่าน้อยสุดคือ <b>20</b> ที่ index <b>6</b></li>
          <li>2. Swap: สลับ 20 กับ 25 ➔ After swap: <b>[ 11, 12, 20, 38, 64, 49, 25 ]</b></li>
          <li>3. Result: จัดเรียงแล้ว 3 ตัว [ 11, 12, 20 ]. ส่วนที่ยังไม่เรียงคือ [ 38, 64, 49, 25 ]</li>
        </ul>
        <p style="margin-top: 8px;"><b>Round 4:</b></p>
        <ul style="margin-left: 20px;">
          <li>1. Find minimum: จากอาร์เรย์ที่ยังไม่เรียง [ 38, 64, 49, 25 ] ค่าน้อยสุดคือ <b>25</b> ที่ index <b>6</b></li>
          <li>2. Swap: สลับ 25 กับ 38 ➔ After swap: <b>[ 11, 12, 20, 25, 64, 49, 38 ]</b></li>
          <li>3. Result: จัดเรียงแล้ว 4 ตัว [ 11, 12, 20, 25 ]. ส่วนที่ยังไม่เรียงคือ [ 64, 49, 38 ]</li>
        </ul>
        <p style="margin-top: 8px;"><b>จำนวนการ Swap สูงสุด:</b> N - 1 = 7 - 1 = <b>6 ครั้ง</b> (Selection Sort มีข้อดีคือเกิด Swap น้อยมากเพียง O(N) ครั้ง)</p>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 5: TOPOLOGICAL SORT -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q5">
    <div class="card-header">
      <div class="card-title">ข้อ 5: Topological Sort (Kahn's Algorithm on 7-Vertex DAG)</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b> กำหนด Directed Acyclic Graph (DAG) มี 7 Vertices และ 9 Edges:<br/>
      <img src="diagrams/set_b_topo.png" class="img-center" style="max-height: 280px;" alt="DAG Topo Graph">
      จงสร้างตาราง In-degree, จำลองการทำงานของ Queue และเขียน Topological Ordering ลำดับสุดท้าย
    </div>

    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยตาราง In-degree, Queue Tracing และผลลัพธ์ (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <p><b>5.1 ตาราง Initial In-degree:</b></p>
        <div class="table-wrapper">
          <table class="exam-table">
            <thead>
              <tr><th>Vertex</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
            </thead>
            <tbody>
              <tr><td><b>In-degree</b></td><td>1</td><td>1</td><td>1</td><td>2</td><td class="highlight-ans">0 (Source)</td><td>2</td><td>2</td></tr>
            </tbody>
          </table>
        </div>
        <p><b>5.2 การไล่ Queue Tracing:</b></p>
        <ul style="margin-left: 20px;">
          <li><b>เริ่มต้น:</b> โหนด 5 มี In-degree = 0 ➔ <code>Enqueue(5)</code> ➔ คิวคือ <code>[ 5 ]</code></li>
          <li><b>รอบ 1:</b> <code>Dequeue() ➔ 5</code>. ตัดเส้นชี้ไป 1 และ 2 ➔ In-degree(1) เหลือ 0 <code>(Enqueue 1)</code>, In-degree(2) เหลือ 0 <code>(Enqueue 2)</code> ➔ คิวคือ <code>[ 1, 2 ]</code></li>
          <li><b>รอบ 2:</b> <code>Dequeue() ➔ 1</code>. ตัดเส้นชี้ไป 3 และ 4 ➔ In-degree(3) เหลือ 0 <code>(Enqueue 3)</code>, In-degree(4) ลดเหลือ 1 ➔ คิวคือ <code>[ 2, 3 ]</code></li>
          <li><b>รอบ 3:</b> <code>Dequeue() ➔ 2</code>. ตัดเส้นชี้ไป 4 และ 7 ➔ In-degree(4) ลดเหลือ 0 <code>(Enqueue 4)</code>, In-degree(7) ลดเหลือ 1 ➔ คิวคือ <code>[ 3, 4 ]</code></li>
          <li><b>รอบ 4:</b> <code>Dequeue() ➔ 3</code>. ตัดเส้นชี้ไป 6 ➔ In-degree(6) ลดเหลือ 1 ➔ คิวคือ <code>[ 4 ]</code></li>
          <li><b>รอบ 5:</b> <code>Dequeue() ➔ 4</code>. ตัดเส้นชี้ไป 6 และ 7 ➔ In-degree(6) เหลือ 0 <code>(Enqueue 6)</code>, In-degree(7) เหลือ 0 <code>(Enqueue 7)</code> ➔ คิวคือ <code>[ 6, 7 ]</code></li>
          <li><b>รอบ 6:</b> <code>Dequeue() ➔ 6</code> ➔ คิวคือ <code>[ 7 ]</code></li>
          <li><b>รอบ 7:</b> <code>Dequeue() ➔ 7</code> ➔ คิวว่าง</li>
        </ul>
        <p><b>Topological Order สุดท้าย:</b> <b class="highlight-ans">5, 1, 2, 3, 4, 6, 7</b></p>
        <p style="margin-top: 6px;"><b>กรณีมี Cycle:</b> โหนดใน Cycle จะมี In-degree ≥ 1 เสมอ ทำให้ไม่ถูกนำเข้า Queue ส่งผลให้ Queue ว่างก่อนประมวลผลครบ |V| โหนด จึงตรวจสอบ Cycle ได้</p>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 6: UNWEIGHTED SHORTEST PATH -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q6">
    <div class="card-header">
      <div class="card-title">ข้อ 6: Unweighted Shortest Path Algorithm (เหมือน Assignment 4)</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b> กำหนดกราฟมี 7 จุดยอด (A ถึง G) และ 11 เส้นเชื่อม จุดเริ่มต้นคือ <b>Vertex A</b>:<br/>
      <img src="diagrams/set_b_shortest_path.png" class="img-center" style="max-height: 280px;" alt="Shortest Path Graph">
      จงแสดงวิธีทำในตาราง Known, Dist (dv), Path (pv) และ Circular Queue แล้วตอบคำถามเส้นทางที่สั้นที่สุด
    </div>

    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยตารางการประมวลผลและการ Backtrack (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <div class="table-wrapper">
          <table class="exam-table">
            <thead>
              <tr>
                <th>Vertex</th>
                <th>Known</th>
                <th>Dist (dᵥ)</th>
                <th>Path (pᵥ)</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><b>A (Start)</b></td><td class="highlight-ans">T</td><td class="highlight-ans">0</td><td>0</td></tr>
              <tr><td><b>B</b></td><td class="highlight-ans">T</td><td><span class="strikethrough">999</span><b class="highlight-ans">1</b></td><td><span class="strikethrough">0</span><b>A</b></td></tr>
              <tr><td><b>C</b></td><td class="highlight-ans">T</td><td><span class="strikethrough">999</span><b class="highlight-ans">2</b></td><td><span class="strikethrough">0</span><b>B</b></td></tr>
              <tr><td><b>D</b></td><td class="highlight-ans">T</td><td><span class="strikethrough">999</span><b class="highlight-ans">1</b></td><td><span class="strikethrough">0</span><b>A</b></td></tr>
              <tr><td><b>E</b></td><td class="highlight-ans">T</td><td><span class="strikethrough">999</span><b class="highlight-ans">2</b></td><td><span class="strikethrough">0</span><b>B</b></td></tr>
              <tr><td><b>F (Sink)</b></td><td class="highlight-ans">T</td><td><span class="strikethrough">999</span><b class="highlight-ans">3</b></td><td><span class="strikethrough">0</span><b>C</b></td></tr>
              <tr><td><b>G</b></td><td class="highlight-ans">T</td><td><span class="strikethrough">999</span><b class="highlight-ans">2</b></td><td><span class="strikethrough">0</span><b>D</b></td></tr>
            </tbody>
          </table>
        </div>
        <p><b>การหาเส้นทางด้วยการ Backtrack:</b></p>
        <ul style="margin-left: 20px;">
          <li><b>เส้นทางจาก A ไปยัง F:</b><br/>
              • ระยะทาง: ดูช่อง F ได้ <b>dᵥ = 3</b> ➔ <b>ตอบ: 3 เส้น</b> (ห้ามตอบเป็นนิ้วหรือ ซม.)<br/>
              • ย้อนรอย: F ➔ C ➔ B ➔ A ➔ <b>ตอบ: A, B, C, F</b> (ห้ามเขียนลูกศร A ➔ B ➔ C ➔ F)</li>
          <li><b>เส้นทางจาก A ไปยัง G:</b><br/>
              • ระยะทาง: <b>dᵥ = 2</b> ➔ <b>ตอบ: 2 เส้น</b><br/>
              • ย้อนรอย: G ➔ D ➔ A ➔ <b>ตอบ: A, D, G</b></li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- QUESTION 7: ADVANCED THEORY, PROPERTIES & CALCULATIONS -->
  <!-- ===================================================================== -->
  <div class="card q-card" id="q7">
    <div class="card-header">
      <div class="card-title">ข้อ 7: Advanced Theory, Structural Properties &amp; Percentage Calculations</div>
      <div class="card-score">10 คะแนน</div>
    </div>
    <div class="problem-box">
      <b>โจทย์:</b> ตอบคำถามทฤษฎี คุณสมบัติ (2, 3 properties) และคำนวณตัวเลขและเปอร์เซ็นต์ (ห้ามติดรูปสูตรหรือเลขยกกำลัง)
    </div>

    <!-- Interactive Checker for Q7 -->
    <div class="checker-box">
      <b>🎯 ซ้อมคำนวณ:</b> Complete Graph ที่มี 12 Vertices มีจำนวนเส้นเชื่อมทั้งหมดกี่เส้น?
      <div class="checker-row">
        <input type="number" id="ans_q7_edges" class="input-text" placeholder="กรอกตัวเลขจำนวนเต็ม...">
        <button class="btn btn-primary btn-sm" onclick="checkQ7()">ตรวจคำตอบ</button>
        <span id="feedback_q7" class="feedback-msg"></span>
      </div>
    </div>

    <div class="solution-box">
      <div class="solution-header" onclick="toggleSolution(this)">
        <span>💡 เฉลยทุกข้อย่อยและวิธีคิดตัวเลข (คลิกเพื่อดู)</span>
        <span>▼</span>
      </div>
      <div class="solution-body">
        <p><b>7.1 คุณสมบัติเชิงโครงสร้าง (Two Properties &amp; Three Properties):</b></p>
        <ul style="margin-left: 20px;">
          <li><b>โครงสร้างที่มี 2 Properties:</b> <b>Binary Heap</b><br/>
              1. <i>Structure Property:</i> ต้องเป็น Complete Binary Tree (เติมเต็มทุกระดับยกเว้นระดับล่างสุดที่เติมจากซ้ายไปขวา ทำให้เก็บในอะเรย์ 1 มิติได้พอดีโดยไม่ต้องใช้พอยน์เตอร์)<br/>
              2. <i>Heap-Order Property:</i> ค่าของ Parent ต้องน้อยกว่าหรือเท่ากับลูกเสมอ ($Parent \le Children$) ส่งผลให้ค่าน้อยที่สุดอยู่ที่ Root (ช่อง 1) เสมอ</li>
          <li><b>สิ่งที่มี 3 Properties:</b> <b>Ideal Hash Function</b> (ฟังก์ชันแฮชในอุดมคติ 3 ข้อ)<br/>
              1. <i>Fast Computation:</i> คำนวณได้รวดเร็วในเวลา $O(1)$<br/>
              2. <i>Deterministic:</i> คีย์เดิมต้องได้ตำแหน่งแอดเดรสเดิมเสมอ<br/>
              3. <i>Uniform Distribution:</i> กระจายคีย์ทุกตัวลงในแต่ละช่องอย่างเท่าเทียมสม่ำเสมอ</li>
          <li><b>ข้อที่เป็นไปไม่ได้จริงในโลกแห่งความเป็นจริง:</b> <b>Uniform Distribution</b><br/>
              • <i>เหตุผล 1 (Pigeonhole Principle):</i> จำนวน Key ที่เป็นไปได้ทั้งหมดมีมากกว่าขนาดตาราง (`TableSize`) เสมอ เมื่อของมากกว่าช่อง ยังไงก็ต้องเกิดการชนกัน<br/>
              • <i>เหตุผล 2 (Data Clustering):</i> ข้อมูลในการใช้งานจริงมักไม่เป็นสุ่มอิสระ แต่มีแพทเทิร์นที่เกาะกลุ่มกัน</li>
        </ul>

        <p style="margin-top: 10px;"><b>7.2 การคำนวณเปอร์เซ็นต์ความสูญเปล่าของ Adjacency Matrix (|V| = 8, |E| = 14):</b></p>
        <ul style="margin-left: 20px;">
          <li>ช่องทั้งหมดใน Matrix: 8 × 8 = <b>64 ช่อง</b></li>
          <li>ช่องที่มีข้อมูลจริง (เลข 1): 14 ช่อง ➔ คิดเป็น <b>(14 / 64) × 100% = 21.88%</b></li>
          <li>ช่องที่สูญเปล่า (เลข 0): 64 - 14 = 50 ช่อง ➔ คิดเป็น <b>(50 / 64) × 100% = 78.13%</b></li>
          <li>หากเปลี่ยนเป็น Adjacency List จะใช้พื้นที่: |V| + |E| = 8 + 14 = <b>22 ช่อง</b></li>
          <li>ประหยัดพื้นที่หน่วยความจำได้: ((64 - 22) / 64) × 100% = <b>65.63%</b></li>
        </ul>

        <p style="margin-top: 10px;"><b>7.3 การคำนวณจำนวนเส้นของ Complete Graph:</b></p>
        <ul style="margin-left: 20px;">
          <li>(a) Undirected Complete Graph $K_{12}$: $E = \frac{12 \times 11}{2} = 6 \times 11 = \mathbf{66}$ เส้น (ห้ามติดรูปสูตรเด็ดขาด)</li>
          <li>(b) Directed Complete Graph (ไม่มี Self-loop): $E = 12 \times 11 = \mathbf{132}$ เส้น</li>
        </ul>

        <p style="margin-top: 10px;"><b>7.4 จำนวนโหนดของ Complete Binary Tree (ความสูง h):</b></p>
        <ul style="margin-left: 20px;">
          <li>ความสูง $h = 12$: Min nodes $= 2^{12} = \mathbf{4,096}$ โหนด &nbsp;|&nbsp; Max nodes $= 2^{13} - 1 = \mathbf{8,191}$ โหนด</li>
          <li>ความสูง $h = 15$: Min nodes $= 2^{15} = \mathbf{32,768}$ โหนด &nbsp;|&nbsp; Max nodes $= 2^{16} - 1 = \mathbf{65,535}$ โหนด</li>
        </ul>

        <p style="margin-top: 10px;"><b>7.5 กับดักข้อสอบและคำถามดัก 0 คะแนน:</b></p>
        <ul style="margin-left: 20px;">
          <li><b>การเขียน Path:</b> ต้องเขียนคั่นด้วยจุลภาค เช่น <code>A, B, C</code> การเขียนลูกศร <code>A -&gt; B -&gt; C</code> แสดงถึง Directed Edges จึงได้ 0 คะแนน</li>
          <li><b>คำถามบน Null Graph:</b> ถ้าถามหาเส้นทางใน Null Graph ตอบว่า <i>"ไม่มี Path เนื่องจากไม่มีโหนดดังกล่าวอยู่ในกราฟ"</i></li>
        </ul>
      </div>
    </div>
  </div>

</div>

<script>
function toggleSolution(header) {
  const box = header.parentElement;
  box.classList.toggle('open');
  const arrow = header.querySelector('span:last-child');
  if (box.classList.contains('open')) {
    arrow.textContent = '▲';
  } else {
    arrow.textContent = '▼';
  }
}

function toggleAllSolutions() {
  const boxes = document.querySelectorAll('.solution-box');
  const allOpen = Array.from(boxes).every(b => b.classList.contains('open'));
  boxes.forEach(b => {
    if (allOpen) {
      b.classList.remove('open');
      b.querySelector('.solution-header span:last-child').textContent = '▼';
    } else {
      b.classList.add('open');
      b.querySelector('.solution-header span:last-child').textContent = '▲';
    }
  });
}

function filterQuestion(qid) {
  const tabs = document.querySelectorAll('.tab-btn');
  tabs.forEach(t => t.classList.remove('active'));
  event.target.classList.add('active');

  const cards = document.querySelectorAll('.q-card');
  if (qid === 'all') {
    cards.forEach(c => c.style.display = 'block');
  } else {
    cards.forEach(c => {
      if (c.id === qid) {
        c.style.display = 'block';
      } else {
        c.style.display = 'none';
      }
    });
  }
}

function checkQ1() {
  const val = document.getElementById('ans_q1_collisions').value.trim();
  const fb = document.getElementById('feedback_q1');
  if (val === '6') {
    fb.innerHTML = '✅ ถูกต้องสมบูรณ์แบบ! (0+1+1+1+1+2 = 6 ครั้ง)';
    fb.style.color = '#15803d';
  } else if (val === '12') {
    fb.innerHTML = '❌ ติดกับดักอาจารย์! ห้ามนับเบิ้ล "ชน 6 แก้ 6" ตอบ 6 ครั้งเท่านั้น';
    fb.style.color = '#b91c1c';
  } else {
    fb.innerHTML = '❌ ยังไม่ถูกต้อง (ลองดูในตารางเฉลยสเต็ปการชน)';
    fb.style.color = '#b91c1c';
  }
}

function checkQ7() {
  const val = document.getElementById('ans_q7_edges').value.trim();
  const fb = document.getElementById('feedback_q7');
  if (val === '66') {
    fb.innerHTML = '✅ ถูกต้อง! 12 × 11 / 2 = 66 เส้น (ตอบเป็นตัวเลขจำนวนเต็ม)';
    fb.style.color = '#15803d';
  } else {
    fb.innerHTML = '❌ ยังไม่ถูกต้อง (สูตร n(n-1)/2 ➔ 12 × 11 / 2 = 66)';
    fb.style.color = '#b91c1c';
  }
}
</script>

</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Built Interactive Web Exam: {HTML_OUT}")
