"""
SVG & Visual Exam Components Generator
Designed for Assoc. Prof. Dr. Pradit Pitaksatheinkul's Data Structures & Algorithms Exams
Matches exact PDF worksheet layouts, classroom whiteboard diagrams, and textbook figures.
"""

import math

def render_svg_graph_lecture10(width=540, height=340):
    """
    Renders the classic 7-vertex DAG & Shortest Path graph from Lecture 10 (p.5) & Lecture 11 (p.2).
    Vertices: v1..v7, 12 directed edges.
    Layout matches Topological_sort_p5_img1.jpeg:
      v1(150, 50), v2(390, 50)
      v3(50, 170), v4(270, 170), v5(490, 170)
      v6(150, 290), v7(390, 290)
    """
    coords = {
        1: (150, 50), 2: (390, 50),
        3: (50, 170), 4: (270, 170), 5: (490, 170),
        6: (150, 290), 7: (390, 290)
    }
    edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 4), (2, 5),
        (3, 6),
        (4, 3), (4, 6), (4, 7),
        (5, 4), (5, 7),
        (7, 6)
    ]
    R = 20
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <defs>',
        '    <marker id="arrow-l10" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '    </marker>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        '  <text x="270" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#334155">Directed Graph G = (V, E) [Lecture 10 &amp; 11]: |V|=7, |E|=12</text>'
    ]
    
    # Draw edges
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist > 0:
            ux = dx / dist
            uy = dy / dist
            sx = x1 + ux * R
            sy = y1 + uy * R
            ex = x2 - ux * (R + 4)
            ey = y2 - uy * (R + 4)
            lines.append(f'  <line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-l10)"/>')
            
    # Draw vertices
    for u, (x, y) in coords.items():
        lines.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>')
        lines.append(f'  <text x="{x}" y="{y+5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v<tspan font-size="11" dy="3">{u}</tspan></text>')
        
    lines.append('</svg>')
    return '\n'.join(lines)


def render_svg_graph_assignment4(width=540, height=340):
    """
    Renders Assignment 4 graph (A..G, 7 vertices) matching Assignment_4_Solved_Complete_StartA.jpg.
    A(60, 170), B(190, 60), C(250, 170), D(190, 280), G(390, 60), E(470, 170), F(390, 280)
    """
    coords = {
        'A': (60, 170),
        'B': (190, 60),
        'C': (250, 170),
        'D': (190, 280),
        'G': (390, 60),
        'E': (470, 170),
        'F': (390, 280)
    }
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'C'), ('B', 'E'), ('B', 'G'),
        ('C', 'D'), ('C', 'E'),
        ('D', 'A'), ('D', 'F'),
        ('E', 'D'), ('E', 'F'),
        ('G', 'E')
    ]
    R = 20
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <defs>',
        '    <marker id="arrow-a4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '    </marker>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        '  <text x="270" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#334155">Directed Graph G = (V, E) [Assignment 4 Worksheet]: |V|=7 (A..G)</text>'
    ]
    
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist > 0:
            ux = dx / dist
            uy = dy / dist
            sx = x1 + ux * R
            sy = y1 + uy * R
            ex = x2 - ux * (R + 4)
            ey = y2 - uy * (R + 4)
            lines.append(f'  <line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-a4)"/>')
            
    for u, (x, y) in coords.items():
        lines.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>')
        lines.append(f'  <text x="{x}" y="{y+5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="#0f172a">{u}</text>')
        
    lines.append('</svg>')
    return '\n'.join(lines)


def render_svg_graph_exam2026_topo(width=540, height=340):
    """
    Renders 2026 Final Exam Topological Sort DAG (Question 5):
    Canonical 7-vertex DAG from Lecture 10 (p.5) and classroom whiteboard.
    Vertices: v1..v7, 12 directed edges.
    Unique Source: v1 (in-degree=0), Unique Sink: v6 (out-degree=0).
    """
    coords = {
        1: (150, 60), 2: (390, 60),
        3: (60, 180), 4: (270, 180), 5: (480, 180),
        6: (150, 300), 7: (390, 300)
    }
    edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 4), (2, 5),
        (3, 6),
        (4, 3), (4, 6), (4, 7),
        (5, 4), (5, 7),
        (7, 6)
    ]
    R = 20
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <defs>',
        '    <marker id="arrow-topo26" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '    </marker>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        '  <text x="270" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#334155">Directed Acyclic Graph (DAG) [Lecture 10 &amp; Exam 2026 Q5]: |V|=7, |E|=12</text>'
    ]
    
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist > 0:
            ux = dx / dist
            uy = dy / dist
            sx = x1 + ux * R
            sy = y1 + uy * R
            ex = x2 - ux * (R + 4)
            ey = y2 - uy * (R + 4)
            lines.append(f'  <line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-topo26)"/>')
                
    for u, (x, y) in coords.items():
        is_source = (u == 1)
        is_sink = (u == 6)
        if is_source:
            fill_col = "#dbeafe"
            stroke_col = "#1d4ed8"
        elif is_sink:
            fill_col = "#fef2f2"
            stroke_col = "#dc2626"
        else:
            fill_col = "#f8fafc"
            stroke_col = "#1e293b"
        lines.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="{fill_col}" stroke="{stroke_col}" stroke-width="{3 if (is_source or is_sink) else 2.5}"/>')
        lines.append(f'  <text x="{x}" y="{y+5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v{u}</text>')
        if is_source:
            lines.append(f'  <text x="{x}" y="{y-26}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-weight="bold" fill="#1d4ed8">SOURCE</text>')
        elif is_sink:
            lines.append(f'  <text x="{x}" y="{y+32}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-weight="bold" fill="#dc2626">SINK</text>')
        
    lines.append('</svg>')
    return '\n'.join(lines)


def render_svg_graph_exam2026_sp(width=540, height=340):
    """
    Renders 2026 Final Exam Shortest Path Graph (Question 6):
    Matches Assignment 4 / For Example Graph canonical 7-vertex directed graph.
    Vertices: v1..v7, 12 directed edges.
    Edges:
      1 -> 2, 4
      2 -> 4, 5
      3 -> 1, 6
      4 -> 3, 5, 6, 7
      5 -> 7
      6 -> empty
      7 -> 6
    Source Vertex = 1
    """
    coords = {
        1: (150, 60), 2: (390, 60),
        3: (60, 180), 4: (270, 180), 5: (480, 180),
        6: (150, 300), 7: (390, 300)
    }
    edges = [
        (1, 2), (1, 4),
        (2, 4), (2, 5),
        (3, 1), (3, 6),
        (4, 3), (4, 5), (4, 6), (4, 7),
        (5, 7),
        (7, 6)
    ]
    R = 20
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <defs>',
        '    <marker id="arrow-sp26" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '    </marker>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        '  <text x="270" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#334155">Directed Graph G = (V, E) [Exam 2026 Question 6]: Source Vertex = 1, |E|=12</text>'
    ]
    
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist > 0:
            ux = dx / dist
            uy = dy / dist
            if u == 3 and v == 1:
                # curved upward left
                lines.append(f'  <path d="M {x1+10} {y1-16} Q 95 105 {x2-16} {y2+10}" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>')
            else:
                sx = x1 + ux * R
                sy = y1 + uy * R
                ex = x2 - ux * (R + 4)
                ey = y2 - uy * (R + 4)
                lines.append(f'  <line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow-sp26)"/>')
                
    for u, (x, y) in coords.items():
        is_source = (u == 1)
        fill_col = "#dbeafe" if is_source else "#f8fafc"
        stroke_col = "#2563eb" if is_source else "#1e293b"
        lines.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="{fill_col}" stroke="{stroke_col}" stroke-width="{3 if is_source else 2.5}"/>')
        lines.append(f'  <text x="{x}" y="{y+5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">v{u}</text>')
        if is_source:
            lines.append(f'  <text x="{x}" y="{y-26}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-weight="bold" fill="#2563eb">SOURCE</text>')
            
    lines.append('</svg>')
    return '\n'.join(lines)


def render_svg_adj_list(adj_dict, title="Adjacency List (Linked Memory Architecture)", width=560, height=360):
    """
    Renders an official Adjacency List diagram identical to Dr. Pradit's worksheets:
    - Header array table on the left (index 1..7 or A..G)
    - Each node is [ Dest | • ] (two compartments)
    - Pointers connect horizontally
    - Ground symbol ⏚ at end of list
    - Empty list points straight to ground ⏚!
    """
    keys = list(adj_dict.keys())
    num_rows = len(keys)
    row_height = 42
    start_y = 50
    header_x = 35
    header_w = 60
    header_h = 32
    node_w = 56
    node_h = 30
    
    total_height = max(height, start_y + num_rows * row_height + 20)
    
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {total_height}" width="100%" height="{total_height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <defs>',
        '    <marker id="arrow-adj" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>',
        '    </marker>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        f'  <text x="{width//2}" y="26" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13.5" font-weight="bold" fill="#1e293b">{title}</text>'
    ]
    
    for row_idx, key in enumerate(keys):
        y = start_y + row_idx * row_height
        cy = y + header_h // 2
        
        # Left label outside
        lines.append(f'  <text x="{header_x - 12}" y="{cy + 5}" text-anchor="end" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#475569">{key}</text>')
        
        # Header Box: [ Label (40px) | Ptr (20px) ]
        lines.append(f'  <rect x="{header_x}" y="{y}" width="{header_w}" height="{header_h}" fill="#f1f5f9" stroke="#334155" stroke-width="1.8"/>')
        lines.append(f'  <line x1="{header_x + 40}" y1="{y}" x2="{header_x + 40}" y2="{y + header_h}" stroke="#334155" stroke-width="1.2"/>')
        lines.append(f'  <text x="{header_x + 20}" y="{cy + 5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#1e293b">{key}</text>')
        lines.append(f'  <circle cx="{header_x + 50}" cy="{cy}" r="3" fill="#0284c7"/>')
        
        neighbors = adj_dict[key]
        curr_x = header_x + header_w
        
        if not neighbors:
            # Points directly down to ground
            gx = curr_x + 22
            lines.append(f'  <path d="M {header_x + 50} {cy} L {gx} {cy} L {gx} {cy + 12}" fill="none" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>')
            # Ground symbol
            lines.append(f'  <line x1="{gx - 9}" y1="{cy + 14}" x2="{gx + 9}" y2="{cy + 14}" stroke="#334155" stroke-width="2"/>')
            lines.append(f'  <line x1="{gx - 6}" y1="{cy + 17}" x2="{gx + 6}" y2="{cy + 17}" stroke="#334155" stroke-width="1.8"/>')
            lines.append(f'  <line x1="{gx - 3}" y1="{cy + 20}" x2="{gx + 3}" y2="{cy + 20}" stroke="#334155" stroke-width="1.5"/>')
        else:
            # Arrow from header to first node
            first_node_x = curr_x + 20
            lines.append(f'  <line x1="{header_x + 50}" y1="{cy}" x2="{first_node_x}" y2="{cy}" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>')
            curr_x = first_node_x
            
            for n_idx, dest in enumerate(neighbors):
                ny = cy - node_h // 2
                # Node box: [ Dest (36px) | Next* (20px) ]
                lines.append(f'  <rect x="{curr_x}" y="{ny}" width="{node_w}" height="{node_h}" fill="#ffffff" stroke="#334155" stroke-width="1.6" rx="2"/>')
                lines.append(f'  <line x1="{curr_x + 36}" y1="{ny}" x2="{curr_x + 36}" y2="{ny + node_h}" stroke="#334155" stroke-width="1.2"/>')
                lines.append(f'  <text x="{curr_x + 18}" y="{cy + 5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{dest}</text>')
                lines.append(f'  <circle cx="{curr_x + 46}" cy="{cy}" r="2.8" fill="#0284c7"/>')
                
                next_x = curr_x + node_w + 20
                if n_idx < len(neighbors) - 1:
                    # Arrow to next node
                    lines.append(f'  <line x1="{curr_x + 46}" y1="{cy}" x2="{next_x}" y2="{cy}" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow-adj)"/>')
                    curr_x = next_x
                else:
                    # Ground symbol at end
                    gx = curr_x + node_w + 14
                    lines.append(f'  <line x1="{curr_x + 46}" y1="{cy}" x2="{gx}" y2="{cy}" stroke="#334155" stroke-width="1.5"/>')
                    lines.append(f'  <line x1="{gx}" y1="{cy}" x2="{gx}" y2="{cy + 8}" stroke="#334155" stroke-width="1.5"/>')
                    lines.append(f'  <line x1="{gx - 9}" y1="{cy + 9}" x2="{gx + 9}" y2="{cy + 9}" stroke="#334155" stroke-width="2"/>')
                    lines.append(f'  <line x1="{gx - 6}" y1="{cy + 12}" x2="{gx + 6}" y2="{cy + 12}" stroke="#334155" stroke-width="1.8"/>')
                    lines.append(f'  <line x1="{gx - 3}" y1="{cy + 15}" x2="{gx + 3}" y2="{cy + 15}" stroke="#334155" stroke-width="1.5"/>')
                    
    lines.append('</svg>')
    return '\n'.join(lines)


def render_svg_circular_queue(slots, front_idx, back_idx, current_size, max_size=7, title="Circular Queue Buffer (7 Slots)", width=480, height=270):
    """
    Renders an official Queue visualization box matching Dr. Pradit's worksheets (Topological sort p.6, For Example Graph p.3-4):
    Slots 0..6 (or 6..0), with front and back pointer arrows and status counters.
    """
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <defs>',
        '    <marker id="arrow-front" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#dc2626"/>',
        '    </marker>',
        '    <marker id="arrow-back" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#16a34a"/>',
        '    </marker>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        f'  <text x="{width//2}" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">{title}</text>'
    ]
    
    # Draw horizontal queue array slots
    slot_w = 48
    slot_h = 42
    start_x = 55
    y_box = 65
    
    for i in range(max_size):
        sx = start_x + i * slot_w
        val = slots[i] if i < len(slots) and slots[i] is not None and slots[i] != '' else '-'
        is_empty = (val == '-')
        
        # Slot box
        lines.append(f'  <rect x="{sx}" y="{y_box}" width="{slot_w}" height="{slot_h}" fill="{"#f8fafc" if is_empty else "#eff6ff"}" stroke="#475569" stroke-width="1.8"/>')
        # Index header
        lines.append(f'  <text x="{sx + slot_w//2}" y="{y_box - 8}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#64748b">[{i}]</text>')
        # Value
        lines.append(f'  <text x="{sx + slot_w//2}" y="{y_box + 26}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="15" font-weight="bold" fill="{"#94a3b8" if is_empty else "#1e3a8a"}">{val}</text>')
        
        # Front pointer arrow (from bottom or top)
        if i == front_idx:
            lines.append(f'  <line x1="{sx + slot_w//2}" y1="{y_box + slot_h + 32}" x2="{sx + slot_w//2}" y2="{y_box + slot_h + 3}" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-front)"/>')
            lines.append(f'  <text x="{sx + slot_w//2}" y="{y_box + slot_h + 46}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="11" font-weight="bold" fill="#dc2626">front={front_idx}</text>')
            
        # Back pointer arrow
        if i == back_idx:
            lines.append(f'  <line x1="{sx + slot_w//2}" y1="{y_box + slot_h + 68}" x2="{sx + slot_w//2}" y2="{y_box + slot_h + 3}" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow-back)"/>')
            lines.append(f'  <text x="{sx + slot_w//2}" y="{y_box + slot_h + 82}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="11" font-weight="bold" fill="#16a34a">back={back_idx}</text>')

    # Summary Info Card on the right
    card_x = start_x + max_size * slot_w + 25
    lines.append(f'  <rect x="{card_x}" y="50" width="160" height="185" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" rx="6"/>')
    lines.append(f'  <text x="{card_x + 12}" y="72" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">สถานะพอยน์เตอร์จบลูป:</text>')
    lines.append(f'  <text x="{card_x + 12}" y="96" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#dc2626">front</tspan> = {front_idx}</text>')
    lines.append(f'  <text x="{card_x + 12}" y="118" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#16a34a">back</tspan> = {back_idx}</text>')
    lines.append(f'  <text x="{card_x + 12}" y="140" font-family="Segoe UI, Tahoma, sans-serif" font-size="12" fill="#334155">• <tspan font-weight="bold" fill="#2563eb">currentSize</tspan> = {current_size}</text>')
    lines.append(f'  <line x1="{card_x + 10}" y1="152" x2="{card_x + 150}" y2="152" stroke="#e2e8f0" stroke-width="1"/>')
    lines.append(f'  <text x="{card_x + 12}" y="172" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" fill="#64748b">สูตร Enqueue:</text>')
    lines.append(f'  <text x="{card_x + 12}" y="188" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-family="Consolas" fill="#0f172a">back = (back+1)%7</text>')
    lines.append(f'  <text x="{card_x + 12}" y="208" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" fill="#64748b">สูตร Dequeue:</text>')
    lines.append(f'  <text x="{card_x + 12}" y="224" font-family="Segoe UI, Tahoma, sans-serif" font-size="10.5" font-family="Consolas" fill="#0f172a">front = (front+1)%7</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


def render_svg_minheap_tree(heap_array, title="Binary Min-Heap Tree Representation", width=540, height=290):
    """
    Renders a complete Binary Min-Heap tree diagram from a 1-based array:
    heap_array: [unused, root, c1, c2, ...]
    Calculates parent-child branches, node circles, and array index badges.
    """
    # Level coordinates
    # Level 0 (root): index 1
    # Level 1: indices 2, 3
    # Level 2: indices 4, 5, 6, 7
    # Level 3: indices 8, 9, 10, 11, 12...
    positions = {
        1: (270, 50),
        2: (140, 110), 3: (400, 110),
        4: (75, 175),  5: (205, 175), 6: (335, 175), 7: (465, 175),
        8: (45, 240),  9: (105, 240), 10: (175, 240), 11: (235, 240),
        12: (305, 240), 13: (365, 240), 14: (435, 240), 15: (495, 240)
    }
    
    R = 16
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05);">',
        '  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>',
        f'  <text x="{width//2}" y="24" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#1e293b">{title}</text>'
    ]
    
    n = len(heap_array) - 1
    # Draw branches first
    for i in range(1, n + 1):
        if i not in positions:
            continue
        px, py = positions[i]
        left = 2 * i
        right = 2 * i + 1
        if left <= n and left in positions:
            cx, cy = positions[left]
            lines.append(f'  <line x1="{px}" y1="{py+R}" x2="{cx}" y2="{cy-R}" stroke="#475569" stroke-width="1.6"/>')
        if right <= n and right in positions:
            cx, cy = positions[right]
            lines.append(f'  <line x1="{px}" y1="{py+R}" x2="{cx}" y2="{cy-R}" stroke="#475569" stroke-width="1.6"/>')
            
    # Draw nodes
    for i in range(1, n + 1):
        if i not in positions:
            continue
        x, y = positions[i]
        val = heap_array[i]
        lines.append(f'  <circle cx="{x}" cy="{y}" r="{R}" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>')
        lines.append(f'  <text x="{x}" y="{y+5}" text-anchor="middle" font-family="Segoe UI, Tahoma, sans-serif" font-size="13" font-weight="bold" fill="#14532d">{val}</text>')
        # Small index badge
        lines.append(f'  <text x="{x+18}" y="{y-8}" text-anchor="start" font-family="Segoe UI, Tahoma, sans-serif" font-size="10" font-weight="bold" fill="#64748b">[{i}]</text>')
        
    lines.append('</svg>')
    return '\n'.join(lines)


def render_html_double_hashing_table(table_data, table_size=19, is_blank=False, title="Hash Table (TableSize = 19, Open Addressing with Double Hashing)"):
    """
    Renders modern Python 1D Hash Table matching Dr. Pradit's Chapter 7 curriculum (slides 17 & 20):
    - Row 1: Slot / Index (0..18)
    - Row 2: Stored Key (Python list item or empty blank)
    - Row 3 (if solved): Collisions & Probes
    (Completely eliminates obsolete C++ 'element' and 'info' fields)
    """
    html = [
        '<div style="overflow-x:auto; margin:15px 0;">',
        f'  <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:6px;">📝 {title}</div>',
        '  <table style="width:100%; border-collapse:collapse; text-align:center; font-family:\'Segoe UI\', Tahoma, sans-serif; font-size:12.5px; border:2px solid #334155;">',
        '    <thead>',
        '      <tr style="background:#1e293b; color:#ffffff;">',
        '        <th style="padding:6px; border:1px solid #475569; width:95px;">Slot / Index</th>'
    ]
    
    # Half 1: 0..9
    for i in range(10):
        html.append(f'        <th style="padding:6px; border:1px solid #475569; font-weight:bold;">[{i}]</th>')
    html.append('      </tr>')
    html.append('    </thead>')
    html.append('    <tbody>')
    
    # Row Stored Key 0..9
    html.append('      <tr style="background:#ffffff;">')
    html.append('        <td style="padding:8px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Stored Key</td>')
    for i in range(10):
        if is_blank:
            html.append('        <td style="padding:8px 4px; border:1px solid #cbd5e1; height:34px;">&nbsp;</td>')
        else:
            val = table_data.get(i, {}).get('key', table_data.get(i, {}).get('element', '-'))
            val_style = 'font-weight:bold; color:#1e40af; font-size:13.5px;' if val != '-' else 'color:#cbd5e1;'
            html.append(f'        <td style="padding:8px 4px; border:1px solid #cbd5e1; {val_style}">{val}</td>')
    html.append('      </tr>')
    
    # If not blank, show collision tracing row
    if not is_blank:
        html.append('      <tr style="background:#f8fafc;">')
        html.append('        <td style="padding:5px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a; font-size:11px;">Collisions</td>')
        for i in range(10):
            collision = table_data.get(i, {}).get('collision', '')
            probes = table_data.get(i, {}).get('probes', '')
            if collision != '' and collision != '0':
                badge = f'<span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน {collision} ครั้ง</span>'
                if probes and probes != '-':
                    badge += f'<br/><span style="font-size:9.5px; color:#64748b;">(ช่อง {probes})</span>'
            elif collision == '0':
                badge = '<span style="background:#dcfce7; color:#15803d; padding:1px 4px; border-radius:3px; font-size:10.5px;">ชน 0</span>'
            else:
                badge = '<span style="color:#cbd5e1;">-</span>'
            html.append(f'        <td style="padding:5px 4px; border:1px solid #cbd5e1;">{badge}</td>')
        html.append('      </tr>')
    
    # Half 2: 10..18
    html.append('      <tr style="background:#1e293b; color:#ffffff;">')
    html.append('        <th style="padding:6px; border:1px solid #475569;">Slot / Index</th>')
    for i in range(10, 19):
        html.append(f'        <th style="padding:6px; border:1px solid #475569; font-weight:bold;">[{i}]</th>')
    html.append('        <th style="padding:6px; border:1px solid #475569; background:#475569;">-</th>')
    html.append('      </tr>')
    
    # Row Stored Key 10..18
    html.append('      <tr style="background:#ffffff;">')
    html.append('        <td style="padding:8px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Stored Key</td>')
    for i in range(10, 19):
        if is_blank:
            html.append('        <td style="padding:8px 4px; border:1px solid #cbd5e1; height:34px;">&nbsp;</td>')
        else:
            val = table_data.get(i, {}).get('key', table_data.get(i, {}).get('element', '-'))
            val_style = 'font-weight:bold; color:#1e40af; font-size:13.5px;' if val != '-' else 'color:#cbd5e1;'
            html.append(f'        <td style="padding:8px 4px; border:1px solid #cbd5e1; {val_style}">{val}</td>')
    html.append('        <td style="padding:8px 4px; border:1px solid #cbd5e1; background:#f1f5f9;">-</td>')
    html.append('      </tr>')
    
    # If not blank, show collision tracing row 10..18
    if not is_blank:
        html.append('      <tr style="background:#f8fafc;">')
        html.append('        <td style="padding:5px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a; font-size:11px;">Collisions</td>')
        for i in range(10, 19):
            collision = table_data.get(i, {}).get('collision', '')
            probes = table_data.get(i, {}).get('probes', '')
            if collision != '' and collision != '0':
                badge = f'<span style="background:#fee2e2; color:#dc2626; padding:1px 4px; border-radius:3px; font-size:10.5px; font-weight:bold;">ชน {collision} ครั้ง</span>'
                if probes and probes != '-':
                    badge += f'<br/><span style="font-size:9.5px; color:#64748b;">(ช่อง {probes})</span>'
            elif collision == '0':
                badge = '<span style="background:#dcfce7; color:#15803d; padding:1px 4px; border-radius:3px; font-size:10.5px;">ชน 0</span>'
            else:
                badge = '<span style="color:#cbd5e1;">-</span>'
            html.append(f'        <td style="padding:5px 4px; border:1px solid #cbd5e1;">{badge}</td>')
        html.append('        <td style="padding:5px 4px; border:1px solid #cbd5e1; background:#f1f5f9;">-</td>')
        html.append('      </tr>')
    
    html.append('    </tbody>')
    html.append('  </table>')
    html.append('</div>')
    return '\n'.join(html)


def render_html_heap_vertical_arrays(arrays_data, labels=None):
    """
    Renders 4 vertical arrays side-by-side matching Dr. Pradit's exam worksheet (exam2564_p1_img1.png):
    insert, deleteMin1, deleteMin2, deleteMin3 (12 slots each)
    """
    if labels is None:
        labels = ["1. Insert 12 Keys", "2. deleteMin() 1", "3. Insert key 3", "4. deleteMin() 2"]
        
    num_cols = len(arrays_data)
    html = [
        '<div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; margin:16px 0;">'
    ]
    
    for c_idx, arr in enumerate(arrays_data):
        label = labels[c_idx]
        html.append('  <div style="flex:1; min-width:140px; max-width:200px; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,0.05);">')
        html.append(f'    <div style="background:#1e293b; color:#ffffff; padding:8px; font-size:12px; font-weight:bold; text-align:center;">{label}</div>')
        html.append('    <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12px;">')
        html.append('      <tr style="background:#f1f5f9; color:#64748b; font-weight:bold;"><th style="padding:4px; border-bottom:1px solid #cbd5e1; width:45px;">Index</th><th style="padding:4px; border-bottom:1px solid #cbd5e1;">Value</th></tr>')
        
        for idx in range(13): # 0 to 12
            val = arr[idx] if idx < len(arr) and arr[idx] is not None else '-'
            is_unused = (idx == 0)
            row_bg = '#fafafa' if is_unused else ('#eff6ff' if idx % 2 == 1 else '#ffffff')
            val_display = '<span style="color:#94a3b8; font-style:italic;">unused</span>' if is_unused else (f'<strong style="color:#1e40af;">{val}</strong>' if val != '-' else '<span style="color:#cbd5e1;">-</span>')
            html.append(f'      <tr style="background:{row_bg};"><td style="padding:4px 6px; border:1px solid #e2e8f0; font-family:Consolas, monospace; font-weight:600; color:#475569;">[{idx}]</td><td style="padding:4px 6px; border:1px solid #e2e8f0;">{val_display}</td></tr>')
            
        html.append('    </table>')
        html.append('  </div>')
        
    html.append('</div>')
    return '\n'.join(html)


def render_html_shortest_path_table(table_rows, enqueue_seq=None, dequeue_seq=None, queue_slots=None, final_pointers=None, title="Shortest Path Processing Table (อะเรย์สำหรับประมวลผล Shortest Path)", source_vertex=1, is_blank=False):
    """
    Renders the official Shortest Path BFS processing table matching Dr. Pradit's worksheets:
    - Columns: Vertex (v) | Known | Dist (Dv) | Path (Pv)
    - Row: Enqueue Sequence
    - Row: Dequeue Sequence
    - Dual Queue Buffers: Horizontal [0]..[6] AND Vertical q [6]..[0]
    - Fill-ins / Answers for front, back, currentSize, and shortest path length/order to v5 & v7.
    """
    if queue_slots is None:
        queue_slots = [''] * 7
    if final_pointers is None:
        final_pointers = {'front': 0, 'back': 6, 'currentSize': 0}
        
    html = [
        '<div style="margin:16px 0; font-family:\'Segoe UI\', Tahoma, sans-serif;">',
        f'  <div style="font-size:14px; font-weight:bold; color:#1e293b; margin-bottom:8px;">📝 {title} (Source Vertex = {source_vertex})</div>',
        '  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">',
        '    <div style="flex:2; min-width:320px;">',
        '      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:13px; border:2px solid #334155;">',
        '        <thead>',
        '          <tr style="background:#1e293b; color:#ffffff;">',
        '            <th style="padding:8px 6px; border:1px solid #475569; width:75px;">Vertex (v)</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569; width:85px;">Known</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">Dist (Dv)</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">Path (Pv)</th>',
        '          </tr>',
        '        </thead>',
        '        <tbody>'
    ]
    
    for row in table_rows:
        v = row['vertex']
        known = row.get('known', 'F') if not is_blank else '&nbsp;'
        dist = row.get('dist', '&infin;') if not is_blank else '&nbsp;'
        path = row.get('path', '0') if not is_blank else '&nbsp;'
        bg = '#eff6ff' if str(v) == str(source_vertex) else '#ffffff'
        
        html.append(f'          <tr style="background:{bg};">')
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; color:#0f172a;">v{v}</td>')
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1;">{known}</td>')
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1;">{dist}</td>')
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1;">{path}</td>')
        html.append('          </tr>')
        
    # Enqueue & Dequeue sequence rows
    eq_val = enqueue_seq if (enqueue_seq and not is_blank) else ('............................................................' if is_blank else '1, 2, 4, 5, 3, 6, 7')
    dq_val = dequeue_seq if (dequeue_seq and not is_blank) else ('............................................................' if is_blank else '1, 2, 4, 5, 3, 6, 7')
    
    html.append('          <tr style="background:#e0e7ff; font-weight:bold;">')
    html.append('            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#1e1b4b; text-align:left;" colspan="2">Enqueue Sequence:</td>')
    html.append(f'            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#1e1b4b;" colspan="2">{eq_val}</td>')
    html.append('          </tr>')
    html.append('          <tr style="background:#fee2e2; font-weight:bold;">')
    html.append('            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#991b1b; text-align:left;" colspan="2">Dequeue Sequence:</td>')
    html.append(f'            <td style="padding:8px 6px; border:1px solid #cbd5e1; color:#991b1b;" colspan="2">{dq_val}</td>')
    html.append('          </tr>')
    
    html.append('        </tbody>')
    html.append('      </table>')
    html.append('    </div>')
    
    # Side Vertical Queue Stack: q [6] down to [0]
    html.append('    <div style="flex:1; min-width:170px; max-width:220px;">')
    html.append('      <div style="font-size:13px; font-weight:bold; color:#1e293b; margin-bottom:6px; text-align:center;">📦 Vertical Queue (q)</div>')
    html.append('      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #475569;">')
    html.append('        <thead><tr style="background:#334155; color:#ffffff;"><th style="padding:6px; border:1px solid #475569; width:45px;">Index</th><th style="padding:6px; border:1px solid #475569;">Vertex</th></tr></thead>')
    html.append('        <tbody>')
    
    for idx in range(6, -1, -1):
        val = queue_slots[idx] if idx < len(queue_slots) and queue_slots[idx] is not None and not is_blank else '&nbsp;'
        val_styled = f'<strong style="color:#1e40af;">{val}</strong>' if val != '&nbsp;' and val != '-' else ('<span style="color:#94a3b8;">-</span>' if not is_blank else '&nbsp;')
        html.append(f'          <tr style="background:{"#f8fafc" if idx % 2 == 1 else "#ffffff"};">')
        html.append(f'            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[{idx}]</td>')
        html.append(f'            <td style="padding:6px 4px; border:1px solid #cbd5e1;">{val_styled}</td>')
        html.append('          </tr>')
        
    html.append('        </tbody>')
    html.append('      </table>')
    html.append('    </div>')
    html.append('  </div>')
    
    # Horizontal Circular Queue buffer & Pointer values
    html.append('  <div style="margin-top:14px; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:8px; padding:12px;">')
    html.append('    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">🔄 Horizontal Circular Queue Buffer &amp; Final Pointer Status:</div>')
    html.append('    <table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:10px;">')
    html.append('      <tr style="background:#334155; color:#ffffff; font-size:12px;"><th style="padding:5px;">Index</th>' + ''.join([f'<th style="padding:5px; border:1px solid #475569;">[{i}]</th>' for i in range(7)]) + '</tr>')
    
    row_cells = []
    for i in range(7):
        val = queue_slots[i] if i < len(queue_slots) and queue_slots[i] is not None and not is_blank else '&nbsp;'
        val_dsp = f'<strong style="color:#1e40af;">{val}</strong>' if val != '&nbsp;' and val != '-' else ('<span style="color:#94a3b8;">-</span>' if not is_blank else '&nbsp;')
        row_cells.append(f'<td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">{val_dsp}</td>')
    html.append('      <tr><td style="padding:6px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; font-size:12px;">q Value</td>' + ''.join(row_cells) + '</tr>')
    html.append('    </table>')
    
    front_val = final_pointers.get('front', 0) if not is_blank else '............'
    back_val = final_pointers.get('back', 6) if not is_blank else '............'
    csize_val = final_pointers.get('currentSize', 0) if not is_blank else '............'
    
    html.append('    <div style="display:flex; justify-content:space-around; font-size:12.5px; color:#1e293b; background:#ffffff; padding:8px; border-radius:6px; border:1px solid #e2e8f0; flex-wrap:wrap; gap:10px;">')
    html.append(f'      <div>• <strong>front</strong> = <span style="color:#dc2626; font-weight:bold;">{front_val}</span> (สูตร: <code>(front+1)%7</code>)</div>')
    html.append(f'      <div>• <strong>back</strong> = <span style="color:#16a34a; font-weight:bold;">{back_val}</span> (สูตร: <code>(back+1)%7</code>)</div>')
    html.append(f'      <div>• <strong>currentSize</strong> = <span style="color:#2563eb; font-weight:bold;">{csize_val}</span> (Empty)</div>')
    html.append('    </div>')
    
    # Path questions / answers
    html.append('    <div style="margin-top:10px; font-size:12.5px; background:#eff6ff; padding:10px; border-radius:6px; border:1px solid #bfdbfe; line-height:1.7;">')
    if is_blank:
        html.append('      <div><strong>6.1 Shortest Path จาก 1 ไปยัง 5:</strong> ความยาวเส้นทาง = .............. edges, ลำดับคือ ............................................................</div>')
        html.append('      <div><strong>6.2 Shortest Path จาก 1 ไปยัง 7:</strong> ความยาวเส้นทาง = .............. edges, ลำดับคือ ............................................................</div>')
        html.append('      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ความยาวเส้นทางนับจำนวน Edge (ไม่ใช่ Node) และลำดับต้องคั่นด้วยเครื่องหมายจุลภาค <code>,</code> ห้ามใส่ลูกศร <code>-&gt;</code> เด็ดขาด!</div>')
    else:
        html.append('      <div><strong>6.1 Shortest Path จาก 1 ไปยัง 5:</strong> ความยาวเส้นทาง = <strong style="color:#1d4ed8;">2 edges</strong>, ลำดับคือ <strong style="color:#1d4ed8;">1, 2, 5</strong> (หรือ <strong style="color:#1d4ed8;">1, 4, 5</strong>)</div>')
        html.append('      <div><strong>6.2 Shortest Path จาก 1 ไปยัง 7:</strong> ความยาวเส้นทาง = <strong style="color:#1d4ed8;">2 edges</strong>, ลำดับคือ <strong style="color:#1d4ed8;">1, 4, 7</strong></div>')
        html.append('      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ความยาวเส้นทางนับจำนวน Edge (2 เส้น) และลำดับต้องคั่นด้วย <code>,</code> ห้ามเขียนลูกศร <code>-&gt;</code> หากเขียนลูกศรจะได้ 0 คะแนน</div>')
    html.append('    </div>')
    
    html.append('  </div>')
    html.append('</div>')
    return '\n'.join(html)


def render_html_topo_indegree_table(indegree_data, enqueue_row=None, dequeue_row=None, queue_slots=None, final_pointers=None, title="Indegree Array Tracing Table (Topological Sort)", is_blank=False):
    """
    Renders the exact Indegree Array Tracing table matching Dr. Pradit's worksheets (Topological sort p.6):
    - Rows for Vertices 1..7
    - Row for Enqueue (v)
    - Row for Dequeue (v)
    - Side Vertical Queue Buffer: q [6] down to [0]
    - Horizontal Circular Queue Buffer: [0]..[6]
    - Status of front, back, currentSize, and topological order.
    """
    if enqueue_row is None:
        enqueue_row = ['1', '2', '5', '4', '3, 7', '-', '6', '-']
    if dequeue_row is None:
        dequeue_row = ['-', '1', '2', '5', '4', '3', '7', '6']
    if queue_slots is None:
        queue_slots = ['1', '2', '5', '4', '3', '7', '6']
    if final_pointers is None:
        final_pointers = {'front': 0, 'back': 6, 'currentSize': 0, 'order': '1, 2, 5, 4, 3, 7, 6'}
        
    html = [
        '<div style="margin:16px 0; font-family:\'Segoe UI\', Tahoma, sans-serif;">',
        f'  <div style="font-size:14px; font-weight:bold; color:#1e293b; margin-bottom:8px;">📝 {title}</div>',
        '  <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">',
        '    <div style="flex:3; min-width:480px; overflow-x:auto;">',
        '      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #334155;">',
        '        <thead>',
        '          <tr style="background:#1e293b; color:#ffffff;">',
        '            <th style="padding:8px 6px; border:1px solid #475569; width:85px;">Vertex (v)</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">เริ่มต้น (Init)</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 1</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 2</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 3</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 4</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 5</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 6</th>',
        '            <th style="padding:8px 6px; border:1px solid #475569;">รอบที่ 7</th>',
        '          </tr>',
        '        </thead>',
        '        <tbody>'
    ]
    
    rounds = ['initial', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
    for v_data in indegree_data:
        v = v_data['vertex']
        html.append('          <tr style="background:#ffffff;">')
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1; font-weight:bold; background:#f8fafc; color:#0f172a;">v{v}</td>')
        
        for r in rounds:
            val = v_data.get(r, '&nbsp;') if not is_blank else '&nbsp;'
            html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1;">{val}</td>')
        html.append('          </tr>')
        
    # Enqueue (v) row
    html.append('          <tr style="background:#e0e7ff; font-weight:bold;">')
    html.append('            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">Enqueue (v)</td>')
    for val in enqueue_row:
        dsp = val if not is_blank else '&nbsp;'
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#1e1b4b;">{dsp}</td>')
    html.append('          </tr>')
    
    # Dequeue (v) row
    html.append('          <tr style="background:#fee2e2; font-weight:bold;">')
    html.append('            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">Dequeue (v)</td>')
    for val in dequeue_row:
        dsp = val if not is_blank else '&nbsp;'
        html.append(f'            <td style="padding:7px 6px; border:1px solid #cbd5e1; color:#991b1b;">{dsp}</td>')
    html.append('          </tr>')
    
    html.append('        </tbody>')
    html.append('      </table>')
    html.append('    </div>')
    
    # Side Vertical Queue Stack: q [6] down to [0]
    html.append('    <div style="flex:1; min-width:160px; max-width:200px;">')
    html.append('      <div style="font-size:13px; font-weight:bold; color:#1e293b; margin-bottom:6px; text-align:center;">📦 Vertical Queue (q)</div>')
    html.append('      <table style="width:100%; border-collapse:collapse; text-align:center; font-size:12.5px; border:2px solid #475569;">')
    html.append('        <thead><tr style="background:#334155; color:#ffffff;"><th style="padding:6px; border:1px solid #475569; width:45px;">Index</th><th style="padding:6px; border:1px solid #475569;">Vertex</th></tr></thead>')
    html.append('        <tbody>')
    
    for idx in range(6, -1, -1):
        val = queue_slots[idx] if idx < len(queue_slots) and queue_slots[idx] is not None and not is_blank else '&nbsp;'
        val_styled = f'<strong style="color:#1e40af;">{val}</strong>' if val != '&nbsp;' and val != '-' else ('<span style="color:#94a3b8;">-</span>' if not is_blank else '&nbsp;')
        html.append(f'          <tr style="background:{"#f8fafc" if idx % 2 == 1 else "#ffffff"};">')
        html.append(f'            <td style="padding:6px 4px; border:1px solid #cbd5e1; font-weight:600; color:#64748b; font-family:Consolas, monospace;">[{idx}]</td>')
        html.append(f'            <td style="padding:6px 4px; border:1px solid #cbd5e1;">{val_styled}</td>')
        html.append('          </tr>')
        
    html.append('        </tbody>')
    html.append('      </table>')
    html.append('    </div>')
    html.append('  </div>')
    
    # Horizontal Circular Queue Buffer & Form fields
    html.append('  <div style="margin-top:14px; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:8px; padding:12px;">')
    html.append('    <div style="font-size:13px; font-weight:bold; color:#334155; margin-bottom:8px;">🔄 Horizontal Circular Queue Buffer &amp; Final Pointer Status:</div>')
    html.append('    <table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:10px;">')
    html.append('      <tr style="background:#334155; color:#ffffff; font-size:12px;"><th style="padding:5px;">Index</th>' + ''.join([f'<th style="padding:5px; border:1px solid #475569;">[{i}]</th>' for i in range(7)]) + '</tr>')
    
    row_cells = []
    for i in range(7):
        val = queue_slots[i] if i < len(queue_slots) and queue_slots[i] is not None and not is_blank else '&nbsp;'
        val_dsp = f'<strong style="color:#1e40af;">{val}</strong>' if val != '&nbsp;' and val != '-' else ('<span style="color:#94a3b8;">-</span>' if not is_blank else '&nbsp;')
        row_cells.append(f'<td style="padding:8px 4px; border:1px solid #cbd5e1; background:#ffffff;">{val_dsp}</td>')
    html.append('      <tr><td style="padding:6px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; font-size:12px;">q Value</td>' + ''.join(row_cells) + '</tr>')
    html.append('    </table>')
    
    front_val = final_pointers.get('front', 0) if not is_blank else '............'
    back_val = final_pointers.get('back', 6) if not is_blank else '............'
    csize_val = final_pointers.get('currentSize', 0) if not is_blank else '............'
    order_val = final_pointers.get('order', '1, 2, 5, 4, 3, 7, 6') if not is_blank else '............................................................'
    
    html.append('    <div style="display:flex; justify-content:space-around; font-size:12.5px; color:#1e293b; background:#ffffff; padding:8px; border-radius:6px; border:1px solid #e2e8f0; flex-wrap:wrap; gap:10px;">')
    html.append(f'      <div>• <strong>front</strong> = <span style="color:#dc2626; font-weight:bold;">{front_val}</span> (สูตร: <code>(front+1)%7</code>)</div>')
    html.append(f'      <div>• <strong>back</strong> = <span style="color:#16a34a; font-weight:bold;">{back_val}</span> (สูตร: <code>(back+1)%7</code>)</div>')
    html.append(f'      <div>• <strong>currentSize</strong> = <span style="color:#2563eb; font-weight:bold;">{csize_val}</span> (Empty)</div>')
    html.append('    </div>')
    
    html.append('    <div style="margin-top:10px; font-size:12.5px; background:#eff6ff; padding:10px; border-radius:6px; border:1px solid #bfdbfe;">')
    html.append(f'      <div><strong>ลำดับ Topological Order:</strong> <span style="color:#1d4ed8; font-weight:bold; font-size:14px;">{order_val}</span></div>')
    html.append('      <div style="font-size:11px; color:#b91c1c; margin-top:4px;">⚠️ <strong>คำเตือนอาจารย์ประดิษฐ์:</strong> ห้ามใส่ลูกศร <code>-&gt;</code> เด็ดขาด ให้คั่นด้วยเครื่องหมายจุลภาค <code>,</code> เท่านั้น หากใส่ลูกศรจะถูกปรับเป็น 0 คะแนน</div>')
    html.append('    </div>')
    
    html.append('  </div>')
    html.append('</div>')
    return '\n'.join(html)

