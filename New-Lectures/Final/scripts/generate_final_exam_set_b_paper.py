r"""
Build Script for Final Exam 2026 Set B PDFs
Generates:
1. Final_Exam_2026_Set_B_Paper.pdf (Blank Exam Paper, 6 Pages A4)
2. Final_Exam_2026_Set_B_Master_Solutions.pdf (Comprehensive Solutions Key, 6 Pages A4)
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
PAPER_PDF = os.path.join(BASE_DIR, 'Final_Exam_2026_Set_B_Paper.pdf')
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
            self.drawString(36, 815, "Data Structures and Algorithms (060243106 / 060223119) — Final Exam 2026 (Set B)")
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

def get_styles():
    styles = getSampleStyleSheet()
    return {
        'title': ParagraphStyle('DocTitle', fontName='Tahoma-Bold', fontSize=11, leading=14, alignment=1, textColor=colors.HexColor('#0f172a')),
        'subtitle': ParagraphStyle('DocSubTitle', fontName='Tahoma', fontSize=8, leading=11, alignment=1, textColor=colors.HexColor('#334155')),
        'student_info': ParagraphStyle('StudentInfo', fontName='Tahoma', fontSize=8, leading=11, textColor=colors.HexColor('#1e293b')),
        'h1': ParagraphStyle('SectionH1', fontName='Tahoma-Bold', fontSize=9.5, leading=12.5, textColor=colors.HexColor('#1e3a8a'), spaceBefore=2, spaceAfter=2),
        'sub_q': ParagraphStyle('SubQ', fontName='Tahoma-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#0f172a')),
        'body': ParagraphStyle('Body', fontName='Tahoma', fontSize=7.5, leading=10, textColor=colors.HexColor('#1e293b')),
        'body_bold': ParagraphStyle('BodyBold', fontName='Tahoma-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#0f172a')),
        'cell': ParagraphStyle('TableCell', fontName='Tahoma', fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#0f172a')),
        'cell_bold': ParagraphStyle('TableCellBold', fontName='Tahoma-Bold', fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#0f172a')),
        'cell_ans': ParagraphStyle('TableCellAns', fontName='Tahoma-Bold', fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#15803d')),
        'notice': ParagraphStyle('Notice', fontName='Tahoma-Bold', fontSize=7, leading=9, textColor=colors.HexColor('#b91c1c')),
        'ans': ParagraphStyle('AnsText', fontName='Tahoma', fontSize=7.5, leading=10, textColor=colors.HexColor('#15803d')),
        'ans_bold': ParagraphStyle('AnsBold', fontName='Tahoma-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#15803d')),
    }

def build_paper_pdf():
    doc = SimpleDocTemplate(PAPER_PDF, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=32, bottomMargin=36)
    st = get_styles()
    story = []

    # =========================================================================
    # PAGE 1: HEADER & QUESTION 1: HASHING
    # =========================================================================
    hdr_data = [
        [Paragraph("<b>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK</b><br/>"
                   "Faculty of Applied Science / Faculty of Information Technology<br/>"
                   "<b>FINAL EXAMINATION — SEMESTER 1, ACADEMIC YEAR 2026 (PRACTICE SET B)</b>", st['title'])],
        [Paragraph("<b>Course:</b> 060243106 / 060223119 Data Structures and Algorithms &nbsp;|&nbsp; <b>Time:</b> 3 Hours (09:00 - 12:00)<br/>"
                   "<b>Total Marks:</b> 70 Marks (Normalized to 35% of Final Grade) &nbsp;|&nbsp; <b>Lecturer:</b> Assoc. Prof. Dr. Pradit Pitaksatheinkul", st['subtitle'])],
        [Paragraph("<b>STUDENT INFO:</b> Name: ............................................................................ ID: ....................................... Room: ................ Seat: ................<br/>"
                   "<font color='#b91c1c'><b>RULES:</b> Open Book (Textbooks & Notes Allowed) | Scientific Calculator Allowed | NO Mobile Phones/Smart Devices</font>", st['student_info'])]
    ]
    t_hdr = Table(hdr_data, colWidths=[523])
    t_hdr.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1e3a8a')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,1), (-1,1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(t_hdr)
    story.append(Spacer(1, 4))

    # Question 1: Hashing
    story.append(Paragraph("<b>Question 1: Hashing & Open Addressing with Double Hashing (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given an empty Open Addressing Hash Table with <b>TableSize = 13</b> (indices 0 to 12).<br/>"
                           "Keys are mapped by primary hash function: <b>h₀(x) = x mod 13</b>.<br/>"
                           "Collisions are resolved by <b>Double Hashing</b>: <b>hᵢ(x) = (h₀(x) + f(i)) mod 13</b>, where <b>f(i) = i × (11 - (x mod 11))</b>.<br/>"
                           "Insert the following 6 keys sequentially: <b>[ 43, 17, 82, 95, 35, 160 ]</b>.", st['body']))
    story.append(Spacer(1, 3))

    # Grid for hash table
    ht_hdr = [Paragraph("<b>Index</b>", st['cell_bold'])] + [Paragraph(f"<b>{i}</b>", st['cell_bold']) for i in range(13)]
    ht_key = [Paragraph("<b>Key</b>", st['cell_bold'])] + [Paragraph("", st['cell']) for _ in range(13)]
    ht_info = [Paragraph("<b>Info</b>", st['cell_bold'])] + [Paragraph("", st['cell']) for _ in range(13)]
    t_ht = Table([ht_hdr, ht_key, ht_info], colWidths=[43] + [36.9]*13)
    t_ht.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_ht)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>1.1 Step-by-Step Collision & Probing Trace Table:</b> [4 Marks]", st['sub_q']))
    trace_h = [
        Paragraph("<b>Key (x)</b>", st['cell_bold']),
        Paragraph("<b>h₀(x) = x mod 13</b>", st['cell_bold']),
        Paragraph("<b>Double Hashing Step & Calculation f(i)</b>", st['cell_bold']),
        Paragraph("<b>Final Index</b>", st['cell_bold']),
        Paragraph("<b>Collisions</b>", st['cell_bold'])
    ]
    trace_rows = [trace_h] + [[Paragraph(str(k), st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell'])] for k in [43, 17, 82, 95, 35, 160]]
    t_trace = Table(trace_rows, colWidths=[55, 95, 233, 70, 70])
    t_trace.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_trace)
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>1.2 Collision Analysis:</b> Which key collided the most? State the key, total collisions, and indices attempted: [1.5 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Key: .................................... Collisions: .................... Indices Attempted: ................................................................<br/>"
        "<b>1.3 Total Collision Count:</b> Total number of collisions and resolving probes accumulated: .................... times [1.5 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<font color='#b91c1c'>*(Warning: Count cumulative probes only. Do NOT double count collision vs resolve)*</font><br/>"
        "<b>1.4 Load Factor Percentage:</b> Calculate the exact Load Factor percentage after inserting all 6 keys: [1 Mark]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Formula & Calculation: λ = (N × 100) / TableSize = ................................................................................ = ........................ %<br/>"
        "<b>1.5 Rehashing Threshold & New Size:</b> If Rehashing occurs at 70% capacity: [1 Mark]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• How many more keys must be inserted to trigger Rehashing? ............................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• What is the TableSize of the newly created hash table? ....................................................................................<br/>"
        "<b>1.6 Concept of Wrap-Around:</b> Define the concept of 'Wrap-Around' in Hashing as taught in class: [1 Mark]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Definition: .............................................................................................................................................................",
        st['body']
    ))

    # =========================================================================
    # PAGE 2: QUESTION 2: BINARY MIN-HEAP
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 2: Priority Queue (Binary Min-Heap) Operations & Array Tracing (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given the sequence of 10 integer keys: <b>[ 65, 30, 48, 15, 22, 10, 50, 18, 25, 8 ]</b>.<br/>"
                           "Trace the 1-based array representation for each of the four operations below (Index 0 is unused / None).", st['body']))
    story.append(Spacer(1, 3))

    def make_heap_table(label):
        hdr = [Paragraph("<b>Index</b>", st['cell_bold'])] + [Paragraph(f"<b>{i}</b>", st['cell_bold']) for i in range(12)]
        val = [Paragraph(f"<b>{label}</b>", st['cell_bold'])] + [Paragraph("None" if i==0 else "", st['cell']) for i in range(12)]
        t = Table([hdr, val], colWidths=[71] + [41]*12)
        t.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
            ('BACKGROUND', (1,1), (1,1), colors.HexColor('#f1f5f9')),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ]))
        return t

    story.append(Paragraph("<b>2.1 Array State 1:</b> After sequentially inserting all 10 elements into Min-Heap (Percolate Up): [3 Marks]", st['sub_q']))
    story.append(make_heap_table("Heap Array"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.2 Array State 2:</b> After executing <b>deleteMin()</b> operation #1 (Percolate Down): [2 Marks]", st['sub_q']))
    story.append(make_heap_table("After Del 1"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.3 Array State 3:</b> After executing <b>insert(12)</b> (Percolate Up): [2 Marks]", st['sub_q']))
    story.append(make_heap_table("After Ins 12"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2.4 Array State 4:</b> After executing second <b>deleteMin()</b> operation #2 (Percolate Down): [1 Mark]", st['sub_q']))
    story.append(make_heap_table("After Del 2"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>2.5 Binary Heap 1D Array Mathematical Formulas:</b> [1 Mark]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;For a node at index <i>i</i> in a 1-based array implementation:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Left Child Index: .................................... &nbsp;|&nbsp; Right Child Index: .................................... &nbsp;|&nbsp; Parent Index: ....................................<br/>"
        "<b>2.6 Truncation Rule:</b> Why must integer floor division (e.g., Python <code>//</code>) be used for parent calculation, and why is rounding up prohibited? [0.5 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Explanation: ....................................................................................................................................................................<br/>"
        "<b>2.7 Percolate Down Code Condition:</b> State the exact Python <code>if-else</code> condition used to pick the smaller child before swapping: [0.5 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Code: ...........................................................................................................................................................................",
        st['body']
    ))

    # =========================================================================
    # PAGE 3: QUESTION 3: INSERTION SORT & QUESTION 4: SELECTION SORT
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 3: Insertion Sort Tracing & Position Moves (10 Marks)</b>", st['h1']))
    story.append(Paragraph(
        "<b>3.1 Worst-Case Mathematical Analysis (N = 10 Elements):</b> [3 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Define Worst-Case input configuration: ....................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Total Position Moves Formula & Exact Calculation: Total Moves = ................................................... = ................ moves.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Best-Case Position Moves: .................... moves.",
        st['body']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.2 Pass Tracing on 10-Element Array:</b> [4 Marks]<br/>"
                           "Given array: <b>[ 54, 38, 16, 27, 10, 62, 45, 9, 70, 31 ]</b>.", st['body']))
    p_hdr = [Paragraph("<b>Pass (p)</b>", st['cell_bold']), Paragraph("<b>Key Element</b>", st['cell_bold']), Paragraph("<b>Elements Shifted (Position Moves)</b>", st['cell_bold']), Paragraph("<b>Array State After Pass p</b>", st['cell_bold'])]
    p_r1 = [Paragraph("<b>p = 3</b>", st['cell_bold']), Paragraph("27", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell'])]
    p_r2 = [Paragraph("<b>p = 6</b>", st['cell_bold']), Paragraph("45", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell'])]
    t_pass = Table([p_hdr, p_r1, p_r2], colWidths=[55, 65, 170, 233])
    t_pass.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_pass)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3.3 Program Modification:</b> How do we modify Insertion Sort to count total position moves in code? [3 Marks]<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;• Describe where the move counter increment statement must be placed:<br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;  ....................................................................................................................................................................................", st['body']))
    story.append(Spacer(1, 4))

    # Question 4: Selection Sort
    story.append(Paragraph("<b>Question 4: Selection Sort Tracing (Test Program 2 Worksheet Template) (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given the 7-element unsorted array: <b>[ 64, 25, 12, 38, 11, 49, 20 ]</b>.<br/>"
                           "Write the exact steps for <b>Round 1, Round 2, Round 3, Round 4</b> according to the classroom format: [8 Marks]", st['body']))
    story.append(Spacer(1, 2))

    story.append(Paragraph(
        "<b>Round 1:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ 64, 25, 12, 38, 11, 49, 20 ], the minimum is ........ at index ........<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum with first element of unsorted array (64)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Before swap: [ ........................................................................................................................................................ ]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;[ ........................................................................................................................................................ ]<br/>"
        "&nbsp;&nbsp;3. Result: Now 1 element sorted. The remaining unsorted array is: [ ................................................................................ ]<br/>"
        "<b>Round 2:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ .................................................... ], the minimum is ........ at index ........<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum with first element of unsorted array<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Before swap: [ ........................................................................................................................................................ ]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;[ ........................................................................................................................................................ ]<br/>"
        "&nbsp;&nbsp;3. Result: Now 2 elements sorted. The remaining unsorted array is: [ ................................................................................ ]<br/>"
        "<b>Round 3:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ .................................................... ], the minimum is ........ at index ........<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum with first element of unsorted array<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;[ ........................................................................................................................................................ ]<br/>"
        "&nbsp;&nbsp;3. Result: Now 3 elements sorted. The remaining unsorted array is: [ ................................................................................ ]<br/>"
        "<b>Round 4:</b><br/>"
        "&nbsp;&nbsp;1. Find minimum: From unsorted array [ .................................................... ], the minimum is ........ at index ........<br/>"
        "&nbsp;&nbsp;2. Swap: swap minimum with first element of unsorted array<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• After swap: &nbsp;[ ........................................................................................................................................................ ]<br/>"
        "&nbsp;&nbsp;3. Result: Now 4 elements sorted. The remaining unsorted array is: [ ................................................................................ ]<br/>"
        "<b>4.2 Maximum Swaps:</b> What is the maximum number of swaps performed by Selection Sort for N = 7? .................... swaps [2 Marks]",
        st['body']
    ))

    # =========================================================================
    # PAGE 4: QUESTION 5: TOPOLOGICAL SORT
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 5: Topological Sort (Kahn's Algorithm on 7-Vertex DAG) (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given the Directed Acyclic Graph (DAG) shown below with <b>|V| = 7</b> vertices and <b>|E| = 9</b> directed edges:", st['body']))
    story.append(Spacer(1, 2))

    topo_img_path = os.path.join(DIAGRAM_DIR, "set_b_topo.png")
    if os.path.exists(topo_img_path):
        img = RLImage(topo_img_path, width=420, height=170)
        img.hAlign = 'CENTER'
        story.append(img)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.1 In-Degree Array Table:</b> Calculate initial in-degree for all vertices: [2 Marks]", st['sub_q']))
    id_hdr = [Paragraph("<b>Vertex</b>", st['cell_bold'])] + [Paragraph(f"<b>{i}</b>", st['cell_bold']) for i in range(1, 8)]
    id_row = [Paragraph("<b>In-Degree</b>", st['cell_bold'])] + [Paragraph("", st['cell']) for _ in range(7)]
    t_id = Table([id_hdr, id_row], colWidths=[71] + [64.5]*7)
    t_id.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_id)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5.2 Circular Queue Simulation Table:</b> Trace Queue states as vertices are processed: [4 Marks]", st['sub_q']))
    q_hdr = [Paragraph("<b>Step #</b>", st['cell_bold']), Paragraph("<b>Action (Dequeue / Enqueue)</b>", st['cell_bold']), Paragraph("<b>Queue Contents</b>", st['cell_bold']), Paragraph("<b>Front Ptr</b>", st['cell_bold']), Paragraph("<b>Back Ptr</b>", st['cell_bold'])]
    q_rows = [q_hdr] + [[Paragraph(str(i), st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell'])] for i in range(1, 9)]
    t_q = Table(q_rows, colWidths=[40, 203, 160, 60, 60])
    t_q.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q)
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "<b>5.3 Final Topological Ordering:</b> State the final output order of vertices: [2 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Order: ....................................................................................................................................................................<br/>"
        "<b>5.4 Directed Cycle Detection:</b> What happens to Kahn's algorithm if the graph contains a directed cycle? [2 Marks]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Explanation: ....................................................................................................................................................................",
        st['body']
    ))

    # =========================================================================
    # PAGE 5: QUESTION 6: UNWEIGHTED SHORTEST PATH
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 6: Unweighted Shortest Path Algorithm (BFS) (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Given the directed graph below with <b>|V| = 7</b> vertices (A to G) and <b>|E| = 11</b> edges.<br/>"
                           "Start vertex is <b>Vertex A</b>. Execute Breadth-First Search (BFS) to find the shortest path to all vertices:", st['body']))
    story.append(Spacer(1, 2))

    sp_img_path = os.path.join(DIAGRAM_DIR, "set_b_shortest_path.png")
    if os.path.exists(sp_img_path):
        img_sp = RLImage(sp_img_path, width=420, height=160)
        img_sp.hAlign = 'CENTER'
        story.append(img_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.1 Shortest Path Processing Table (Assignment 4 Style):</b> [5 Marks]<br/>"
                           "<i>(Cross out previous values when updated: Known starts F, Dist starts 999 except start vertex, Path starts 0)</i>", st['sub_q']))
    sp_hdr = [Paragraph("<b>Vertex (v)</b>", st['cell_bold']), Paragraph("<b>Known (T / F)</b>", st['cell_bold']), Paragraph("<b>Dist (dᵥ)</b>", st['cell_bold']), Paragraph("<b>Path (pᵥ)</b>", st['cell_bold'])]
    sp_rows = [sp_hdr] + [[Paragraph(v, st['cell_bold']), Paragraph("", st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell'])] for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    t_sp = Table(sp_rows, colWidths=[90, 140, 140, 153])
    t_sp.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>6.2 Circular Queue Tracing:</b> [2 Marks]", st['sub_q']))
    q_sp_hdr = [Paragraph("<b>Step</b>", st['cell_bold']), Paragraph("<b>Action</b>", st['cell_bold']), Paragraph("<b>Queue State</b>", st['cell_bold'])]
    q_sp_rows = [q_sp_hdr] + [[Paragraph(str(i), st['cell']), Paragraph("", st['cell']), Paragraph("", st['cell'])] for i in range(1, 8)]
    t_q_sp = Table(q_sp_rows, colWidths=[60, 240, 223])
    t_q_sp.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_q_sp)
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "<b>6.3 Backtracking Analysis & Shortest Path Query:</b> [3 Marks]<br/>"
        "• Find shortest path from <b>Vertex A to Vertex F</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Length (exact number of edges): .................... edges &nbsp;|&nbsp; Path Sequence: ............................................................................<br/>"
        "• Find shortest path from <b>Vertex A to Vertex G</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Length (exact number of edges): .................... edges &nbsp;|&nbsp; Path Sequence: ............................................................................<br/>"
        "<font color='#b91c1c'>*(Strict rule: Length must be integer number of edges, NOT cm/inches. Path must be comma-separated, NO arrows)*</font>",
        st['body']
    ))

    # =========================================================================
    # PAGE 6: QUESTION 7: ADVANCED THEORY, PROPERTIES & % CALCULATIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 7: Advanced Theory, Structural Properties & Percentage Calculations (10 Marks)</b>", st['h1']))
    story.append(Paragraph("Answer the following questions concisely. All calculations must be computed as <b>exact integers or percentages</b> (No formulas/powers).", st['body']))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.1 Structural Properties (Two Properties vs Three Properties):</b> [3 Marks]", st['sub_q']))
    story.append(Paragraph(
        "(a) Which fundamental data structure possesses exactly <b>two formal properties</b>? State the data structure and define both properties:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Data Structure: ........................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 1: ....................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 2: ....................................................................................................................................................................<br/>"
        "(b) Which theoretical concept possesses exactly <b>three formal properties</b>? State the concept and list all three properties:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Concept: ................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 1: ....................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 2: ....................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Property 3: ....................................................................................................................................................................<br/>"
        "(c) Which of the three properties in (b) is <b>impossible to achieve in practice</b>, and state the <b>two fundamental reasons</b> why:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Impossible Property: ....................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Reason 1: ........................................................................................................................................................................<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Reason 2: ........................................................................................................................................................................",
        st['body']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.2 Graph Memory Waste Percentage Calculation:</b> [2 Marks]", st['sub_q']))
    story.append(Paragraph(
        "A directed graph has |V| = 8 vertices and |E| = 14 directed edges.<br/>"
        "• Total cells in Adjacency Matrix: .................................... cells.<br/>"
        "• Number and percentage of cells containing 1 (active edges): .................. cells &nbsp;(........................ %)<br/>"
        "• Number and percentage of cells containing 0 (wasted space): .................. cells &nbsp;(........................ %)<br/>"
        "• Total memory cells required if represented as an Adjacency List (|V| + |E|): .................................... cells.<br/>"
        "• Percentage of memory saved by Adjacency List compared to Adjacency Matrix: .................................... %",
        st['body']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.3 Complete Graph Edge Calculations:</b> [1.5 Marks]", st['sub_q']))
    story.append(Paragraph(
        "(a) A complete undirected graph K₁₂ has |V| = 12 vertices. Calculate the total number of edges as an <b>exact integer</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Calculation & Answer: ................................................................................................................................ edges.<br/>"
        "(b) A complete directed graph with 12 vertices without self-loops has: ............................................................ directed edges.<br/>"
        "<font color='#b91c1c'>*(Strict rule: Answers must be evaluated integers, NOT mathematical formulas)*</font>",
        st['body']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.4 Complete Binary Tree Node Bounds:</b> [2 Marks]", st['sub_q']))
    story.append(Paragraph(
        "For a Complete Binary Tree where the Root is at height h = 0, calculate exact integer bounds:<br/>"
        "• Height h = 12: Minimum nodes = .................................... nodes &nbsp;|&nbsp; Maximum nodes = .................................... nodes.<br/>"
        "• Height h = 15: Minimum nodes = .................................... nodes &nbsp;|&nbsp; Maximum nodes = .................................... nodes.<br/>"
        "<font color='#b91c1c'>*(Strict rule: Answers MUST be computed exact integers, NOT exponential expressions like 2¹² or 2¹⁵)*</font>",
        st['body']
    ))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>7.5 Instructor Exam Traps & Specific Definitions:</b> [1.5 Marks]", st['sub_q']))
    story.append(Paragraph(
        "(a) In graph theory, why does writing path sequence with arrows (e.g., A → B → C) result in <b>zero marks</b>? What is the correct format?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Explanation & Format: ........................................................................................................................................................<br/>"
        "(b) If asked for the shortest path between two vertices in a Null Graph (V = {}, E = {}), what is the correct response?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Answer: ...........................................................................................................................................................................",
        st['body']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>*** END OF EXAMINATION PAPER — WISHING YOU THE BEST OF LUCK! ***</b>", ParagraphStyle('EndNotice', fontName='Tahoma-Bold', fontSize=8, leading=10, alignment=1, textColor=colors.HexColor('#1e3a8a'))))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built Blank Exam Paper: {PAPER_PDF}")

if __name__ == '__main__':
    build_paper_pdf()
