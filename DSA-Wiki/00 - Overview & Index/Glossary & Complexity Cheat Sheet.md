# 📖 Master Glossary & Complexity Cheat Sheet (สรุปศัพท์และความเร็ว Big-O สำหรับสอบ)

> [!NOTE]
> หน้านี้รวบรวม **ตารางเปรียบเทียบความเร็ว (Time & Space Complexity Cheat Sheet)**, **คำศัพท์สำคัญ** และ **สูตรที่ต้องใช้ในห้องสอบ** สำหรับวิชา Data Structures & Algorithms

---

## 📊 1. Master Time & Space Complexity Table (ตารางออกสอบยอดฮิต!)

| Data Structure / Algorithm | Access / Search (Average) | Search (Worst) | Insert (Average) | Insert (Worst) | Delete (Average) | Delete (Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Python List (Array)** | $O(1)$ Access / $O(N)$ Search | $O(N)$ | $O(1)$ Append / $O(N)$ Insert | $O(N)$ | $O(1)$ Pop End / $O(N)$ Pop(0) | $O(N)$ | $O(N)$ |
| **Singly Linked List** | $O(N)$ | $O(N)$ | $O(1)$ Head / $O(N)$ Tail* | $O(1)$ Head | $O(1)$ Head / $O(N)$ Tail | $O(N)$ | $O(N)$ |
| **Doubly Linked List** | $O(N)$ | $O(N)$ | $O(1)$ Head & Tail | $O(1)$ | $O(1)$ Head & Tail | $O(1)$ | $O(N)$ |
| **Stack (Array / Linked List)**| $O(N)$ Search | $O(N)$ | $O(1)$ Push | $O(1)$ | $O(1)$ Pop | $O(1)$ | $O(N)$ |
| **Queue (Circular Array)** | $O(N)$ Search | $O(N)$ | $O(1)$ Enqueue | $O(1)$ | $O(1)$ Dequeue | $O(1)$ | $O(N)$ |
| **Binary Search Tree (BST)** | $O(\log N)$ | $O(N)$ (Unbalanced) | $O(\log N)$ | $O(N)$ | $O(\log N)$ | $O(N)$ | $O(N)$ |
| **Binary Heap (Min/Max)** | $O(1)$ FindMin / $O(N)$ Search | $O(N)$ | $O(\log N)$ PercolateUp | $O(\log N)$ | $O(\log N)$ DeleteMin | $O(\log N)$ | $O(N)$ |
| **Hash Table (Open Addr/Chaining)**| $O(1)$ | $O(N)$ (Collisions) | $O(1)$ | $O(N)$ | $O(1)$ | $O(N)$ | $O(N)$ |

*\*หมายเหตุ: Singly Linked List หากมี Tail Pointer การ Insert at Tail จะเป็น $O(1)$ แต่การ Delete at Tail ยังคงเป็น $O(N)$ เนื่องจากต้องถอย Pointer ไปยัง Node ก่อนหน้า Tail*

---

## 🔀 2. Sorting Algorithms Complexity Comparison Table

| Sorting Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stability | In-place? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(N)$ (Optimized) | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Stable** | Yes |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Unstable** | Yes |
| **Insertion Sort** | $O(N)$ (Nearly Sorted) | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Stable** | Yes |
| **Merge Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | **Stable** | No |
| **Quick Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ (Bad Pivot) | $O(\log N)$ | **Unstable** | Yes |
| **Heap Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | **Unstable** | Yes |

---

## 🔤 3. คำศัพท์อักษรย่อและมโนทัศน์สำคัญ (Key Terminology)

- **ADT (Abstract Data Type)**: คำนิยามของโครงสร้างข้อมูลทางตรรกศาสตร์ที่ระบุว่าทำอะไรได้บ้าง (Operations) โดยไม่สนใจรายละเอียดการเขียนโค้ดภายใน
- **In-place Algorithm**: อัลกอริทึมที่ใช้หน่วยความจำสำรองเพิ่มเติมเป็นค่าคงที่ $O(1)$
- **Stable Sort**: การเรียงลำดับที่รักษาลำดับดั้งเดิมของข้อมูลที่มีค่าเท่ากันไว้ได้
- **Inorder Successor**: โหนดที่มีค่าน้อยที่สุดใน Subtree ฝั่งขวา (Minimum of Right Subtree) ซึ่งใช้ทดแทนโหนดที่ถูกลบในกรณี BST 2 Children
- **Complete Binary Tree**: ต้นไม้ทวิภาคที่ทุก Level ถูกเติมเต็มครบทั้งหมด ยกเว้นอาจเหลือ Levelสุดท้าย แต่ต้องเติมโหนดชิดซ้ายสุดเสมอ (เป็นคุณสมบัติบังคับของ Binary Heap)
- **Load Factor ($\lambda$)**: อัตราส่วนระหว่างจำนวนข้อมูล ($N$) ต่อขนาดของ Hash Table ($M$) โดย $\lambda = N / M$

---

## 🔗 ลิงก์เชื่อมโยงใน Obsidian Wiki
- กลับหน้าหลัก: [[Index]]
- เข้าสู่ Module 01: [[01.1 - Introduction to Data Structures & Algorithm Analysis]]
