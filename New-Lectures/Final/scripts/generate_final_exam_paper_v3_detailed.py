"""
Final Exam Paper Generator (Version 3 - Comprehensive & Detailed Sub-Questions)
Course: 060243106 / 060223119 Data Structures and Algorithms
Faculty of Applied Science / Faculty of Information Technology, KMUTNB
Semester 1, Academic Year 2026
Instructor: Assoc. Prof. Dr. Pradit Pitaksatheinkul
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image as RLImage, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register Fonts
pdfmetrics.registerFont(TTFont('Tahoma', r'C:\Windows\Fonts\tahoma.ttf'))
pdfmetrics.registerFont(TTFont('Tahoma-Bold', r'C:\Windows\Fonts\tahomabd.ttf'))

OUTPUT_PDF = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\Final_Exam_2026_Paper_v3_Detailed.pdf'
DIAGRAM_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'diagrams')

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Tahoma", 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.drawString(36, 815, "Data Structures and Algorithms (060243106 / 060223119) — Final Exam 2026 (Detailed v3)")
            self.drawRightString(559, 815, f"Name: ............................................  ID: ........................")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(36, 810, 559, 810)

        # Footer
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(36, 32, 559, 32)
        
        self.drawString(36, 22, "KMUTNB Department of Computer and Information Science — Confidential Exam Paper")
        self.drawRightString(559, 22, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    style_title = ParagraphStyle('DocTitle', fontName='Tahoma-Bold', fontSize=12, leading=15, alignment=1, textColor=colors.HexColor('#0f172a'))
    style_subtitle = ParagraphStyle('DocSubTitle', fontName='Tahoma', fontSize=8.5, leading=11.5, alignment=1, textColor=colors.HexColor('#334155'))
    style_student_info = ParagraphStyle('StudentInfo', fontName='Tahoma', fontSize=8.5, leading=12, textColor=colors.HexColor('#1e293b'))
    style_section_h1 = ParagraphStyle('SectionH1', fontName='Tahoma-Bold', fontSize=10, leading=13.5, textColor=colors.HexColor('#1e3a8a'), spaceBefore=3, spaceAfter=2)
    style_sub_q = ParagraphStyle('SubQ', fontName='Tahoma-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor('#0f172a'))
    style_body = ParagraphStyle('Body', fontName='Tahoma', fontSize=8, leading=10.5, textColor=colors.HexColor('#1e293b'))
    style_body_bold = ParagraphStyle('BodyBold', fontName='Tahoma-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#0f172a'))
    style_table_cell = ParagraphStyle('TableCell', fontName='Tahoma', fontSize=7.5, leading=9.5, alignment=1, textColor=colors.HexColor('#0f172a'))
    style_table_cell_bold = ParagraphStyle('TableCellBold', fontName='Tahoma-Bold', fontSize=7.5, leading=9.5, alignment=1, textColor=colors.HexColor('#0f172a'))
    style_notice = ParagraphStyle('Notice', fontName='Tahoma-Bold', fontSize=7.5, leading=9.5, textColor=colors.HexColor('#b91c1c'))

    story = []

    # =========================================================================
    # PAGE 1: COVER HEADER & QUESTION 1: HASHING & DOUBLE HASHING
    # =========================================================================
    header_table_data = [
        [
            Paragraph("<b>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK</b><br/>"
                      "Faculty of Applied Science / Faculty of Information Technology<br/>"
                      "<b>FINAL EXAMINATION — SEMESTER 1, ACADEMIC YEAR 2026 (DETAILED VERSION 3)</b>", style_title)
        ],
        [
            Paragraph("<b>Course:</b> 060243106 & 060223119 Data Structures and Algorithms &nbsp;|&nbsp; "
                      "<b>Instructor:</b> Assoc. Prof. Dr. Pradit Pitaksatheinkul<br/>"
                      "<b>Duration:</b> 3 Hours (180 Mins) &nbsp;|&nbsp; <b>Total Score:</b> 70 Raw Marks (35% Final Grade) &nbsp;|&nbsp; <b>Open Book & Scientific Calculator Allowed</b>", style_subtitle)
        ]
    ]
    t_header = Table(header_table_data, colWidths=[523])
    t_header.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#1e3a8a')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 4))

    info_table_data = [
        [
            Paragraph("<b>Student Name:</b> ....................................................................................", style_student_info),
            Paragraph("<b>Student ID:</b> ........................................", style_student_info),
            Paragraph("<b>Section:</b> .............", style_student_info)
        ]
    ]
    t_info = Table(info_table_data, colWidths=[270, 180, 73])
    t_info.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 4))

    # Question 1
    story.append(Paragraph("<b>Question 1: Hashing & Open Addressing with Double Hashing (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "Given an empty Hash Table of size <b>TableSize = 19</b> (indices 0 to 18) using <b>Open Addressing</b> with <b>Double Hashing</b>.<br/>"
        "• Primary Hash Function: <b>h₀(X) = X mod 19</b><br/>"
        "• Collision Resolution Function: <b>f(i) = i × hash₂(X) = i × (17 - (X mod 17))</b> for probe i = 0, 1, 2, ...<br/>"
        "• Probe Sequence Address: <b>h_i(X) = (h₀(X) + f(i)) mod 19</b><br/>"
        "<b>Keys to insert sequentially:</b> [ 26, 45, 70, 85, 102, 123, 143, 155 ]",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>1.1 Step-by-Step Probe Calculation & Collision Tracing:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph("Show the complete hash calculations for each key. For keys experiencing collisions, record every probe step:", style_body))

    calc_headers = [
        Paragraph("<b>Key (X)</b>", style_table_cell_bold),
        Paragraph("<b>h₀(X) = X mod 19</b>", style_table_cell_bold),
        Paragraph("<b>hash₂(X) = 17 - (X mod 17)</b>", style_table_cell_bold),
        Paragraph("<b>Probe Sequence & Collision Trace</b>", style_table_cell_bold),
        Paragraph("<b>Final Slot</b>", style_table_cell_bold),
        Paragraph("<b>Collisions</b>", style_table_cell_bold)
    ]
    calc_rows = [calc_headers]
    for k in [26, 45, 70, 85, 102, 123, 143, 155]:
        calc_rows.append([
            Paragraph(f"<b>{k}</b>", style_table_cell),
            Paragraph("....................", style_table_cell),
            Paragraph("....................", style_table_cell),
            Paragraph("................................................................................", style_table_cell),
            Paragraph("..........", style_table_cell),
            Paragraph(".....", style_table_cell)
        ])
    t_calc = Table(calc_rows, colWidths=[45, 90, 115, 185, 48, 40])
    t_calc.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_calc)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.2 Final Hash Table Array Representation (Element & Info):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph("Fill in the table array below. Record <b>Element</b> (Key) and <b>Info</b> ('A' = Active, '-' = Empty):", style_body))

    ht_row1 = [Paragraph("<b>Index</b>", style_table_cell_bold)] + [Paragraph(f"<b>{i}</b>", style_table_cell) for i in range(19)]
    ht_row2 = [Paragraph("<b>Element</b>", style_table_cell_bold)] + [Paragraph("", style_table_cell) for _ in range(19)]
    ht_row3 = [Paragraph("<b>Info</b>", style_table_cell_bold)] + [Paragraph("", style_table_cell) for _ in range(19)]
    
    col_w = [43] + [25.26] * 19
    t_ht = Table([ht_row1, ht_row2, ht_row3], colWidths=col_w)
    t_ht.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_ht)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.3 Collisions Breakdown & Max Colliding Keys:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• Keys with 0 collisions: .................................................................... &nbsp;|&nbsp; "
        "Keys with 1 collision: ....................................................................<br/>"
        "• Which key(s) experienced the <b>maximum number of collisions</b>? ........................................................................<br/>"
        "&nbsp;&nbsp;Number of collisions: ......... collisions each &nbsp;|&nbsp; Slot locations of collisions: ........................................................................<br/>"
        "• <b>Total cumulative number of collisions</b> across all 8 insertions: ..................... collisions.",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.4 Load Factor & Rehashing Threshold Analysis:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "• Current Load Factor (λ = N / TableSize): ......................................................... (State exact fraction and percentage)<br/>"
        "• If Rehashing is triggered when the load factor reaches <b>λ ≥ 80%</b>:<br/>"
        "&nbsp;&nbsp;(a) Maximum number of elements allowed before Rehashing: .................................... elements.<br/>"
        "&nbsp;&nbsp;(b) How many <b>MORE keys</b> must be inserted before Rehashing occurs? .................................... more keys.<br/>"
        "&nbsp;&nbsp;(c) When Rehashing occurs, what must the <b>New Table Size</b> be? State the prime number rule and exact size: .........................",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: QUESTION 2: BINARY MIN-HEAP
    # =========================================================================
    story.append(Paragraph("<b>Question 2: Priority Queue (Binary Min-Heap) Tracing & Operations (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "Given an empty Binary Min-Heap represented as a 1D array using <b>1-based indexing</b> (Index 0 is unused / sentinel).<br/>"
        "<b>Keys to insert sequentially:</b> [ 64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20 ] (Total 12 keys).",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2.1 Fundamental Properties & 1D Array Mapping:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• State the 2 fundamental properties of a Binary Min-Heap:<br/>"
        "&nbsp;&nbsp;1. Structure Property: ....................................................................................................................................................<br/>"
        "&nbsp;&nbsp;2. Heap-Order Property: ....................................................................................................................................................<br/>"
        "• 1-Based Array Formulas for index i: Left Child = .................... &nbsp;|&nbsp; Right Child = .................... &nbsp;|&nbsp; Parent = .................... (Why is index 0 unused? ....................................)",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.2 Four Vertical Array Tracing Tables (Past Exam Official Format):</b> [4 Marks]", style_sub_q))
    story.append(Paragraph("Fill in the array contents after each operation. Write only final states. Follow classroom program behavior:", style_body))

    heap_table_headers = [
        Paragraph("<b>Index</b>", style_table_cell_bold),
        Paragraph("<b>2.1 After Insert 12 Keys</b>", style_table_cell_bold),
        Paragraph("<b>2.2 After deleteMin() #1</b>", style_table_cell_bold),
        Paragraph("<b>2.3 After Insert Key 3</b>", style_table_cell_bold),
        Paragraph("<b>2.4 After deleteMin() #2</b>", style_table_cell_bold)
    ]
    heap_rows = [heap_table_headers]
    for idx in range(13):
        idx_str = f"[{idx}]" if idx > 0 else "[0] (Unused)"
        heap_rows.append([
            Paragraph(f"<b>{idx_str}</b>", style_table_cell_bold),
            Paragraph("-" if idx == 0 else "", style_table_cell),
            Paragraph("-" if idx == 0 else ("N/A" if idx == 12 else ""), style_table_cell),
            Paragraph("-" if idx == 0 else "", style_table_cell),
            Paragraph("-" if idx == 0 else ("N/A" if idx == 12 else ""), style_table_cell),
        ])
    t_heap = Table(heap_rows, colWidths=[70, 113, 113, 113, 113])
    t_heap.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_heap)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.3 Tree Structure Diagrams:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph("Draw the complete binary tree structure corresponding to <b>Table 2.1</b> (All 12 keys) and <b>Table 2.4</b> (Final state):", style_body))
    
    # 2 boxes for drawing tree
    tree_box_data = [
        [
            Paragraph("<b>Tree Diagram: 2.1 After 12 Inserts</b><br/><br/><br/><br/><br/><br/><br/>", style_body),
            Paragraph("<b>Tree Diagram: 2.4 Final State (After deleteMin #2)</b><br/><br/><br/><br/><br/><br/><br/>", style_body)
        ]
    ]
    t_tree_box = Table(tree_box_data, colWidths=[256, 256])
    t_tree_box.setStyle(TableStyle([
        ('BOX', (0,0), (0,0), 0.8, colors.HexColor('#94a3b8')),
        ('BOX', (1,0), (1,0), 0.8, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_tree_box)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.4 'hole' Variable Tracing & Algorithmic Steps:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>deleteMin() #1:</b> Root (1) removed. Last element temp = 20 placed at hole. Trace hole positions during percolateDown:<br/>"
        "&nbsp;&nbsp;hole starts at index: ......... → compares children at ......... → hole moves to: ......... → compares children at ......... → hole moves to: .........<br/>"
        "• <b>Insert Key 3:</b> hole starts at index 12. Trace hole positions during percolateUp:<br/>"
        "&nbsp;&nbsp;hole at index 12 compares parent at index ......... → hole moves to: ......... → compares parent at index ......... → hole moves to: .........",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.5 Time Complexity Analysis:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• Worst-case time complexity of insert: .................... &nbsp;|&nbsp; Average-case time complexity of insert: ....................<br/>"
        "• Worst-case time complexity of deleteMin: .................... (Explain briefly why average insert is O(1): ................................................................)",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: QUESTION 3 (INSERTION SORT) & QUESTION 4 (SELECTION & BUBBLE SORT)
    # =========================================================================
    story.append(Paragraph("<b>Question 3: Insertion Sort Tracing & Position Moves (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("<b>3.1 Worst-Case Mathematical Analysis (N = 12 Elements):</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "• Write down the initial array of 12 elements representing the <b>Worst-Case input</b> (Warning: Wrong initial input = 0 marks):<br/>"
        "&nbsp;&nbsp;Initial Array: [ ...................................................................................................................................................................................... ]<br/>"
        "• State the formula for total position moves (shifts): ........................................................ &nbsp;|&nbsp; "
        "Total Position Moves for N = 12: = .................. moves.<br/>"
        "• Total element comparisons in Worst Case: = .................. comparisons.",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.2 Array Tracing Table:</b> Given input [ 61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2 ]: [4 Marks]", style_sub_q))
    
    ins_headers = [Paragraph("<b>Pass (p)</b>", style_table_cell_bold), Paragraph("<b>Key</b>", style_table_cell_bold)] + [Paragraph(f"<b>[{i}]</b>", style_table_cell_bold) for i in range(12)] + [Paragraph("<b>Moves</b>", style_table_cell_bold)]
    ins_rows = [ins_headers]
    # initial row
    init_data = [61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]
    ins_rows.append([Paragraph("Initial", style_table_cell_bold), Paragraph("-", style_table_cell)] + [Paragraph(str(v), style_table_cell) for v in init_data] + [Paragraph("-", style_table_cell)])
    for p_num in range(1, 12):
        key_val = str(init_data[p_num])
        ins_rows.append([Paragraph(f"p = {p_num}", style_table_cell_bold), Paragraph(key_val, style_table_cell)] + [Paragraph("", style_table_cell) for _ in range(12)] + [Paragraph("", style_table_cell)])
    
    t_ins = Table(ins_rows, colWidths=[40, 25] + [35]*12 + [38])
    t_ins.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_ins)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.3 Specific Pass Verification & Inversions Sum:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Pass p = 3 (Key 24):</b> Comparisons made: ............................................................ &nbsp;|&nbsp; Position Moves in this pass: ......... moves.<br/>"
        "• <b>Pass p = 6 (Key 32):</b> Comparisons made: ............................................................ &nbsp;|&nbsp; Position Moves in this pass: ......... moves.<br/>"
        "• <b>Grand Total of Position Moves</b> from start to finish: = .................. moves &nbsp;|&nbsp; Total Inversions in original array: = .................. inversions.",
        style_body
    ))
    story.append(Spacer(1, 4))

    # Question 4
    story.append(Paragraph("<b>Question 4: Selection Sort & Bubble Sort Tracing (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("Given the 8-element unsorted array: <b>[ 45, 18, 72, 31, 12, 88, 25, 60 ]</b>", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>4.1 Selection Sort Tracing (Pass-by-Pass):</b> [5 Marks]", style_sub_q))
    story.append(Paragraph(
        "For each round i (0 to 6), find the minimum element in unsorted subarray and swap with a[i]:<br/>"
        "• Round 0: min_idx = ......... (val = .........) → Swap with index 0 → Array: [ ............................................................................................ ]<br/>"
        "• Round 1: min_idx = ......... (val = .........) → Swap with index 1 → Array: [ ............................................................................................ ]<br/>"
        "• Round 2: min_idx = ......... (val = .........) → Swap with index 2 → Array: [ ............................................................................................ ]<br/>"
        "• Round 3: min_idx = ......... (val = .........) → Swap with index 3 → Array: [ ............................................................................................ ]<br/>"
        "• Round 4: min_idx = ......... (val = .........) → Swap with index 4 → Array: [ ............................................................................................ ]<br/>"
        "• Total passes = ......... &nbsp;|&nbsp; Total element comparisons = ........................ &nbsp;|&nbsp; Total swaps = ......... swaps.",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4.2 Bubble Sort Tracing & Early Termination:</b> [5 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Pass 1 Tracing:</b> Detail all 7 adjacent comparisons and swaps:<br/>"
        "&nbsp;&nbsp;(45, 18) → ......... &nbsp;|&nbsp; (45, 72) → ......... &nbsp;|&nbsp; (72, 31) → ......... &nbsp;|&nbsp; (72, 12) → ......... &nbsp;|&nbsp; (72, 88) → ......... &nbsp;|&nbsp; (88, 25) → ......... &nbsp;|&nbsp; (88, 60) → .........<br/>"
        "&nbsp;&nbsp;Array after Pass 1: [ ............................................................................................ ] &nbsp;|&nbsp; Swaps in Pass 1: ......... swaps.<br/>"
        "• Total swaps from start to finish: = ......... swaps &nbsp;|&nbsp; Total outer loop passes made: ......... passes.<br/>"
        "• If optimized with a swap flag, at which pass does the algorithm terminate early? Pass: ......... (Explain: ................................................)",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: QUESTION 5: TOPOLOGICAL SORT
    # =========================================================================
    story.append(Paragraph("<b>Question 5: Topological Sort (Kahn's Algorithm on 7-Vertex DAG) (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "A Directed Acyclic Graph (DAG) with 7 vertices (1 to 7) and 12 directed edges is defined by the diagram and Adjacency List below.<br/>"
        "We execute <b>Kahn's Algorithm</b> using an Indegree table and a Circular Queue.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Side-by-side diagrams: Graph & Adjacency List
    graph_img_path = os.path.join(DIAGRAM_DIR, 'graph_topo_sort.png')
    adj_img_path = os.path.join(DIAGRAM_DIR, 'adj_topo_sort.png')
    
    diagram_row = []
    if os.path.exists(graph_img_path):
        diagram_row.append(RLImage(graph_img_path, width=250, height=125))
    else:
        diagram_row.append(Paragraph("Graph Diagram", style_body))
    
    if os.path.exists(adj_img_path):
        diagram_row.append(RLImage(adj_img_path, width=265, height=125))
    else:
        diagram_row.append(Paragraph("Adjacency List", style_body))
    
    t_diag_5 = Table([diagram_row], colWidths=[255, 268])
    t_diag_5.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_diag_5)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.1 Indegree Array Processing Table across All 7 Rounds:</b> [4 Marks]", style_sub_q))
    story.append(Paragraph("Record the Indegree count for each vertex in each round. Cross out values as vertices are removed:", style_body))

    indegree_headers = [Paragraph("<b>Round</b>", style_table_cell_bold), Paragraph("<b>Vertex Dequeued</b>", style_table_cell_bold)] + [Paragraph(f"<b>v_{i}</b>", style_table_cell_bold) for i in range(1, 8)]
    indegree_rows = [indegree_headers]
    indegree_rows.append([Paragraph("Initial", style_table_cell_bold), Paragraph("-", style_table_cell)] + [Paragraph("", style_table_cell) for _ in range(7)])
    for r in range(1, 8):
        indegree_rows.append([Paragraph(f"Round {r}", style_table_cell_bold), Paragraph("", style_table_cell)] + [Paragraph("", style_table_cell) for _ in range(7)])
    
    t_indegree = Table(indegree_rows, colWidths=[55, 95] + [53]*7)
    t_indegree.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_indegree)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>5.2 Circular Queue Tracing (Capacity 7, Slots 0 to 6):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph("The queue uses circular array indexing: <b>enqueue: back = (back+1)%7</b> and <b>dequeue: front = (front+1)%7</b>.<br/>"
                           "• Complete sequence of vertices <b>Enqueued</b> into Queue: ....................................................................................<br/>"
                           "• Complete sequence of vertices <b>Dequeued</b> from Queue: ....................................................................................", style_body))
    story.append(Spacer(1, 2))

    q_h1 = [Paragraph("<b>Slot Index</b>", style_table_cell_bold)] + [Paragraph(f"<b>[{i}]</b>", style_table_cell_bold) for i in range(7)]
    q_h2 = [Paragraph("<b>Final Queue Array</b>", style_table_cell_bold)] + [Paragraph("", style_table_cell) for _ in range(7)]
    t_q5 = Table([q_h1, q_h2], colWidths=[103] + [60]*7)
    t_q5.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_q5)
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "• <b>Final Pointer Locations:</b> front is at index: ......... &nbsp;|&nbsp; back is at index: ......... &nbsp;|&nbsp; currentSize = .........<br/>"
        "• Final Queue Status: [ &nbsp; ] Empty (0 elements) &nbsp;&nbsp;&nbsp;&nbsp; [ &nbsp; ] Non-empty (Data remains)",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>5.3 Final Topological Ordering:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "Write the resulting Topological Ordering sequence produced by Kahn's algorithm:<br/>"
        "<b>Answer:</b> ........................................................................................................................................................................................<br/>"
        "<font color='#b91c1c'><b>* CRITICAL ZERO-MARK WARNING:</b> Must write comma-separated sequence (e.g. 5, 7, 2, 1, 3, 4, 6). DO NOT write arrows (5 → 7 → 2...) which receives 0 marks!</font>",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.4 Cycle Detection & DAG Verification:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "How does Kahn's algorithm detect if a graph contains a cycle (is NOT a DAG)? State the exact mathematical condition:<br/>"
        "Answer: ........................................................................................................................................................................................",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: QUESTION 6: UNWEIGHTED SHORTEST PATH
    # =========================================================================
    story.append(Paragraph("<b>Question 6: Unweighted Shortest Path Algorithm (BFS) (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "A directed unweighted graph with 7 vertices (1 to 7) and 12 directed edges is given below. (<b>Source Vertex = 1</b>).<br/>"
        "We execute the BFS-based unweighted shortest path algorithm using a processing table and a Queue of capacity 7.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Side-by-side diagrams: Graph & Adjacency List
    graph_sp_path = os.path.join(DIAGRAM_DIR, 'graph_shortest_path.png')
    adj_sp_path = os.path.join(DIAGRAM_DIR, 'adj_shortest_path.png')
    
    diagram_row_6 = []
    if os.path.exists(graph_sp_path):
        diagram_row_6.append(RLImage(graph_sp_path, width=250, height=125))
    else:
        diagram_row_6.append(Paragraph("Graph Diagram", style_body))
    
    if os.path.exists(adj_sp_path):
        diagram_row_6.append(RLImage(adj_sp_path, width=265, height=125))
    else:
        diagram_row_6.append(Paragraph("Adjacency List", style_body))
    
    t_diag_6 = Table([diagram_row_6], colWidths=[255, 268])
    t_diag_6.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_diag_6)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.1 BFS Execution Table for Shortest Path (Source Vertex = 1):</b> [4 Marks]", style_sub_q))
    story.append(Paragraph("Fill in the processing array table containing Known (T / F), Distance (d_v), Previous Path (p_v), and Shortest Route:", style_body))

    sp_headers = [
        Paragraph("<b>Vertex (v)</b>", style_table_cell_bold),
        Paragraph("<b>Known (T / F)</b>", style_table_cell_bold),
        Paragraph("<b>Distance (d_v)</b>", style_table_cell_bold),
        Paragraph("<b>Previous Path (p_v)</b>", style_table_cell_bold),
        Paragraph("<b>Shortest Route from Source (1)</b>", style_table_cell_bold)
    ]
    sp_rows = [sp_headers]
    for v_num in range(1, 8):
        sp_rows.append([
            Paragraph(f"<b>v_{v_num}</b>", style_table_cell_bold),
            Paragraph("", style_table_cell),
            Paragraph("", style_table_cell),
            Paragraph("", style_table_cell),
            Paragraph("", style_table_cell)
        ])
    t_sp = Table(sp_rows, colWidths=[65, 80, 80, 100, 198])
    t_sp.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.2 Circular Queue State upon Completion (Capacity 7, Slots 0 to 6):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph("• Enqueue Sequence: ............................................................ &nbsp;|&nbsp; Dequeue Sequence: ............................................................", style_body))
    story.append(Spacer(1, 2))

    q6_h1 = [Paragraph("<b>Slot Index</b>", style_table_cell_bold)] + [Paragraph(f"<b>[{i}]</b>", style_table_cell_bold) for i in range(7)]
    q6_h2 = [Paragraph("<b>Final Queue Array</b>", style_table_cell_bold)] + [Paragraph("", style_table_cell) for _ in range(7)]
    t_q6 = Table([q6_h1, q6_h2], colWidths=[103] + [60]*7)
    t_q6.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_q6)
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "• front is at index: ......... &nbsp;|&nbsp; back is at index: ......... &nbsp;|&nbsp; currentSize: ......... &nbsp;|&nbsp; Status: [ &nbsp; ] Empty &nbsp;&nbsp; [ &nbsp; ] Non-empty",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.3 Shortest Path Reconstruction & Distance (4 Destinations):</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "<font color='#b91c1c'><b>* CRITICAL PROFESSOR'S RULE:</b> Must write comma-separated sequences ONLY (e.g. 1, 4, 5). DO NOT write arrows (1 → 4 → 5). Distance is measured in number of EDGES!</font><br/>"
        "• Shortest Path to <b>Vertex 5</b>: Distance = ......... edges &nbsp;|&nbsp; Route Sequence: = ........................................................................<br/>"
        "• Shortest Path to <b>Vertex 7</b>: Distance = ......... edges &nbsp;|&nbsp; Route Sequence: = ........................................................................<br/>"
        "• Shortest Path to <b>Vertex 6</b>: Distance = ......... edges &nbsp;|&nbsp; Route Sequence: = ........................................................................<br/>"
        "• Shortest Path to <b>Vertex 3</b>: Distance = ......... edges &nbsp;|&nbsp; Route Sequence: = ........................................................................",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.4 Algorithm Complexity & BFS Property:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• Time complexity of unweighted shortest path with Adjacency List: ....................................<br/>"
        "• Why does BFS guarantee the shortest path in unweighted graphs but fail in weighted graphs? ................................................................................",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: QUESTION 7: ADVANCED THEORY, STRUCTURAL PROPERTIES & CALCULATIONS
    # =========================================================================
    story.append(Paragraph("<b>Question 7: Advanced Theory, Structural Properties & Calculations (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("Answer the following questions concisely. All calculations must be computed as <b>exact integers or percentages</b> (No formulas/powers).", style_body))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.1 Structural Properties (Data Structures Classification):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "(a) Which fundamental data structure possesses exactly <b>two formal properties</b>? State the data structure and define both properties:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Data Structure: ........................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 1: ....................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 2: ....................................................................................................................................................................<br/>"
        "(b) Which tree data structure possesses exactly <b>three formal properties</b>? State the data structure and list all three properties:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Data Structure: ........................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Properties: ....................................................................................................................................................................",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.2 Hash Function Theoretical Properties & Realistic Limitation:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• State the <b>3 ideal properties</b> of a theoretical hash function:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;1. ....................................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;2. ....................................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;3. ....................................................................................................................................................................................<br/>"
        "• Which of these 3 properties is <b>impossible to achieve in practice</b>? ....................................................................................<br/>"
        "• State the <b>two fundamental reasons</b> why it is impossible:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Reason 1: ........................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Reason 2: ........................................................................................................................................................................",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.3 Graph Memory Waste Percentage (Sparse Graph Analysis):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "A directed graph has |V| = 7 vertices and |E| = 12 edges.<br/>"
        "• Total cells in Adjacency Matrix: .................................... cells.<br/>"
        "• Number and percentage of cells containing 1 (active edges): .................. cells &nbsp;(........................ %)<br/>"
        "• Number and percentage of cells containing 0 (wasted space): .................. cells &nbsp;(........................ %)<br/>"
        "• Total memory cells required if represented as an Adjacency List (|V| + |E|): .................................... cells.<br/>"
        "• Percentage of memory saved by Adjacency List compared to Adjacency Matrix: .................................... %",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.4 Complete Graph Edge Calculations:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "(a) A complete undirected graph K₁₆ has |V| = 16 vertices. Calculate the total number of edges as an <b>exact integer</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Calculation & Answer: ................................................................................................................................ edges.<br/>"
        "(b) A complete directed graph with 16 vertices without self-loops has: ............................................................ directed edges.",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.5 Complete Binary Tree Node Bounds:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "For a Complete Binary Tree where the Root is at height h = 0, calculate exact integer bounds:<br/>"
        "• Height h = 10: Minimum nodes = .................................... nodes &nbsp;|&nbsp; Maximum nodes = .................................... nodes.<br/>"
        "• Height h = 15: Minimum nodes = .................................... nodes &nbsp;|&nbsp; Maximum nodes = .................................... nodes.<br/>"
        "• Height h = 16: Minimum nodes = .................................... nodes &nbsp;|&nbsp; Maximum nodes = .................................... nodes.<br/>"
        "<font color='#b91c1c'>*(Strict rule: Answers MUST be computed exact integers, NOT exponential expressions like 2¹⁰ or 2¹⁶)*</font>",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.6 Binary Heap 1D Array Formulas:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "For a node located at index i in a 1-based array implementation of a Binary Heap, state the exact formula for:<br/>"
        "• Left Child Index: .................................... &nbsp;|&nbsp; Right Child Index: .................................... &nbsp;|&nbsp; Parent Index: ....................................<br/>"
        "• Why must integer floor division (i // 2) be used instead of rounding up? ................................................................................",
        style_body
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>*** END OF EXAMINATION PAPER — WISHING YOU THE BEST OF LUCK! ***</b>", ParagraphStyle('EndNotice', fontName='Tahoma-Bold', fontSize=8.5, leading=11, alignment=1, textColor=colors.HexColor('#1e3a8a'))))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built exam paper PDF: {OUTPUT_PDF}")

if __name__ == '__main__':
    build_pdf()
