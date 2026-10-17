# -*- coding: utf-8 -*-
import sys, re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

filepath = r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

blank_boxes = re.findall(r'<div class="blank-sheet-box[\s\S]*?</div>', text)
print("Total blank sheet boxes found:", len(blank_boxes))

spoilers_found = 0
for i, box in enumerate(blank_boxes, 1):
    for sp in ['R = 17', 'R=17', 'h_0(X) = X mod 19', 'h0(X) = X mod 19', '75.51%', '2047']:
        if sp in box:
            print(f"Blank sheet box {i} contains spoiler: {sp}!")
            spoilers_found += 1

print(f"Total spoilers in blank sheets: {spoilers_found}")

# Also check thai-trans outside solution-box
thai_trans = re.findall(r'<div class="thai-trans">([\s\S]*?)</div>', text)
print("Total thai-trans blocks found:", len(thai_trans))
for i, tt in enumerate(thai_trans, 1):
    # Check if any answer leak in thai-trans
    for leak in ['ชน 3 ครั้ง', 'รวมชน 7 ครั้ง', 'ได้ 45 เส้น', 'ตอบ 45', '75.51%', '2047 โหนด', '1024 โหนด']:
        if leak in tt:
            print(f"thai-trans {i} contains leak: {leak}!")
            spoilers_found += 1

print(f"Comprehensive check complete. Total leaks: {spoilers_found}")
