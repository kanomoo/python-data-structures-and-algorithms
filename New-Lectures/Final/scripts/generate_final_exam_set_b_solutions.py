r"""
Master Solutions PDF Generator for Final Exam 2026 Set B
Course: 060243106 / 060223119 Data Structures and Algorithms, KMUTNB
Instructor: Assoc. Prof. Dr. Pradit Pitaksatheinkul
Location: C:/Project/python-data-structures-and-algorithms/New-Lectures/Final/
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAM_DIR = os.path.join(BASE_DIR, 'diagrams')
SOL_PDF = os.path.join(BASE_DIR, 'Final_Exam_2026_Set_B_Master_Solutions.pdf')

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
            self.drawString(36, 815, "Data Structures and Algorithms (060243106 / 060223119) — MASTER SOLUTIONS (Set B)")
            self.drawRightString(559, 815, "OFFICIAL SOLUTION KEY & PRINCIPLES")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(36, 810, 559, 810)

        # Footer
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(36, 32, 559, 32)
        
        self.drawString(36, 22, "KMUTNB Department of Computer and Information Science — Master Solutions Guide")
        self.drawRightString(559, 22, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def get_styles():
    styles = getSampleStyleSheet()
    return {
        'title': ParagraphStyle('DocTitle', fontName='Tahoma-Bold', fontSize=11, leading=14, alignment=1, textColor=colors.HexColor('#0f172a')),
        'subtitle': ParagraphStyle('DocSubTitle', fontName='Tahoma', fontSize=8, leading=11, alignment=1, textColor=colors.HexColor('#166534')),
        'h1': ParagraphStyle('SectionH1', fontName='Tahoma-Bold', fontSize=9.5, leading=12.5, textColor=colors.HexColor('#1e3a8a'), spaceBefore=2, spaceAfter=2),
        'sub_q': ParagraphStyle('SubQ', fontName='Tahoma-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#0f172a')),
        'body': ParagraphStyle('Body', fontName='Tahoma', fontSize=7.5, leading=10, textColor=colors.HexColor('#1e293b')),
        'cell': ParagraphStyle('TableCell', fontName='Tahoma', fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#0f172a')),
        'cell_bold': ParagraphStyle('TableCellBold', fontName='Tahoma-Bold', fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#0f172a')),
        'cell_ans': ParagraphStyle('TableCellAns', fontName='Tahoma-Bold', fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#15803d')),
        'ans': ParagraphStyle('AnsText', fontName='Tahoma', fontSize=7.5, leading=10, textColor=colors.HexColor('#15803d')),
        'ans_bold': ParagraphStyle('AnsBold', fontName='Tahoma-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#15803d')),
        'notice': ParagraphStyle('Notice', fontName='Tahoma-Bold', fontSize=7, leading=9, textColor=colors.HexColor('#b91c1c')),
    }

def build_solutions_pdf():
    doc = SimpleDocTemplate(SOL_PDF, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=32, bottomMargin=36)
    st = get_styles()
    story = []

    # =========================================================================
    # PAGE 1: COVER & QUESTION 1: HASHING SOLUTIONS
    # =========================================================================
    hdr_data = [
        [Paragraph("<b>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK</b><br/>"
                   "Faculty of Applied Science / Faculty of Information Technology<br/>"
                   "<b>FINAL EXAMINATION MASTER SOLUTIONS — SEMESTER 1, ACADEMIC YEAR 2026 (SET B)</b>", st['title'])],
        [Paragraph("<b>Course:</b> 060243106 / 060223119 Data Structures and Algorithms &nbsp;|&nbsp; <b>Total Marks:</b> 70 Marks (Normalized to 35% of Grade)<br/>"
                   "<b>Lecturer:</b> Assoc. Prof. Dr. Pradit Pitaksatheinkul &nbsp;|&nbsp; <b>Status:</b> 100% Comprehensive Step-by-Step Master Solution Key", st['subtitle'])],
    ]
    t_hdr = Table(hdr_data, colWidths=[523])
    t_hdr.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#166534')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor('#bbf7d0')),
    ]))
    story.append(t_hdr)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Question 1: Hashing & Open Addressing with Double Hashing (10 Marks) — Solution</b>", st['h1']))
    story.append(Paragraph("<b>Formula & Parameters:</b> TableSize = 13, R = 11 (largest prime < 13).<br/>"
                           "h₀(x) = x mod 13, &nbsp; f(i) = i × (11 - (x mod 11)), &nbsp; hᵢ(x) = (h₀(x) + f(i)) mod 13.<br/>"
                           "Sequence of keys inserted: <b>[ 43, 17, 82, 95, 35, 160 ]</b>.", st['body']))
    story.append(Spacer(1, 3))

    # Grid for hash table filled
    ht_hdr = [Paragraph("<b>Index</b>", st['cell_bold'])] + [Paragraph(f"<b>{i}</b>", st['cell_bold']) for i in range(13)]
    keys_in_slots = ["", "160", "", "", "43", "35", "", "", "95", "17", "82", "", ""]
    info_in_slots = ["", "A", "", "", "A", "A", "", "", "A", "A", "A", "", ""]
    ht_key = [Paragraph("<b>Key</b>", st['cell_bold'])] + [Paragraph(k, st['cell_ans']) for k in keys_in_slots]
    ht_info = [Paragraph("<b>Info</b>", st['cell_bold'])] + [Paragraph(inf, st['cell_ans']) for inf in info_in_slots]
    t_ht = Table([ht_hdr, ht_key, ht_info], colWidths=[43] + [36.9]*13)
    t_ht.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (2,1), (2,2), colors.HexColor('#dcfce7')),
        ('BACKGROUND', (5,1), (6,2), colors.HexColor('#dcfce7')),
        ('BACKGROUND', (9,1), (11,2), colors.HexColor('#dcfce7')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_ht)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.1 Step-by-Step Collision & Probing Trace Table:</b> [4 Marks]", st['sub_q']))
    trace_sol_rows = [
        [Paragraph("<b>Key (x)</b>", st['cell_bold']), Paragraph("<b>h₀(x) = x mod 13</b>", st['cell_bold']), Paragraph("<b>Double Hashing Step & Calculation f(i)</b>", st['cell_bold']), Paragraph("<b>Final Index</b>", st['cell_bold']), Paragraph("<b>Collisions</b>", st['cell_bold'])],
        [Paragraph("<b>43</b>", st['cell']), Paragraph("43 mod 13 = 4", st['cell']), Paragraph("Empty slot. Placed immediately.", st['cell']), Paragraph("<b>Index 4</b>", st['cell_ans']), Paragraph("0", st['cell'])],
        [Paragraph("<b>17</b>", st['cell']), Paragraph("17 mod 13 = 4", st['cell']), Paragraph("Collision at 4! f(1)=1×(11-(17 mod 11))=5. h₁=(4+5) mod 13=9 (Empty).", st['cell']), Paragraph("<b>Index 9</b>", st['cell_ans']), Paragraph("1", st['cell'])],
        [Paragraph("<b>82</b>", st['cell']), Paragraph("82 mod 13 = 4", st['cell']), Paragraph("Collision at 4! f(1)=1×(11-(82 mod 11))=6. h₁=(4+6) mod 13=10 (Empty).", st['cell']), Paragraph("<b>Index 10</b>", st['cell_ans']), Paragraph("1", st['cell'])],
        [Paragraph("<b>95</b>", st['cell']), Paragraph("95 mod 13 = 4", st['cell']), Paragraph("Collision at 4! f(1)=1×(11-(95 mod 11))=4. h₁=(4+4) mod 13=8 (Empty).", st['cell']), Paragraph("<b>Index 8</b>", st['cell_ans']), Paragraph("1", st['cell'])],
        [Paragraph("<b>35</b>", st['cell']), Paragraph("35 mod 13 = 9", st['cell']), Paragraph("Collision at 9! f(1)=1×(11-(35 mod 11))=9. h₁=(9+9) mod 13=5 (Empty).", st['cell']), Paragraph("<b>Index 5</b>", st['cell_ans']), Paragraph("1", st['cell'])],
        [Paragraph("<b>160</b>", st['cell']), Paragraph("160 mod 13 = 4", st['cell']), Paragraph("Collision at 4! h₁=9 (Collision with 17!). f(2)=2×5=10. h₂=(4+10) mod 13=1 (Empty).", st['cell']), Paragraph("<b>Index 1</b>", st['cell_ans']), Paragraph("<b>2</b>", st['cell_ans'])],
    ]
    t_trace_sol = Table(trace_sol_rows, colWidths=[45, 95, 253, 65, 65])
    t_trace_sol.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_trace_sol)
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>1.2 Collision Analysis Answer:</b> The key that collided the most is <b>160</b> (total <b>2 collisions</b>, attempted index 4 and index 9 before placing in slot 1).<br/>"
        "<b>1.3 Total Collision Count:</b> Total collisions = 0 + 1 + 1 + 1 + 1 + 2 = <b>6 times</b>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<font color='#b91c1c'>*(Instructor's Warning: Count each probe impact once. Do NOT answer 12! Answer is 6)*</font><br/>"
        "<b>1.4 Load Factor Percentage:</b> λ = (6 / 13) × 100% = <b>46.15%</b>.<br/>"
        "<b>1.5 Rehashing Threshold & New TableSize:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• 70% of 13 = 13 × 0.70 = 9.1 ➔ Threshold requires <b>10 keys</b>. Currently 6 keys are inserted.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Must insert: 10 - 6 = <b>4 more keys</b> to trigger Rehashing.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• New TableSize: First prime > 2 × 13 (26) ➔ <b>TableSize = 29</b>.<br/>"
        "<b>1.6 Concept of Wrap-Around:</b> <i>'When the calculated hash address reaches or exceeds the last index of the table, it wraps back to index 0 using modulo TableSize arithmetic.'</i>",
        st['ans_bold']
    ))

    # =========================================================================
    # PAGE 2: QUESTION 2: BINARY MIN-HEAP SOLUTIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 2: Priority Queue (Binary Min-Heap) Operations — Master Solution (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given keys: <b>[ 65, 30, 48, 15, 22, 10, 50, 18, 25, 8 ]</b>.<br/>"
                           "Array indexing: 1-based (Index 0 is None / Unused Sentinel).", st['body']))
    story.append(Spacer(1, 3))

    def make_sol_heap_table(label, arr, highlight_idx=None):
        hdr = [Paragraph("<b>Index</b>", st['cell_bold'])] + [Paragraph(f"<b>{i}</b>", st['cell_bold']) for i in range(12)]
        cells = [Paragraph(f"<b>{label}</b>", st['cell_bold']), Paragraph("None", st['cell'])]
        for i in range(1, 12):
            if i - 1 < len(arr):
                cells.append(Paragraph(str(arr[i-1]), st['cell_ans']))
            else:
                cells.append(Paragraph("-", st['cell']))
        t = Table([hdr, cells], colWidths=[71] + [41]*12)
        style = [
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
            ('BACKGROUND', (1,1), (1,1), colors.HexColor('#f1f5f9')),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ]
        t.setStyle(TableStyle(style))
        return t

    story.append(Paragraph("<b>2.1 Array State 1:</b> After sequentially inserting all 10 elements into Min-Heap (Percolate Up): [3 Marks]", st['sub_q']))
    story.append(make_sol_heap_table("Heap Array", [8, 10, 15, 22, 18, 48, 50, 65, 25, 30]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.2 Array State 2:</b> After executing <b>deleteMin()</b> operation #1 (Removes 8, places 30 at root, Percolates Down): [2 Marks]", st['sub_q']))
    story.append(make_sol_heap_table("After Del 1", [10, 18, 15, 22, 30, 48, 50, 65, 25]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.3 Array State 3:</b> After executing <b>insert(12)</b> (Adds 12 at index 10, Percolates Up): [2 Marks]", st['sub_q']))
    story.append(make_sol_heap_table("After Ins 12", [10, 12, 15, 22, 18, 48, 50, 65, 25, 30]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.4 Array State 4:</b> After executing second <b>deleteMin()</b> operation #2 (Removes 10, places 30 at root, Percolates Down): [1 Mark]", st['sub_q']))
    story.append(make_sol_heap_table("After Del 2", [12, 18, 15, 22, 30, 48, 50, 65, 25]))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>2.5 Mathematical Formulas:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Left Child Index: <b>2i</b> &nbsp;|&nbsp; Right Child Index: <b>2i + 1</b> &nbsp;|&nbsp; Parent Index: <b>⌊i / 2⌋</b> (Python: <code>i // 2</code>).<br/>"
        "<b>2.6 Truncation Rule (Instructor's Strict Caveat):</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Array indices are integers. Integer floor division discards the fractional part (e.g. index 7: 7 // 2 = 3). "
        "Rounding up (e.g., 7/2 = 3.5 ➔ 4) points to the WRONG parent node and violates the Complete Binary Tree property.<br/>"
        "<b>2.7 Percolate Down Code Condition:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<code>if child != self.current_size and self.heap[child + 1] < self.heap[child]: child += 1</code>",
        st['ans_bold']
    ))

    # =========================================================================
    # PAGE 3: QUESTION 3: INSERTION SORT & QUESTION 4: SELECTION SORT SOLUTIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 3: Insertion Sort Tracing & Position Moves — Master Solution (10 Marks)</b>", st['h1']))
    story.append(Paragraph(
        "<b>3.1 Worst-Case Mathematical Analysis (N = 10 Elements):</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Worst-Case Configuration: Array sorted in <b>strictly descending order</b> (e.g. [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]).<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Formula & Calculation: Total Moves = N(N - 1) / 2 = (10 × 9) / 2 = <b>45 moves</b>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Best-Case Configuration: Array already sorted in ascending order ➔ <b>0 moves</b>.",
        st['ans_bold']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.2 Pass Tracing on 10-Element Array: [ 54, 38, 16, 27, 10, 62, 45, 9, 70, 31 ]</b>", st['sub_q']))
    p_hdr = [Paragraph("<b>Pass (p)</b>", st['cell_bold']), Paragraph("<b>Key Element</b>", st['cell_bold']), Paragraph("<b>Elements Shifted (Position Moves)</b>", st['cell_bold']), Paragraph("<b>Array State After Pass p</b>", st['cell_bold'])]
    p_r1 = [Paragraph("<b>p = 3</b>", st['cell_bold']), Paragraph("27", st['cell']), Paragraph("Shifts 54 and 38 to right (<b>2 moves</b>)", st['cell_ans']), Paragraph("<b>[ 16, 27, 38, 54, 10, 62, 45, 9, 70, 31 ]</b>", st['cell_ans'])]
    p_r2 = [Paragraph("<b>p = 6</b>", st['cell_bold']), Paragraph("45", st['cell']), Paragraph("Shifts 62 and 54 to right (<b>2 moves</b>)", st['cell_ans']), Paragraph("<b>[ 10, 16, 27, 38, 45, 54, 62, 9, 70, 31 ]</b>", st['cell_ans'])]
    t_pass = Table([p_hdr, p_r1, p_r2], colWidths=[55, 65, 170, 233])
    t_pass.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_pass)
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "<b>3.3 Code Modification:</b> Place <code>total_moves += 1</code> inside the inner <code>while (j >= 0 and arr[j] > key)</code> loop directly adjacent to the element shift statement <code>arr[j + 1] = arr[j]</code>.",
        st['ans_bold']
    ))
    story.append(Spacer(1, 4))

    # Question 4: Selection Sort Solution
    story.append(Paragraph("<b>Question 4: Selection Sort Tracing (Test Program 2 Format) — Master Solution (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given array: <b>[ 64, 25, 12, 38, 11, 49, 20 ]</b>.", st['body']))
    story.append(Spacer(1, 2))

    story.append(Paragraph(
        "<b>Round 1:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ 64, 25, 12, 38, 11, 49, 20 ], the minimum is <b>11</b> at index <b>4</b>.<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum (11) with first element of unsorted array (64):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Before swap: [ 64, 25, 12, 38, 11, 49, 20 ]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;<b>[ 11, 25, 12, 38, 64, 49, 20 ]</b><br/>"
        "&nbsp;&nbsp;3. Result: Now 1 element [ 11 ] sorted. The remaining unsorted array is: [ 25, 12, 38, 64, 49, 20 ]<br/>"
        "<b>Round 2:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ 25, 12, 38, 64, 49, 20 ], the minimum is <b>12</b> at index <b>2</b>.<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum (12) with first element of unsorted array (25):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Before swap: [ 11, 25, 12, 38, 64, 49, 20 ]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;<b>[ 11, 12, 25, 38, 64, 49, 20 ]</b><br/>"
        "&nbsp;&nbsp;3. Result: Now 2 elements [ 11, 12 ] sorted. The remaining unsorted array is: [ 25, 38, 64, 49, 20 ]<br/>"
        "<b>Round 3:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ 25, 38, 64, 49, 20 ], the minimum is <b>20</b> at index <b>6</b>.<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum (20) with first element of unsorted array (25):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;<b>[ 11, 12, 20, 38, 64, 49, 25 ]</b><br/>"
        "&nbsp;&nbsp;3. Result: Now 3 elements [ 11, 12, 20 ] sorted. The remaining unsorted array is: [ 38, 64, 49, 25 ]<br/>"
        "<b>Round 4:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ 38, 64, 49, 25 ], the minimum is <b>25</b> at index <b>6</b>.<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum (25) with first element of unsorted array (38):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;<b>[ 11, 12, 20, 25, 64, 49, 38 ]</b><br/>"
        "&nbsp;&nbsp;3. Result: Now 4 elements [ 11, 12, 20, 25 ] sorted. The remaining unsorted array is: [ 64, 49, 38 ]<br/>"
        "<b>4.2 Maximum Swaps:</b> N - 1 = 7 - 1 = <b>6 swaps</b>. Selection Sort guarantees O(N) memory writes.",
        st['ans_bold']
    ))

    # =========================================================================
    # PAGE 4: QUESTION 5: TOPOLOGICAL SORT SOLUTIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 5: Topological Sort (Kahn's Algorithm on 7-Vertex DAG) — Master Solution (10 Marks)</b>", st['h1']))
    story.append(Paragraph("DAG: <b>|V| = 7</b> vertices, <b>|E| = 9</b> edges. Adjacency: 5:[1,2], 1:[3,4], 2:[4,7], 3:[6], 4:[6,7], 6:[], 7:[].", st['body']))
    story.append(Spacer(1, 2))

    topo_img_path = os.path.join(DIAGRAM_DIR, "set_b_topo.png")
    if os.path.exists(topo_img_path):
        img = RLImage(topo_img_path, width=420, height=170)
        img.hAlign = 'CENTER'
        story.append(img)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.1 In-Degree Array Table:</b> [2 Marks]", st['sub_q']))
    id_hdr = [Paragraph("<b>Vertex</b>", st['cell_bold'])] + [Paragraph(f"<b>{i}</b>", st['cell_bold']) for i in range(1, 8)]
    id_vals = [Paragraph("<b>In-Degree</b>", st['cell_bold']), Paragraph("1", st['cell']), Paragraph("1", st['cell']), Paragraph("1", st['cell']), Paragraph("2", st['cell']), Paragraph("<b>0 (Source)</b>", st['cell_ans']), Paragraph("2", st['cell']), Paragraph("2", st['cell'])]
    t_id = Table([id_hdr, id_vals], colWidths=[71] + [64.5]*7)
    t_id.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (5,1), (5,1), colors.HexColor('#dcfce7')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_id)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.2 Circular Queue Simulation Table:</b> [4 Marks]", st['sub_q']))
    q_sol_rows = [
        [Paragraph("<b>Step #</b>", st['cell_bold']), Paragraph("<b>Action (Dequeue / Enqueue)</b>", st['cell_bold']), Paragraph("<b>Queue Contents</b>", st['cell_bold']), Paragraph("<b>Front Ptr</b>", st['cell_bold']), Paragraph("<b>Back Ptr</b>", st['cell_bold'])],
        [Paragraph("Init", st['cell']), Paragraph("Enqueue initial in-degree 0 vertex (5)", st['cell']), Paragraph("[ 5 ]", st['cell_ans']), Paragraph("0", st['cell']), Paragraph("0", st['cell'])],
        [Paragraph("1", st['cell']), Paragraph("Dequeue 5 (Output 5). Indegree 1➔0 (enq 1), 2➔0 (enq 2)", st['cell']), Paragraph("[ 1, 2 ]", st['cell_ans']), Paragraph("1", st['cell']), Paragraph("2", st['cell'])],
        [Paragraph("2", st['cell']), Paragraph("Dequeue 1 (Output 1). Indegree 3➔0 (enq 3), 4: 2➔1", st['cell']), Paragraph("[ 2, 3 ]", st['cell_ans']), Paragraph("2", st['cell']), Paragraph("3", st['cell'])],
        [Paragraph("3", st['cell']), Paragraph("Dequeue 2 (Output 2). Indegree 4➔0 (enq 4), 7: 2➔1", st['cell']), Paragraph("[ 3, 4 ]", st['cell_ans']), Paragraph("3", st['cell']), Paragraph("4", st['cell'])],
        [Paragraph("4", st['cell']), Paragraph("Dequeue 3 (Output 3). Indegree 6: 2➔1", st['cell']), Paragraph("[ 4 ]", st['cell_ans']), Paragraph("4", st['cell']), Paragraph("4", st['cell'])],
        [Paragraph("5", st['cell']), Paragraph("Dequeue 4 (Output 4). Indegree 6➔0 (enq 6), 7➔0 (enq 7)", st['cell']), Paragraph("[ 6, 7 ]", st['cell_ans']), Paragraph("5", st['cell']), Paragraph("6", st['cell'])],
        [Paragraph("6", st['cell']), Paragraph("Dequeue 6 (Output 6)", st['cell']), Paragraph("[ 7 ]", st['cell_ans']), Paragraph("6", st['cell']), Paragraph("6", st['cell'])],
        [Paragraph("7", st['cell']), Paragraph("Dequeue 7 (Output 7). Queue empty.", st['cell']), Paragraph("[ ] (Empty)", st['cell_ans']), Paragraph("7", st['cell']), Paragraph("6", st['cell'])],
    ]
    t_q = Table(q_sol_rows, colWidths=[35, 230, 138, 60, 60])
    t_q.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q)
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "<b>5.3 Final Topological Ordering:</b> <b>5, 1, 2, 3, 4, 6, 7</b> (All 7 vertices processed).<br/>"
        "<b>5.4 Directed Cycle Detection:</b> If the graph contains a directed cycle, all vertices within the cycle will continuously maintain in-degree ≥ 1. "
        "Consequently, the Queue becomes empty before all |V| vertices are processed. The algorithm detects the cycle because <code>processed_count < |V|</code>.",
        st['ans_bold']
    ))

    # =========================================================================
    # PAGE 5: QUESTION 6: UNWEIGHTED SHORTEST PATH SOLUTIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 6: Unweighted Shortest Path Algorithm (BFS) — Master Solution (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given graph with <b>|V| = 7</b> vertices (A to G), <b>|E| = 11</b> edges. Start vertex is <b>Vertex A</b>:", st['body']))
    story.append(Spacer(1, 2))

    sp_img_path = os.path.join(DIAGRAM_DIR, "set_b_shortest_path.png")
    if os.path.exists(sp_img_path):
        img_sp = RLImage(sp_img_path, width=420, height=160)
        img_sp.hAlign = 'CENTER'
        story.append(img_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.1 Shortest Path Processing Table (Assignment 4 Style):</b> [5 Marks]", st['sub_q']))
    sp_hdr = [Paragraph("<b>Vertex (v)</b>", st['cell_bold']), Paragraph("<b>Known (T / F)</b>", st['cell_bold']), Paragraph("<b>Dist (dᵥ)</b>", st['cell_bold']), Paragraph("<b>Path (pᵥ)</b>", st['cell_bold'])]
    sp_sol_rows = [
        sp_hdr,
        [Paragraph("<b>A (Start)</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>0</b>", st['cell_ans']), Paragraph("0", st['cell_ans'])],
        [Paragraph("<b>B</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>1</b>", st['cell_ans']), Paragraph("0 ➔ <b>A</b>", st['cell_ans'])],
        [Paragraph("<b>C</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>2</b>", st['cell_ans']), Paragraph("0 ➔ <b>B</b>", st['cell_ans'])],
        [Paragraph("<b>D</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>1</b>", st['cell_ans']), Paragraph("0 ➔ <b>A</b>", st['cell_ans'])],
        [Paragraph("<b>E</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>2</b>", st['cell_ans']), Paragraph("0 ➔ <b>B</b>", st['cell_ans'])],
        [Paragraph("<b>F (Sink)</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>3</b>", st['cell_ans']), Paragraph("0 ➔ <b>C</b>", st['cell_ans'])],
        [Paragraph("<b>G</b>", st['cell_bold']), Paragraph("F ➔ <b>T</b>", st['cell_ans']), Paragraph("999 ➔ <b>2</b>", st['cell_ans']), Paragraph("0 ➔ <b>D</b>", st['cell_ans'])],
    ]
    t_sp = Table(sp_sol_rows, colWidths=[90, 140, 140, 153])
    t_sp.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f0fdf4')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.2 Circular Queue Tracing:</b> [2 Marks]", st['sub_q']))
    q_sp_sol = [
        [Paragraph("<b>Step</b>", st['cell_bold']), Paragraph("<b>Action</b>", st['cell_bold']), Paragraph("<b>Queue State</b>", st['cell_bold'])],
        [Paragraph("Init", st['cell']), Paragraph("Enqueue Start Vertex A", st['cell']), Paragraph("[ A ]", st['cell_ans'])],
        [Paragraph("1", st['cell']), Paragraph("Dequeue A (Known=T). Enqueue neighbors B, D (dist=1)", st['cell']), Paragraph("[ B, D ]", st['cell_ans'])],
        [Paragraph("2", st['cell']), Paragraph("Dequeue B (Known=T). Enqueue neighbors C, E (dist=2)", st['cell']), Paragraph("[ D, C, E ]", st['cell_ans'])],
        [Paragraph("3", st['cell']), Paragraph("Dequeue D (Known=T). Enqueue neighbor G (dist=2)", st['cell']), Paragraph("[ C, E, G ]", st['cell_ans'])],
        [Paragraph("4", st['cell']), Paragraph("Dequeue C (Known=T). Enqueue neighbor F (dist=3)", st['cell']), Paragraph("[ E, G, F ]", st['cell_ans'])],
        [Paragraph("5", st['cell']), Paragraph("Dequeue E (Known=T). Neighbors C, F, G already reached", st['cell']), Paragraph("[ G, F ]", st['cell_ans'])],
        [Paragraph("6", st['cell']), Paragraph("Dequeue G (Known=T). Neighbor F already reached", st['cell']), Paragraph("[ F ]", st['cell_ans'])],
        [Paragraph("7", st['cell']), Paragraph("Dequeue F (Known=T). Queue empty", st['cell']), Paragraph("[ ] (Empty)", st['cell_ans'])],
    ]
    t_q_sp = Table(q_sp_sol, colWidths=[40, 260, 223])
    t_q_sp.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "<b>6.3 Backtracking Analysis Answers:</b><br/>"
        "• Shortest Path from <b>A to F</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Backtrack: F ➔ pv(F)=C ➔ pv(C)=B ➔ pv(B)=A.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Length: 3 edges</b> &nbsp;|&nbsp; <b>Path: A, B, C, F</b><br/>"
        "• Shortest Path from <b>A to G</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Backtrack: G ➔ pv(G)=D ➔ pv(D)=A.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Length: 2 edges</b> &nbsp;|&nbsp; <b>Path: A, D, G</b><br/>"
        "<font color='#b91c1c'>*(Instructor's Warning: Length is counted in EDGES [integer]. Writing arrows A ➔ B ➔ C ➔ F receives ZERO marks)*</font>",
        st['ans_bold']
    ))

    # =========================================================================
    # PAGE 6: QUESTION 7: ADVANCED THEORY, PROPERTIES & % CALCULATIONS SOLUTIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 7: Advanced Theory, Structural Properties & Percentage Calculations — Master Solution (10 Marks)</b>", st['h1']))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>7.1 Structural Properties (Two Properties vs Three Properties):</b> [3 Marks]", st['sub_q']))
    story.append(Paragraph(
        "(a) Data structure with <b>Two Formal Properties</b>: <b>Binary Heap</b> (Priority Queue)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Structure Property:</b> Must be a <i>Complete Binary Tree</i> (completely filled at all levels except the lowest level, which is filled from left to right). This allows pointerless 1D array representation.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Heap-Order Property:</b> In a Min-Heap, for every node X, Key(Parent) ≤ Key(X), ensuring the minimum element is ALWAYS located at the Root (array index 1).<br/>"
        "(b) Concept with <b>Three Formal Properties</b>: <b>Ideal Hash Function</b> (Lecture 7)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Property 1: Fast Computation:</b> Executes in constant O(1) time.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Property 2: Deterministic:</b> Identical key always hashes to the exact same table slot.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Property 3: Uniform Distribution:</b> Distributes all keys evenly across all table slots without bias.<br/>"
        "(c) Impossible property in practice: <b>Uniform Distribution (Zero Collisions)</b>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Reason 1: Pigeonhole Principle:</b> Key space is infinitely or vastly larger than TableSize; collisions are mathematically guaranteed.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Reason 2: Data Distribution Clustering:</b> Real-world data is non-random and naturally clusters around specific patterns.",
        st['ans_bold']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.2 Graph Memory Waste Percentage Calculation:</b> [2 Marks]", st['sub_q']))
    story.append(Paragraph(
        "Given |V| = 8 vertices, |E| = 14 edges:<br/>"
        "• Total cells in Adjacency Matrix = |V|² = 8 × 8 = <b>64 cells</b>.<br/>"
        "• Cells containing 1 (active edges) = 14 cells ➔ (14 / 64) × 100% = <b>21.88%</b>.<br/>"
        "• Cells containing 0 (wasted memory) = 64 - 14 = 50 cells ➔ (50 / 64) × 100% = <b>78.13%</b>.<br/>"
        "• Adjacency List memory = |V| + |E| = 8 + 14 = <b>22 cells</b>.<br/>"
        "• Percentage of memory saved = ((64 - 22) / 64) × 100% = <b>65.63% saved</b>.<br/>"
        "<i>Conclusion: For sparse graphs, Adjacency Matrix wastes over 78% of space. Adjacency List is optimal.</i>",
        st['ans_bold']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.3 Complete Graph Edge Calculations:</b> [1.5 Marks]", st['sub_q']))
    story.append(Paragraph(
        "(a) Undirected Complete Graph K₁₂: E = V(V - 1) / 2 = (12 × 11) / 2 = 6 × 11 = <b>66 edges</b>. (Exact integer: 66)<br/>"
        "(b) Directed Complete Graph without self-loops: E = V(V - 1) = 12 × 11 = <b>132 directed edges</b>.<br/>"
        "<font color='#b91c1c'>*(Instructor's Warning: Writing 12*11/2 or formulas receives 0 marks. Answer must be 66)*</font>",
        st['ans_bold']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.4 Complete Binary Tree Node Bounds:</b> [2 Marks]", st['sub_q']))
    story.append(Paragraph(
        "For Complete Binary Tree of height h (Root at h = 0): Min = 2ʰ, Max = 2ʰ⁺¹ - 1:<br/>"
        "• Height h = 12: Minimum nodes = 2¹² = <b>4,096 nodes</b> &nbsp;|&nbsp; Maximum nodes = 2¹³ - 1 = 8,192 - 1 = <b>8,191 nodes</b>.<br/>"
        "• Height h = 15: Minimum nodes = 2¹⁵ = <b>32,768 nodes</b> &nbsp;|&nbsp; Maximum nodes = 2¹⁶ - 1 = 65,536 - 1 = <b>65,535 nodes</b>.<br/>"
        "<font color='#b91c1c'>*(Strict rule: Evaluated exact integers only. Do NOT leave as 2¹² or 2¹⁵)*</font>",
        st['ans_bold']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.5 Instructor Exam Traps & Specific Definitions:</b> [1.5 Marks]", st['sub_q']))
    story.append(Paragraph(
        "(a) Path sequence notation: In graph theory, a Path is formally defined as an <i>ordered sequence of vertices</i> separated by commas (e.g., <b>A, B, C</b>). Writing arrows (A ➔ B ➔ C) represents directed edge relations, violating mathematical convention and receives <b>0 marks</b>.<br/>"
        "(b) Null Graph Query: If asked for the shortest path between two vertices in a Null Graph (V = {}, E = {}), the only correct answer is: <b>'No path exists because neither vertex exists in the graph.'</b>",
        st['ans_bold']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>*** END OF MASTER SOLUTIONS (SET B) — COMPREHENSIVE STUDY GUIDE ***</b>", ParagraphStyle('EndNotice', fontName='Tahoma-Bold', fontSize=8, leading=10, alignment=1, textColor=colors.HexColor('#166534'))))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built Master Solutions Paper: {SOL_PDF}")

if __name__ == '__main__':
    build_solutions_pdf()
