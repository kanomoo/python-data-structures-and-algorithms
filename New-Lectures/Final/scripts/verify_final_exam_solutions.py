"""
Verification Script for Final Exam 2026
Course: 060243106 / 060223119 Data Structures and Algorithms
Instructor: Dr. Pradit Pitaksatheinkul, KMUTNB
"""

import math
from collections import deque

def verify_all():
    print("==================================================================")
    print("FINAL EXAM 2026: COMPUTATIONAL VERIFICATION SUITE")
    print("==================================================================")

    # ---------------------------------------------------------
    # Question 1: Hashing
    # ---------------------------------------------------------
    print("\n--- QUESTION 1: HASHING VERIFICATION ---")
    M = 19
    R = 17
    rehash_pct = 0.80
    keys = [26, 45, 70, 85, 102, 123, 143, 155]
    table = [None] * M
    info = ['E'] * M
    collisions = {}
    collision_details = {}

    for k in keys:
        h0 = k % M
        step = 0
        visited_slots = []
        while True:
            if step == 0:
                slot = h0
            else:
                f_i = step * (R - (k % R))
                slot = (h0 + f_i) % M
            
            if table[slot] is None:
                table[slot] = k
                info[slot] = 'A'
                collisions[k] = step
                collision_details[k] = visited_slots
                break
            else:
                visited_slots.append(slot)
                step += 1

    print("Final Hash Table (Index: Element [Info]):")
    for i in range(M):
        print(f"  Slot {i:2d}: {str(table[i]):4s} [{info[i]}]")
    
    print("\nCollisions per Key:")
    for k in keys:
        print(f"  Key {k:3d}: {collisions[k]} collision(s) -> Collided at slots: {collision_details[k]}")
    
    total_collisions = sum(collisions.values())
    max_collision_count = max(collisions.values())
    keys_with_max_collisions = [k for k, v in collisions.items() if v == max_collision_count]
    rehash_threshold_count = math.ceil(M * rehash_pct) # 15.2 -> 16
    keys_needed_for_rehash = rehash_threshold_count - len(keys)

    print(f"\n1.2 Key(s) with max collisions: {keys_with_max_collisions} (Each collided {max_collision_count} times)")
    print(f"1.3 Total cumulative collisions: {total_collisions}")
    print(f"1.4 Threshold for 80% Rehash: ceil({M} * 0.8) = {rehash_threshold_count} keys.")
    print(f"    Currently inserted: {len(keys)} keys -> Need {keys_needed_for_rehash} more key(s) to trigger Rehashing.")

    # ---------------------------------------------------------
    # Question 2: Binary Min-Heap
    # ---------------------------------------------------------
    print("\n--- QUESTION 2: BINARY MIN-HEAP VERIFICATION ---")
    class MinHeap:
        def __init__(self):
            self.arr = [None] # 1-based indexing
        def insert(self, val):
            self.arr.append(val)
            hole = len(self.arr) - 1
            while hole > 1 and val < self.arr[hole // 2]:
                self.arr[hole] = self.arr[hole // 2]
                hole //= 2
            self.arr[hole] = val
        def delete_min(self):
            if len(self.arr) <= 1: return None
            min_val = self.arr[1]
            last = self.arr.pop()
            if len(self.arr) > 1:
                hole = 1
                while hole * 2 < len(self.arr):
                    child = hole * 2
                    if child + 1 < len(self.arr) and self.arr[child + 1] < self.arr[child]:
                        child += 1
                    if self.arr[child] < last:
                        self.arr[hole] = self.arr[child]
                        hole = child
                    else:
                        break
                self.arr[hole] = last
            return min_val

    heap = MinHeap()
    q2_inputs = [64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20]
    for x in q2_inputs:
        heap.insert(x)
    print("2.1 Array after inserting 12 elements:")
    print("    Indices 1..12:", heap.arr[1:])
    
    del1 = heap.delete_min()
    print(f"2.2 Array after 1st deleteMin() (removed {del1}):")
    print("    Indices 1..11:", heap.arr[1:])
    
    heap.insert(3)
    print("2.3 Array after insert(3):")
    print("    Indices 1..12:", heap.arr[1:])
    
    del2 = heap.delete_min()
    print(f"2.4 Array after 2nd deleteMin() (removed {del2}):")
    print("    Indices 1..11:", heap.arr[1:])

    # ---------------------------------------------------------
    # Question 3: Insertion Sort
    # ---------------------------------------------------------
    print("\n--- QUESTION 3: INSERTION SORT VERIFICATION ---")
    # 3.1 Worst-case
    worst_input = list(range(12, 0, -1))
    worst_moves = sum(p for p in range(1, 12))
    print(f"3.1 Worst-Case 12 elements: {worst_input}")
    print(f"    Total Position Moves = 12 * 11 / 2 = {worst_moves}")

    # 3.2 Tracing
    arr = [61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]
    print(f"3.2 Initial Array: {arr}")
    for p in range(1, len(arr)):
        tmp = arr[p]
        j = p
        moves = 0
        while j > 0 and arr[j - 1] > tmp:
            arr[j] = arr[j - 1]
            j -= 1
            moves += 1
        arr[j] = tmp
        if p in [3, 6]:
            print(f"    Pass p={p}: Array = {arr}")
            print(f"            Position Moves in pass {p} = {moves}")

    # ---------------------------------------------------------
    # Question 4: Selection Sort & Bubble Sort
    # ---------------------------------------------------------
    print("\n--- QUESTION 4: SELECTION & BUBBLE SORT VERIFICATION ---")
    sel_arr = [64, 25, 12, 22, 11]
    print(f"4.1 Selection Sort initial: {sel_arr}")
    for p in range(len(sel_arr) - 1):
        min_idx = p
        for j in range(p + 1, len(sel_arr)):
            if sel_arr[j] < sel_arr[min_idx]:
                min_idx = j
        sel_arr[p], sel_arr[min_idx] = sel_arr[min_idx], sel_arr[p]
        print(f"    Pass {p+1}: Swapped min element {sel_arr[p]} (from idx {min_idx}) -> Array = {sel_arr}")

    bub_arr = [54, 26, 93, 17, 77]
    print(f"\n4.2 Bubble Sort initial: {bub_arr}")
    total_swaps = 0
    total_comparisons = 0
    for p in range(len(bub_arr) - 1):
        swapped = False
        print(f"    Pass {p+1}:")
        for j in range(len(bub_arr) - 1 - p):
            total_comparisons += 1
            if bub_arr[j] > bub_arr[j + 1]:
                bub_arr[j], bub_arr[j + 1] = bub_arr[j + 1], bub_arr[j]
                swapped = True
                total_swaps += 1
        print(f"      State after pass {p+1}: {bub_arr} (Swapped: {swapped})")
        if not swapped:
            print("      Early termination triggered!")
            break
    print(f"    Total Comparisons = {total_comparisons}, Total Swaps = {total_swaps}")

    # ---------------------------------------------------------
    # Question 5: Topological Sort
    # ---------------------------------------------------------
    print("\n--- QUESTION 5: TOPOLOGICAL SORT VERIFICATION ---")
    adj_topo = {
        1: [4, 3],
        2: [4, 6, 1],
        3: [4],
        4: [6],
        5: [6, 7],
        6: [],
        7: [6, 2]
    }
    indeg = {v: 0 for v in range(1, 8)}
    for u, neighbors in adj_topo.items():
        for v in neighbors:
            indeg[v] += 1
    print("Initial In-degrees:", indeg)
    
    # Trace rounds
    q_topo = [v for v in range(1, 8) if indeg[v] == 0]
    print("Initial Queue (In-degree == 0):", q_topo)
    topo_order = []
    round_history = []
    
    # Store initial state for table
    round_history.append(dict(indeg))
    
    while q_topo:
        curr = q_topo.pop(0)
        topo_order.append(curr)
        for nxt in adj_topo[curr]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q_topo.append(nxt)
        round_history.append(dict(indeg))
        
    print(f"5.3 Resulting Topological Ordering: {topo_order}")

    # ---------------------------------------------------------
    # Question 6: Unweighted Shortest Path
    # ---------------------------------------------------------
    print("\n--- QUESTION 6: UNWEIGHTED SHORTEST PATH VERIFICATION ---")
    adj_sp = {
        1: [4, 3, 2, 6],
        2: [3, 4, 5, 6, 7],
        3: [4, 5, 1],
        4: [6, 5],
        5: [6],
        6: [3],
        7: [1, 6]
    }
    dist = {v: 999 for v in range(1, 8)}
    path = {v: 0 for v in range(1, 8)}
    known = {v: False for v in range(1, 8)}
    
    q_sp = deque([1])
    dist[1] = 0
    path[1] = 0
    
    while q_sp:
        v = q_sp.popleft()
        known[v] = True
        for w in adj_sp[v]:
            if dist[w] == 999:
                dist[w] = dist[v] + 1
                path[w] = v
                q_sp.append(w)
                
    print("Final Shortest Path Table:")
    for v in range(1, 8):
        print(f"  Vertex {v}: Known={known[v]}, Dist={dist[v]}, Path={path[v]}")
        
    # Backtrack shortest paths
    print("\nReconstructed Shortest Paths from Vertex 1:")
    for target in range(1, 8):
        curr = target
        route = [curr]
        while curr != 1 and path[curr] != 0:
            curr = path[curr]
            route.append(curr)
        route.reverse()
        route_str = ", ".join(f"v{node}" for node in route)
        print(f"  Path to v{target}: {route_str} (Length: {dist[target]})")

    # ---------------------------------------------------------
    # Question 7: Theory & Formulas
    # ---------------------------------------------------------
    print("\n--- QUESTION 7: ADVANCED THEORY & FORMULAS VERIFICATION ---")
    v_count = 7
    e_count = 12
    matrix_cells = v_count * v_count
    active_pct = (e_count / matrix_cells) * 100
    waste_pct = 100 - active_pct
    print(f"7.2 Memory Waste in Adjacency Matrix (V={v_count}, E={e_count}):")
    print(f"    Matrix size: {matrix_cells} cells")
    print(f"    Used cells (1s): {e_count} / {matrix_cells} = {active_pct:.2f}% (approx 24.48% - 24.49%)")
    print(f"    Wasted cells (0s): {matrix_cells - e_count} / {matrix_cells} = {waste_pct:.2f}% (approx 75.51%)")
    print(f"    Adjacency List requirement: |V| + |E| = {v_count + e_count} cells")
    
    v_comp = 16
    comp_edges = (v_comp * (v_comp - 1)) // 2
    print(f"\n7.3 Complete Graph K_16 Edges: 16 * 15 / 2 = {comp_edges} edges")
    
    h = 16
    min_nodes = 2**h
    max_nodes = 2**(h + 1) - 1
    print(f"\n7.4 Complete Binary Tree (h={h}):")
    print(f"    Min nodes = 2^{h} = {min_nodes:,}")
    print(f"    Max nodes = 2^{h+1} - 1 = {max_nodes:,}")

    print("\n==================================================================")
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY WITHOUT ERROR!")
    print("==================================================================")

if __name__ == '__main__':
    verify_all()
