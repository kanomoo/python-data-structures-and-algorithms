const fs = require('fs');

// Read wiki-data.js
const wikiCode = fs.readFileSync('Wiki/wiki-data.js', 'utf8');
const window = {};
eval(wikiCode);

const docs = window.WIKI_DATA.documents;

// Read engine code from build_all_visualizers.py
const pyScript = fs.readFileSync('scratch/build_all_visualizers.py', 'utf8');
const startToken = "def get_engine_code():\n    return r'''";
const endToken = "\n'''\n";
const engineStart = pyScript.indexOf(startToken) + startToken.length;
const engineEnd = pyScript.indexOf(endToken, engineStart);
const engineJs = pyScript.substring(engineStart, engineEnd);

// Read app.js generic visualizer
const appJs = fs.readFileSync('Wiki/app.js', 'utf8');
const genStart = appJs.indexOf('function generateGenericDsaLabVisual');
const genEnd = appJs.indexOf('async function renderMermaidDiagrams');
const genJs = appJs.substring(genStart, genEnd);

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Evaluate
eval(genJs);
eval(engineJs);

console.log('Testing 48 diagrams...\n');

let diagramIndex = 0;
let genericCount = 0;
let dedicatedCount = 0;

const results = [];

for (const [docId, doc] of Object.entries(docs)) {
  const content = doc.content || '';
  const regex = /```mermaid\s*\n([\s\S]*?)\n```/g;
  let match;
  let inDocIdx = 0;
  while ((match = regex.exec(content)) !== null) {
    diagramIndex++;
    inDocIdx++;
    const code = match[1];
    const res = buildNativeDsaVisual(code, docId);
    const isGeneric = !res.title || res.title.includes('แบบจำลองโครงสร้าง') || res.html.includes('dsa-native-tree-wrap');
    
    results.push({
      num: diagramIndex,
      docId: docId,
      inDocIdx: inDocIdx,
      title: res.title,
      isGeneric: isGeneric,
      codePreview: code.split('\n')[0]
    });

    if (isGeneric) {
      genericCount++;
      console.log(`❌ #${diagramIndex} [GENERIC] Doc: "${docId}" (${inDocIdx}) -> ${res.title}`);
    } else {
      dedicatedCount++;
      console.log(`✅ #${diagramIndex} [DEDICATED] Doc: "${docId}" (${inDocIdx}) -> ${res.title}`);
    }
  }
}

console.log(`\n========================================`);
console.log(`Total: ${diagramIndex} | Dedicated: ${dedicatedCount} | Generic: ${genericCount}`);
console.log(`========================================`);
