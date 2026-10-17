# -*- coding: utf-8 -*-
"""
Script to fix generate_tab1.py:
1. Remove spoiler R=17 from rules box
2. Purge C++ '(ใน 1 ช่อง มี element กับ info)' from prompt
3. Purge C++ 'Element' & 'Info: A' rows from Hash Table, replacing with pure Python 'Value (Key)'
4. Remove duplicate lines 557-775 (accidental duplicate Q1 solution and duplicate Q2 header)
5. Seamlessly merge Question 2 (2 Properties + 4 vertical tables + 4 tree SVG diagrams + 4 arrays)
"""
import sys, re

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix spoiler in rules box
content = content.replace(
    r'• <strong>ค่าคงที่ R ใน Double Hashing:</strong> สำหรับตารางขนาด 19 ต้องเลือก $R = 17$ (จำนวนเฉพาะที่มากที่สุดที่ $R < 19$) และหากขนาดตารางเป็น 11 ต้องเลือก $R = 7$ <em>ห้ามเลือก 11 เด็ดขาด เพราะจะเกิด Infinite Loop</em>',
    r'• <strong>ค่าคงที่ R ใน Double Hashing:</strong> ต้องเลือกจำนวนเฉพาะที่มากที่สุดที่น้อยกว่าขนาดตาราง ($R < \text{TableSize}$) อย่างเคร่งครัด หากขนาดตารางเป็น 11 ต้องเลือก $R = 7$ (ห้ามเลือก 11 เด็ดขาด เพราะจะเกิด Infinite Loop)'
)

# 2. Fix C++ element/info mention in prompt
content = content.replace(
    r'1. ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Hash Table (ใน 1 ช่อง มี <code>element</code> กับ <code>info</code>) กำหนด <strong>TableSize ให้เป็น 19</strong>',
    r'1. ให้นักศึกษาเขียนตารางอะเรย์ ตามโครงสร้าง Hash Table กำหนด <strong>TableSize ให้เป็น 19</strong>'
)

# 3. Fix Element label in blank sheet box
content = content.replace(
    r'<td style="padding:6px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Element</td>',
    r'<td style="padding:6px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Value (Key)</td>'
)

# 4. In Q1 solution table, remove Info row and replace Element with Value (Key)
# Pattern for Info row 0-9:
info_row_pattern1 = r'<tr style="background:#f8fafc;">\s*<td style="padding:6px 4px; font-weight:bold; background:#e2e8f0; border:1px solid #cbd5e1; color:#0f172a;">Info</td>[\s\S]*?</tr>'
# Pattern for Info row 10-18:
# Let's replace Element in Q1 solution table with Value (Key)
content = content.replace(
    r'<td style="padding:7px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Element</td>',
    r'<td style="padding:7px 4px; font-weight:bold; background:#f1f5f9; border:1px solid #cbd5e1; color:#0f172a;">Value (Key)</td>'
)

# Remove the Info rows in Q1 solution table
content = re.sub(r'<tr style="background:#f8fafc;">\s*<td[^>]*>Info</td>[\s\S]*?</tr>\s*', '', content)

# 5. Fix Question 2:
# In Question 2's problem statement before the 4 tables, make sure 2.1 asks for properties:
old_q2_intro = r"""  <h3 class="question-title">
    <span>2. Binary Heap 4 Vertical Arrays (Insertions, deleteMin, Insert, deleteMin)</span>
    <span class="score-badge">Score: 10 Marks (1 + 2 + 2 + 3 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Binary Min-Heap implemented as a 1-based array (where index 0 is unused / sentinel). You are given the sequence of 12 keys:</p>
  $$\mathbf{64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20}$$
  <p><strong>Sub-questions according to the official exam paper:</strong></p>
  <ul>
    <li><strong>2.1:</strong> Insert the 12 keys into the Binary Heap. Write <em>only the final resulting array</em> into vertical table 1 [1 คะแนน]</li>
    <li><strong>2.2:</strong> Perform <code>deleteMin()</code> 1 time and write the resulting array into vertical table 2 [2 คะแนน]</li>
    <li><strong>2.3:</strong> Insert key <code>3</code> into the heap and write the resulting array into vertical table 3 [2 คะแนน]</li>
    <li><strong>2.4:</strong> Perform <code>deleteMin()</code> one more time and write the final resulting array into vertical table 4 [3 คะแนน]</li>
  </ul>"""

new_q2_intro = r"""  <h3 class="question-title">
    <span>2. Binary Min-Heap: Properties, 4-Stage Array Operations &amp; Tree Visualizations</span>
    <span class="score-badge">Score: 10 Marks (2 + 2 + 2 + 2 + 2 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given an empty Binary Min-Heap implemented as a 1-based array in Python (where index 0 is unused / <code>None</code>). You are given the sequence of 12 keys:</p>
  $$\mathbf{64, 14, 24, 1, 20, 2, 5, 10, 6, 8, 15, 20}$$
  <p><strong>Sub-questions according to the official examination standards:</strong></p>
  <ol>
    <li><strong>2.1 Fundamental Properties:</strong> State the two fundamental properties (Structure Property &amp; Heap-Order Property) that govern a Binary Min-Heap [2 คะแนน]</li>
    <li><strong>2.2 Sequential Insertions:</strong> Insert all 12 keys into the Binary Heap. Write the resulting array into vertical table 1 [2 คะแนน]</li>
    <li><strong>2.3 First deleteMin:</strong> Perform <code>deleteMin()</code> 1 time and write the resulting array into vertical table 2 [2 คะแนน]</li>
    <li><strong>2.4 Key Insertion:</strong> Insert key <code>3</code> into the heap and write the resulting array into vertical table 3 [2 คะแนน]</li>
    <li><strong>2.5 Second deleteMin:</strong> Perform <code>deleteMin()</code> one more time and write the final resulting array into vertical table 4 [2 คะแนน]</li>
  </ol>"""

content = content.replace(old_q2_intro, new_q2_intro)

# 6. Remove the duplicate block between line 556 and line 776:
# Find:
# </div>\s*</div>\s*</div>\s*<div class="solution-box">\s*<div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>[\s\S]*?<div class="solution-box">\s*<div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี (Complete Solution &amp; Principles):</div>\s*<div class="theory-box">
dup_marker_start = '<!-- Table 4 -->'
dup_regex = r'(<!-- Table 4 -->[\s\S]*?</table>\s*</div>\s*</div>\s*</div>)\s*<div class="solution-box">\s*<div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี \(Complete Solution &amp; Principles\):</div>[\s\S]*?(<div class="solution-box">\s*<div class="solution-title">💡 เฉลยละเอียดและหลักการทางทฤษฎี \(Complete Solution &amp; Principles\):</div>\s*<div class="theory-box">)'

match = re.search(dup_regex, content)
if match:
    print("Found duplicate block! Replacing...")
    content = content[:match.start()] + match.group(1) + "\n\n  " + match.group(2) + content[match.end():]
else:
    print("WARNING: Duplicate regex did not match!")

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_tab1.py updated successfully!")
