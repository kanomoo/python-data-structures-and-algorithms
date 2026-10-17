# 📘 บทที่ 4: สแตกและคิว (Stack & Queue ADTs)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **Stack ADT (LIFO - Last In, First Out)**:
   - เมธอดหลัก: `push(x)`, `pop()`, `top()` / `peek()`, `isEmpty()`
   - การประยุกต์ใช้งาน:
     - การตรวจสอบความสมดุลของวงเล็บ (Parenthesis Balancing)
     - การแปลง Infix เป็น Postfix Expression และการคำนวณผลลัพธ์ Postfix Evaluation
2. **Queue ADT (FIFO - First In, First Out)**:
   - เมธอดหลัก: `enqueue(x)`, `dequeue()`, `front()`, `isEmpty()`
   - Circular Queue และการประยุกต์ใช้งาน (Level-order traversal, การจัดการคิวงาน)

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | • [`DATA STRUCTURES - ALGORITHMS_Lecture 4 Edit168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%204%20Edit168.pdf)<br>• [`DATA STRUCTURES - ALGORITHMS_Lecture 4.1.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%204.1.pdf) | สไลด์ฉบับทางการ Google Classroom ครบทั้ง Stack และ Queue |
| 📝 **ใบงานแบบฝึกหัด Stack** | [`For example Stack.pdf`](./For%20example%20Stack.pdf) | โจทย์ไล่สถานะ Stack ตารางตามแบบในห้องเรียน |
| 🌟 **เฉลยแบบฝึกหัด Stack** | [`For example Stack_solved.pdf`](./For%20example%20Stack_solved.pdf) | เฉลยละเอียดพร้อมแสดงสเต็ป LIFO ทุกขั้นตอน |
| 📝 **ใบงานแบบฝึกหัด Queue** | [`For example Queue.pdf`](./For%20example%20Queue.pdf) | โจทย์ไล่สถานะ Circular Queue |
| 🌟 **เฉลยแบบฝึกหัด Queue** | [`For example Queue_solved.pdf`](./For%20example%20Queue_solved.pdf) | เฉลยละเอียดพร้อมตำแหน่ง Front/Rear ชัดเจน |
| 📝 **ใบงาน Infix to Postfix** | [`Postfix Expression.pdf`](./Postfix%20Expression.pdf)<br>[`postfix.pdf`](./postfix.pdf) | โจทย์ตารางแปลงนิพจน์ Infix เป็น Postfix ด้วย Stack |
| 🌟 **เฉลย Infix to Postfix** | [`Postfix Expression_solved.pdf`](./Postfix%20Expression_solved.pdf) | เฉลยตารางแปลง Infix to Postfix ละเอียดครบทุกเครื่องหมาย |
| 📖 **เอกสารแปล & เสริมความเข้าใจ** | • [`แปลเอกสารบทท 3.6 The Stack ADT.pdf`](./แปลเอกสารบทท%203.6%20The%20Stack%20ADT.pdf)<br>• [`สำเนาของ วิธีการทำตามระดับให้ดูคู่กับชีทบท4.pdf`](./สำเนาของ%20วิธีการทำตามระดับให้ดูคู่กับชีทบท4.pdf) | คำแปลตำรา Stack ADT และคู่มือ Level-order traversal |
| 🐍 **โค้ดภาษา Python** | • [`ch4-Stack.py`](./ch4-Stack.py)<br>• [`ch4.1_Queue.py`](./ch4.1_Queue.py)<br>• [`BasicStack.py`](./BasicStack.py)<br>• [`BasicQueue.py`](./BasicQueue.py) | โค้ดตัวอย่างโครงสร้างข้อมูล Stack และ Queue ฉบับสมบูรณ์ |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 12 ภาพ: กระดานตาราง Stack/Queue, การแปลง Postfix, Test Program 1 |

---

## 💡 กฎสำคัญของการแปลง Infix -> Postfix ที่ออกสอบประจำ
- ลำดับความสำคัญของตัวดำเนินการ (Operator Precedence):
  1. `^` (เลขยกกำลัง - ขวาก่อน/สูงที่สุด)
  2. `*`, `/` (คูณ, หาร)
  3. `+`, `-` (บวก, ลบ)
- ตัวดำเนินการที่มีลำดับความสำคัญสูงกว่าหรือเท่ากันที่อยู่ใน Stack ต้องถูก `pop()` ออกมายังผลลัพธ์ก่อนเสมอ
