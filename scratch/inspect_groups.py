import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/all_diagrams.json', 'r', encoding='utf-8') as f:
    diagrams = json.load(f)

for i, d in enumerate(diagrams):
    code_first = d["code"].splitlines()[0]
    print(f"[{i+1:02d}] docId: '{d['docId']}' | inDoc: {d['indexInDoc']} | line1: {code_first}")
