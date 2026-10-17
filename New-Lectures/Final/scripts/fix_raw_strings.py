# -*- coding: utf-8 -*-
"""
Script to ensure all tab generators use raw triple quotes r\"\"\"
and master builder uses raw template with .replace()
"""

import sys

for fname in ["generate_tab1.py", "generate_tab2.py", "generate_tab3.py"]:
    fpath = rf"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\{fname}"
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace 'return """' with 'return r"""'
    if 'return """' in content:
        content = content.replace('return """', 'return r"""')
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fname} to use raw triple quotes r\"\"\"")
    else:
        print(f"{fname} already uses raw quotes or has different syntax")

print("All tab generators checked.")
