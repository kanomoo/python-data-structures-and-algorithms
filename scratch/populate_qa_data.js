// Script to populate rich Q&A data and renderQaPanel calls for all simulators
const fs = require('fs');
const path = require('path');

const targetFile = path.join(__dirname, '..', 'Wiki', 'dsa-interactive-studio.js');
let code = fs.readFileSync(targetFile, 'utf8').replace(/\r\n/g, '\n');

// 1. Assign1PointerSwapSimulator QA
const assign1PresetMarker = "if (preset === 'assign1') {";
const assign1QaP1 = `if (preset === 'assign1') {
        this.qa = {
          question: 'สลับโหนดค่า 1 และโหนดค่า 3 ใน Singly Linked List ที่สร้างจากรหัสนักศึกษา 612037 โดยย้ายเฉพาะ Pointer เท่านั้น (ห้ามแตะ Data) ลิสต์ผลลัพธ์คืออะไร?',
          answer: '<strong>คำสั่งสลับ Pointer:</strong><br><code>prev_x.next = curr_y</code> (โหนด 6 ชี้ไป 3)<br><code>prev_y.next = curr_x</code> (โหนด 0 ชี้ไป 1)<br><code>curr_x.next, curr_y.next = curr_y.next, curr_x.next</code><br><strong>ผลลัพธ์สุดท้าย:</strong> <code>6 -> 3 -> 2 -> 0 -> 1 -> 7</code>',
          danger: '<strong>ข้อควรระวัง:</strong> ห้ามสลับ <code>curr_x.data, curr_y.data = curr_y.data, curr_x.data</code> เด็ดขาด! อาจารย์ให้ 0 คะแนนทันทีเพราะผิดหลักการจัดการ Pointer'
        };`;

const assign1Lec3Marker = "} else if (preset === 'lec3') {";
const assign1QaP2 = `} else if (preset === 'lec3') {
        this.qa = {
          question: 'ใน Lecture 3 จงสลับโหนด 4 และ 2 ในลิสต์ 1 -> 4 -> 3 -> 2 -> 5 เพื่อให้เรียงลำดับอย่างถูกต้อง',
          answer: '<strong>คำสั่งสลับ Pointer:</strong> ปรับ <code>prev_x.next = curr_y</code> (1 ชี้ 2), <code>prev_y.next = curr_x</code> (3 ชี้ 4) และสลับ .next ปลายทาง<br><strong>ผลลัพธ์สุดท้าย:</strong> <code>1 -> 2 -> 3 -> 4 -> 5</code> (Sorted)',
          danger: '<strong>ข้อควรระวัง:</strong> ต้องระบุและจำตัวแปร <code>prev_x</code> และ <code>prev_y</code> ไว้ล่วงหน้าเสมอ มิฉะนั้นจะไม่สามารถต่อสาย Pointer ย้อนกลับได้'
        };`;

const assign1AddTrapMarker = "} else if (preset === 'add_trap') {";
const assign1QaP3 = `} else if (preset === 'add_trap') {
        this.qa = {
          question: 'ถ้าเรียกเมธอด add() ที่เขียนแบบแทรกที่หัว นำเข้าเลข 1, 2, 3, 4, 5 ตามลำดับ ผลลัพธ์ในลิสต์คืออะไร? และทำไมจึงได้ 0 คะแนน?',
          answer: '<strong>ผลลัพธ์ในลิสต์:</strong> <code>5 -> 4 -> 3 -> 2 -> 1</code> (ลำดับกลับทิศทางกลายเป็น Descending Order!)',
          danger: '<strong>กับดักคะแนน 0:</strong> ข้อสอบสั่งให้เก็บ 1 ถึง 5 แบบเรียงลำดับ แต่การแทรกที่ Head เสมอทำให้ข้อมูลที่ใส่ทีหลังกลายเป็นตัวหน้าสุด (พฤติกรรม LIFO เหมือน Stack) ต้องแก้โดยแทรกที่ Tail หรือใช้ <code>append()</code>'
        };`;

code = code.replace(assign1PresetMarker, assign1QaP1);
code = code.replace(assign1Lec3Marker, assign1QaP2);
code = code.replace(assign1AddTrapMarker, assign1QaP3);

// Assign1 renderQaPanel call
const assign1RenderCodeMarker = 'renderCodeDebugger(container, this.codeLines, step.line);';
// We'll replace it in Assign1, Assign2, Assign3, Assign4, TestSuite, BigO

// 2. Assign2TreeReconstructSimulator QA
const assign2PostInMarker = "if (mode === 'post_in') {";
const assign2QaM1 = `if (mode === 'post_in') {
        this.qa = {
          question: 'สร้าง Binary Tree จาก In-order [D, B, E, A, F, C, G] และ Post-order [D, E, B, F, G, C, A] จงระบุ Root, ผล Pre-order Traversal และ Array 1-Based',
          answer: '<strong>Root หลัก:</strong> คือโหนด <code>A</code> (ตัวสุดท้ายของ Post-order)<br><strong>ผล Pre-order Traversal:</strong> <code>A, B, D, E, C, F, G</code><br><strong>ตาราง Array 1-Based:</strong> [1]=A, [2]=B, [3]=C, [4]=D, [5]=E, [6]=F, [7]=G',
          danger: '<strong>ข้อควรระวัง:</strong> ตัวสุดท้ายของ Post-order คือ Root เสมอ จากนั้นนำ Root ไปตัดแบ่ง In-order เป็นฝั่งซ้าย [D, B, E] และฝั่งขวา [F, C, G]'
        };`;

const assign2PreInMarker = "} else if (mode === 'pre_in') {";
const assign2QaM2 = `} else if (mode === 'pre_in') {
        this.qa = {
          question: 'สร้าง Binary Tree จาก Pre-order [A, B, D, E, C, F, G] และ In-order [D, B, E, A, F, C, G]',
          answer: '<strong>Root:</strong> คือโหนด <code>A</code> (ตัวแรกของ Pre-order) มี Subtree ซ้ายคือ B และ Subtree ขวาคือ C',
          danger: '<strong>ข้อควรระวัง:</strong> ใน Pre-order โหนด Root จะอยู่ตัวแรกสุด ต่างจาก Post-order ที่ Root อยู่ตัวสุดท้าย'
        };`;

const assign2StrictPathMarker = "} else if (mode === 'strict_path') {";
const assign2QaM3 = `} else if (mode === 'strict_path') {
        this.qa = {
          question: 'จงเขียนเส้นทาง (Path) จาก Root A ไปยังโหนดใบ E และโหนด Q ตามกฎระเบียบของอาจารย์ประดิษฐ์',
          answer: '<strong>คำตอบที่ถูกต้อง 100%:</strong> <code>A, B, E</code> และ <code>A, E, J, Q</code> (คั่นด้วยเครื่องหมายจุลภาค/ลูกน้ำเท่านั้น)',
          danger: '🚨 <strong>กฎเหล็กของอาจารย์:</strong> ห้ามใส่ลูกศร <code>A -> B -> E</code> หรือ <code>A -> E -> J -> Q</code> เด็ดขาด! อาจารย์ประกาศชัดเจนว่าหากมีลูกศรจะหักคะแนนข้อนั้นทันที 100%!'
        };`;

code = code.replace(assign2PostInMarker, assign2QaM1);
code = code.replace(assign2PreInMarker, assign2QaM2);
code = code.replace(assign2StrictPathMarker, assign2QaM3);

// 3. Assign3HeapSimulator QA
const assign3InsertMarker = "if (preset === 'insert14') {";
const assign3QaP1 = `if (preset === 'insert14') {
        this.qa = {
          question: 'แทรกค่า 14 ลงใน Min-Heap [Sentinel, 13, 21, 16, 24, 31, 19, 68, 65, 26, 32] จงเขียนลำดับการเปลี่ยนแปลงของตัวแปร hole และอาร์เรย์ผลลัพธ์',
          answer: '<strong>ลำดับตัวแปร hole:</strong> <code>hole = 11 → hole = 5 → hole = 2</code> (เลื่อน 3 จังหวะ)<br><strong>ตำแหน่งสุดท้ายของ 14:</strong> อยู่ที่ Index <code>[2]</code><br><strong>อาร์เรย์ผลลัพธ์:</strong> <code>[-, 13, 14, 16, 24, 21, 19, 68, 65, 26, 32, 31]</code>',
          danger: '<strong>ข้อควรระวัง:</strong> สูตรหาโหนดพ่อคือ <code>hole // 2</code> และ Index [0] ต้องคง Sentinel (-∞) ไว้เสมอ'
        };`;

const assign3DeleteMinMarker = "} else if (preset === 'deleteMin') {";
const assign3QaP2 = `} else if (preset === 'deleteMin') {
        this.qa = {
          question: 'ทำคำสั่ง deleteMin() บน Min-Heap จงระบุค่าที่ถูกส่งกลับ (Returned value) และโหนดใดจะขึ้นมาแทนที่ Root',
          answer: '<strong>ค่าที่ถูกส่งกลับ (Min Value):</strong> <code>13</code><br><strong>โหนดที่ขึ้นมาแทนที่ Root:</strong> คือโหนด <code>14</code> (เปรียบเทียบลูกซ้าย 14 กับลูกขวา 16 ดึงตัวเล็กกว่าขึ้นมา)',
          danger: '<strong>ข้อควรระวัง:</strong> การ Percolate Down ต้องเปรียบเทียบลูกทั้งสองข้างเสมอแล้วเลือก <strong>ลูกที่มีค่าน้อยกว่า</strong> ขึ้นมาแทนที่'
        };`;

const assign3Assign15Marker = "} else if (preset === 'assign3_15') {";
const assign3QaP3 = `} else if (preset === 'assign3_15') {
        this.qa = {
          question: 'แทรกข้อมูล 15 ค่าของ Assignment 3 [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2] ค่าต่ำสุดที่อยู่ที่ Root คืออะไร?',
          answer: '<strong>ค่าต่ำสุดที่ Root (Index 1):</strong> คือเลข <code>1</code> เสมอตามนิยาม Min-Heap Order Property',
          danger: '<strong>ข้อสังเกต:</strong> หากสร้างด้วย <code>build_heap()</code> (Percolate Down จาก N//2) จะใช้เวลาเพียง O(N) รวดเร็วกว่าการแทรกทีละตัว O(N log N)'
        };`;

code = code.replace(assign3InsertMarker, assign3QaP1);
code = code.replace(assign3DeleteMinMarker, assign3QaP2);
code = code.replace(assign3Assign15Marker, assign3QaP3);

// 4. Assign4GraphSimulator QA
const assign4BfsMarker = "if (preset === 'bfs') {";
const assign4QaP1 = `if (preset === 'bfs') {
        this.qa = {
          question: 'จากกราฟระบุทิศทาง 7 จุดยอด (V1..V7) จงหา Shortest Path จาก V1 ไปยัง V7 พร้อมระยะทางสั้นสุด และตารางสถานะสุดท้าย',
          answer: '<strong>Shortest Path ไปยัง V7:</strong> <code>V1 -> V4 -> V7</code><br><strong>ระยะทางสั้นสุด (d_v7):</strong> <code>2</code> Edges<br><strong>ตารางสถานะ:</strong> V1(T,0,0), V2(T,1,V1), V3(T,2,V4), V4(T,1,V1), V5(T,2,V2), V6(T,2,V4), V7(T,2,V4)',
          danger: '<strong>ข้อควรระวัง:</strong> ในคอลัมน์ p_v ต้องบันทึกจุดยอดก่อนหน้าที่ทำให้เกิดระยะทางสั้นที่สุดเท่านั้น'
        };`;

const assign4RamMarker = "} else if (preset === 'ram_waste') {";
const assign4QaP2 = `} else if (preset === 'ram_waste') {
        this.qa = {
          question: 'จงแสดงวิธีคำนวณความสูญเปล่าของหน่วยความจำ (Memory Waste) เมื่อเก็บกราฟ 7 จุดยอด 12 เส้นเชื่อมด้วย Adjacency Matrix',
          answer: '<strong>จำนวนช่องทั้งหมด:</strong> 7 x 7 = 49 ช่อง<br><strong>ช่องที่มีเส้นเชื่อมจริง (1):</strong> 12 ช่อง<br><strong>ช่องว่างที่สูญเปล่า (0):</strong> 49 - 12 = 37 ช่อง<br><strong>คิดเป็นความสูญเปล่า:</strong> (37 / 49) x 100% = <strong>75.51%</strong> (≈ 75.69%)',
          danger: '<strong>ข้อสรุปในข้อสอบ:</strong> กราฟที่มีเส้นเชื่อมน้อย (Sparse Graph) ไม่ควรใช้ Adjacency Matrix ให้เปลี่ยนไปใช้ Adjacency List แทน'
        };`;

const assign4TopologicalMarker = "} else if (preset === 'topological') {";
const assign4QaP3 = `} else if (preset === 'topological') {
        this.qa = {
          question: 'จงระบุ In-degree ของจุดยอดทุกตัว และอธิบายหลักการเริ่มต้นทำ Topological Sort',
          answer: '<strong>In-degrees:</strong> V1: 1, V2: 1, V3: 1, V4: 2, V5: 2, V6: 3, V7: 2<br><strong>หลักการ:</strong> นำจุดยอดที่มี In-degree = 0 ใส่ลงใน Queue เพื่อเป็นจุดเริ่มต้นกระบวนการ',
          danger: '<strong>ข้อควรระวัง:</strong> หากกราฟมี Cycle (วงรอบ) จะไม่มีจุดยอดใดที่มี In-degree = 0 และไม่สามารถทำ Topological Sort ได้'
        };`;

code = code.replace(assign4BfsMarker, assign4QaP1);
code = code.replace(assign4RamMarker, assign4QaP2);
code = code.replace(assign4TopologicalMarker, assign4QaP3);

// 5. TestProgramSuiteSimulator QA
const testQueueOverMarker = "if (mode === 'queue_overflow') {";
const testQaP1 = `if (mode === 'queue_overflow') {
        this.qa = {
          question: 'ใน program.py กำหนด Queue(5) แล้วเรียก enqueue() 7 ครั้งติดต่อกัน จะเกิดอะไรขึ้นในครั้งที่ 6?',
          answer: '<strong>ผลลัพธ์:</strong> เกิดข้อผิดพลาด <code>QueueOverflowException: Queue is full!</code> ในการ Enqueue ครั้งที่ 6 เพราะ count == capacity (5 == 5)',
          danger: '<strong>ข้อควรระวัง:</strong> ต้องเขียนดักจับด้วย <code>try ... except QueueOverflowException</code> เพื่อไม่ให้โปรแกรมหยุดทำงาน'
        };`;

const testQueueUnderMarker = "} else if (mode === 'queue_underflow') {";
const testQaP2 = `} else if (mode === 'queue_underflow') {
        this.qa = {
          question: 'ใน program.py กำหนด Queue(6) แล้วเรียก dequeue() 7 ครั้ง จะเกิดอะไรขึ้นในครั้งที่ 7?',
          answer: '<strong>ผลลัพธ์:</strong> เกิดข้อผิดพลาด <code>QueueUnderflowException: Queue is empty!</code> ในการ Dequeue ครั้งที่ 7 เพราะ count == 0',
          danger: '<strong>ข้อควรระวัง:</strong> ก่อนเรียก dequeue() ควรตรวจสอบด้วย <code>is_empty()</code> เสมอ'
        };`;

const testSortMovesMarker = "} else if (mode === 'insertion_moves') {";
const testQaP3 = `} else if (mode === 'insertion_moves') {
        this.qa = {
          question: 'ใน Test Program 2 นำอาร์เรย์ [29, 10, 14, 37, 13] มาเรียงด้วย Insertion Sort จงนับจำนวน Position Moves รวมทั้งหมด และแจกแจงแต่ละ Pass',
          answer: '<strong>ผลรวม Position Moves ทั้งหมด = 9 ครั้ง</strong><br>• Pass 1 (i=1, key=10): เลื่อน 29 (+1), วาง 10 (+1) = <strong>2 Moves</strong><br>• Pass 2 (i=2, key=14): เลื่อน 29 (+1), วาง 14 (+1) = <strong>2 Moves</strong><br>• Pass 3 (i=3, key=37): ไม่เลื่อน (+0), วาง 37 (+1) = <strong>1 Move</strong><br>• Pass 4 (i=4, key=13): เลื่อน 37, 29, 14 (+3), วาง 13 (+1) = <strong>4 Moves</strong><br><strong>รวม:</strong> 2 + 2 + 1 + 4 = <strong>9 Moves</strong>',
          danger: '⚠️ <strong>เกณฑ์ตรวจของอาจารย์ประดิษฐ์:</strong> ให้นับทั้งการเลื่อนสมาชิกไปทางขวา (Shift) และนับจังหวะนำ key วางลงในช่องว่างด้วย! จึงได้ 9 Moves ตรงตามเฉลย'
        };`;

const testModuloMarker = "} else if (mode === 'circular_modulo') {";
const testQaP4 = `} else if (mode === 'circular_modulo') {
        this.qa = {
          question: 'จงเขียนสูตรการเลื่อน Front และ Rear ใน Circular Queue แบบไม่ล้น Buffer',
          answer: '<strong>สูตรเลื่อน Rear:</strong> <code>rear = (rear + 1) % capacity</code><br><strong>สูตรเลื่อน Front:</strong> <code>front = (front + 1) % capacity</code>',
          danger: '<strong>ข้อควรระวัง:</strong> ห้ามใช้ <code>rear += 1</code> เดี่ยวๆ เพราะเมื่อถึงช่องสุดท้ายจะเกิด <code>IndexError</code>'
        };`;

code = code.replace(testQueueOverMarker, testQaP1);
code = code.replace(testQueueUnderMarker, testQaP2);
code = code.replace(testSortMovesMarker, testQaP3);
code = code.replace(testModuloMarker, testQaP4);

// 6. BigOExercisesSimulator QA
const bigOBugMarker = "if (mode === 'indent_bug_inside') {";
const bigOQaP1 = `if (mode === 'indent_bug_inside') {
        this.qa = {
          question: 'ในฟังก์ชัน function(n) ถ้าคำสั่ง print("*") เยื้องอยู่ในลูป j จะพิมพ์ดาวกี่ดวงเมื่อ n=5? ความซับซ้อน Big-O คือเท่าใด?',
          answer: '<strong>จำนวนดาวที่พิมพ์:</strong> <strong>25 ดวง</strong> (5 x 5 = 25)<br><strong>ความซับซ้อน Time Complexity:</strong> <code>O(N²)</code>',
          danger: '<strong>กับดักคะแนน 0:</strong> เกิดจากการกด Tab เกิน 1 ครั้ง ทำให้คำสั่งถูกดึงเข้าไปในลูปด้านในโดยไม่รู้ตัว'
        };`;

const bigOFixedMarker = "} else if (mode === 'indent_fixed_outside') {";
const bigOQaP2 = `} else if (mode === 'indent_fixed_outside') {
        this.qa = {
          question: 'หากแก้ Indentation ให้คำสั่ง print("*") ถอยออกมาอยู่นอกลูป j จะพิมพ์ดาวกี่ดวงเมื่อ n=5? ความซับซ้อน Big-O คือเท่าใด?',
          answer: '<strong>จำนวนดาวที่พิมพ์:</strong> <strong>5 ดวง</strong> เท่านั้น (พิมพ์เพียงรอบละ 1 ดวงตอนจบลูป j แต่ละแถว)<br><strong>ความซับซ้อน Time Complexity:</strong> <code>O(N)</code>',
          danger: '<strong>ข้อสังเกต:</strong> การเปลี่ยน Indentation เพียง 4 เคาะ สามารถเปลี่ยนความเร็วของโปรแกรมจาก O(N²) เป็น O(N) ได้ทันที'
        };`;

const bigOMatrixMarker = "} else if (mode === 'nested_matrix') {";
const bigOQaP3 = `} else if (mode === 'nested_matrix') {
        this.qa = {
          question: 'Nested Loop สามเหลี่ยม j = range(i, n) มีจำนวนรอบการทำงานทั้งหมดกี่รอบ?',
          answer: '<strong>สูตรจำนวนรอบ:</strong> N(N+1)/2 = 5(6)/2 = <strong>15 รอบ</strong> (5 + 4 + 3 + 2 + 1)<br><strong>ความซับซ้อน:</strong> ยังคงเป็น <code>O(N²)</code>',
          danger: '<strong>ข้อควรจำ:</strong> แม้จำนวนรอบจะลดลงครึ่งหนึ่ง แต่ในทาง Big-O ค่าสัมประสิทธิ์ 1/2 จะถูกตัดทิ้ง คงเหลือ O(N²)'
        };`;

code = code.replace(bigOBugMarker, bigOQaP1);
code = code.replace(bigOFixedMarker, bigOQaP2);
code = code.replace(bigOMatrixMarker, bigOQaP3);

// 7. Inject renderQaPanel(container, this.qa); into each simulator's render method
code = code.replace(
  /renderCodeDebugger\(container, this\.codeLines, step\.line\);/g,
  'renderCodeDebugger(container, this.codeLines, step.line);\n      renderQaPanel(container, this.qa);'
);

fs.writeFileSync(targetFile, code, 'utf8');
console.log('Successfully populated rich Q&A data for all simulators!');
