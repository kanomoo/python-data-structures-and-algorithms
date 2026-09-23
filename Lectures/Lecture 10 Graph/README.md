# Lecture 10 Graph (ทฤษฎีกราฟ, โครงสร้างข้อมูล และ Topological Sort)

เอกสารประกอบการสอนและแบบฝึกหัดวิชา Data Structures and Algorithms (ผู้สอน: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล).

---

## 📁 ไฟล์เอกสารในโฟลเดอร์นี้

1. **[`Topological sort_solved.pdf`](./Topological%20sort_solved.pdf)** 🌟 **(เอกสารเฉลยสมบูรณ์แบบ)**:
   - เอกสารต้นฉบับทั้ง 6 หน้าที่เติมคำตอบ การคำนวณ สูตร และรูปภาพกำกับลงไปในเอกสารโดยตรง
   - ตาราง Adjacency Matrix $7 \times 7$ เติมค่าครบทุกช่อง พร้อมคำนวณความสูญเสีย $24.48\%$ และ $75.52\%$
   - แสดงวิธีทำ Complete Graph $N=10$ ($45$ เส้น)
   - ตาราง Indegree Tracing ครบ 6 รอบ และ Circular Array Queue พร้อมเฉลยคำตอบทางการ `1, 2, 5, 4, 3, 7, 6`
2. **[`Topological sort.pdf`](./Topological%20sort.pdf)**:
   - เอกสารแจกในห้องเรียนต้นฉบับ 6 หน้า (แบบฝึกหัดสำหรับเติมคำตอบ)
3. **[`Lecture 10 Graph.pdf`](./Lecture%2010%20Graph.pdf)**:
   - สไลด์บรรยายหลักทางการ 15 สไลด์ (Definition, Representation of Graphs, Topological Sort)
4. **[`Topological_Sort_Classroom_Wiki.md`](./Topological_Sort_Classroom_Wiki.md)** 📖:
   - สารานุกรมถอดความและเฉลยละเอียดครบทุกหน้า (หน้า 1 ถึง 6)
   - มีแผนภาพ Mermaid, ตาราง Tracing, โค้ด Python Kahn's Algorithm และวิเคราะห์กับดักจุด 0 คะแนน

---

## 📖 การเชื่อมโยงกับระบบ Wiki และแบบฝึกหัด

- 📚 **สารานุกรมเฉลยละเอียดรายหน้า:** [`Topological_Sort_Classroom_Wiki.md`](./Topological_Sort_Classroom_Wiki.md)
- 🎯 **คลังข้อสอบและตัวอย่างห้องเรียนรวม (Lecture 10 & 11):** [`DSA-Wiki/13 - ตัวอย่างโจทย์และข้อควรระวังในห้องเรียน/13.8 - For Example Lecture 10 & 11 Graph.md`](../../DSA-Wiki/13%20-%20ตัวอย่างโจทย์และข้อควรระวังในห้องเรียน%20(Classroom%20For%20Example%20Tracing)/13.8%20-%20For%20Example%20Lecture%2010%20&%2011%20Graph%20(Topological%20Sort,%20BFS%20Shortest%20Path%20&%20คำนวณขยะ%20Matrix).md)
- 🕸️ **ทฤษฎีบทที่ 9 (Graph):** [`DSA-Wiki/09 - บทที่ 9 Graph/09.1 - Graph Fundamentals & Traversals.md`](../../DSA-Wiki/09%20-%20บทที่%209%20Graph%20(โครงสร้างข้อมูลกราฟ)/09.1%20-%20Graph%20Fundamentals%20&%20Traversals%20(BFS,%20DFS,%20Topological%20Sort).md)
- 🚀 **Interactive Debugger:** [เปิด Graph BFS Shortest Path Debugger ใน DsaLab](../../DSA-Wiki/DsaLab/index.html?topic=assign4)