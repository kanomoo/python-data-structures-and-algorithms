# 📘 บทที่ 10: ทฤษฎีกราฟและการเรียงลำดับเชิงทอพอโลยี (Graph Fundamentals & Topological Sort)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **นิยามของกราฟ (Graph Definition)**: $G = (V, E)$
   - จุดยอด (Vertices $V$) และเส้นเชื่อม (Edges $E$)
   - Directed Graph (กราฟระบุทิศทาง) vs Undirected Graph (กราฟไม่ระบุทิศทาง)
   - In-degree (จำนวนเส้นที่พุ่งเข้าโหนด) และ Out-degree (จำนวนเส้นที่พุ่งออกจากโหนด)
2. **การแทนโครงสร้างกราฟในคอมพิวเตอร์**:
   - **Adjacency Matrix**: ตาราง 2 มิติ ขนาด $|V| \times |V|$ (Space Complexity: $O(|V|^2)$)
   - **Adjacency List**: อาร์เรย์ของ Linked List ขนาด $|V|$ (Space Complexity: $O(|V| + |E|)$)
3. **Topological Sort (การเรียงลำดับเชิงทอพอโลยี)**:
   - ใช้ได้เฉพาะกับ **DAG (Directed Acyclic Graph)** เท่านั้น (กราฟมีทิศทางที่ปราศจากวงวน)
   - อัลกอริทึม: ค้นหาโหนดที่มี In-degree = 0 นำเข้าคิว/ผลลัพธ์ แล้วลด In-degree ของโหนดข้างเคียงลง 1 ทำซ้ำจนครบทุกโหนด

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 10 168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%2010%20168.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงาน Topological Sort** | [`Topological sort.pdf`](./Topological%20sort.pdf) | โจทย์ตารางการเรียงลำดับ DAG 7 จุด |
| 🌟 **เฉลย Topological Sort** | [`Topological sort_solved.pdf`](./Topological%20sort_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 📖 **สรุปวิชาการ (Wiki)** | [`Topological_Sort_Classroom_Wiki.md`](./Topological_Sort_Classroom_Wiki.md) | บทวิเคราะห์ทฤษฎีกราฟและขั้นตอนอย่างละเอียด |
| 🎙️ **เสียงบรรยายถอดความสด** | [`20260923_091645.txt`](./20260923_091645.txt) | บันทึกเสียงสอนสด อ.ประดิษฐ์ (23 ก.ย.) เจาะลึกกราฟ การแทนเมทริกซ์ และแนวข้อสอบ |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม **17 ภาพ**: กระดาน DAG จริง 7 จุด (840922631...), ตาราง In-degree, และตัวอย่างคลาส |
