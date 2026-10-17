# 📘 บทที่ 9: อัลกอริทึมการเรียงลำดับข้อมูล (Sorting Algorithms)

**วิชา**: 060243106 DATA STRUCTURE AND ALGORITHM  
**ผู้สอน**: ดร.ประดิษฐ์ พิทักษ์เสถียรกุล (KMUTNB)

---

## 🎯 สาระสำคัญประจำบท (Core Concepts)
1. **Bubble Sort**: เปรียบเทียบคู่ติดกันแล้วสลับ (Complexity: $O(N^2)$)
2. **Selection Sort**: ค้นหาค่าน้อยที่สุดในส่วนที่เหลือแล้วนำมาสลับกับตำแหน่งแรก (Complexity: $O(N^2)$)
3. **Insertion Sort**: แทรกข้อมูลแต่ละตัวเข้าไปในตำแหน่งที่ถูกต้องในส่วนที่เรียงแล้ว
   - **กฎการนับจำนวน Move (การเคลื่อนย้ายข้อมูล)**: แต่ละรอบจะมีการเปรียบเทียบและการขยับข้อมูลตามจำนวนการแทรก (ออกข้อสอบตารางสรุป Move เสมอ)
4. **Shell Sort & Heapsort**: อัลกอริทึมที่มีประสิทธิภาพสูงขึ้น

---

## 📁 ไฟล์เอกสารและสื่อการเรียนรู้ในบทนี้

| ประเภท | ชื่อไฟล์ | สถานะ/คำอธิบาย |
| :---: | :--- | :--- |
| 📑 **สไลด์บรรยายหลักสูตรใหม่** | [`DATA STRUCTURES - ALGORITHMS_Lecture 9 168.pdf`](./DATA%20STRUCTURES%20-%20ALGORITHMS_Lecture%209%20168.pdf) | สไลด์ฉบับทางการ Google Classroom |
| 📝 **ใบงานแบบฝึกหัด Bubble Sort** | [`For Example Bubble sort.pdf`](./For%20Example%20Bubble%20sort.pdf) | โจทย์ไล่สถานะ Bubble Sort |
| 🌟 **เฉลย Bubble Sort** | [`For Example Bubble sort_solved.pdf`](./For%20Example%20Bubble%20sort_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 📝 **ใบงานแบบฝึกหัด Selection Sort** | [`For Example Selection sort 169.pdf`](./For%20Example%20Selection%20sort%20169.pdf) | โจทย์ไล่สถานะ Selection Sort |
| 🌟 **เฉลย Selection Sort** | [`For Example Selection sort 169_solved.pdf`](./For%20Example%20Selection%20sort%20169_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 📝 **สรุปสั้นและหมายเหตุ Insertion Sort** | • [`Short note Insertion sort.pdf`](./Short%20note%20Insertion%20sort.pdf)<br>• [`หมายเหตุ ในหัวข้อ insertion sort.pdf`](./หมายเหตุ%20ในหัวข้อ%20insertion%20sort.pdf) | สรุปประเด็นสำคัญและสูตรการนับ Move |
| 🌟 **เฉลย Insertion Sort** | [`Short note Insertion sort_solved.pdf`](./Short%20note%20Insertion%20sort_solved.pdf) | เฉลยละเอียดระดับ Master Solution |
| 🐍 **โค้ดภาษา Python** | [`BubbleSort.py`](./BubbleSort.py) | ตัวอย่างการเขียนโค้ด Sorting |
| 📸 **ภาพถ่ายกระดานห้องเรียน** | [`images/`](./images/) | รวม 6 ภาพ: สไลด์ห้องเรียน 16 ก.ย., ตาราง Moves, และกระดานสรุป |
