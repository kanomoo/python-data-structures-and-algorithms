/**
 * build-wiki.js
 * Scans all Markdown files in DSA-Wiki/, extracts metadata & headings,
 * and compiles them into Wiki/wiki-data.js for fast instant client-side reading.
 * Chapters 1 to 10 are organized sequentially, and Exam Prep is cleanly isolated.
 */

const fs = require('fs');
const path = require('path');

const DSA_WIKI_DIR = path.join(__dirname, 'DSA-Wiki');
const OUTPUT_FILE = path.join(__dirname, 'Wiki', 'wiki-data.js');

// Core sequential curriculum chapters (Chapters 1 to 10)
const CURRICULUM_CATEGORIES = [
  {
    id: 'ch1',
    type: 'curriculum',
    title: '🏛️ บทที่ 1: Introduction & Algorithm Analysis',
    description: 'ความหมาย Data Structure, ADT และการวิเคราะห์ขั้นตอนวิธี Big-O',
    files: [
      '01.1 - Introduction to Data Structures & Algorithm Analysis.md'
    ]
  },
  {
    id: 'ch2',
    type: 'curriculum',
    title: '🐍 บทที่ 2: Review Python & OOP',
    description: 'ทบทวนภาษา Python, คลาส, วัตถุ และหลักการ OOP 4 เสาหลัก',
    files: [
      '02.1 - Python Review & Object-Oriented Programming (OOP).md'
    ]
  },
  {
    id: 'ch3',
    type: 'curriculum',
    title: '🔗 บทที่ 3: Linked Lists',
    description: 'Singly Linked List, Doubly Linked List, Circular Linked List & Pointer Operations',
    files: [
      '03.1 - Linked Lists (Singly, Doubly, Circular).md'
    ]
  },
  {
    id: 'ch4',
    type: 'curriculum',
    title: '🥞 บทที่ 4: Stacks & Queues',
    description: 'Stack (LIFO, Infix/Postfix) และ Queue (FIFO, Circular Array Queue)',
    files: [
      '04.1 - Stacks & Applications (Infix, Postfix, Parentheses).md',
      '04.2 - Queues & Circular Array Queues.md'
    ]
  },
  {
    id: 'ch5',
    type: 'curriculum',
    title: '🌲 บทที่ 5: Trees & Binary Search Trees',
    description: 'นิยามต้นไม้, Tree Traversals, BST Search/Insert และการลบโหนด 3 กรณี',
    files: [
      '05.1 - Tree Terminology & Binary Trees.md',
      '05.2 - Binary Search Trees (BST) & Insertion.md',
      '05.3 - Binary Search Tree Removal (Node Deletion Cases).md'
    ]
  },
  {
    id: 'ch6',
    type: 'curriculum',
    title: '🏷️ บทที่ 6: Hashing & Hash Tables',
    description: 'Hash Tables, Collision Handling (Linear, Quadratic, Chaining) & Rehashing',
    files: [
      '06.1 - Hash Tables & Collision Resolution Strategies.md'
    ]
  },
  {
    id: 'ch7',
    type: 'curriculum',
    title: '⚡ บทที่ 7: Priority Queue & Binary Heap',
    description: 'Priority Queue ADT, Complete Binary Tree Array Indexing, Percolate Up/Down',
    files: [
      '07.1 - Priority Queue & Binary Heaps (Min-Heap, Max-Heap).md'
    ]
  },
  {
    id: 'ch8',
    type: 'curriculum',
    title: '🔀 บทที่ 8: Sorting Algorithms',
    description: 'Bubble, Selection, Insertion, Merge, Quick Sort & ตารางเปรียบเทียบ',
    files: [
      '08.1 - Sorting Algorithms (Bubble, Selection, Insertion, Merge, Quick).md'
    ]
  },
  {
    id: 'ch9',
    type: 'curriculum',
    title: '🌐 บทที่ 9: Graph Traversals & Algorithms',
    description: 'โครงสร้างกราฟ, Adjacency Matrix vs List, BFS, DFS & Topological Sort',
    files: [
      '09.1 - Graph Fundamentals & Traversals (BFS, DFS, Topological Sort).md'
    ]
  },
  {
    id: 'ch10',
    type: 'curriculum',
    title: '🚀 บทที่ 10: Shortest Path Algorithms',
    description: 'Unweighted Shortest Path (BFS) และ Dijkstra Algorithm พร้อมตาราง Trace',
    files: [
      '10.1 - Shortest Path Algorithms (Dijkstra, Unweighted Shortest Path).md'
    ]
  }
];

// Exam preparation & Mock exam zone (Cleanly isolated)
const EXAM_CATEGORIES = [
  {
    id: 'exam-final',
    type: 'exam',
    title: '🏁 ข้อสอบปลายภาค & กับดักอาจารย์ (Final Exam 2568)',
    description: 'ข้อสอบปลายภาคฉบับจริง: Hashing, Binary Heap, Sorting, Graphs, Dijkstra และ 5 กับดักห้องเรียนที่อาจารย์เน้นย้ำ',
    files: [
      '11.7 - รวมข้อสอบจริงที่อาจารย์พูดในห้องเรียน (All Classroom Leaked Exam Problems & Solutions).md',
      '11.6 - Final Exam Real Classroom Prep & Solutions.md'
    ]
  },
  {
    id: 'exam-mock',
    type: 'exam',
    title: '🎯 ข้อสอบจำลองกลางภาค & ตะลุยโจทย์ (Midterm Mock)',
    description: 'แนวข้อสอบเสมือนจริง Midterm, ข้อสอบเก็งปี 2026 และคลังข้อสอบ 20 ข้อ',
    files: [
      '11.1 - Midterm Real Exam Mock & Solutions.md',
      '11.2 - Predicted Midterm Exam 2026 Comprehensive.md',
      '11.5 - Comprehensive Exam Questions, Tracing & Python Solutions.md'
    ]
  },
  {
    id: 'exam-drill',
    type: 'exam',
    title: '🥞 โจทย์เจาะลึกเฉพาะเรื่อง (Topic Drills)',
    description: 'ข้อสอบเฉพาะทางเรื่อง Stack, วงเล็บ, Infix/Postfix และ Circular Queue',
    files: [
      '11.3 - Stack Practice Exam Problems & Solutions.md',
      '11.4 - Queue Practice Exam Problems & Solutions.md'
    ]
  },
  {
    id: 'exam-reference',
    type: 'exam',
    title: '📖 สารบัญและสรุปสูตร (Reference & Cheat Sheet)',
    description: 'ตารางสรุป Time & Space Complexity ทุกบท และแผนผัง Mindmap',
    files: [
      'Glossary & Complexity Cheat Sheet.md',
      'Index.md'
    ]
  }
];

// Course Assignments & Teacher Tasks (ข้อกำหนดอาจารย์, โค้ดส่งจริง, และข้อควรระวัง)
const ASSIGNMENT_CATEGORIES = [
  {
    id: 'assign-course',
    type: 'assignment',
    title: '📋 งานและการบ้านที่อาจารย์สั่ง (Course Assignments & Labs)',
    description: 'รวมข้อกำหนดโจทย์อาจารย์ประดิษฐ์ พิทักษ์เสถียรกุล, ขั้นตอนวิธีทำ, เฉลยโค้ด Python, และกับดักคะแนน 0',
    files: [
      '12.1 - Assignment 1 Singly Linked List Student ID & Node Swap.md',
      '12.2 - Assignment 2 Construct Binary Tree from Post-order & In-order.md',
      '12.3 - Assignment 3 Binary Min-Heap In-class Insertion & DeleteMin.md',
      '12.4 - Assignment 4 Graph Topological Sort & Unweighted Shortest Path.md',
      '12.5 - Test Program 1 & 2 Queue Implementation & Sorting Trace.md',
      '12.6 - 0Exercises Warm-up Function Tracing & Attendance Tasks.md',
      '12.7 - In-Class Assignment Binary Heap DeleteMin & Hashing Trace.md'
    ]
  }
];

// Classroom Live Lecture Transcripts & Visual Slides (ถอดความเสียงสอนสด & สไลด์กระดาน 125 รูป)
const CLASSROOM_TRANSCRIPT_CATEGORIES = [
  {
    id: 'classroom-transcripts',
    type: 'classroom',
    title: '🎙️ บันทึกการสอนและถอดความเสียงสด (Classroom Transcripts & Slides)',
    description: 'ถอดความเสียงคำต่อคำของ ดร.ประดิษฐ์ พิทักษ์เสถียรกุล พร้อมภาพสไลด์และกระดานดำ 125 ภาพ เจาะลึก Hashing, Heap และข้อสอบปลายภาค',
    files: [
      '14.1 - Classroom Lecture Hashing, Open Addressing & Rehashing.md',
      '14.2 - Classroom Lecture Priority Queue & Binary Heap Properties.md',
      '14.3 - Classroom Lecture Exam Focus Node Calculation & 1D Array.md',
      '14.4 - Classroom Lecture Binary Heap Python Implementation & Final Exam Trace.md',
      '14.5 - Master Catalog Classroom Slides & Photos (87 Photos).md'
    ]
  }
];

// Classroom For Example Tracing (เอกสาร For Example PDFs ทุกบทเรียนของอาจารย์)
const CLASSROOM_EXAMPLE_CATEGORIES = [
  {
    id: 'classroom-examples',
    type: 'example',
    title: '💡 ตัวอย่างโจทย์ในห้องเรียน (For Example Tracing ทุกบท)',
    description: 'ถอดรหัสเฉลยและ Tracing จากเอกสาร For Example PDFs ทุกบทเรียนของอาจารย์ประดิษฐ์ พร้อมจุดผิดที่ได้ 0 คะแนน',
    files: [
      '13.1 - For Example Lecture 3 Linked List (โจทย์สร้างโหนด สลับพอยน์เตอร์ และกับดัก add).md',
      '13.2 - For Example Lecture 4 Stack & Postfix (Trace Push-Pop และแปลงนิพจน์ Shunting-Yard).md',
      '13.3 - For Example Lecture 4 Queue (Trace Enqueue-Dequeue และวงรอบ Circular Queue).md',
      '13.4 - For Example Lecture 5 Binary Tree (กฎเหล็กเขียน Path ห้ามใช้ลูกศร และ Reconstruct Tree).md',
      '13.5 - For Example Lecture 5.1 & 5.2 BST (Trace _insert_recursive & _delete_recursive 2 เคส).md',
      '13.6 - For Example Lecture 8.1 Binary Heap (Trace ตัวแปร hole ใน Percolate Up และ Down).md',
      '13.7 - For Example Lecture 9 Sorting (Pass-by-Pass Tracing Bubble, Selection, Insertion).md',
      '13.8 - For Example Lecture 10 & 11 Graph (Topological Sort, BFS Shortest Path & คำนวณขยะ Matrix).md'
    ]
  }
];

function getAllMarkdownFiles(dir) {
  let results = [];
  if (!fs.existsSync(dir)) return results;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getAllMarkdownFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      results.push(fullPath);
    }
  }
  return results;
}

function parseFrontmatter(text) {
  const meta = {};
  let body = text;
  if (text.startsWith('---')) {
    const endIdx = text.indexOf('\n---', 3);
    if (endIdx !== -1) {
      const rawMeta = text.slice(3, endIdx).trim();
      body = text.slice(endIdx + 4).trim();
      const lines = rawMeta.split('\n');
      let currentKey = null;
      lines.forEach(line => {
        const colonIdx = line.indexOf(':');
        if (line.trim().startsWith('- ') && currentKey) {
          if (!Array.isArray(meta[currentKey])) meta[currentKey] = [];
          meta[currentKey].push(line.trim().slice(2).trim());
        } else if (colonIdx !== -1) {
          const key = line.slice(0, colonIdx).trim();
          const val = line.slice(colonIdx + 1).trim();
          currentKey = key;
          meta[key] = val || [];
        }
      });
    }
  }
  return { meta, body };
}

function extractHeadings(markdown) {
  const headings = [];
  const lines = markdown.split('\n');
  lines.forEach(line => {
    const match = line.match(/^(#{1,3})\s+(.+)$/);
    if (match) {
      const level = match[1].length;
      const title = match[2].replace(/\[!.*?\]/g, '').trim();
      const id = title
        .toLowerCase()
        .replace(/[^\w\u0E00-\u0E7F\s-]/g, '')
        .trim()
        .replace(/\s+/g, '-');
      headings.push({ level, title, id });
    }
  });
  return headings;
}

function extractExcerpt(markdown) {
  const lines = markdown.split('\n');
  for (let line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('> [!SUMMARY]') || trimmed.startsWith('> [!INFO]') || trimmed.startsWith('> [!TIP]')) {
      continue;
    }
    if (trimmed.startsWith('>')) {
      const clean = trimmed.replace(/^>\s*/, '').trim();
      if (clean.length > 20) return clean.slice(0, 160) + '...';
    }
    if (trimmed && !trimmed.startsWith('#') && !trimmed.startsWith('---') && !trimmed.startsWith('```')) {
      if (trimmed.length > 20) return trimmed.slice(0, 160) + '...';
    }
  }
  return '';
}

function build() {
  console.log('Scanning DSA-Wiki files...');
  const files = getAllMarkdownFiles(DSA_WIKI_DIR);
  const processedMap = new Map();

  files.forEach(filePath => {
    const filename = path.basename(filePath);
    const relPath = path.relative(DSA_WIKI_DIR, filePath);
    const parentDir = path.dirname(relPath);
    const content = fs.readFileSync(filePath, 'utf8');
    const { meta, body } = parseFrontmatter(content);

    const titleMatch = content.match(/^#\s+(.+)$/m);
    const displayTitle = titleMatch ? titleMatch[1].trim() : filename.replace('.md', '');
    const headings = extractHeadings(content);
    const excerpt = extractExcerpt(body);
    const charCount = content.length;
    const wordCount = content.split(/\s+/).length;
    const estMinutes = Math.max(1, Math.round(charCount / 600));

    const id = filename.replace('.md', '').trim();

    processedMap.set(filename, {
      id,
      filename,
      relPath,
      parentDir,
      title: displayTitle,
      meta,
      excerpt,
      charCount,
      wordCount,
      estMinutes,
      headings,
      content
    });
  });

  function processCategoryList(catList) {
    return catList.map(cat => {
      const docs = cat.files.map(f => {
        const doc = processedMap.get(f);
        if (!doc) {
          console.warn('File not found in processedMap:', f);
          return null;
        }
        return {
          id: doc.id,
          filename: doc.filename,
          title: doc.title,
          parentDir: doc.parentDir,
          excerpt: doc.excerpt,
          charCount: doc.charCount,
          estMinutes: doc.estMinutes,
          headingsCount: doc.headings.length
        };
      }).filter(Boolean);

      return {
        id: cat.id,
        type: cat.type,
        title: cat.title,
        description: cat.description,
        docs
      };
    });
  }

  const curriculumCategories = processCategoryList(CURRICULUM_CATEGORIES);
  const assignmentCategories = processCategoryList(ASSIGNMENT_CATEGORIES);
  const exampleCategories = processCategoryList(CLASSROOM_EXAMPLE_CATEGORIES);
  const examCategories = processCategoryList(EXAM_CATEGORIES);
  const classroomTranscriptCategories = processCategoryList(CLASSROOM_TRANSCRIPT_CATEGORIES);
  const allCategories = [...curriculumCategories, ...assignmentCategories, ...exampleCategories, ...examCategories, ...classroomTranscriptCategories];

  const documents = {};
  processedMap.forEach((val) => {
    documents[val.id] = val;
  });

  const wikiData = {
    generatedAt: new Date().toISOString(),
    initialDocId: '01.1 - Introduction to Data Structures & Algorithm Analysis',
    curriculumCategories,
    assignmentCategories,
    exampleCategories,
    examCategories,
    classroomTranscriptCategories,
    categories: allCategories,
    documents
  };

  const jsContent = `/**
 * Pre-bundled DSA Knowledge Wiki Data
 * Generated: ${new Date().toLocaleString('th-TH')}
 * Total Documents: ${Object.keys(documents).length}
 * 100% Offline Compatible.
 */
window.WIKI_DATA = ${JSON.stringify(wikiData)};
`;

  fs.mkdirSync(path.dirname(OUTPUT_FILE), { recursive: true });
  fs.writeFileSync(OUTPUT_FILE, jsContent, 'utf8');
  console.log(`Successfully compiled ${Object.keys(documents).length} DSA Wiki documents to ${OUTPUT_FILE}`);
  console.log(`Curriculum categories: ${curriculumCategories.length}, Exam categories: ${examCategories.length}`);
}

build();
