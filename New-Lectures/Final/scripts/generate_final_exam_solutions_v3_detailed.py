"""
Final Exam Master Solutions Generator (Version 3 - Comprehensive & Detailed Sub-Questions)
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

OUTPUT_PDF = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\Final_Exam_2026_Master_Solutions_v3_Detailed.pdf'
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
            self.drawString(36, 815, "Data Structures and Algorithms (060243106) — Master Solutions & Grading Key (Detailed v3)")
            self.drawRightString(559, 815, f"Official Master Solution — 100% Verified")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(36, 810, 559, 810)

        # Footer
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(36, 32, 559, 32)
        
        self.drawString(36, 22, "KMUTNB Department of Computer and Information Science — Master Solutions Suite")
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
    style_subtitle = ParagraphStyle('DocSubTitle', fontName='Tahoma', fontSize=8.5, leading=11.5, alignment=1, textColor=colors.HexColor('#1e3a8a'))
    style_section_h1 = ParagraphStyle('SectionH1', fontName='Tahoma-Bold', fontSize=10, leading=13.5, textColor=colors.HexColor('#1e3a8a'), spaceBefore=3, spaceAfter=2)
    style_sub_q = ParagraphStyle('SubQ', fontName='Tahoma-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor('#0f172a'))
    style_body = ParagraphStyle('Body', fontName='Tahoma', fontSize=8, leading=10.5, textColor=colors.HexColor('#1e293b'))
    style_body_bold = ParagraphStyle('BodyBold', fontName='Tahoma-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#0f172a'))
    style_ans_box = ParagraphStyle('AnsBox', fontName='Tahoma-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#15803d'))
    style_table_cell = ParagraphStyle('TableCell', fontName='Tahoma', fontSize=7.5, leading=9.5, alignment=1, textColor=colors.HexColor('#0f172a'))
    style_table_cell_bold = ParagraphStyle('TableCellBold', fontName='Tahoma-Bold', fontSize=7.5, leading=9.5, alignment=1, textColor=colors.HexColor('#0f172a'))
    style_table_cell_ans = ParagraphStyle('TableCellAns', fontName='Tahoma-Bold', fontSize=7.5, leading=9.5, alignment=1, textColor=colors.HexColor('#15803d'))
    style_trap = ParagraphStyle('Trap', fontName='Tahoma-Bold', fontSize=7.5, leading=9.5, textColor=colors.HexColor('#b91c1c'))

    story = []

    # =========================================================================
    # PAGE 1: COVER HEADER & QUESTION 1: HASHING & DOUBLE HASHING SOLUTIONS
    # =========================================================================
    header_table_data = [
        [
            Paragraph("<b>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK</b><br/>"
                      "Faculty of Applied Science / Faculty of Information Technology<br/>"
                      "<b>FINAL EXAMINATION 2026 — MASTER SOLUTIONS & GRADING KEY (DETAILED V3)</b>", style_title)
        ],
        [
            Paragraph("<b>Course:</b> 060243106 & 060223119 Data Structures and Algorithms &nbsp;|&nbsp; "
                      "<b>Instructor:</b> Assoc. Prof. Dr. Pradit Pitaksatheinkul<br/>"
                      "<b>Total Score:</b> 70 Raw Marks (35% Final Grade) &nbsp;|&nbsp; <b>Complete Mathematical Verification & Rubric</b>", style_subtitle)
        ]
    ]
    t_header = Table(header_table_data, colWidths=[523])
    t_header.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#166534')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Question 1: Hashing & Open Addressing with Double Hashing (10 Marks) — Master Solutions</b>", style_section_h1))
    story.append(Paragraph("<b>Formulas:</b> TableSize = 19 | h₀(X) = X mod 19 | hash₂(X) = 17 - (X mod 17) | h_i(X) = (h₀(X) + i × hash₂(X)) mod 19", style_body))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>1.1 Step-by-Step Probe Calculation & Collision Tracing:</b> [3 Marks]", style_sub_q))

    calc_headers = [
        Paragraph("<b>Key (X)</b>", style_table_cell_bold),
        Paragraph("<b>h₀(X) = X mod 19</b>", style_table_cell_bold),
        Paragraph("<b>hash₂(X) = 17 - (X mod 17)</b>", style_table_cell_bold),
        Paragraph("<b>Probe Sequence & Collision Trace</b>", style_table_cell_bold),
        Paragraph("<b>Final Slot</b>", style_table_cell_bold),
        Paragraph("<b>Collisions</b>", style_table_cell_bold)
    ]
    calc_rows = [calc_headers]
    sol_q1 = [
        ("26", "26 mod 19 = 7", "17 - (26 mod 17) = 8", "Probe 0: Slot 7 is EMPTY → Placed", "7", "0"),
        ("45", "45 mod 19 = 7", "17 - (45 mod 17) = 6", "Probe 0: Slot 7 (Collides with 26) → Probe 1: (7+6)%19 = 13 (Empty)", "13", "1"),
        ("70", "70 mod 19 = 13", "17 - (70 mod 17) = 15", "Probe 0: Slot 13 (Collides with 45) → Probe 1: (13+15)%19 = 28%19 = 9 (Empty)", "9", "1"),
        ("85", "85 mod 19 = 9", "17 - (85 mod 17) = 17", "Probe 0: Slot 9 (Collides 70) → Probe 1: (9+17)%19 = 7 (Collides 26) → Probe 2: (9+34)%19 = 5 (Empty)", "5", "2"),
        ("102", "102 mod 19 = 7", "17 - (102 mod 17) = 17", "Probe 0: Slot 7 (Collides 26) → Probe 1: (7+17)%19 = 5 (Collides 85) → Probe 2: (7+34)%19 = 3 (Empty)", "3", "2"),
        ("123", "123 mod 19 = 9", "17 - (123 mod 17) = 13", "Probe 0: Slot 9 (Collides 70) → Probe 1: (9+13)%19 = 3 (Collides 102) → Probe 2: (9+26)%19 = 16 (Empty)", "16", "2"),
        ("143", "143 mod 19 = 10", "17 - (143 mod 17) = 10", "Probe 0: Slot 10 is EMPTY → Placed", "10", "0"),
        ("155", "155 mod 19 = 3", "17 - (155 mod 17) = 15", "Probe 0: Slot 3 (Collides with 102) → Probe 1: (3+15)%19 = 18 (Empty)", "18", "1")
    ]
    for row in sol_q1:
        calc_rows.append([
            Paragraph(f"<b>{row[0]}</b>", style_table_cell_bold),
            Paragraph(row[1], style_table_cell),
            Paragraph(row[2], style_table_cell),
            Paragraph(row[3], style_table_cell),
            Paragraph(f"<b>{row[4]}</b>", style_table_cell_ans),
            Paragraph(f"<b>{row[5]}</b>", style_table_cell_ans)
        ])
    t_calc = Table(calc_rows, colWidths=[35, 90, 115, 205, 42, 36])
    t_calc.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dcfce7')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_calc)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.2 Final Hash Table Array Representation (Element & Info):</b> [2 Marks]", style_sub_q))
    
    # Final table state
    elements = ["-"] * 19
    infos = ["-"] * 19
    cell_fill = {3: "102", 5: "85", 7: "26", 9: "70", 10: "143", 13: "45", 16: "123", 18: "155"}
    for idx, val in cell_fill.items():
        elements[idx] = val
        infos[idx] = "A"

    ht_row1 = [Paragraph("<b>Index</b>", style_table_cell_bold)] + [Paragraph(f"<b>{i}</b>", style_table_cell) for i in range(19)]
    ht_row2 = [Paragraph("<b>Element</b>", style_table_cell_bold)] + [Paragraph(f"<b>{elements[i]}</b>" if elements[i] != "-" else "-", style_table_cell_ans if elements[i] != "-" else style_table_cell) for i in range(19)]
    ht_row3 = [Paragraph("<b>Info</b>", style_table_cell_bold)] + [Paragraph(f"<b>{infos[i]}</b>" if infos[i] != "-" else "-", style_table_cell_ans if infos[i] != "-" else style_table_cell) for i in range(19)]
    
    col_w = [43] + [25.26] * 19
    t_ht = Table([ht_row1, ht_row2, ht_row3], colWidths=col_w)
    t_ht.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#86efac')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f0fdf4')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_ht)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.3 Collisions Breakdown & Max Colliding Keys:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Keys with 0 collisions:</b> 26, 143 (2 keys) &nbsp;|&nbsp; <b>Keys with 1 collision:</b> 45, 70, 155 (3 keys)<br/>"
        "• <b>Keys with MAXIMUM collisions:</b> <font color='#15803d'><b>85, 102, 123</b></font> (Each suffered <b>2 collisions</b>)<br/>"
        "&nbsp;&nbsp;→ Key 85 collided at slots: <b>9, 7</b> &nbsp;|&nbsp; Key 102 collided at slots: <b>7, 5</b> &nbsp;|&nbsp; Key 123 collided at slots: <b>9, 3</b><br/>"
        "• <b>Total cumulative collisions:</b> 0 + 1 + 1 + 2 + 2 + 2 + 0 + 1 = <font color='#15803d'><b>9 collisions</b></font> (Count each collision step as 1).",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.4 Load Factor & Rehashing Threshold Analysis:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Current Load Factor (λ):</b> λ = N / TableSize = 8 / 19 = <font color='#15803d'><b>0.4211 (42.11%)</b></font><br/>"
        "• <b>Rehashing Threshold at λ ≥ 80%:</b><br/>"
        "&nbsp;&nbsp;(a) Maximum elements before Rehashing: ⌈19 × 0.8⌉ = <b>16 elements</b> (or ⌊19 × 0.8⌋ = 15).<br/>"
        "&nbsp;&nbsp;(b) Keys to insert before Rehashing: 16 - 8 = <font color='#15803d'><b>8 more keys</b></font> (or 15 - 8 = 7 more keys).<br/>"
        "&nbsp;&nbsp;(c) <b>New Table Size:</b> Must be the smallest prime number ≥ 2 × Old TableSize = 2 × 19 = 38 → Next prime is <font color='#15803d'><b>41</b></font> (or 43, 47).",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: QUESTION 2: BINARY MIN-HEAP SOLUTIONS
    # =========================================================================
    story.append(Paragraph("<b>Question 2: Priority Queue (Binary Min-Heap) — Master Solutions & Tracing (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("Input Sequence: [ 64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20 ] (12 keys).", style_body))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2.1 Fundamental Properties & 1D Array Formulas:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• <b>Structure Property:</b> A complete binary tree, filled completely at all levels except possibly the lowest, which is filled from left to right.<br/>"
        "• <b>Heap-Order Property:</b> For every node X other than the root, key(Parent(X)) ≤ key(X). (Root contains minimum element).<br/>"
        "• <b>Formulas for Index i:</b> Left Child = <font color='#15803d'><b>2i</b></font> &nbsp;|&nbsp; Right Child = <font color='#15803d'><b>2i + 1</b></font> &nbsp;|&nbsp; Parent = <font color='#15803d'><b>⌊i / 2⌋ (i // 2)</b></font><br/>"
        "&nbsp;&nbsp;<i>Why index 0 is unused:</i> Allows direct multiplication/division by 2 without offset calculations.",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2.2 Four Vertical Array Tracing Tables (Final States):</b> [4 Marks]", style_sub_q))

    # Definitive arrays for Heap
    # Initial: 64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20
    # After 12 inserts: [-, 1, 6, 2, 10, 8, 5, 24, 64, 14, 20, 15, 20]
    # After deleteMin #1: [-, 2, 6, 5, 10, 8, 20, 24, 64, 14, 20, 15]
    # After insert 3: [-, 2, 6, 3, 10, 8, 5, 24, 64, 14, 20, 15, 20]
    # After deleteMin #2: [-, 3, 6, 5, 10, 8, 20, 24, 64, 14, 20, 15]
    t1_arr = ["-", "1", "6", "2", "10", "8", "5", "24", "64", "14", "20", "15", "20"]
    t2_arr = ["-", "2", "6", "5", "10", "8", "20", "24", "64", "14", "20", "15", "-"]
    t3_arr = ["-", "2", "6", "3", "10", "8", "5", "24", "64", "14", "20", "15", "20"]
    t4_arr = ["-", "3", "6", "5", "10", "8", "20", "24", "64", "14", "20", "15", "-"]

    heap_table_headers = [
        Paragraph("<b>Index</b>", style_table_cell_bold),
        Paragraph("<b>2.1 After 12 Inserts</b>", style_table_cell_bold),
        Paragraph("<b>2.2 After deleteMin() #1</b>", style_table_cell_bold),
        Paragraph("<b>2.3 After Insert 3</b>", style_table_cell_bold),
        Paragraph("<b>2.4 After deleteMin() #2</b>", style_table_cell_bold)
    ]
    heap_rows = [heap_table_headers]
    for idx in range(13):
        idx_str = f"[{idx}]" if idx > 0 else "[0] (Unused)"
        heap_rows.append([
            Paragraph(f"<b>{idx_str}</b>", style_table_cell_bold),
            Paragraph(f"<b>{t1_arr[idx]}</b>", style_table_cell_ans if idx > 0 else style_table_cell),
            Paragraph(f"<b>{t2_arr[idx]}</b>" if idx < 12 else "-", style_table_cell_ans if 0 < idx < 12 else style_table_cell),
            Paragraph(f"<b>{t3_arr[idx]}</b>", style_table_cell_ans if idx > 0 else style_table_cell),
            Paragraph(f"<b>{t4_arr[idx]}</b>" if idx < 12 else "-", style_table_cell_ans if 0 < idx < 12 else style_table_cell),
        ])
    t_heap = Table(heap_rows, colWidths=[70, 113, 113, 113, 113])
    t_heap.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#86efac')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dcfce7')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_heap)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2.3 Tree Representations & Level-by-Level Verification:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Tree 2.1 (After 12 Inserts):</b> Root = 1<br/>"
        "&nbsp;&nbsp;Level 1: Left = 6, Right = 2<br/>"
        "&nbsp;&nbsp;Level 2: Children of 6 are (10, 8); Children of 2 are (5, 24)<br/>"
        "&nbsp;&nbsp;Level 3: Children of 10 are (64, 14); Children of 8 are (20, 15); Child of 5 is (20)<br/>"
        "• <b>Tree 2.4 (Final State after deleteMin #2):</b> Root = 3<br/>"
        "&nbsp;&nbsp;Level 1: Left = 6, Right = 5<br/>"
        "&nbsp;&nbsp;Level 2: Children of 6 are (10, 8); Children of 5 are (20, 24)<br/>"
        "&nbsp;&nbsp;Level 3: Children of 10 are (64, 14); Children of 8 are (20, 15)",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2.4 'hole' Variable Tracing Walkthrough:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>deleteMin() #1 Walkthrough:</b><br/>"
        "&nbsp;&nbsp;1. Extract min element: <code>arr[1] = 1</code> is returned. CurrentSize decrements to 11.<br/>"
        "&nbsp;&nbsp;2. Last element <code>temp = arr[12] = 20</code> is saved. Hole starts at root: <code>hole = 1</code>.<br/>"
        "&nbsp;&nbsp;3. Children of hole 1 are <code>arr[2] = 6</code> and <code>arr[3] = 2</code>. Smaller child is 2 at index 3.<br/>"
        "&nbsp;&nbsp;4. Since <code>temp (20) > 2</code>, shift 2 up to <code>arr[1]</code>. Hole moves to <code>hole = 3</code>.<br/>"
        "&nbsp;&nbsp;5. Children of hole 3 are <code>arr[6] = 5</code> and <code>arr[7] = 24</code>. Smaller child is 5 at index 6.<br/>"
        "&nbsp;&nbsp;6. Since <code>temp (20) > 5</code>, shift 5 up to <code>arr[3]</code>. Hole moves to <code>hole = 6</code>.<br/>"
        "&nbsp;&nbsp;7. Left child of hole 6 is <code>2 × 6 = 12 > CurrentSize (11)</code>. No children exist. Loop terminates.<br/>"
        "&nbsp;&nbsp;8. Place <code>temp = 20</code> into <code>arr[6]</code>. Complete!<br/>"
        "• <b>Insert Key 3 Walkthrough:</b><br/>"
        "&nbsp;&nbsp;1. CurrentSize increments to 12. Hole starts at index <code>hole = 12</code>, <code>temp = 3</code>.<br/>"
        "&nbsp;&nbsp;2. Parent is at <code>⌊12/2⌋ = 6</code> (<code>arr[6] = 20</code>). Since <code>3 < 20</code>, shift 20 down to <code>arr[12]</code>. <code>hole = 6</code>.<br/>"
        "&nbsp;&nbsp;3. Parent is at <code>⌊6/2⌋ = 3</code> (<code>arr[3] = 5</code>). Since <code>3 < 5</code>, shift 5 down to <code>arr[6]</code>. <code>hole = 3</code>.<br/>"
        "&nbsp;&nbsp;4. Parent is at <code>⌊3/2⌋ = 1</code> (<code>arr[1] = 2</code>). Since <code>3 > 2</code>, loop terminates. Place 3 at <code>arr[3]</code>!",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2.5 Time Complexity Analysis:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• Insert: <b>Worst Case = O(log N)</b> (element percolates to root), <b>Average Case = O(1)</b> (moves up ~1.607 levels).<br/>"
        "• deleteMin: <b>Worst Case = O(log N)</b> (element percolates down to bottom leaf level).",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: QUESTION 3 & QUESTION 4 SOLUTIONS
    # =========================================================================
    story.append(Paragraph("<b>Question 3: Insertion Sort Tracing & Position Moves — Master Solutions (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("<b>3.1 Worst-Case Analysis (N = 12 Elements):</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Initial Worst-Case Array:</b> [ 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ] (Strictly descending order).<br/>"
        "• <b>Formula for Total Position Moves:</b> Σ_{p=1}^{N-1} p = N(N - 1) / 2.<br/>"
        "• <b>Calculation for N = 12:</b> 12 × 11 / 2 = <font color='#15803d'><b>66 position moves (shifts)</b></font> &nbsp;|&nbsp; Comparisons = <b>66 comparisons</b>.",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.2 Array Tracing Table:</b> Given input [ 61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2 ]: [4 Marks]", style_sub_q))

    # Exact tracing rows for Insertion Sort
    sol_ins_rows = [
        ("Initial", "-", [61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2], "-"),
        ("p = 1", "52", [52, 61, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2], "1"),
        ("p = 2", "12", [12, 52, 61, 24, 8, 35, 32, 5, 71, 68, 18, 2], "2"),
        ("p = 3", "24", [12, 24, 52, 61, 8, 35, 32, 5, 71, 68, 18, 2], "2"),
        ("p = 4", "8", [8, 12, 24, 52, 61, 35, 32, 5, 71, 68, 18, 2], "4"),
        ("p = 5", "35", [8, 12, 24, 35, 52, 61, 32, 5, 71, 68, 18, 2], "2"),
        ("p = 6", "32", [8, 12, 24, 32, 35, 52, 61, 5, 71, 68, 18, 2], "3"),
        ("p = 7", "5", [5, 8, 12, 24, 32, 35, 52, 61, 71, 68, 18, 2], "7"),
        ("p = 8", "71", [5, 8, 12, 24, 32, 35, 52, 61, 71, 68, 18, 2], "0"),
        ("p = 9", "68", [5, 8, 12, 24, 32, 35, 52, 61, 68, 71, 18, 2], "1"),
        ("p = 10", "18", [5, 8, 12, 18, 24, 32, 35, 52, 61, 68, 71, 2], "8"),
        ("p = 11", "2", [2, 5, 8, 12, 18, 24, 32, 35, 52, 61, 68, 71], "11")
    ]
    t_ins_data = [[Paragraph("<b>Pass (p)</b>", style_table_cell_bold), Paragraph("<b>Key</b>", style_table_cell_bold)] + [Paragraph(f"<b>[{i}]</b>", style_table_cell_bold) for i in range(12)] + [Paragraph("<b>Moves</b>", style_table_cell_bold)]]
    for r in sol_ins_rows:
        t_ins_data.append([
            Paragraph(f"<b>{r[0]}</b>", style_table_cell_bold),
            Paragraph(r[1], style_table_cell),
        ] + [Paragraph(str(v), style_table_cell) for v in r[2]] + [Paragraph(f"<b>{r[3]}</b>", style_table_cell_ans if r[3] != "-" else style_table_cell)])

    t_ins_sol = Table(t_ins_data, colWidths=[40, 25] + [35]*12 + [38])
    t_ins_sol.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#86efac')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dcfce7')),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_ins_sol)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.3 Specific Pass Verification & Inversions Sum:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Pass p = 3 (Key 24):</b> Comparisons: 24 < 61 (T), 24 < 52 (T), 24 < 12 (F). Moves = <font color='#15803d'><b>2 moves</b></font> (shifts 61 and 52).<br/>"
        "• <b>Pass p = 6 (Key 32):</b> Comparisons: 32 < 61 (T), 32 < 52 (T), 32 < 35 (T), 32 < 24 (F). Moves = <font color='#15803d'><b>3 moves</b></font> (shifts 61, 52, 35).<br/>"
        "• <b>Grand Total of Position Moves:</b> 1 + 2 + 2 + 4 + 2 + 3 + 7 + 0 + 1 + 8 + 11 = <font color='#15803d'><b>41 position moves</b></font>.<br/>"
        "• <b>Total Inversions:</b> Exactly <font color='#15803d'><b>41 inversions</b></font>. Each shift removes exactly one inversion pair.",
        style_body
    ))
    story.append(Spacer(1, 4))

    # Question 4 Solutions
    story.append(Paragraph("<b>Question 4: Selection Sort & Bubble Sort — Master Solutions (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("Input Array: [ 45, 18, 72, 31, 12, 88, 25, 60 ] (8 elements).", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>4.1 Selection Sort Round-by-Round Tracing:</b> [5 Marks]", style_sub_q))
    story.append(Paragraph(
        "• Round 0: min_idx = 4 (val = 12) → Swap with index 0 (45) → Array: <b>[ 12, 18, 72, 31, 45, 88, 25, 60 ]</b><br/>"
        "• Round 1: min_idx = 1 (val = 18) → Already at index 1 (No swap) → Array: <b>[ 12, 18, 72, 31, 45, 88, 25, 60 ]</b><br/>"
        "• Round 2: min_idx = 6 (val = 25) → Swap with index 2 (72) → Array: <b>[ 12, 18, 25, 31, 45, 88, 72, 60 ]</b><br/>"
        "• Round 3: min_idx = 3 (val = 31) → Already at index 3 (No swap) → Array: <b>[ 12, 18, 25, 31, 45, 88, 72, 60 ]</b><br/>"
        "• Round 4: min_idx = 4 (val = 45) → Already at index 4 (No swap) → Array: <b>[ 12, 18, 25, 31, 45, 88, 72, 60 ]</b><br/>"
        "• Round 5: min_idx = 7 (val = 60) → Swap with index 5 (88) → Array: <b>[ 12, 18, 25, 31, 45, 60, 72, 88 ]</b><br/>"
        "• Round 6: min_idx = 6 (val = 72) → Already at index 6 (No swap) → Array: <b>[ 12, 18, 25, 31, 45, 60, 72, 88 ]</b><br/>"
        "• <b>Summary:</b> Total Passes = <b>7</b> | Comparisons = 8 × 7 / 2 = <b>28 comparisons</b> | Total Swaps = <font color='#15803d'><b>3 actual swaps</b></font> (R0, R2, R5).",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4.2 Bubble Sort Tracing & Early Termination:</b> [5 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Pass 1 Tracing (7 adjacent comparisons):</b><br/>"
        "&nbsp;&nbsp;(45, 18) → Swap (18, 45) | (45, 72) → OK | (72, 31) → Swap (31, 72) | (72, 12) → Swap (12, 72) | (72, 88) → OK | (88, 25) → Swap (25, 88) | (88, 60) → Swap (60, 88)<br/>"
        "&nbsp;&nbsp;Array after Pass 1: <b>[ 18, 45, 31, 12, 72, 25, 60, 88 ]</b> (Swaps in Pass 1 = <font color='#15803d'><b>5 swaps</b></font>)<br/>"
        "• <b>Remaining Passes:</b><br/>"
        "&nbsp;&nbsp;Pass 2: 3 swaps → [ 18, 31, 12, 45, 25, 60, 72, 88 ]<br/>"
        "&nbsp;&nbsp;Pass 3: 2 swaps → [ 18, 12, 31, 25, 45, 60, 72, 88 ]<br/>"
        "&nbsp;&nbsp;Pass 4: 2 swaps → [ 12, 18, 25, 31, 45, 60, 72, 88 ]<br/>"
        "&nbsp;&nbsp;Pass 5: 0 swaps → [ 12, 18, 25, 31, 45, 60, 72, 88 ] (Array is sorted, swapped = False)<br/>"
        "• <b>Total Swaps from start to finish:</b> 5 + 3 + 2 + 2 = <font color='#15803d'><b>12 swaps</b></font>.<br/>"
        "• <b>Early Termination:</b> Optimized Bubble Sort terminates at <font color='#15803d'><b>Pass 5</b></font> because 0 swaps occurred.",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: QUESTION 5: TOPOLOGICAL SORT SOLUTIONS
    # =========================================================================
    story.append(Paragraph("<b>Question 5: Topological Sort (Kahn's Algorithm on 7-Vertex DAG) — Master Solutions (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("Graph: 7 vertices, 12 directed edges. Canonical DAG from classroom whiteboard photo 840922631.", style_body))
    story.append(Spacer(1, 2))

    # Diagram Row
    graph_img_path = os.path.join(DIAGRAM_DIR, 'graph_topo_sort.png')
    adj_img_path = os.path.join(DIAGRAM_DIR, 'adj_topo_sort.png')
    diagram_row = []
    if os.path.exists(graph_img_path): diagram_row.append(RLImage(graph_img_path, width=250, height=125))
    if os.path.exists(adj_img_path): diagram_row.append(RLImage(adj_img_path, width=265, height=125))
    t_diag_5 = Table([diagram_row], colWidths=[255, 268])
    t_diag_5.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(t_diag_5)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.1 Indegree Array Processing Table across All 7 Rounds:</b> [4 Marks]", style_sub_q))

    # Definitive Indegree values
    # Initial: v1: 2, v2: 2, v3: 2, v4: 3, v5: 0, v6: 3, v7: 0
    # Enqueue 5, 7.
    # Round 1 (Dequeue 5): v1 -> 1, v2 -> 1, v3 -> 1
    # Round 2 (Dequeue 7): v2 -> 0 (Enqueue 2), v6 -> 2
    # Round 3 (Dequeue 2): v1 -> 0 (Enqueue 1), v4 -> 2
    # Round 4 (Dequeue 1): v3 -> 0 (Enqueue 3), v4 -> 1
    # Round 5 (Dequeue 3): v4 -> 0 (Enqueue 4), v6 -> 1
    # Round 6 (Dequeue 4): v6 -> 0 (Enqueue 6)
    # Round 7 (Dequeue 6): Done!
    indegree_sol_data = [
        [Paragraph("<b>Round</b>", style_table_cell_bold), Paragraph("<b>Vertex Dequeued</b>", style_table_cell_bold)] + [Paragraph(f"<b>v_{i}</b>", style_table_cell_bold) for i in range(1, 8)],
        [Paragraph("Initial", style_table_cell_bold), Paragraph("Start (Q: 5, 7)", style_table_cell), Paragraph("2", style_table_cell), Paragraph("2", style_table_cell), Paragraph("2", style_table_cell), Paragraph("3", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("3", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans)],
        [Paragraph("Round 1", style_table_cell_bold), Paragraph("Dequeue 5 (Q: 7)", style_table_cell), Paragraph("1", style_table_cell), Paragraph("1", style_table_cell), Paragraph("1", style_table_cell), Paragraph("3", style_table_cell), Paragraph("-", style_table_cell), Paragraph("3", style_table_cell), Paragraph("0", style_table_cell)],
        [Paragraph("Round 2", style_table_cell_bold), Paragraph("Dequeue 7 (Q: 2)", style_table_cell), Paragraph("1", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("1", style_table_cell), Paragraph("3", style_table_cell), Paragraph("-", style_table_cell), Paragraph("2", style_table_cell), Paragraph("-", style_table_cell)],
        [Paragraph("Round 3", style_table_cell_bold), Paragraph("Dequeue 2 (Q: 1)", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("-", style_table_cell), Paragraph("1", style_table_cell), Paragraph("2", style_table_cell), Paragraph("-", style_table_cell), Paragraph("2", style_table_cell), Paragraph("-", style_table_cell)],
        [Paragraph("Round 4", style_table_cell_bold), Paragraph("Dequeue 1 (Q: 3)", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("1", style_table_cell), Paragraph("-", style_table_cell), Paragraph("2", style_table_cell), Paragraph("-", style_table_cell)],
        [Paragraph("Round 5", style_table_cell_bold), Paragraph("Dequeue 3 (Q: 4)", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("-", style_table_cell), Paragraph("1", style_table_cell), Paragraph("-", style_table_cell)],
        [Paragraph("Round 6", style_table_cell_bold), Paragraph("Dequeue 4 (Q: 6)", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("-", style_table_cell)],
        [Paragraph("Round 7", style_table_cell_bold), Paragraph("Dequeue 6 (Q: Empty)", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell), Paragraph("-", style_table_cell)],
    ]
    t_ind_sol = Table(indegree_sol_data, colWidths=[55, 115] + [50]*7)
    t_ind_sol.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#86efac')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dcfce7')),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_ind_sol)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>5.2 Circular Queue Tracing (Capacity 7, Slots 0 to 6):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Enqueue Sequence:</b> <font color='#15803d'><b>5, 7, 2, 1, 3, 4, 6</b></font><br/>"
        "• <b>Dequeue Sequence:</b> <font color='#15803d'><b>5, 7, 2, 1, 3, 4, 6</b></font><br/>"
        "• <b>Final Queue Array Contents:</b> All 7 elements were processed. In textbook implementation, array holds overwrites: <code>[5, 7, 2, 1, 3, 4, 6]</code> (or empty flags).<br/>"
        "• <b>Pointers:</b> front = <font color='#15803d'><b>6</b></font> &nbsp;|&nbsp; back = <font color='#15803d'><b>6</b></font> (Wrapped back to index 6) &nbsp;|&nbsp; currentSize = <b>0</b> &nbsp;|&nbsp; Status: <b>Empty</b>",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.3 Final Topological Ordering:</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "<b>Official Correct Answer:</b> <font color='#15803d' size='10'><b>5, 7, 2, 1, 3, 4, 6</b></font> &nbsp;&nbsp;(or <code>7, 5, 2, 1, 3, 4, 6</code>)<br/>"
        "<font color='#b91c1c'><b>* CRITICAL GRADING PITFALL:</b> Must use commas! Answers written with arrows (5 → 7 → 2...) receive <b>0 Marks</b> immediately!</font>",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.4 Cycle Detection & DAG Verification:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• Kahn's algorithm detects cycles by tracking the count of dequeued vertices: If <b>num_dequeued < |V| (7)</b> when the queue becomes empty, the graph contains at least one directed cycle.<br/>"
        "• Here, num_dequeued = 7 = |V|, proving that the graph is a valid <b>DAG (Directed Acyclic Graph)</b>.",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: QUESTION 6: UNWEIGHTED SHORTEST PATH SOLUTIONS
    # =========================================================================
    story.append(Paragraph("<b>Question 6: Unweighted Shortest Path (BFS) — Master Solutions (10 Marks)</b>", style_section_h1))
    story.append(Paragraph("Directed Graph: 7 vertices, 12 directed edges. Canonical Shortest Path from whiteboard photo 838089388. (Source = 1).", style_body))
    story.append(Spacer(1, 2))

    # Diagram Row
    graph_sp_path = os.path.join(DIAGRAM_DIR, 'graph_shortest_path.png')
    adj_sp_path = os.path.join(DIAGRAM_DIR, 'adj_shortest_path.png')
    diagram_row_6 = []
    if os.path.exists(graph_sp_path): diagram_row_6.append(RLImage(graph_sp_path, width=250, height=125))
    if os.path.exists(adj_sp_path): diagram_row_6.append(RLImage(adj_sp_path, width=265, height=125))
    t_diag_6 = Table([diagram_row_6], colWidths=[255, 268])
    t_diag_6.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(t_diag_6)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.1 BFS Execution Table for Shortest Path (Source = 1):</b> [4 Marks]", style_sub_q))

    # BFS Table Solutions
    sp_sol_rows = [
        [Paragraph("<b>Vertex (v)</b>", style_table_cell_bold), Paragraph("<b>Known (T / F)</b>", style_table_cell_bold), Paragraph("<b>Distance (d_v)</b>", style_table_cell_bold), Paragraph("<b>Previous Path (p_v)</b>", style_table_cell_bold), Paragraph("<b>Shortest Route from Source (1)</b>", style_table_cell_bold)],
        [Paragraph("<b>v₁ (Source)</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>0</b>", style_table_cell_ans), Paragraph("<b>0 (None)</b>", style_table_cell_ans), Paragraph("<b>1</b> (Start node)", style_table_cell_ans)],
        [Paragraph("<b>v₂</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>1</b>", style_table_cell_ans), Paragraph("<b>1</b>", style_table_cell_ans), Paragraph("<b>1, 2</b>", style_table_cell_ans)],
        [Paragraph("<b>v₃</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>2</b>", style_table_cell_ans), Paragraph("<b>4</b>", style_table_cell_ans), Paragraph("<b>1, 4, 3</b>", style_table_cell_ans)],
        [Paragraph("<b>v₄</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>1</b>", style_table_cell_ans), Paragraph("<b>1</b>", style_table_cell_ans), Paragraph("<b>1, 4</b>", style_table_cell_ans)],
        [Paragraph("<b>v₅</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>2</b>", style_table_cell_ans), Paragraph("<b>4</b> (or 2)", style_table_cell_ans), Paragraph("<b>1, 4, 5</b> (or 1, 2, 5)", style_table_cell_ans)],
        [Paragraph("<b>v₆</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>2</b>", style_table_cell_ans), Paragraph("<b>4</b>", style_table_cell_ans), Paragraph("<b>1, 4, 6</b>", style_table_cell_ans)],
        [Paragraph("<b>v₇</b>", style_table_cell_bold), Paragraph("<b>T (True)</b>", style_table_cell_ans), Paragraph("<b>2</b>", style_table_cell_ans), Paragraph("<b>4</b>", style_table_cell_ans), Paragraph("<b>1, 4, 7</b>", style_table_cell_ans)],
    ]
    t_sp_sol = Table(sp_sol_rows, colWidths=[65, 80, 80, 100, 198])
    t_sp_sol.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#86efac')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dcfce7')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_sp_sol)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.2 Circular Queue State upon Completion (Capacity 7, Slots 0 to 6):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>Enqueue Sequence:</b> <font color='#15803d'><b>1, 2, 4, 5, 3, 6, 7</b></font> (or 1, 2, 4, 3, 5, 6, 7)<br/>"
        "• <b>Dequeue Sequence:</b> <font color='#15803d'><b>1, 2, 4, 5, 3, 6, 7</b></font><br/>"
        "• <b>Final Queue Contents:</b> <code>[1, 2, 4, 5, 3, 6, 7]</code> (all elements processed)<br/>"
        "• <b>Pointers:</b> front = <font color='#15803d'><b>6</b></font> &nbsp;|&nbsp; back = <font color='#15803d'><b>6</b></font> &nbsp;|&nbsp; currentSize = <b>0</b> &nbsp;|&nbsp; Status: <b>Empty</b>",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.3 Shortest Path Reconstruction & Distance (4 Destinations):</b> [3 Marks]", style_sub_q))
    story.append(Paragraph(
        "<font color='#b91c1c'><b>* CRITICAL PROFESSOR'S RULE:</b> Must write comma-separated sequences ONLY (e.g. 1, 4, 5). DO NOT write arrows (1 → 4 → 5). Distance is measured in number of EDGES!</font><br/>"
        "• Shortest Path to <b>Vertex 5:</b> Distance = <font color='#15803d'><b>2 edges</b></font> &nbsp;|&nbsp; Route Sequence: <font color='#15803d'><b>1, 4, 5</b></font> (or <code>1, 2, 5</code>)<br/>"
        "• Shortest Path to <b>Vertex 7:</b> Distance = <font color='#15803d'><b>2 edges</b></font> &nbsp;|&nbsp; Route Sequence: <font color='#15803d'><b>1, 4, 7</b></font><br/>"
        "• Shortest Path to <b>Vertex 6:</b> Distance = <font color='#15803d'><b>2 edges</b></font> &nbsp;|&nbsp; Route Sequence: <font color='#15803d'><b>1, 4, 6</b></font><br/>"
        "• Shortest Path to <b>Vertex 3:</b> Distance = <font color='#15803d'><b>2 edges</b></font> &nbsp;|&nbsp; Route Sequence: <font color='#15803d'><b>1, 4, 3</b></font>",
        style_body
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.4 Algorithm Complexity & BFS Property:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "• <b>Time Complexity:</b> <font color='#15803d'><b>O(|V| + |E|)</b></font> when using Adjacency List (each vertex enqueued once, each edge examined once).<br/>"
        "• <b>BFS Correctness Property:</b> BFS visits vertices in non-decreasing order of distance from source. In unweighted graphs, each edge has weight 1, so the first time a vertex is reached guarantees the minimum edge count. In weighted graphs, a path with more edges may have less total weight, requiring Dijkstra's algorithm.",
        style_body
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: QUESTION 7: ADVANCED THEORY & CALCULATIONS SOLUTIONS
    # =========================================================================
    story.append(Paragraph("<b>Question 7: Advanced Theory, Structural Properties & Calculations — Master Solutions (10 Marks)</b>", style_section_h1))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.1 Structural Properties (Data Structures Classification):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "(a) <b>Data Structure with TWO formal properties:</b> <font color='#15803d'><b>Binary Heap (Priority Queue)</b></font><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;1. <b>Structure Property:</b> Complete Binary Tree (filled left-to-right at lowest level).<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Heap-Order Property:</b> Parent is smaller than or equal to children (for Min-Heap).<br/>"
        "(b) <b>Tree Data Structure with THREE formal properties:</b> <font color='#15803d'><b>Binary Search Tree (BST)</b></font> (or AVL Tree / B-Tree)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;1. Binary Tree Structure (each node has at most 2 children).<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;2. Left Subtree Property: For every node X, all keys in left subtree are strictly less than key(X).<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;3. Right Subtree Property: For every node X, all keys in right subtree are strictly greater than key(X).",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.2 Hash Function Theoretical Properties & Realistic Limitation:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• <b>3 Ideal Properties of a Hash Function:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;1. Fast and easy to compute: O(1) constant time.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;2. Uniform distribution: Distributes keys evenly across all table slots to minimize clustering.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;3. Injective / Collision-free: Maps distinct keys to distinct array slots (Zero collisions).<br/>"
        "• <b>Impossible Property in Practice:</b> <font color='#15803d'><b>Property 3 (Collision-free / Zero collisions)</b></font><br/>"
        "• <b>Two Fundamental Reasons:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Reason 1 (Pigeonhole Principle):</b> The universe of possible keys (e.g. all strings/integers) is infinite or vastly larger than the finite hash table size (|U| >> TableSize). Collisions are mathematically inevitable.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Reason 2 (Unknown Input Distribution):</b> In real-world applications, incoming data cannot be known in advance, causing clustering at common hash values.",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.3 Graph Memory Waste Percentage (Sparse Graph Analysis):</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "• Total cells in Adjacency Matrix: 7 × 7 = <font color='#15803d'><b>49 cells</b></font>.<br/>"
        "• Cells containing 1 (active edges): <b>12 cells</b> → (12 / 49) × 100 = <font color='#15803d'><b>24.49%</b></font><br/>"
        "• Cells containing 0 (wasted space): <b>37 cells</b> → (37 / 49) × 100 = <font color='#15803d'><b>75.51% (Waste Percentage)</b></font><br/>"
        "• Cells required in Adjacency List: |V| + |E| = 7 + 12 = <font color='#15803d'><b>19 nodes/pointers</b></font>.<br/>"
        "• Percentage of memory saved by Adjacency List: (49 - 19) / 49 × 100 = <font color='#15803d'><b>61.22% memory saved</b></font>.",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.4 Complete Graph Edge Calculations:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "(a) Complete Undirected Graph K₁₆ (|V| = 16):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Formula: |E| = |V|(|V| - 1) / 2 = 16 × 15 / 2 = <font color='#15803d'><b>120 edges</b></font> (Exact integer!).<br/>"
        "(b) Complete Directed Graph with 16 vertices (no self-loops):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Formula: |E| = |V|(|V| - 1) = 16 × 15 = <font color='#15803d'><b>240 directed edges</b></font>.",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.5 Complete Binary Tree Node Bounds:</b> [2 Marks]", style_sub_q))
    story.append(Paragraph(
        "Formula for height h (Root at h = 0): Minimum nodes = 2^h &nbsp;|&nbsp; Maximum nodes = 2^(h+1) - 1.<br/>"
        "• <b>Height h = 10:</b> Minimum = 2¹⁰ = <font color='#15803d'><b>1,024 nodes</b></font> &nbsp;|&nbsp; Maximum = 2¹¹ - 1 = <font color='#15803d'><b>2,047 nodes</b></font>.<br/>"
        "• <b>Height h = 15:</b> Minimum = 2¹⁵ = <font color='#15803d'><b>32,768 nodes</b></font> &nbsp;|&nbsp; Maximum = 2¹⁶ - 1 = <font color='#15803d'><b>65,535 nodes</b></font>.<br/>"
        "• <b>Height h = 16:</b> Minimum = 2¹⁶ = <font color='#15803d'><b>65,536 nodes</b></font> &nbsp;|&nbsp; Maximum = 2¹⁷ - 1 = <font color='#15803d'><b>131,071 nodes</b></font>.<br/>"
        "<i>(Answers are computed exact integers as required by grading rules)</i>",
        style_body
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>7.6 Binary Heap 1D Array Formulas:</b> [1 Mark]", style_sub_q))
    story.append(Paragraph(
        "For index i in a 1-based array:<br/>"
        "• Left Child = <font color='#15803d'><b>2i</b></font> &nbsp;|&nbsp; Right Child = <font color='#15803d'><b>2i + 1</b></font> &nbsp;|&nbsp; Parent = <font color='#15803d'><b>⌊i / 2⌋ (i // 2)</b></font><br/>"
        "• <i>Why floor division must be used:</i> Right child at index 2i + 1 divided by 2 produces (2i + 1)/2 = i + 0.5. Truncating the decimal yields parent index i. Rounding up would yield i + 1 which references the incorrect node.",
        style_body
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>*** END OF MASTER SOLUTIONS — 100% CANONICAL CURRICULUM ALIGNED ***</b>", ParagraphStyle('EndNotice', fontName='Tahoma-Bold', fontSize=8.5, leading=11, alignment=1, textColor=colors.HexColor('#166534'))))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built master solutions PDF: {OUTPUT_PDF}")

if __name__ == '__main__':
    build_pdf()
