r"""
Build Script for Final Exam 2026 Set B
Generates:
1. Diagrams (PNG & SVG)
2. Blank Exam Paper PDF (6 Pages A4)
3. Master Solutions PDF (6 Pages A4)
4. Interactive Web Application HTML
All in: C:/Project/python-data-structures-and-algorithms/New-Lectures/Final/
"""

import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont

# Base Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAM_DIR = os.path.join(BASE_DIR, 'diagrams')
os.makedirs(DIAGRAM_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_names = [
        r"C:\Windows\Fonts\tahomabd.ttf" if bold else r"C:\Windows\Fonts\tahoma.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for fn in font_names:
        if os.path.exists(fn):
            try:
                return ImageFont.truetype(fn, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_arrow(draw, x1, y1, x2, y2, color="#1e293b", width=3, arrow_size=14):
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
    ax1 = x2 - ux * arrow_size + px * (arrow_size * 0.45)
    ay1 = y2 - uy * arrow_size + py * (arrow_size * 0.45)
    ax2 = x2 - ux * arrow_size - px * (arrow_size * 0.45)
    ay2 = y2 - uy * arrow_size - py * (arrow_size * 0.45)
    draw.polygon([(x2, y2), (ax1, ay1), (ax2, ay2)], fill=color)

def generate_set_b_diagrams():
    # 1. Topological Sort DAG (set_b_topo.png)
    # 7 vertices: 1..7, edges: (5,1), (5,2), (1,3), (1,4), (2,4), (2,7), (3,6), (4,6), (4,7)
    W, H = 800, 440
    im_topo = Image.new("RGB", (W, H), "#ffffff")
    draw_t = ImageDraw.Draw(im_topo)
    
    # Border
    draw_t.rounded_rectangle([(10, 10), (W - 10, H - 10)], radius=12, fill="#f8fafc", outline="#cbd5e1", width=2)
    
    # Title
    font_title = get_font(18, bold=True)
    draw_t.text((W // 2, 28), "Directed Acyclic Graph G = (V, E) [Set B]: |V| = 7, |E| = 9", fill="#1e3a8a", font=font_title, anchor="mm")
    
    coords_topo = {
        5: (100, 160),
        1: (260, 90),
        2: (260, 270),
        3: (460, 90),
        4: (460, 270),
        6: (680, 160),
        7: (460, 390)
    }
    
    edges_topo = [
        (5, 1), (5, 2),
        (1, 3), (1, 4),
        (2, 4), (2, 7),
        (3, 6),
        (4, 6), (4, 7)
    ]
    
    R = 24
    for u, v in edges_topo:
        x1, y1 = coords_topo[u]
        x2, y2 = coords_topo[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist > 0:
            ux = dx / dist
            uy = dy / dist
            sx = x1 + ux * R
            sy = y1 + uy * R
            ex = x2 - ux * (R + 6)
            ey = y2 - uy * (R + 6)
            draw_arrow(draw_t, sx, sy, ex, ey, color="#334155", width=3, arrow_size=12)
            
    # Nodes
    font_node = get_font(18, bold=True)
    font_in = get_font(12, bold=True)
    indegrees = {5: 0, 1: 1, 2: 1, 3: 1, 4: 2, 6: 2, 7: 2}
    
    for u, (x, y) in coords_topo.items():
        # Node circle
        bg_col = "#dbeafe" if indegrees[u] == 0 else "#f1f5f9"
        border_col = "#2563eb" if indegrees[u] == 0 else "#475569"
        draw_t.ellipse([(x - R, y - R), (x + R, y + R)], fill=bg_col, outline=border_col, width=3)
        draw_t.text((x, y - 1), str(u), fill="#0f172a", font=font_node, anchor="mm")
        # Indegree label
        draw_t.text((x, y + R + 12), f"in={indegrees[u]}", fill="#2563eb" if indegrees[u]==0 else "#64748b", font=font_in, anchor="mm")

    topo_path = os.path.join(DIAGRAM_DIR, "set_b_topo.png")
    im_topo.save(topo_path)
    print(f"Saved: {topo_path}")

    # 2. Shortest Path Graph (set_b_shortest_path.png)
    # 7 vertices: A..G
    # Edges: (A,B), (A,D), (B,C), (B,E), (C,F), (D,E), (D,G), (E,C), (E,F), (E,G), (G,F)
    W, H = 840, 460
    im_sp = Image.new("RGB", (W, H), "#ffffff")
    draw_s = ImageDraw.Draw(im_sp)
    
    draw_s.rounded_rectangle([(10, 10), (W - 10, H - 10)], radius=12, fill="#f8fafc", outline="#cbd5e1", width=2)
    draw_s.text((W // 2, 28), "Directed Graph G = (V, E) [Set B]: Start Vertex = A, |V| = 7, |E| = 11", fill="#1e3a8a", font=font_title, anchor="mm")

    coords_sp = {
        'A': (90, 230),
        'B': (260, 110),
        'D': (260, 350),
        'C': (450, 110),
        'E': (450, 230),
        'G': (450, 350),
        'F': (680, 230)
    }

    edges_sp = [
        ('A', 'B'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'E'), ('D', 'G'),
        ('E', 'C'), ('E', 'F'), ('E', 'G'),
        ('G', 'F')
    ]

    for u, v in edges_sp:
        x1, y1 = coords_sp[u]
        x2, y2 = coords_sp[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist > 0:
            ux = dx / dist
            uy = dy / dist
            sx = x1 + ux * R
            sy = y1 + uy * R
            ex = x2 - ux * (R + 6)
            ey = y2 - uy * (R + 6)
            draw_arrow(draw_s, sx, sy, ex, ey, color="#334155", width=3, arrow_size=12)

    for u, (x, y) in coords_sp.items():
        bg_col = "#dcfce7" if u == 'A' else ("#fee2e2" if u == 'F' else "#f1f5f9")
        border_col = "#16a34a" if u == 'A' else ("#dc2626" if u == 'F' else "#475569")
        draw_s.ellipse([(x - R, y - R), (x + R, y + R)], fill=bg_col, outline=border_col, width=3)
        draw_s.text((x, y - 1), u, fill="#0f172a", font=font_node, anchor="mm")
        
        lbl = "Start (0)" if u == 'A' else ("Target" if u == 'F' else "")
        if lbl:
            draw_s.text((x, y + R + 14), lbl, fill="#16a34a" if u == 'A' else "#dc2626", font=font_in, anchor="mm")

    sp_path = os.path.join(DIAGRAM_DIR, "set_b_shortest_path.png")
    im_sp.save(sp_path)
    print(f"Saved: {sp_path}")

if __name__ == '__main__':
    generate_set_b_diagrams()
