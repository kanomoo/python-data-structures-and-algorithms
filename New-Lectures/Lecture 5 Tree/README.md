# 📘 บทที่ 5: โครงสร้างข้อมูลต้นไม้พื้นฐาน (Tree Foundations & Binary Tree)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **นิยามและศัพท์เฉพาะของ Tree (Terminology)**:
   - Root, Node, Edge, Parent, Child, Sibling, Leaf Node, Internal Node
   - Depth (ความลึกจาก Root), Height (ความสูงถึง Leaf), Degree (จำนวนบุตร)
2. **Binary Tree**: ต้นไม้ทวิภาคที่แต่ละโหนดมีลูกได้ไม่เกิน 2 โหนด (Left child, Right child)
3. **การท่องต้นไม้ทวิภาค (Binary Tree Traversals)**:
   - **Pre-order**: Node -> Left -> Right
   - **In-order**: Left -> Node -> Right
   - **Post-order**: Left -> Right -> Node
   - **Level-order**: ท่องทีละระดับจากบนลงล่าง ซ้ายไปขวา (ใช้ Queue)
4. **การสร้าง Binary Tree จากรหัสนักศึกษา (Assignment 2)**: กฎการกระจายตัวเลขเพื่อสร้างโครงสร้างต้นไม้

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 5 Edit168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%205%20Edit168.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานตัวอย่างห้องเรียน** | [`For example Binary Tree.pdf`](./For%20example%20Binary%20Tree.pdf) | แบบฝึกหัดการหา Height, Depth และ Traversal |
| 🌟 **เฉลยใบงานตัวอย่าง** | [`For example Binary Tree_solved.pdf`](./For%20example%20Binary%20Tree_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 💼 **ใบงานการบ้าน (Assign 2)** | [`Assign 2 Binary Tree.pdf`](./Assign%202%20Binary%20Tree.pdf) | โจทย์ Assignment 2 การสร้าง Binary Tree จากรหัสนักศึกษา |
| 🌟 **เฉลยการบ้าน (Assign 2)** | [`Assign 2 Binary Tree_solved.pdf`](./Assign%202%20Binary%20Tree_solved.pdf) | เฉลยแนวทางการวาดทรีและการเขียนโปรแกรม |
| 🐍 **โค้ดภาษา Python** | • [`ch5_Tree.py`](./ch5_Tree.py)<br>• [`BinaryTrees.py`](./BinaryTrees.py) | โค้ดโครงสร้างคลาส `TreeNode` และฟังก์ชัน Traversal |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 7 ภาพ: สไลด์ทรี, ไดอะแกรม Traversal, และผลงาน Assignment 2 |
