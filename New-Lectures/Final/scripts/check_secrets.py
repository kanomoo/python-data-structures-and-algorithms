# -*- coding: utf-8 -*-
import sys, re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab_secrets.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for spoilers outside <details> or outside <div class="solution-box">
blocks = re.split(r'<details|<div class="solution-box"', text)
for b_idx, block in enumerate(blocks):
    # Only the first part of each split is outside solution
    # In each block, before the next </details> or </div> might be solution,
    # but let's check all <p><strong>Question Statement</strong> or thai-trans
    for match in re.finditer(r'<div class="thai-trans">([\s\S]*?)</div>', block):
        content = match.group(1)
        # Check if answers are leaked in thai-trans
        for leak in ['ชน 3 ครั้ง', 'รวมชน 7 ครั้ง', 'ได้ 45 เส้น', 'ตอบ 45', '75.51%', '2047 โหนด', '1024 โหนด']:
            if leak in content:
                print(f"Block {b_idx} thai-trans contains answer leak: {leak}")
    
    for match in re.finditer(r'<div class="blank-sheet-box[\s\S]*?</div>', block):
        content = match.group(0)
        for leak in ['45', '75.51%', '2047', '1024', '7 ครั้ง']:
            if leak in content:
                print(f"Block {b_idx} blank-sheet contains answer leak: {leak}")
