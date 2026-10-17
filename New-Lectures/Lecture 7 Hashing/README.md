# 📘 บทที่ 7: ตารางแฮชและการแก้ปัญหาการชน (Hashing & Collision Resolution)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **แฮชชิ่ง (Hashing)**: การแปลงคีย์ (Key) ไปเป็นดัชนี (Index) ของตารางด้วยแฮชฟังก์ชัน $h(k) = k \bmod m$
2. **ปัญหาการชน (Collision)**: เมื่อคีย์สองตัวได้ผลลัพธ์ตำแหน่งเดียวกัน
3. **วิธีแก้ปัญหาการชน (Collision Resolution Strategies)**:
   - **Separate Chaining**: ใช้ Linked List เชื่อมต่อข้อมูลในช่องเดียวกัน
   - **Open Addressing**:
     - **Linear Probing**: $h(k, i) = (h'(k) + i) \bmod m$ (เกิด Primary Clustering)
     - **Quadratic Probing**: $h(k, i) = (h'(k) + i^2) \bmod m$ (ลดคลัสเตอร์ แต่ต้องระวังวงรอบ)
     - **Double Hashing**: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod m$
4. **Load Factor ($\lambda = N/m$) และ Rehashing**: การขยายขนาดตารางเป็นจำนวนเฉพาะถัดไป (Next Prime $\ge 2m$) เมื่อ $\lambda > 0.5$

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 7.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%207.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 🎙️ **เสียงบรรยายถอดความสด** | • [`20260902_091736.txt`](./20260902_091736.txt)<br>• [`20260902_094834.txt`](./20260902_094834.txt)<br>• [`20260902_104259.txt`](./20260902_104259.txt)<br>• [`20260902_104304.txt`](./20260902_104304.txt) | บันทึกการสอนสดของ อ.ประดิษฐ์ (2 ก.ย.) เจาะลึก Hashing & Linear/Quad/Double |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม **76 ภาพ**: ภาพกระดานไล่ Linear Probing, Quadratic, Rehashing, ภาพรั่วข้อสอบ |
