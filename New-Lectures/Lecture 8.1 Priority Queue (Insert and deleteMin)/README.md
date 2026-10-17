# 📘 บทที่ 8.1: ปฏิบัติการในฮีป (Heap Operations: Insert & deleteMin)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **การแทรกข้อมูล (`insert(x)`) & Percolate Up (Up-Heap)**:
   - นำค่าใหม่ไปวางที่ตำแหน่งว่างถัดไปในอาร์เรย์ (`size = size + 1`)
   - เปรียบเทียบกับ Parent ($i // 2$) หากค่าน้อยกว่า Parent ให้ลอยขึ้นไปแทนที่จนกว่าจะถูกคุณสมบัติ
   - Time Complexity: $O(\log N)$
2. **การดึงค่าน้อยสุดออก (`deleteMin()`) & Percolate Down (Down-Heap)**:
   - นำ Root (index 1) ออกมาเป็นคำตอบ
   - นำโหนดตัวสุดท้ายในอาร์เรย์มาวางแทนที่ Root ชั่วคราว แล้วลดขนาด (`size = size - 1`)
   - เปรียบเทียบกับบุตรทั้งสองข้าง เลือกลูกที่มีค่าน้อยที่สุด แล้วสลับตำแหน่งลงไปเรื่อยๆ จนกว่าจะถูกต้อง
   - Time Complexity: $O(\log N)$

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 8.1.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%208.1.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานตัวอย่างฮีป** | [`For example Binary Heap.pdf`](./For%20example%20Binary%20Heap.pdf) | โจทย์ไล่ขั้นตอน Percolate Up และ Percolate Down |
| 🌟 **เฉลยตัวอย่างฮีป** | [`For example Binary Heap_solved.pdf`](./For%20example%20Binary%20Heap_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 💼 **ใบงาน Assignment 3** | [`Assignment 3 Inclass.pdf`](./Assignment%203%20Inclass.pdf) | โจทย์แบบฝึกหัดหน้า 283 (Insert 14 และ deleteMin 3 ครั้ง) |
| 🌟 **เฉลย Assignment 3** | [`Assignment 3 Inclass_solved.pdf`](./Assignment%203%20Inclass_solved.pdf) | เฉลยระดับตำราพร้อมรูปวาดกระดานครบทุกสเต็ป |
| 🎙️ **เสียงบรรยายถอดความสด** | • [`20260909_103704.txt`](./20260909_103704.txt)<br>• [`dsa20260909_092303.txt`](./dsa20260909_092303.txt) | บันทึกเสียง อ.ประดิษฐ์ (9 ก.ย.) ไล่โค้ดทีละบรรทัด |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 64 ภาพ: เฉลยหน้า 283, ลายมือนักศึกษา, และสเต็ป Percolate |
