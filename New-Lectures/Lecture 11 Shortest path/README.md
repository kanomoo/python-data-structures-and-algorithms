# 📘 บทที่ 11: เส้นทางที่สั้นที่สุด (Shortest Path Algorithms & Dijkstra's Algorithm)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **Single-Source Shortest Path**: การค้นหาเส้นทางที่มีผลรวมน้ำหนักค่าน้อยที่สุดจากจุดเริ่มต้นไปยังทุกจุด
2. **Dijkstra's Algorithm (อัลกอริทึมของไดก์สตรา)**:
   - ใช้หลักการ Greedy Method
   - ข้อมูลแต่ละจุดยอด $v$:
     - `Known`: สถานะเยี่ยมชม (True/False)
     - `Cost` ($d_v$): ระยะทางรวมที่สั้นที่สุดที่ค้นพบ
     - `Path` ($p_v$): โหนดก่อนหน้าบนเส้นทางที่สั้นที่สุด
   - กฎการอัปเดต: ถ้า $d_v + c_{v,w} < d_w$ ให้ปรับ $d_w = d_v + c_{v,w}$ และ $p_w = v$
   - ตารางต้องไล่ทีละรอบอย่างละเอียดถูกต้อง (หัวข้อหลักของการบ้าน Assignment 4 และข้อสอบปลายภาค)

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 11 168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%2011%20168.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานกราฟและเส้นทางสั้นสุด** | [`For Example Graph.pdf`](./For%20Example%20Graph.pdf) | โจทย์แบบฝึกหัดตาราง Dijkstra และกราฟมีทิศทาง |
| 🌟 **เฉลยใบงานกราฟ** | [`For Example Graph_solved.pdf`](./For%20Example%20Graph_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 🔗 **โฟลเดอร์การบ้าน Assignment 4** | [`../Assignment 4 Shortest Path/`](../Assignment%204%20Shortest%20Path/) | โฟลเดอร์งาน Assignment 4 พร้อมเฉลยเริ่มจุด A และจุด B ครบถ้วน |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 9 ภาพ: กระดานสอนสด Dijkstra (838089388...), การลงตาราง Known/Cost/Path |
