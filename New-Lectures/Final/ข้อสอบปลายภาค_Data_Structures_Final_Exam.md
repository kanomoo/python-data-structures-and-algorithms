# 📝 รวมแนวข้อสอบปลายภาค Data Structures & Algorithms: ฉบับจริง + เก็งชุดใหม่ 2026 (ครบ 2 ชุดเต็ม 140 คะแนน พร้อมเฉลยละเอียดทุกข้อย่อย)

> [!IMPORTANT] **ข้อมูลและระเบียบการสอบปลายภาค (Final Exam Official Information)**
> - **รหัสและชื่อวิชา:** 060243106 / 060223119 โครงสร้างข้อมูลและขั้นตอนวิธี (Data Structures and Algorithms)
> - **ผู้ออกข้อสอบ:** รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (ภาควิชาเทคโนโลยีสารสนเทศ / คอมพิวเตอร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ: KMUTNB)
> - **โครงสร้างข้อสอบ:** ข้อสอบมี 7 ข้อใหญ่ คะแนนเต็มในข้อสอบ **70 คะแนน** (คิดเป็น $\frac{\text{คะแนนดิบ}}{2} = \mathbf{35\%}$ ของเกรดรวมทั้งภาคการศึกษา)
> - **เวลาในการทำข้อสอบ:** 3 ชั่วโมงเต็ม (180 นาที)
> - **เงื่อนไข:** **เปิดตำราได้ทุกชนิด (Open-Book & Open-Notes)** แต่อ้างอิงเนื้อหาและโปรแกรมตามที่สอนในห้องเรียนเป็นเกณฑ์การวัดผล
> - **อุปกรณ์ที่อนุญาต:** **ใช้เครื่องคิดเลขวิทยาศาสตร์ได้ (Scientific Calculator Allowed)**
> - **ข้อห้ามเด็ดขาด:** **ห้ามใช้โทรศัพท์มือถือ สมาร์ตโฟน แท็บเล็ต หรืออุปกรณ์สื่อสารทุกชนิดในห้องสอบโดยเด็ดขาด!**
> - **ภาษาของข้อสอบ:** คำถามในข้อสอบทางการเป็น **ภาษาอังกฤษ (English)** ทั้งหมด โดยในเอกสารชุดนี้ได้จัดทำ **คำแปลภาษาไทยกำกับในวงเล็บ `( )` อย่างละเอียดครบทุกประโยค** และในการสอบจริง **อาจารย์อนุโลมให้ตอบเป็นภาษาไทยหรือภาษาอังกฤษได้**
> - **การเขียนตอบ:** เขียนคำตอบด้วยลายมือลงบนกระดาษคำตอบอย่างชัดเจน รูป Heap และ Graph วาดด้วยดินสอหรือปากกาได้ ห้ามตอบติดรูปสูตรหรือเลขยกกำลังในข้อคำนวณตัวเลขเด็ดขาด

---

# 📑 สารบัญรวมข้อสอบปลายภาคทั้ง 2 ชุด (Table of Contents)

### 🌟 ชุดที่ 1: ข้อสอบปลายภาคฉบับจริงอิงข้อสอบเก่าและห้องเรียนสด (Real Final Exam Benchmark - 70 คะแนน)
- [Part 1: Hashing & Open Addressing Double Hashing (10 คะแนน)](#part-1-hashing--open-addressing-double-hashing-10-คะแนน-ชุดที่-1)
- [Part 2: Priority Queue & Binary Min-Heap Tracing (10 คะแนน)](#part-2-priority-queue--binary-min-heap-tracing-10-คะแนน-ชุดที่-1)
- [Part 3: Insertion Sort Tracing & Position Moves (10 คะแนน)](#part-3-insertion-sort-tracing--position-moves-10-คะแนน-ชุดที่-1)
- [Part 4: Selection Sort & Bubble Sort Tracing (10 คะแนน)](#part-4-selection-sort--bubble-sort-tracing-10-คะแนน-ชุดที่-1)
- [Part 5: Topological Sort & Circular Queue Tracing (10 คะแนน)](#part-5-topological-sort--circular-queue-tracing-10-คะแนน-ชุดที่-1)
- [Part 6: Unweighted Shortest Path (BFS) Table Tracing (10 คะแนน)](#part-6-unweighted-shortest-path-bfs-table-tracing-10-คะแนน-ชุดที่-1)
- [Part 7: Properties, Formulas & Memory Percentage Calculations (10 คะแนน)](#part-7-properties-formulas--memory-percentage-calculations-10-คะแนน-ชุดที่-1)

---

### 🚀 ชุดที่ 2: เก็งข้อสอบปลายภาคชุดประยุกต์ใหม่ 2026 (Predicted Final Exam Suite - 70 คะแนน)
- [Part 1: Hashing: Quadratic Probing, Secondary Clustering & Rehashing % (10 คะแนน)](#part-1-hashing-quadratic-probing-secondary-clustering--rehashing--10-คะแนน-ชุดที่-2)
- [Part 2: Binary Heap: BuildHeap, Sequential Insert & DeleteMin Array Mapping (10 คะแนน)](#part-2-binary-heap-buildheap-sequential-insert--deletemin-array-mapping-10-คะแนน-ชุดที่-2)
- [Part 3: Insertion Sort: Worst Case Analysis & Intermediate Pass Tracing (10 คะแนน)](#part-3-insertion-sort-worst-case-analysis--intermediate-pass-tracing-10-คะแนน-ชุดที่-2)
- [Part 4: Selection Sort vs Bubble Sort: Inversions, Comparisons & Early Exit (10 คะแนน)](#part-4-selection-sort-vs-bubble-sort-inversions-comparisons--early-exit-10-คะแนน-ชุดที่-2)
- [Part 5: Topological Sort: DAG with Disconnected Components & Cycle Detection (10 คะแนน)](#part-5-topological-sort-dag-with-disconnected-components--cycle-detection-10-คะแนน-ชุดที่-2)
- [Part 6: Unweighted Shortest Path: Complex 7-Vertex Graph with Backtracking (10 คะแนน)](#part-6-unweighted-shortest-path-complex-7-vertex-graph-with-backtracking-10-คะแนน-ชุดที่-2)
- [Part 7: Rapid-Fire Sub-Questions: Tree Heights, Graph Densities & RAM Waste (10 คะแนน)](#part-7-rapid-fire-sub-questions-tree-heights-graph-densities--ram-waste-10-คะแนน-ชุดที่-2)

---
---

# 🌟 ชุดที่ 1: ข้อสอบปลายภาคฉบับจริง (Real Final Exam Benchmark)
*(ถอดแบบ 100% จากข้อสอบจริง มจพ., บันทึกเทปคำพูดอาจารย์ 20260902, 20260909, 20260923, 20261007, และภาพถ่ายกระดานห้องเรียน DSA-pic)*

---

## Part 1: Hashing & Open Addressing Double Hashing (10 คะแนน) (ชุดที่ 1)

### ข้อ 1: Double Hashing Collision Resolution & Analysis (10 คะแนน) *(ตรงตามข้อสอบจริง มจพ. หน้า 1/5 และบันทึกคำบรรยาย 2 ก.ย.)*
**Question (EN):**  
Given an empty Hash Table of size $\text{TableSize} = 19$ (with indices from $0$ to $18$, where each cell contains `element` and `info`). The table uses **Open Addressing** with **Double Hashing** to resolve collisions.  
The primary hash function is:
$$h_0(X) = X \bmod 19$$
The collision resolution probe function is:
$$f(i) = i \times (R - (X \bmod R)) \quad \text{where } R = 17 \text{ is prime and } R < \text{TableSize}$$
The overall probing address function for probe $i = 0, 1, 2, \dots$ is:
$$h_i(X) = (h_0(X) + f(i)) \bmod 19$$
The system triggers **Rehashing** when the load factor reaches $\mathbf{80\%}$ of the table capacity.

Insert the following sequence of **8 integer keys** into the Hash Table:
$$26, \; 45, \; 70, \; 85, \; 102, \; 123, \; 143, \; 155$$

Answer all of the following sub-questions:
- **1.1 (4 Marks):** Show step-by-step mathematical calculations for all 8 keys and write the final resulting Hash Table array.
- **1.2 (2 Marks):** Which key(s) experienced the **maximum number of collisions** during insertion? How many collisions did they experience, and at which cell indices did the collisions occur?
- **1.3 (2 Marks):** After inserting all 8 keys, what is the **total cumulative number of collisions and resolution steps** that occurred? *(Note: Each collision with resolution step counts as 1, not 2, as explicitly emphasized by the instructor).*
- **1.4 (2 Marks):** After all 8 keys have been inserted, **how many more keys must be inserted** into the Hash Table before Rehashing is triggered at $80\%$ capacity? Show the percentage calculation.

---

**(คำแปลไทย):**  
*(กำหนดตารางแฮชว่างขนาด `TableSize = 19` (ดัชนี 0 ถึง 18 โดยในแต่ละช่องประกอบด้วยฟิลด์ `element` และ `info`) โครงสร้างใช้วิธี Open Addressing แก้ปัญหาการชนกันด้วย Double Hashing โดยมีฟังก์ชันแฮชหลักคือ $h_0(X) = X \bmod 19$, ฟังก์ชันแก้การชนคือ $f(i) = i \times (17 - (X \bmod 17))$ เมื่อ $R = 17$, และสูตรการตรวจสอบตำแหน่งคือ $h_i(X) = (h_0(X) + f(i)) \bmod 19$ โดยระบบกำหนดให้ทำ Rehashing เมื่อตารางมีความจุถึง 80%)*  
*(จงแทรกข้อมูลตัวเลข 8 ตัว: `26, 45, 70, 85, 102, 123, 143, 155` ลงในตารางแฮช แล้วตอบคำถามย่อยต่อไปนี้:)*  
- *1.1 (4 คะแนน): แสดงการคำนวณทีละขั้นตอนและเขียนตารางแฮชผลลัพธ์สุดท้าย*  
- *1.2 (2 คะแนน): ข้อมูลตัวใดขณะใส่เข้าไปแล้วเกิดการชนกันมากที่สุด เกิดการชนกี่ครั้ง และชนที่ตำแหน่งใดบ้าง?*  
- *1.3 (2 คะแนน): เกิดการชนกันและแก้การชนกันรวมทั้งสิ้นกี่ครั้ง? (นับเป็น 1 ครั้ง ไม่ใช่นับ 2)*  
- *1.4 (2 คะแนน): จะต้องใส่ข้อมูลเพิ่มอีกกี่ตัว จึงจะเกิดการ Rehash ที่ 80%? จงแสดงการคำนวณเปอร์เซ็นต์*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 1):

##### 1.1 การคำนวณการ Probe และการลงตารางแฮชทีละตัว:
สูตรคงที่: $s(X) = 17 - (X \bmod 17)$ (ระยะก้าวเดิน Double Hashing)

1. **Key 26:**
   - $h_0(26) = 26 \bmod 19 = \mathbf{7}$
   - ช่อง 7 ว่าง $\rightarrow$ **บรรจุ 26 ลงช่อง 7** *(ชน 0 ครั้ง)*
2. **Key 45:**
   - $h_0(45) = 45 \bmod 19 = \mathbf{7}$ *(ชนครั้งที่ 1 กับ key 26 ที่ช่อง 7)*
   - คำนวณระยะก้าว: $s(45) = 17 - (45 \bmod 17) = 17 - 11 = 6$
   - Probe $i=1$: $h_1(45) = (7 + 1 \times 6) \bmod 19 = 13 \bmod 19 = \mathbf{13}$
   - ช่อง 13 ว่าง $\rightarrow$ **บรรจุ 45 ลงช่อง 13** *(ชน 1 ครั้ง)*
3. **Key 70:**
   - $h_0(70) = 70 \bmod 19 = \mathbf{13}$ *(ชนครั้งที่ 1 กับ key 45 ที่ช่อง 13)*
   - คำนวณระยะก้าว: $s(70) = 17 - (70 \bmod 17) = 17 - 2 = 15$
   - Probe $i=1$: $h_1(70) = (13 + 1 \times 15) \bmod 19 = 28 \bmod 19 = \mathbf{9}$
   - ช่อง 9 ว่าง $\rightarrow$ **บรรจุ 70 ลงช่อง 9** *(ชน 1 ครั้ง)*
4. **Key 85:**
   - $h_0(85) = 85 \bmod 19 = \mathbf{9}$ *(ชนครั้งที่ 1 กับ key 70 ที่ช่อง 9)*
   - คำนวณระยะก้าว: $s(85) = 17 - (85 \bmod 17) = 17 - 0 = 17$
   - Probe $i=1$: $h_1(85) = (9 + 1 \times 17) \bmod 19 = 26 \bmod 19 = \mathbf{7}$ *(ชนครั้งที่ 2 กับ key 26 ที่ช่อง 7)*
   - Probe $i=2$: $h_2(85) = (9 + 2 \times 17) \bmod 19 = (9 + 34) \bmod 19 = 43 \bmod 19 = \mathbf{5}$
   - ช่อง 5 ว่าง $\rightarrow$ **บรรจุ 85 ลงช่อง 5** *(ชน 2 ครั้ง)*
5. **Key 102:**
   - $h_0(102) = 102 \bmod 19 = \mathbf{7}$ *(ชนครั้งที่ 1 กับ key 26 ที่ช่อง 7)*
   - คำนวณระยะก้าว: $s(102) = 17 - (102 \bmod 17) = 17 - 0 = 17$
   - Probe $i=1$: $h_1(102) = (7 + 1 \times 17) \bmod 19 = 24 \bmod 19 = \mathbf{5}$ *(ชนครั้งที่ 2 กับ key 85 ที่ช่อง 5)*
   - Probe $i=2$: $h_2(102) = (7 + 2 \times 17) \bmod 19 = (7 + 34) \bmod 19 = 41 \bmod 19 = \mathbf{3}$
   - ช่อง 3 ว่าง $\rightarrow$ **บรรจุ 102 ลงช่อง 3** *(ชน 2 ครั้ง)*
6. **Key 123:**
   - $h_0(123) = 123 \bmod 19 = \mathbf{9}$ *(ชนครั้งที่ 1 กับ key 70 ที่ช่อง 9)*
   - คำนวณระยะก้าว: $s(123) = 17 - (123 \bmod 17) = 17 - 4 = 13$
   - Probe $i=1$: $h_1(123) = (9 + 1 \times 13) \bmod 19 = 22 \bmod 19 = \mathbf{3}$ *(ชนครั้งที่ 2 กับ key 102 ที่ช่อง 3)*
   - Probe $i=2$: $h_2(123) = (9 + 2 \times 13) \bmod 19 = (9 + 26) \bmod 19 = 35 \bmod 19 = \mathbf{16}$
   - ช่อง 16 ว่าง $\rightarrow$ **บรรจุ 123 ลงช่อง 16** *(ชน 2 ครั้ง)*
7. **Key 143:**
   - $h_0(143) = 143 \bmod 19 = \mathbf{10}$
   - ช่อง 10 ว่าง $\rightarrow$ **บรรจุ 143 ลงช่อง 10** *(ชน 0 ครั้ง)*
8. **Key 155:**
   - $h_0(155) = 155 \bmod 19 = \mathbf{3}$ *(ชนครั้งที่ 1 กับ key 102 ที่ช่อง 3)*
   - คำนวณระยะก้าว: $s(155) = 17 - (155 \bmod 17) = 17 - 2 = 15$
   - Probe $i=1$: $h_1(155) = (3 + 1 \times 15) \bmod 19 = 18 \bmod 19 = \mathbf{18}$
   - ช่อง 18 ว่าง $\rightarrow$ **บรรจุ 155 ลงช่อง 18** *(ชน 1 ครั้ง)*

##### ตาราง Hash Table ผลลัพธ์สุดท้าย (TableSize = 19):

| Index | Element | Info | Index | Element | Info |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | `Empty` | 0 | **10** | **143** | 1 (Active) |
| **1** | `Empty` | 0 | **11** | `Empty` | 0 |
| **2** | `Empty` | 0 | **12** | `Empty` | 0 |
| **3** | **102** | 1 (Active) | **13** | **45** | 1 (Active) |
| **4** | `Empty` | 0 | **14** | `Empty` | 0 |
| **5** | **85** | 1 (Active) | **15** | `Empty` | 0 |
| **6** | `Empty` | 0 | **16** | **123** | 1 (Active) |
| **7** | **26** | 1 (Active) | **17** | `Empty` | 0 |
| **8** | `Empty` | 0 | **18** | **155** | 1 (Active) |
| **9** | **70** | 1 (Active) | | | |

##### 1.2 ข้อมูลตัวที่มีการชนกันมากที่สุด:
- **ข้อมูลที่มีการชนมากที่สุด:** มี 3 ตัว คือ **`85`**, **`102`**, และ **`123`**
- **จำนวนครั้งที่ชน:** ชนตัวละ **2 ครั้ง**
- **ตำแหน่งที่เกิดการชน:**
  - ตัวเลข `85`: ชนที่ช่อง **9** และช่อง **7**
  - ตัวเลข `102`: ชนที่ช่อง **7** และช่อง **5**
  - ตัวเลข `123`: ชนที่ช่อง **9** และช่อง **3**

##### 1.3 จำนวนการชนกันและแก้การชนกันรวมทั้งสิ้น:
$$\text{Total Collisions} = 0 + 1 + 1 + 2 + 2 + 2 + 0 + 1 = \mathbf{9} \text{ ครั้ง}$$
*(คำเตือนของอาจารย์: การชนและแก้ชน 1 ครั้งให้นับ 1 ห้ามตอบ 18 ครั้งเด็ดขาด)*

##### 1.4 จำนวนข้อมูลที่ต้องใส่เพิ่มจนเกิดการ Rehash ที่ 80%:
- ความจุสูงสุดที่จุด Rehash $80\%$:
  $$\text{Threshold} = 19 \times 0.80 = 15.2 \xrightarrow{\text{ปัดขึ้นเพื่อไม่ให้เกิน}} \mathbf{16} \text{ ตัว}$$
  *(หรือในตำราอ้างอิง: $\lfloor 19 \times 0.80 \rfloor = 15$ หรือ $\lceil 19 \times 0.80 \rceil = 16$)*
- ปัจจุบันมีข้อมูลอยู่ในตารางแล้ว $= 8$ ตัว
- ดังนั้น จะต้องใส่ข้อมูลเพิ่มอีก:
  $$16 - 8 = \mathbf{8} \text{ ตัว} \quad (\text{หรือ } 15 - 8 = 7 \text{ ตัว ตามเกณฑ์ปัดลง})$$
  *(ในห้องสอบให้เขียน: $19 \times 80\% = 15.2$ หากถือเกณฑ์เริ่ม Rehash เมื่อถึงตัวที่ 16 ต้องใส่อีก $16 - 8 = \mathbf{8 \text{ ตัว}}$)*

---

## Part 2: Priority Queue & Binary Min-Heap Tracing (10 คะแนน) (ชุดที่ 1)

### ข้อ 2: Binary Min-Heap Array Operations (10 คะแนน) *(ตรงตามข้อสอบจริง มจพ. หน้า 1/5 และเทปบรรยาย 9 ก.ย.)*
**Question (EN):**  
Given an empty Priority Queue implemented as a **Binary Min-Heap** using a 1-based array (where `array[0]` is an unused sentinel marked with `-` or `None`).

- **2.1 (2 Marks):** State the **two fundamental properties** that every Binary Min-Heap must strictly satisfy. Why is `array[0]` deliberately left unused in the array representation? State the index mathematical formulas for `leftChild(i)`, `rightChild(i)`, and `parent(i)`.
- **2.2 (3 Marks):** Sequentially insert the following 12 integer keys into the empty Binary Min-Heap:
  $$64, \; 14, \; 24, \; 1, \; 20, \; 2, \; 5, \; 10, \; 6, \; 8, \; 15, \; 20$$
  Show the percolate-up mechanism and write the final resulting array in **Table 2.1**.
- **2.3 (2 Marks):** Perform one `deleteMin()` operation on the heap from 2.2. Show the percolate-down process and write the resulting array in **Table 2.2**.
- **2.4 (1 Mark):** Insert the integer key **`3`** into the heap from 2.3. Write the resulting array in **Table 2.3**.
- **2.5 (2 Marks):** Perform another `deleteMin()` operation on the heap from 2.4. Write the final resulting array in **Table 2.4**. What is the exact Python syntax for calling the `deleteMin()` method on heap instance `h`?

---

**(คำแปลไทย):**  
*(กำหนด Binary Min-Heap ว่างเปล่าที่เก็บด้วย 1D Array เริ่มจาก Index 1 โดยเว้น Index 0 ไว้)*  
- *2.1 (2 คะแนน): จงบอกคุณสมบัติพื้นฐาน 2 ประการของ Binary Min-Heap, เหตุผลที่เว้น Index 0 ไว้, และเขียนสูตรหาตำแหน่งลูกซ้าย ลูกขวา และพ่อแม่*  
- *2.2 (3 คะแนน): จงแทรกข้อมูล 12 ตัว: `64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20` ลงใน Heap และเขียนผลลัพธ์ลงในตารางที่ 2.1*  
- *2.3 (2 คะแนน): ทำการ `deleteMin()` 1 ครั้ง และเขียนผลลัพธ์ลงในตารางที่ 2.2*  
- *2.4 (1 คะแนน): แทรกเลข `3` ลงใน Heap แล้วเขียนผลลัพธ์ลงในตารางที่ 2.3*  
- *2.5 (2 คะแนน): ทำการ `deleteMin()` อีก 1 ครั้ง และเขียนผลลัพธ์ลงในตารางที่ 2.4 พร้อมบอกไวยากรณ์การเรียกเมธอด `deleteMin()` ในภาษา Python*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 2):

##### 2.1 คุณสมบัติ 2 ประการและสูตร Index:
1. **Structure Property (คุณสมบัติเชิงโครงสร้าง):** ต้องเป็น **Complete Binary Tree** (ต้นไม้ไบนารีสมบูรณ์) คือโหนดเต็มทุกชั้น ยกเว้นชั้นล่างสุดที่ต้องเรียงชิดซ้ายจากซ้ายไปขวาเท่านั้น
2. **Heap-Order Property (คุณสมบัติการจัดลำดับของฮีป):** สำหรับ Min-Heap โหนดแม่ต้องมีค่าน้อยกว่าหรือเท่ากับโหนดลูกเสมอ ($\text{Parent} \le \text{Children}$) ส่งผลให้โหนดราก (Root) มีค่าน้อยที่สุดเสมอ
- **ทำไมต้องเว้น Index 0:** เพื่อให้ความสัมพันธ์ของดัชนีเป็นจำนวนเท่าที่แม่นยำทางคณิตศาสตร์:
  - $\text{Left Child}(i) = \mathbf{2i}$
  - $\text{Right Child}(i) = \mathbf{2i + 1}$
  - $\text{Parent}(i) = \mathbf{\lfloor i/2 \rfloor}$ (ภาษา Python ใช้การหารตัดเศษ `i // 2`)

##### 2.2 ตารางที่ 2.1 (หลัง Insert ครบ 12 ตัว):
ขั้นตอนการ Percolate Up ทีละตัว:
- ใส่ 64 $\rightarrow$ `[64]`
- ใส่ 14 $\rightarrow$ 14 สลับกับ 64 $\rightarrow$ `[14, 64]`
- ใส่ 24 $\rightarrow$ `[14, 64, 24]`
- ใส่ 1 $\rightarrow$ 1 สลับกับ 64, สลับกับ 14 $\rightarrow$ `[1, 14, 24, 64]`
- ... ทำต่อเนื่องจนครบ 12 ตัว:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Table 2.1 (Insert 12 ตัว)** | `-` | **1** | **6** | **2** | **10** | **8** | **20** | **5** | **64** | **14** | **20** | **15** | **24** |

##### 2.3 ตารางที่ 2.2 (หลัง deleteMin ครั้งที่ 1):
- ดึง Root คือ `1` ออก
- นำตัวสุดท้ายคือ `24` มาวางที่ Root (`hole = 1`)
- Percolate Down: เปรียบเทียบลูกซ้าย (6) กับลูกขวา (2) $\rightarrow$ ลูกที่น้อยกว่าคือ 2 (Index 3)
- 24 > 2 จึงเลื่อน 2 ขึ้นมาแทนที่ 1 (`hole = 3`)
- ลูกของ Index 3 คือ 20 (Index 6) และ 5 (Index 7) $\rightarrow$ ลูกที่น้อยกว่าคือ 5
- 24 > 5 จึงเลื่อน 5 ขึ้นมาแทนที่ (`hole = 7`)
- โหนด 7 ไม่มีลูก จึงบรรจุ 24 ลงที่ช่อง 7:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Table 2.2 (deleteMin 1)** | `-` | **2** | **6** | **5** | **10** | **8** | **20** | **24** | **64** | **14** | **20** | **15** |

##### 2.4 ตารางที่ 2.3 (หลัง Insert 3):
- ขยายขนาดตารางเป็น 12 ช่อง (`hole = 12`)
- นำ 3 เปรียบเทียบกับ Parent ที่ $\lfloor 12/2 \rfloor = 6$ (ค่าคือ 20) $\rightarrow 3 < 20$ เลื่อน 20 ลงมา (`hole = 6`)
- นำ 3 เปรียบเทียบกับ Parent ที่ $\lfloor 6/2 \rfloor = 3$ (ค่าคือ 5) $\rightarrow 3 < 5$ เลื่อน 5 ลงมา (`hole = 3`)
- นำ 3 เปรียบเทียบกับ Parent ที่ $\lfloor 3/2 \rfloor = 1$ (ค่าคือ 2) $\rightarrow 3 > 2$ หยุด! บรรจุ 3 ลงที่ช่อง 3:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Table 2.3 (Insert 3)** | `-` | **2** | **6** | **3** | **10** | **8** | **5** | **24** | **64** | **14** | **20** | **15** | **20** |

##### 2.5 ตารางที่ 2.4 (หลัง deleteMin ครั้งที่ 2):
- ดึง Root คือ `2` ออก
- นำตัวสุดท้ายคือ `20` มาวางที่ Root (`hole = 1`)
- เปรียบเทียบลูกซ้าย (6) กับลูกขวา (3) $\rightarrow$ ลูกที่น้อยกว่าคือ 3 (Index 3) เลื่อน 3 ขึ้นมา (`hole = 3`)
- ลูกของ Index 3 คือ 5 (Index 6) และ 24 (Index 7) $\rightarrow$ ลูกที่น้อยกว่าคือ 5 เลื่อน 5 ขึ้นมา (`hole = 6`)
- ช่อง 6 ไม่มีลูก เลื่อน 20 ลงบรรจุที่ช่อง 6:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Table 2.4 (deleteMin 2)** | `-` | **3** | **6** | **5** | **10** | **8** | **20** | **24** | **64** | **14** | **20** | **15** |

- **ไวยากรณ์ Python:** เมธอด `deleteMin()` **ไม่มีการรับพารามิเตอร์** ต้องเรียก:
  ```python
  h.deleteMin()  # หรือ h.delete_min()
  ```
  *(คำเตือนของอาจารย์: ห้ามใส่ค่าพารามิเตอร์เด็ดขาด เช่น `h.deleteMin(2)` จะได้ 0 คะแนนทันที)*

---

## Part 3: Insertion Sort Tracing & Position Moves (10 คะแนน) (ชุดที่ 1)

### ข้อ 3: Insertion Sort Tracing & Worst-Case Calculation (10 คะแนน) *(ตรงตามข้อสอบจริง มจพ. หน้า 2/5)*
**Question (EN):**  
- **3.1 (4 Marks):** Define an initial input array of **12 elements** that represents the **Worst-Case** scenario for `insertionSort`. Write this input array into **Table 3.1**. After running `insertionSort` to completion (sorting in ascending order), **how many total Position Moves** occurred in total? State the mathematical summation formula used to calculate this value.
- **3.2 (6 Marks):** Given the initial 12-element array:
  $$61, \; 52, \; 12, \; 24, \; 8, \; 35, \; 32, \; 5, \; 71, \; 68, \; 18, \; 2$$
  Write the contents of the array after the completion of **Pass $p = 3$** and **Pass $p = 6$**. For both passes, count and state the exact number of **Position Moves**, and state the value of loop index variable `j` when the pass finishes.

---

**(คำแปลไทย):**  
*(3.1 (4 คะแนน): จงกำหนดข้อมูลอินพุต 12 ตัวแบบกรณีแย่ที่สุด (Worst Case) สำหรับ insertionSort ลงในตารางที่ 3.1 เมื่อเรียงเสร็จสิ้น เกิด Position Move รวมทั้งสิ้นกี่ครั้ง? พร้อมบอกสูตรคณิตศาสตร์)*  
*(3.2 (6 คะแนน): กำหนดข้อมูล 12 ตัว: `61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2` จงเขียนผลลัพธ์ของอาร์เรย์ในรอบ $p = 3$ และ $p = 6$ พร้อมระบุจำนวน Position Move และค่าของตัวแปร $j$ ในทั้งสองรอบ)*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 3):

##### 3.1 ข้อมูลแบบ Worst Case สำหรับ $N = 12$:
- ข้อมูล Worst Case ของการเรียงจากน้อยไปมาก คือ **ข้อมูลที่เรียงกลับทิศจากมากไปน้อย (Descending Order)**:
  `[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`
- **สูตรคำนวณจำนวน Position Moves (การเลื่อนตำแหน่งข้อมูล):**
  $$\text{Total Moves} = \sum_{p=1}^{N-1} p = \frac{N(N - 1)}{2} = \frac{12 \times 11}{2} = \mathbf{66} \text{ ครั้ง}$$

##### 3.2 การ Trace อาร์เรย์ในรอบ $p = 3$ และ $p = 6$:
อาร์เรย์เริ่มต้น ($p=0$): `[61, 52, 12, 24, 8, 35, 32, 5, 71, 68, 18, 2]`
- **Pass $p = 1$ (คีย์ $52$):** เลื่อน 61 $\rightarrow$ `[52, 61, 12, 24, 8, ...]` (เลื่อน 1 ครั้ง)
- **Pass $p = 2$ (คีย์ $12$):** เลื่อน 61, 52 $\rightarrow$ `[12, 52, 61, 24, 8, ...]` (เลื่อน 2 ครั้ง)
- **Pass $p = 3$ (คีย์ $24$, ตรวจสอบกับ $61, 52$):**
  - นำ $tmp = 24$, เปรียบเทียบ $61 > 24 \implies a[3] = 61$
  - เปรียบเทียบ $52 > 24 \implies a[2] = 52$
  - เปรียบเทียบ $12 < 24$ (หยุดลูป) $\implies a[1] = 24$
  - **สถานะอาร์เรย์หลัง $p = 3$:** `[12, 24, 52, 61, 8, 35, 32, 5, 71, 68, 18, 2]`
  - **Position Move ในรอบ $p = 3$:** **2 ครั้ง**
  - **ค่าตัวแปร $j$ เมื่อจบรอบ:** **$j = 1$**
- **Pass $p = 4$ (คีย์ $8$):** เลื่อน 4 ตัว $\rightarrow$ `[8, 12, 24, 52, 61, 35, 32, 5, ...]`
- **Pass $p = 5$ (คีย์ $35$):** เลื่อน 2 ตัว $\rightarrow$ `[8, 12, 24, 35, 52, 61, 32, 5, ...]`
- **Pass $p = 6$ (คีย์ $32$, ตรวจสอบกับ $61, 52, 35$):**
  - นำ $tmp = 32$, เปรียบเทียบ $61 > 32 \implies a[6] = 61$
  - เปรียบเทียบ $52 > 32 \implies a[5] = 52$
  - เปรียบเทียบ $35 > 32 \implies a[4] = 35$
  - เปรียบเทียบ $24 < 32$ (หยุดลูป) $\implies a[3] = 32$
  - **สถานะอาร์เรย์หลัง $p = 6$:** `[8, 12, 24, 32, 35, 52, 61, 5, 71, 68, 18, 2]`
  - **Position Move ในรอบ $p = 6$:** **3 ครั้ง**
  - **ค่าตัวแปร $j$ เมื่อจบรอบ:** **$j = 3$**

---

## Part 4: Selection Sort & Bubble Sort Tracing (10 คะแนน) (ชุดที่ 1)

### ข้อ 4: Selection Sort vs. Bubble Sort Execution (10 คะแนน) *(ตามแนวข้อสอบปี 2569 ที่ปรับเปลี่ยนแทน Quicksort)*
**Question (EN):**  
Given the following unsorted array of **8 integer elements**:
$$45, \; 18, \; 72, \; 31, \; 12, \; 88, \; 25, \; 60$$

- **4.1 (5 Marks) Selection Sort:**
  - Trace the array step-by-step for each pass ($p = 1 \text{ to } 7$).
  - For each pass, identify the **minimum element (`min_idx`)** found in the unsorted sub-array and write the pair of elements that were swapped.
  - What is the total number of swaps executed?
- **4.2 (5 Marks) Bubble Sort:**
  - Trace the array step-by-step for each pass until sorting completes.
  - Show how the algorithm uses an **early termination flag** (`swapped == False`) to detect when the array is already sorted.
  - State the exact **pass number at which the algorithm terminates**, and calculate the total number of comparisons and swaps.

---

**(คำแปลไทย):**  
*(กำหนดอาร์เรย์ข้อมูล 8 ตัว: `45, 18, 72, 31, 12, 88, 25, 60`)*  
- *4.1 (5 คะแนน) Selection Sort: จง Trace ค่าในอาร์เรย์ทีละรอบ ($p = 1$ ถึง 7) ระบุค่าต่ำสุดที่พบและคู่ที่สลับ และนับจำนวนครั้งที่สลับทั้งหมด*  
- *4.2 (5 คะแนน) Bubble Sort: จง Trace ค่าในอาร์เรย์ทีละรอบ แสดงการทำงานของ flag ที่หยุดการทำงานก่อนกำหนด และระบุรอบที่โปรแกรมหยุดทำงาน พร้อมนับจำนวนครั้งที่เปรียบเทียบและสลับทั้งหมด*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 4):

##### 4.1 Selection Sort Tracing (N = 8):
- **Pass 1:** ตรวจหาค่าน้อยสุดจาก index 0..7 $\rightarrow$ พบ **12** (Index 4)  
  $\implies$ สลับ Index 0 กับ 4 (สลับ 45 กับ 12):  
  `[12, 18, 72, 31, 45, 88, 25, 60]` &bull; *(Swap 1)*
- **Pass 2:** ตรวจหาค่าน้อยสุดจาก index 1..7 $\rightarrow$ พบ **18** (Index 1)  
  $\implies$ อยู่ตำแหน่งเดิม ไม่ต้องสลับ:  
  `[12, 18, 72, 31, 45, 88, 25, 60]` &bull; *(Swap 0)*
- **Pass 3:** ตรวจหาค่าน้อยสุดจาก index 2..7 $\rightarrow$ พบ **25** (Index 6)  
  $\implies$ สลับ Index 2 กับ 6 (สลับ 72 กับ 25):  
  `[12, 18, 25, 31, 45, 88, 72, 60]` &bull; *(Swap 2)*
- **Pass 4:** ตรวจหาค่าน้อยสุดจาก index 3..7 $\rightarrow$ พบ **31** (Index 3)  
  $\implies$ อยู่ตำแหน่งเดิม:  
  `[12, 18, 25, 31, 45, 88, 72, 60]` &bull; *(Swap 0)*
- **Pass 5:** ตรวจหาค่าน้อยสุดจาก index 4..7 $\rightarrow$ พบ **45** (Index 4)  
  $\implies$ อยู่ตำแหน่งเดิม:  
  `[12, 18, 25, 31, 45, 88, 72, 60]` &bull; *(Swap 0)*
- **Pass 6:** ตรวจหาค่าน้อยสุดจาก index 5..7 $\rightarrow$ พบ **60** (Index 7)  
  $\implies$ สลับ Index 5 กับ 7 (สลับ 88 กับ 60):  
  `[12, 18, 25, 31, 45, 60, 72, 88]` &bull; *(Swap 3)*
- **Pass 7:** ตรวจหาค่าน้อยสุดจาก index 6..7 $\rightarrow$ พบ **72** (Index 6)  
  $\implies$ อยู่ตำแหน่งเดิม:  
  `[12, 18, 25, 31, 45, 60, 72, 88]` &bull; *(Swap 0)*
- **สรุปจำนวนครั้งที่สลับ (Total Swaps):** **3 ครั้ง**

##### 4.2 Bubble Sort Tracing & Early Termination:
- **Pass 1:** เปรียบเทียบคู่ติดกัน $(45,18)\to$สลับ, $(45,72)$, $(72,31)\to$สลับ, $(72,12)\to$สลับ, $(72,88)$, $(88,25)\to$สลับ, $(88,60)\to$สลับ  
  ผลลัพธ์ Pass 1: `[18, 45, 31, 12, 72, 25, 60, 88]` *(สลับ 5 ครั้ง)*
- **Pass 2:** $(45,31)\to$สลับ, $(45,12)\to$สลับ, $(72,25)\to$สลับ, $(72,60)\to$สลับ  
  ผลลัพธ์ Pass 2: `[18, 31, 12, 45, 25, 60, 72, 88]` *(สลับ 4 ครั้ง)*
- **Pass 3:** $(31,12)\to$สลับ, $(45,25)\to$สลับ  
  ผลลัพธ์ Pass 3: `[18, 12, 31, 25, 45, 60, 72, 88]` *(สลับ 2 ครั้ง)*
- **Pass 4:** $(18,12)\to$สลับ, $(31,25)\to$สลับ  
  ผลลัพธ์ Pass 4: `[12, 18, 25, 31, 45, 60, 72, 88]` *(สลับ 2 ครั้ง)*
- **Pass 5:** ตรวจสอบทุกคู่ที่เหลือ ไม่มีการสลับเลยแม้แต่คู่เดียว!  
  `swapped == False` เกิดขึ้น  
  ผลลัพธ์ Pass 5: `[12, 18, 25, 31, 45, 60, 72, 88]` *(สลับ 0 ครั้ง)*
- **สรุปการ Early Termination:**
  - อัลกอริทึมหยุดทำงานที่ **Pass 5** ทันที ไม่ต้องทำถึง Pass 7
  - **จำนวนครั้งที่สลับรวมทั้งหมด:** $5 + 4 + 2 + 2 + 0 = \mathbf{13} \text{ ครั้ง}$

---

## Part 5: Topological Sort & Circular Queue Tracing (10 คะแนน) (ชุดที่ 1)

### ข้อ 5: Topological Sort on 7-Vertex DAG (10 คะแนน) *(ตรงตามรูปกระดานห้องเรียน 840922631... และเทปบรรยาย 23 ก.ย.)*
**Question (EN):**  
Given a Directed Acyclic Graph (DAG) with **7 vertices** ($V = \{1, 2, 3, 4, 5, 6, 7\}$) defined by the Adjacency List:
- $v_1 \rightarrow 3, 4$
- $v_2 \rightarrow 1$
- $v_3 \rightarrow 4, 6$
- $v_4 \rightarrow 6$
- $v_5 \rightarrow 1, 2, 7$
- $v_6 \rightarrow \emptyset$
- $v_7 \rightarrow 2$

- **5.1 (5 Marks):** Fill the **Indegree Tracking Table** showing the initial indegrees and the step-by-step value updates across all 7 rounds (Round 1 to 7).
- **5.2 (2 Marks):** A Circular Queue of size 7 (indices 0 to 6) is used. Draw the queue state and specify the exact index positions of **`front`** and **`back`** after the algorithm completes. (Assume `front` points to the cell of the first item, and `back` points to the last enqueued item).
- **5.3 (3 Marks):** Write down the final valid **Topological Ordering** sequence.

---

**(คำแปลไทย):**  
*(กำหนดกราฟ DAG 7 จุดยอดตาม Adjacency List ที่ให้มา)*  
- *5.1 (5 คะแนน): จงเขียนตาราง Indegree Tracking Table แสดงค่าเริ่มต้นและการขีดฆ่าเปลี่ยนค่าในแต่ละรอบ (รอบที่ 1 ถึง 7)*  
- *5.2 (2 คะแนน): ใช้ Circular Queue ขนาด 7 ช่อง (ดัชนี 0 ถึง 6) จงเขียนภาพ Queue และระบุตำแหน่งของ `front` และ `back` เมื่อจบการทำงาน*  
- *5.3 (3 คะแนน): จงเขียนลำดับผลลัพธ์ Topological Ordering ที่ถูกต้อง*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 5):

##### 5.1 ตาราง Indegree Array Tracking Table:
คำนวณ Indegree เริ่มต้น:
- $v_1$: มีเส้นเข้าจาก $v_2, v_5 \implies \mathbf{2}$
- $v_2$: มีเส้นเข้าจาก $v_5, v_7 \implies \mathbf{2}$
- $v_3$: มีเส้นเข้าจาก $v_1 \implies \mathbf{1}$
- $v_4$: มีเส้นเข้าจาก $v_1, v_3 \implies \mathbf{2}$
- $v_5$: ไม่มีเส้นเข้า $\implies \mathbf{0}$
- $v_6$: มีเส้นเข้าจาก $v_3, v_4 \implies \mathbf{2}$
- $v_7$: มีเส้นเข้าจาก $v_5 \implies \mathbf{1}$

| Vertex | Initial | R1 ($v=5$) | R2 ($v=7$) | R3 ($v=2$) | R4 ($v=1$) | R5 ($v=3$) | R6 ($v=4$) | R7 ($v=6$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2 | 1 | 1 | **0** | 0 | 0 | 0 | 0 |
| **2** | 2 | 1 | **0** | 0 | 0 | 0 | 0 | 0 |
| **3** | 1 | 1 | 1 | 1 | **0** | 0 | 0 | 0 |
| **4** | 2 | 2 | 2 | 2 | 1 | **0** | 0 | 0 |
| **5** | **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **6** | 2 | 2 | 2 | 2 | 2 | 1 | **0** | 0 |
| **7** | 1 | **0** | 0 | 0 | 0 | 0 | 0 | 0 |

##### 5.2 สถานะของ Circular Queue (ขนาด 7 ช่อง, ดัชนี 0..6):
- **เริ่มต้น:** Enqueue $v_5 \implies$ `Queue = [5, -, -, -, -, -, -]`, `front = 0`, `back = 0`
- **รอบที่ 1:** Dequeue $5$ (`front = 1`), Enqueue $7 \implies$ `[5, 7, -, -, -, -, -]`, `back = 1`
- **รอบที่ 2:** Dequeue $7$ (`front = 2`), Enqueue $2 \implies$ `[5, 7, 2, -, -, -, -]`, `back = 2`
- **รอบที่ 3:** Dequeue $2$ (`front = 3`), Enqueue $1 \implies$ `[5, 7, 2, 1, -, -, -]`, `back = 3`
- **รอบที่ 4:** Dequeue $1$ (`front = 4`), Enqueue $3 \implies$ `[5, 7, 2, 1, 3, -, -]`, `back = 4`
- **รอบที่ 5:** Dequeue $3$ (`front = 5`), Enqueue $4 \implies$ `[5, 7, 2, 1, 3, 4, -]`, `back = 5`
- **รอบที่ 6:** Dequeue $4$ (`front = 6`), Enqueue $6 \implies$ `[5, 7, 2, 1, 3, 4, 6]`, `back = 6`
- **รอบที่ 7:** Dequeue $6$ (`front = (6+1) % 7 = 0`)
- **ตำแหน่งเมื่อจบโปรแกรม:**
  - **`front` อยู่ที่ตำแหน่ง: 0**
  - **`back` อยู่ที่ตำแหน่ง: 6**

##### 5.3 ลำดับ Topological Ordering:
$$\mathbf{5, \; 7, \; 2, \; 1, \; 3, \; 4, \; 6}$$

---

## Part 6: Unweighted Shortest Path (BFS) Table Tracing (10 คะแนน) (ชุดที่ 1)

### ข้อ 6: BFS Shortest Path Processing & Route Extraction (10 คะแนน) *(ตรงตามรูปกระดานห้องเรียน 838089388... และใบงาน Assignment 4)*
**Question (EN):**  
Given a directed graph with **7 vertices** ($V = \{1, 2, 3, 4, 5, 6, 7\}$) and 12 directed edges defined by the Adjacency List:
- $v_1 \rightarrow 2, 4$
- $v_2 \rightarrow 4, 5, 7$
- $v_3 \rightarrow 1, 6$
- $v_4 \rightarrow 3, 5, 6, 7$
- $v_5 \rightarrow 7$
- $v_6 \rightarrow \emptyset$
- $v_7 \rightarrow 6$

- **6.1 (5 Marks):** Execute the **Unweighted Shortest Path Algorithm (BFS)** with **Start Vertex = 1**. Fill the table tracking `Known` ($T/F$), `Dist` ($d_v$), and `Path` ($p_v$) for all vertices across all rounds.
- **6.2 (2 Marks):** Trace the queue dequeue sequence and write down the exact order in which vertices were dequeued.
- **6.3 (3 Marks):** Write down the shortest path and path length from vertex 1 to **vertex 5**, and from vertex 1 to **vertex 7**.  
  *(CRITICAL RULE: Format paths strictly as comma-separated lists, e.g. `1, 4, 5`. Do NOT use arrows).*

---

**(คำแปลไทย):**  
*(กำหนดกราฟมีทิศทาง 7 จุดยอด 12 เส้นเชื่อมตาม Adjacency List)*  
- *6.1 (5 คะแนน): จงแสดงวิธีหา Shortest Path แบบไม่มีน้ำหนัก โดยให้จุดยอด 1 เป็นจุดเริ่มต้น เขียนตารางผลลัพธ์ Known, Dist, Path ครบทุกรอบ*  
- *6.2 (2 คะแนน): จงเขียนลำดับของจุดยอดที่ถูก Dequeue ออกจาก Queue ตามลำดับ*  
- *6.3 (3 คะแนน): จงเขียนเส้นทางที่สั้นที่สุดและความยาวเส้นทางจากจุด 1 ไปยังจุด 5 และจากจุด 1 ไปยังจุด 7 (กฎเหล็ก: คั่นด้วยจุลภาค ห้ามใส่ลูกศร)*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 6):

##### 6.1 ตาราง BFS Shortest Path (Start Vertex = 1):
ค่าเริ่มต้น: $v_1$: `Known=F, Dist=0, Path=0`; โหนดอื่นๆ ทั้งหมด: `Known=F, Dist=`$\infty$`, Path=0`

| Vertex | Initial | Round 1 ($v=1$) | Round 2 ($v=2$) | Round 3 ($v=4$) | Round 4 ($v=5$) | Round 5 ($v=7$) | Round 6 ($v=3$) | Round 7 ($v=6$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | F, 0, 0 | **T, 0, 0** | T, 0, 0 | T, 0, 0 | T, 0, 0 | T, 0, 0 | T, 0, 0 | T, 0, 0 |
| **2** | F, $\infty$, 0 | F, 1, 1 | **T, 1, 1** | T, 1, 1 | T, 1, 1 | T, 1, 1 | T, 1, 1 | T, 1, 1 |
| **3** | F, $\infty$, 0 | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 4 | F, 2, 4 | F, 2, 4 | **T, 2, 4** | T, 2, 4 |
| **4** | F, $\infty$, 0 | F, 1, 1 | F, 1, 1 | **T, 1, 1** | T, 1, 1 | T, 1, 1 | T, 1, 1 | T, 1, 1 |
| **5** | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 2 | F, 2, 2 | **T, 2, 2** | T, 2, 2 | T, 2, 2 | T, 2, 2 |
| **6** | F, $\infty$, 0 | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 4 | F, 2, 4 | F, 2, 4 | F, 2, 4 | **T, 2, 4** |
| **7** | F, $\infty$, 0 | F, $\infty$, 0 | F, 2, 2 | F, 2, 2 | F, 2, 2 | **T, 2, 2** | T, 2, 2 | T, 2, 2 |

##### 6.2 ลำดับการ Dequeue ออกจาก Queue:
$$\mathbf{1, \; 2, \; 4, \; 5, \; 7, \; 3, \; 6}$$

##### 6.3 เส้นทางและระยะทางที่สั้นที่สุด:
1. **เส้นทางจาก 1 ไปยัง 5:**
   - จากตาราง: $p_v(5) = 2 \implies p_v(2) = 1 \implies$ จุดเริ่มต้น
   - **เส้นทาง (Shortest Path):** **`1, 2, 5`** *(หรือ `1, 4, 5`)*
   - **ความยาวเส้นทาง (Length):** **2 ขอบ (2 edges)**
2. **เส้นทางจาก 1 ไปยัง 7:**
   - จากตาราง: $p_v(7) = 2 \implies p_v(2) = 1 \implies$ จุดเริ่มต้น
   - **เส้นทาง (Shortest Path):** **`1, 2, 7`** *(หรือ `1, 4, 7`)*
   - **ความยาวเส้นทาง (Length):** **2 ขอบ (2 edges)**

> [!CAUTION] **กับดักได้ 0 คะแนนของ อ.ประดิษฐ์:**
> - ห้ามใส่ลูกศร `1 -> 2 -> 5` เด็ดขาด ต้องเขียนคั่นด้วยจุลภาค `1, 2, 5` เท่านั้น
> - ความยาวของเส้นทางนับจำนวนเส้นเชื่อม (2) ห้ามตอบหน่วยไม้บรรทัด (เช่น 2 ซม.) หรือจำนวนจุดยอด (3)

---

## Part 7: Properties, Formulas & Memory Percentage Calculations (10 คะแนน) (ชุดที่ 1)

### ข้อ 7: Theory, Properties & Percentage Calculations (10 คะแนน) *(รวมทุกประเด็นรั่วจากเทปบรรยายและข้อสอบจริงหน้า 5/5)*
**Question (EN) & (คำแปลไทย):**

- **7.1 (2 Marks):** Name a data structure that has **two fundamental properties**, and name a data structure that has **three fundamental properties**. State those properties clearly.  
  *(จงบอกชื่อโครงสร้างข้อมูลที่มี 2 properties และโครงสร้างข้อมูลที่มี 3 properties พร้อมระบุ properties เหล่านั้น)*
- **7.2 (2 Marks):** What are the **three ideal properties** of a hash function in theoretical computer science? Which one of these three is **impossible to achieve in practical reality**, and what are the **two specific reasons** why it is impossible?  
  *(คุณสมบัติของ hash function ในทางอุดมคติ 3 ข้อคืออะไร? ข้อใดเป็นไปไม่ได้ในความเป็นจริง และด้วยเหตุผล 2 ประการใด?)*
- **7.3 (2 Marks):** In an **Adjacency Matrix** representation of a directed graph with $|V| = 7$ vertices and $|E| = 12$ edges:
  - What percentage of the total memory space is used for entries with a value of **`1`**?
  - What percentage of the total memory space is wasted on entries with a value of **`0`**?  
  *(ในการแทนกราฟ 7 จุดยอด 12 เส้นเชื่อมด้วย Adjacency Matrix: ช่องที่มีค่าเป็น 1 ใช้พื้นที่ไปกี่เปอร์เซ็นต์? และช่องที่มีค่าเป็น 0 สิ้นเปลืองไปกี่เปอร์เซ็นต์?)*
- **7.4 (1 Mark):** For a directed graph with $|V| = 10$ vertices and $|E| = 20$ edges:
  - How many memory slots are required if implemented using an **Adjacency Matrix**?
  - How many memory slots are required if implemented using an **Adjacency List**?
  - What percentage of memory is saved by using the Adjacency List?  
  *(สำหรับกราฟมีทิศทาง 10 จุดยอด 20 เส้นเชื่อม: Adjacency Matrix ใช้พื้นที่กี่ช่อง? Adjacency List ใช้กี่ช่อง? และประหยัดหน่วยความจำได้กี่เปอร์เซ็นต์?)*
- **7.5 (1 Mark):** An undirected **Complete Graph** has $V = 16$ vertices. How many total edges does it have? Calculate the exact integer answer. *(Answering in formula form yields 0 marks).*  
  *(Undirected Complete Graph มี 16 จุดยอด จะมีจำนวนเส้นเชื่อมทั้งหมดกี่เส้น? ตอบเป็นตัวเลขจำนวนเต็มเท่านั้น)*
- **7.6 (1 Mark):** A **Complete Binary Tree** has a height of $h = 16$ (where root height = 0). What are the **minimum** and **maximum** possible numbers of nodes in this tree? Answer as exact integer values. *(Answers left in exponent power form yield 0 marks).*  
  *(Complete Binary Tree สูง 16 ชั้น จะมีจำนวนโหนดน้อยที่สุดและมากที่สุดเท่าใด? ตอบเป็นตัวเลขจำนวนเต็ม ห้ามติดเลขยกกำลัง)*
- **7.7 (1 Mark):** Write the exact statement in Python or C++ to replace the `HashEntry` creation in `insert` function:  
  `array[ currentPos ] = HashEntry( x, ACTIVE );`  
  *(จงเขียน Statement เพื่อใช้แทนการเรียก HashEntry ในเมธอด insert)*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 7):

##### 7.1 โครงสร้างที่มี 2 Properties และ 3 Properties:
- **โครงสร้างที่มี 2 Properties:** **Binary Heap**
  1. *Structure Property* (ต้องเป็น Complete Binary Tree)
  2. *Heap-Order Property* (โหนดแม่ต้อง $\le$ โหนดลูกสำหรับ Min-Heap)
- **โครงสร้างที่มี 3 Properties:** **AVL Tree**
  1. *Binary Tree Property* (ทุกโหนดมีลูกไม่เกิน 2 คน)
  2. *BST Property* (Left < Root < Right)
  3. *Balance Property* (ความสูงของ Subtree ซ้ายและขวาต่างกันไม่เกิน 1: $|\text{height}(L) - \text{height}(R)| \le 1$)

##### 7.2 คุณสมบัติ 3 ประการของ Hash Function ในทางอุดมคติ:
1. **Deterministic:** คีย์เดียวกันต้องได้ค่าแฮชเดิมเสมอ
2. **Uniform Distribution:** กระจายคีย์ลงทุกช่องในตารางเท่าๆ กันอย่างสม่ำเสมอ
3. **Fast Computation:** คำนวณได้รวดเร็วในเวลาคงที่ $O(1)$
- **ข้อที่เป็นไปไม่ได้ในทางปฏิบัติ:** **Uniform Distribution (การกระจายตัวอย่างสม่ำเสมอโดยไม่เกิดการชนกัน)**
- **เหตุผล 2 ประการ:**
  1. **Pigeonhole Principle (หลักการรังนกพิราบ):** ขอบเขตของคีย์อินพุตในจักรวาล ($U$) มีขนาดใหญ่กว่าขนาดของตารางแฮช ($M$) มากมหาศาล ($|U| \gg M$) จึงหลีกเลี่ยงการชนกันไม่ได้
  2. **Key Pattern Clustering (การเกาะกลุ่มของข้อมูลจริง):** ข้อมูลในโลกความเป็นจริงมักมีรูปแบบซ้ำซ้อน ไม่ได้กระจายแบบสุ่มแท้จริง

##### 7.3 การคำนวณเปอร์เซ็นต์ Memory Waste ใน Adjacency Matrix ($V = 7, E = 12$):
- ขนาดตาราง Matrix ทั้งหมด: $7 \times 7 = \mathbf{49} \text{ ช่อง}$
- ช่องที่มีค่าเป็น 1 (มีเส้นเชื่อมจริง): $12$ ช่อง
  $$\text{Percentage of Value 1} = \frac{12}{49} \times 100 = \mathbf{24.49\%} \quad (\text{หรือ } 24.48\%)$$
- ช่องที่มีค่าเป็น 0 (ช่องว่าง/สิ้นเปลือง): $49 - 12 = 37$ ช่อง
  $$\text{Percentage of Value 0 (Wasted)} = \frac{37}{49} \times 100 = \mathbf{75.51\%} \quad (\text{หรือ } 75.52\%)$$

##### 7.4 การเปรียบเทียบพื้นที่ Matrix vs List ($V = 10, E = 20$):
- **Adjacency Matrix ใช้:** $|V|^2 = 10^2 = \mathbf{100} \text{ ช่อง}$
- **Adjacency List ใช้:** $|V| + |E| = 10 + 20 = \mathbf{30} \text{ ช่อง}$
- **ประหยัดพื้นที่ได้:** $\frac{100 - 30}{100} \times 100 = \mathbf{70.0\%}$

##### 7.5 จำนวนเส้นของ Complete Graph ($V = 16$):
$$\text{Edges} = \frac{V(V - 1)}{2} = \frac{16 \times 15}{2} = \frac{240}{2} = \mathbf{120} \text{ เส้น}$$
*(กฎเหล็ก: ต้องตอบตัวเลข 120 เท่านั้น ห้ามตอบ $16 \times 15 / 2$)*

##### 7.6 จำนวนโหนดใน Complete Binary Tree สูง $h = 16$:
- **น้อยที่สุด (Min Nodes):** เมื่อชั้นล่างสุดมีโหนดชิดซ้ายเพียง 1 โหนด:
  $$\text{Min} = 2^{16} = \mathbf{65,536} \text{ โหนด}$$
- **มากที่สุด (Max Nodes):** เมื่อเต็มทุกชั้นอย่างสมบูรณ์ (Full Binary Tree):
  $$\text{Max} = 2^{16 + 1} - 1 = 2^{17} - 1 = 131,072 - 1 = \mathbf{131,071} \text{ โหนด}$$
*(กฎเหล็ก: ต้องตอบตัวเลขจำนวนเต็ม 65,536 และ 131,071 เท่านั้น ห้ามตอบ $2^{16}$)*

##### 7.7 Statement แทน HashEntry:
ในภาษา Python / C++ สำหรับ Hash Table ที่เก็บ tuple หรือ object:
```python
# ใน Python:
self.array[currentPos] = (x, ACTIVE)
# หรือกำหนดค่า attributes โดยตรง:
self.array[currentPos].element = x
self.array[currentPos].info = ACTIVE
```

---
---

# 🚀 ชุดที่ 2: เก็งข้อสอบปลายภาคชุดประยุกต์ใหม่ 2026 (Predicted Final Exam Suite)
*(ชุดซ้อมมือเข้มข้น ออกแบบเพื่อดักจุดรั่วที่อาจารย์เน้นย้ำในคาบสุดท้ายและสไลด์ New-Lectures)*

---

## Part 1: Hashing: Quadratic Probing, Secondary Clustering & Rehashing % (10 คะแนน) (ชุดที่ 2)

### ข้อ 1: Quadratic Probing, Secondary Clustering & Perfect Square Collision (10 คะแนน)
**Question (EN):**  
Given an empty Hash Table of size $\text{TableSize} = 11$ (indices $0$ to $10$). The collision resolution strategy is **Open Addressing with Quadratic Probing**:
$$h_i(X) = (h_0(X) + i^2) \bmod 11 \quad \text{where } h_0(X) = X \bmod 11$$

- **1.1 (4 Marks):** Sequentially insert keys: `47, 25, 36, 14, 58, 69`. Show the probe sequence calculation for each key and fill the hash table.
- **1.2 (2 Marks):** Define **Secondary Clustering** in English and contrast it with **Primary Clustering**. Why does Quadratic Probing guarantee finding an empty cell if TableSize is prime and table is less than half full?
- **1.3 (2 Marks):** Explain the **Perfect Square Collision Phenomenon** discussed in lecture. If keys inserted are squares of integers ($0^2, 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, \dots$) into a table of size 10 ($X \bmod 10$), which two keys form the very **first collision pair**, and at which cell index do they collide?
- **1.4 (2 Marks):** If Rehashing occurs when the load factor $\lambda \ge 0.5$ ($50\%$), how many elements can be stored in this table before rehashing is triggered? What should be the new TableSize after Rehashing?

---

**(คำแปลไทย):**  
*(กำหนดตารางแฮชขนาด 11 ช่อง ใช้ Quadratic Probing: $h_i(X) = (X \bmod 11 + i^2) \bmod 11$)*  
- *1.1 (4 คะแนน): จงแทรกข้อมูล `47, 25, 36, 14, 58, 69` แสดงวิธีคิดทีละขั้นตอนและเขียนตารางแฮช*  
- *1.2 (2 คะแนน): จงอธิบาย Secondary Clustering เป็นภาษาอังกฤษ เปรียบเทียบกับ Primary Clustering และบอกทฤษฎีการันตีช่องว่างของ Quadratic Probing*  
- *1.3 (2 คะแนน): ปรากฏการณ์การชนของเลขยกกำลังสองสมบูรณ์ (Perfect Square Collision) เมื่อนำ $0^2, 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, \dots$ mod 10 คู่ใดชนกันเป็นคู่แรก และชนที่ช่องใด?*  
- *1.4 (2 คะแนน): ถ้า Rehash เมื่อ $\lambda \ge 50\%$ ตารางนี้ใส่ได้กี่ตัวก่อน Rehash และตารางใหม่ควรมีขนาดเท่าใด?*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 1 - ชุดที่ 2):

##### 1.1 การคำนวณและผลลัพธ์ตาราง:
1. `47`: $47 \bmod 11 = \mathbf{3} \implies$ ลงช่อง **3** (ชน 0)
2. `25`: $25 \bmod 11 = \mathbf{3}$ (ชนช่อง 3 กับ 47)  
   $i=1: (3 + 1^2) \bmod 11 = \mathbf{4} \implies$ ลงช่อง **4** (ชน 1)
3. `36`: $36 \bmod 11 = \mathbf{3}$ (ชนช่อง 3 กับ 47)  
   $i=1: (3 + 1) \bmod 11 = 4$ (ชนช่อง 4 กับ 25)  
   $i=2: (3 + 2^2) \bmod 11 = 7 \bmod 11 = \mathbf{7} \implies$ ลงช่อง **7** (ชน 2)
4. `14`: $14 \bmod 11 = \mathbf{3}$ (ชนช่อง 3)  
   $i=1: (3 + 1) \bmod 11 = 4$ (ชนช่อง 4)  
   $i=2: (3 + 4) \bmod 11 = 7$ (ชนช่อง 7)  
   $i=3: (3 + 3^2) \bmod 11 = 12 \bmod 11 = \mathbf{1} \implies$ ลงช่อง **1** (ชน 3)
5. `58`: $58 \bmod 11 = \mathbf{3}$ (ชนช่อง 3)  
   $i=1: 4$ (ชน), $i=2: 7$ (ชน), $i=3: 1$ (ชน)  
   $i=4: (3 + 4^2) \bmod 11 = 19 \bmod 11 = \mathbf{8} \implies$ ลงช่อง **8** (ชน 4)
6. `69`: $69 \bmod 11 = \mathbf{3}$ (ชนช่อง 3)  
   $i=1..4$ ชนทั้งหมด  
   $i=5: (3 + 5^2) \bmod 11 = 28 \bmod 11 = \mathbf{6} \implies$ ลงช่อง **6** (ชน 5)

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Key** | - | **14** | - | **47** | **25** | - | **69** | **36** | **58** | - | - |

##### 1.2 นิยาม Secondary Clustering:
- **English Definition:** *"Secondary Clustering occurs when keys that hash to the exact same initial position follow the identical probe sequence because $f(i) = i^2$ is fixed."*
- **ทฤษฎีการันตี:** หาก TableSize เป็นจำนวนเฉพาะ และ Load Factor $\lambda < 0.5$ รับประกันว่า Quadratic Probing จะพบช่องว่างเสมอเสมอโดยไม่ติดลูปอนันต์

##### 1.3 Perfect Square Collision:
- $0^2=0, 1^2=1, 2^2=4, 3^2=9$
- $4^2 = 16 \bmod 10 = \mathbf{6}$
- $5^2 = 25 \bmod 10 = 5$
- $6^2 = 36 \bmod 10 = \mathbf{6}$
- **คู่แรกที่ชนกันคือ:** **`16` และ `36`** โดยชนที่ช่อง **`6`**

##### 1.4 Rehashing Analysis:
- ความจุ $50\%$: $\lfloor 11 \times 0.5 \rfloor = \mathbf{5} \text{ ตัว}$ (ใส่ตัวที่ 6 จะเกิด Rehash)
- ขนาดตารางใหม่: ต้องเป็นจำนวนเฉพาะที่มากกว่า $2 \times \text{TableSize} = 2 \times 11 = 22 \implies \mathbf{23}$

---

## Part 2: Binary Heap: BuildHeap, Sequential Insert & DeleteMin Array Mapping (10 คะแนน) (ชุดที่ 2)

### ข้อ 2: Min-Heap BuildHeap Algorithm & Tree-to-Array Conversion (10 คะแนน)
**Question (EN):**  
Given an arbitrary unordered array of 10 elements stored at indices 1 to 10:
$$[-, \; 70, \; 40, \; 30, \; 20, \; 60, \; 50, \; 10, \; 90, \; 80, \; 15]$$

- **2.1 (4 Marks):** Trace the **`buildHeap`** algorithm (Percolate Down starting from index $\lfloor N/2 \rfloor = 5$ down to index 1). Show the state of the array after each step.
- **2.2 (3 Marks):** Draw the complete binary tree corresponding to the final heap array from 2.1.
- **2.3 (3 Marks):** Perform `deleteMin()` twice. Show the extracted minimum values and the final array state.

---

**(คำแปลไทย):**  
*(กำหนดอาร์เรย์เริ่มต้น 10 ตัว: `[-, 70, 40, 30, 20, 60, 50, 10, 90, 80, 15]`)*  
- *2.1 (4 คะแนน): จง Trace ขั้นตอนวิธี `buildHeap` โดย Percolate Down จากดัชนี $\lfloor 10/2 \rfloor = 5$ ถอยลงมาถึงดัชนี 1*  
- *2.2 (3 คะแนน): จงวาดภาพ Complete Binary Tree จากอาร์เรย์ผลลัพธ์ของ 2.1*  
- *2.3 (3 คะแนน): ทำการ `deleteMin()` 2 ครั้ง แสดงค่าที่ถูกลบและอาร์เรย์สุดท้าย*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 2 - ชุดที่ 2):

##### 2.1 การทำ BuildHeap (Index 5 ถอยไป 1):
1. **$i = 5$ (ค่า 60):** ลูกคือ index 10 (ค่า 15) $\rightarrow 15 < 60 \implies$ สลับ 60 กับ 15  
   Array: `[-, 70, 40, 30, 20, 15, 50, 10, 90, 80, 60]`
2. **$i = 4$ (ค่า 20):** ลูกคือ index 8 (90) และ index 9 (80) $\rightarrow 20 < 80 \implies$ อยู่ตำแหน่งเดิม
3. **$i = 3$ (ค่า 30):** ลูกคือ index 6 (50) และ index 7 (10) $\rightarrow$ ลูกที่น้อยกว่าคือ 10 (index 7) $\rightarrow 10 < 30 \implies$ สลับ 30 กับ 10  
   Array: `[-, 70, 40, 10, 20, 15, 50, 30, 90, 80, 60]`
4. **$i = 2$ (ค่า 40):** ลูกคือ index 4 (20) และ index 5 (15) $\rightarrow$ ลูกที่น้อยกว่าคือ 15 $\rightarrow 15 < 40 \implies$ สลับ 40 กับ 15. จากนั้น 40 เทียบกับลูกที่ index 10 (60) $\rightarrow 40 < 60$ หยุด!  
   Array: `[-, 70, 15, 10, 20, 40, 50, 30, 90, 80, 60]`
5. **$i = 1$ (ค่า 70):** ลูกคือ index 2 (15) และ index 3 (10) $\rightarrow$ ลูกที่น้อยกว่าคือ 10 $\rightarrow$ สลับ 70 กับ 10.  
   ต่อมา 70 อยู่ที่ index 3 ลูกคือ index 6 (50) และ index 7 (30) $\rightarrow$ สลับ 70 กับ 30.  
   Array: `[-, 10, 15, 30, 20, 40, 50, 70, 90, 80, 60]`

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Final Heap** | `-` | **10** | **15** | **30** | **20** | **40** | **50** | **70** | **90** | **80** | **60** |

##### 2.3 การทำ deleteMin() 2 ครั้ง:
- **ครั้งที่ 1:** ดึง **`10`** ออก, นำ 60 มาวางที่ root, percolate down ผ่าน 15 และ 20:  
  `[-, 15, 20, 30, 60, 40, 50, 70, 90, 80]` &bull; *(ลบ 10 ออก)*
- **ครั้งที่ 2:** ดึง **`15`** ออก, นำ 80 มาวางที่ root, percolate down ผ่าน 20 และ 40:  
  `[-, 20, 40, 30, 60, 80, 50, 70, 90]` &bull; *(ลบ 15 ออก)*

---

## Part 3: Insertion Sort: Worst Case Analysis & Intermediate Pass Tracing (10 คะแนน) (ชุดที่ 2)

### ข้อ 3: Insertion Sort Tracing on Real Exam Data (10 คะแนน)
**Question (EN):**  
Given the 10-element array:
$$[34, \; 8, \; 64, \; 51, \; 32, \; 21, \; 15, \; 9, \; 40, \; 2]$$

- **3.1 (5 Marks):** Trace the array state after each pass from $p = 1$ to $p = 5$.
- **3.2 (3 Marks):** For Pass $p = 4$ (key 32) and Pass $p = 5$ (key 21), state the number of comparisons and position moves executed.
- **3.3 (2 Marks):** Under what condition does Insertion Sort achieve its **Best-Case** time complexity of $O(N)$? How many position moves occur in the Best Case?

---

**(คำแปลไทย):**  
*(กำหนดอาร์เรย์ 10 ตัว: `[34, 8, 64, 51, 32, 21, 15, 9, 40, 2]`)*  
- *3.1 (5 คะแนน): จง Trace ค่าในอาร์เรย์หลังจบรอบ $p = 1$ ถึง $p = 5$*  
- *3.2 (3 คะแนน): ในรอบ $p = 4$ (คีย์ 32) และ $p = 5$ (คีย์ 21) มีการเปรียบเทียบและย้ายตำแหน่งกี่ครั้ง*  
- *3.3 (2 คะแนน): Insertion Sort จะมี Best-Case เป็น $O(N)$ ภายใต้เงื่อนไขใด และเกิด Position Move กี่ครั้ง?*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 3 - ชุดที่ 2):

##### 3.1 Tracing รอบที่ 1 ถึง 5:
- **Pass 1 ($tmp = 8$):** เลื่อน 34 $\rightarrow$ `[8, 34, 64, 51, 32, 21, 15, 9, 40, 2]`
- **Pass 2 ($tmp = 64$):** $64 > 34 \rightarrow$ ไม่เลื่อน $\rightarrow$ `[8, 34, 64, 51, 32, 21, 15, 9, 40, 2]`
- **Pass 3 ($tmp = 51$):** เลื่อน 64 $\rightarrow$ `[8, 34, 51, 64, 32, 21, 15, 9, 40, 2]`
- **Pass 4 ($tmp = 32$):** เลื่อน 64, 51, 34 $\rightarrow$ `[8, 32, 34, 51, 64, 21, 15, 9, 40, 2]`
- **Pass 5 ($tmp = 21$):** เลื่อน 64, 51, 34, 32 $\rightarrow$ `[8, 21, 32, 34, 51, 64, 15, 9, 40, 2]`

##### 3.2 จำนวนครั้งใน Pass 4 และ Pass 5:
- **Pass $p = 4$ (คีย์ 32):** เปรียบเทียบ 4 ครั้ง, **Position Moves = 3 ครั้ง** ($j = 1$)
- **Pass $p = 5$ (คีย์ 21):** เปรียบเทียบ 5 ครั้ง, **Position Moves = 4 ครั้ง** ($j = 1$)

##### 3.3 Best-Case Analysis:
- เกิดขึ้นเมื่อ **ข้อมูลในอาร์เรย์เรียงลำดับจากน้อยไปมากอยู่แล้ว (Already Sorted in Ascending Order)**
- จำนวน Position Moves เท่ากับ **0 ครั้ง** (เปรียบเทียบ $N-1$ ครั้ง ใช้เวลา $O(N)$)

---

## Part 4: Selection Sort vs Bubble Sort: Inversions, Comparisons & Early Exit (10 คะแนน) (ชุดที่ 2)

### ข้อ 4: Detailed Mechanics Comparison & Inversions (10 คะแนน)
**Question (EN):**  
Given array $A = [29, \; 10, \; 14, \; 37, \; 13]$ ($N = 5$).
- **4.1 (4 Marks):** Trace Bubble Sort pass-by-pass. Show adjacent element comparisons and swaps.
- **4.2 (4 Marks):** Trace Selection Sort pass-by-pass. Show minimum element searches and swaps.
- **4.3 (2 Marks):** Explain why Bubble Sort's swap count is strictly equal to the number of **Inversions** in the original array, whereas Selection Sort executes at most $N-1$ swaps regardless of inversions.

---

**(คำแปลไทย):**  
*(กำหนดอาร์เรย์ $A = [29, 10, 14, 37, 13]$ ขนาด 5 ตัว)*  
- *4.1 (4 คะแนน): จง Trace Bubble Sort ทีละรอบ แสดงการเปรียบเทียบคู่ติดกันและการสลับ*  
- *4.2 (4 คะแนน): จง Trace Selection Sort ทีละรอบ แสดงการหาค่าน้อยสุดและการสลับ*  
- *4.3 (2 คะแนน): จงอธิบายว่าทำไมจำนวนครั้งที่สลับของ Bubble Sort จึงเท่ากับจำนวน Inversion ในอาร์เรย์เริ่มต้นอย่างแม่นยำ ขณะที่ Selection Sort สลับไม่เกิน $N-1$ ครั้งเสมอ*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 4 - ชุดที่ 2):

##### 4.1 Bubble Sort Tracing:
- **Pass 1:** $(29,10)\to$สลับ, $(29,14)\to$สลับ, $(29,37)$, $(37,13)\to$สลับ  
  State: `[10, 14, 29, 13, 37]` *(สลับ 3 ครั้ง)*
- **Pass 2:** $(10,14)$, $(14,29)$, $(29,13)\to$สลับ  
  State: `[10, 14, 13, 29, 37]` *(สลับ 1 ครั้ง)*
- **Pass 3:** $(10,14)$, $(14,13)\to$สลับ  
  State: `[10, 13, 14, 29, 37]` *(สลับ 1 ครั้ง)*
- **Pass 4:** ตรวจสอบ ไม่มีการสลับ (`swapped == False`) $\rightarrow$ จบการทำงาน  
  **จำนวนสลับรวม = 5 ครั้ง**

##### 4.2 Selection Sort Tracing:
- Pass 1: Min is 10 (idx 1) $\rightarrow$ swap with idx 0 $\rightarrow$ `[10, 29, 14, 37, 13]` (Swap 1)
- Pass 2: Min is 13 (idx 4) $\rightarrow$ swap with idx 1 $\rightarrow$ `[10, 13, 14, 37, 29]` (Swap 2)
- Pass 3: Min is 14 (idx 2) $\rightarrow$ already at pos $\rightarrow$ `[10, 13, 14, 37, 29]` (Swap 0)
- Pass 4: Min is 29 (idx 4) $\rightarrow$ swap with idx 3 $\rightarrow$ `[10, 13, 14, 29, 37]` (Swap 3)
- **จำนวนสลับรวม = 3 ครั้ง**

##### 4.3 ทฤษฎี Inversion:
- คู่ Inversion ในอาร์เรย์เดิมคือคู่ $(i, j)$ ที่ $i < j$ แต่ $A[i] > A[j]$:
  $(29,10), (29,14), (29,13), (37,13), (14,13) \implies \mathbf{5} \text{ คู่}$
- Bubble Sort สลับเฉพาะคู่ติดกัน จึงขจัด Inversion ได้ทีละ 1 คู่เสมอ ทำให้จำนวนสลับ $= 5$ ครั้งเท่ากับจำนวน Inversion พอดี
- ส่วน Selection Sort ข้ามไปสลับกับตัวที่น้อยที่สุดโดยตรง จึงสามารถขจัด Inversion ได้หลายคู่ในการสลับเพียงครั้งเดียว ทำให้จำนวนสลับรวมน้อยกว่า ($3$ ครั้ง)

---

## Part 5: Topological Sort: DAG with Disconnected Components & Cycle Detection (10 คะแนน) (ชุดที่ 2)

### ข้อ 5: Topological Sort with Kahn's Algorithm & Cycle Analysis (10 คะแนน)
**Question (EN):**  
Given the Directed Graph $G = (V, E)$ with 6 vertices:
- $A \rightarrow B, C$
- $B \rightarrow D$
- $C \rightarrow D, E$
- $D \rightarrow F$
- $E \rightarrow F$
- $F \rightarrow \emptyset$

- **5.1 (5 Marks):** Trace Kahn's algorithm by completing the Indegree array and Circular Queue state (size 6) at every step.
- **5.2 (3 Marks):** Write the resulting Topological Ordering. Is the ordering unique? Why or why not?
- **5.3 (2 Marks):** If a directed edge $F \rightarrow C$ is added to the graph, what happens when Kahn's algorithm is executed? Explain how the algorithm detects cycles.

---

**(คำแปลไทย):**  
*(กำหนดกราฟมีทิศทาง 6 จุดยอด $A, B, C, D, E, F$)*  
- *5.1 (5 คะแนน): จง Trace ขั้นตอนวิธีของ Kahn แสดง Indegree array และ Circular Queue (ขนาด 6 ช่อง)*  
- *5.2 (3 คะแนน): จงเขียน Topological Ordering ผลลัพธ์ และอธิบายว่าผลลัพธ์มีรูปแบบเดียวหรือไม่ เพราะเหตุใด*  
- *5.3 (2 คะแนน): หากเพิ่มเส้นเชื่อม $F \rightarrow C$ เข้าไปในกราฟ จะเกิดอะไรขึ้นเมื่อรันขั้นตอนวิธี และขั้นตอนวิธีตรวจจับ Cycle ได้อย่างไร?*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 5 - ชุดที่ 2):

##### 5.1 ตาราง Indegree และ Queue:
- Indegree เริ่มต้น: $A: 0, \; B: 1, \; C: 1, \; D: 2, \; E: 1, \; F: 2$
- Queue เริ่มต้น: `[A]`
- R1: Dequeue A $\rightarrow$ ลด B เหลือ 0, ลด C เหลือ 0 $\implies$ Enqueue B, C $\rightarrow$ Queue: `[B, C]`
- R2: Dequeue B $\rightarrow$ ลด D จาก 2 เหลือ 1 $\rightarrow$ Queue: `[C]`
- R3: Dequeue C $\rightarrow$ ลด D จาก 1 เหลือ 0, ลด E จาก 1 เหลือ 0 $\implies$ Enqueue D, E $\rightarrow$ Queue: `[D, E]`
- R4: Dequeue D $\rightarrow$ ลด F จาก 2 เหลือ 1 $\rightarrow$ Queue: `[E]`
- R5: Dequeue E $\rightarrow$ ลด F จาก 1 เหลือ 0 $\implies$ Enqueue F $\rightarrow$ Queue: `[F]`
- R6: Dequeue F $\rightarrow$ Queue ว่าง

##### 5.2 ผลลัพธ์ Topological Ordering:
$$\mathbf{A, \; B, \; C, \; D, \; E, \; F} \quad (\text{หรือ } A, C, B, E, D, F)$$
- **ความไม่เป็นเอกลักษณ์ (Not Unique):** ลำดับ **ไม่เป็นเอกลักษณ์** เพราะในรอบที่ 1 ทั้ง B และ C มี Indegree เป็น 0 พร้อมกัน ทำให้สามารถเลือกประมวลผลตัวใดก่อนก็ได้

##### 5.3 ผลกระทบเมื่อมี Cycle ($F \rightarrow C$):
- วงรอบ $C \rightarrow D \rightarrow F \rightarrow C$ จะทำให้โหนดในวงรอบมี Indegree ไม่มีทางลดลงเป็น 0
- ส่งผลให้ Queue ว่างเปล่าก่อนที่จุดยอดทุกตัวจะถูกประมวลผลครบ ($N_{\text{processed}} < |V|$) ระบบจึงตรวจพบทันทีว่า **กราฟมี Cycle และไม่สามารถหา Topological Sort ได้**

---

## Part 6: Unweighted Shortest Path: Complex 7-Vertex Graph with Backtracking (10 คะแนน) (ชุดที่ 2)

### ข้อ 6: Unweighted Shortest Path on Assignment 4 Model (10 คะแนน) *(แบบจำลองทางการห้องเรียน)*
**Question (EN):**  
Given the graph from Assignment 4 with vertices $\{A, B, C, D, E, F, G\}$ and Adjacency List:
- $A \rightarrow B, C$
- $B \rightarrow C, E, G$
- $C \rightarrow D, E$
- $D \rightarrow A, F$
- $E \rightarrow D, F$
- $F \rightarrow \emptyset$
- $G \rightarrow E$

- **6.1 (5 Marks):** Using **Start Vertex = A**, fill the complete BFS table (`Known`, `Dist`, `Path`).
- **6.2 (2 Marks):** State the dequeue sequence from the queue.
- **6.3 (3 Marks):** Write down the shortest path and path length from $A$ to $D$, and from $A$ to $F$.

---

**(คำแปลไทย):**  
*(กำหนดกราฟใบงาน Assignment 4 จุดยอด $A, B, C, D, E, F, G$)*  
- *6.1 (5 คะแนน): ให้จุดเริ่มต้นคือ $A$ จงเขียนตาราง Known, Dist, Path ฉบับสมบูรณ์*  
- *6.2 (2 คะแนน): ระบุลำดับการ Dequeue ออกจาก Queue*  
- *6.3 (3 คะแนน): เขียนเส้นทางและความยาวเส้นทางที่สั้นที่สุดจาก $A$ ไป $D$ และจาก $A$ ไป $F$*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 6 - ชุดที่ 2):

##### 6.1 ตารางผลลัพธ์สุดท้าย (Start = A):
| Vertex | Known | Dist ($d_v$) | Path ($p_v$) |
| :---: | :---: | :---: | :---: |
| **A** | **T** | **0** | **0** |
| **B** | **T** | **1** | **A** |
| **C** | **T** | **1** | **A** |
| **D** | **T** | **2** | **C** |
| **E** | **T** | **2** | **B** |
| **F** | **T** | **3** | **D** (or E) |
| **G** | **T** | **2** | **B** |

##### 6.2 ลำดับการ Dequeue:
$$\mathbf{A, \; B, \; C, \; E, \; G, \; D, \; F}$$

##### 6.3 เส้นทางและระยะทาง:
1. **เส้นทางจาก A ไปยัง D:**  
   $p_v(D) = C \implies p_v(C) = A \implies$ **`A, C, D`** &bull; **Length = 2 edges**
2. **เส้นทางจาก A ไปยัง F:**  
   $p_v(F) = D \implies p_v(D) = C \implies p_v(C) = A \implies$ **`A, C, D, F`** &bull; **Length = 3 edges**

---

## Part 7: Rapid-Fire Sub-Questions: Tree Heights, Graph Densities & RAM Waste (10 คะแนน) (ชุดที่ 2)

### ข้อ 7: Comprehensive Mathematical & Theoretical Quiz (10 คะแนน)
**Question (EN) & (คำแปลไทย):**
- **7.1 (2 Marks):** An undirected complete graph $K_{10}$ has 10 vertices. How many edges does it contain? Calculate the exact integer. *(If answered as formula, 0 marks).*  
  *(Undirected Complete Graph 10 จุดยอด มีเส้นเชื่อมกี่เส้น? ตอบเป็นจำนวนเต็ม)*
- **7.2 (2 Marks):** A Binary Min-Heap has a height of $h = 10$. What are the minimum and maximum possible numbers of nodes in this heap? Calculate the exact integer values.  
  *(Binary Min-Heap สูง 10 ชั้น จะมีจำนวนโหนดน้อยที่สุดและมากที่สุดเท่าใด? ตอบเป็นจำนวนเต็ม)*
- **7.3 (2 Marks):** If a Directed Graph has 10 vertices and 20 edges, calculate the exact percentage of memory saved when switching from an Adjacency Matrix to an Adjacency List.  
  *(กราฟ 10 จุดยอด 20 เส้นเชื่อม Adjacency List ประหยัดหน่วยความจำกว่า Adjacency Matrix กี่เปอร์เซ็นต์?)*
- **7.4 (2 Marks):** Define the **Wrap-Around** concept in Hashing in English. Why must the table size be a prime number in Open Addressing?  
  *(จงนิยาม Wrap-Around ใน Hashing เป็นภาษาอังกฤษ และทำไม TableSize ต้องเป็นจำนวนเฉพาะ?)*
- **7.5 (2 Marks):** In Quicksort, how much faster is **Median-of-Three** partitioning compared to standard pivot selection (state the approximate percentage), and why does it prevent the $O(N^2)$ worst-case on sorted inputs?  
  *(Median-of-three ทำให้ Quicksort เร็วขึ้นกี่เปอร์เซ็นต์ และทำไมจึงป้องกันกรณีแย่สุด $O(N^2)$ บนข้อมูลที่เรียงแล้ว?)*

---

#### 💡 เฉลยและวิธีคิดอย่างละเอียด (Solution 7 - ชุดที่ 2):

##### 7.1 จำนวนเส้น $K_{10}$:
$$E = \frac{10 \times 9}{2} = \mathbf{45} \text{ เส้น}$$

##### 7.2 จำนวนโหนดใน Heap สูง $h = 10$:
- $\text{Min Nodes} = 2^{10} = \mathbf{1,024} \text{ โหนด}$
- $\text{Max Nodes} = 2^{10+1} - 1 = 2^{11} - 1 = \mathbf{2,047} \text{ โหนด}$

##### 7.3 เปอร์เซ็นต์การประหยัดหน่วยความจำ:
- Matrix: $10^2 = 100$ ช่อง, List: $10 + 20 = 30$ ช่อง
- ประหยัด: $\frac{100 - 30}{100} \times 100 = \mathbf{70.0\%}$

##### 7.4 นิยาม Wrap-Around และ TableSize จำนวนเฉพาะ:
- **English Definition:** *"When the hashed key index reaches or exceeds the last cell of the hash table, it wraps around back to the beginning of the table (index 0) by computing modulo TableSize."*
- **ทำไม TableSize ต้องเป็น Prime:** เพื่อป้องกันไม่ให้ระยะก้าวเดิน ($f(i)$ หรือ $s(X)$) มีตัวหารร่วมมากกับ TableSize ซึ่งจะทำให้การ Probe วนซ้ำแต่ช่องเดิมและไม่สามารถสำรวจช่องว่างอื่นๆ ได้ครบทั้งตาราง

##### 7.5 Median-of-Three Speedup:
- ทำให้ Quicksort ทำงานเร็วขึ้นประมาณ **$\approx 5\%$**
- ป้องกัน $O(N^2)$ เพราะการเลือกค่ามัธยฐานจาก 3 ค่า (ตัวแรก, ตัวกลาง, ตัวท้าย) รับประกันว่า Pivot จะไม่เป็นค่าน้อยสุดหรือมากสุดเด็ดขาด ทำให้การแบ่ง Partition สมดุลใกล้เคียงกึ่งกลางเสมอ แม้ข้อมูลจะเรียงลำดับมาแล้วก็ตาม

---

# 🛡️ สรุปกฎเหล็กและตารางกับดัก 0 คะแนน (Zero-Score Pitfalls Master Table)

| หัวข้อสอบ | ข้อผิดพลาดที่ได้ 0 คะแนน ❌ | คำตอบที่ได้คะแนนเต็ม 100% ✅ | เหตุผลทางวิชาการตามที่ อ.ประดิษฐ์ สอน |
| :--- | :--- | :--- | :--- |
| **การเขียน Shortest Path** | ใส่ลูกศร เช่น `1 -> 4 -> 5` หรือ `A -> B -> E` | คั่นด้วยจุลภาค **`1, 4, 5`** หรือ **`A, B, E`** | นิยาม Path คือลำดับของจุดยอด (Sequence of vertices) ห้ามใส่เครื่องหมายลูกศร |
| **หน่วยของความยาว Path** | ตอบเป็นหน่วยวัด เช่น 2 ซม., 3 นิ้ว | ตอบเป็นจำนวน **เส้น** หรือ **Edges** | ความยาวของทางเดินในทฤษฎีกราฟคือนับจำนวนเส้นเชื่อม ($N-1$) |
| **การนับจำนวนการชน (Collision)** | ตอบ 18 ครั้ง (นับชน 9 + แก้ชน 9) | ตอบ **9 ครั้ง** | อาจารย์ย้ำในห้อง: การชนพร้อมการแก้ชนในแต่ละรอบให้นับเป็น 1 ครั้ง |
| **Complete Graph $K_{10}$** | ตอบติดสูตร `10*(9)/2` หรือ `90/2` | ตอบตัวเลขจำนวนเต็ม **45** | กฎเหล็กห้ามตอบติดรูปสูตร ต้องคำนวณจนได้ตัวเลขสุดท้าย |
| **Heap Node Count ($h=10$)** | ตอบติดเลขยกกำลัง `2^10` หรือ `2^11 - 1` | ตอบตัวเลข **1,024** และ **2,047** | กฎเหล็กห้ามตอบติดเลขยกกำลัง เครื่องคิดเลขวิทยาศาสตร์นำเข้าได้ |
| **การหา Parent ใน Heap** | ปัดเศษขึ้น เช่น $7/2 = 3.5 \to 4$ | ตัดเศษทิ้ง **$7 // 2 = 3$** | ดัชนีอาร์เรย์ต้องเป็นจำนวนเต็มโดยใช้ Truncate Fraction |
| **Index 0 ของ Binary Heap** | วาง Root ที่ `array[0]` | **เว้นช่อง 0 ไว้เป็น `-` หรือ Sentinel** | เพื่อให้สูตร $2i, 2i+1, \lfloor i/2 \rfloor$ ทำงานถูกต้องโดยไม่มี Offset |
| **การเรียกเมธอด `deleteMin`** | ใส่พารามิเตอร์ เช่น `h.deleteMin(1)` | **`h.deleteMin()` (ไม่ใส่พารามิเตอร์)** | ฮีปลบตัวรากเสมอ เมธอดไม่มีการรับอาร์กิวเมนต์ |
| **การเลือกค่า $R$ Double Hash** | เลือกเลขคู่ หรือเลขมากกว่า TableSize | **$R$ ต้องเป็นจำนวนเฉพาะที่ $R < \text{TableSize}$** | ป้องกันก้าวเดินเป็น 0 และลดปัญหาการเกาะกลุ่ม |
| **Path บน Null Graph ($V=\emptyset$)** | เขียนเดา หรือเว้นว่าง | **"ไม่มี Path เพราะไม่มีโหนดในกราฟ"** | กราฟว่างไม่มีจุดยอด จึงไม่มีทางเดินใดๆ เกิดขึ้นได้ |
