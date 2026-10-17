# 📘 บทที่ 1: บทนำและการวิเคราะห์อัลกอริทึม (Introduction & Algorithm Analysis)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **นิยามของ Data Structure & Algorithm**: โครงสร้างการจัดเก็บและการประมวลผลข้อมูล
2. **Abstract Data Type (ADT)**: ความแตกต่างระหว่างแบบจำลองข้อมูลทางนามธรรมกับการเขียนโค้ดจริง
3. **การวิเคราะห์ประสิทธิภาพของอัลกอริทึม (Algorithm Analysis)**:
   - **Time Complexity** (เวลาที่ใช้ในการประมวลผล)
   - **Space Complexity** (หน่วยความจำที่ต้องใช้)
4. **สัญกรณ์ Big-O (Asymptotic Notations)**:
   - $O(1)$ Constant Time
   - $O(\log N)$ Logarithmic Time
   - $O(N)$ Linear Time
   - $O(N \log N)$ Linearithmic Time
   - $O(N^2)$ Quadratic Time
   - $O(2^N)$ Exponential Time

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 1 Edit168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%201%20Edit168.pdf) | สไลด์ฉบับปรับปรุงใหม่ทางการจาก Google Classroom |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 5 ภาพ: สไลด์ ADT, การเปรียบเทียบฟังก์ชัน Big-O, และกราฟประสิทธิภาพ |

---

## 💡 แนวทางการอ่านทบทวนเพื่อสอบ
- เข้าใจการเปรียบเทียบการเติบโตของฟังก์ชัน $O(1) < O(\log N) < O(N) < O(N \log N) < O(N^2) < O(2^N)$
- จำแนกประเภทการวนซ้ำ (Single loop = $O(N)$, Nested loop 2 ชั้น = $O(N^2)$)
