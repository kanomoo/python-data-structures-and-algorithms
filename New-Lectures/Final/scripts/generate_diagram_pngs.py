"""
Diagram PNG Generator using Pillow
Generates crisp, high-resolution (300 DPI equivalent) PNG diagrams
for ReportLab PDF embedding and external image viewers.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'diagrams')
os.makedirs(OUT_DIR, exist_ok=True)

# Also ensure scratch/diagrams exists for backwards compatibility
SCRATCH_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'scratch', 'diagrams')
os.makedirs(SCRATCH_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\tahomabd.ttf" if bold else "C:\\Windows\\Fonts\\tahoma.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
    ]
    for fn in font_names:
        if os.path.exists(fn):
            try:
                return ImageFont.truetype(fn, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_arrow(draw, x1, y1, x2, y2, color="#1e293b", width=3, arrow_size=12):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    ux = dx / dist
    uy = dy / dist
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
    
    # Arrow head
    px = -uy
    py = ux
    ax1 = x2 - ux * arrow_size + px * (arrow_size * 0.5)
    ay1 = y2 - uy * arrow_size + py * (arrow_size * 0.5)
    ax2 = x2 - ux * arrow_size - px * (arrow_size * 0.5)
    ay2 = y2 - uy * arrow_size - py * (arrow_size * 0.5)
    draw.polygon([(x2, y2), (ax1, ay1), (ax2, ay2)], fill=color)

def generate_png_graph_exam2026_topo():
    """
    Generates canonical 7-vertex DAG for Exam 2026 Question 5 (Topological Sort).
    Matches Lecture 10 (p.5), toposort_p5.png, and whiteboard photo IMG_20260923_110059.
    Vertices: v1..v7, 12 directed edges.
    v1 is the unique Source (in-degree=0), v6 is the Sink (out-degree=0).
    """
    W, H = 1000, 560
    im = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(im)
    
    # Canonical layout from Dr. Pradit's course slide p.5
    coords = {
        1: (260, 125), 2: (740, 125),
        3: (110, 305), 4: (500, 305), 5: (890, 305),
        6: (260, 480), 7: (740, 480)
    }
    edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 4), (2, 5),
        (3, 6),
        (4, 3), (4, 6), (4, 7),
        (5, 4), (5, 7),
        (7, 6)
    ]
    R = 36
    font_title = get_font(23, bold=True)
    font_node = get_font(22, bold=True)
    font_sub = get_font(15, bold=True)
    
    # Title
    draw.text((W // 2, 28), "Directed Acyclic Graph (DAG) [Lecture 10 & Exam 2026 Q5]: |V|=7, |E|=12", font=font_title, fill="#1e293b", anchor="mm")
    
    # Draw Edges
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        ux = dx / dist
        uy = dy / dist
        sx = x1 + ux * R
        sy = y1 + uy * R
        ex = x2 - ux * (R + 6)
        ey = y2 - uy * (R + 6)
        draw_arrow(draw, sx, sy, ex, ey, color="#334155", width=3, arrow_size=14)
        
    # Draw Vertices
    for u, (x, y) in coords.items():
        is_source = (u == 1)
        is_sink = (u == 6)
        if is_source:
            fill_col = "#dbeafe"
            outline_col = "#1d4ed8"
        elif is_sink:
            fill_col = "#fef2f2"
            outline_col = "#dc2626"
        else:
            fill_col = "#f8fafc"
            outline_col = "#1e293b"
            
        draw.ellipse([x - R, y - R, x + R, y + R], fill=fill_col, outline=outline_col, width=4 if (is_source or is_sink) else 3)
        draw.text((x, y), f"v{u}", font=font_node, fill="#0f172a", anchor="mm")
        
        if is_source:
            draw.text((x, y - R - 16), "SOURCE (In-deg=0)", font=font_sub, fill="#1d4ed8", anchor="mm")
        elif is_sink:
            draw.text((x, y + R + 16), "SINK (Out-deg=0)", font=font_sub, fill="#dc2626", anchor="mm")

    path1 = os.path.join(OUT_DIR, "graph_topo_sort.png")
    path2 = os.path.join(SCRATCH_DIR, "graph_topo_sort.png")
    im.save(path1)
    im.save(path2)
    return path1

def generate_png_adj_topo():
    """
    Generates Adjacency List for Canonical DAG (Exam 2026 Question 5).
    Matches Lecture 10 p.5, toposort_solved_p5.png, and whiteboard photo IMG_20260923_110059.
    """
    W, H = 1000, 530
    im = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(im)
    
    font_title = get_font(22, bold=True)
    font_hdr = get_font(20, bold=True)
    font_val = get_font(18, bold=True)
    
    draw.text((W // 2, 30), "Adjacency List: Directed Acyclic Graph (|V|=7, |E|=12)", font=font_title, fill="#1e293b", anchor="mm")
    
    # Exact adjacency list from Lecture 10 p.5 / toposort_p5.png
    adj = {
        1: [2, 4, 3],
        2: [4, 5],
        3: [6],
        4: [3, 6, 7],
        5: [4, 7],
        6: [],
        7: [6]
    }
    
    row_h = 58
    start_y = 65
    hdr_x = 70
    hdr_w = 90
    hdr_h = 44
    node_w = 75
    node_h = 42
    
    for row_idx, (v, neighbors) in enumerate(adj.items()):
        y = start_y + row_idx * row_h
        cy = y + hdr_h // 2
        
        # Header box: [ Label | • ]
        draw.rectangle([hdr_x, y, hdr_x + hdr_w, y + hdr_h], fill="#f1f5f9", outline="#1e293b", width=3)
        draw.line([hdr_x + 55, y, hdr_x + 55, y + hdr_h], fill="#1e293b", width=2)
        draw.text((hdr_x + 27, cy), f"v{v}", font=font_hdr, fill="#0f172a", anchor="mm")
        draw.ellipse([hdr_x + 70, cy - 4, hdr_x + 78, cy + 4], fill="#0284c7")
        
        curr_x = hdr_x + hdr_w
        if not neighbors:
            # Points down to ground symbol ⏚
            gx = curr_x + 35
            draw.line([(hdr_x + 74, cy), (gx, cy), (gx, cy + 18)], fill="#1e293b", width=2)
            draw.line([(gx - 14, cy + 18), (gx + 14, cy + 18)], fill="#1e293b", width=3)
            draw.line([(gx - 9, cy + 23), (gx + 9, cy + 23)], fill="#1e293b", width=2)
            draw.line([(gx - 4, cy + 28), (gx + 4, cy + 28)], fill="#1e293b", width=2)
        else:
            first_nx = curr_x + 25
            draw_arrow(draw, hdr_x + 74, cy, first_nx, cy, color="#1e293b", width=2, arrow_size=10)
            curr_x = first_nx
            
            for n_idx, dest in enumerate(neighbors):
                ny = cy - node_h // 2
                draw.rectangle([curr_x, ny, curr_x + node_w, ny + node_h], fill="#ffffff", outline="#334155", width=2)
                draw.line([curr_x + 46, ny, curr_x + 46, ny + node_h], fill="#334155", width=2)
                draw.text((curr_x + 23, cy), str(dest), font=font_val, fill="#0f172a", anchor="mm")
                draw.ellipse([curr_x + 58, cy - 4, curr_x + 66, cy + 4], fill="#0284c7")
                
                next_x = curr_x + node_w + 25
                if n_idx < len(neighbors) - 1:
                    draw_arrow(draw, curr_x + 62, cy, next_x, cy, color="#1e293b", width=2, arrow_size=10)
                    curr_x = next_x
                else:
                    gx = curr_x + node_w + 20
                    draw.line([(curr_x + 62, cy), (gx, cy), (gx, cy + 14)], fill="#1e293b", width=2)
                    draw.line([(gx - 12, cy + 14), (gx + 12, cy + 14)], fill="#1e293b", width=3)
                    draw.line([(gx - 8, cy + 19), (gx + 8, cy + 19)], fill="#1e293b", width=2)
                    draw.line([(gx - 4, cy + 24), (gx + 4, cy + 24)], fill="#1e293b", width=2)

    path1 = os.path.join(OUT_DIR, "adj_topo_sort.png")
    path2 = os.path.join(SCRATCH_DIR, "adj_topo_sort.png")
    im.save(path1)
    im.save(path2)
    return path1

def generate_png_graph_exam2026_sp():
    """Generates Shortest Path Graph for Exam 2026 Question 6."""
    W, H = 1000, 560
    im = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(im)
    
    coords = {
        1: (120, 280),
        2: (320, 110),
        3: (320, 450),
        4: (440, 280),
        5: (660, 110),
        7: (660, 450),
        6: (880, 280)
    }
    edges = [
        (1, 2), (1, 4),
        (2, 4), (2, 5),
        (3, 1), (3, 6),
        (4, 3), (4, 5), (4, 6), (4, 7),
        (5, 7),
        (7, 6)
    ]
    R = 36
    font_title = get_font(24, bold=True)
    font_node = get_font(22, bold=True)
    font_sub = get_font(16, bold=True)
    
    draw.text((W // 2, 35), "Directed Graph G = (V, E) [Exam 2026 Question 6]: Source Vertex = 1", font=font_title, fill="#1e293b", anchor="mm")
    
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        ux = dx / dist
        uy = dy / dist
        sx = x1 + ux * R
        sy = y1 + uy * R
        ex = x2 - ux * (R + 6)
        ey = y2 - uy * (R + 6)
        draw_arrow(draw, sx, sy, ex, ey, color="#334155", width=3, arrow_size=14)
        
    for u, (x, y) in coords.items():
        is_source = (u == 1)
        fill_col = "#dbeafe" if is_source else "#f8fafc"
        outline_col = "#2563eb" if is_source else "#1e293b"
        draw.ellipse([x - R, y - R, x + R, y + R], fill=fill_col, outline=outline_col, width=4 if is_source else 3)
        draw.text((x, y), str(u), font=font_node, fill="#0f172a", anchor="mm")
        if is_source:
            draw.text((x, y - R - 16), "SOURCE", font=font_sub, fill="#2563eb", anchor="mm")

    path1 = os.path.join(OUT_DIR, "graph_shortest_path.png")
    path2 = os.path.join(SCRATCH_DIR, "graph_shortest_path.png")
    im.save(path1)
    im.save(path2)
    return path1

def generate_png_adj_sp():
    """Generates Adjacency List for Exam 2026 Question 6."""
    W, H = 1000, 520
    im = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(im)
    
    font_title = get_font(22, bold=True)
    font_hdr = get_font(20, bold=True)
    font_val = get_font(18, bold=True)
    
    draw.text((W // 2, 30), "Adjacency List: Directed Graph (Source = 1, 7 Vertices)", font=font_title, fill="#1e293b", anchor="mm")
    
    adj = {
        1: [2, 4],
        2: [4, 5],
        3: [1, 6],
        4: [3, 5, 6, 7],
        5: [7],
        6: [],
        7: [6]
    }
    
    row_h = 58
    start_y = 70
    hdr_x = 70
    hdr_w = 90
    hdr_h = 44
    node_w = 75
    node_h = 42
    
    for row_idx, (v, neighbors) in enumerate(adj.items()):
        y = start_y + row_idx * row_h
        cy = y + hdr_h // 2
        
        draw.rectangle([hdr_x, y, hdr_x + hdr_w, y + hdr_h], fill="#f1f5f9", outline="#1e293b", width=3)
        draw.line([hdr_x + 55, y, hdr_x + 55, y + hdr_h], fill="#1e293b", width=2)
        draw.text((hdr_x + 27, cy), str(v), font=font_hdr, fill="#0f172a", anchor="mm")
        draw.ellipse([hdr_x + 70, cy - 4, hdr_x + 78, cy + 4], fill="#0284c7")
        
        curr_x = hdr_x + hdr_w
        if not neighbors:
            gx = curr_x + 35
            draw.line([(hdr_x + 74, cy), (gx, cy), (gx, cy + 18)], fill="#1e293b", width=2)
            draw.line([(gx - 14, cy + 18), (gx + 14, cy + 18)], fill="#1e293b", width=3)
            draw.line([(gx - 9, cy + 23), (gx + 9, cy + 23)], fill="#1e293b", width=2)
            draw.line([(gx - 4, cy + 28), (gx + 4, cy + 28)], fill="#1e293b", width=2)
        else:
            first_nx = curr_x + 25
            draw_arrow(draw, hdr_x + 74, cy, first_nx, cy, color="#1e293b", width=2, arrow_size=10)
            curr_x = first_nx
            
            for n_idx, dest in enumerate(neighbors):
                ny = cy - node_h // 2
                draw.rectangle([curr_x, ny, curr_x + node_w, ny + node_h], fill="#ffffff", outline="#334155", width=2)
                draw.line([curr_x + 46, ny, curr_x + 46, ny + node_h], fill="#334155", width=2)
                draw.text((curr_x + 23, cy), str(dest), font=font_val, fill="#0f172a", anchor="mm")
                draw.ellipse([curr_x + 58, cy - 4, curr_x + 66, cy + 4], fill="#0284c7")
                
                next_x = curr_x + node_w + 25
                if n_idx < len(neighbors) - 1:
                    draw_arrow(draw, curr_x + 62, cy, next_x, cy, color="#1e293b", width=2, arrow_size=10)
                    curr_x = next_x
                else:
                    gx = curr_x + node_w + 20
                    draw.line([(curr_x + 62, cy), (gx, cy), (gx, cy + 14)], fill="#1e293b", width=2)
                    draw.line([(gx - 12, cy + 14), (gx + 12, cy + 14)], fill="#1e293b", width=3)
                    draw.line([(gx - 8, cy + 19), (gx + 8, cy + 19)], fill="#1e293b", width=2)
                    draw.line([(gx - 4, cy + 24), (gx + 4, cy + 24)], fill="#1e293b", width=2)

    path1 = os.path.join(OUT_DIR, "adj_shortest_path.png")
    path2 = os.path.join(SCRATCH_DIR, "adj_shortest_path.png")
    im.save(path1)
    im.save(path2)
    return path1

def generate_png_graph_lecture10():
    """Generates classic DAG & Shortest Path graph from Lecture 10 & 11."""
    W, H = 1000, 560
    im = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(im)
    
    coords = {
        1: (260, 100), 2: (740, 100),
        3: (100, 280), 4: (500, 280), 5: (900, 280),
        6: (260, 460), 7: (740, 460)
    }
    edges = [
        (1, 2), (1, 3), (1, 4),
        (2, 4), (2, 5),
        (3, 6),
        (4, 3), (4, 6), (4, 7),
        (5, 4), (5, 7),
        (7, 6)
    ]
    R = 36
    font_title = get_font(24, bold=True)
    font_node = get_font(22, bold=True)
    
    draw.text((W // 2, 35), "Directed Graph G = (V, E) [Lecture 10 & 11]: |V|=7, |E|=12", font=font_title, fill="#1e293b", anchor="mm")
    
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        ux = dx / dist
        uy = dy / dist
        sx = x1 + ux * R
        sy = y1 + uy * R
        ex = x2 - ux * (R + 6)
        ey = y2 - uy * (R + 6)
        draw_arrow(draw, sx, sy, ex, ey, color="#334155", width=3, arrow_size=14)
        
    for u, (x, y) in coords.items():
        draw.ellipse([x - R, y - R, x + R, y + R], fill="#f8fafc", outline="#1e293b", width=3)
        draw.text((x, y), f"v{u}", font=font_node, fill="#0f172a", anchor="mm")

    path1 = os.path.join(OUT_DIR, "graph_lecture10.png")
    path2 = os.path.join(SCRATCH_DIR, "graph_lecture10.png")
    im.save(path1)
    im.save(path2)
    return path1

def generate_png_adj_lecture10():
    """Generates Adjacency List for Lecture 10 & 11."""
    W, H = 1000, 520
    im = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(im)
    
    font_title = get_font(22, bold=True)
    font_hdr = get_font(20, bold=True)
    font_val = get_font(18, bold=True)
    
    draw.text((W // 2, 30), "Adjacency List: Lecture 10 & 11 Graph (7 Vertices)", font=font_title, fill="#1e293b", anchor="mm")
    
    adj = {
        1: [2, 4, 3],
        2: [4, 5],
        3: [6],
        4: [6, 7, 3],
        5: [4, 7],
        6: [],
        7: [6]
    }
    
    row_h = 58
    start_y = 70
    hdr_x = 70
    hdr_w = 90
    hdr_h = 44
    node_w = 75
    node_h = 42
    
    for row_idx, (v, neighbors) in enumerate(adj.items()):
        y = start_y + row_idx * row_h
        cy = y + hdr_h // 2
        
        draw.rectangle([hdr_x, y, hdr_x + hdr_w, y + hdr_h], fill="#f1f5f9", outline="#1e293b", width=3)
        draw.line([hdr_x + 55, y, hdr_x + 55, y + hdr_h], fill="#1e293b", width=2)
        draw.text((hdr_x + 27, cy), str(v), font=font_hdr, fill="#0f172a", anchor="mm")
        draw.ellipse([hdr_x + 70, cy - 4, hdr_x + 78, cy + 4], fill="#0284c7")
        
        curr_x = hdr_x + hdr_w
        if not neighbors:
            gx = curr_x + 35
            draw.line([(hdr_x + 74, cy), (gx, cy), (gx, cy + 18)], fill="#1e293b", width=2)
            draw.line([(gx - 14, cy + 18), (gx + 14, cy + 18)], fill="#1e293b", width=3)
            draw.line([(gx - 9, cy + 23), (gx + 9, cy + 23)], fill="#1e293b", width=2)
            draw.line([(gx - 4, cy + 28), (gx + 4, cy + 28)], fill="#1e293b", width=2)
        else:
            first_nx = curr_x + 25
            draw_arrow(draw, hdr_x + 74, cy, first_nx, cy, color="#1e293b", width=2, arrow_size=10)
            curr_x = first_nx
            
            for n_idx, dest in enumerate(neighbors):
                ny = cy - node_h // 2
                draw.rectangle([curr_x, ny, curr_x + node_w, ny + node_h], fill="#ffffff", outline="#334155", width=2)
                draw.line([curr_x + 46, ny, curr_x + 46, ny + node_h], fill="#334155", width=2)
                draw.text((curr_x + 23, cy), str(dest), font=font_val, fill="#0f172a", anchor="mm")
                draw.ellipse([curr_x + 58, cy - 4, curr_x + 66, cy + 4], fill="#0284c7")
                
                next_x = curr_x + node_w + 25
                if n_idx < len(neighbors) - 1:
                    draw_arrow(draw, curr_x + 62, cy, next_x, cy, color="#1e293b", width=2, arrow_size=10)
                    curr_x = next_x
                else:
                    gx = curr_x + node_w + 20
                    draw.line([(curr_x + 62, cy), (gx, cy), (gx, cy + 14)], fill="#1e293b", width=2)
                    draw.line([(gx - 12, cy + 14), (gx + 12, cy + 14)], fill="#1e293b", width=3)
                    draw.line([(gx - 8, cy + 19), (gx + 8, cy + 19)], fill="#1e293b", width=2)
                    draw.line([(gx - 4, cy + 24), (gx + 4, cy + 24)], fill="#1e293b", width=2)

    path1 = os.path.join(OUT_DIR, "adj_lecture10.png")
    path2 = os.path.join(SCRATCH_DIR, "adj_lecture10.png")
    im.save(path1)
    im.save(path2)
    return path1

if __name__ == '__main__':
    print("Generating diagram PNGs...")
    p1 = generate_png_graph_exam2026_topo()
    p2 = generate_png_adj_topo()
    p3 = generate_png_graph_exam2026_sp()
    p4 = generate_png_adj_sp()
    p5 = generate_png_graph_lecture10()
    p6 = generate_png_adj_lecture10()
    print("All PNG diagrams generated successfully!")
    print(f"Files saved in: {OUT_DIR} and {SCRATCH_DIR}")
