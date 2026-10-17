# -*- coding: utf-8 -*-
import sys, re, os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

target_files = [
    r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab_set0.py',
    r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py',
    r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab_secrets.py',
    r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab2.py',
    r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab3.py',
]

for f in target_files:
    fname = os.path.basename(f)
    print(f"\n==================== {fname} ====================")
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    
    in_sol = 0
    for i, line in enumerate(lines, 1):
        if 'solution-box' in line:
            in_sol += 1
        if in_sol > 0 and '</div>' in line:
            in_sol -= line.count('</div>')
            if in_sol < 0:
                in_sol = 0
        
        # Check C++ keywords
        for kw in ['HashEntry', 'ACTIVE', 'vector<', 'void insertionSort', 'vector <']:
            if kw in line:
                print(f"  [C++ kw {kw}] Line {i}: {line.strip()[:100]}")
        
        # Check for info row or element row in tables
        if re.search(r'<td>\s*(?:Info|info|Element|element)\s*</td>', line, re.I):
            print(f"  [Table row Info/Element] Line {i}: {line.strip()[:100]}")
        
        # Check for spoilers outside solution box
        if in_sol == 0:
            for sp in ['R = 17', 'R=17', 'h_0(X) = X mod 19', 'h0(X) = X mod 19', 'R = 7', 'R=7']:
                if sp in line:
                    print(f"  [Spoiler {sp}] Line {i}: {line.strip()[:100]}")
