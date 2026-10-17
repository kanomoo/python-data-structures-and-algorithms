# -*- coding: utf-8 -*-
"""
Generate the Master Bilingual Final Examination Web Application with 3 Tabs:
- Tab 1: 🌟 ข้อสอบเก็งฉบับจริงปี 2569 (Official Final Exam 2026 Suite)
- Tab 2: 🏛️ ข้อสอบจริงย้อนหลังปี 2564 & 2561 (Real Past Exams 2564 & 2561 Suite)
- Tab 3: 📖 คลังสรุปทฤษฎี นิยามข้อเขียน & 12 กับดักได้ 0 คะแนน (Theory Mastery & 12 Traps)
"""

import os
import sys

def build_html():
    css_content = """
  :root {
    --primary: #0f172a;
    --primary-accent: #2563eb;
    --secondary-accent: #0284c7;
    --teal-accent: #0d9488;
    --bg-page: #f1f5f9;
    --bg-card: #ffffff;
    --text-main: #1e293b;
    --text-muted: #64748b;
    --border-color: #cbd5e1;
    --success: #15803d;
    --success-bg: #f0fdf4;
    --danger: #b91c1c;
    --danger-bg: #fef2f2;
    --warning: #b45309;
    --warning-bg: #fffbeb;
    --ref-bg: #f8fafc;
    --ref-border: #94a3b8;
  }

  * { box-sizing: border-box; }
  body {
    font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--bg-page);
    color: var(--text-main);
    line-height: 1.6;
    margin: 0;
    padding: 20px;
  }

  .container {
    max-width: 1060px;
    margin: 0 auto;
    background: var(--bg-card);
    padding: 35px 45px;
    border-radius: 12px;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.08);
    border: 1px solid var(--border-color);
  }

  /* Header Section */
  .header {
    text-align: center;
    border-bottom: 2px solid var(--primary);
    padding-bottom: 20px;
    margin-bottom: 20px;
  }
  .university-title {
    font-family: 'Chakra Petch', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--primary);
    margin: 0 0 4px 0;
  }
  .exam-title {
    font-size: 19px;
    font-weight: 700;
    color: var(--primary-accent);
    margin: 4px 0;
  }
  .course-info {
    font-size: 14.5px;
    color: var(--text-muted);
    margin: 4px 0;
  }
  .student-box {
    display: flex;
    justify-content: space-between;
    background: #f8fafc;
    padding: 12px 18px;
    border-radius: 6px;
    margin-top: 15px;
    font-size: 14px;
    font-weight: 500;
    border: 1px solid #e2e8f0;
  }

  /* Rules Box */
  .rules-box {
    background: #eff6ff;
    border-left: 4px solid var(--primary-accent);
    padding: 14px 18px;
    margin-bottom: 22px;
    border-radius: 0 8px 8px 0;
    font-size: 13.5px;
  }
  .rules-title {
    font-weight: 700;
    color: #1e40af;
    margin-bottom: 6px;
    font-size: 15px;
  }

  /* TAB NAVIGATION SYSTEM */
  .tab-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    background: #e2e8f0;
    padding: 6px;
    border-radius: 10px;
    margin-bottom: 25px;
  }
  .tab-btn {
    flex: 1;
    min-width: 220px;
    padding: 12px 16px;
    background: transparent;
    border: none;
    border-radius: 8px;
    font-family: inherit;
    font-size: 14.5px;
    font-weight: 700;
    color: #475569;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }
  .tab-btn:hover {
    background: rgba(255, 255, 255, 0.6);
    color: var(--primary);
  }
  .tab-btn.active {
    background: #ffffff;
    color: var(--primary-accent);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  .tab-btn.active.tab-btn-past {
    color: #0d9488;
  }
  .tab-btn.active.tab-btn-theory {
    color: #b45309;
  }

  .tab-content {
    display: none;
  }
  .tab-content.active {
    display: block;
    animation: fadeIn 0.25s ease;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Section Headings */
  h1.section-heading {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
    padding: 12px 18px;
    border-radius: 8px;
    font-size: 17.5px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 20px;
  }
  h1.section-heading.past-heading {
    background: linear-gradient(135deg, #0f766e, #134e4a);
  }
  h1.section-heading.theory-heading {
    background: linear-gradient(135deg, #9a3412, #7c2d12);
  }

  .part-title {
    font-size: 16.5px;
    font-weight: 700;
    color: var(--primary);
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 25px;
    margin-bottom: 12px;
  }

  .question-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    padding: 8px 14px;
    margin: 14px 0 8px 0;
    font-size: 15px;
    font-weight: 700;
    color: #1e3a8a;
  }
  .question-title.past-q {
    border-left-color: #0d9488;
    color: #0f766e;
  }

  .score-badge {
    background: #dbeafe;
    color: #1d4ed8;
    padding: 3px 9px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 700;
  }
  .score-badge.past-badge {
    background: #ccfbf1;
    color: #0f766e;
  }

  /* Reference Citation Badge */
  .ref-tag {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #cbd5e1;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 8px;
  }

  /* Translations and Solutions */
  .thai-trans {
    background-color: #f8fafc;
    border-left: 3px solid #64748b;
    padding: 10px 14px;
    margin: 8px 0 12px 0;
    font-size: 14px;
    color: #334155;
    border-radius: 0 6px 6px 0;
  }

  .blank-sheet-box {
    background: #ffffff;
    border: 1.5px dashed #94a3b8;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 15px 0;
  }
  .blank-sheet-box.compact {
    padding: 10px 15px;
  }

  .solution-box {
    background: #f0fdf4;
    border: 1px solid #86efac;
    border-left: 4px solid #16a34a;
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
    margin: 16px 0 25px 0;
    font-size: 14px;
  }
  .solution-title {
    font-weight: 700;
    color: #15803d;
    margin-bottom: 10px;
    font-size: 15px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .theory-box {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #d97706;
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
    margin: 16px 0;
    font-size: 14px;
  }

  .alert-box {
    background: #fef2f2;
    border-left: 4px solid #dc2626;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin: 14px 0;
    font-size: 13.5px;
    color: #991b1b;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 13.5px;
  }
  th, td {
    border: 1px solid var(--border-color);
    padding: 8px 10px;
    text-align: left;
  }
  th {
    background-color: #f1f5f9;
    color: #334155;
    font-weight: 600;
  }
  tr:nth-child(even) td {
    background-color: #fbfcfe;
  }

  pre {
    background-color: #1e293b;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 6px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 13px;
    line-height: 1.5;
  }

  code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    background-color: #e2e8f0;
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 0.9em;
  }

  /* Quick Navigation Jump Bar */
  .nav-jump-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin: 12px 0 20px 0;
    padding: 10px 14px;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
  }
  .nav-jump-label {
    font-size: 13px;
    font-weight: 700;
    color: #1e293b;
    margin-right: 4px;
  }
  .jump-pill {
    display: inline-block;
    padding: 4px 10px;
    background: #ffffff;
    color: #2563eb;
    border: 1px solid #bfdbfe;
    border-radius: 16px;
    font-size: 12px;
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
    background: #f0fdfa;
    color: #0d9488;
    border-color: #99f6e4;
  }
  .jump-pill.alt:hover {
    background: #0d9488;
    color: #ffffff;
    border-color: #0d9488;
  }
  .jump-pill.warn {
    background: #fffbeb;
    color: #b45309;
    border-color: #fde68a;
  }
  .jump-pill.warn:hover {
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
    gap: 8px;
    z-index: 9999;
  }
  .action-btn {
    background: #2563eb;
    color: white;
    border: none;
    padding: 11px 18px;
    border-radius: 50px;
    font-size: 13.5px;
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
  .action-btn.print-all-btn {
    background: #0f766e;
    box-shadow: 0 4px 15px rgba(15, 118, 110, 0.35);
  }
  .action-btn.print-all-btn:hover {
    background: #115e59;
  }
  .action-btn.toggle-btn {
    background: #d97706;
    box-shadow: 0 4px 15px rgba(217, 119, 6, 0.35);
  }
  .action-btn.toggle-btn:hover {
    background: #b45309;
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
    .floating-bar, .nav-jump-bar, .tab-nav {
      display: none !important;
    }
    /* When not printing all, hide inactive tabs */
    body:not(.print-all-tabs) .tab-content:not(.active) {
      display: none !important;
    }
    body.print-all-tabs .tab-content {
      display: block !important;
      page-break-after: always !important;
    }
    .solution-box, .blank-sheet-box, table, .question-title, svg, .theory-box {
      page-break-inside: avoid !important;
    }
    .section-heading, .part-title {
      page-break-after: avoid !important;
    }
  }
"""
    return css_content

print("Base CSS prepared.")
