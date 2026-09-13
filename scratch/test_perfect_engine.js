const fs = require('fs');

// Read wiki-data.js
const wikiCode = fs.readFileSync('Wiki/wiki-data.js', 'utf8');
const window = {};
eval(wikiCode);

const docs = window.WIKI_DATA.documents;

// Read perfect_engine.js
const perfectEngineJs = fs.readFileSync('scratch/perfect_engine.js', 'utf8');

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
eval(perfectEngineJs);

console.log('Testing all 48 diagrams against perfect engine...\n');

let diagramIndex = 0;
let genericCount = 0;
let dedicatedCount = 0;

for (const [docId, doc] of Object.entries(docs)) {
  const content = doc.content || '';
  const regex = /```mermaid\s*\n([\s\S]*?)\n```/g;
  let match;
  let inDocIdx = 0;
  while ((match = regex.exec(content)) !== null) {
    diagramIndex++;
    inDocIdx++;
    const code = match[1];
    const res = buildNativeDsaVisual(code, docId, inDocIdx);
    const isGeneric = !res.title || res.title.includes('แบบจำลองโครงสร้าง') || res.html.includes('dsa-native-tree-wrap');
    
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

if (genericCount > 0) {
  process.exit(1);
} else {
  console.log('🎉 100% SUCCESS: All 48 diagrams have dedicated DsaLab models!');
}
