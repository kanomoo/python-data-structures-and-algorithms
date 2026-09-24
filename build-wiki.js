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

// Core unified curriculum categories (Lectures 1 to 11 - Grouping Theory, Assignments, Examples, Transcripts & Exam Drills by Lecture)
const CURRICULUM_CATEGORIES = [
  {
    id: 'ch1',
    type: 'curriculum',
    title: '🏛️ บทที่ 1 (Lecture 1): Introduction & Algorithm Analysis',
    description: 'ความหมาย Data Structure, ADT และการวิเคราะห์ขั้นตอนวิธี Big-O',
    files: [
      '01.1 - Introduction to Data Structures & Algorithm Analysis.md',
      '12.6 - 0Exercises Warm-up Function Tracing & Attendance Tasks.md'
    ],
    pdfs: [
      { name: 'Lecture 1 Introduction.pdf', title: 'สไลด์หลัก: Lecture 1 Introduction (Data Structures & Big-O)', kind: 'slide', path: 'Lectures/Lecture 1 Introduction/Lecture 1 Introduction.pdf' },
      { name: 'DATA STRUCTURES & ALGORITHMS_Lecture 1 Edit168.pdf', title: 'สไลด์ปรับปรุง Edit168: Lecture 1', kind: 'slide', path: 'Lectures/Lecture 1 Introduction/DATA STRUCTURES & ALGORITHMS_Lecture 1 Edit168.pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 1 Edit168.pdf', title: 'สไลด์หลักสูตรใหม่: Lecture 1', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 1 Edit168.pdf' }
    ]
  },
  {
    id: 'ch2',
    type: 'curriculum',
    title: '🐍 บทที่ 2 (Lecture 2): Review Python & OOP',
    description: 'ทบทวนภาษา Python, คลาส, วัตถุ และหลักการ OOP 4 เสาหลัก',
    files: [
      '02.1 - Python Review & Object-Oriented Programming (OOP).md'
    ],
    pdfs: [
      { name: 'Lecture 2 Review Python.pdf', title: 'สไลด์หลัก: Lecture 2 Review Python & OOP', kind: 'slide', path: 'Lectures/Lecture 2 Review Python/Lecture 2 Review Python.pdf' },
      { name: 'DATA STRUCTURES & ALGORITHMS_Lecture 2 Edit168.pdf', title: 'สไลด์ปรับปรุง Edit168: Lecture 2', kind: 'slide', path: 'Lectures/Lecture 2 Review Python/DATA STRUCTURES & ALGORITHMS_Lecture 2 Edit168.pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 2 Edit168.pdf', title: 'สไลด์หลักสูตรใหม่: Lecture 2', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 2 Edit168.pdf' },
      { name: 'Python_Oop.pdf', title: 'เอกสารสรุปทบทวน: Python OOP ฉบับสมบูรณ์', kind: 'slide', path: 'Lectures/Python_Oop.pdf' }
    ]
  },
  {
    id: 'ch3',
    type: 'curriculum',
    title: '🔗 บทที่ 3 (Lecture 3): Linked Lists',
    description: 'Singly, Doubly, Circular Linked Lists, การบ้านสลับพอยน์เตอร์ และตัวอย่างกับดัก add',
    files: [
      '03.1 - Linked Lists (Singly, Doubly, Circular).md',
      '12.1 - Assignment 1 Singly Linked List Student ID & Node Swap.md',
      '13.1 - For Example Lecture 3 Linked List (โจทย์สร้างโหนด สลับพอยน์เตอร์ และกับดัก add).md'
    ],
    pdfs: [
      { name: 'Lecture 3 Linked List.pdf', title: 'สไลด์หลัก: Lecture 3 Linked List', kind: 'slide', path: 'Lectures/Lecture 3 Linked List/Lecture 3 Linked List.pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 3.pdf', title: 'สไลด์หลักสูตร 168: Lecture 3', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 3.pdf' },
      { name: 'For example.pdf', title: 'ใบงานโจทย์: For Example Linked List (สร้างโหนด & สลับ)', kind: 'worksheet', path: 'Lectures/Lecture 3 Linked List/For example.pdf' },
      { name: 'For example_solved.pdf', title: 'เฉลยอาจารย์: For Example Linked List', kind: 'solved', path: 'Lectures/Lecture 3 Linked List/For example_solved.pdf' },
      { name: 'For example Linked List 169.pdf', title: 'ใบงานโจทย์: For Example Linked List 169', kind: 'worksheet', path: 'New-Lectures/For example Linked List 169.pdf' },
      { name: 'For example Linked List 169_solved.pdf', title: 'เฉลยอาจารย์: For Example Linked List 169', kind: 'solved', path: 'New-Lectures/For example Linked List 169_solved.pdf' },
      { name: 'Assign 1 Linked List.pdf', title: 'โจทย์การบ้าน 1: Singly Linked List เรียงรหัสนักศึกษา', kind: 'assignment', path: 'New-Lectures/Assign 1 Linked List.pdf' },
      { name: 'Assign 1 Linked List_solved.pdf', title: 'เฉลยการบ้าน 1: Singly Linked List', kind: 'solved', path: 'New-Lectures/Assign 1 Linked List_solved.pdf' },
      { name: 'Test Program 1 Linked List.pdf', title: 'โจทย์แบบฝึกแล็บ: Test Program 1 Linked List', kind: 'assignment', path: 'New-Lectures/Test Program 1 Linked List.pdf' },
      { name: 'Test Program 1 Linked List_solved.pdf', title: 'เฉลยแบบฝึกแล็บ: Test Program 1 Linked List', kind: 'solved', path: 'New-Lectures/Test Program 1 Linked List_solved.pdf' }
    ]
  },
  {
    id: 'ch4',
    type: 'curriculum',
    title: '🥞 บทที่ 4 (Lecture 4): Stacks & Queues',
    description: 'Stack (LIFO, Infix/Postfix) และ Queue (FIFO, Circular Queue) พร้อมการบ้านและคลังข้อสอบ',
    files: [
      '04.1 - Stacks & Applications (Infix, Postfix, Parentheses).md',
      '04.2 - Queues & Circular Array Queues.md',
      '12.5 - Test Program 1 & 2 Queue Implementation & Sorting Trace.md',
      '13.2 - For Example Lecture 4 Stack & Postfix (Trace Push-Pop และแปลงนิพจน์ Shunting-Yard).md',
      '13.3 - For Example Lecture 4 Queue (Trace Enqueue-Dequeue และวงรอบ Circular Queue).md',
      '11.3 - Stack Practice Exam Problems & Solutions.md',
      '11.4 - Queue Practice Exam Problems & Solutions.md'
    ],
    pdfs: [
      { name: 'Lecture 4 Stack.pdf', title: 'สไลด์หลัก: Lecture 4 Stack ADT', kind: 'slide', path: 'Lectures/Lecture 4 Stack/Lecture 4 Stack.pdf' },
      { name: 'Lecture 04.1.pdf', title: 'สไลด์หลัก: Lecture 04.1 Queue & Circular Queue', kind: 'slide', path: 'Lectures/Lecture 4 Stack/Lecture 04.1.pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 4 Edit168.pdf', title: 'สไลด์ปรับปรุง Edit168: Lecture 4 Stack', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 4 Edit168.pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 4.1.pdf', title: 'สไลด์ปรับปรุง Edit168: Lecture 4.1 Queue', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 4.1.pdf' },
      { name: 'For example Stack.pdf', title: 'ใบงานโจทย์: For Example Stack (Push/Pop Tracing)', kind: 'worksheet', path: 'Lectures/Lecture 4 Stack/For example Stack.pdf' },
      { name: 'For example Stack_solved.pdf', title: 'เฉลยอาจารย์: For Example Stack', kind: 'solved', path: 'Lectures/Lecture 4 Stack/For example Stack_solved.pdf' },
      { name: 'For example Queue.pdf', title: 'ใบงานโจทย์: For Example Queue (Circular Queue)', kind: 'worksheet', path: 'Lectures/Lecture 4 Stack/For example Queue.pdf' },
      { name: 'For example Queue_solved.pdf', title: 'เฉลยอาจารย์: For Example Queue', kind: 'solved', path: 'Lectures/Lecture 4 Stack/For example Queue_solved.pdf' },
      { name: 'Postfix Expression.pdf', title: 'ใบงานโจทย์: Postfix Expression & Shunting-Yard', kind: 'worksheet', path: 'Lectures/Lecture 4 Stack/Postfix Expression.pdf' },
      { name: 'Postfix Expression_solved.pdf', title: 'เฉลยอาจารย์: Postfix Expression', kind: 'solved', path: 'Lectures/Lecture 4 Stack/Postfix Expression_solved.pdf' },
      { name: 'แปลเอกสารบทท 3.6 The Stack ADT.pdf', title: 'เอกสารแปลตำรา: Mark Allen Weiss 3.6 The Stack ADT', kind: 'slide', path: 'Lectures/Lecture 4 Stack/แปลเอกสารบทท 3.6 The Stack ADT.pdf' }
    ]
  },
  {
    id: 'ch5',
    type: 'curriculum',
    title: '🌲 บทที่ 5 (Lecture 5): Trees & Tree Traversals',
    description: 'นิยามต้นไม้, Complete Binary Tree, การสร้าง Tree จาก Post/In-order และกฎห้ามใส่ลูกศร',
    files: [
      '05.1 - Tree Terminology & Binary Trees.md',
      '12.2 - Assignment 2 Construct Binary Tree from Post-order & In-order.md',
      '13.4 - For Example Lecture 5 Binary Tree (กฎเหล็กเขียน Path ห้ามใช้ลูกศร และ Reconstruct Tree).md'
    ],
    pdfs: [
      { name: 'Lecture 5 Tree.pdf', title: 'สไลด์หลัก: Lecture 5 Trees & Binary Trees', kind: 'slide', path: 'Lectures/Lecture 5 Tree/Lecture 5 Tree.pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 5 Edit168.pdf', title: 'สไลด์ปรับปรุง Edit168: Lecture 5 Trees', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 5 Edit168.pdf' },
      { name: 'For example Binary Tree.pdf', title: 'ใบงานโจทย์: For Example Binary Tree (กฎห้ามใส่ลูกศร)', kind: 'worksheet', path: 'Lectures/Lecture 5 Tree/For example Binary Tree.pdf' },
      { name: 'For example Binary Tree_solved.pdf', title: 'เฉลยอาจารย์: For Example Binary Tree', kind: 'solved', path: 'Lectures/Lecture 5 Tree/For example Binary Tree_solved.pdf' },
      { name: 'Assign 2 Binary Tree.pdf', title: 'โจทย์การบ้าน 2: สร้างทรีจาก Post & In-order', kind: 'assignment', path: 'Lectures/Assignment 2 Construct Binary Tree/Assign 2 Binary Tree.pdf' },
      { name: 'Assign 2 Binary Tree_solved.pdf', title: 'เฉลยการบ้าน 2: สร้างทรีจาก Post & In-order', kind: 'solved', path: 'Lectures/Assignment 2 Construct Binary Tree/Assign 2 Binary Tree_solved.pdf' }
    ]
  },
  {
    id: 'ch6',
    type: 'curriculum',
    title: '🌿 บทที่ 6 (Lecture 5.1 & 5.2): Binary Search Tree (BST) & Deletion',
    description: 'Binary Search Tree Property, Insertion, Search และการลบโหนด 3 กรณีพร้อม Trace ละเอียด',
    files: [
      '05.2 - Binary Search Trees (BST) & Insertion.md',
      '05.3 - Binary Search Tree Removal (Node Deletion Cases).md',
      '13.5 - For Example Lecture 5.1 & 5.2 BST (Trace _insert_recursive & _delete_recursive 2 เคส).md'
    ],
    pdfs: [
      { name: 'Lecture 5.1add in method delete.pdf', title: 'สไลด์หลัก: Lecture 5.1 BST Insertion & Deletion', kind: 'slide', path: 'Lectures/Lecture 5.1 Binary Search Tree/Lecture 5.1add in method delete.pdf' },
      { name: 'Lecture 5.2 Binary Search Tree (Remove node which has 2 children).pdf', title: 'สไลด์หลัก: Lecture 5.2 BST Deletion (2 Children)', kind: 'slide', path: 'Lectures/Lecture 5.2 Binary Search Tree Remove/Lecture 5.2 Binary Search Tree (Remove node which has 2 children).pdf' },
      { name: 'DATA STRUCTURES - ALGORITHMS_Lecture 5.1.pdf', title: 'สไลด์ปรับปรุง: Lecture 5.1 BST', kind: 'slide', path: 'New-Lectures/DATA STRUCTURES - ALGORITHMS_Lecture 5.1.pdf' },
      { name: 'removebst.pdf', title: 'เอกสารสรุป: Remove BST สรุปขั้นตอน 3 กรณี', kind: 'slide', path: 'Lectures/Lecture 5.1 Binary Search Tree/removebst.pdf' },
      { name: 'For example Binary Search Tree std delete round 4 in insert_s step.pdf', title: 'ใบงานโจทย์: BST Delete Round 4', kind: 'worksheet', path: 'Lectures/Lecture 5.1 Binary Search Tree/For example Binary Search Tree std delete round 4 in insert_s step.pdf' },
      { name: 'For example Binary Search Tree std delete round 4 in insert_s step_solved.pdf', title: 'เฉลยอาจารย์: BST Delete Round 4', kind: 'solved', path: 'Lectures/Lecture 5.1 Binary Search Tree/For example Binary Search Tree std delete round 4 in insert_s step_solved.pdf' },
      { name: 'Example for Binary Search Tree remove 2 std.pdf', title: 'ใบงานโจทย์: BST Remove 2 Children', kind: 'worksheet', path: 'Lectures/Lecture 5.2 Binary Search Tree Remove/Example for Binary Search Tree remove 2 std.pdf' },
      { name: 'Example for Binary Search Tree remove 2 std_solved.pdf', title: 'เฉลยอาจารย์: BST Remove 2 Children', kind: 'solved', path: 'Lectures/Lecture 5.2 Binary Search Tree Remove/Example for Binary Search Tree remove 2 std_solved.pdf' }
    ]
  },
  {
    id: 'ch7',
    type: 'curriculum',
    title: '🏷️ บทที่ 7 (Lecture 7): Hashing & Collision Strategies',
    description: 'Hash Tables, Separate Chaining, Open Addressing, Rehashing และงานส่งในห้องชน 7 ครั้ง',
    files: [
      '06.1 - Hash Tables & Collision Resolution Strategies.md',
      '12.7 - In-Class Assignment Binary Heap DeleteMin & Hashing Trace.md',
      '14.1 - Classroom Lecture Hashing, Open Addressing & Rehashing.md'
    ],
    pdfs: [
      { name: 'Lecture 7 Hashing.pdf', title: 'สไลด์หลัก: Lecture 7 Hash Tables & Collision Resolution', kind: 'slide', path: 'Lectures/Lecture 7 Hashing/Lecture 7 Hashing.pdf' }
    ]
  },
  {
    id: 'ch8',
    type: 'curriculum',
    title: '⚡ บทที่ 8 (Lecture 8 & 8.1): Priority Queue & Binary Heap',
    description: 'Priority Queue ADT, Complete Binary Tree Array, การบ้านแทรก 15 ค่า, เสียงสอนสด และเฉลยข้อสอบ DeleteMin 3 ครั้ง',
    files: [
      '07.1 - Priority Queue & Binary Heaps (Min-Heap, Max-Heap).md',
      '12.3 - Assignment 3 Binary Min-Heap In-class Insertion & DeleteMin.md',
      '13.6 - For Example Lecture 8.1 Binary Heap (Trace ตัวแปร hole ใน Percolate Up และ Down).md',
      '14.2 - Classroom Lecture Priority Queue & Binary Heap Properties.md',
      '14.3 - Classroom Lecture Exam Focus Node Calculation & 1D Array.md',
      '14.4 - Classroom Lecture Binary Heap Python Implementation & Final Exam Trace.md'
    ],
    pdfs: [
      { name: 'Lecture 8 Priority Queue (Heap).pdf', title: 'สไลด์หลัก: Lecture 8 Priority Queue & Binary Heap', kind: 'slide', path: 'Lectures/Lecture 8 Priority Queue (Heap)/Lecture 8 Priority Queue (Heap).pdf' },
      { name: 'Lecture 8.1 Priority Queue (Insert and deleteMin).pdf', title: 'สไลด์หลัก: Lecture 8.1 Binary Heap (Insert & DeleteMin)', kind: 'slide', path: 'Lectures/Lecture 8.1 Priority Queue (Insert and deleteMin)/Lecture 8.1 Priority Queue (Insert and deleteMin).pdf' },
      { name: 'For example Binary Heap.pdf', title: 'ใบงานโจทย์: For Example Binary Heap (Percolate Up/Down)', kind: 'worksheet', path: 'Lectures/Lecture 8.1 Priority Queue (Insert and deleteMin)/For example Binary Heap.pdf' },
      { name: 'For example Binary Heap_solved.pdf', title: 'เฉลยอาจารย์: For Example Binary Heap', kind: 'solved', path: 'Lectures/Lecture 8.1 Priority Queue (Insert and deleteMin)/For example Binary Heap_solved.pdf' },
      { name: 'Assignment 3 Inclass.pdf', title: 'โจทย์การบ้าน 3: Binary Min-Heap In-class แทรก 15 ค่า', kind: 'assignment', path: 'Lectures/Assignment 3 Binary Heap/Assignment 3 Inclass.pdf' },
      { name: 'Assignment 3 Inclass_solved.pdf', title: 'เฉลยการบ้าน 3: Binary Min-Heap In-class', kind: 'solved', path: 'Lectures/Assignment 3 Binary Heap/Assignment 3 Inclass_solved.pdf' }
    ]
  },
  {
    id: 'ch9',
    type: 'curriculum',
    title: '🔀 บทที่ 9 (Lecture 9): Sorting Algorithms',
    description: 'Bubble, Selection, Insertion, Pass-by-Pass Traces, Inversions และการบ้าน Take-Home 2',
    files: [
      '08.1 - Sorting Algorithms (Bubble, Selection, Insertion, Merge, Quick).md',
      '12.8 - In-Class Assignment Bubble Sort Trace & Total Swaps Calculation.md',
      '13.7 - For Example Lecture 9 Sorting (Pass-by-Pass Tracing Bubble, Selection, Insertion).md',
      '14.6 - Classroom Lecture Sorting (Insertion, Selection, Bubble Sort) & Exam Inversions.md'
    ],
    pdfs: [
      { name: 'Lecture 9 Sorting.pdf', title: 'สไลด์หลัก: Lecture 9 Sorting Algorithms', kind: 'slide', path: 'Lectures/Lecture 9 Sorting/Lecture 9 Sorting.pdf' },
      { name: 'Lecture 9.1.pdf', title: 'สไลด์เสริม: Lecture 9.1 Sorting', kind: 'slide', path: 'Lectures/Lecture 9 Sorting/Lecture 9.1.pdf' },
      { name: 'DATA STRUCTURES & ALGORITHMS_Lecture 9 168.pdf', title: 'สไลด์ปรับปรุง Edit168: Lecture 9 Sorting', kind: 'slide', path: 'Lectures/Lecture 9 Sorting/New/DATA STRUCTURES & ALGORITHMS_Lecture 9 168.pdf' },
      { name: 'For Example Bubble sort.pdf', title: 'ใบงานโจทย์: Bubble Sort Tracing & Swaps', kind: 'worksheet', path: 'Lectures/Lecture 9 Sorting/For Example Bubble sort.pdf' },
      { name: 'For Example Bubble sort_solved.pdf', title: 'เฉลยอาจารย์: Bubble Sort Tracing', kind: 'solved', path: 'Lectures/Lecture 9 Sorting/For Example Bubble sort_solved.pdf' },
      { name: 'For Example Selection sort.pdf', title: 'ใบงานโจทย์: Selection Sort Tracing', kind: 'worksheet', path: 'Lectures/Lecture 9 Sorting/For Example Selection sort.pdf' },
      { name: 'For Example Selection sort_solved.pdf', title: 'เฉลยอาจารย์: Selection Sort Tracing', kind: 'solved', path: 'Lectures/Lecture 9 Sorting/For Example Selection sort_solved.pdf' },
      { name: 'Short note Insertion sort.pdf', title: 'ใบงานสรุป: Insertion Sort Tracing', kind: 'worksheet', path: 'Lectures/Lecture 9 Sorting/Short note Insertion sort.pdf' },
      { name: 'Short note Insertion sort_solved.pdf', title: 'เฉลยอาจารย์: Insertion Sort Tracing', kind: 'solved', path: 'Lectures/Lecture 9 Sorting/Short note Insertion sort_solved.pdf' },
      { name: 'หมายเหตุ ในหัวข้อ insertion sort.pdf', title: 'หมายเหตุอาจารย์: Insertion Sort Analysis', kind: 'slide', path: 'Lectures/Lecture 9 Sorting/หมายเหตุ ในหัวข้อ insertion sort.pdf' }
    ]
  },
  {
    id: 'ch10',
    type: 'curriculum',
    title: '🌐 บทที่ 10 (Lecture 10): Graph & Topological Sort',
    description: 'โครงสร้างกราฟ, Adjacency Matrix vs List, Memory Waste 24.48%, DAG, Kahn\'s TopoSort และข้อสอบไม่ต่ำกว่า 20 คะแนน',
    files: [
      '09.1 - Graph Fundamentals & Traversals (BFS, DFS, Topological Sort).md',
      '12.4 - Assignment 4 Graph Topological Sort & Unweighted Shortest Path.md',
      '13.8 - For Example Lecture 10 & 11 Graph (Topological Sort, BFS Shortest Path & คำนวณขยะ Matrix).md',
      '14.7 - Classroom Lecture Graph Theory, Representations & Final Exam Leaks.md'
    ],
    pdfs: [
      { name: 'Lecture 10 Graph.pdf', title: 'สไลด์หลัก: Lecture 10 Graph Fundamentals & Representations', kind: 'slide', path: 'Lectures/Lecture 10 Graph/Lecture 10 Graph.pdf' },
      { name: 'Topological sort.pdf', title: 'ใบงานโจทย์: Topological Sort (Kahn Algorithm)', kind: 'worksheet', path: 'Lectures/Lecture 10 Graph/Topological sort.pdf' },
      { name: 'Topological sort_solved.pdf', title: 'เฉลยอาจารย์: Topological Sort', kind: 'solved', path: 'Lectures/Lecture 10 Graph/Topological sort_solved.pdf' }
    ]
  },
  {
    id: 'ch11',
    type: 'curriculum',
    title: '🚀 บทที่ 11 (Lecture 11): Shortest Path & Dijkstra Algorithms',
    description: 'Unweighted Shortest Path (BFS), Dijkstra Algorithm บนกราฟมีค่าน้ำหนัก พร้อมตารางสถานะ Known, Dist, Path',
    files: [
      '10.1 - Shortest Path Algorithms (Dijkstra, Unweighted Shortest Path).md'
    ],
    pdfs: [
      { name: 'Lecture 11 Shortest path.pdf', title: 'สไลด์หลัก: Lecture 11 Shortest Path Algorithms & Dijkstra', kind: 'slide', path: 'Lectures/Lecture 11 Shortest path/Lecture 11 Shortest path.pdf' },
      { name: 'For Example Graph.pdf', title: 'ใบงานโจทย์: Unweighted Shortest Path (BFS)', kind: 'worksheet', path: 'Lectures/Lecture 11 Shortest path/For Example Graph.pdf' },
      { name: 'For Example Graph_solved.pdf', title: 'เฉลยอาจารย์: Unweighted Shortest Path & Dijkstra', kind: 'solved', path: 'Lectures/Lecture 11 Shortest path/For Example Graph_solved.pdf' },
      { name: 'Assign 4 Shortest Path.pdf', title: 'โจทย์การบ้าน 4: Graph BFS Shortest Path & TopoSort', kind: 'assignment', path: 'Lectures/Assignment 4 Shortest Path/For Example Graph.pdf' },
      { name: 'Assign 4 Shortest Path_solved.pdf', title: 'เฉลยการบ้าน 4: Graph BFS Shortest Path & TopoSort', kind: 'solved', path: 'Lectures/Assignment 4 Shortest Path/For Example Graph_solved.pdf' }
    ]
  },
  {
    id: 'ch-pdf-master',
    type: 'curriculum',
    title: '📑 คลัง PDF สไลด์ ใบงาน และภาพข้อสอบจริง (Master PDF & Media Catalog)',
    description: 'รวบรวมไฟล์ PDF สไลด์บรรยาย ใบงาน For Example และไฟล์เฉลย _solved.pdf ครบทั้ง 11 บท รวม 91 ไฟล์ และภาพถ่ายข้อสอบจริง 12 หน้า',
    files: [
      '15.1 - คลังไฟล์ PDF สไลด์บรรยาย ใบงาน For Example และไฟล์เฉลยอาจารย์ครบทั้ง 11 บท (Teacher Master PDF & Media Catalog).md',
      '15.2 - ภาพถ่ายข้อสอบกลางภาคฉบับจริงในห้องสอบ 12 หน้า (Midterm Real Exam Paper Photos Gallery).md',
      '14.5 - Master Catalog Classroom Slides & Photos (87 Photos).md'
    ],
    pdfs: [
      { name: 'planstd060243106.pdf', title: 'แผนการสอนรายวิชา & เกณฑ์การให้คะแนน (Course Syllabus)', kind: 'slide', path: 'Lectures/planstd060243106.pdf' },
      { name: 'Data Structures & Algorithms in Python.pdf', title: 'ตำราหลัก: Data Structures & Algorithms in Python (Goodrich / Weiss)', kind: 'slide', path: 'Lectures/Data Structures & Algorithms in Python.pdf' }
    ]
  },
  {
    id: 'ch-exam-master',
    type: 'curriculum',
    title: '🎯 ศูนย์รวมแนวข้อสอบ & สรุปสูตร (Master Exam Hub & Cheat Sheet)',
    description: 'รวมข้อสอบจริงที่อาจารย์พูดในห้องเรียน, แนวข้อสอบปลายภาค 2568, ข้อสอบจำลอง Midterm Real Mock และตาราง Big-O',
    files: [
      '11.7 - รวมข้อสอบจริงที่อาจารย์พูดในห้องเรียน (All Classroom Leaked Exam Problems & Solutions).md',
      '11.6 - Final Exam Real Classroom Prep & Solutions.md',
      '11.1 - Midterm Real Exam Mock & Solutions.md',
      '11.2 - Predicted Midterm Exam 2026 Comprehensive.md',
      '11.5 - Comprehensive Exam Questions, Tracing & Python Solutions.md',
      'Glossary & Complexity Cheat Sheet.md',
      'Index.md'
    ]
  }
];

// Master PDF & Media Archive (สไลด์บรรยาย, ใบงาน For Example, เฉลย _solved.pdf, ภาพกระดาน, ภาพข้อสอบจริง)
const PDF_ARCHIVE_CATEGORIES = [
  {
    id: 'pdf-master',
    type: 'pdf',
    title: '📑 คลังไฟล์ PDF สไลด์ ใบงาน และเฉลยอาจารย์ (Teacher Master PDF & Media Catalog)',
    description: 'รวบรวมไฟล์ PDF สไลด์บรรยาย ใบงาน For Example และไฟล์เฉลย _solved.pdf ของอาจารย์ประดิษฐ์ ครบทั้ง 11 บท รวม 91 ไฟล์',
    files: [
      '15.1 - คลังไฟล์ PDF สไลด์บรรยาย ใบงาน For Example และไฟล์เฉลยอาจารย์ครบทั้ง 11 บท (Teacher Master PDF & Media Catalog).md',
      '15.2 - ภาพถ่ายข้อสอบกลางภาคฉบับจริงในห้องสอบ 12 หน้า (Midterm Real Exam Paper Photos Gallery).md'
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
      '12.7 - In-Class Assignment Binary Heap DeleteMin & Hashing Trace.md',
      '12.8 - In-Class Assignment Bubble Sort Trace & Total Swaps Calculation.md'
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
      '14.5 - Master Catalog Classroom Slides & Photos (87 Photos).md',
      '14.6 - Classroom Lecture Sorting (Insertion, Selection, Bubble Sort) & Exam Inversions.md',
      '14.7 - Classroom Lecture Graph Theory, Representations & Final Exam Leaks.md'
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
        docs,
        pdfs: cat.pdfs || []
      };
    });
  }

  const curriculumCategories = processCategoryList(CURRICULUM_CATEGORIES);
  const assignmentCategories = processCategoryList(ASSIGNMENT_CATEGORIES);
  const exampleCategories = processCategoryList(CLASSROOM_EXAMPLE_CATEGORIES);
  const examCategories = processCategoryList(EXAM_CATEGORIES);
  const classroomTranscriptCategories = processCategoryList(CLASSROOM_TRANSCRIPT_CATEGORIES);
  const pdfArchiveCategories = processCategoryList(PDF_ARCHIVE_CATEGORIES);
  const allCategories = [...curriculumCategories, ...assignmentCategories, ...exampleCategories, ...examCategories, ...classroomTranscriptCategories, ...pdfArchiveCategories];

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
    pdfArchiveCategories,
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
