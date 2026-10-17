# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

t = open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py', encoding='utf-8').read()
for q in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']:
    pos = t.find('id="' + q + '"')
    next_pos = t.find('id="q', pos + 10) if q != 'q7' else len(t)
    chunk = t[pos:next_pos]
    has_warn = ('🎙️' in chunk) or ('คำเตือน' in chunk) or ('คำพูด' in chunk) or ('กับดัก' in chunk)
    print(f"{q}: has_warn={has_warn}")
