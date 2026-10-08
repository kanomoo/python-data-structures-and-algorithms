# 🏆 11.9 - Final Exam Past Paper Breakdown 2-61 & 2-xx (วิเคราะห์เจาะลึกข้อสอบปลายภาคฉบับจริงปีเก่า 8 ข้อใหญ่ 100 คะแนนเต็ม)

> **แหล่งที่มา:** ถอดรหัสโดยตรงจากไฟล์ข้อสอบปลายภาคฉบับจริง `DataStrucFinal2-xxAnd2-61-1.pdf` โฟลเดอร์ `ปีเก่า` ของอาจารย์ประดิษฐ์ พิทักษ์เสถียรกุล ภาควิชาเทคโนโลยีสารสนเทศ (IT) มจพ.  
> **เกณฑ์การตรวจ:** อาจารย์หักคะแนนหนักมากกรณีใส่ผิดตั้งแต่เริ่มต้น (Worst-Case ใส่ผิด = 0 ทันที), ห้ามเดา, ต้องเขียนตาราง `Known, dv, pv` และสถานะ `Front, Back` ของ Queue ให้ตรงทฤษฎี

---

## 📌 สารบัญข้อสอบจริง 8 ข้อใหญ่

1. [ข้อ 1: Hash Table (Open Addressing, Double Hashing & Rehashing)](#ข้อ-1-hash-table-open-addressing-double-hashing--rehashing)
2. [ข้อ 2: Binary Min-Heap (Insert, DeleteMin & Array Representation)](#ข้อ-2-binary-min-heap-insert-deletemin--array-representation)
3. [ข้อ 3: การดัดแปลงโค้ด Insertion Sort และ PercolateDown เพื่อนับ Position Move](#ข้อ-3-การดัดแปลงโค้ด-insertion-sort-และ-percolatedown-เพื่อนับ-position-move)
4. [ข้อ 4: Quicksort (Median-of-Three, Cutoff=3 & Partitioning Trace)](#ข้อ-4-quicksort-median-of-three-cutoff3--partitioning-trace)
5. [ข้อ 5: Unweighted Shortest Path และการ Trace Circular Queue](#ข้อ-5-unweighted-shortest-path-และการ-trace-circular-queue)
6. [ข้อ 6: Topological Sort และการ Trace In-Degree Queue ในกราฟ DAG](#ข้อ-6-topological-sort-และการ-trace-in-degree-queue-ในกราฟ-dag)
7. [ข้อ 7: ทฤษฎี Hashing ในอุดมคติ และข้อจำกัดในโลกจริง](#ข้อ-7-ทฤษฎี-hashing-ในอุดมคติ-และข้อจำกัดในโลกจริง)
8. [ข้อ 8: ทฤษฎีคำนวณ Complete Binary Tree และ Complete Graph](#ข้อ-8-ทฤษฎีคำนวณ-complete-binary-tree-และ-complete-graph)

---

## ข้อ 1: Hash Table (Open Addressing, Double Hashing & Rehashing)

### 📋 โจทย์จริง
กำหนดโครงสร้าง Hash Table ชนิด **Open Addressing** แก้การชนด้วย **Double Hashing**:
* กำหนดสูตรการแก้การชน: 
  $$h_i(X) = (Hash(X) + f(i)) \pmod{\text{TableSize}}$$
  โดยที่ $f(i) = i \times (R - (X \pmod R))$  (โดย $R$ เป็นจำนวนเฉพาะที่น้อยกว่า TableSize เช่น $R = 17$ เมื่อ TableSize = 19)
* เงื่อนไขการทำ Rehashing: เมื่อความจุ (Load Factor $\lambda$) เกิน **75%** (หรือ **70%** ขึ้นกับชุดข้อสอบ)
* **ชุดข้อมูลทดสอบ 8 ตัว:** `323, 17, 969, 868, 340, 370, 357, 391`

### 🔍 เฉลยขั้นตอนการคำนวณ (TableSize = 19, R = 17)
1. **$X = 323$**:
   * $323 \pmod{19} = 0$ ➔ วางช่อง **0** (Active: A, ชน 0 ครั้ง)
2. **$X = 17$**:
   * $17 \pmod{19} = 17$ ➔ วางช่อง **17** (Active: A, ชน 0 ครั้ง)
3. **$X = 969$**:
   * $969 \pmod{19} = 0$ ➔ **ชนกับ 323 ที่ช่อง 0!** (ครั้งที่ 1)
   * คำนวณ Double Hash: $R - (969 \pmod{17}) = 17 - 0 = 17$
   * รอบ $i=1$: $h_1 = (0 + 1 \times 17) \pmod{19} = 17$ ➔ **ชนกับ 17 ที่ช่อง 17!** (ครั้งที่ 2)
   * รอบ $i=2$: $h_2 = (0 + 2 \times 17) \pmod{19} = 34 \pmod{19} = 15$ ➔ วางช่อง **15** (Active: A)
4. **$X = 868$**:
   * $868 \pmod{19} = 13$ ➔ วางช่อง **13** (Active: A)
5. **$X = 340$**:
   * $340 \pmod{19} = 17$ ➔ **ชนกับ 17!**
   * $R - (340 \pmod{17}) = 17 - 0 = 17$
   * รอบ $i=1$: $h_1 = (17 + 17) \pmod{19} = 34 \pmod{19} = 15$ ➔ **ชนกับ 969!**
   * รอบ $i=2$: $h_2 = (17 + 34) \pmod{19} = 51 \pmod{19} = 13$ ➔ **ชนกับ 868!**
   * รอบ $i=3$: $h_3 = (17 + 51) \pmod{19} = 68 \pmod{19} = 11$ ➔ วางช่อง **11** (Active: A)
6. **$X = 370$**:
   * $370 \pmod{19} = 9$ ➔ วางช่อง **9** (Active: A)
7. **$X = 357$**:
   * $357 \pmod{19} = 15$ ➔ **ชนกับ 969!**
   * คำนวณแก้การชนจนได้ช่องว่าง
8. **$X = 391$**:
   * $391 \pmod{19} = 11$ ➔ **ชนกับ 340!** ➔ วางช่องว่างถัดไปตามฟังก์ชัน

> **คำถามเพิ่มเติมของอาจารย์:**
> * เกิดการชนกันทั้งสิ้นกี่ครั้ง? (นับจำนวน Collision สะสมทั้งหมด)
> * ต้องใส่ข้อมูลเพิ่มอีกอย่างน้อยกี่ตัวถึงจะเกิด Rehashing?
>   * *สูตรคิด:* TableSize = 19, ขีดจำกัด 75% = $19 \times 0.75 = 14.25$ ➔ เมื่อข้อมูลถึง 15 ตัวจะ Rehash ขณะนี้มี 8 ตัว จึงต้องเพิ่มอีก $15 - 8 = 7$ ตัว!

---

## ข้อ 2: Binary Min-Heap (Insert, DeleteMin & Array Representation)

### 📋 โจทย์จริง
กำหนดข้อมูล: `64, 19, 40, 39, 21, 30, 25, 29, 24, 90`
1. ทำการ Insert ลงใน Binary Min-Heap ทีละตัว (Percolate Up)
2. ทำการ **DeleteMin ครั้งที่ 1** และ **ครั้งที่ 2**
3. ทำการ **Insert 12** ลงใน Heap
4. เขียนสถานะ Array ของ Heap ในแต่ละขั้นตอน (ดัชนีช่อง 0 ว่างไว้ ข้อมูลเริ่มที่ช่อง 1)

### 🔍 กฎทองของอาจารย์ประดิษฐ์
* **ดัชนีของลูกและพ่อใน Array:**
  * Root อยู่ที่ Index **1**
  * ลูกซ้าย (Left Child) ของโหนด $i$ คือ $2i$
  * ลูกขวา (Right Child) ของโหนด $i$ คือ $2i + 1$
  * พ่อ (Parent) ของโหนด $i$ คือ $\lfloor i / 2 \rfloor$
* **DeleteMin (Percolate Down):**
  * ดึงค่าต่ำสุดที่ Root (Index 1) ออก
  * นำค่าในช่องสุดท้ายของ Heap มาวางชั่วคราวที่ Root แล้วเปรียบเทียบกับลูกที่ค่าน้อยกว่า เพื่อสลับลงไปจนถูกตำแหน่ง

---

## ข้อ 3: การดัดแปลงโค้ด Insertion Sort และ PercolateDown เพื่อนับ Position Move

### 📋 โจทย์จริง (C++ / Python)
อาจารย์ถามว่า: *"จาก Insertion Sort ในบทเรียน ต้องแก้ไขโปรแกรมอย่างไรจึงจะสามารถนับการเลื่อนตำแหน่งของข้อมูล (Position Move ของแต่ละรอบ) ได้?"*

```cpp
// เฉลยการแก้ไขโค้ด Insertion Sort (ภาษา C++)
template <class Comparable>
int insertionSortCountMoves(vector<Comparable> &a) {
    int totalMoves = 0;
    for (int p = 1; p < a.size(); p++) {
        Comparable tmp = a[p];
        int j;
        int movesInRound = 0;
        for (j = p; j > 0 && tmp < a[j - 1]; j--) {
            a[j] = a[j - 1]; // การเลื่อนตำแหน่ง (Shift 1 ครั้ง)
            movesInRound++;
        }
        a[j] = tmp; // วาง tmp ลงช่องว่าง
        totalMoves += movesInRound;
        cout << "Round " << p << " moves: " << movesInRound << endl;
    }
    return totalMoves;
}
```

### 💡 กรณีของ Worst Case
* ถ้าข้อมูล 15 ตัวเป็น Worst Case (เรียงจากมากไปน้อย):
  * ข้อมูลจะเลื่อนในรอบที่ $p$ เท่ากับ $p$ ครั้งเสมอ
  * จำนวนการเลื่อนทั้งหมด = $\sum_{p=1}^{N-1} p = \frac{N(N-1)}{2} = \frac{15 \times 14}{2} = 105$ ครั้ง!

---

## ข้อ 4: Quicksort (Median-of-Three, Cutoff=3 & Partitioning Trace)

### 📋 โจทย์จริง
ข้อมูล 15 ตัว: `79, 57, 36, 17, 14, 5, 9, 23, 38, 19, 45, 31, 11, 4, 3`  
กำหนด Cutoff = 3
* **Median-of-Three:** เปรียบเทียบ `a[left]`, `a[center]`, `a[right]` แล้วจัดเรียง 3 ตัวนี้
* ซ่อน Pivot ไว้ที่ `a[right - 1]`
* ค่าที่ไม่ถูกนำไปทำ Partitioning คือ: **Pivot (ที่ right - 1), ค่าตัวซ้ายสุด (left) และค่าตัวขวาสุด (right)** เพราะได้รับการจัดเรียงเรียบร้อยแล้วตั้งแต่ขั้นตอน Median-of-Three!

---

## ข้อ 5: Unweighted Shortest Path และการ Trace Circular Queue

### 📋 โจทย์จริง
กำหนดกราฟ 7 Vertex ให้หา Shortest Path แบบ Unweighted โดยมี Vertex 4 เป็นจุดเริ่มต้น:
1. เขียนตาราง `Known, dv, pv` สำหรับทุก Vertex
2. เขียนภาพสถานะของ Queue ขนาด 7 ช่อง พร้อมระบุลูกศร `Front` และ `Back` ในแต่ละรอบ

```
ตารางผลลัพธ์ (เริ่มที่ Vertex 4):
Vertex | Known | dv (ระยะทาง) | pv (โหนดก่อนหน้า)
-----------------------------------------------
  1    |   T   |      2      |        3
  2    |   T   |      3      |        1
  3    |   T   |      1      |        4
  4    |   T   |      0      |        0
  5    |   T   |      1      |        4
  6    |   T   |      2      |        5
  7    |   T   |      2      |        5
```

---

## ข้อ 6: Topological Sort และการ Trace In-Degree Queue ในกราฟ DAG

### 📋 โจทย์จริง
กำหนดกราฟ DAG 7 Vertex ให้เขียนลำดับ Topological Sort:
1. คำนวณ `In-degree` ของแต่ละโหนด
2. โหนดที่มี In-degree = 0 ให้ถูก `Enqueue` เข้า Queue
3. วนลูป `Dequeue` โหนดออกมา แล้วลด In-degree ของโหนดลูกที่เชื่อมต่อไป
4. แสดงภาพ Circular Queue ขนาด 7 ช่องในแต่ละรอบ พร้อมตำแหน่ง `Front` และ `Back`

---

## ข้อ 7: ทฤษฎี Hashing ในอุดมคติ และข้อจำกัดในโลกจริง

### 8.1 คุณสมบัติของ Hash Function ในอุดมคติ (Ideal Hash Function) 3 ข้อ:
1. **Uniform Distribution (การกระจายตัวสม่ำเสมอ):** กระจายข้อมูลทุกคีย์ลงในแต่ละช่องของตารางด้วยความน่าจะเป็นเท่ากัน ($1 / \text{TableSize}$)
2. **Deterministic (ความแน่นอนคงที่):** ข้อมูลคีย์ตัวเดิม ต้องให้ผลลัพธ์ดัชนีเดิมเสมอ
3. **Fast Computation (คำนวณรวดเร็ว):** ใช้เวลาในการคำนวณค่าแฮชเป็น $O(1)$

### 8.2 ข้อใดเป็นไปไม่ได้ในทางปฏิบัติ และสาเหตุ 2 ประการ:
* **ข้อที่เป็นไปไม่ได้สมบูรณ์:** การกระจายตัวแบบสมบูรณ์โดยไม่เกิดการชนเลย (Zero Collision)
* **สาเหตุ 2 ประการ:**
  1. **Pigeonhole Principle (หลักการรังนกพิราบ):** จำนวนคีย์ที่เป็นไปได้ (Key Space) มีขนาดใหญ่กว่า TableSize มหาศาล ย่อมต้องมีคีย์ที่แมปตรงช่องเดียวกัน
  2. **ไม่ทราบการกระจายตัวของข้อมูลล่วงหน้า (Data Distribution Unknown):** ข้อมูลจริงในโลกไม่ได้กระจายแบบ Random อย่างสมบูรณ์ มักมีรูปแบบ (Patterns/Clustering) ที่ทำให้เกิด Collision

---

## ข้อ 8: ทฤษฎีคำนวณ Complete Binary Tree และ Complete Graph

### 8.4 Complete Binary Tree สูง $h = 15$:
* **จำนวนโหนดน้อยที่สุด (Minimum Nodes):**
  $$\text{Min Nodes} = 2^h = 2^{15} = 32,768 \text{ โหนด}$$
* **จำนวนโหนดมากที่สุด (Maximum Nodes - Full Binary Tree):**
  $$\text{Max Nodes} = 2^{h+1} - 1 = 2^{16} - 1 = 65,536 - 1 = 65,535 \text{ โหนด}$$

### 8.5 Complete Graph ที่มี Vertex $V = 15$ มีกี่ Edge?
* **สูตรคำนวณ:**
  $$E = \frac{V(V - 1)}{2} = \frac{15 \times (15 - 1)}{2} = \frac{15 \times 14}{2} = 15 \times 7 = 105 \text{ เส้น (Edges)}$$

---

> [!TIP]
> เอกสารฉบับนี้เชื่อมโยงกับโปรแกรมข้อสอบจำลอง [`Final_Exam_2026_Mock_and_Solutions.py`](file:///C:/Project/python-data-structures-and-algorithms/Exams/Final_Exam_2026_Mock_and_Solutions.py) ในโฟลเดอร์ `Exams/` เพื่อให้นักศึกษาสามารถรันเทสโค้ดและทดสอบความเข้าใจได้ทันที!
