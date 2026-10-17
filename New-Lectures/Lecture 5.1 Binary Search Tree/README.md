# 📘 บทที่ 5.1: ต้นไม้ค้นหาแบบทวิภาค (Binary Search Tree - BST Insertion & Search)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **คุณสมบัติเฉพาะของ Binary Search Tree (BST Property)**:
   - ข้อมูลในกิ่งซ้าย (Left Subtree) ต้องมีค่าน้อยกว่าโหนดปัจจุบันเสมอ (`Left < Root`)
   - ข้อมูลในกิ่งขวา (Right Subtree) ต้องมีค่ามากกว่าโหนดปัจจุบันเสมอ (`Right > Root`)
2. **การค้นหา (Searching)**:
   - เปรียบเทียบกับ Root: ถ้าน้อยกว่าไปซ้าย ถ้ามากกว่าไปขวา
   - Time Complexity: เฉลี่ย $O(\log N)$, กรณีแย่สุด (Skewed Tree) $O(N)$
3. **การแทรกข้อมูล (Insertion)**:
   - เริ่มต้นที่ Root เปรียบเทียบและเลื่อนพอยน์เตอร์ลงไปจนพบตำแหน่งว่างที่เป็น Leaf
   - การแทรกข้อมูลทีละตัวตามลำดับลำลอง

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 5.1.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%205.1.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานแบบฝึกหัด BST** | [`For example Binary Search Tree std.pdf`](./For%20example%20Binary%20Search%20Tree%20std.pdf) | โจทย์การสร้าง BST และขั้นตอนการแทรกโหนด |
| 🌟 **เฉลยแบบฝึกหัด BST** | [`For example Binary Search Tree std_solved.pdf`](./For%20example%20Binary%20Search%20Tree%20std_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 📝 **ใบงาน BST Delete Step** | [`For example Binary Search Tree std delete round 4 in insert_s step.pdf`](./For%20example%20Binary%20Search%20Tree%20std%20delete%20round%204%20in%20insert_s%20step.pdf) | โจทย์เน้นรอบที่ 4 ในการปรับแต่งโครงสร้าง |
| 🌟 **เฉลย BST Delete Step** | [`For example Binary Search Tree std delete round 4 in insert_s step_solved.pdf`](./For%20example%20Binary%20Search%20Tree%20std%20delete%20round%204%20in%20insert_s%20step_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 📄 **เอกสารสรุปเมธอดลบ** | [`removebst.pdf`](./removebst.pdf) | สรุปขั้นตอนการลบข้อมูลใน BST |
| 🐍 **โค้ดภาษา Python** | • [`ch5.1_Binary_Search.py`](./ch5.1_Binary_Search.py)<br>• [`BinarySearchTrees.py`](./BinarySearchTrees.py) | โค้ดคลาส `BST` และเมธอด `insert()`, `search()` |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 7 ภาพ: สไลด์และการไล่ขั้นตอนสร้าง BST |
