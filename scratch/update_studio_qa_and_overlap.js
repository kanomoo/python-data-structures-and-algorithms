// Script to inject renderQaPanel, update tree coordinates to eliminate overlap,
// and add comprehensive Q&A Solution data to all simulators in Wiki/dsa-interactive-studio.js
const fs = require('fs');
const path = require('path');

const targetFile = path.join(__dirname, '..', 'Wiki', 'dsa-interactive-studio.js');
let code = fs.readFileSync(targetFile, 'utf8').replace(/\r\n/g, '\n');

// 1. Add renderQaPanel helper right after renderCodeDebugger
const helperMarker = 'function renderCodeDebugger(container, codeLines, activeLine) {';
const newQaHelper = `function renderQaPanel(container, qa) {
    if (!container || !qa) return;
    const qEl = container.querySelector('.qa-question-text');
    const aEl = container.querySelector('.qa-answer-text');
    const dEl = container.querySelector('.qa-danger-text');
    if (qEl) qEl.innerHTML = qa.question || '-';
    if (aEl) aEl.innerHTML = qa.answer || '-';
    if (dEl) dEl.innerHTML = qa.danger || '-';
  }

  `;

if (!code.includes('function renderQaPanel(')) {
  code = code.replace(helperMarker, newQaHelper + helperMarker);
}

// 2. Add the QA panel HTML template into createStudioWidgetHtml
const canvasMarker = `<!-- Interactive Canvas Viewport -->
        <div class="studio-main-viewport">
          <div class="studio-canvas-area"></div>
        </div>`;

const newCanvasWithQa = `<!-- Interactive Canvas Viewport -->
        <div class="studio-main-viewport">
          <div class="studio-canvas-area"></div>
        </div>

        <!-- Official Exam Q&A Solution Panel -->
        <div class="studio-qa-solution-panel">
          <div class="qa-header">
            <span class="qa-icon">🎯</span>
            <span class="qa-title">โจทย์คำถามและเฉลยคำตอบสำหรับส่งอาจารย์ (Official Exam Q&A Solution)</span>
            <span class="qa-badge">คำตอบฉบับสมบูรณ์</span>
          </div>
          <div class="qa-content">
            <div class="qa-question-box">
              <div class="qa-lbl">📌 คำถามในห้องเรียน / ข้อสอบ:</div>
              <div class="qa-text qa-question-text">พร้อมตอบคำถาม...</div>
            </div>
            <div class="qa-answer-box">
              <div class="qa-lbl">🏆 เฉลยคำตอบที่ถูกต้อง (Official Final Answer):</div>
              <div class="qa-text qa-answer-text">พร้อมแสดงเฉลย...</div>
            </div>
            <div class="qa-danger-box">
              <div class="qa-lbl">⚠️ จุดที่ต้องระวัง (Zero-Point Danger / Trap):</div>
              <div class="qa-text qa-danger-text">จุดที่อาจารย์หักคะแนน...</div>
            </div>
          </div>
        </div>`;

if (!code.includes('class="studio-qa-solution-panel"')) {
  code = code.replace(canvasMarker, newCanvasWithQa);
}

// 3. Fix the overlapping coordinates in Assign3HeapSimulator.render()
const oldCoordsRegex = /const svgW = 600;\s*const svgH = 150;\s*let svgHtml = `<svg width="100%" height="\${svgH}" viewBox="0 0 \${svgW} \${svgH}">`;\s*const treeCoords = \[\s*null,\s*\{ x: 300, y: 24 \},\s*\{ x: 180, y: 65 \}, \{ x: 420, y: 65 \},\s*\{ x: 110, y: 110 \}, \{ x: 230, y: 110 \}, \{ x: 350, y: 110 \}, \{ x: 470, y: 110 \},\s*\{ x: 70, y: 140 \}, \{ x: 130, y: 140 \}, \{ x: 190, y: 140 \}, \{ x: 250, y: 140 \}\s*\];/;

const newCoords = `const svgW = 760;
        const svgH = 240;
        let svgHtml = \`<svg width="100%" height="\${svgH}" viewBox="0 0 \${svgW} \${svgH}">\`;
        const treeCoords = [
          null,
          { x: 380, y: 30 },
          { x: 210, y: 85 }, { x: 550, y: 85 },
          { x: 125, y: 145 }, { x: 295, y: 145 }, { x: 465, y: 145 }, { x: 635, y: 145 },
          { x: 75, y: 205 }, { x: 175, y: 205 }, { x: 245, y: 205 }, { x: 345, y: 205 }
        ];`;

if (oldCoordsRegex.test(code)) {
  code = code.replace(oldCoordsRegex, newCoords);
  console.log('Fixed Assign3 tree coordinates!');
} else {
  console.log('treeCoords regex did not match exactly, searching manually...');
}

fs.writeFileSync(targetFile, code, 'utf8');
console.log('Successfully wrote base changes.');
