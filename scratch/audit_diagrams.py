import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/all_diagrams.json', 'r', encoding='utf-8') as f:
    diagrams = json.load(f)

for idx, d in enumerate(diagrams, 1):
    print(f"=== DIAGRAM #{idx:02d} | Doc: {d['docId']} | IndexInDoc: {d['indexInDoc']} ===")
    lines = d['code'].split('\n')
    for l in lines[:10]:
        print("  " + l)
    if len(lines) > 10:
        print(f"  ... ({len(lines) - 10} more lines)")
    print()
