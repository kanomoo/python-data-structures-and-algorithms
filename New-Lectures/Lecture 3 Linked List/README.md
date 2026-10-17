# 📘 บทที่ 3: โครงสร้างข้อมูลแถวลำดับเชื่อมโยง (Linked List)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **ความแตกต่างระหว่าง Array และ Linked List**: Contiguous memory vs Dynamic node pointer
2. **Singly Linked List**:
   - โครงสร้างโหนด (`Node`: `item`, `next`)
   - `head` pointer และการตรวจสอบ `isEmpty()`
   - การแทรกโหนด (Insert at head, Insert at tail, Insert between nodes)
   - การลบโหนด (Delete head, Delete tail, Delete target key)
   - การท่องสำรวจ (Traversal) และการหาความยาว (Size/Count)
3. **Doubly Linked List & Circular Linked List**: การเชื่อมต่อไปข้างหน้าและย้อนกลับ

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 3.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%203.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานตัวอย่างห้องเรียน** | [`For example Linked List 169.pdf`](./For%20example%20Linked%20List%20169.pdf) | โจทย์ตัวอย่างการเชื่อมต่อและย้ายพอยน์เตอร์ |
| 🌟 **เฉลยใบงานตัวอย่าง** | [`For example Linked List 169_solved.pdf`](./For%20example%20Linked%20List%20169_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 📝 **ใบงานแบบฝึกหัดเสริม** | [`linklist ex169 Edit1.pdf`](./linklist%20ex169%20Edit1.pdf) | โจทย์แบบฝึกหัดการไล่พอยน์เตอร์ในห้องเรียน |
| 🌟 **เฉลยแบบฝึกหัดเสริม** | [`linklist ex169 Edit1_solved.pdf`](./linklist%20ex169%20Edit1_solved.pdf) | เฉลยละเอียดพร้อมรูปวาดและไดอะแกรมพอยน์เตอร์ |
| 💼 **ใบงานการบ้าน (Assign 1)** | [`Assign 1 Linked List.pdf`](./Assign%201%20Linked%20List.pdf) | โจทย์ Assignment 1 Linked List ประจำวิชา |
| 🌟 **เฉลยการบ้าน (Assign 1)** | [`Assign 1 Linked List_solved.pdf`](./Assign%201%20Linked%20List_solved.pdf) | เฉลยครบทุกฟังก์ชันทั้งภาษาและรูปประกอบ |
| 🧪 **โจทย์สอบโปรแกรม 1** | [`Test Program 1 Linked List.pdf`](./Test%20Program%201%20Linked%20List.pdf) | โจทย์ทดสอบการเขียนโค้ด Linked List |
| 🌟 **เฉลยสอบโปรแกรม 1** | [`Test Program 1 Linked List_solved.pdf`](./Test%20Program%201%20Linked%20List_solved.pdf) | โค้ดเฉลยสมบูรณ์พร้อมคำอธิบาย |
| 🐍 **โค้ดภาษา Python** | [`ch3-Linked-List.py`](./ch3-Linked-List.py)<br>[`BasicSinglyLinkedList.py`](./BasicSinglyLinkedList.py) | โค้ดโครงสร้างคลาส `Node` และ `LinkedList` ฉบับเต็ม |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 23 ภาพ: กระดานสอนสด 26 ส.ค., การเขียน Pointer, และตัวอย่าง VS Code |

---

## 💡 ข้อควรระวังในการสอบ
- ลำดับการเปลี่ยนตัวชี้ (Pointer manipulation order): ต้องชี้โหนดใหม่ไปยังโหนดถัดไปก่อน (`new_node.next = current.next`) เสมอ มิฉะนั้นข้อมูลข้างหลังจะหลุดหาย (Memory leak/Broken chain)
