"""
Graph Master Classroom Summary & Solutions HTML Generator
Integrates all official SVG diagrams from Lecture 10, Lecture 11, Assignment 4,
and Classroom Whiteboard/Exam 2026 leaks into a single comprehensive guide.
"""

import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svg_exam_components as sec

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "สรุปเนื้อหากราฟ_Graph_Master_Classroom_Summary.html"
)

# 1. SVGs for Lecture 10 & 11
svg_graph_l10 = sec.render_svg_graph_lecture10(width=620, height=330)
adj_l10 = {
    1: [2, 4, 3],
    2: [4, 5],
    3: [6],
    4: [6, 7, 3],
    5: [4, 7],
    6: [],
    7: [6]
}
svg_adj_l10 = sec.render_svg_adj_list(adj_l10, title="Adjacency List: Lecture 10 & 11 Graph (7 Vertices)", width=560, height=370)

# 2. SVGs for Assignment 4
svg_graph_a4 = sec.render_svg_graph_assignment4(width=620, height=330)
adj_a4 = {
    'A': ['B', 'C'],
    'B': ['C', 'E', 'G'],
    'C': ['D', 'E'],
    'D': ['A', 'F'],
    'E': ['D', 'F'],
    'F': [],
    'G': ['E']
}
svg_adj_a4 = sec.render_svg_adj_list(adj_a4, title="Adjacency List: Assignment 4 Worksheet (Vertices A..G)", width=560, height=370)

# 3. SVGs for 2026 Whiteboard Exam
svg_graph_topo26 = sec.render_svg_graph_exam2026_topo(width=620, height=330)
adj_topo26 = {
    1: [3, 4],
    2: [1],
    3: [4, 6],
    4: [6],
    5: [1, 2, 7],
    6: [],
    7: [2]
}
svg_adj_topo26 = sec.render_svg_adj_list(adj_topo26, title="Adjacency List: 2026 Exam DAG (7 Vertices)", width=560, height=370)

svg_graph_sp26 = sec.render_svg_graph_exam2026_sp(width=620, height=340)
adj_sp26 = {
    1: [2, 4],
    2: [4, 5, 7],
    3: [1, 6],
    4: [3, 5, 6, 7],
    5: [7],
    6: [],
    7: [6]
}
svg_adj_sp26 = sec.render_svg_adj_list(adj_sp26, title="Adjacency List: 2026 Exam Shortest Path (Source = 1)", width=560, height=370)

# 4. Tables and Queues
# Lecture 10 Topo Indegree
topo_l10_indeg_data = [
    {'vertex': '1', 'initial': '0 (In Q)', 'r1': 'ออก', 'r2': '-', 'r3': '-', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '2', 'initial': '1', 'r1': '0 (In Q)', 'r2': 'ออก', 'r3': '-', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '3', 'initial': '2', 'r1': '1', 'r2': '1', 'r3': '1', 'r4': '0 (In Q)', 'r5': 'ออก', 'r6': '-', 'r7': '-'},
    {'vertex': '4', 'initial': '3', 'r1': '2', 'r2': '1', 'r3': '0 (In Q)', 'r4': 'ออก', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '5', 'initial': '1', 'r1': '1', 'r2': '0 (In Q)', 'r3': 'ออก', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
    {'vertex': '6', 'initial': '3', 'r1': '3', 'r2': '3', 'r3': '3', 'r4': '2', 'r5': '1', 'r6': '0 (In Q)', 'r7': 'ออก'},
    {'vertex': '7', 'initial': '2', 'r1': '2', 'r2': '2', 'r3': '1', 'r4': '0 (In Q)', 'r5': '0', 'r6': 'ออก', 'r7': '-'},
]
html_topo_l10_table = sec.render_html_topo_indegree_table(topo_l10_indeg_data, queue_slots=['1', '2', '5', '4', '3', '7', '6'], title="ตาราง Indegree Tracing สำหรับโจทย์ Lecture 10 (ผลลัพธ์ Ordering: 1, 2, 5, 4, 3, 7, 6)")
svg_queue_l10_topo = sec.render_svg_circular_queue(['1', '2', '5', '4', '3', '7', '6'], front_idx=0, back_idx=6, current_size=0, title="Circular Queue เมื่อจบ Topological Sort ของ Lecture 10 (front=0, back=6)")

# Lecture 11 Shortest Path (Source = 3)
sp_l10_rows = [
    {'vertex': '1', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">3</strong>'},
    {'vertex': '2', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">1</strong>'},
    {'vertex': '3', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<strong style="color:#1e40af;">0</strong>', 'path': '<strong style="color:#1e40af;">0</strong>'},
    {'vertex': '4', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">1</strong>'},
    {'vertex': '5', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">3</strong>', 'path': '<strong style="color:#1e40af;">2</strong>'},
    {'vertex': '6', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">3</strong>'},
    {'vertex': '7', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">3</strong>', 'path': '<strong style="color:#1e40af;">4</strong>'}
]
html_sp_l10_table = sec.render_html_shortest_path_table(sp_l10_rows, queue_slots=['3', '6', '1', '2', '4', '5', '7'], title="ตารางประมวลผล Shortest Path: Lecture 11 (Source Vertex = 3)", source_vertex=3)
svg_queue_l10_sp = sec.render_svg_circular_queue(['3', '6', '1', '2', '4', '5', '7'], front_idx=0, back_idx=6, current_size=0, title="Circular Queue เมื่อจบ Shortest Path ของ Lecture 11 (front=0, back=6)")

# Assignment 4 Shortest Path (Source = A)
sp_a4_a_rows = [
    {'vertex': 'A', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<strong style="color:#1e40af;">0</strong>', 'path': '<strong style="color:#1e40af;">0</strong>'},
    {'vertex': 'B', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">A</strong>'},
    {'vertex': 'C', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">A</strong>'},
    {'vertex': 'D', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">C</strong>'},
    {'vertex': 'E', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">B</strong>'},
    {'vertex': 'F', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">3</strong>', 'path': '<strong style="color:#1e40af;">E</strong>'},
    {'vertex': 'G', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">B</strong>'}
]
html_sp_a4_a_table = sec.render_html_shortest_path_table(sp_a4_a_rows, queue_slots=['A', 'B', 'C', 'E', 'G', 'D', 'F'], title="ตารางประมวลผล Shortest Path: Assignment 4 (Source Vertex = A)", source_vertex='A')

# Assignment 4 Shortest Path (Source = B)
sp_a4_b_rows = [
    {'vertex': 'A', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">3</strong>', 'path': '<strong style="color:#1e40af;">D</strong>'},
    {'vertex': 'B', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<strong style="color:#1e40af;">0</strong>', 'path': '<strong style="color:#1e40af;">0</strong>'},
    {'vertex': 'C', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">B</strong>'},
    {'vertex': 'D', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">C</strong>'},
    {'vertex': 'E', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">B</strong>'},
    {'vertex': 'F', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">2</strong>', 'path': '<strong style="color:#1e40af;">E</strong>'},
    {'vertex': 'G', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">999</del> <strong style="color:#1e40af;">1</strong>', 'path': '<strong style="color:#1e40af;">B</strong>'}
]
html_sp_a4_b_table = sec.render_html_shortest_path_table(sp_a4_b_rows, queue_slots=['B', 'C', 'E', 'G', 'D', 'F', 'A'], title="ตารางประมวลผล Shortest Path: Assignment 4 (Source Vertex = B)", source_vertex='B')

# 2026 Shortest Path (Source = 1)
sp_rows_solved = [
    {'vertex': '1', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<strong style="color:#1e40af;">0</strong>', 'path': '<strong style="color:#1e40af;">0</strong>'},
    {'vertex': '2', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">1</strong>'},
    {'vertex': '3', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong>'},
    {'vertex': '4', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">1</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">1</strong>'},
    {'vertex': '5', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">2</strong>'},
    {'vertex': '6', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">4</strong>'},
    {'vertex': '7', 'known': '<del style="color:#dc2626;">F</del> <strong style="color:#15803d;">T</strong>', 'dist': '<del style="color:#94a3b8;">&infin;</del> <strong style="color:#1e40af;">2</strong>', 'path': '<del style="color:#94a3b8;">0</del> <strong style="color:#1e40af;">2</strong>'}
]

html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>คลังสรุปเนื้อหากราฟและเฉลยโจทย์ทุกชุด (Graph Master Classroom Summary &amp; Solutions)</title>
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
    --danger: #b91c1c;
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

  .header {{
    text-align: center;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 20px;
    margin-bottom: 25px;
  }}
  .header h1 {{
    font-family: 'Chakra Petch', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: var(--primary);
    margin: 0 0 6px 0;
  }}
  .header p {{
    font-size: 15px;
    color: var(--text-muted);
    margin: 0;
  }}

  /* Quick Navigation */
  .quick-nav {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    background: #f1f5f9;
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 25px;
  }}
  .quick-nav a {{
    color: #1e40af;
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 600;
    padding: 6px 12px;
    background: #ffffff;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
  }}
  .quick-nav a:hover {{ background: #dbeafe; }}

  /* Section Headings */
  h1.section-heading {{
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
    padding: 12px 18px;
    border-radius: 8px;
    font-size: 18px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 18px;
  }}

  .part-title {{
    font-size: 16.5px;
    font-weight: 700;
    color: var(--primary);
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 25px;
    margin-bottom: 12px;
  }}

  .theory-box {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #2563eb;
    padding: 14px 18px;
    border-radius: 0 6px 6px 0;
    margin: 14px 0;
    font-size: 14.5px;
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
    z-index: 1000;
  }}
  .print-btn:hover {{ background: #1d4ed8; }}

  @media print {{
    body {{ padding: 0; background: white; }}
    .container {{ box-shadow: none; border: none; padding: 0; max-width: 100%; }}
    .quick-nav, .print-btn {{ display: none; }}
  }}
</style>
</head>
<body>

<div class="container">
  <!-- HEADER -->
  <div class="header">
    <h1>🕸️ คลังสรุปเนื้อหากราฟและเฉลยโจทย์ทุกชุดจากห้องเรียน</h1>
    <p>Graph Master Classroom Summary &amp; Complete Step-by-Step Solutions | รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล</p>
  </div>

  <div class="quick-nav">
    <a href="#sec1">1. นิยามพื้นฐานและกฎ Path</a>
    <a href="#sec2">2. Complete Graph &amp; สูตรเส้น</a>
    <a href="#sec3">3. Adjacency Matrix &amp; List</a>
    <a href="#sec4">4. Topological Sort &amp; Queue</a>
    <a href="#sec5">5. Unweighted Shortest Path</a>
    <a href="#sec6">6. ตารางกับดัก 0 คะแนน</a>
  </div>

  <!-- SECTION 1 -->
  <div id="sec1">
    <h1 class="section-heading">1. นิยามพื้นฐานของกราฟและกฎเหล็กการเขียน Path (Graph Fundamentals)</h1>

    <div class="theory-box">
      <strong>1.1 นิยามสำคัญ: Connect = "ต่อเนื่อง ไม่ใช่ ต่อเชื่อม"</strong><br>
      อ.ประดิษฐ์ สั่งเน้นย้ำในชั่วโมงเรียนว่า <code>Connect</code> แปลว่า <strong>"ต่อเนื่อง"</strong> (หมายถึง มีวิถีเดินถึงกันได้ แม้ไม่มีเส้นเชื่อมตรง) <em>ไม่ใช่</em> "ต่อเชื่อม" (Adjacent)!<br>
      • กราฟไม่มีทิศทาง (Undirected Graph) จะเป็น <strong>Connected Graph</strong> ก็ต่อเมื่อ ทุกคู่จุดยอด $(u, v)$ มีเส้นทาง (Path) เชื่อมถึงกันได้<br>
      • ใน Directed Graph เรียกว่า <strong>Strongly Connected</strong> เมื่อมีวิถีแบบมีทิศทางเดินถึงกันได้ไป-กลับทุกคู่จุดยอด
    </div>

    <div class="theory-box">
      <strong>1.2 นิยาม Adjacent ในกราฟระบุทิศทาง (Directed Graph):</strong><br>
      พิจารณาคู่อันดับ $(u, v)$ ที่มีเส้นเชื่อมพุ่งจาก $u$ ไปยัง $v$ ($u \\rightarrow v$):<br>
      • <strong>$v$ is adjacent to $u$</strong> (หัวลูกศร adjacent ท้ายลูกศร) &mdash; ถูกต้องตามนิยาม!<br>
      • แต่ $u$ <em>ไม่ได้</em> adjacent กับ $v$ (ยกเว้นจะมีคู่อันดับ $(v, u)$ ย้อนกลับมาด้วย)
    </div>

    <div class="alert-box">
      <strong>🚨 กฎเหล็กการเขียนวิถี (Path) ในกระดาษคำตอบ:</strong><br>
      ห้ามเขียนเครื่องหมายลูกศรเด็ดขาด! เช่น ห้ามเขียน <code>A -&gt; B -&gt; C -&gt; D</code> (ปรับ 0 คะแนนทันทีทั้งข้อ!)<br>
      ต้องเขียนคั่นด้วย Comma เท่านั้น เช่น <strong><code>A, B, C, D</code></strong><br>
      และความยาววิถี (Length) ให้นับจำนวน <strong>"เส้นเชื่อม" (Edges)</strong> เท่านั้น เช่น วิถี <code>A, B, C, D</code> มีความยาว = <strong>3</strong> (ไม่ใช่ 4)
    </div>
  </div>

  <!-- SECTION 2 -->
  <div id="sec2">
    <h1 class="section-heading">2. Complete Graph ($K_N$) และสูตรคำนวณจำนวนเส้นเชื่อม</h1>

    <div class="theory-box">
      <strong>สูตรการคำนวณเส้นเชื่อมใน Complete Undirected Graph:</strong>
      $$\\text{{Edges}} = \\frac{{N(N - 1)}}{{2}}$$
      <strong>ตัวอย่างการคำนวณตามจำนวนจุดยอด:</strong><br>
      • 2 จุดยอด: $\\frac{{2 \\times 1}}{{2}} = \\mathbf{{1 \\text{{ เส้น}}}}$<br>
      • 3 จุดยอด: $\\frac{{3 \\times 2}}{{2}} = \\mathbf{{3 \\text{{ เส้น}}}}$<br>
      • 4 จุดยอด: $\\frac{{4 \\times 3}}{{2}} = \\mathbf{{6 \\text{{ เส้น}}}}$<br>
      • 5 จุดยอด: $\\frac{{5 \\times 4}}{{2}} = \\mathbf{{10 \\text{{ เส้น}}}}$<br>
      • 10 จุดยอด: $\\frac{{10 \\times 9}}{{2}} = \\mathbf{{45 \\text{{ เส้น}}}}$<br>
      • 16 จุดยอด ($K_{{16}}$ ในข้อสอบจริง 2569): $\\frac{{16 \\times 15}}{{2}} = \\frac{{240}}{{2}} = \\mathbf{{120 \\text{{ เส้น}}}}$
    </div>
  </div>

  <!-- SECTION 3 -->
  <div id="sec3">
    <h1 class="section-heading">3. การจัดเก็บกราฟและการวิเคราะห์ขยะใน RAM (Adjacency Matrix vs List)</h1>

    <p>ภาพกราฟต้นแบบจากชีทเรียน Lecture 10 &amp; 11 ($|V|=7, |E|=12$) และการแปลงเป็น Adjacency List:</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_graph_l10}</div>
      <div>{svg_adj_l10}</div>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 3.1 ตาราง Adjacency Matrix $7 \\times 7$ ที่เติมเต็มสมบูรณ์:</div>
      <table>
        <thead>
          <tr style="background:#1e293b; color:white; text-align:center;">
            <th>$u \\backslash v$</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th>
          </tr>
        </thead>
        <tbody style="text-align:center;">
          <tr><td><strong>1</strong></td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
          <tr><td><strong>2</strong></td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>
          <tr><td><strong>3</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
          <tr><td><strong>4</strong></td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>
          <tr><td><strong>5</strong></td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>
          <tr><td><strong>6</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
          <tr><td><strong>7</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
        </tbody>
      </table>

      <p><strong>3.2 เฉลยการคำนวณร้อยละความสูญเสียหน่วยความจำ (ข้อสอบภาษาอังกฤษยอดฮิต):</strong></p>
      <ul>
        <li>พื้นที่ทั้งหมดของเมทริกซ์: $7 \\times 7 = \\mathbf{{49 \\text{{ ช่อง}}}}$</li>
        <li>ช่องที่มีค่าเป็น 1 (Used Entries): $12$ ช่อง &rarr; คิดเป็น $\\frac{{12}}{{49}} \\times 100 = \\mathbf{{24.48\\%}}$</li>
        <li>ช่องที่มีค่าเป็น 0 (Wasted Memory): $49 - 12 = 37$ ช่อง &rarr; คิดเป็น $\\frac{{37}}{{49}} \\times 100 = \\mathbf{{75.52\\%}}$ (สูญเปล่าใน RAM!)</li>
      </ul>
      <p><em>สรุปเหตุผลทางวิชาการ:</em> Adjacency Matrix ไม่นิยมใช้ใน Sparse Graph เพราะสิ้นเปลืองพื้นที่จัดเก็บ $\\Theta(|V|^2)$ โดยเสียพื้นที่ไปกับเลข 0 ถึง 75.52%</p>
    </div>
  </div>

  <!-- SECTION 4 -->
  <div id="sec4">
    <h1 class="section-heading">4. Topological Sort &amp; Kahn's Algorithm พร้อมเฉลยละเอียด 2 โจทย์ใหญ่</h1>

    <!-- EXERCISE 1: LECTURE 10 -->
    <h2 class="part-title">โจทย์ที่ 1: กราฟในชีทเรียน Lecture 10 (หน้า 5-6)</h2>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_graph_l10}</div>
      <div>{svg_adj_l10}</div>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 ตาราง Indegree Tracing ละเอียดครบ 7 รอบ (Lecture 10):</div>
      {html_topo_l10_table}

      <p><strong>สถานะ Circular Queue (ขนาด 7 ช่อง, ดัชนี 0..6):</strong></p>
      <div style="max-width:560px; margin:12px 0;">
        {svg_queue_l10_topo}
      </div>

      <p><strong>Topological Ordering ที่ได้:</strong></p>
      <p style="font-size:17px; font-weight:bold; color:#1e40af; text-align:center; background:#dbeafe; padding:10px; border-radius:8px;">
        1, 2, 5, 4, 3, 7, 6
      </p>
    </div>

    <!-- EXERCISE 2: WHITEBOARD 2026 -->
    <h2 class="part-title">โจทย์ที่ 2: กราฟข้อสอบจริงกระดานดำปี 2569 (Topological Sort DAG)</h2>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_graph_topo26}</div>
      <div>{svg_adj_topo26}</div>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 ตาราง Indegree Tracing สำหรับข้อสอบปี 2569:</div>
      {sec.render_html_topo_indegree_table([
        {'vertex': '1', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '1', 'r2': '1', 'r3': '0 (In Q)', 'r4': 'ออก', 'r5': '-', 'r6': '-', 'r7': '-'},
        {'vertex': '2', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '1', 'r2': '0 (In Q)', 'r3': 'ออก', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
        {'vertex': '3', 'initial': '<del style="color:#94a3b8;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '1', 'r2': '1', 'r3': '1', 'r4': '0 (In Q)', 'r5': 'ออก', 'r6': '-', 'r7': '-'},
        {'vertex': '4', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '2', 'r2': '2', 'r3': '2', 'r4': '1', 'r5': '0 (In Q)', 'r6': 'ออก', 'r7': '-'},
        {'vertex': '5', 'initial': '<strong style="color:#15803d;">0</strong> (In Q)', 'r1': 'ออก', 'r2': '-', 'r3': '-', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'},
        {'vertex': '6', 'initial': '<del style="color:#94a3b8;">2</del> <del style="color:#ea580c;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '2', 'r2': '2', 'r3': '2', 'r4': '2', 'r5': '1', 'r6': '0 (In Q)', 'r7': 'ออก'},
        {'vertex': '7', 'initial': '<del style="color:#94a3b8;">1</del> <strong style="color:#15803d;">0</strong> (Q)', 'r1': '0 (In Q)', 'r2': 'ออก', 'r3': '-', 'r4': '-', 'r5': '-', 'r6': '-', 'r7': '-'}
      ], queue_slots=['5', '7', '2', '1', '3', '4', '6'], title="ตาราง Indegree Tracing: ข้อสอบจริงปี 2569 (ผลลัพธ์: 5, 7, 2, 1, 3, 4, 6)")}

      <p><strong>สถานะ Circular Queue เมื่อจบ:</strong></p>
      <div style="max-width:560px; margin:12px 0;">
        {sec.render_svg_circular_queue(['5', '7', '2', '1', '3', '4', '6'], front_idx=0, back_idx=6, current_size=0, title="สถานะ Queue จบขั้นตอน 2026 (front=0, back=6)")}
      </div>

      <p><strong>Topological Ordering ที่ได้:</strong></p>
      <p style="font-size:17px; font-weight:bold; color:#1e40af; text-align:center; background:#dbeafe; padding:10px; border-radius:8px;">
        5, 7, 2, 1, 3, 4, 6
      </p>
    </div>
  </div>

  <!-- SECTION 5 -->
  <div id="sec5">
    <h1 class="section-heading">5. Unweighted Shortest Path (BFS) พร้อมเฉลยละเอียด 3 โจทย์ใหญ่</h1>

    <!-- EXERCISE 1: FOR EXAMPLE GRAPH (START FROM 3) -->
    <h2 class="part-title">โจทย์ที่ 1: ชีท For Example Graph หน้า 4-5 (จุดเริ่มต้น Vertex 3)</h2>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_graph_l10}</div>
      <div>{svg_adj_l10}</div>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 ตารางประมวลผล Shortest Path (Source = 3):</div>
      {html_sp_l10_table}

      <div style="max-width:560px; margin:12px 0;">
        {svg_queue_l10_sp}
      </div>

      <p><strong>คำตอบข้อสอบหน้า 5:</strong></p>
      <ul>
        <li><strong>Shortest path จาก v3 ไป v5:</strong> <strong style="color:#1e40af;">3, 1, 2, 5</strong> (หรือ <code>3, 1, 4, 5</code>) &mdash; ความยาว (Length) = <strong>3</strong> (หรือ 3 เส้น)</li>
        <li><strong>Shortest path จาก v3 ไป v7:</strong> <strong style="color:#1e40af;">3, 1, 4, 7</strong> &mdash; ความยาว (Length) = <strong>3</strong> (หรือ 3 เส้น)</li>
      </ul>
      <p><em>วิธีไล่สายย้อนกลับ (Backtracking):</em> ดูที่โหนด 5 ในตาราง: $\\text{{Dist}}(5)=3$ และ $\\text{{Path}}(5)=2$ &rarr; ถอยกลับ: $5 \\leftarrow 2 \\leftarrow 1 \\leftarrow 3$ &rarr; ได้วิถี <code>3, 1, 2, 5</code></p>
    </div>

    <!-- EXERCISE 2: ASSIGNMENT 4 -->
    <h2 class="part-title">โจทย์ที่ 2: ใบงานส่งการบ้าน Assignment 4 (จุดเริ่มต้น A และ B)</h2>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_graph_a4}</div>
      <div>{svg_adj_a4}</div>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 ตารางเฉลย Assignment 4 (จุดเริ่มต้น A):</div>
      {html_sp_a4_a_table}
      <p><strong>ลำดับใน Queue:</strong> <code>A, B, C, E, G, D, F</code></p>

      <div class="solution-title" style="margin-top:20px;">💡 ตารางเฉลย Assignment 4 (จุดเริ่มต้น B):</div>
      {html_sp_a4_b_table}
      <p><strong>ลำดับใน Queue:</strong> <code>B, C, E, G, D, F, A</code></p>
    </div>

    <!-- EXERCISE 3: WHITEBOARD 2026 -->
    <h2 class="part-title">โจทย์ที่ 3: กราฟข้อสอบจริงกระดานดำปี 2569 (จุดเริ่มต้น Vertex 1)</h2>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:16px 0;">
      <div>{svg_graph_sp26}</div>
      <div>{svg_adj_sp26}</div>
    </div>

    <div class="solution-box">
      <div class="solution-title">💡 ตารางประมวลผล Shortest Path (Source = 1):</div>
      {sec.render_html_shortest_path_table(sp_rows_solved, queue_slots=['1', '2', '4', '5', '7', '3', '6'], title="ตารางประมวลผล Shortest Path ข้อสอบปี 2569 (Source = 1)", source_vertex=1)}

      <div style="max-width:560px; margin:12px 0;">
        {sec.render_svg_circular_queue(['1', '2', '4', '5', '7', '3', '6'], front_idx=0, back_idx=6, current_size=0, title="Circular Queue เมื่อจบขั้นตอน Shortest Path 2026 (front=0, back=6)")}
      </div>

      <p><strong>คำตอบเส้นทางและระยะทาง:</strong></p>
      <ul>
        <li><strong>Shortest path จาก 1 ไป 5:</strong> <strong style="color:#1e40af;">1, 4, 5</strong> (หรือ <code>1, 2, 5</code>) &mdash; ความยาว = <strong>2</strong> (หรือ 2 เส้น)</li>
        <li><strong>Shortest path จาก 1 ไป 7:</strong> <strong style="color:#1e40af;">1, 2, 7</strong> (หรือ <code>1, 4, 7</code>) &mdash; ความยาว = <strong>2</strong> (หรือ 2 เส้น)</li>
      </ul>
    </div>
  </div>

  <!-- SECTION 6 -->
  <div id="sec6">
    <h1 class="section-heading">6. ตารางสรุป 8 กับดัก 0 คะแนนในข้อสอบเรื่อง Graph (Zero-Score Traps)</h1>

    <table>
      <thead>
        <tr style="background:#1e293b; color:white;">
          <th style="width:50px; text-align:center;">ข้อที่</th>
          <th style="width:230px;">ประเด็นในข้อสอบ</th>
          <th>คำตอบที่ได้ 0 คะแนน (Trap)</th>
          <th>คำตอบที่ถูกต้องตามเกณฑ์ อ.ประดิษฐ์</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align:center; font-weight:bold;">1</td>
          <td><strong>การเขียนวิถี (Path)</strong></td>
          <td>เขียนลูกศร เช่น <code>A -&gt; B -&gt; C</code></td>
          <td>เขียนคั่นด้วย Comma: <strong><code>A, B, C</code></strong></td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">2</td>
          <td><strong>ความยาววิถี (Path Length)</strong></td>
          <td>ตอบหน่วยนิ้ว, ซม. หรือนับจำนวนจุดยอด (4)</td>
          <td>นับจำนวน <strong>"เส้นเชื่อม"</strong> (เช่น 3 หรือ 3 เส้น)</td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">3</td>
          <td><strong>Topological Ordering</strong></td>
          <td>เขียนลูกศร เช่น <code>1 -&gt; 2 -&gt; 5</code></td>
          <td>เขียนคั่นด้วย Comma: <strong><code>1, 2, 5, 4, 3, 7, 6</code></strong></td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">4</td>
          <td><strong>สูตร Complete Graph</strong></td>
          <td>ตอบติดรูปสมการ เช่น $10(9)/2$</td>
          <td>คำนวณเป็นตัวเลขเต็ม: <strong><code>45 เส้น</code></strong></td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">5</td>
          <td><strong>นิยาม Connect</strong></td>
          <td>ตอบว่า "ต่อเชื่อม"</td>
          <td>ตอบว่า <strong>"ต่อเนื่อง"</strong> (มีวิถีเดินถึงกันได้)</td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">6</td>
          <td><strong>นิยาม Adjacent ใน Directed Graph</strong></td>
          <td>$(u, v)$ แล้วบอกว่า $u$ adjacent $v$</td>
          <td>ตอบว่า <strong>$v$ adjacent $u$</strong></td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">7</td>
          <td><strong>สถานะ Circular Queue</strong></td>
          <td>ไม่ mod เมื่อค่าเกินขนาดตาราง</td>
          <td>ใช้สูตร <code>(index + 1) % 7</code> เสมอ</td>
        </tr>
        <tr>
          <td style="text-align:center; font-weight:bold;">8</td>
          <td><strong>ตรวจจับ Cycle ใน Topological Sort</strong></td>
          <td>ตอบว่าทำได้แม้วนลูป</td>
          <td>หากจำนวนโหนดที่ dequeue ได้ไม่ครบ $|V|$ แสดงว่ามี Cycle</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div style="text-align:center; margin-top:40px; padding-top:20px; border-top:1px solid #cbd5e1; color:#64748b; font-size:14px;">
    เอกสารสรุปเนื้อหากราฟ Data Structures &amp; Algorithms (มจพ.) | รวบรวมและจัดทำเพื่อความเป็นเลิศทางวิชาการ
  </div>
</div>

<button class="print-btn" onclick="window.print()">
  🖨️ พิมพ์เอกสาร / บันทึก PDF (Print Summary)
</button>

</body>
</html>
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Graph Master Classroom Summary generated successfully at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
