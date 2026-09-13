# Exam & Reference Links (แหล่งอ้างอิงและเครื่องมือเรียนรู้)

> เวอร์ชันในโฟลเดอร์ Exams: [`Exams/link.md`](file:///C:/Project/python-data-structures-and-algorithms/Exams/link.md)  
> 🔬 **ห้องทดลองระบบใหม่ในโปรเจกต์:** เปิดใช้งาน [`DsaLab Visual Studio`](file:///C:/Project/python-data-structures-and-algorithms/DsaLab/index.html) หรือ [`DSA Wiki`](file:///C:/Project/python-data-structures-and-algorithms/Wiki/index.html)

รวบรวมลิงก์อ้างอิงภายนอก (Claude Artifact, Gemini, Perplexity) พร้อมโมดูลทดลองเชิงโต้ตอบภายในโปรเจกต์:

| ไฟล์ในโปรเจกต์ | หัวข้อ / เนื้อหา | เครื่องมือในโปรเจกต์ (DsaLab) | แพลตฟอร์มอ้างอิงเดิม | ลิงก์อ้างอิงภายนอก |
| :--- | :--- | :--- | :--- | :--- |
| [`Exams/Heap.py`](file:///C:/Project/python-data-structures-and-algorithms/Exams/Heap.py) | **Binary Heap** (Min/Max Heap, Percolate Up/Down) | [เปิดทดลอง Heap Visualizer](file:///C:/Project/python-data-structures-and-algorithms/DsaLab/index.html) | Claude Artifact<br>Perplexity | [Claude Artifact](https://claude.ai/public/artifacts/3be9a554-8360-460f-9fad-c041859bccdb)<br>[Perplexity AI](https://www.perplexity.ai/computer/a/8e421185-9a16-4483-9acd-9905f4bdd0c4) |
| [`Exams/BinarySearchTrees.py`](file:///C:/Project/python-data-structures-and-algorithms/Exams/BinarySearchTrees.py) | **Binary Search Tree** (BST Insert, Search, Deletion 3 Cases) | [เปิดทดลอง BST Visualizer](file:///C:/Project/python-data-structures-and-algorithms/DsaLab/index.html) | Gemini | [Gemini Share 1](https://share.gemini.google/68l68tkQ4gyZ)<br>[Gemini Share 2](https://share.gemini.google/buHkJaab2mpf) |
| [`Exams/Hash.py`](file:///C:/Project/python-data-structures-and-algorithms/Exams/Hash.py) | **Hash Table** (Linear Probing, Separate Chaining, Load Factor) | [เปิดทดลอง Hash Visualizer](file:///C:/Project/python-data-structures-and-algorithms/DsaLab/index.html) | Gemini | [Gemini Share 1](https://share.gemini.google/SJXI2wdwjceD)<br>[Gemini Share 2](https://share.gemini.google/v6raXDvrr0Tp) |
| [`Exams/InfixToPostFix.py`](file:///C:/Project/python-data-structures-and-algorithms/Exams/InfixToPostFix.py) | **Stack: Infix to Postfix** (Precedence & Token Scanner) | [เปิดทดลอง Stack Visualizer](file:///C:/Project/python-data-structures-and-algorithms/DsaLab/index.html) | Gemini | [Gemini Share 1](https://gemini.google.com/share/cc48e0f025be)<br>[Gemini Share 2](https://gemini.google.com/share/8746e44a615d) |

---

## รายละเอียดแยกตามโครงสร้างข้อมูล

### 1. Binary Heap (`Heap.py`)
- **DsaLab Visualizer:** มีทั้งโหมด Min-Heap / Max-Heap แสดงภาพ Tree SVG เชื่อมโยงกับ Array 1-based indexing, ระบบ Percolate Up & Down แบบ Step-by-Step พร้อมปุ่มกดค่าเอง
- **Claude Artifact:** https://claude.ai/public/artifacts/3be9a554-8360-460f-9fad-c041859bccdb
- **Perplexity Notebook:** https://www.perplexity.ai/computer/a/8e421185-9a16-4483-9acd-9905f4bdd0c4

### 2. Binary Search Trees (`BinarySearchTrees.py`)
- **DsaLab Visualizer:** รองรับ Insert ทีละค่า, Search ค้นหาพร้อม highlight เส้นทาง, และ Delete ครบทั้ง 3 เคส (Leaf, One child, Two children ด้วย In-order successor)
- **Gemini Share 1:** https://share.gemini.google/68l68tkQ4gyZ
- **Gemini Share 2:** https://share.gemini.google/buHkJaab2mpf

### 3. Hash Table (`Hash.py`)
- **DsaLab Visualizer:** รองรับทั้ง Separate Chaining (Linked Lists) และ Linear Probing พร้อมเกจวัด Load Factor ($\lambda = N/M$) แบบ Real-time
- **Gemini Share 1:** https://share.gemini.google/SJXI2wdwjceD
- **Gemini Share 2:** https://share.gemini.google/v6raXDvrr0Tp

### 4. Stack: Infix to Postfix (`InfixToPostFix.py`)
- **DsaLab Visualizer:** ตัวแปลง Infix เป็น Postfix พร้อมแอนิเมชัน Token Scanner, ตาราง Precedence และ Stack Animation
- **Gemini Share 1:** https://gemini.google.com/share/cc48e0f025be
- **Gemini Share 2:** https://gemini.google.com/share/8746e44a615d
