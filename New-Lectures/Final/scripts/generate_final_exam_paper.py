"""
Final Exam Paper Generator (English Version)
Course: 060243106 / 060223119 Data Structures and Algorithms
Faculty of Information Technology / Faculty of Applied Science, KMUTNB
Semester 1, Academic Year 2026
Instructor: Dr. Pradit Pitaksatheinkul
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image as RLImage, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Fonts
pdfmetrics.registerFont(TTFont('Tahoma', r'C:\Windows\Fonts\tahoma.ttf'))
pdfmetrics.registerFont(TTFont('Tahoma-Bold', r'C:\Windows\Fonts\tahomabd.ttf'))

OUTPUT_PDF = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\Final_Exam_2026_Paper_English.pdf'
DIAGRAM_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'diagrams')

def build_pdf():
    # Page setup: A4 = 595.27 x 841.89 pt. Margins: 36 pt (0.5 in)
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    style_title = ParagraphStyle(
        'DocTitle',
        fontName='Tahoma-Bold',
        fontSize=13,
        leading=16,
        alignment=1, # Center
        textColor=colors.HexColor('#0f172a')
    )
    style_subtitle = ParagraphStyle(
        'DocSubTitle',
        fontName='Tahoma',
        fontSize=10,
        leading=13,
        alignment=1,
        textColor=colors.HexColor('#334155')
    )
    style_student_info = ParagraphStyle(
        'StudentInfo',
        fontName='Tahoma',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#1e293b')
    )
    style_section_h1 = ParagraphStyle(
        'SectionH1',
        fontName='Tahoma-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=6,
        spaceAfter=3
    )
    style_body = ParagraphStyle(
        'Body',
        fontName='Tahoma',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor('#1e293b')
    )
    style_body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Tahoma-Bold',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor('#0f172a')
    )
    style_code = ParagraphStyle(
        'Code',
        fontName='Tahoma-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#095299')
    )
    style_table_cell = ParagraphStyle(
        'TableCell',
        fontName='Tahoma',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.HexColor('#0f172a')
    )
    style_table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Tahoma-Bold',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.HexColor('#0f172a')
    )
    style_notice = ParagraphStyle(
        'Notice',
        fontName='Tahoma-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#b91c1c')
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER & HEADER & QUESTION 1 (HASHING)
    # =========================================================================
    header_table_data = [
        [
            Paragraph("<b>KING MONGKUT'S UNIVERSITY OF TECHNOLOGY NORTH BANGKOK</b><br/>"
                      "Faculty of Applied Science / Faculty of Information Technology<br/>"
                      "<b>FINAL EXAMINATION — SEMESTER 1, ACADEMIC YEAR 2026</b>", style_title)
        ],
        [
            Paragraph("<b>Course:</b> 060243106 & 060223119 Data Structures and Algorithms &nbsp;&nbsp;|&nbsp;&nbsp; "
                      "<b>Instructor:</b> Dr. Pradit Pitaksatheinkul<br/>"
                      "<b>Duration:</b> 3 Hours (09:00 - 12:00) &nbsp;&nbsp;|&nbsp;&nbsp; "
                      "<b>Total Score:</b> 70 Raw Marks (Scaled to 35% of Final Grade)", style_subtitle)
        ]
    ]
    t_header = Table(header_table_data, colWidths=[523])
    t_header.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#1e3a8a')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 6))

    # Student identification bar & Instructions
    info_table_data = [
        [
            Paragraph("<b>Student Name:</b> ....................................................................................", style_student_info),
            Paragraph("<b>Student ID:</b> ........................................", style_student_info),
            Paragraph("<b>Section:</b> .............", style_student_info)
        ],
        [
            Paragraph("<b>Instructions & Regulations:</b><br/>"
                      "1. <b>Open Book:</b> Textbooks, lecture handouts, and personal handwritten notes are permitted.<br/>"
                      "2. <b>Scientific Calculator:</b> Allowed for hash modular arithmetic and percentage calculations.<br/>"
                      "3. <b>Strict Prohibition:</b> Smartphones, tablets, and communication devices are strictly prohibited (Turn OFF and put in bags).<br/>"
                      "4. Answer all <b>7 questions</b> clearly in the provided grids and blank lines. Points are awarded based on strict algorithmic tracing.",
                      style_body),
            "", ""
        ]
    ]
    t_info = Table(info_table_data, colWidths=[270, 180, 73])
    t_info.setStyle(TableStyle([
        ('SPAN', (0,1), (2,1)),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94a3b8')),
        ('BACKGROUND', (0,1), (2,1), colors.HexColor('#eff6ff')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------------------
    # Question 1: Hashing (10 Marks)
    # -------------------------------------------------------------------------
    story.append(Paragraph("<b>Question 1: Hash Table with Open Addressing and Double Hashing (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "A hash table using <b>Open Addressing</b> is designed with a table capacity <b>TableSize = 19</b>. "
        "The system triggers automatic <b>Rehashing</b> when the load factor reaches or exceeds <b>80%</b>.<br/>"
        "Collision resolution is performed using <b>Double Hashing</b> with primary and secondary functions defined as:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; Primary Hash Function: <b>h<sub>0</sub>(X) = X mod 19</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; Collision Offset Function: <b>f(i) = i &times; (R - (X mod R))</b>, where <b>R = 17</b> and <b>i</b> is the collision index (1, 2, ...)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; Probe Sequence: <b>h<sub>i</sub>(X) = (h<sub>0</sub>(X) + f(i)) mod 19</b><br/>"
        "Insert the following <b>8 keys</b> sequentially into the hash table: "
        "<b>26, &nbsp;45, &nbsp;70, &nbsp;85, &nbsp;102, &nbsp;123, &nbsp;143, &nbsp;155</b>",
        style_body
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<i>Note: Each probed slot that is already occupied counts as exactly 1 collision (as explained in classroom lectures).</i>",
        style_body_bold
    ))
    story.append(Spacer(1, 5))

    # Table grid 0..18 (Python 1D Hash Table: Slot and Stored Key)
    h_row0 = ['Slot'] + [str(i) for i in range(19)]
    h_row1 = ['Stored Key'] + ['' for _ in range(19)]
    
    t_q1_grid = Table([h_row0, h_row1], colWidths=[55] + [24.6]*19, rowHeights=[18, 28])
    t_q1_grid.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#334155')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f1f5f9')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_q1_grid)
    story.append(Spacer(1, 6))

    # Sub-questions 1.1 - 1.4
    q1_sub = [
        [
            Paragraph("<b>1.1 Collision Tracing Table:</b> Write the step-by-step collision sequence for each key:", style_body_bold),
            Paragraph("<b>[4 Marks]</b>", style_body_bold)
        ],
        [
            Paragraph(
                "&bull; <b>Key 26:</b> h<sub>0</sub> = 26 mod 19 = ..... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 45:</b> h<sub>0</sub> = 45 mod 19 = ..... &rarr; Collision at Slot: ....... &rarr; f(1) = ....... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 70:</b> h<sub>0</sub> = 70 mod 19 = ..... &rarr; Collision at Slot: ....... &rarr; f(1) = ....... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 85:</b> h<sub>0</sub> = 85 mod 19 = ..... &rarr; Collision 1: ....... &rarr; Collision 2: ....... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 102:</b> h<sub>0</sub> = 102 mod 19 = ..... &rarr; Collision 1: ....... &rarr; Collision 2: ....... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 123:</b> h<sub>0</sub> = 123 mod 19 = ..... &rarr; Collision 1: ....... &rarr; Collision 2: ....... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 143:</b> h<sub>0</sub> = 143 mod 19 = ..... &rarr; Slot: ....... (Collisions: .....)<br/>"
                "&bull; <b>Key 155:</b> h<sub>0</sub> = 155 mod 19 = ..... &rarr; Collision at Slot: ....... &rarr; f(1) = ....... &rarr; Slot: ....... (Collisions: .....)",
                style_body
            ),
            ""
        ],
        [
            Paragraph("<b>1.2 Maximum Collisions:</b> Which key(s) experienced the highest number of collisions? State the key(s), the number of collisions, and the specific slot indices where collisions occurred.<br/>"
                      "<b>Answer:</b> Key(s): ............................................ | Max Collisions: ............. | Collided at slots: ...........................................................", style_body),
            Paragraph("<b>[2 Marks]</b>", style_body_bold)
        ],
        [
            Paragraph("<b>1.3 Total Collision Count:</b> What is the total cumulative number of collisions and resolution steps across all 8 insertions?<br/>"
                      "<b>Answer:</b> Total Collisions = .......................................................................................................................................................", style_body),
            Paragraph("<b>[2 Marks]</b>", style_body_bold)
        ],
        [
            Paragraph("<b>1.4 Rehashing Threshold:</b> After inserting all 8 keys, how many additional keys must be inserted into the table to trigger Rehashing? (Show calculation step).<br/>"
                      "<b>Calculation & Answer:</b> ..........................................................................................................................................................", style_body),
            Paragraph("<b>[2 Marks]</b>", style_body_bold)
        ]
    ]
    t_q1_sub = Table(q1_sub, colWidths=[460, 63])
    t_q1_sub.setStyle(TableStyle([
        ('SPAN', (0,1), (1,1)),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,1), (-1,1), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,2), (-1,2), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,3), (-1,3), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(t_q1_sub)

    # =========================================================================
    # PAGE 2: QUESTION 2 (BINARY MIN-HEAP)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 2: Binary Min-Heap Operations & Array Representation (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "A <b>Binary Min-Heap</b> is represented in a 1-dimensional array using 1-based indexing (where <b>Index 0 is unused</b>). "
        "The fundamental array indexing properties are:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Left Child(i) = 2i</b> &nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Right Child(i) = 2i + 1</b> &nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Parent(i) = floor(i / 2)</b><br/>"
        "You are given the following sequence of <b>12 integer keys</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>64, &nbsp;14, &nbsp;24, &nbsp;1, &nbsp;20, &nbsp;2, &nbsp;5, &nbsp;10, &nbsp;6, &nbsp;8, &nbsp;15, &nbsp;20</b><br/>"
        "Perform the operations sequentially from <b>2.1 to 2.4</b> and record the final array states in the <b>4 vertical columns</b> below.",
        style_body
    ))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "<i>Instructor's Strict Warning: Perform all operations strictly adhering to the algorithmic Percolate-Up and Percolate-Down procedures taught in class. Do not guess the final tree layout by intuition. Grading strictly follows program execution traces.</i>",
        style_notice
    ))
    story.append(Spacer(1, 6))

    # 4 Vertical Array Columns matching Dr. Pradit's official worksheet
    heap_headers = [
        Paragraph("<b>Index</b>", style_body_bold),
        Paragraph("<b>2.1 Insert 12 Keys</b><br/><font size='7' color='#475569'>[1 Mark]</font>", style_body_bold),
        Paragraph("<b>2.2 deleteMin() 1</b><br/><font size='7' color='#475569'>[2 Marks]</font>", style_body_bold),
        Paragraph("<b>2.3 Insert key 3</b><br/><font size='7' color='#475569'>[2 Marks]</font>", style_body_bold),
        Paragraph("<b>2.4 deleteMin() 2</b><br/><font size='7' color='#475569'>[3 Marks]</font>", style_body_bold)
    ]
    heap_rows = [heap_headers]
    for idx in range(13):
        idx_str = f"[{idx}]"
        if idx == 0:
            heap_rows.append([idx_str, '-', '-', '-', '-'])
        elif idx == 12:
            heap_rows.append([idx_str, '', '-', '', '-'])
        else:
            heap_rows.append([idx_str, '', '', '', ''])

    t_heap_vert = Table(heap_rows, colWidths=[55, 117, 117, 117, 117])
    t_heap_vert.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0f2fe')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (1,1), (-1,1), colors.HexColor('#e2e8f0')), # row [0]
        ('BACKGROUND', (2,13), (2,13), colors.HexColor('#e2e8f0')), # row [12] col 2
        ('BACKGROUND', (4,13), (4,13), colors.HexColor('#e2e8f0')), # row [12] col 4
        ('FONTNAME', (0,0), (-1,-1), 'Tahoma'),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_heap_vert)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>2.5 Heap Properties Verification:</b> [2 Marks]<br/>"
        "State the two fundamental properties that every Binary Heap must satisfy:<br/>"
        "1. <b>Structure Property:</b> ...................................................................................................................................................................<br/>"
        "2. <b>Heap-Order Property:</b> ...................................................................................................................................................................",
        style_body
    ))

    # =========================================================================
    # PAGE 3: QUESTION 3 (INSERTION SORT) & QUESTION 4 (SELECTION & BUBBLE SORT)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 3: Insertion Sort Tracing & Position Moves (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "Recall the standard <code>insertionSort</code> algorithm from Chapter 7. A <b>Position Move</b> (or Data Shift) is defined "
        "as each shift assignment <code>a[j] = a[j - 1]</code> executed inside the inner loop.",
        style_body
    ))
    story.append(Spacer(1, 4))

    # 3.1 Worst case
    story.append(Paragraph(
        "<b>3.1 Worst-Case Analysis:</b> [4 Marks]<br/>"
        "Specify an initial input array of <b>12 integers</b> that represents the exact <b>Worst-Case Scenario</b> for insertion sort. "
        "Write the input array in the first table, and calculate the <b>Total Position Moves</b> upon completion.<br/>"
        "<b>Input Array (Worst Case):</b>",
        style_body
    ))
    story.append(Spacer(1, 3))
    
    t_worst = Table([['Index'] + [str(i) for i in range(12)], ['Value'] + ['' for _ in range(12)]], colWidths=[47] + [39.6]*12)
    t_worst.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_worst)
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "Formula & Calculation for Total Position Moves: .............................................................................................................<br/>"
        "<b>Total Position Moves = ............................ moves.</b>",
        style_body_bold
    ))
    story.append(Spacer(1, 6))

    # 3.2 Specific Trace
    story.append(Paragraph(
        "<b>3.2 Pass Tracing for Input Array:</b> [6 Marks]<br/>"
        "Given the initial array of 12 numbers: <b>[61, &nbsp;52, &nbsp;12, &nbsp;24, &nbsp;8, &nbsp;35, &nbsp;32, &nbsp;5, &nbsp;71, &nbsp;68, &nbsp;18, &nbsp;2]</b><br/>"
        "Write the array content and count the position moves occurred specifically at <b>Pass p = 3</b> and <b>Pass p = 6</b>:",
        style_body
    ))
    story.append(Spacer(1, 3))

    t_p3_p6 = Table([
        ['Pass'] + [f"[{i}]" for i in range(12)] + [Paragraph("<b>Position Moves<br/>in Pass</b>", style_table_cell_bold)],
        ['Initial', '61', '52', '12', '24', '8', '35', '32', '5', '71', '68', '18', '2', '-'],
        ['p = 3', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['p = 6', '', '', '', '', '', '', '', '', '', '', '', '', '']
    ], colWidths=[38] + [33.0]*12 + [89])
    t_p3_p6.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#f8fafc')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
    ]))
    story.append(t_p3_p6)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------------------
    # Question 4: Selection Sort & Bubble Sort (10 Marks)
    # -------------------------------------------------------------------------
    story.append(Paragraph("<b>Question 4: Selection Sort & Bubble Sort Tracing (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "Trace the execution of <b>Selection Sort</b> and <b>Bubble Sort</b> on the given arrays as instructed below.",
        style_body
    ))
    story.append(Spacer(1, 4))

    # 4.1 Selection Sort
    story.append(Paragraph(
        "<b>4.1 Selection Sort Tracing:</b> [5 Marks]<br/>"
        "Given the array <b>[64, &nbsp;25, &nbsp;12, &nbsp;22, &nbsp;11]</b>. Trace the array contents after each pass. "
        "Record the index of the minimum element found and the swap operation performed:",
        style_body
    ))
    story.append(Spacer(1, 3))
    t_sel = Table([
        ['Pass', 'Current Array State', 'Min Element Found (Index)', 'Swap Action'],
        ['Initial', '[64,  25,  12,  22,  11]', '-', '-'],
        ['Pass 1', '', '', ''],
        ['Pass 2', '', '', ''],
        ['Pass 3', '', '', ''],
        ['Pass 4', '', '', '']
    ], colWidths=[55, 190, 140, 138])
    t_sel.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0e7ff')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_sel)
    story.append(Spacer(1, 6))

    # 4.2 Bubble Sort
    story.append(Paragraph(
        "<b>4.2 Bubble Sort Tracing & Early Termination:</b> [5 Marks]<br/>"
        "Given the array <b>[54, &nbsp;26, &nbsp;93, &nbsp;17, &nbsp;77]</b>. Trace each pass, count comparisons and swaps. "
        "Does the algorithm terminate early? If so, after which pass?",
        style_body
    ))
    story.append(Spacer(1, 3))
    t_bub = Table([
        ['Pass', 'Array State after Pass', 'Comparisons in Pass', 'Swaps in Pass', 'Swapped (T/F)'],
        ['Initial', '[54,  26,  93,  17,  77]', '-', '-', '-'],
        ['Pass 1', '', '', '', ''],
        ['Pass 2', '', '', '', ''],
        ['Pass 3', '', '', '', ''],
        ['Pass 4', '', '', '', '']
    ], colWidths=[55, 175, 105, 95, 93])
    t_bub.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#fef3c7')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_bub)
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Total Comparisons:</b> ........... &nbsp;&nbsp;|&nbsp;&nbsp; <b>Total Swaps:</b> ........... &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Early Termination occurred at Pass:</b> ...........",
        style_body_bold
    ))

    # =========================================================================
    # PAGE 4: QUESTION 5 (TOPOLOGICAL SORT)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 5: Topological Sort in Directed Acyclic Graph (DAG) (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "A Directed Acyclic Graph (DAG) with <b>7 vertices (1 to 7)</b> is defined by the graph structure and its linked <b>Adjacency List</b> below:",
        style_body
    ))
    story.append(Spacer(1, 3))

    # Dual Diagrams: Directed Acyclic Graph (DAG) + Linked Adjacency List side by side
    img_topo_graph = os.path.join(DIAGRAM_DIR, 'graph_topo_sort.png')
    img_topo_adj = os.path.join(DIAGRAM_DIR, 'adj_topo_sort.png')
    if os.path.exists(img_topo_graph) and os.path.exists(img_topo_adj):
        t_diag_topo = Table([[
            RLImage(img_topo_graph, width=255, height=125),
            RLImage(img_topo_adj, width=255, height=125)
        ]], colWidths=[260, 260])
        t_diag_topo.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_diag_topo)
        story.append(Spacer(1, 4))

    # 5.1 Indegree tracking table
    story.append(Paragraph(
        "<b>5.1 Indegree Array Tracing:</b> [5 Marks]<br/>"
        "Fill in the <b>Indegree Array</b> below. Show the initial in-degree of each vertex, and show the update "
        "values after each round as vertices are dequeued. Record the exact vertices <b>Enqueued</b> and <b>Dequeued</b> in each round:",
        style_body
    ))
    story.append(Spacer(1, 3))

    t_topo_indeg = Table([
        ['Vertex (v)', 'Initial', 'Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5', 'Round 6', 'Round 7'],
        ['1', '', '', '', '', '', '', '', ''],
        ['2', '', '', '', '', '', '', '', ''],
        ['3', '', '', '', '', '', '', '', ''],
        ['4', '', '', '', '', '', '', '', ''],
        ['5', '', '', '', '', '', '', '', ''],
        ['6', '', '', '', '', '', '', '', ''],
        ['7', '', '', '', '', '', '', '', ''],
        ['Enqueue (v)', '', '', '', '', '', '', '', ''],
        ['Dequeue (v)', '', '', '', '', '', '', '', '']
    ], colWidths=[67] + [57]*8)
    t_topo_indeg.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (0,-2), (-1,-2), colors.HexColor('#f0fdf4')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#fef2f2')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('FONTNAME', (0,-2), (0,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_topo_indeg)
    story.append(Spacer(1, 6))

    # 5.2 Queue simulation (Dual representation: Horizontal past-exam array + Vertical worksheet stack)
    story.append(Paragraph(
        "<b>5.2 Circular Queue Simulation:</b> [2 Marks]<br/>"
        "Given a <b>Queue of capacity 7 (Indices 0 to 6)</b> implementing the circular queue functions "
        "<code>enqueue</code> and <code>dequeue</code> from Chapter 3.<br/>"
        "Draw the contents of the Queue array upon algorithm completion, and explicitly specify <b>front</b>, <b>back</b>, and <b>currentSize</b>:",
        style_body
    ))
    story.append(Spacer(1, 3))

    # Horizontal queue table
    t_q_horiz = Table([
        ['Index', '0', '1', '2', '3', '4', '5', '6'],
        ['Queue', '', '', '', '', '', '', '']
    ], colWidths=[48] + [44]*7, rowHeights=[16, 20])
    t_q_horiz.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0f2fe')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))

    # Vertical queue stack [6..0]
    t_q_vert = Table([
        ['q', 'Slot'],
        ['6', ''],
        ['5', ''],
        ['4', ''],
        ['3', ''],
        ['2', ''],
        ['1', ''],
        ['0', '']
    ], colWidths=[24, 60], rowHeights=[14]*8)
    t_q_vert.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#334155')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f1f5f9')),
        ('FONTNAME', (0,0), (-1,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))

    # Left info block
    q_left_flow = [
        t_q_horiz,
        Spacer(1, 4),
        Paragraph("<b>front อยู่ที่ตำแหน่ง:</b> .................................... &nbsp;&nbsp;&nbsp;&nbsp; <b>back อยู่ที่ตำแหน่ง:</b> ....................................", style_body_bold),
        Spacer(1, 2),
        Paragraph("<b>currentSize เมื่อจบการทำงาน:</b> .......................... &nbsp;&nbsp;|&nbsp;&nbsp; <b>สถานะคิว:</b> [ ] ว่างเปล่า (Empty) &nbsp;&nbsp; [ ] มีข้อมูลตกค้าง", style_body),
        Spacer(1, 2),
        Paragraph("<i>* การนำข้อมูลเข้าออกจาก Queue ยึดตามฟังก์ชัน enqueue: (back+1)%7 และ dequeue: (front+1)%7 ในหนังสือบทที่ 3</i>", style_body)
    ]

    t_dual_q = Table([[q_left_flow, t_q_vert]], colWidths=[425, 95])
    t_dual_q.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_dual_q)
    story.append(Spacer(1, 6))

    # 5.3 Final Topological Ordering
    story.append(Paragraph(
        "<b>5.3 Final Topological Ordering:</b> [3 Marks]<br/>"
        "Write the resulting Topological Ordering sequence produced by the algorithm:<br/>"
        "<b>Answer:</b> &nbsp;&nbsp;.......................................................................................................................................................................<br/>"
        "<i>* คำเตือนจุดได้ 0 คะแนน: ต้องคั่นด้วยเครื่องหมายจุลภาค (Comma เช่น 1, 2, 5, 4...) ห้ามเขียนเครื่องหมายลูกศร (1 &rarr; 2 &rarr; 5...) เด็ดขาด</i>",
        style_body
    ))

    # =========================================================================
    # PAGE 5: QUESTION 6 (UNWEIGHTED SHORTEST PATH)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 6: Unweighted Shortest Path Algorithm (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "A directed unweighted graph with <b>7 vertices (1 to 7)</b> is defined by the graph structure and its linked <b>Adjacency List</b> below (Source Vertex = 1):",
        style_body
    ))
    story.append(Spacer(1, 3))

    # Dual Diagrams: Directed Graph + Linked Adjacency List side by side
    img_sp_graph = os.path.join(DIAGRAM_DIR, 'graph_shortest_path.png')
    img_sp_adj = os.path.join(DIAGRAM_DIR, 'adj_shortest_path.png')
    if os.path.exists(img_sp_graph) and os.path.exists(img_sp_adj):
        t_diag_sp = Table([[
            RLImage(img_sp_graph, width=255, height=120),
            RLImage(img_sp_adj, width=255, height=120)
        ]], colWidths=[260, 260])
        t_diag_sp.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_diag_sp)
        story.append(Spacer(1, 3))

    story.append(Paragraph(
        "<b>6.1 Execution Table for Shortest Path (Starting Vertex = 1):</b> [5 Marks]<br/>"
        "Execute the BFS-based unweighted shortest path algorithm. Fill in the processing array table containing "
        "<b>Known (T / F)</b>, <b>Distance (d<sub>v</sub>)</b>, <b>Path (p<sub>v</sub>)</b>, and record the <b>Enqueue / Dequeue</b> sequences:",
        style_body
    ))
    story.append(Spacer(1, 3))

    t_sp_grid = Table([
        ['Vertex (v)', 'Known (T / F)', 'Distance (d_v)', 'Previous Path (p_v)', 'Shortest Route from Source (1)'],
        ['1', '', '', '', ''],
        ['2', '', '', '', ''],
        ['3', '', '', '', ''],
        ['4', '', '', '', ''],
        ['5', '', '', '', ''],
        ['6', '', '', '', ''],
        ['7', '', '', '', ''],
        ['Enqueue Sequence', '', '', '', ''],
        ['Dequeue Sequence', '', '', '', '']
    ], colWidths=[105, 80, 85, 105, 148])
    t_sp_grid.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (0,-2), (-1,-2), colors.HexColor('#f0fdf4')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#fef2f2')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('FONTNAME', (0,0), (0,-1), 'Tahoma-Bold'),
        ('FONTNAME', (0,-2), (0,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 7.8),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    story.append(t_sp_grid)
    story.append(Spacer(1, 6))

    # 6.2 Queue Status & Textbook Pseudocode Box (Dual representation matching past exam p.4 & p.10)
    story.append(Paragraph(
        "<b>6.2 Circular Queue State upon Completion & Algorithm Pseudocode:</b> [2 Marks]<br/>"
        "Given a <b>Queue of capacity 7 (Slots 0 to 6)</b> used to process BFS shortest paths.<br/>"
        "Draw the final contents of the Queue array and specify the pointer positions after the algorithm finishes:",
        style_body
    ))
    story.append(Spacer(1, 3))

    t_sp_q_horiz = Table([
        ['Index', '0', '1', '2', '3', '4', '5', '6'],
        ['Queue', '', '', '', '', '', '', '']
    ], colWidths=[48] + [44]*7, rowHeights=[16, 20])
    t_sp_q_horiz.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0f2fe')),
        ('FONTNAME', (0,0), (-1,0), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))

    t_sp_q_vert = Table([
        ['q', 'Slot'],
        ['6', ''],
        ['5', ''],
        ['4', ''],
        ['3', ''],
        ['2', ''],
        ['1', ''],
        ['0', '']
    ], colWidths=[24, 60], rowHeights=[14]*8)
    t_sp_q_vert.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.8, colors.HexColor('#475569')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#334155')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#f1f5f9')),
        ('FONTNAME', (0,0), (-1,-1), 'Tahoma-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))

    sp_q_left_flow = [
        t_sp_q_horiz,
        Spacer(1, 4),
        Paragraph("<b>front อยู่ที่ตำแหน่ง:</b> .................................... &nbsp;&nbsp;&nbsp;&nbsp; <b>back อยู่ที่ตำแหน่ง:</b> ....................................", style_body_bold),
        Spacer(1, 2),
        Paragraph("<b>currentSize:</b> .......................... &nbsp;&nbsp;|&nbsp;&nbsp; <b>สถานะคิว:</b> [ ] ว่างเปล่า (Empty) &nbsp;&nbsp; [ ] มีข้อมูลตกค้าง", style_body),
        Spacer(1, 2),
        Paragraph(
            "<b>Algorithm Pseudocode (Textbook Chapter 9 / Past Exam):</b><br/>"
            "<code>while (!q.isEmpty()) { v = q.dequeue(); v.known = true;<br/>"
            "&nbsp;&nbsp;for each w adjacent to v: if (w.dist == INFINITY) {<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;w.dist = v.dist + 1; w.path = v; q.enqueue(w); } }</code>",
            style_code
        )
    ]

    t_dual_sp_q = Table([[sp_q_left_flow, t_sp_q_vert]], colWidths=[425, 95])
    t_dual_sp_q.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_dual_sp_q)
    story.append(Spacer(1, 6))

    # 6.3 Backtracking Path
    story.append(Paragraph(
        "<b>6.3 Shortest Path Reconstruction & Zero-Mark Warning:</b> [3 Marks]<br/>"
        "<i>Professor's Rule: Path sequences MUST be written as comma-separated sequences (e.g. 1, 4, 5). "
        "DO NOT write arrows (1 &rarr; 4 &rarr; 5) which receives 0 marks. Path length is measured in number of EDGES.</i><br/>"
        "&bull; <b>The length of the shortest path from Vertex 1 to Vertex 5:</b> = ............. edges &nbsp;&nbsp;|&nbsp;&nbsp; <b>Sequence:</b> = .....................................................<br/>"
        "&bull; <b>The length of the shortest path from Vertex 1 to Vertex 7:</b> = ............. edges &nbsp;&nbsp;|&nbsp;&nbsp; <b>Sequence:</b> = .....................................................",
        style_body
    ))

    # =========================================================================
    # PAGE 6: QUESTION 7 (ADVANCED THEORY, PROPERTIES & CALCULATIONS)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("<b>Question 7: Advanced Theory, Structural Properties & Calculations (10 Marks)</b>", style_section_h1))
    story.append(Paragraph(
        "Answer the following short theory and mathematical questions concisely. All numerical calculations must be computed "
        "as <b>exact integers or percentages</b> (do NOT leave answers in exponent or algebraic forms).",
        style_body
    ))
    story.append(Spacer(1, 8))

    q7_items = [
        # 7.1
        [
            Paragraph("<b>7.1 Structural Properties (Data Structures Classification):</b><br/>"
                      "<b>(a)</b> Which fundamental data structure possesses exactly <b>two formal properties</b>? State the structure and define both properties.<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;<b>Data Structure:</b> ........................................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;1. ....................................................................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;2. ....................................................................................................................................................................<br/>"
                      "<b>(b)</b> Which tree data structure possesses exactly <b>three formal properties</b>? State the structure and list the properties.<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;<b>Data Structure:</b> ........................................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;Properties: .......................................................................................................................................................",
                      style_body),
            Paragraph("<b>[3 Marks]</b>", style_body_bold)
        ],
        # 7.2
        [
            Paragraph("<b>7.2 Hash Function Theoretical Properties & Realistic Limitation:</b><br/>"
                      "State the <b>3 ideal properties</b> of a theoretical hash function:<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;1. ....................................................................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;2. ....................................................................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;3. ....................................................................................................................................................................<br/>"
                      "Which of these 3 properties is <b>impossible to achieve in the physical real world</b>, and explain the <b>two fundamental reasons</b> why?<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Impossible Property:</b> ............................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Reason 1:</b> .................................................................................................................................................<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Reason 2:</b> .................................................................................................................................................",
                      style_body),
            Paragraph("<b>[2 Marks]</b>", style_body_bold)
        ],
        # 7.3
        [
            Paragraph("<b>7.3 Graph Memory Waste Percentage (Sparse Graph Analysis):</b><br/>"
                      "A directed graph has <b>|V| = 7 vertices</b> and <b>|E| = 12 edges</b>.<br/>"
                      "&bull; What is the total number of cells in its <b>Adjacency Matrix</b>? .....................................................................<br/>"
                      "&bull; What <b>percentage of matrix cells</b> contain 1 (active edges)? .......................................................................<br/>"
                      "&bull; What <b>percentage of matrix cells</b> are 0 (wasted unused space)? ....................................................................<br/>"
                      "&bull; How many cells are required if represented as an <b>Adjacency List</b> (|V| + |E|)? ...........................................",
                      style_body),
            Paragraph("<b>[2 Marks]</b>", style_body_bold)
        ],
        # 7.4
        [
            Paragraph("<b>7.4 Complete Graph Edge Calculation:</b><br/>"
                      "A complete undirected graph K<sub>16</sub> has <b>|V| = 16 vertices</b>. "
                      "How many edges are in this graph? <i>(Must answer as an exact integer, do NOT leave as formula).</i><br/>"
                      "<b>Calculation & Answer:</b> .........................................................................................................................................",
                      style_body),
            Paragraph("<b>[1 Mark]</b>", style_body_bold)
        ],
        # 7.5
        [
            Paragraph("<b>7.5 Binary Tree Node Bounds:</b><br/>"
                      "A Complete Binary Tree has height <b>h = 16</b> (assuming Root is at height 0).<br/>"
                      "&bull; <b>Minimum number of nodes:</b> ............................................................ <i>(Must be exact integer, not 2<sup>16</sup>)</i><br/>"
                      "&bull; <b>Maximum number of nodes:</b> ............................................................ <i>(Must be exact integer, not 2<sup>17</sup> - 1)</i>",
                      style_body),
            Paragraph("<b>[1 Mark]</b>", style_body_bold)
        ],
        # 7.6
        [
            Paragraph("<b>7.6 Binary Heap 1-Based Array Index Formulas:</b><br/>"
                      "For a node located at index <b>i</b> in a 1-based array implementation of a Binary Heap, state the exact formula for:<br/>"
                      "&bull; <b>Left Child Index:</b> .................................... &nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Right Child Index:</b> .................................... &nbsp;&nbsp;&nbsp;&nbsp;&bull; <b>Parent Index:</b> ....................................",
                      style_body),
            Paragraph("<b>[1 Mark]</b>", style_body_bold)
        ]
    ]

    t_q7 = Table(q7_items, colWidths=[460, 63])
    t_q7.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,1), (-1,1), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,2), (-1,2), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,3), (-1,3), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0,4), (-1,4), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(t_q7)
    story.append(Spacer(1, 15))

    story.append(Paragraph(
        "<b>*** END OF EXAMINATION PAPER — WISHING YOU ALL THE BEST! ***</b>",
        ParagraphStyle('EndNotice', fontName='Tahoma-Bold', fontSize=10, alignment=1, textColor=colors.HexColor('#1e3a8a'))
    ))

    # Build document
    doc.build(story)
    print(f"Successfully generated: {OUTPUT_PDF}")

if __name__ == '__main__':
    build_pdf()
