import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('Wiki/wiki-data.js', 'r', encoding='utf-8') as f:
    wiki_text = f.read()

# Match docs by finding: id: 'doc-...' or id: "doc-..."
doc_splits = re.split(r'\n\s*id:\s*[\'"]', wiki_text)
print(f"Doc splits: {len(doc_splits)}")

total_mermaid = 0
for idx, chunk in enumerate(doc_splits[1:], 1):
    doc_id = chunk.split("'", 1)[0].split('"', 1)[0]
    mermaid_blocks = re.findall(r'```mermaid\s*\n(.*?)\n```', chunk, re.DOTALL)
    if mermaid_blocks:
        print(f"Doc [{doc_id}]: {len(mermaid_blocks)} diagrams")
        total_mermaid += len(mermaid_blocks)

print(f"Total mermaid diagrams found: {total_mermaid}")
