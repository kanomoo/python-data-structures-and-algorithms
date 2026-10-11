# KMUTNB Data Structures & Algorithms - Final Examination 2026 Master Guide
**Course Code:** 060243106 / 060223119 | **Instructor:** Assoc. Prof. Dr. Pradit Pitaksatheinkul  
**Department of Computer and Information Science, Faculty of Applied Science, KMUTNB**

---

## 1. Executive Summary & Examination Blueprint

### 1.1 Overview & Grading Criteria
* **Total Raw Score:** 70 Marks (Calculated as $\frac{\text{Raw Score}}{2} = 35\%$ of total semester grade).
* **Duration:** 3 Hours (180 Minutes).
* **Permitted Materials:** Open-book (Textbooks, printed lecture slides, handwritten notes, scientific calculator). Mobile phones, tablets, smart watches, and internet access are **strictly prohibited**.
* **Language Requirement:** All official examination questions are formatted in **English**, accompanied by complete Thai translations (`thai-trans`) and rigorous step-by-step principles.

### 1.2 Verification Sources
This master guide and its accompanying exam suite are synthesized directly from:
1. **Audio Lecture Transcripts (Complete Verbatim Records):**
   - Recording dated October 7, 2026 (`20261007_092525.txt`): Exam scope announcement by Dr. Pradit.
   - Recording dated September 2, 2026 (`20260902_112213.txt`, `20260902_112628.txt`, `20260902_113741.txt`): Binary Heap array mapping, `hole` variable tracing, and Complete Binary Tree node count at height $H=10$.
   - Recording dated September 9, 2026 (`dsa20260909_092303.txt`): `insert(14)` tracing, `deleteMin()` 3-pass chaining, and zero-parameter method calling syntax.
   - Recording dated September 23, 2026 (`20260923_091645.txt`): Graph theory, complete graph edge count ($K_{10}, K_{16}$), memory waste percentage of Adjacency Matrix ($7 \times 7$), and comma-separated path rules.
2. **Classroom Screen Captures & Whiteboard Photos:**
   - [`838089388_1415326226689667_7275141095890058178_n.jpg`](file:///C:/Project/python-data-structures-and-algorithms/final/sources/whiteboard_photos/838089388_1415326226689667_7275141095890058178_n.jpg): Shortest Path Graph (7 vertices, 12 directed edges).
   - [`840922631_2536514460095565_4007011001871590815_n.jpg`](file:///C:/Project/python-data-structures-and-algorithms/final/sources/whiteboard_photos/840922631_2536514460095565_4007011001871590815_n.jpg): Topological Sort Graph (7 vertices, 12 directed edges, DAG).
   - 9 Live Classroom Exam Screenshots (`Screenshot 2026-09-09 011621.png` to `011759.png`): 3 Ideal hash properties, perfect square collisions, wrap around, double hashing $R$ selection, and array-to-tree conversion.
3. **Past Examination Benchmarks:**
   - [00_ข้อสอบปลายภาคจริงปี2564_พร้อมเฉลยและลายมือรุ่นพี่_FinalExam2564_อ_ประดิษฐ์.pdf](file:///C:/Project/python-data-structures-and-algorithms/final/sources/past_exams/00_ข้อสอบปลายภาคจริงปี2564_พร้อมเฉลยและลายมือรุ่นพี่_FinalExam2564_อ_ประดิษฐ์.pdf)
   - [DataStrucFinal2-xxAnd2-61-1.pdf](file:///C:/Project/python-data-structures-and-algorithms/final/sources/past_exams/DataStrucFinal2-xxAnd2-61-1.pdf)
4. **Computational Proof Script:** [`verify_final_exam_solutions.py`](file:///C:/Project/python-data-structures-and-algorithms/final/scripts/verify_final_exam_solutions.py) confirming exact values for all 7 problems mathematically.
5. **Dedicated Graph Classroom Master Summary:** [สรุปเนื้อหากราฟ_Graph_Master_Classroom_Summary.html](file:///C:/Project/python-data-structures-and-algorithms/final/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B%E0%B9%80%E0%B8%99%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%81%E0%B8%A3%E0%B8%B2%E0%B8%9F_Graph_Master_Classroom_Summary.html) synthesizing all graph lectures, memory waste math, and BFS/TopSort problems.

---

## 2. Examination Structure: 2026 vs. Past Years

| Question | Topic | 2026 Leaked Parameters | 2564 / 2561 Historical Context | Dr. Pradit's Grading Pitfalls |
| :--- | :--- | :--- | :--- | :--- |
| **Q1 (10 pts)** | **Hashing** | Double Hashing: $h_0(X) = X \bmod 19$<br>$f(i) = i \times (17 - (X \bmod 17))$<br>TableSize = 19, Rehash @ 80% (16 keys)<br>Keys: `26, 45, 70, 85, 102, 123, 143, 155` | Older years used TableSize = 17 or 13, $R = 13$ or $7$. | Must record probe calculations ($h_0, f(i)$) explicitly. Max collisions: 85, 102, 123 (2 collisions each). Total = 9 collisions. |
| **Q2 (10 pts)** | **Binary Min-Heap** | 12 Keys: `64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20`<br>Sequential Inserts $\rightarrow$ `deleteMin()` $\rightarrow$ Insert `3` $\rightarrow$ `deleteMin()`. | Past papers used 10–12 keys with Max-Heap or Min-Heap. | **Index 0 is unused (`arr[0] = -`)**. Formulas: Left = $2i$, Right = $2i+1$, Parent = $\lfloor i/2 \rfloor$. Must state the 2 fundamental properties. |
| **Q3 (10 pts)** | **Insertion Sort** | 3.1: Worst-case formula ($N=12$, descending) $\rightarrow$ 66 moves.<br>3.2: Tracing array `[61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]`. Moves for Pass $p=3$ (2 moves) and $p=6$ (3 moves). | Exact identical question style to 2564 Q3. | "Position moves" means shifts. Worst case is $\frac{N(N-1)}{2}$. |
| **Q4 (10 pts)** | **Selection & Bubble Sort** | **MAJOR CHANGE**: Quicksort is replaced by Selection Sort (Pass-by-pass) and Bubble Sort (Early termination tracking). | Older years (2561, 2564) tested Quicksort partitioning and median-of-three. | For Selection Sort: track minimum index and swap. For Bubble Sort: track adjacent comparisons and swaps; state pass when sorted (Pass 5). |
| **Q5 (10 pts)** | **Topological Sort** | 7-Vertex DAG (from whiteboard photo `840922631...`).<br>Adjacency List + Indegree table (Round 1 to 7) + Circular Queue (Size 7, 0-indexed). | Identical structure to 2564 Q5. | Circular Queue `front` and `back` pointers must be tracked carefully ($(\text{ptr}+1) \bmod 7$). Output: `5, 7, 2, 1, 3, 4, 6`. |
| **Q6 (10 pts)** | **Unweighted Shortest Path** | 7-Vertex Directed Graph (from photo `838089388...`).<br>Table tracking `Known`, `dv`, `pv` starting from vertex 1.<br>Shortest paths to $v_5$ and $v_7$. | Assignment 4 & 2564 Q6. | **CRITICAL TRAP:** Writing arrows like `1 -> 4 -> 5` results in **0 marks**. Must write comma-separated: `1, 4, 5`. Path length is edge count (2), not vertex count. |
| **Q7 (10 pts)** | **Theory & Calculations** | 1. Structure with 2 properties vs 3 properties.<br>2. 3 Ideal Hash properties & impossible one.<br>3. Memory waste percentage of Adjacency Matrix ($7 \times 7 = 49$, waste 75.51%).<br>4. Complete graph $K_{16}$ edges = 120.<br>5. Complete binary tree height $h=16$ min/max nodes (65,536 / 131,071).<br>6. Binary heap child/parent index formulas. | Combines theoretical questions seen in 2561 and 2564. | **Answers MUST be calculated integers** (e.g. 120, 65536, 131071), NOT raw mathematical formulas. |

---

## 3. Leaked Examination Questions (Official English Specification)

### Question 1: Hashing & Open Addressing (18 Marks)
Given an empty hash table of size $\text{TableSize} = 19$ (indices $0$ to $18$), using **Open Addressing** with **Double Hashing**:
$$\text{Primary Hash Function: } h_0(X) = X \bmod 19$$
$$\text{Collision Function: } f(i) = i \times (17 - (X \bmod 17)) \quad \text{for probe } i = 0, 1, 2, \dots$$
$$\text{Probe Sequence: } h_i(X) = (h_0(X) + f(i)) \bmod 19$$

**Keys to insert sequentially:**
$$26, 45, 70, 85, 102, 123, 143, 155$$

**Sub-Questions:**
1. **1.1 (8 Marks):** Show the probe calculation for each key and fill the resulting hash table.
2. **1.2 (3 Marks: 1+1+1):** Which key(s) experienced the maximum number of collisions during insertion? How many collisions did they experience, and at which cell locations?  
   *Answer:* `85, 102, 123` (Each 2 collisions: 85 at slots 9, 7 | 102 at slots 7, 5 | 123 at slots 9, 3)
3. **1.3 (3 Marks):** What is the total cumulative number of collisions and resolution steps that occurred during the insertion of all 8 keys? *(Count each collision step as 1).*  
   *Answer:* `9 collisions`
4. **1.4 (4 Marks):** If rehashing is triggered when the load factor reaches $\lambda \ge 80\%$, how many more keys must be inserted before rehashing occurs?  
   *Answer:* `8 more keys` ($\lceil 19 \times 0.8 \rceil = 16 \rightarrow 16 - 8 = 8$)

---

### Question 2: Priority Queue (Binary Min-Heap) (10 Marks)
Given an empty Binary Min-Heap represented as a 1-based array (index $0$ is unused).

**Keys to insert sequentially:**
$$64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20$$

**Tasks:**
1. State the **two fundamental properties** of a Binary Min-Heap.
2. Show the tree and the array after inserting all 12 keys.
3. Perform `deleteMin()`. Show the resulting tree and array.
4. Insert key `3`. Show the resulting tree and array.
5. Perform `deleteMin()`. Show the final tree and array.

---

### Question 3: Insertion Sort Tracing & Position Moves (10 Marks)
1. **(3 Marks)** If an array of size $N = 12$ contains elements in descending order (worst case):
   $$[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]$$
   Calculate the total number of position moves (element shifts + insertion) required to sort the array into ascending order. State the formula.
2. **(7 Marks)** Given the array:
   $$[61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]$$
   - Trace the array state after each pass ($p = 1$ to $11$).
   - State the number of position moves during **Pass $p = 3$** (key $24$).
   - State the number of position moves during **Pass $p = 6$** (key $32$).

---

### Question 4: Selection Sort & Bubble Sort Tracing (10 Marks)
Given the unsorted array of 8 elements:
$$[45, 18, 72, 31, 12, 88, 25, 60]$$

1. **(5 Marks) Selection Sort:**
   - Trace the array state at each pass ($p = 1$ to $7$).
   - In each pass, identify the minimum element in the unsorted subarray and the swap performed.
   - What is the total number of swaps executed?
2. **(5 Marks) Bubble Sort:**
   - Trace the array state at each pass until sorted.
   - Explain how the algorithm detects early termination when no swaps occur.
   - State the pass number at which the algorithm terminates.

---

### Question 5: Topological Sort (10 Marks)
Given the Directed Acyclic Graph (DAG) $G = (V, E)$ with 7 vertices ($V = \{1, 2, 3, 4, 5, 6, 7\}$) defined by the Adjacency List:
* $v_1 \rightarrow 3, 4$
* $v_2 \rightarrow 1$
* $v_3 \rightarrow 4, 6$
* $v_4 \rightarrow 6$
* $v_5 \rightarrow 1, 2, 7$
* $v_6 \rightarrow \emptyset$
* $v_7 \rightarrow 2$

**Tasks:**
1. Complete the Indegree tracking table for all vertices across all rounds (Initial to Round 7).
2. Trace the Circular Queue of size 7 (indices $0$ to $6$, 0-based indexing) showing the contents, `front`, and `back` pointers at each step.
3. State the final valid Topological Ordering sequence.

---

### Question 6: Unweighted Shortest Path (10 Marks)
Given the directed graph $G = (V, E)$ with 7 vertices ($V = \{1, 2, 3, 4, 5, 6, 7\}$) defined by the Adjacency List:
* $v_1 \rightarrow 2, 4$
* $v_2 \rightarrow 4, 5, 7$
* $v_3 \rightarrow 1, 6$
* $v_4 \rightarrow 3, 5, 6, 7$
* $v_5 \rightarrow 7$
* $v_6 \rightarrow \emptyset$
* $v_7 \rightarrow 6$

**Tasks:**
1. Execute the Unweighted Shortest Path algorithm (BFS) using **Source Vertex = 1**. Fill the table tracking `Known`, $d_v$ (shortest distance), and $p_v$ (previous vertex) for all vertices across all rounds.
2. State the shortest path and path length from vertex $1$ to **vertex $5$**.
3. State the shortest path and path length from vertex $1$ to **vertex $7$**.

*(Note: Follow the strict output formatting rules specified by the instructor: comma-separated list, NO arrows).*

---

### Question 7: Properties & Theory Calculations (10 Marks)
Answer the following questions with exact calculations and justifications:
1. **(1 Mark)** Name a data structure that has **2 fundamental properties**.
2. **(1 Mark)** Name a data structure that has **3 fundamental properties**.
3. **(2 Marks)** State the **3 ideal properties** of a hash function, and identify which one is impossible to guarantee in practical applications and why.
4. **(2 Marks)** For a graph with $|V| = 7$ vertices and $|E| = 12$ directed edges:
   - What is the percentage of memory used and wasted in an Adjacency Matrix?
   - How much memory does an Adjacency List save compared to the Adjacency Matrix?
5. **(1 Mark)** What is the total number of edges in a complete undirected graph $K_{16}$? Calculate the exact integer value.
6. **(1 Mark)** In a complete binary tree of height $h = 16$ (where root height = 0), what are the minimum and maximum possible numbers of nodes? Calculate exact integer values.
7. **(2 Marks)** In a Binary Heap implemented as a 1-based array, write the index formulas for:
   - Left child of node at index $i$
   - Right child of node at index $i$
   - Parent of node at index $i$

---

## 4. Master Solutions & Step-by-Step Proofs

### Solution 1: Hashing
* **Table Size:** $M = 19$, Hash functions: $h_0(X) = X \bmod 19$, step $s(X) = 17 - (X \bmod 17)$, probe $h_i(X) = (h_0(X) + i \cdot s(X)) \bmod 19$.

#### Key-by-Key Probe Tracing:
1. **Key 26:** $h_0(26) = 26 \bmod 19 = 7$. Slot 7 is empty $\rightarrow$ Insert at **Index 7** (0 collisions).
2. **Key 45:** $h_0(45) = 45 \bmod 19 = 7$ (collision 1). $s(45) = 17 - 11 = 6$.  
   $i=1: (7 + 6) \bmod 19 = 13$. Slot 13 is empty $\rightarrow$ Insert at **Index 13** (1 collision).
3. **Key 70:** $h_0(70) = 70 \bmod 19 = 13$ (collision 1). $s(70) = 17 - 2 = 15$.  
   $i=1: (13 + 15) \bmod 19 = 9$. Slot 9 empty $\rightarrow$ Insert at **Index 9** (1 collision).
4. **Key 85:** $h_0(85) = 85 \bmod 19 = 9$ (collision 1). $s(85) = 17 - 0 = 17$.  
   $i=1: (9 + 17) \bmod 19 = 7$ (collision 2).  
   $i=2: (9 + 34) \bmod 19 = 5$. Slot 5 empty $\rightarrow$ Insert at **Index 5** (2 collisions).
5. **Key 102:** $h_0(102) = 102 \bmod 19 = 7$ (collision 1). $s(102) = 17 - 0 = 17$.  
   $i=1: (7 + 17) \bmod 19 = 5$ (collision 2).  
   $i=2: (7 + 34) \bmod 19 = 3$. Slot 3 empty $\rightarrow$ Insert at **Index 3** (2 collisions).
6. **Key 123:** $h_0(123) = 123 \bmod 19 = 9$ (collision 1). $s(123) = 17 - 4 = 13$.  
   $i=1: (9 + 13) \bmod 19 = 3$ (collision 2).  
   $i=2: (9 + 26) \bmod 19 = 16$. Slot 16 empty $\rightarrow$ Insert at **Index 16** (2 collisions).
7. **Key 143:** $h_0(143) = 143 \bmod 19 = 10$. Slot 10 empty $\rightarrow$ Insert at **Index 10** (0 collisions).
8. **Key 155:** $h_0(155) = 155 \bmod 19 = 3$ (collision 1). $s(155) = 17 - 2 = 15$.  
   $i=1: (3 + 15) \bmod 19 = 18$. Slot 18 empty $\rightarrow$ Insert at **Index 18** (1 collision).

#### Hash Table State:
| Index | Key | Index | Key | Index | Key | Index | Key |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | - | 5 | 85 (2) | 10 | 143 (0) | 15 | - |
| 1 | - | 6 | - | 11 | - | 16 | 123 (2) |
| 2 | - | 7 | 26 (0) | 12 | - | 17 | - |
| 3 | 102 (2) | 8 | - | 13 | 45 (1) | 18 | 155 (1) |
| 4 | - | 9 | 70 (1) | 14 | - | | |

* **Total Collisions:** $0 + 1 + 1 + 2 + 2 + 2 + 0 + 1 = \mathbf{9}$ collisions.
* **Keys with Maximum Collisions:** **85, 102, 123** (each experienced 2 collisions).
* **Rehashing Calculation:** Threshold $= \lceil 19 \times 0.80 \rceil = 16$ keys. Current keys $= 8$. Remaining keys before rehash $= 16 - 8 = \mathbf{8}$ keys.

---

### Solution 2: Binary Min-Heap
#### 1. Two Fundamental Properties:
1. **Structure Property:** Complete Binary Tree (all levels filled except possibly the bottom, filled from left to right).
2. **Heap-Order Property:** For every node $X$ with parent $P$, $\text{key}(P) \le \text{key}(X)$ (root contains the minimum key).

#### 2. Sequential Insertions (12 Keys):
* **Array 2.1 (After inserting 12 keys):**  
  `arr[1..12] = [1, 6, 2, 10, 8, 20, 5, 64, 14, 20, 15, 24]`
* **Array 2.2 (After 1st deleteMin()):**  
  Root 1 extracted. Last element 24 placed at root. Percolates down through 2 and 5:  
  `arr[1..11] = [2, 6, 5, 10, 8, 20, 24, 64, 14, 20, 15]`
* **Array 2.3 (After inserting key 3):**  
  Key 3 appended at index 12. Percolates up through 20 and 5:  
  `arr[1..12] = [2, 6, 3, 10, 8, 5, 24, 64, 14, 20, 15, 20]`
* **Array 2.4 (After 2nd deleteMin()):**  
  Root 2 extracted. Last element 20 placed at root. Percolates down through 3 and 5:  
  `arr[1..11] = [3, 6, 5, 10, 8, 20, 24, 64, 14, 20, 15]`

---

### Solution 3: Insertion Sort Tracing & Position Moves
#### 3.1 Worst-Case Calculation:
* Array: descending $[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]$ ($N = 12$).
* Formula:
  $$\text{Total Moves} = \sum_{p=1}^{N-1} p = \frac{N(N-1)}{2} = \frac{12 \times 11}{2} = \mathbf{66} \text{ moves}$$

#### 3.2 Given Array Tracing:
Given: `[61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]`
* **Pass $p=1$ (key 52):** moves: 1 $\rightarrow$ `[52, 61, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]`
* **Pass $p=2$ (key 12):** moves: 2 $\rightarrow$ `[12, 52, 61, 24, 8, 35, 32, 5, 71, 68, 18, 2]`
* **Pass $p=3$ (key 24):** moves: 2 $\rightarrow$ `[12, 24, 52, 61, 8, 35, 32, 5, 71, 68, 18, 2]` &bull; **Answer: 2 moves**
* **Pass $p=4$ (key 8):** moves: 4 $\rightarrow$ `[8, 12, 24, 52, 61, 35, 32, 5, 71, 68, 18, 2]`
* **Pass $p=5$ (key 35):** moves: 2 $\rightarrow$ `[8, 12, 24, 35, 52, 61, 32, 5, 71, 68, 18, 2]`
* **Pass $p=6$ (key 32):** moves: 3 $\rightarrow$ `[8, 12, 24, 32, 35, 52, 61, 5, 71, 68, 18, 2]` &bull; **Answer: 3 moves**
* **Pass $p=7$ (key 5):** moves: 7 $\rightarrow$ `[5, 8, 12, 24, 32, 35, 52, 61, 71, 68, 18, 2]`
* **Pass $p=8$ (key 71):** moves: 0 $\rightarrow$ `[5, 8, 12, 24, 32, 35, 52, 61, 71, 68, 18, 2]`
* **Pass $p=9$ (key 68):** moves: 1 $\rightarrow$ `[5, 8, 12, 24, 32, 35, 52, 61, 68, 71, 18, 2]`
* **Pass $p=10$ (key 18):** moves: 7 $\rightarrow$ `[5, 8, 12, 18, 24, 32, 35, 52, 61, 68, 71, 2]`
* **Pass $p=11$ (key 2):** moves: 11 $\rightarrow$ `[2, 5, 8, 12, 18, 24, 32, 35, 52, 61, 68, 71]`

---

### Solution 4: Selection Sort & Bubble Sort
Given: `[45, 18, 72, 31, 12, 88, 25, 60]` ($N = 8$)

#### 4.1 Selection Sort Tracing:
* Pass 1: Min is 12 (idx 4) $\rightarrow$ swap with idx 0 $\rightarrow$ `[12, 18, 72, 31, 45, 88, 25, 60]` (Swap 1)
* Pass 2: Min is 18 (idx 1) $\rightarrow$ already at position
* Pass 3: Min is 25 (idx 6) $\rightarrow$ swap with idx 2 $\rightarrow$ `[12, 18, 25, 31, 45, 88, 72, 60]` (Swap 2)
* Pass 4: Min is 31 (idx 3) $\rightarrow$ already at position
* Pass 5: Min is 45 (idx 4) $\rightarrow$ already at position
* Pass 6: Min is 60 (idx 7) $\rightarrow$ swap with idx 5 $\rightarrow$ `[12, 18, 25, 31, 45, 60, 72, 88]` (Swap 3)
* Pass 7: Min is 72 (idx 6) $\rightarrow$ already at position
* **Total Swaps:** 3 active value-exchanging swaps.

#### 4.2 Bubble Sort Tracing & Early Termination:
* Pass 1: 5 swaps $\rightarrow$ `[18, 45, 31, 12, 72, 25, 60, 88]`
* Pass 2: 4 swaps $\rightarrow$ `[18, 31, 12, 45, 25, 60, 72, 88]`
* Pass 3: 2 swaps $\rightarrow$ `[18, 12, 31, 25, 45, 60, 72, 88]`
* Pass 4: 2 swaps $\rightarrow$ `[12, 18, 25, 31, 45, 60, 72, 88]`
* Pass 5: **0 swaps occurred!**
* **Early Termination:** Boolean flag `swapped == False` at end of pass detects that array is already sorted, terminating algorithm at **Pass 5**.

---

### Solution 5: Topological Sort
#### Graph $G = (V, E)$:
$v_1 \rightarrow 3, 4$; $v_2 \rightarrow 1$; $v_3 \rightarrow 4, 6$; $v_4 \rightarrow 6$; $v_5 \rightarrow 1, 2, 7$; $v_6 \rightarrow \emptyset$; $v_7 \rightarrow 2$.

#### 1. Indegree Table:
| Vertex | Initial | Round 1 (v=5) | Round 2 (v=7) | Round 3 (v=2) | Round 4 (v=1) | Round 5 (v=3) | Round 6 (v=4) | Round 7 (v=6) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2 | 1 | 1 | **0** | 0 | 0 | 0 | 0 |
| **2** | 2 | 1 | **0** | 0 | 0 | 0 | 0 | 0 |
| **3** | 1 | 1 | 1 | 1 | **0** | 0 | 0 | 0 |
| **4** | 2 | 2 | 2 | 2 | 1 | **0** | 0 | 0 |
| **5** | **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **6** | 2 | 2 | 2 | 2 | 2 | 1 | **0** | 0 |
| **7** | 1 | **0** | 0 | 0 | 0 | 0 | 0 | 0 |

#### 2. Circular Queue Tracing (Size = 7, indices 0..6):
* Initial: Enqueue 5 $\rightarrow$ `[5, -, -, -, -, -, -]`, `front=0, back=0`
* R1: Dequeue 5 (`front=1`), Enqueue 7 $\rightarrow$ `[5, 7, -, -, -, -, -]`, `back=1`
* R2: Dequeue 7 (`front=2`), Enqueue 2 $\rightarrow$ `[5, 7, 2, -, -, -, -]`, `back=2`
* R3: Dequeue 2 (`front=3`), Enqueue 1 $\rightarrow$ `[5, 7, 2, 1, -, -, -]`, `back=3`
* R4: Dequeue 1 (`front=4`), Enqueue 3 $\rightarrow$ `[5, 7, 2, 1, 3, -, -]`, `back=4`
* R5: Dequeue 3 (`front=5`), Enqueue 4 $\rightarrow$ `[5, 7, 2, 1, 3, 4, -]`, `back=5`
* R6: Dequeue 4 (`front=6`), Enqueue 6 $\rightarrow$ `[5, 7, 2, 1, 3, 4, 6]`, `back=6`
* R7: Dequeue 6 (`front=0`) $\rightarrow$ Queue empty.
* **Topological Ordering:** $\mathbf{5, 7, 2, 1, 3, 4, 6}$

---

### Solution 6: Unweighted Shortest Path
* Source Vertex = 1.

#### 1. BFS Tracing Table:
| Vertex | Initial | Round 1 (v=1) | Round 2 (v=2) | Round 3 (v=4) | Round 4 (v=5) | Round 5 (v=7) | Round 6 (v=3) | Round 7 (v=6) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | F, 0, 0 | **T, 0, 0** | T, 0, 0 | T, 0, 0 | T, 0, 0 | T, 0, 0 | T, 0, 0 | T, 0, 0 |
| **2** | F, $\infty$, 0 | F, 1, 1 | **T, 1, 1** | T, 1, 1 | T, 1, 1 | T, 1, 1 | T, 1, 1 | T, 1, 1 |
| **3** | F, $\infty$, 0 | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 4 | F, 2, 4 | F, 2, 4 | **T, 2, 4** | T, 2, 4 |
| **4** | F, $\infty$, 0 | F, 1, 1 | F, 1, 1 | **T, 1, 1** | T, 1, 1 | T, 1, 1 | T, 1, 1 | T, 1, 1 |
| **5** | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 2 | F, 2, 2 | **T, 2, 2** | T, 2, 2 | T, 2, 2 | T, 2, 2 |
| **6** | F, $\infty$, 0 | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 4 | F, 2, 4 | F, 2, 4 | F, 2, 4 | **T, 2, 4** |
| **7** | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 2 | F, 2, 2 | F, 2, 2 | **T, 2, 2** | T, 2, 2 | T, 2, 2 |

#### 2. Shortest Paths:
* Shortest Path to $v_5$: $\mathbf{1, 4, 5}$ (or $1, 2, 5$) &bull; **Length = 2 edges**
* Shortest Path to $v_7$: $\mathbf{1, 2, 7}$ (or $1, 4, 7$) &bull; **Length = 2 edges**

> [!CAUTION]
> **DR. PRADIT'S ZERO-MARK ARROW TRAP:**
> Must write comma-separated sequence: `1, 4, 5`. **NEVER write arrows like `1 -> 4 -> 5`** (instant 0 marks). Path length is number of edges (2).

---

### Solution 7: Properties & Theory Calculations
1. **2 Properties:** **Binary Heap** (Structure Property & Heap-Order Property).
2. **3 Properties:** **AVL Tree** (BST order, Binary tree structure, Height-Balance $|\Delta h| \le 1$).
3. **Ideal Hash Properties:** Uniform distribution, Deterministic, $O(1)$ evaluation.  
   *Impossible in reality:* Uniform collision-free distribution due to **Pigeonhole Principle** ($|U| \gg M$) and input key clustering.
4. **Memory Waste ($V=7, E=12$):**  
   Adjacency Matrix ($7 \times 7 = 49$): Used $= 12/49 = \mathbf{24.49\%}$, Wasted $= 37/49 = \mathbf{75.51\%}$.  
   Adjacency List uses $7 + 12 = \mathbf{19 \text{ slots}}$ (saves **61.22%** memory).
5. **Edges in Complete Graph $K_{16}$:** $\frac{16 \times 15}{2} = \mathbf{120 \text{ edges}}$ (must write integer 120).
6. **Complete Binary Tree Height $h=16$ Nodes:**  
   Min $= 2^{16} = \mathbf{65,536 \text{ nodes}}$ &bull; Max $= 2^{17} - 1 = \mathbf{131,071 \text{ nodes}}$ (must write integer).
7. **Heap Formulas (1-based array):**  
   Left child $= \mathbf{2i}$, Right child $= \mathbf{2i + 1}$, Parent $= \mathbf{\lfloor i/2 \rfloor}$ (Python `//`).

---

## 5. Classroom Short Essay Leaks & Theory Deep-Dive

### 5.1 หลักการ Map ของ Binary Heap (Complete Binary Tree to 1D Array)
* **ทำไมถึง Map เป็น Array ได้โดยไม่ต้องใช้ Pointer:**  
  เพราะ Complete Binary Tree มีโครงสร้างสมบูรณ์แบบที่แน่นหนาเต็มทุกชั้น ยกเว้นชั้นล่างสุดที่ต้องชิดซ้าย (Regular and dense structure) ทำให้ไม่มีช่องว่างโหว่ (No gaps) จึงสามารถแปลงลำดับแบบ Level-Order (บนลงล่าง ซ้ายไปขวา) เก็บในช่องอาร์เรย์ที่ต่อเนื่องกันได้ทันที
* **ประโยชน์สูงสุด:**  
  1) ขจัด Pointer Overhead ประหยัดหน่วยความจำ  
  2) สมาชิกอยู่ในหน่วยความจำที่ต่อเนื่องกัน ทำให้แคชของ CPU ทำงานได้อย่างรวดเร็ว (Cache Locality)
* **ทำไมต้องเว้น Index 0 ไว้ (`self.array[0] = None` หรือ `-`):**  
  เพื่อให้ความสัมพันธ์ทางคณิตศาสตร์สอดคล้องอย่างสมบูรณ์แบบ:
  - ลูกซ้าย: $2i$ (ใช้บิตชิฟต์ซ้าย `i << 1`)
  - ลูกขวา: $2i + 1$
  - พ่อแม่: $\lfloor i/2 \rfloor$ (ใช้บิตชิฟต์ขวา `i >> 1`)  
  หากเริ่มที่ Index 0 สูตรจะกลายเป็น $2i+1, 2i+2, \lfloor (i-1)/2 \rfloor$ ซึ่งต้องเสียเวลาคำนวณ Offset ในคอมพิวเตอร์
* **กฎการตัดเศษทศนิยมในการหา Parent:**  
  ตำแหน่งของอาร์เรย์ต้องเป็นจำนวนเต็มเท่านั้น ดังนั้นเมื่อนำดัชนีมาหาร 2 แล้วได้ทศนิยม **ให้ตัดเศษทิ้งเสมอ (Truncate fraction) ห้ามปัดขึ้นเด็ดขาด!** (เช่น โหนด $i=7$: $7/2 = 3.5 \rightarrow \mathbf{3}$, ในภาษา Python ใช้ `7 // 2 = 3`)

### 5.2 การ Trace ฟังก์ชัน `insert(x)` ด้วยตัวแปร `hole`
* **การขยายหลุม:** `self.currentSize += 1`, `hole = self.currentSize`
* **เงื่อนไขลูป:** `while hole > 1 and x < self.array[hole // 2]:`
* **การเลื่อน Parent ลงมาแทนที่หลุม:** `self.array[hole] = self.array[hole // 2]`, `hole = hole // 2`
* **การบรรจุค่า:** `self.array[hole] = x`
* **สิ่งที่ต้องเขียนตอบในข้อสอบแต่ละรอบ:**  
  1) ค่าในตัวแปร `hole`  
  2) การเปรียบเทียบในเงื่อนไข `while` (เช่น $14 < 31 \rightarrow$ True, $14 < 21 \rightarrow$ True, $14 < 13 \rightarrow$ False)

### 5.3 ไวยากรณ์การเรียกเมธอด `deleteMin()` ใน Python
* เมธอด `deleteMin()` **ไม่มีการรับพารามิเตอร์ใดๆ ทั้งสิ้น** (No arguments)
* ❌ ห้ามเขียน: `myheap.deleteMin(13)` (ได้ 0 คะแนนทันที)
* ✅ เขียน: `myheap.deleteMin()` เพราะลบตัวรากเสมอ

### 5.4 นิยามภาษาอังกฤษของหลักการ Wrap Around ใน Hashing
* *"When the key was mapped to the last index of hash table, it goes back to the first index of hash table by mod tablesize one more time."*

### 5.5 การเลือกค่า $R$ ในสูตร Double Hashing
* สูตร: $\text{hash}_2(X) = R - (X \bmod R)$
* $R$ ต้องเป็นจำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize ($R < \text{TableSize}$ and $R$ is prime)
* ทำไมต้องมี $R - (\dots)$: เพื่อป้องกันไม่ให้ $\text{hash}_2(X) = 0$ ซึ่งทำให้ก้าวเดินเป็น 0 และติดลูปอนันต์ ($i \times 0 = 0$)

### 5.6 การชนของเลขกำลังสอง (Perfect Square Collision)
* เมื่อแทรกลำดับ $0, 1, 4, 9, 16, 25, 36, \dots$ ลงตารางขนาด 10 ($X \bmod 10$)
* $4^2 = 16 \bmod 10 = 6$
* $6^2 = 36 \bmod 10 = 6$
* คู่ที่ชนคู่แรกคือ **16 และ 36** โดยชนที่ **ช่อง 6**

---

## 6. ตารางสรุป 12 กับดักได้ 0 คะแนน (Zero-Score Traps Cheat Sheet)

| ประเด็นตรวจข้อสอบ | คำตอบที่ได้ 0 คะแนน ❌ | คำตอบที่ได้คะแนนเต็ม 100% ✅ | เหตุผลทางทฤษฎีตามที่ อ.ประดิษฐ์ สอน |
| :--- | :--- | :--- | :--- |
| **การเขียน Shortest Path** | ใส่ลูกศร `1 -> 4 -> 5` | คั่นด้วยจุลภาค **`1, 4, 5`** | นิยาม Path คือ Sequence of vertices ห้ามใส่ลูกศร |
| **หน่วยของความยาว Path** | ตอบหน่วยไม้บรรทัด (เช่น 2 ซม., 3 นิ้ว) | ตอบเป็นจำนวน **เส้น** หรือ **Edges** | ความยาวของทางเดินคือนับจำนวนเส้นเชื่อม ($N-1$) |
| **การนับจำนวนการชน (Collision)** | ตอบ 14 ครั้ง | ตอบ **7 ครั้ง** หรือ **9 ครั้ง** | นับเฉพาะจำนวนครั้งที่เกิดการขยับหาช่องใหม่ของคีย์ |
| **สูตร Complete Graph $K_{10}$** | ตอบติดรูปสูตร `10*(10-1)/2` หรือ `90/2` | ตอบเลขจำนวนเต็ม **45** หรือ **45 เส้น** | กฎเหล็กห้ามตอบติดสูตร ต้องคำนวณจนได้ตัวเลข |
| **จำนวนโหนด Heap สูง $H=10$** | ตอบติดรูปเลขยกกำลัง $2^{10}$ หรือ $2^{11}-1$ | ตอบเลขจำนวนเต็ม **1,024** และ **2,047** โหนด | กฎเหล็กห้ามตอบติดเลขยกกำลัง ต้องตอบเลขเต็ม |
| **การหา Parent ของโหนด $i=7$** | ปัดเศษขึ้น ตอบตำแหน่ง 4 | ตัดเศษทิ้ง ตอบตำแหน่ง **3** | $7 // 2 = 3.5 \to 3$ ใช้ Truncate Fraction |
| **การใช้งาน Index 0 ของ Heap** | ใส่ Root ที่ช่อง `array[0]` | **เว้นช่อง Index 0 ไว้เสมอ (`-`)** | ช่อง 0 เว้นไว้เพื่อให้สูตร $2i, 2i+1, \lfloor i/2 \rfloor$ ใช้งานได้ |
| **การเรียกเมธอด `deleteMin()`** | ใส่พารามิเตอร์ เช่น `deleteMin(13)` | **`deleteMin()` ไม่รับพารามิเตอร์** | ฮีปลบตัวรากเสมอ ไม่ต้องระบุค่าที่ต้องการลบ |
| **การเลือกค่า $R$ Double Hash** | ตอบ $R=8$ หรือ $R=9$ (เมื่อ TableSize=10) | ตอบ **$R = 7$** | $R$ ต้องเป็นจำนวนเฉพาะที่น้อยกว่า TableSize |
| **Path บน Null Graph ($V=\emptyset$)** | เขียนมั่ว หรือเว้นว่าง | ตอบ **"ไม่มี Path เพราะไม่มีโหนดในกราฟ"** | กราฟว่างไม่มีจุดยอดให้เดินทาง |
| **คีย์ 58 ลงช่องใด (ตารางขนาด 10)** | ตอบช่อง 6 | ตอบ **ช่อง 1** | $h_3(58) = (8+3) \bmod 10 = 1$ |
| **สูตรลูกซ้าย ลูกขวา พ่อแม่ของฮีป** | จำสลับกัน หรือบวกผิด | Left: **$2i$**, Right: **$2i+1$**, Parent: **$\lfloor i/2 \rfloor$** | สูตร 1D Array ของ Complete Binary Tree |

---

## 7. สรุปไฟล์ส่งมอบในโฟลเดอร์ `final/`

### 7.1 เอกสารหลักสำหรับนักศึกษา (Main Deliverables)
| ชื่อไฟล์ | รูปแบบและขนาด | คำอธิบายรายละเอียด |
| :--- | :--- | :--- |
| [**ข้อสอบปลายภาค_Data_Structures_Final_Exam.html**](file:///C:/Project/python-data-structures-and-algorithms/final/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%9A%E0%B8%9B%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B8%A0%E0%B8%B2%E0%B8%84_Data_Structures_Final_Exam.html) | HTML Interactive / Print-Ready | **ตัวข้อสอบปลายภาค 2 ภาษา (English + Thai Translation)** พร้อมเฉลยละเอียด, คลังข้อเขียนย่อย, และตารางกับดัก 0 คะแนน สไตล์เดียวกับ Midterm HTML |
| [**Final_Exam_2026_Paper_English.pdf**](file:///C:/Project/python-data-structures-and-algorithms/final/Final_Exam_2026_Paper_English.pdf) | PDF (6 หน้า) | **ตัวเล่มข้อสอบจริงฉบับภาษาอังกฤษล้วน** พร้อมช่องว่างและตารางเขียนตอบ มาตรฐานข้อสอบ มจพ. |
| [**Final_Exam_2026_Master_Solutions_and_Principles.pdf**](file:///C:/Project/python-data-structures-and-algorithms/final/Final_Exam_2026_Master_Solutions_and_Principles.pdf) | PDF (6 หน้า) | **เล่มเฉลยละเอียดและหลักการทางวิชาการ** ทุกข้อพร้อมตารางและวิธีคิด |
| [**FINAL_EXAM_MASTER_GUIDE.md**](file:///C:/Project/python-data-structures-and-algorithms/final/FINAL_EXAM_MASTER_GUIDE.md) | Markdown | คู่มือเตรียมสอบฉบับสมบูรณ์สรุปเนื้อหาและหลักการทั้งหมด |

### 7.2 โฟลเดอร์จัดเก็บอย่างเป็นระบบ (Organized Subfolders)
* 📁 [**`sources/past_exams/`**](file:///C:/Project/python-data-structures-and-algorithms/final/sources/past_exams/): รวบรวมข้อสอบเก่าปี 2561 และ 2564 พร้อมลายมือเฉลยรุ่นพี่
* 📁 [**`sources/whiteboard_photos/`**](file:///C:/Project/python-data-structures-and-algorithms/final/sources/whiteboard_photos/): รวบรวมภาพถ่ายกระดานดำ/สไลด์ที่ อ.ประดิษฐ์ บรรยายโจทย์จริง
* 📁 [**`scripts/`**](file:///C:/Project/python-data-structures-and-algorithms/final/scripts/): สคริปต์ Python คำนวณและสร้างเอกสาร PDF/ตรวจคำตอบ
  - [`verify_final_exam_solutions.py`](file:///C:/Project/python-data-structures-and-algorithms/final/scripts/verify_final_exam_solutions.py)
  - [`generate_final_exam_paper.py`](file:///C:/Project/python-data-structures-and-algorithms/final/scripts/generate_final_exam_paper.py)
  - [`generate_final_exam_solutions.py`](file:///C:/Project/python-data-structures-and-algorithms/final/scripts/generate_final_exam_solutions.py)
