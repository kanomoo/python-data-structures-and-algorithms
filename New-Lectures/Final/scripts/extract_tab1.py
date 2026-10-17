# -*- coding: utf-8 -*-
with open(r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "🌟 ตอนที่ 1:"
end_marker = "🎯 ตอนที่ 2:"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

print("start_idx:", start_idx, "end_idx:", end_idx)
# Find the start tag <h1 before start_marker
h1_start = text.rfind("<h1", 0, start_idx)
# Find the separator before end_idx
h1_end = text.rfind("<!-- ======", 0, end_idx)
print("h1_start:", h1_start, "h1_end:", h1_end)
tab1_raw = text[h1_start:h1_end]
print("tab1_raw length:", len(tab1_raw))
