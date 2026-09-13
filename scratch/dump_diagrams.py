import json, re

with open('Wiki/wiki-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.WIKI_DATA = ')
raw_json = text[idx + len('window.WIKI_DATA = '):].rstrip('; \r\n')
data = json.loads(raw_json)
docs = data.get('documents', {})

all_diagrams = []

for doc_id, doc_info in docs.items():
    content = doc_info.get('content', '')
    blocks = re.findall(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
    for i, b in enumerate(blocks):
        all_diagrams.append({
            'docId': doc_id,
            'indexInDoc': i + 1,
            'code': b.strip()
        })

print(f"Extracted {len(all_diagrams)} diagrams.")
with open('scratch/all_diagrams.json', 'w', encoding='utf-8') as out:
    json.dump(all_diagrams, out, ensure_ascii=False, indent=2)
print("Saved to scratch/all_diagrams.json")
