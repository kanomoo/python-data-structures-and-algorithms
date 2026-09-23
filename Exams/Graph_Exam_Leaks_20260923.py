"""
================================================================================
Graph Theory Exam Shortcuts & Leak Verifier (Dr. Pradit's Class - 2026-09-23)
================================================================================
This script automates and verifies all mathematical formulas, memory calculations,
and exam questions revealed by Dr. Pradit Pitaksatheinkul during the 2026-09-23 lecture.
"""

def complete_graph_edge_count(v: int) -> int:
    """
    Calculates the exact number of edges in an undirected complete graph.
    Formula: E = V * (V - 1) / 2
    
    EXAM TRAP:
    Must return an integer (e.g. 45 for V=10).
    Answering in formula form yields 0 points on the final exam.
    """
    return v * (v - 1) // 2


def adjacency_matrix_space(v: int) -> int:
    """Space requirement for Adjacency Matrix: O(|V|^2) cells."""
    return v * v


def adjacency_list_space(v: int, e: int) -> int:
    """Space requirement for Adjacency List: O(|V| + |E|) cells/nodes."""
    return v + e


def memory_waste_percentage(v: int, e: int):
    """
    Calculates percentage of memory used for value 1 vs value 0 in Adjacency Matrix.
    Used for English exam question:
    'What percentage of memory space is used for entries with value 1, and what for value 0?'
    """
    total_cells = v * v
    used_cells = e
    unused_cells = total_cells - e
    pct_used = (used_cells * 100.0) / total_cells
    pct_unused = (unused_cells * 100.0) / total_cells
    return total_cells, used_cells, unused_cells, pct_used, pct_unused


def run_exam_simulations():
    print("=" * 70)
    print("  GRAPH THEORY EXAM LEAKS & SHORTCUT VERIFICATION (2026-09-23)")
    print("=" * 70)

    # Question 1: 10 Vertices Complete Graph
    v10 = 10
    e10 = complete_graph_edge_count(v10)
    print(f"[Exam Question 1] Undirected Complete Graph with {v10} vertices:")
    print(f"  Formula: E = V * (V - 1) / 2 = {v10} * {v10-1} / 2")
    print(f"  EXACT REQUIRED ANSWER (Integer): {e10} edges")
    print("  WARNING: Do not answer as a formula; answer must be an integer!\n")

    # Question 2: Memory Waste in Lecture's 7-Vertex Graph (IMG_20260923_110522)
    v7, e12 = 7, 12
    tot, used, unused, pct_1, pct_0 = memory_waste_percentage(v7, e12)
    print(f"[Exam Question 2] 7-Vertex Graph with 12 Edges (Whiteboard Calculation):")
    print(f"  Total Matrix Cells: {tot} (7x7)")
    print(f"  Entries with value 1: {used} cells ({pct_1:.2f}%)")
    print(f"  Entries with value 0 (Wasted): {unused} cells ({pct_0:.2f}%)")
    print(f"  Conclusion: Matrix is inefficient because {pct_0:.2f}% of memory is wasted!\n")

    # Question 3: 10 Vertices, 20 Edges Comparison (IMG_20260923_113450 & 113807)
    v_comp, e_comp = 10, 20
    matrix_cells = adjacency_matrix_space(v_comp)
    list_cells = adjacency_list_space(v_comp, e_comp)
    savings = ((matrix_cells - list_cells) / matrix_cells) * 100.0
    print(f"[Exam Question 3] Directed Graph with {v_comp} Vertices and {e_comp} Edges:")
    print(f"  Adjacency Matrix uses: {matrix_cells} slots (|V|^2 = 10^2)")
    print(f"  Adjacency List uses:   {list_cells} slots (|E| + |V| = 20 + 10)")
    print(f"  Memory Savings by using Adjacency List: {savings:.1f}%\n")

    print("=" * 70)


if __name__ == "__main__":
    run_exam_simulations()
