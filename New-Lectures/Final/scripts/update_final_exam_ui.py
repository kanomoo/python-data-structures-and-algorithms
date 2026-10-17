import os

file_path = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
old_css = '''  .print-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: #2563eb;
    color: white;
    border: none;
    padding: 12px 22px;
    border-radius: 50px;
    font-size: 15px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 1000;
  }
  .print-btn:hover { background: #1d4ed8; }

  @media print {
    body { padding: 0; background: white; }
    .container { box-shadow: none; border: none; padding: 0; max-width: 100%; }
    .print-btn { display: none; }
  }'''

new_css = '''  /* Quick Navigation Jump Bar */
  .nav-jump-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin: 15px 0 25px 0;
    padding: 12px 16px;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
  }
  .nav-jump-label {
    font-size: 13.5px;
    font-weight: 700;
    color: #1e293b;
    margin-right: 4px;
  }
  .jump-pill {
    display: inline-block;
    padding: 5px 12px;
    background: #ffffff;
    color: #2563eb;
    border: 1px solid #bfdbfe;
    border-radius: 20px;
    font-size: 12.5px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.15s ease;
  }
  .jump-pill:hover {
    background: #2563eb;
    color: #ffffff;
    border-color: #2563eb;
  }
  .jump-pill.alt {
    background: #fef3c7;
    color: #92400e;
    border-color: #fde68a;
  }
  .jump-pill.alt:hover {
    background: #d97706;
    color: #ffffff;
    border-color: #d97706;
  }
  .jump-pill.danger {
    background: #fee2e2;
    color: #991b1b;
    border-color: #fecaca;
  }
  .jump-pill.danger:hover {
    background: #dc2626;
    color: #ffffff;
    border-color: #dc2626;
  }

  /* Floating Action Bar */
  .floating-bar {
    position: fixed;
    bottom: 25px;
    right: 25px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 9999;
  }
  .action-btn {
    background: #2563eb;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s ease;
    font-family: inherit;
  }
  .action-btn:hover {
    background: #1d4ed8;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.45);
  }
  .action-btn.toggle-btn {
    background: #0d9488;
    box-shadow: 0 4px 15px rgba(13, 148, 136, 0.35);
  }
  .action-btn.toggle-btn:hover {
    background: #0f766e;
    box-shadow: 0 6px 20px rgba(13, 148, 136, 0.45);
  }
  .action-btn.toggle-btn.alt {
    background: #d97706;
    box-shadow: 0 4px 15px rgba(217, 119, 6, 0.35);
  }
  .action-btn.top-btn {
    background: #475569;
    box-shadow: 0 4px 15px rgba(71, 85, 105, 0.35);
  }
  .action-btn.top-btn:hover {
    background: #334155;
  }

  @media print {
    @page {
      size: A4;
      margin: 12mm 15mm 15mm 15mm;
    }
    body {
      padding: 0 !important;
      background: white !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    .container {
      box-shadow: none !important;
      border: none !important;
      padding: 0 !important;
      max-width: 100% !important;
      width: 100% !important;
    }
    .floating-bar, .nav-jump-bar {
      display: none !important;
    }
    .solution-box, .blank-sheet-box, table, .question-title, svg, .theory-box {
      page-break-inside: avoid !important;
    }
    .section-heading, .part-title {
      page-break-after: avoid !important;
    }
  }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    print("CSS replaced successfully")
else:
    print("CSS old chunk not found")

# 2. Add nav jump bar right below rules box
old_rules_end = '      </li>\n    </ul>\n  </div>'
nav_jump_bar = '''      </li>
    </ul>
  </div>

  <!-- QUICK NAVIGATION JUMP BAR -->
  <div class="nav-jump-bar">
    <span class="nav-jump-label">⚡ ทางลัดไปข้อสอบ (Quick Navigation):</span>
    <a href="#q1" class="jump-pill">ข้อ 1 Hashing</a>
    <a href="#q2" class="jump-pill">ข้อ 2 Binary Min-Heap</a>
    <a href="#q3" class="jump-pill">ข้อ 3 Insertion Sort</a>
    <a href="#q4" class="jump-pill">ข้อ 4 Selection & Bubble</a>
    <a href="#q5" class="jump-pill">ข้อ 5 Topological Sort</a>
    <a href="#q6" class="jump-pill">ข้อ 6 Shortest Path</a>
    <a href="#q7" class="jump-pill">ข้อ 7 ทฤษฎีและการคำนวณ</a>
    <a href="#part2" class="jump-pill alt">ตอนที่ 2 นิยามและทฤษฎี</a>
    <a href="#traps" class="jump-pill danger">ตอนที่ 3 ตาราง 12 กับดัก 0 คะแนน</a>
  </div>'''

if old_rules_end in content:
    content = content.replace(old_rules_end, nav_jump_bar, 1)
    print("Nav jump bar inserted successfully")
else:
    print("Rules box end not found")

# 3. Add ids to question titles
content = content.replace('<h2 class="part-title">Question 1:', '<h2 id="q1" class="part-title">Question 1:')
content = content.replace('<h2 class="part-title">Question 2:', '<h2 id="q2" class="part-title">Question 2:')
content = content.replace('<h2 class="part-title">Question 3:', '<h2 id="q3" class="part-title">Question 3:')
content = content.replace('<h2 class="part-title">Question 4:', '<h2 id="q4" class="part-title">Question 4:')
content = content.replace('<h2 class="part-title">Question 5:', '<h2 id="q5" class="part-title">Question 5:')
content = content.replace('<h2 class="part-title">Question 6:', '<h2 id="q6" class="part-title">Question 6:')
content = content.replace('<h2 class="part-title">Question 7:', '<h2 id="q7" class="part-title">Question 7:')
content = content.replace('<h1 class="section-heading">📖 ตอนที่ 2:', '<h1 id="part2" class="section-heading">📖 ตอนที่ 2:')
content = content.replace('<h1 class="section-heading">🛑 ตอนที่ 3:', '<h1 id="traps" class="section-heading">🛑 ตอนที่ 3:')

# 4. Update button and add floating bar & script at the bottom
old_btn = '''<button class="print-btn" onclick="window.print()">
  🖨️ พิมพ์ข้อสอบ / บันทึก PDF (Print Exam)
</button>'''

new_btn_and_script = '''<div class="floating-bar">
  <button class="action-btn" onclick="window.print()" title="พิมพ์ข้อสอบหรือบันทึกเป็น PDF">
    🖨️ พิมพ์ / บันทึก PDF (Print Exam)
  </button>
  <button id="toggleSolBtn" class="action-btn toggle-btn" onclick="toggleSolutions()" title="สลับโหมดข้อสอบเปล่า vs ข้อสอบพร้อมเฉลย">
    👁️ ซ่อนเฉลย (โหมดข้อสอบเปล่า)
  </button>
  <button class="action-btn top-btn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="กลับขึ้นบนสุด">
    ⬆️ กลับขึ้นบนสุด
  </button>
</div>

<script>
let solutionsVisible = true;
function toggleSolutions() {
  const solutions = document.querySelectorAll('.solution-box');
  const btn = document.getElementById('toggleSolBtn');
  solutionsVisible = !solutionsVisible;
  solutions.forEach(box => {
    box.style.display = solutionsVisible ? 'block' : 'none';
  });
  if (solutionsVisible) {
    btn.innerHTML = '👁️ ซ่อนเฉลย (โหมดข้อสอบเปล่า)';
    btn.classList.remove('alt');
  } else {
    btn.innerHTML = '👁️ แสดงเฉลย (โหมดเฉลยละเอียด)';
    btn.classList.add('alt');
  }
}
</script>'''

if old_btn in content:
    content = content.replace(old_btn, new_btn_and_script)
    print("Floating bar and script replaced successfully")
else:
    print("Old button not found")

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open(r'C:\Project\python-data-structures-and-algorithms\Exams\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Both final exam web files successfully updated!")
