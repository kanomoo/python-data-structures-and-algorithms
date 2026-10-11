"""
Final Exam Bilingual HTML Generator (2026 Official Suite)
Integrates all official SVG diagrams, 2-tier Double Hashing tables,
4-stage Min-Heap arrays and trees, DAG graphs, Adjacency Lists,
Shortest Path tables with strikethroughs, and Circular Queue visualizers.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svg_exam_components as sec

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ข้อสอบปลายภาค_Data_Structures_Final_Exam.html"
)

# Generate SVGs and HTML components
svg_graph_topo = sec.render_svg_graph_exam2026_topo(width=620, height=330)
adj_exam_topo = {
    1: [3, 4],
    2: [1],
    3: [4, 6],
    4: [6],
    5: [1, 2, 7],
    6: [],
    7: [2]
}
svg_adj_topo = sec.render_svg_adj_list(adj_exam_topo, title="Adjacency List: Directed Acyclic Graph (7 Vertices)", width=560, height=370)

svg_graph_sp = sec.render_svg_graph_exam2026_sp(width=620, height=340)
adj_exam_sp = {
    1: [2, 4],
    2: [4, 5, 7],
    3: [1, 6],
    4: [3, 5, 6, 7],
    5: [7],
    6: [],
    7: [6]
}
svg_adj_sp = sec.render_svg_adj_list(adj_exam_sp, title="Adjacency List: Directed Graph (Source = 1, 7 Vertices)", width=560, height=370)

# Double Hashing Data (Python 1D List Structure)
hash_table_solved_data = {
    3: {'key': '102', 'collision': '2', 'probes': '7, 5'},
    5: {'key': '85', 'collision': '2', 'probes': '9, 7'},
    7: {'key': '26', 'collision': '0', 'probes': '-'},
    9: {'key': '70', 'collision': '1', 'probes': '9'},
    10: {'key': '143', 'collision': '0', 'probes': '-'},
    13: {'key': '45', 'collision': '1', 'probes': '7'},
    16: {'key': '123', 'collision': '2', 'probes': '9, 3'},
    18: {'key': '155', 'collision': '1', 'probes': '3'},
}
html_hash_blank = sec.render_html_double_hashing_table({}, table_size=19, is_blank=True, title="ช่องจำลองกระดาษคำตอบข้อ 1.1: ตารางแฮชขนาด 19 ช่อง (ดัชนี 0 ถึง 18 ตามโครงสร้างภาษา Python)")
html_hash_solved = sec.render_html_double_hashing_table(hash_table_solved_data, table_size=19, is_blank=False, title="เฉลยตารางแฮชสมบูรณ์: แสดง Stored Key และประวัติการชน (Collisions) ตามโครงสร้างภาษา Python")

# Min-Heap Trees & Arrays
heap_12_keys = [None, 1, 6, 2, 10, 8, 15, 5, 64, 14, 20, 24, 20]
heap_del1 = [None, 2, 6, 5, 10, 8, 15, 20, 64, 14, 20, 24]
heap_ins3 = [None, 2, 6, 3, 10, 8, 5, 20, 64, 14, 20, 24, 15]
heap_del2 = [None, 3, 6, 5, 10, 8, 15, 20, 64, 14, 20, 24]

svg_heap_tree_12 = sec.render_svg_minheap_tree(heap_12_keys, title="Stage 1: Binary Min-Heap Tree หลังแทรกครบ 12 ตัว (Insert 12 Keys)", width=560, height=270)
svg_heap_tree_del1 = sec.render_svg_minheap_tree(heap_del1, title="Stage 2: Binary Min-Heap Tree หลัง deleteMin() ครั้งที่ 1", width=560, height=270)
svg_heap_tree_ins3 = sec.render_svg_minheap_tree(heap_ins3, title="Stage 3: Binary Min-Heap Tree หลังแทรกเลข 3 (Insert 3)", width=560, height=270)
svg_heap_tree_del2 = sec.render_svg_minheap_tree(heap_del2, title="Stage 4: Binary Min-Heap Tree หลัง deleteMin() ครั้งที่ 2", width=560, height=270)

html_heap_4_vertical = sec.render_html_heap_vertical_arrays([heap_12_keys, heap_del1, heap_ins3, heap_del2], labels=["1. Insert 12 Keys", "2. deleteMin() 1", "3. Insert key 3", "4. deleteMin() 2"])

# Topological Sort Tables & Queue
topo_indeg_solved_data = [
    {'vertex': '1', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '1', 'r2': '1', 'r3': '0 (In Q)', 'r4': 'ออก', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '2', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '1', 'r2': '0 (In Q)', 'r3': 'ออก', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '3', 'initial': '<del style="color:#94a3b8;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '1', 'r2': '1', 'r3': '1', 'r4': '0 (In Q)', 'r5': 'ออก', 'r6': '-', 'r7': '-'},
    {'vertex': '4', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '2', 'r2': '2', 'r3': '2', 'r4': '1', 'r5': '0 (In Q)', 'r6': 'ออก', 'r7': '-'},
    {'vertex': '5', 'initial': '<strong style="color:#15803d;">0</strong> (In Q)', 'r1': 'ออก', 'r2': '-', 'r3': '-', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '6', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '2', 'r2': '2', 'r3': '2', 'r4': '2', 'r5': '1', 'r6': '0 (In Q)', 'r7': 'ออก'},
    {'vertex': '7', 'initial': '<del style="color:#94a3b8;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '0 (In Q)', 'r2': 'ออก', 'r3': '-', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
]
html_topo_indeg_blank = sec.render_html_topo_indegree_table([{'vertex': str(i)} for i in range(1, 8)], queue_slots=['']*7, title="ช่องจำลองกระดาษคำตอบ: ตาราง Indegree Array Tracing (ขนาด 7 จุดยอด)", is_blank=True)
html_topo_indeg_solved = sec.render_html_topo_indegree_table(topo_indeg_solved_data, queue_slots=['5', '7', '2', '1', '3', '4', '6'], title="เฉลยตาราง Indegree Array Tracing ละเอียดครบ 7 รอบ", is_blank=False)
svg_topo_queue = sec.render_svg_circular_queue(['5', '7', '2', '1', '3', '4', '6'], front_idx=0, back_idx=6, current_size=0, title="สถานะ Circular Queue เมื่อจบขั้นตอน Topological Sort (front=0, back=6)")

# Shortest Path Tables & Queue
sp_rows_solved = [
    {'vertex': '1', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<strong style="color:#1e40af;">0</strong>', 'path': '<strong style="color:#1e40af;">0</strong>'},
    {'vertex': '2', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">1</strong>'},
    {'vertex': '3', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong>'},
    {'vertex': '4', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">1</strong>'},
    {'vertex': '5', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">2</strong>'},
    {'vertex': '6', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong>'},
    {'vertex': '7', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">2</strong>'}
]
html_sp_blank = sec.render_html_shortest_path_table([{'vertex': str(i)} for i in range(1, 8)], queue_slots=['']*7, title="ช่องจำลองกระดาษคำตอบ: ตารางประมวลผล Shortest Path (Known, Dist, Path)", source_vertex=1, is_blank=True)
html_sp_solved = sec.render_html_shortest_path_table(sp_rows_solved, queue_slots=['1', '2', '4', '5', '7', '3', '6'], title="เฉลยละเอียดตารางประมวลผล Shortest Path (การขีดฆ่าอัปเดตตามลำดับ BFS)", source_vertex=1, is_blank=False)
svg_sp_queue = sec.render_svg_circular_queue(['1', '2', '4', '5', '7', '3', '6'], front_idx=0, back_idx=6, current_size=0, title="สถานะ Circular Queue เมื่อจบขั้นตอน Shortest Path (front=0, back=6)")

html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ข้อสอบปลายภาค Data Structures & Algorithms (Final Exam 2026 ฉบับจริง + เฉลยละเอียด + รูปภาพและตารางตรงมาตรฐาน)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Chakra+Petch:wght@500;600;700&display=swap" rel="stylesheet">
<!-- MathJax configuration -->
<script>
  window.MathJax = {{
    tex: {{
      inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
      displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
    }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
  :root {{
    --primary: #0f172a;
    --primary-accent: #2563eb;
    --secondary-accent: #0284c7;
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --text-main: #1e293b;
    --text-muted: #64748b;
    --border-color: #cbd5e1;
    --success: #15803d;
    --success-bg: #f0fdf4;
    --danger: #b91c1c;
    --danger-bg: #fef2f2;
    --warning: #b45309;
    --warning-bg: #fffbeb;
  }}

  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--bg-page);
    color: var(--text-main);
    line-height: 1.6;
    margin: 0;
    padding: 24px;
  }}

  .container {{
    max-width: 1040px;
    margin: 0 auto;
    background: var(--bg-card);
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid var(--border-color);
  }}

  /* Header Section */
  .header {{
    text-align: center;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 20px;
    margin-bottom: 25px;
  }}
  .university-title {{
    font-family: 'Chakra Petch', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--primary);
    margin: 0 0 4px 0;
  }}
  .exam-title {{
    font-size: 19px;
    font-weight: 700;
    color: var(--primary-accent);
    margin: 4px 0;
  }}
  .course-info {{
    font-size: 15px;
    color: var(--text-muted);
    margin: 4px 0;
  }}
  .student-box {{
    display: flex;
    justify-content: space-between;
    background: #f1f5f9;
    padding: 12px 18px;
    border-radius: 6px;
    margin-top: 15px;
    font-size: 14.5px;
    font-weight: 500;
  }}

  /* Rules Box */
  .rules-box {{
    background: #eff6ff;
    border-left: 4px solid var(--primary-accent);
    padding: 14px 18px;
    margin-bottom: 25px;
    border-radius: 0 8px 8px 0;
    font-size: 14px;
  }}
  .rules-title {{
    font-weight: 700;
    color: #1e40af;
    margin-bottom: 6px;
  }}

  /* Section Headings */
  h1.section-heading {{
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
    padding: 12px 18px;
    border-radius: 8px;
    font-size: 18px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 20px;
  }}

  .part-title {{
    font-size: 17px;
    font-weight: 700;
    color: var(--primary);
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 25px;
    margin-bottom: 12px;
  }}

  .question-title {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    padding: 8px 14px;
    margin: 14px 0 8px 0;
    font-size: 15.5px;
    font-weight: 700;
    color: #1e3a8a;
  }}

  .score-badge {{
    background: #dbeafe;
    color: #1d4ed8;
    padding: 3px 9px;
    border-radius: 12px;
    font-size: 12.5px;
    font-weight: 700;
  }}

  /* Translations and Solutions */
  .thai-trans {{
    background-color: #f1f5f9;
    border-left: 3px solid #64748b;
    padding: 10px 14px;
    margin: 8px 0 12px 0;
    font-size: 14px;
    color: #334155;
    border-radius: 0 4px 4px 0;
  }}

  .blank-sheet-box {{
    background: #fafafa;
    border: 1.5px dashed #94a3b8;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 15px 0;
  }}

  .solution-box {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    padding: 16px 20px;
    margin: 16px 0;
    border-radius: 0 8px 8px 0;
    font-size: 14.5px;
  }}
  .solution-title {{
    font-size: 15px;
    font-weight: 700;
    color: #15803d;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .theory-box {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #2563eb;
    padding: 14px 18px;
    border-radius: 0 6px 6px 0;
    margin: 12px 0;
    font-size: 14px;
  }}

  .alert-box {{
    background: #fef2f2;
    border-left: 4px solid #dc2626;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin: 14px 0;
    font-size: 14px;
    color: #991b1b;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 13.5px;
  }}
  th, td {{
    border: 1px solid var(--border-color);
    padding: 8px 10px;
    text-align: left;
  }}
  th {{
    background-color: #f1f5f9;
    color: #334155;
    font-weight: 600;
  }}

  pre {{
    background-color: #1e293b;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 6px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 13px;
    line-height: 1.5;
  }}

  code {{
    font-family: 'JetBrains Mono', Consolas, monospace;
    background-color: #e2e8f0;
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 0.9em;
  }}

  .print-btn {{
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: #2563eb;
    color: white;
    border: none;
    padding: 12px 22px;
    border-radius: 50px;
    font-size: 15px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 1000;
  }}
  .print-btn:hover {{ background: #1d4ed8; }}

  @media print {{
    body {{ padding: 0; background: white; }}
    .container {{ box-shadow: none; border: none; padding: 0; max-width: 100%; }}
    .print-btn {{ display: none; }}
  }}
</style>
</head>
<body>

<div class="container">
  <!-- HEADER -->
  <div class="header">
    <div class="university-title">มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ (KMUTNB)</div>
    <div class="course-info">คณะเทคโนโลยีและการจัดการอุตสาหกรรม / คณะวิทยาศาสตร์ประยุกต์ | ภาคเรียนที่ 1 ปีการศึกษา 2569</div>
    <div class="exam-title">การสอบปลายภาค: วิชา 060243106 / 060223119 Data Structures and Algorithms</div>
    <div style="font-size:14px; color:#475569; margin-top:2px;">อาจารย์ผู้สอน: รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (Assoc. Prof. Dr. Pradit Pitaksatheinkul)</div>

    <div class="student-box">
      <div>ชื่อ-นามสกุล: ............................................................................</div>
      <div>รหัสนักศึกษา: ....................................................</div>
      <div>ตอนเรียน (Sec): .............</div>
    </div>
  </div>

  <!-- INSTRUCTIONS -->
  <div class="rules-box">
    <div class="rules-title">📌 ระเบียบและคำชี้แจงในการสอบ (Examination Regulations):</div>
    <ul style="margin:4px 0; padding-left:20px;">
      <li><strong>คะแนนรวมในข้อสอบ:</strong> 70 คะแนน (นำไปหาร 2 เหลือคะแนนเก็บสุทธิ 35 คะแนน) | เวลาสอบ: 3 ชั่วโมง</li>
      <li><strong>อุปกรณ์ที่อนุญาต:</strong> เปิดตำราและชีทเรียนได้ (Open Book), ใช้เครื่องคิดเลขได้ <strong>ห้ามใช้โทรศัพท์มือถือทุกกรณี</strong></li>
      <li><strong>กฎเหล็กการเขียนคำตอบ:</strong>
        <ul>
          <li><strong>เรื่องวิถี (Path):</strong> ต้องเขียนเป็นลำดับคั่นด้วย Comma เท่านั้น เช่น <code>1, 4, 5</code> (<strong>ห้ามใส่ลูกศร <code>-&gt;</code> เด็ดขาด ใครใส่ปรับ 0 คะแนนทันที</strong>)</li>
          <li><strong>ความยาววิถี (Path Length):</strong> ตอบเป็นจำนวน <strong>"เส้น" (Edges)</strong> เท่านั้น</li>
          <li><strong>Complete Graph:</strong> จำนวนเส้นเชื่อมต้องคำนวณเป็นตัวเลขจำนวนเต็ม ห้ามติดอยู่ในรูปสูตร</li>
        </ul>
      </li>
    </ul>
  </div>

  <!-- ========================================================================= -->
  <!-- PART 1: OFFICIAL EXAM 2026 QUESTIONS & DETAILED SOLUTIONS                -->
  <!-- ========================================================================= -->
  <h1 class="section-heading">🌟 ตอนที่ 1: ชุดข้อสอบปลายภาคฉบับจริงปี 2569 (Official Final Exam - 7 ข้อใหญ่ 70 คะแนน)</h1>

  <!-- QUESTION 1 -->
  <h2 class="part-title">Question 1: Hashing &amp; Open Addressing (Double Hashing) (18 คะแนน)</h2>

  <h3 class="question-title">
    <span>1.1 Double Hashing Table &amp; Probe Calculations</span>
    <span class="score-badge">Score: 8 Marks (8 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty hash table of size $\\text{{TableSize}} = 19$ (indexed from $0$ to $18$) using Python 1D List structure. Using <strong>Open Addressing</strong> with <strong>Double Hashing</strong> defined by:</p>
  $$\\text{{Primary Hash Function: }} h_0(X) = X \\bmod 19$$
  $$\\text{{Probe Formula: }} h_i(X) = (h_0(X) + f(i)) \\bmod 19 \\quad \\text{{where }} f(i) = i \\times (17 - (X \\bmod 17)) \\quad \\text{{for }} i = 0, 1, 2, \\dots$$
  <p>Insert the following sequence of keys sequentially into the hash table:</p>
  $$\\mathbf{{26, 45, 70, 85, 102, 123, 143, 155}}$$
  <p>Show all probe calculations ($h_0, h_1, h_2, \\dots$) for each key and fill the resulting hash table (1D Python List indexed from 0 to 18 with key values).</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดตารางแฮชว่างขนาด $19$ ช่อง (ดัชนี $0$ ถึง $18$) ตามโครงสร้างภาษา Python ใช้วิธี Open Addressing แบบ Double Hashing โดยมีฟังก์ชันแฮชหลัก $h_0(X) = X \\bmod 19$ และฟังก์ชันการกระจาย $f(i) = i \\times (17 - (X \\bmod 17))$ จงแทรกคีย์ $26, 45, 70, 85, 102, 123, 143, 155$ ลงในตารางแฮชตามลำดับ พร้อมแสดงวิธีคำนวณการชนและการแก้การชนทีละตัว และกรอกผลลัพธ์ลงในตารางแฮชให้สมบูรณ์ตามโครงสร้างภาษา Python
  </div>

  <div class="blank-sheet-box">
    {html_hash_blank}
  </div>

  <!-- SUB-QUESTION 1.2 -->
  <h3 class="question-title">
    <span>1.2 ข้อมูลตัวใดชนมากที่สุด ชนกี่ครั้ง และที่ตำแหน่งใด / Key with Maximum Collisions</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน: 1 + 1 + 1)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Which key(s) experienced the maximum number of collisions during insertion? How many collisions did they experience, and at which cell locations?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> ข้อมูลตัวใด ขณะใส่เข้าไปใน Hash Table แล้ว มีการชนกันและแก้การชนกันมากที่สุด (มีมากกว่า 1 ตัวก็ได้) และขณะใส่ข้อมูลตัวนั้น เกิดการชนกันกี่ครั้ง ที่ตำแหน่งใด?
  </div>
  <div class="blank-sheet-box">
    <p style="margin:0; font-size:15px; line-height:2;">
      ข้อมูลตัวที่มีการชนมากที่สุด คือ .................................................................... เกิดการชนกัน ............ ครั้ง ที่ตำแหน่ง ....................................................................
    </p>
  </div>

  <!-- SUB-QUESTION 1.3 -->
  <h3 class="question-title">
    <span>1.3 จำนวนการชนและแก้การชนรวมทั้งสิ้น / Total Cumulative Collisions</span>
    <span class="score-badge">Score: 3 Marks (3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> What is the total cumulative number of collisions and resolution steps that occurred during the insertion of all 8 keys?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> เกิดการชนกันและแก้การชนกันรวมทั้งสิ้นกี่ครั้งตลอดการใส่ข้อมูลครบทั้ง 8 ตัว?
  </div>
  <div class="blank-sheet-box">
    <p style="margin:0; font-size:15px; line-height:2;">
      เกิดการชนกันและแก้การชนกันรวมทั้งสิ้น ............ ครั้ง
    </p>
  </div>

  <!-- SUB-QUESTION 1.4 -->
  <h3 class="question-title">
    <span>1.4 จำนวนข้อมูลที่ต้องใส่เพิ่มอีกกี่ตัว จึงจะเกิดการ Rehashing / Threshold for Rehashing</span>
    <span class="score-badge">Score: 4 Marks (4 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> If the rehashing threshold policy is set to trigger when the load factor strictly exceeds <strong>80%</strong> of $\\text{{TableSize}} = 19$, how many <em>additional</em> keys must be inserted before rehashing occurs?</p>
  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> หากกำหนดเงื่อนไขให้ทำการ Rehash เมื่อตารางมีข้อมูลมากกว่า 80% หลังจากใส่ข้อมูลครบทั้ง 8 ตัวแล้ว จะต้องใส่ข้อมูลเพิ่มอีกอย่างน้อยกี่ตัว จึงจะเกิดการ Rehashing?
  </div>
  <div class="blank-sheet-box">
    <p style="margin:0; font-size:15px; line-height:2;">
      จะต้องใส่ข้อมูลเพิ่มอีก ............ ตัว จึงจะเกิดการ Rehash
    </p>
  </div>

  <!-- QUESTION 1 SOLUTIONS -->
  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. การคำนวณการชนและการแทรกทีละคีย์:</strong></p>
    <ul>
      <li><strong>Key 26:</strong> $h_0(26) = 26 \\bmod 19 = \\mathbf{{7}}$ &rarr; ช่อง 7 ว่าง &rarr; บรรจุลง <strong>ช่อง 7</strong> (ชน 0 ครั้ง)</li>
      <li><strong>Key 45:</strong> $h_0(45) = 45 \\bmod 19 = \\mathbf{{7}}$ &rarr; <em>ชนกับ 26 ที่ช่อง 7!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $s(45) = 17 - (45 \\bmod 17) = 17 - 11 = 6$<br>
        $i=1: h_1(45) = (7 + 1 \\times 6) \\bmod 19 = 13 \\bmod 19 = \\mathbf{{13}}$ &rarr; ช่อง 13 ว่าง &rarr; บรรจุลง <strong>ช่อง 13</strong> (ชน 1 ครั้ง)
      </li>
      <li><strong>Key 70:</strong> $h_0(70) = 70 \\bmod 19 = \\mathbf{{13}}$ &rarr; <em>ชนกับ 45 ที่ช่อง 13!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $s(70) = 17 - (70 \\bmod 17) = 17 - 2 = 15$<br>
        $i=1: h_1(70) = (13 + 1 \\times 15) \\bmod 19 = 28 \\bmod 19 = \\mathbf{{9}}$ &rarr; ช่อง 9 ว่าง &rarr; บรรจุลง <strong>ช่อง 9</strong> (ชน 1 ครั้ง)
      </li>
      <li><strong>Key 85:</strong> $h_0(85) = 85 \\bmod 19 = \\mathbf{{9}}$ &rarr; <em>ชนกับ 70 ที่ช่อง 9!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $s(85) = 17 - (85 \\bmod 17) = 17 - 0 = 17$<br>
        $i=1: h_1(85) = (9 + 1 \\times 17) \\bmod 19 = 26 \\bmod 19 = \\mathbf{{7}}$ &rarr; <em>ชนกับ 26 ที่ช่อง 7!</em> (ชนครั้งที่ 2)<br>
        $i=2: h_2(85) = (9 + 2 \\times 17) \\bmod 19 = 43 \\bmod 19 = \\mathbf{{5}}$ &rarr; ช่อง 5 ว่าง &rarr; บรรจุลง <strong>ช่อง 5</strong> (ชน 2 ครั้ง)
      </li>
      <li><strong>Key 102:</strong> $h_0(102) = 102 \\bmod 19 = \\mathbf{{7}}$ &rarr; <em>ชนกับ 26 ที่ช่อง 7!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $s(102) = 17 - (102 \\bmod 17) = 17 - 0 = 17$<br>
        $i=1: h_1(102) = (7 + 1 \\times 17) \\bmod 19 = 24 \\bmod 19 = \\mathbf{{5}}$ &rarr; <em>ชนกับ 85 ที่ช่อง 5!</em> (ชนครั้งที่ 2)<br>
        $i=2: h_2(102) = (7 + 2 \\times 17) \\bmod 19 = 41 \\bmod 19 = \\mathbf{{3}}$ &rarr; ช่อง 3 ว่าง &rarr; บรรจุลง <strong>ช่อง 3</strong> (ชน 2 ครั้ง)
      </li>
      <li><strong>Key 123:</strong> $h_0(123) = 123 \\bmod 19 = \\mathbf{{9}}$ &rarr; <em>ชนกับ 70 ที่ช่อง 9!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $s(123) = 17 - (123 \\bmod 17) = 17 - 4 = 13$<br>
        $i=1: h_1(123) = (9 + 1 \\times 13) \\bmod 19 = 22 \\bmod 19 = \\mathbf{{3}}$ &rarr; <em>ชนกับ 102 ที่ช่อง 3!</em> (ชนครั้งที่ 2)<br>
        $i=2: h_2(123) = (9 + 2 \\times 13) \\bmod 19 = 35 \\bmod 19 = \\mathbf{{16}}$ &rarr; ช่อง 16 ว่าง &rarr; บรรจุลง <strong>ช่อง 16</strong> (ชน 2 ครั้ง)
      </li>
      <li><strong>Key 143:</strong> $h_0(143) = 143 \\bmod 19 = \\mathbf{{10}}$ &rarr; ช่อง 10 ว่าง &rarr; บรรจุลง <strong>ช่อง 10</strong> (ชน 0 ครั้ง)</li>
      <li><strong>Key 155:</strong> $h_0(155) = 155 \\bmod 19 = \\mathbf{{3}}$ &rarr; <em>ชนกับ 102 ที่ช่อง 3!</em> (ชนครั้งที่ 1)<br>
        คำนวณก้าวเดิน: $s(155) = 17 - (155 \\bmod 17) = 17 - 2 = 15$<br>
        $i=1: h_1(155) = (3 + 1 \\times 15) \\bmod 19 = 18 \\bmod 19 = \\mathbf{{18}}$ &rarr; ช่อง 18 ว่าง &rarr; บรรจุลง <strong>ช่อง 18</strong> (ชน 1 ครั้ง)
      </li>
    </ul>

    {html_hash_solved}

    <p><strong>สรุปคำตอบข้อ 1.2 - 1.4:</strong></p>
    <ul>
      <li><strong>ข้อ 1.2 ข้อมูลที่ชนมากที่สุด:</strong> <strong>85, 102, 123</strong> (เกิดการชนตัวละ <strong>2 ครั้ง</strong> โดย 85 ชนที่ช่อง 9 และ 7 | 102 ชนที่ช่อง 7 และ 5 | 123 ชนที่ช่อง 9 และ 3)</li>
      <li><strong>ข้อ 1.3 จำนวนการชนรวม:</strong> $0 + 1 + 1 + 2 + 2 + 2 + 0 + 1 = \\mathbf{{9 \\text{{ ครั้ง}}}}$</li>
      <li><strong>ข้อ 1.4 จำนวนที่ต้องใส่เพิ่มก่อน Rehash:</strong><br>
        $\\text{{Threshold}} = \\lceil 19 \\times 0.80 \\rceil = \\lceil 15.2 \\rceil = \\mathbf{{16 \\text{{ คีย์}}}}$<br>
        ปัจจุบันใส่ไปแล้ว 8 คีย์ &rarr; ดังนั้นจะต้องใส่ข้อมูลเพิ่มอีก $16 - 8 = \\mathbf{{8 \\text{{ คีย์}}}}$ จึงจะเกิดการ Rehash
      </li>
    </ul>
  </div>

  <!-- QUESTION 2 -->
  <h2 class="part-title">Question 2: Priority Queue (Binary Min-Heap) (10 คะแนน)</h2>

  <h3 class="question-title">
    <span>2.1 Two Properties, Sequential Insertions, DeleteMin, and Array Mapping</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Binary Min-Heap implemented as a 1-based array (where index 0 is unused / sentinel). You are given the sequence of 12 keys:</p>
  $$\\mathbf{{64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20}}$$
  <p><strong>Tasks to complete:</strong></p>
  <ol>
    <li>State the <strong>two fundamental properties</strong> that define a Binary Min-Heap.</li>
    <li>Show the resulting Tree and Array after inserting all 12 keys sequentially.</li>
    <li>Perform the first <code>deleteMin()</code>. Show the resulting Tree and Array.</li>
    <li>Insert the key <code>3</code> into the heap. Show the resulting Tree and Array.</li>
    <li>Perform the second <code>deleteMin()</code>. Show the final Tree and Array.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนด Binary Min-Heap เปล่าที่เก็บในอาร์เรย์ 1 มิติ เริ่มต้นที่ดัชนี 1 (ดัชนี 0 ห้ามใช้) กำหนดชุดข้อมูล 12 ตัวคือ $64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20$ จงระบุคุณสมบัติ 2 ประการของฮีป, วาดต้นไม้และเขียนอาร์เรย์หลังแทรกครบ 12 ตัว, ทำ <code>deleteMin()</code> ครั้งที่ 1, แทรกเลข <code>3</code>, และทำ <code>deleteMin()</code> ครั้งที่ 2
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <div class="theory-box">
      <strong>📌 1. คุณสมบัติพื้นฐาน 2 ประการของ Binary Min-Heap (Two Fundamental Properties):</strong>
      <ol>
        <li><strong>Structure Property (คุณสมบัติเชิงโครงสร้าง):</strong> ต้องเป็น Complete Binary Tree คือโหนดจะเต็มสมบูรณ์ทุกชั้น ยกเว้นชั้นล่างสุดที่เต็มหรือไม่เต็มก็ได้ แต่หากไม่เต็ม โหนดจะต้องบรรจุชิดจากซ้ายไปขวาอย่างต่อเนื่องเสมอ</li>
        <li><strong>Heap-Order Property (คุณสมบัติเชิงอันดับ):</strong> สำหรับโหนด $X$ ใดๆ ที่มี Parent คือ $P$ ค่าใน Parent จะต้องน้อยกว่าหรือเท่ากับค่าใน Child เสมอ ($\\text{{Key}}(P) \\le \\text{{Key}}(X)$) ส่งผลให้โหนดที่มีค่าน้อยที่สุดจะอยู่ที่ Root เสมอ</li>
      </ol>
    </div>

    <p><strong>2. ผังต้นไม้ (Tree Diagrams) ครบทั้ง 4 ขั้นตอน:</strong></p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_heap_tree_12}</div>
      <div>{svg_heap_tree_del1}</div>
      <div>{svg_heap_tree_ins3}</div>
      <div>{svg_heap_tree_del2}</div>
    </div>

    <p><strong>3. ตารางอาร์เรย์แนวตั้ง 4 ตาราง (Vertical Arrays Matching Exam Paper):</strong></p>
    {html_heap_4_vertical}
  </div>

  <!-- QUESTION 3 -->
  <h2 class="part-title">Question 3: Insertion Sort Tracing &amp; Position Moves (10 คะแนน)</h2>

  <h3 class="question-title">
    <span>3.1 Tracing Array States &amp; Shifting Counts across Passes</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an array of 12 integers indexed from $0$ to $11$:</p>
  $$\\mathbf{{[9, 14, 2, 15, 6, 12, 1, 10, 5, 11, 7, 3]}}$$
  <p>Execute the standard <code>insertionSort</code> algorithm from pass $P = 1$ to $P = 11$. For each pass, show the complete array state after insertion, the element being inserted, and the exact count of position moves (element shifts) that occurred.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดอาร์เรย์ขนาด 12 ช่อง (ดัชนี 0 ถึง 11) จงรัน Insertion Sort จากรอบ $P = 1$ ถึง $P = 11$ โดยแสดงสถานะของอาร์เรย์หลังจบรอบ, ตัวเลขที่ถูกนำมาแทรก (tmp), และจำนวนครั้งของการเลื่อนตำแหน่งข้อมูล (position moves)
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. สูตรคำนวณกรณีแย่ที่สุด (Worst-Case Formula):</strong></p>
    $$\\text{{Max Comparisons/Moves}} = \\frac{{N(N-1)}}{{2}} = \\frac{{12 \\times 11}}{{2}} = 66 \\text{{ ครั้ง}}$$

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
    <p><strong>จำนวนครั้งที่มีการขยับเลื่อนตำแหน่งรวม (Total Position Moves):</strong> $0+2+0+3+2+6+3+6+3+6+9 = \\mathbf{{40 \\text{{ ครั้ง}}}}$</p>
  </div>

  <!-- QUESTION 4 -->
  <h2 class="part-title">Question 4: Selection Sort &amp; Bubble Sort Tracing (10 คะแนน)</h2>

  <h3 class="question-title">
    <span>4.1 Selection Sort &amp; 4.2 Bubble Sort Tracing (5 + 5 = 10 Marks)</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the input array $\\mathbf{{[64, 25, 12, 22, 11]}}$.</p>
  <ol>
    <li>Show the state of the array after each pass of <strong>Selection Sort</strong> until fully sorted. State the min element identified and the swap made.</li>
    <li>Show the state of the array after each pass of <strong>Bubble Sort</strong> with early-termination flag checking.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> กำหนดอาร์เรย์ $[64, 25, 12, 22, 11]$ จงแสดงผลลัพธ์ของอาร์เรย์ในแต่ละรอบเมื่อเรียงลำดับด้วย Selection Sort (ระบุค่าต่ำสุดที่พบและการสลับ) และแสดงผลลัพธ์แต่ละรอบเมื่อเรียงลำดับด้วย Bubble Sort
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
  <h2 class="part-title">Question 5: Topological Sort in DAG (10 คะแนน)</h2>

  <h3 class="question-title">
    <span>5.1 Indegree Array Tracing &amp; Topological Ordering (Strict Comma Output Rule)</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> A Directed Acyclic Graph (DAG) with <strong>7 vertices (1 to 7)</strong> is given by the diagram and Adjacency List below:</p>
  
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
    <div>{svg_graph_topo}</div>
    <div>{svg_adj_topo}</div>
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
    {html_topo_indeg_blank}
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. ตารางค่า Indegree ทีละรอบ (Indegree Tracking Table):</strong></p>
    {html_topo_indeg_solved}

    <p><strong>2. การทำงานของ Circular Queue (ขนาด 7 ช่อง, ดัชนี 0..6):</strong></p>
    <div style="max-width:560px; margin:14px 0;">
      {svg_topo_queue}
    </div>

    <p><strong>3. ผลลัพธ์ Topological Ordering:</strong></p>
    <p style="font-size:18px; font-weight:bold; color:#1e40af; text-align:center; background:#dbeafe; padding:12px; border-radius:8px;">
      5, 7, 2, 1, 3, 4, 6
    </p>
    <div class="alert-box">
      <strong>🚨 กับดักได้ 0 คะแนน:</strong> ห้ามเขียนลูกศร เช่น <code>5 -&gt; 7 -&gt; 2 -&gt; ...</code> ต้องเขียน <code>5, 7, 2, 1, 3, 4, 6</code> เท่านั้น!
    </div>
  </div>

  <!-- QUESTION 6 -->
  <h2 class="part-title">Question 6: Unweighted Shortest Path (10 คะแนน)</h2>

  <h3 class="question-title">
    <span>6.1 BFS Processing Table, Shortest Path to v5 and v7 (With Strict Comma Output Rule)</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the directed graph $G = (V, E)$ with 7 vertices ($V = \\{{1, 2, 3, 4, 5, 6, 7\\}}$) defined by the diagram and Adjacency List below:</p>
  
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
    <div>{svg_graph_sp}</div>
    <div>{svg_adj_sp}</div>
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
    {html_sp_blank}
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <p><strong>1. ตารางประมวลผล Shortest Path (การขีดฆ่าอัปเดตตามลำดับ BFS):</strong></p>
    {html_sp_solved}

    <p><strong>2. ผังจำลอง Circular Queue เมื่อจบขั้นตอน:</strong></p>
    <div style="max-width:560px; margin:14px 0;">
      {svg_sp_queue}
    </div>

    <p><strong>3. คำตอบเส้นทางและระยะทาง (Strict Comma Notation):</strong></p>
    <ul>
      <li><strong>Shortest Path to Vertex 5:</strong> <strong style="color:#1e40af; font-size:16px;">1, 4, 5</strong> (หรือ <code>1, 2, 5</code>) &mdash; ความยาว (Length) = <strong>2</strong> (หรือ 2 เส้น)</li>
      <li><strong>Shortest Path to Vertex 7:</strong> <strong style="color:#1e40af; font-size:16px;">1, 2, 7</strong> (หรือ <code>1, 4, 7</code>) &mdash; ความยาว (Length) = <strong>2</strong> (หรือ 2 เส้น)</li>
    </ul>

    <div class="alert-box">
      <strong>🚨 กับดักได้ 0 คะแนนขั้นวิกฤต (Zero-Mark Arrow Trap):</strong><br>
      อ.ประดิษฐ์ สั่งเน้นย้ำหลายรอบว่า <strong>ห้ามเขียนลูกศรเด็ดขาด!</strong> (เช่น ห้ามเขียน <code>1 -&gt; 4 -&gt; 5</code>) ใครเขียนลูกศรจะถูกปรับ <strong>0 คะแนนทันทีทั้งข้อ</strong>!<br>
      ต้องเขียนเป็นลำดับคั่นด้วยเครื่องหมายจุลภาคเท่านั้น เช่น <strong><code>1, 4, 5</code></strong><br>
      และหน่วยของความยาวตอบเป็นจำนวน <strong>"เส้น" (Edges)</strong> ห้ามตอบหน่วยนิ้วหรือเซนติเมตร
    </div>
  </div>

  <!-- QUESTION 7 -->
  <h2 class="part-title">Question 7: Properties &amp; Theory Calculations (10 คะแนน)</h2>

  <h3 class="question-title">
    <span>7.1 Data Structure Properties, Ideal Hash, Memory Waste &amp; Tree Formulas</span>
    <span class="score-badge">Score: 10 Marks</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Answer the following sub-questions thoroughly:</p>
  <ol>
    <li>Which data structures are governed by <strong>2 properties</strong>? Which are governed by <strong>3 properties</strong>? State each property clearly.</li>
    <li>State 3 ideal theoretical properties of Hash Functions. Which one is impossible in practice, and why (2 reasons)?</li>
    <li>In a directed graph with $|V| = 7$ vertices and $|E| = 12$ edges stored as a $7 \\times 7$ Adjacency Matrix:
      <ul>
        <li>What percentage of memory entries are actively used (contain 1)?</li>
        <li>What percentage of memory entries are wasted (contain 0)?</li>
      </ul>
    </li>
    <li>How many edges are in a Complete Graph $K_{{16}}$? (Calculate as an exact integer).</li>
    <li>A Complete Binary Tree has height $H = 10$. What are the minimum and maximum possible number of nodes?</li>
    <li>State the 1-based array formulas for finding the Parent, Left Child, and Right Child of node at index $i$ in a Binary Heap.</li>
  </ol>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย):</strong> ตอบคำถามเชิงทฤษฎีและการคำนวณ: โครงสร้างใดมี 2 คุณสมบัติ/3 คุณสมบัติ, คุณสมบัติในอุดมคติของ Hash Function, เปอร์เซ็นต์ความสูญเสียในหน่วยความจำของ Adjacency Matrix, จำนวนเส้นใน Complete Graph $K_{{16}}$, จำนวนโหนดต่ำสุดและสูงสุดของ Complete Binary Tree สูง 10, และสูตร Parent/Left/Right Child ในอาร์เรย์ฮีป
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>
    
    <ol>
      <li><strong>โครงสร้างข้อมูลที่มี 2 คุณสมบัติ:</strong><br>
        • <strong>Binary Min-Heap:</strong> (1) Structure Property (Complete Binary Tree), (2) Heap-Order Property (Parent &le; Children)<br>
        • <strong>AVL Tree:</strong> (1) Binary Search Tree Property, (2) Balance Property ($|h_L - h_R| \\le 1$)<br>
        <strong>โครงสร้างข้อมูลที่มี 3 คุณสมบัติ:</strong><br>
        • <strong>Hashing:</strong> (1) Deterministic, (2) Uniform Distribution, (3) Fast Computation / Range Matching
      </li>
      <li><strong>คุณสมบัติในอุดมคติของ Hash Function 3 ข้อ:</strong><br>
        1. คำนวณง่ายและรวดเร็ว ($O(1)$)<br>
        2. กระจายคีย์ได้สม่ำเสมอทั่วทุกช่องในตาราง (Uniform Distribution)<br>
        3. คีย์ที่ต่างกันต้องได้ค่าดัชนีต่างกัน (One-to-One Mapping หรือ Perfect Hashing)<br>
        <strong>ข้อที่เป็นไปไม่ได้ในทางปฏิบัติ:</strong> <strong>ข้อ 3 (One-to-One Mapping)</strong><br>
        <em>สาเหตุ 2 ประการ:</em><br>
        (1) ขนาดของ Key Space มีค่าเป็นอนันต์หรือใหญ่กว่าขนาด TableSize มาก ($|K| \\gg \\text{{TableSize}}$)<br>
        (2) กฎช่องนกพิราบ (Pigeonhole Principle): เมื่อจำนวนคีย์มากกว่าจำนวนช่อง ย่อมเกิด Collision อย่างหลีกเลี่ยงไม่ได้
      </li>
      <li><strong>การคำนวณร้อยละความสูญเสียใน RAM (Adjacency Matrix $7 \\times 7$):</strong><br>
        • พื้นที่ทั้งหมดในตาราง: $7 \\times 7 = \\mathbf{{49 \\text{{ ช่อง}}}}$<br>
        • ช่องที่เป็น 1 (Used): $\\frac{{12}}{{49}} \\times 100 \\approx \\mathbf{{24.48\\%}}$<br>
        • ช่องที่เป็น 0 (Wasted): $\\frac{{37}}{{49}} \\times 100 \\approx \\mathbf{{75.52\\%}}$ (สูญเปล่าในหน่วยความจำ)
      </li>
      <li><strong>จำนวนเส้นเชื่อมใน Complete Graph $K_{{16}}$:</strong><br>
        $$\\text{{Edges}} = \\frac{{N(N-1)}}{{2}} = \\frac{{16 \\times 15}}{{2}} = \\frac{{240}}{{2}} = \\mathbf{{120 \\text{{ เส้น}}}}$$
      </li>
      <li><strong>จำนวนโหนดของ Complete Binary Tree สูง $H = 10$:</strong><br>
        • น้อยที่สุด (Minimum Nodes): $2^H = 2^{{10}} = \\mathbf{{1,024 \\text{{ โหนด}}}}$ (หรือ $H+1 = 11$ หากเป็นโหนดแบบ Binary Tree ทั่วไป)<br>
        • มากที่สุด (Maximum Nodes): $2^{{H+1}} - 1 = 2^{{11}} - 1 = 2,048 - 1 = \\mathbf{{2,047 \\text{{ โหนด}}}}$
      </li>
      <li><strong>สูตรการคำนวณตำแหน่งใน 1-Based Array Binary Heap:</strong><br>
        • $\\text{{Parent}}(i) = \\lfloor i / 2 \\rfloor$ (หรือ <code>i // 2</code> ใน Python)<br>
        • $\\text{{Left Child}}(i) = 2 \\times i$<br>
        • $\\text{{Right Child}}(i) = 2 \\times i + 1$
      </li>
    </ol>
  </div>

  <!-- ========================================================================= -->
  <!-- PART 2: INTERVIEW & WHITEBOARD SECRETS                                    -->
  <!-- ========================================================================= -->
  <h1 class="section-heading">🎯 ตอนที่ 2: คลังข้อสอบข้อเขียนย่อย &amp; หลักการที่ ดร.ประดิษฐ์ ย้ำในห้องเรียน</h1>

  <div class="theory-box">
    <h3 style="margin-top:0; color:#1e40af;">2.1 หลักการ Map ของ Binary Heap (Complete Binary Tree to 1D Array)</h3>
    <p>ทำไม Binary Heap จึงไม่จำเป็นต้องใช้ Pointer เชื่อมโยงเหมือน Linked Tree ทั่วไป?</p>
    <p><strong>คำตอบ:</strong> เพราะคุณสมบัติ <strong>Complete Binary Tree</strong> รับประกันว่าโหนดจะถูกเติมเต็มชิดซ้ายเสมอ จึงสามารถ Map ลงใน 1D Array ได้โดยไม่มีช่องว่าง (Gaps) ทำให้หา Parent และ Child ได้ด้วยสูตรคณิตศาสตร์ $\\lfloor i/2 \\rfloor, 2i, 2i+1$ ได้ทันทีในเวลา $O(1)$ ประหยัด Memory ของ Pointer และเพิ่ม Cache Locality</p>
  </div>

  <div class="theory-box">
    <h3 style="margin-top:0; color:#1e40af;">2.2 การ Trace ฟังก์ชัน insert(x) ด้วยตัวแปร hole</h3>
    <p>การแทรกข้อมูลใน Binary Min-Heap จะเปิดช่องว่างที่เรียกว่า <code>hole</code> ที่ตำแหน่งท้ายสุดของอาร์เรย์ (<code>currentSize + 1</code>) จากนั้นทำการเปรียบเทียบค่า <code>x</code> กับ Parent ที่ <code>hole // 2</code> หาก <code>x &lt; array[hole // 2]</code> จะเลื่อนค่า Parent ลงมาที่ <code>hole</code> และเลื่อน <code>hole = hole // 2</code> จนกว่าจะเจอตำแหน่งที่เหมาะสม (Percolate Up) จึงใส่ <code>x</code> ลงใน <code>hole</code></p>
  </div>

  <div class="theory-box">
    <h3 style="margin-top:0; color:#1e40af;">2.3 ไวยากรณ์การเรียกเมธอด deleteMin() ใน Python</h3>
    <p>ในภาษา Python คลาส BinaryHeap เมธอด <code>deleteMin()</code> <strong>ไม่มีการรับพารามิเตอร์ใดๆ</strong></p>
    <pre><code>min_val = heap.deleteMin()  # ถูกต้อง! ห้ามใส่พารามิเตอร์ เช่น heap.deleteMin(x) เด็ดขาด</code></pre>
  </div>

  <div class="theory-box">
    <h3 style="margin-top:0; color:#1e40af;">2.4 นิยามภาษาอังกฤษของหลักการ Wrap Around ใน Hashing &amp; Queue</h3>
    <p><strong>Wrap Around Definition:</strong> "The circular indexing mechanism where the pointer or probe index that reaches the end of the array (<code>size - 1</code>) cycles back to the beginning (<code>index 0</code>) using the modulo operator (<code>index % size</code>), avoiding array boundary overflow."</p>
  </div>

  <div class="theory-box">
    <h3 style="margin-top:0; color:#1e40af;">2.5 การเลือกค่า R ในสูตร Double Hashing</h3>
    <p>ในสูตร $f(i) = i \\times (R - (X \\bmod R))$ ค่า $R$ จะต้องเป็น <strong>จำนวนเฉพาะ (Prime Number) ที่น้อยกว่า TableSize</strong> เสมอ เพื่อให้ค่า step size ที่ได้เป็นจำนวนเต็มบวก ($1 \\le \\text{{step}} \\le R$) และเป็น Coprime กับ TableSize ป้องกันการวนลูปไม่ทั่วตาราง</p>
  </div>

  <!-- ========================================================================= -->
  <!-- PART 3: ZERO-SCORE TRAPS MATRIX                                          -->
  <!-- ========================================================================= -->
  <h1 class="section-heading">🛑 ตอนที่ 3: ตารางสรุป 12 กับดักได้ 0 คะแนน (Zero-Score Traps Cheat Sheet)</h1>

  <table>
    <thead>
      <tr style="background:#1e293b; color:white;">
        <th style="width:50px; text-align:center;">ข้อที่</th>
        <th style="width:220px;">หัวข้อ / โจทย์</th>
        <th>กับดักที่ทำให้ได้ 0 คะแนน</th>
        <th>คำตอบที่ถูกต้องตามเกณฑ์ อ.ประดิษฐ์</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align:center; font-weight:bold;">1</td>
        <td><strong>การเขียน Shortest Path</strong></td>
        <td>เขียนลูกศร เช่น <code>1 -&gt; 4 -&gt; 5</code> หรือ <code>A -&gt; C -&gt; D</code></td>
        <td>เขียนคั่นด้วย Comma เท่านั้น: <strong><code>1, 4, 5</code></strong></td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">2</td>
        <td><strong>หน่วยของความยาววิถี (Path Length)</strong></td>
        <td>ตอบหน่วยเป็นนิ้ว, ซม., หรือกิโลเมตร</td>
        <td>ตอบเป็นจำนวน <strong>"เส้น"</strong> (Edges) หรือตัวเลขจำนวนเต็ม</td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">3</td>
        <td><strong>Topological Ordering</strong></td>
        <td>เขียนลูกศร เช่น <code>5 -&gt; 7 -&gt; 2 -&gt; 1</code></td>
        <td>เขียนเป็นลำดับคั่นด้วย Comma: <strong><code>5, 7, 2, 1, 3, 4, 6</code></strong></td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">4</td>
        <td><strong>Complete Graph</strong></td>
        <td>ตอบติดอยู่ในรูปสูตร เช่น $16(15)/2$</td>
        <td>คำนวณเป็นตัวเลขจำนวนเต็ม: <strong><code>120 เส้น</code></strong></td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">5</td>
        <td><strong>Binary Heap Array Index 0</strong></td>
        <td>ใส่ข้อมูล Root ลงที่ช่อง 0</td>
        <td>ช่อง 0 เว้นว่าง (unused/sentinel) Root ต้องเริ่มที่ <strong>ช่อง 1</strong></td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">6</td>
        <td><strong>การเรียก deleteMin() ใน Python</strong></td>
        <td>ส่งค่าเข้าไป เช่น <code>heap.deleteMin(2)</code></td>
        <td>เรียกแบบไม่มีพารามิเตอร์: <strong><code>heap.deleteMin()</code></strong></td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">7</td>
        <td><strong>นิยาม Connect ใน Graph</strong></td>
        <td>แปลว่า "ต่อเชื่อม"</td>
        <td>แปลว่า <strong>"ต่อเนื่อง"</strong> (มีวิถีเดินถึงกันได้)</td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">8</td>
        <td><strong>Adjacent ใน Directed Graph</strong></td>
        <td>ตอบสลับทิศทาง เช่น $(u, v)$ แล้วบอกว่า $u$ adjacent $v$</td>
        <td>$(u, v)$ แปลว่า <strong>$v$ adjacent $u$</strong> (หัวลูกศร adjacent ท้ายลูกศร)</td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">9</td>
        <td><strong>การนับจำนวนการชนใน Hashing</strong></td>
        <td>เผลอนับการชนของคีย์ตัวอื่นมารวมด้วย (เช่น ตอบ 6 ครั้ง) หรือนับการชนและการแก้การชนแยกเป็น 2 ครั้ง</td>
        <td>นับเฉพาะการชนของตัวมันเองเท่านั้น (ตอบ 3 ครั้ง) และการชนกับการแก้การชนในแต่ละครั้งนับเป็น 1 ครั้ง ไม่ใช่นับเป็น 2 ครั้ง</td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">10</td>
        <td><strong>Circular Queue Wrap Around</strong></td>
        <td>บวก index เกินขนาดตาราง (เช่น 7) โดยไม่ mod</td>
        <td>ใช้สูตร Modulo เสมอ: <code>(index + 1) % TableSize</code></td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">11</td>
        <td><strong>Unweighted Shortest Path</strong></td>
        <td>ใช้ Dijkstra หรือคำนวณน้ำหนัก</td>
        <td>ใช้ <strong>BFS + Queue</strong> เท่านั้น</td>
      </tr>
      <tr>
        <td style="text-align:center; font-weight:bold;">12</td>
        <td><strong>Insertion Sort Worst Case</strong></td>
        <td>สับสนระหว่างจำนวนครั้งที่เปรียบเทียบกับการเลื่อนตำแหน่ง</td>
        <td>จำนวนครั้งเลื่อนตำแหน่งเท่ากับ $N(N-1)/2$ ในกรณีเรียงกลับหลัง</td>
      </tr>
    </tbody>
  </table>

  <div style="text-align:center; margin-top:40px; padding-top:20px; border-top:1px solid #cbd5e1; color:#64748b; font-size:14px;">
    เอกสารรวบรวมข้อสอบปลายภาคและเฉลยละเอียด Data Structures &amp; Algorithms (มจพ.) | จัดทำขึ้นเพื่อการเตรียมสอบปลายภาคอย่างสมบูรณ์แบบ
  </div>
</div>

<button class="print-btn" onclick="window.print()">
  🖨️ พิมพ์ข้อสอบ / บันทึก PDF (Print Exam)
</button>

</body>
</html>
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Master Final Exam HTML generated successfully at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
