"""
Final Exam Complete Practice Suite & Solutions (2026 / ภาคเรียนที่ 1 ปีการศึกษา 2569)
วิชา: 060243106 Data Structures and Algorithms
อาจารย์ผู้สอน: นายประดิษฐ์ พิทักษ์เสถียรกุล

สอดคล้องกับข้อสอบปลายภาค 7 ข้อ 70 คะแนน (หาร 2 เหลือ 35%):
1. Hashing (Separate Chaining, Linear Probing, Quadratic Probing)
2. Binary Min-Heap (Insertion, Percolate Up, DeleteMin, Percolate Down)
3. Insertion Sort (Pass-by-Pass Tracing)
4. Selection Sort & Bubble Sort (Min index swap & Total Swaps / Inversions)
5. Topological Sort (Indegree Array & Queue Trace)
6. Unweighted Shortest Path (BFS Table: Known, Dist, Path, Dequeue Order)
7. Properties & Theory Calculations (Heap, Complete Graph, Tree Max Nodes, Matrix Waste %)
"""

from collections import deque
import math
import sys

# Ensure UTF-8 output on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass



# =====================================================================
# ข้อที่ 1: Hashing (10 คะแนน)
# =====================================================================
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash_func(key)
        self.table[idx].append(key)

    def display(self):
        return {i: list(self.table[i]) for i in range(self.size)}


class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.linear_table = [None] * size
        self.quadratic_table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert_linear(self, key):
        base = self.hash_func(key)
        for i in range(self.size):
            idx = (base + i) % self.size
            if self.linear_table[idx] is None:
                self.linear_table[idx] = key
                return idx, i  # (slot, collisions)
        raise OverflowError("Hash table is full")

    def insert_quadratic(self, key):
        base = self.hash_func(key)
        for i in range(self.size):
            idx = (base + i * i) % self.size
            if self.quadratic_table[idx] is None:
                self.quadratic_table[idx] = key
                return idx, i  # (slot, collisions)
        raise OverflowError("Cannot insert using quadratic probing")


# =====================================================================
# ข้อที่ 2: Binary Min-Heap (10 คะแนน)
# =====================================================================
class BinaryMinHeap:
    def __init__(self):
        # 1-based indexing, index 0 is dummy sentinel
        self.heap = [None]

    def build_from_list(self, elements):
        self.heap = [None] + list(elements)

    def insert(self, val):
        """Percolate Up insertion"""
        self.heap.append(val)
        hole = len(self.heap) - 1
        trace = [hole]
        while hole > 1 and val < self.heap[hole // 2]:
            self.heap[hole] = self.heap[hole // 2]
            hole //= 2
            trace.append(hole)
        self.heap[hole] = val
        return trace

    def delete_min(self):
        """Percolate Down deletion"""
        if len(self.heap) <= 1:
            return None
        min_val = self.heap[1]
        last_val = self.heap.pop()
        if len(self.heap) == 1:
            return min_val

        hole = 1
        trace = [hole]
        n = len(self.heap) - 1
        while hole * 2 <= n:
            child = hole * 2
            if child != n and self.heap[child + 1] < self.heap[child]:
                child += 1
            if last_val > self.heap[child]:
                self.heap[hole] = self.heap[child]
                hole = child
                trace.append(hole)
            else:
                break
        self.heap[hole] = last_val
        return min_val, trace


# =====================================================================
# ข้อที่ 3: Insertion Sort (10 คะแนน)
# =====================================================================
def insertion_sort_trace(arr):
    a = list(arr)
    n = len(a)
    history = [("Initial", list(a), None)]
    for p in range(1, n):
        tmp = a[p]
        j = p
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
        history.append((f"Pass {p} (insert {tmp})", list(a), tmp))
    return history


# =====================================================================
# ข้อที่ 4: Selection Sort & Bubble Sort (10 คะแนน)
# =====================================================================
def selection_sort_trace(arr):
    a = list(arr)
    n = len(a)
    history = [("Initial", list(a), None, None)]
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        history.append((f"Pass {i+1}", list(a), min_idx, (i, min_idx)))
    return history


def bubble_sort_trace(arr):
    a = list(arr)
    n = len(a)
    history = [("Initial", list(a), 0)]
    total_swaps = 0
    for p in range(n - 1):
        pass_swaps = 0
        for j in range(n - 1 - p):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                pass_swaps += 1
                total_swaps += 1
        history.append((f"Pass {p+1}", list(a), pass_swaps))
    return history, total_swaps


# =====================================================================
# ข้อที่ 5: Topological Sort (10 คะแนน)
# =====================================================================
def topological_sort_trace(adj):
    indegree = {u: 0 for u in adj}
    for u in adj:
        for v in adj[u]:
            indegree[v] += 1

    initial_indegree = dict(indegree)
    q = deque([u for u in adj if indegree[u] == 0])
    order = []
    step_trace = []

    while q:
        curr = q.popleft()
        order.append(curr)
        newly_enqueued = []
        for nxt in adj[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
                newly_enqueued.append(nxt)
        step_trace.append((curr, list(q), newly_enqueued, dict(indegree)))

    return initial_indegree, order, step_trace


# =====================================================================
# ข้อที่ 6: Unweighted Shortest Path (10 คะแนน)
# =====================================================================
def unweighted_shortest_path_trace(adj, start_vertex):
    vertices = sorted(adj.keys())
    dist = {v: float('inf') for v in vertices}
    path = {v: 0 for v in vertices}
    known = {v: False for v in vertices}

    dist[start_vertex] = 0
    q = deque([start_vertex])
    dequeue_order = []
    table_history = []

    while q:
        v = q.popleft()
        known[v] = True
        dequeue_order.append(v)

        for w in adj[v]:
            if dist[w] == float('inf'):
                dist[w] = dist[v] + 1
                path[w] = v
                q.append(w)

        table_history.append((v, dict(known), dict(dist), dict(path), list(q)))

    return dist, path, known, dequeue_order, table_history


def reconstruct_path(path_dict, start, dest):
    if dist_val := path_dict.get(dest):
        pass
    curr = dest
    route = []
    while curr != 0 and curr is not None:
        route.append(curr)
        if curr == start:
            break
        curr = path_dict[curr]
    route.reverse()
    # กฎเหล็กอาจารย์: คั่นด้วยจุลภาค ห้ามใช้ลูกศร
    return ", ".join(route)


# =====================================================================
# ข้อที่ 7: Properties & Theory Calculations (10 คะแนน)
# =====================================================================
def calculate_heap_properties():
    return {
        "properties": [
            "1. Structure Property (ต้องเป็น Complete Binary Tree - โหนดเต็มทุกระดับ ยกเว้นระดับสุดท้ายที่ชิดซ้าย)",
            "2. Heap-Order Property (สำหรับ Min-Heap โหนดแม่ต้องค่าน้อยกว่าหรือเท่ากับลูกเสมอ: parent <= children)"
        ],
        "index_formulas": {
            "root": 1,
            "parent(i)": "floor(i / 2)",
            "left_child(i)": "2 * i",
            "right_child(i)": "2 * i + 1"
        }
    }


def calculate_tree_max_nodes(height):
    # Max nodes at height h = 2^(h+1) - 1
    return 2 ** (height + 1) - 1


def calculate_complete_graph_edges(vertices, directed=False):
    if directed:
        return vertices * (vertices - 1)
    return vertices * (vertices - 1) // 2


def calculate_matrix_waste(vertices, edges):
    total_cells = vertices * vertices
    used_cells = edges
    waste_cells = total_cells - used_cells
    waste_percent = (waste_cells / total_cells) * 100
    used_percent = (used_cells / total_cells) * 100
    return {
        "total_cells": total_cells,
        "used_cells": used_cells,
        "waste_cells": waste_cells,
        "waste_percent": round(waste_percent, 2),
        "used_percent": round(used_percent, 2)
    }


# =====================================================================
# MAIN VERIFICATION & RUNNER
# =====================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("🎓 DATA STRUCTURES & ALGORITHMS - FINAL EXAM COMPLETE VERIFICATION")
    print("=" * 70)

    # 1. Hashing
    print("\n[PART 1] HASHING (10 MARKS)")
    keys = [43, 22, 10, 44, 23, 73, 24]
    sc = HashTableChaining(10)
    oa = HashTableOpenAddressing(10)
    for k in keys:
        sc.insert(k)
        oa.insert_linear(k)
        oa.insert_quadratic(k)

    print("Separate Chaining Table:", sc.display())
    print("Linear Probing Table:   ", oa.linear_table)
    print("Quadratic Probing Table:", oa.quadratic_table)
    assert oa.linear_table[3] == 43
    assert oa.linear_table[2] == 22
    assert oa.linear_table[0] == 10
    print(">> Part 1 Hashing verification PASSED.")

    # 2. Binary Heap
    print("\n[PART 2] BINARY MIN-HEAP (10 MARKS)")
    initial_heap_nodes = [13, 14, 16, 19, 21, 19, 68, 65, 26, 31, 32]
    heap = BinaryMinHeap()
    heap.build_from_list(initial_heap_nodes)
    print(f"Initial Heap (size {len(initial_heap_nodes)}):", heap.heap[1:])

    # Insert 14
    trace_up = heap.insert(14)
    print(f"After insert(14) (Percolate up path {trace_up}):", heap.heap[1:])
    assert heap.heap[1] == 13

    # DeleteMin
    min_val, trace_down = heap.delete_min()
    print(f"After deleteMin() (Popped {min_val}, Percolate down path {trace_down}):", heap.heap[1:])
    assert min_val == 13
    print(">> Part 2 Binary Heap verification PASSED.")

    # 3. Insertion Sort
    print("\n[PART 3] INSERTION SORT (10 MARKS)")
    test_arr = [34, 8, 64, 51, 32, 21]
    ins_trace = insertion_sort_trace(test_arr)
    for step, state, tmp in ins_trace:
        print(f"  {step:<22}: {state}")
    assert ins_trace[-1][1] == sorted(test_arr)
    print(">> Part 3 Insertion Sort verification PASSED.")

    # 4. Selection & Bubble Sort
    print("\n[PART 4] SELECTION SORT & BUBBLE SORT (10 MARKS)")
    sel_trace = selection_sort_trace(test_arr)
    print("Selection Sort Final:", sel_trace[-1][1])
    assert sel_trace[-1][1] == sorted(test_arr)

    bub_trace, total_swaps = bubble_sort_trace(test_arr)
    print(f"Bubble Sort Final:   {bub_trace[-1][1]} | Total Swaps: {total_swaps}")
    assert bub_trace[-1][1] == sorted(test_arr)
    print(">> Part 4 Selection & Bubble Sort verification PASSED.")

    # 5. Topological Sort
    print("\n[PART 5] TOPOLOGICAL SORT (10 MARKS)")
    dag_adj = {
        'v1': ['v2', 'v3', 'v4'],
        'v2': ['v4', 'v5'],
        'v3': ['v6'],
        'v4': ['v3', 'v6', 'v7'],
        'v5': ['v4', 'v7'],
        'v6': [],
        'v7': ['v6']
    }
    in_deg, topo_res, _ = topological_sort_trace(dag_adj)
    print("Initial In-Degrees:", in_deg)
    print("Topological Ordering:", " -> ".join(topo_res))
    assert topo_res[0] == 'v1'
    assert topo_res[-1] == 'v6'
    print(">> Part 5 Topological Sort verification PASSED.")

    # 6. Unweighted Shortest Path (Assignment 4 Classroom Graph)
    print("\n[PART 6] UNWEIGHTED SHORTEST PATH (10 MARKS - ASSIGNMENT 4 MODEL)")
    # ลำดับ Adjacency List ตรงตามภาพเฉลย 1_Adjacency_List_Answer.jpg 100%
    class_graph = {
        'A': ['B', 'C'],
        'B': ['C', 'E', 'G'],
        'C': ['D', 'E'],
        'D': ['A', 'F'],
        'E': ['D', 'F'],
        'F': [],
        'G': ['E']
    }
    dist_a, path_a, known_a, deq_a, _ = unweighted_shortest_path_trace(class_graph, 'A')
    print("Start Vertex A:")
    print("  Dequeue Order:", " -> ".join(deq_a))
    for v in sorted(class_graph.keys()):
        p_str = reconstruct_path(path_a, 'A', v)
        print(f"  Vertex {v}: Dist = {dist_a[v]}, Path = {path_a[v]} | Route: ({p_str})")

    assert dist_a['A'] == 0
    assert dist_a['B'] == 1 and path_a['B'] == 'A'
    assert dist_a['C'] == 1 and path_a['C'] == 'A'
    assert dist_a['D'] == 2 and path_a['D'] == 'C'
    assert dist_a['E'] == 2 and path_a['E'] == 'B'
    assert dist_a['G'] == 2 and path_a['G'] == 'B'
    assert dist_a['F'] == 3
    assert deq_a == ['A', 'B', 'C', 'E', 'G', 'D', 'F']
    print(">> Part 6 Shortest Path (Start A) verification PASSED.")

    dist_b, path_b, known_b, deq_b, _ = unweighted_shortest_path_trace(class_graph, 'B')
    print("Start Vertex B:")
    print("  Dequeue Order:", " -> ".join(deq_b))
    for v in sorted(class_graph.keys()):
        p_str = reconstruct_path(path_b, 'B', v)
        print(f"  Vertex {v}: Dist = {dist_b[v]}, Path = {path_b[v]} | Route: ({p_str})")

    assert dist_b['B'] == 0
    assert dist_b['C'] == 1 and path_b['C'] == 'B'
    assert dist_b['E'] == 1 and path_b['E'] == 'B'
    assert dist_b['G'] == 1 and path_b['G'] == 'B'
    assert dist_b['D'] == 2 and path_b['D'] == 'C'
    assert dist_b['F'] == 2 and path_b['F'] == 'E'
    assert dist_b['A'] == 3 and path_b['A'] == 'D'
    assert deq_b == ['B', 'C', 'E', 'G', 'D', 'F', 'A']
    print(">> Part 6 Shortest Path (Start B) verification PASSED.")

    # 7. Properties & Calculations
    print("\n[PART 7] PROPERTIES & THEORY CALCULATIONS (10 MARKS)")
    props = calculate_heap_properties()
    for p in props['properties']:
        print(" ", p)

    max_nodes_h4 = calculate_tree_max_nodes(4)
    print(f"Max nodes for height 4: 2^(4+1) - 1 = {max_nodes_h4}")
    assert max_nodes_h4 == 31

    comp_edges_v7 = calculate_complete_graph_edges(7, directed=False)
    print(f"Edges in Undirected Complete Graph (V=7): 7*(6)/2 = {comp_edges_v7}")
    assert comp_edges_v7 == 21

    waste_data = calculate_matrix_waste(7, 12)
    print(f"Sparse Graph 7x7 with 12 edges: Waste = {waste_data['waste_percent']}% | Used = {waste_data['used_percent']}%")
    assert waste_data['waste_percent'] == 75.51
    assert waste_data['used_percent'] == 24.49
    print(">> Part 7 Properties & Theory verification PASSED.")

    print("\n" + "=" * 70)
    print("🎉 ALL 7 FINAL EXAM SECTIONS VERIFIED ACCURATELY WITH 100% SUCCESS!")
    print("=" * 70)
