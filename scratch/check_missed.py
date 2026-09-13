import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/all_diagrams.json', 'r', encoding='utf-8') as f:
    diagrams = json.load(f)

for num in [1, 2, 5, 25, 28, 29, 30, 36, 43, 44]:
    d = diagrams[num - 1]
    print(f"=== #{num:02d} Doc: {d['docId']} ===")
    print(d['code'])
    print("------------------------------------------\n")
