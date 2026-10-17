# 📘 บทที่ 2: ทบทวนภาษาไพทอนและการเขียนโปรแกรมเชิงวัตถุ (Review Python & OOP)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **โครงสร้างพื้นฐานภาษา Python**: Dynamic Typing, Indentation, List, Dict, Tuple, Set
2. **การทำงานของ Reference & Memory Management**:
   - การชี้แอดเดรสของอ็อบเจกต์ (Object Reference)
   - ความแตกต่างระหว่าง Primitive Value และ Compound Reference
3. **การเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming - OOP)**:
   - **Encapsulation**: การห่อหุ้มข้อมูลและเมธอด
   - **Inheritance**: การสืบทอดคุณสมบัติของคลาสแม่สู่คลาสลูก
   - **Polymorphism**: พฤติกรรมที่หลากหลายของเมธอดชื่อเดียวกัน
   - **Abstraction**: การสร้างอินเทอร์เฟซเพื่อซ่อนรายละเอียดภายใน

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 2 Edit168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%202%20Edit168.pdf) | สไลด์ฉบับปรับปรุงใหม่ทางการจาก Google Classroom |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 4 ภาพ: สไลด์ทบทวน OOP, แผนภาพอ็อบเจกต์, และโครงสร้างคลาส |

---

## 💡 จุดที่พบบ่อยในการเขียนโครงสร้างข้อมูล
- การประกาศคลาส `Node` สำหรับ Linked List และ Tree ต้องเข้าใจการเชื่อมโยง reference ด้วย `self.next` หรือ `self.left`, `self.right`
