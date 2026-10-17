# 📘 บทที่ 5.2: การลบโหนดในต้นไม้ค้นหาทวิภาค (BST Deletion with 2 Children)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
การลบโหนดใน BST แบ่งเป็น 3 กรณีตามจำนวนลูกของโหนดที่จะลบ:
1. **Case 1: Node with 0 Children (Leaf Node)**: ลบโหนดทิ้งได้ทันที โดยตั้ง pointer ของ Parent เป็น `None`
2. **Case 2: Node with 1 Child**: เลื่อนลูกขึ้นมาเชื่อมต่อกับ Parent แทนโหนดที่ถูกลบ
3. **Case 3: Node with 2 Children (กรณีไฮไลท์ข้อสอบ)**:
   - นำค่า **In-order Successor** (ค่าน้อยที่สุดในต้นไม้ย่อยทางขวา: Min of Right Subtree) หรือ **In-order Predecessor** (ค่ามากที่สุดในต้นไม้ย่อยทางซ้าย: Max of Left Subtree) มาเขียนทับตำแหน่งของโหนดที่ต้องการลบ
   - จากนั้นทำการลบโหนดตัวแทนเดิมออกจากตำแหน่งเดิม (ซึ่งจะมีบุตรไม่เกิน 1 คนแน่นอน)

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 5.2.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%205.2.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานตัวอย่างการลบ** | [`Example for Binary Search Tree remove 2 std.pdf`](./Example%20for%20Binary%20Search%20Tree%20remove%202%20std.pdf) | โจทย์เน้นการลบโหนดที่มี 2 บุตรอย่างเป็นลำดับขั้น |
| 🌟 **เฉลยตัวอย่างการลบ** | [`Example for Binary Search Tree remove 2 std_solved.pdf`](./Example%20for%20Binary%20Search%20Tree%20remove%202%20std_solved.pdf) | เฉลยละเอียดระดับ Master Solution แสดงการเลือก Successor |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 7 ภาพ: ขั้นตอนการลบและผลลัพธ์ของโครงสร้างทรี |
