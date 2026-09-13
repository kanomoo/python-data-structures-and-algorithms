import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/all_diagrams.json', 'r', encoding='utf-8') as f:
    diagrams = json.load(f)

for idx, d in enumerate(diagrams, 1):
    first_line = d['code'].split('\n')[0]
    sample_nodes = [line.strip() for line in d['code'].split('\n') if '-->' in line or '---' in line][:2]
    print(f"#{idx:02d} | Doc: {d['docId'][:35]} | Line1: {first_line[:30]} | Sample: {' ; '.join(sample_nodes)[:60]}")
