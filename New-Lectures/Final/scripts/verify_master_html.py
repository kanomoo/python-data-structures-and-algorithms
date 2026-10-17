# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

filepath = r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

print("File size:", len(text), "bytes")

# Check tabs
tabs = re.findall(r'<div id="(tab-[^"]+)" class="tab-content', text)
print("Tabs found:", tabs)

# Check Tab 0 questions
q_set0 = re.findall(r'<h2 id="(set0-q\d)"', text)
print("Tab Set 0 questions:", q_set0)

# Check Tab 1 questions
q_tab1 = re.findall(r'<h2 id="(q\d)"', text)
print("Tab 1 questions:", q_tab1)

# Check Tab Secrets questions
q_secrets = re.findall(r'<h2 id="(sec-q\d)"', text)
print("Tab Secrets questions:", q_secrets)

# Check Tab 3 (Past) questions
q_tab2 = re.findall(r'<h2 id="(past-q\d)"', text)
print("Tab Past questions:", q_tab2)

# Check Tab 3 anchors
th_anchors = re.findall(r'<div id="(th-[^"]+)"', text)
print("Tab 3 theory sections:", th_anchors)

# Check key terms
terms = [
    "Wrap Around", "mod tablesize", "How to choose a new TableSize",
    "smallest prime", "Double Hashing", "R = 17", "R = 7",
    "Worst-Case", "Average-Case", "Best-Case", "Inversions",
    "deleteMin()", "hole", "1,024", "2,047", "65,536", "131,071",
    "45 เส้น", "120 เส้น", "24.49", "75.51", "Pigeonhole",
    "Structure Property", "Heap-Order Property", "12 กับดัก",
    "168 ตัว", "ASCII", "CAT", "DOG", "th-primes", "th-ascii"
]

print("\n--- Keyword Presence Check ---")
for t in terms:
    count = text.count(t)
    print(f"[{'OK' if count > 0 else 'MISSING'}] '{t}': {count} occurrences")

print("\n--- Floating Buttons & JS Check ---")
print("printActiveTab:", "printActiveTab()" in text)
print("printAllTabs:", "printAllTabs()" in text)
print("toggleSolutions:", "toggleSolutions()" in text)
print("scrollToTop:", "scrollToTop()" in text)
print("MathJax present:", "MathJax-script" in text)
print("SVG diagrams count:", text.count("<svg"))
