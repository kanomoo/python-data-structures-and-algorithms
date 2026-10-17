# -*- coding: utf-8 -*-
"""
Script to inject classroom worksheet problems (Images 1-5) into generate_tab1.py and generate_tab3.py:
1. Question 2: Add Sub-question 2.5 (15-key Min-Heap insert & deleteMin from Image 1)
2. Question 6: Add Sub-question 6.3 (Shortest Path with Source Vertex = v3 from Image 3 with queries v3->v5, v3->v7, v4->v5)
3. Question 5: Add worksheet pseudocode and variable trace (Images 2, 4, 5)
4. Tab 3: Add Section 12 (ถอดรหัสใบงานจริง 2569 ทั้ง 5 ใบ)
"""

import os
import re

# =========================================================================
# 1. UPDATE GENERATE_TAB1.PY
# =========================================================================
tab1_path = r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab1.py"
with open(tab1_path, "r", encoding="utf-8") as f:
    t1 = f.read()

# Add Sub-question 2.5 to Question 2 (before <!-- QUESTION 3 -->)
q2_5_html = r"""  <!-- SUB-QUESTION 2.5: 15-KEY MIN-HEAP WORKSHEET -->
  <h3 class="question-title" style="background:#eff6ff; border-left-color:#2563eb; margin-top:25px;">
    <span>2.5 การสร้าง Binary Min-Heap 15 ตัว และการ deleteMin() [ถอดรหัสจากใบงานจริง 2569 ภาพที่ 1]</span>
    <span class="score-badge">Score: 8 Marks (8 คะแนน: 5 + 3)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Insert the following sequence of 15 integers into an initially empty Binary Min-Heap sequentially:</p>
  $$\mathbf{10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2}$$
  <p>Show the step-by-step tree insertion or array state up to 15 elements. Then perform one <code>deleteMin()</code> operation. Write the resulting array and show how the replacement element percolates down.</p>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - จากใบงานจริงในห้องเรียน 2569 ภาพที่ 1):</strong> ให้นักศึกษาทำการ insert ข้อมูลจำนวน 15 ตัว: <strong>10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2</strong> เข้าไปใน Binary Min-Heap ว่าง และกรอกข้อมูลลงใน Array ขนาด 15 ช่อง จากนั้นให้ทำคำสั่ง <code>deleteMin()</code> 1 ครั้ง พร้อมเขียนผลลัพธ์ของ Array หลังการลบ
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#1e3a8a; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 2.5: อาร์เรย์ของ Binary Min-Heap ขนาด 15 ช่อง และหลัง deleteMin()</div>
    <table style="text-align:center; font-size:12px;">
      <thead>
        <tr style="background:#1e3a8a; color:white;">
          <th style="width:110px;">การทำงาน</th>
          <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th>
          <th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="font-weight:bold; background:#f1f5f9;">หลัง Insert 15 ตัว</td>
          <td style="color:#94a3b8;">-</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
        <tr>
          <td style="font-weight:bold; background:#fef2f2; color:#b91c1c;">หลัง deleteMin()</td>
          <td style="color:#94a3b8;">-</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#f1f5f9;">-</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดข้อ 2.5 (15-Key Min-Heap Insertion &amp; deleteMin Solution):</div>
    <p><strong>1. ลำดับการแทรกข้อมูลและ Percolate Up ทีละตัว:</strong></p>
    <ul>
      <li>Insert 10: <code>[-, 10]</code></li>
      <li>Insert 12: <code>[-, 10, 12]</code></li>
      <li>Insert 1: เลื่อน 10 ลงมา &rarr; <code>[-, 1, 12, 10]</code></li>
      <li>Insert 14: <code>[-, 1, 12, 10, 14]</code></li>
      <li>Insert 6: เลื่อน 12 ลงมา &rarr; <code>[-, 1, 6, 10, 14, 12]</code></li>
      <li>Insert 5: เลื่อน 10 ลงมา &rarr; <code>[-, 1, 6, 5, 14, 12, 10]</code></li>
      <li>Insert 8: <code>[-, 1, 6, 5, 14, 12, 10, 8]</code></li>
      <li>Insert 15: <code>[-, 1, 6, 5, 14, 12, 10, 8, 15]</code></li>
      <li>Insert 3: เลื่อน 14 &rarr; 6 ลงมา &rarr; <code>[-, 1, 3, 5, 6, 12, 10, 8, 15, 14]</code></li>
      <li>Insert 9: เลื่อน 12 ลงมา &rarr; <code>[-, 1, 3, 5, 6, 9, 10, 8, 15, 14, 12]</code></li>
      <li>Insert 7: เลื่อน 9 ลงมา &rarr; <code>[-, 1, 3, 5, 6, 7, 10, 8, 15, 14, 12, 9]</code></li>
      <li>Insert 4: เลื่อน 10 &rarr; 5 ลงมา &rarr; <code>[-, 1, 3, 4, 6, 7, 5, 8, 15, 14, 12, 9, 10]</code></li>
      <li>Insert 11: <code>[-, 1, 3, 4, 6, 7, 5, 8, 15, 14, 12, 9, 10, 11]</code></li>
      <li>Insert 13: <code>[-, 1, 3, 4, 6, 7, 5, 8, 15, 14, 12, 9, 10, 11, 13]</code></li>
      <li>Insert 2: อยู่ช่อง 15 &rarr; เทียบ Parent ช่อง 7 (ค่า 8): $2 < 8$ เลื่อน 8 ลงช่อง 15, hole=7 &rarr; เทียบ Parent ช่อง 3 (ค่า 4): $2 < 4$ เลื่อน 4 ลงช่อง 7, hole=3 &rarr; เทียบ Parent ช่อง 1 (ค่า 1): $2 < 1$ (False) จบการ Percolate วาง 2 ที่ช่อง 3!</li>
    </ul>

    <p><strong>ตารางอาร์เรย์หลังแทรกครบ 15 ตัว:</strong></p>
    <table style="text-align:center; font-size:12px;">
      <tr style="background:#1e3a8a; color:white;">
        <th>Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th>
      </tr>
      <tr>
        <td style="font-weight:bold; background:#f1f5f9;">Value</td>
        <td style="color:#94a3b8;">-</td><td><strong>1</strong></td><td><strong>3</strong></td><td><strong>2</strong></td><td><strong>6</strong></td><td><strong>7</strong></td><td><strong>5</strong></td><td><strong>4</strong></td><td><strong>15</strong></td><td><strong>14</strong></td><td><strong>12</strong></td><td><strong>9</strong></td><td><strong>10</strong></td><td><strong>11</strong></td><td><strong>13</strong></td><td><strong>8</strong></td>
      </tr>
    </table>

    <p><strong>2. ขั้นตอนการทำงานของ deleteMin():</strong></p>
    <ul>
      <li>ลบ Root (ค่า 1) ออกจากช่อง 1 &rarr; เกิด <code>hole = 1</code></li>
      <li>นำค่าตัวสุดท้ายท้ายแถวคือ <strong>8</strong> (จากช่อง 15) มาเตรียม Percolate Down</li>
      <li>เทียบลูกของ hole 1: ช่อง 2 (ค่า 3) และช่อง 3 (ค่า 2) &rarr; ลูกที่น้อยกว่าคือ <strong>2 (ช่อง 3)</strong> &rarr; $8 > 2$ ดึง 2 ขึ้นมาที่ช่อง 1, เลื่อน <code>hole = 3</code></li>
      <li>เทียบลูกของ hole 3: ช่อง 6 (ค่า 5) และช่อง 7 (ค่า 4) &rarr; ลูกที่น้อยกว่าคือ <strong>4 (ช่อง 7)</strong> &rarr; $8 > 4$ ดึง 4 ขึ้นมาที่ช่อง 3, เลื่อน <code>hole = 7</code></li>
      <li>เทียบลูกของ hole 7: มีเฉพาะลูกซ้ายช่อง 14 (ค่า 13) &rarr; $8 < 13$ (เงื่อนไขเป็นเท็จ) หยุดการ Percolate Down วาง <strong>8</strong> ลงที่ช่อง 7!</li>
    </ul>

    <p><strong>ตารางอาร์เรย์สุดท้ายหลัง deleteMin():</strong></p>
    <table style="text-align:center; font-size:12px;">
      <tr style="background:#b91c1c; color:white;">
        <th>Index</th><th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th><th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th>
      </tr>
      <tr>
        <td style="font-weight:bold; background:#fef2f2;">Value</td>
        <td style="color:#94a3b8;">-</td><td><strong>2</strong></td><td><strong>3</strong></td><td><strong>4</strong></td><td><strong>6</strong></td><td><strong>7</strong></td><td><strong>5</strong></td><td><strong>8</strong></td><td><strong>15</strong></td><td><strong>14</strong></td><td><strong>12</strong></td><td><strong>9</strong></td><td><strong>10</strong></td><td><strong>11</strong></td><td><strong>13</strong></td><td style="background:#f1f5f9; color:#94a3b8;">-</td>
      </tr>
    </table>
  </div>
"""

if "2.5 การสร้าง Binary Min-Heap 15 ตัว" not in t1:
    idx_q3 = t1.find('<h2 id="q3"')
    t1 = t1[:idx_q3] + q2_5_html + "\n\n  " + t1[idx_q3:]

# Add Sub-question 6.2/6.3 to Question 6 (Worksheet Image 3: Source Vertex = v3)
q6_worksheet_html = r"""  <!-- SUB-QUESTION 6.2: WORKSHEET SOURCE VERTEX V3 -->
  <h3 class="question-title" style="background:#f0fdfa; border-left-color:#0d9488; margin-top:25px;">
    <span>6.2 การประมวลผล Shortest Path โดยมีจุดเริ่มต้นที่ $v_3$ (Source Vertex = 3) [ถอดรหัสจากใบงานจริง 2569 ภาพที่ 3]</span>
    <span class="score-badge" style="background:#ccfbf1; color:#0f766e;">Score: 10 Marks (10 คะแนน)</span>
  </h3>
  <p><strong>Question Statement (EN):</strong> Given the same directed graph $G = (V, E)$ with 7 vertices. Now set the <strong>Source Vertex to $v_3$</strong> (Vertex 3). Execute the Breadth-First Search (BFS) Unweighted Shortest Path algorithm using the pseudo-code:</p>
  <pre><code>if w.dist == INFINITY :
    w.dist = v.dist + 1
    w.path = v
    q.enqueue (w)</code></pre>
  <p>Fill the processing table (Known, Dist, Path) and the Queue states. Then answer the exact questions from the worksheet:</p>
  <ul>
    <li>Write down the length and the shortest path from Vertex 3 to Vertex 5: <code>The length = ? The shortest path = ?</code></li>
    <li>Write down the length and the shortest path from Vertex 3 to Vertex 7: <code>The length = ? The shortest path = ?</code></li>
    <li>Write down the length and the shortest path from Vertex 4 to Vertex 5: <code>The length = ? The shortest path = ?</code></li>
  </ul>

  <div class="thai-trans">
    <strong>(คำแปลภาษาไทย - จากใบงานจริงในห้องเรียน 2569 ภาพที่ 3):</strong> กำหนดกราฟเดิม 7 โหนด แต่เปลี่ยน <strong>จุดเริ่มต้น (Source Vertex) เป็นโหนด $v_3$</strong> ให้นักศึกษาเติมตารางประมวลผล Shortest Path (Known, Dist, Path) และ Queue ให้สมบูรณ์ จากนั้นตอบคำถาม 3 ข้อย่อย:<br>
    1. จงหาเส้นทางที่สั้นที่สุดจาก $v_3$ ไป $v_5$ จากตารางที่คำนวณได้ และความยาวของเส้นทางนั้นเท่ากับเท่าไร?<br>
    2. จงหาเส้นทางที่สั้นที่สุดจาก $v_3$ ไป $v_7$ จากตารางที่คำนวณได้ และความยาวของเส้นทางนั้นเท่ากับเท่าไร?<br>
    3. เส้นทางที่สั้นที่สุดจาก $v_4$ ไป $v_5$ มีความยาวและเส้นทางคืออะไร?
  </div>

  <div class="blank-sheet-box">
    <div style="font-size:13px; font-weight:bold; color:#0f766e; margin-bottom:6px;">📝 ช่องจำลองกระดาษคำตอบข้อ 6.2: ตารางประมวลผล Shortest Path (Source = 3)</div>
    <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start;">
      <div style="flex:2; min-width:280px;">
        <table style="text-align:center; font-size:12.5px;">
          <thead>
            <tr style="background:#0f766e; color:white;">
              <th>Vertex</th><th>Known</th><th>Dist ($d_v$)</th><th>Path ($p_v$)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>$v_1$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_2$</td><td></td><td></td><td></td></tr>
            <tr><td style="font-weight:bold; background:#f0fdfa;">$v_3$ (Src)</td><td></td><td></td><td></td></tr>
            <tr><td>$v_4$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_5$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_6$</td><td></td><td></td><td></td></tr>
            <tr><td>$v_7$</td><td></td><td></td><td></td></tr>
          </tbody>
        </table>
      </div>
      <div style="flex:1; min-width:140px; max-width:180px;">
        <div style="font-size:12px; font-weight:bold; text-align:center; color:#0f766e; margin-bottom:4px;">Queue (q)</div>
        <table style="text-align:center; font-size:12px;">
          <tr style="background:#0f766e; color:white;"><th>Slot</th><th>Vertex</th></tr>
          <tr><td>[6]</td><td></td></tr><tr><td>[5]</td><td></td></tr><tr><td>[4]</td><td></td></tr>
          <tr><td>[3]</td><td></td></tr><tr><td>[2]</td><td></td></tr><tr><td>[1]</td><td></td></tr><tr><td>[0]</td><td></td></tr>
        </table>
        <div style="font-size:11px; margin-top:4px; text-align:center;">front = ? &nbsp; back = ?</div>
      </div>
    </div>

    <div style="margin-top:12px; font-size:13.5px; line-height:2; background:#f8fafc; padding:12px; border-radius:6px; border:1px solid #cbd5e1;">
      <div>• <strong>จาก $v_3$ ไป $v_5$:</strong> The length = ............ The shortest path = ............................................................</div>
      <div>• <strong>จาก $v_3$ ไป $v_7$:</strong> The length = ............ The shortest path = ............................................................</div>
      <div>• <strong>จาก $v_4$ ไป $v_5$:</strong> The length = ............ The shortest path = ............................................................</div>
    </div>
  </div>

  <div class="solution-box">
    <div class="solution-title">💡 เฉลยละเอียดข้อ 6.2 (Shortest Path from Source Vertex 3 Solution):</div>
    <p><strong>1. ลำดับการประมวลผล BFS และการอัปเดตตาราง:</strong></p>
    <ul>
      <li><strong>เริ่มต้น (Init):</strong> $v_3$ เป็น Source &rarr; $d(v_3) = \mathbf{0}, p(v_3) = \mathbf{0}$, โหนดอื่นๆ มี $d = \infty, p = 0$ ทั้งหมด &rarr; <code>q.enqueue(3)</code></li>
      <li><strong>รอบที่ 1 (Dequeue 3):</strong> Known[3] = True &rarr; โหนดติดกันของ 3 คือ <strong>1 และ 6</strong><br>
        • โหนด 1: $d(1) = \infty \implies d(1) = 0 + 1 = \mathbf{1}, p(1) = \mathbf{3}$ &rarr; <code>q.enqueue(1)</code><br>
        • โหนด 6: $d(6) = \infty \implies d(6) = 0 + 1 = \mathbf{1}, p(6) = \mathbf{3}$ &rarr; <code>q.enqueue(6)</code>
      </li>
      <li><strong>รอบที่ 2 (Dequeue 1):</strong> Known[1] = True &rarr; โหนดติดกันของ 1 คือ <strong>2 และ 4</strong><br>
        • โหนด 2: $d(2) = \infty \implies d(2) = 1 + 1 = \mathbf{2}, p(2) = \mathbf{1}$ &rarr; <code>q.enqueue(2)</code><br>
        • โหนด 4: $d(4) = \infty \implies d(4) = 1 + 1 = \mathbf{2}, p(4) = \mathbf{1}$ &rarr; <code>q.enqueue(4)</code>
      </li>
      <li><strong>รอบที่ 3 (Dequeue 6):</strong> Known[6] = True &rarr; โหนด 6 ไม่มีเส้นทางออก (Sink)</li>
      <li><strong>รอบที่ 4 (Dequeue 2):</strong> Known[2] = True &rarr; โหนดติดกันของ 2 คือ <strong>4 และ 5</strong><br>
        • โหนด 4: $d(4) = 2 \neq \infty$ (ไม่ทำอะไร)<br>
        • โหนด 5: $d(5) = \infty \implies d(5) = 2 + 1 = \mathbf{3}, p(5) = \mathbf{2}$ &rarr; <code>q.enqueue(5)</code>
      </li>
      <li><strong>รอบที่ 5 (Dequeue 4):</strong> Known[4] = True &rarr; โหนดติดกันของ 4 คือ <strong>3, 6, 5, 7</strong><br>
        • โหนด 3, 6, 5: มีค่า dist ไม่เป็น $\infty$ แล้ว<br>
        • โหนด 7: $d(7) = \infty \implies d(7) = 2 + 1 = \mathbf{3}, p(7) = \mathbf{4}$ &rarr; <code>q.enqueue(7)</code>
      </li>
      <li><strong>รอบที่ 6 (Dequeue 5):</strong> Known[5] = True &rarr; โหนดติดกันคือ 7 ($d(7)=3$ แล้ว ไม่ทำอะไร)</li>
      <li><strong>รอบที่ 7 (Dequeue 7):</strong> Known[7] = True &rarr; โหนดติดกันคือ 6 ($d(6)=1$ แล้ว ไม่ทำอะไร)</li>
    </ul>

    <p><strong>ตารางผลลัพธ์สุทธิ Shortest Path Table (Source = 3):</strong></p>
    <table style="text-align:center; font-size:13px;">
      <tr style="background:#0f766e; color:white;">
        <th>Vertex ($v$)</th><th>Known</th><th>Dist ($d_v$)</th><th>Path ($p_v$)</th><th>Shortest Path จาก $v_3$</th><th>ความยาว (Length)</th>
      </tr>
      <tr><td>$v_1$</td><td>T (1)</td><td>1</td><td>3</td><td><strong>$v_3, v_1$</strong></td><td>1 edge</td></tr>
      <tr><td>$v_2$</td><td>T (1)</td><td>2</td><td>1</td><td><strong>$v_3, v_1, v_2$</strong></td><td>2 edges</td></tr>
      <tr><td style="background:#f0fdfa; font-weight:bold;">$v_3$ (Src)</td><td>T (1)</td><td>0</td><td>0</td><td><strong>$v_3$</strong></td><td>0</td></tr>
      <tr><td>$v_4$</td><td>T (1)</td><td>2</td><td>1</td><td><strong>$v_3, v_1, v_4$</strong></td><td>2 edges</td></tr>
      <tr><td style="background:#fef9c3; font-weight:bold;">$v_5$</td><td>T (1)</td><td>3</td><td>2</td><td><strong>$v_3, v_1, v_2, v_5$</strong></td><td><strong>3 edges</strong></td></tr>
      <tr><td>$v_6$</td><td>T (1)</td><td>1</td><td>3</td><td><strong>$v_3, v_6$</strong></td><td>1 edge</td></tr>
      <tr><td style="background:#fef9c3; font-weight:bold;">$v_7$</td><td>T (1)</td><td>3</td><td>4</td><td><strong>$v_3, v_1, v_4, v_7$</strong></td><td><strong>3 edges</strong></td></tr>
    </table>

    <p><strong>2. คำตอบตรงตามคำถามในใบงานจริง (Image 3 Answers):</strong></p>
    <ul style="line-height:1.8;">
      <li><strong>ตอบคำถาม 1:</strong> The length of the shortest path from Vertex 3 to Vertex 5 = <strong>3</strong><br>
        The shortest path from Vertex 3 to Vertex 5 = <strong>$v_3, v_1, v_2, v_5$</strong> (ย้อนรอยจาก $v_5 \leftarrow p(5)=2 \leftarrow p(2)=1 \leftarrow p(1)=3$)
      </li>
      <li><strong>ตอบคำถาม 2:</strong> The length of the shortest path from Vertex 3 to Vertex 7 = <strong>3</strong><br>
        The shortest path from Vertex 3 to Vertex 7 = <strong>$v_3, v_1, v_4, v_7$</strong> (ย้อนรอยจาก $v_7 \leftarrow p(7)=4 \leftarrow p(4)=1 \leftarrow p(1)=3$)
      </li>
      <li><strong>ตอบคำถาม 3 (v4 ไป v5):</strong> จาก Adjacency List มีเส้นเชื่อมตรงจากโหนด 4 ไปโหนด 5<br>
        The length of shortest path from Vertex 4 to Vertex 5 = <strong>1</strong> | The shortest path = <strong>$v_4, v_5$</strong>
      </li>
    </ul>
  </div>
"""

if "6.2 การประมวลผล Shortest Path โดยมีจุดเริ่มต้นที่ $v_3$" not in t1:
    idx_q7 = t1.find('<h2 id="q7"')
    t1 = t1[:idx_q7] + q6_worksheet_html + "\n\n  " + t1[idx_q7:]

with open(tab1_path, "w", encoding="utf-8") as f:
    f.write(t1)

print("generate_tab1.py updated with worksheet questions successfully!")

# =========================================================================
# 2. UPDATE GENERATE_TAB3.PY
# =========================================================================
tab3_path = r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab3.py"
with open(tab3_path, "r", encoding="utf-8") as f:
    t3 = f.read()

# Add Section 12 to Tab 3 (before </div> <!-- END TAB 3 -->)
tab3_section12 = r"""    <!-- 12. CLASSROOM WORKSHEETS DEEP DIVE -->
    <div id="th-worksheets" class="theory-box" style="border-left-color:#0284c7; background:#f0f9ff;">
      <div class="ref-tag">📖 อ้างอิง: ชุดใบงานจริงในห้องเรียน 2569 (DSA-pic ภาพที่ 1-5) / รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล</div>
      <h3 style="margin-top:4px; color:#0369a1; display:flex; align-items:center; gap:8px;">
        🎯 12. ถอดรหัสและวิเคราะห์เจาะลึก 5 ใบงานจริงในห้องเรียน (Classroom Worksheets Mastery)
      </h3>
      <p style="font-size:13.5px; color:#0369a1; margin-bottom:12px;">
        สรุปเจตนารมณ์ รูปแบบตาราง และจุดที่อาจารย์มักนำมาดัดแปลงออกเป็นข้อสอบปลายภาคจริง จากใบงานกระดาษทั้ง 5 ใบ:
      </p>

      <h4>1. ใบงานที่ 1: การสร้าง Binary Min-Heap 15 ตัว และการ deleteMin()</h4>
      <ul>
        <li><strong>ชุดตัวเลขทดสอบ:</strong> <code>10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2</code></li>
        <li><strong>วัตถุประสงค์ของอาจารย์:</strong> ทดสอบการสร้าง Complete Binary Tree ที่มีโหนดเต็มถึง 4 ระดับความสูง ($h=3$) ครบ 15 โหนด เพื่อดูว่านักศึกษาสามารถจัดการ Index ใน 1D Array แบบ 1-based (ช่อง [0] เว้นว่าง) ได้ถูกต้องหรือไม่</li>
        <li><strong>จุดที่ต้องระวังในการ deleteMin():</strong> นำค่าตัวสุดท้าย (8 ที่ช่อง 15) ย้ายมาที่ Root แล้ว Percolate Down:
          เปรียบเทียบลูกช่อง 2 (ค่า 3) และช่อง 3 (ค่า 2) &rarr; ลูกค่าน้อยสุดคือ 2 &rarr; ดึง 2 ขึ้นมา &rarr; hole เลื่อนไปที่ 3 &rarr; เปรียบเทียบลูกช่อง 6 (ค่า 5) และช่อง 7 (ค่า 4) &rarr; ลูกค่าน้อยสุดคือ 4 &rarr; ดึง 4 ขึ้นมา &rarr; hole เลื่อนไปที่ 7 &rarr; ลูกช่อง 14 (ค่า 13) มีค่ามากกว่า 8 &rarr; สิ้นสุดการ Percolate วาง 8 ที่ช่อง 7!</li>
      </ul>

      <h4>2. ใบงานที่ 2, 4, 5: Topological Sort (DAG &amp; Indegree Array)</h4>
      <ul>
        <li><strong>การแปลงกราฟเป็น Adjacency List:</strong> สังเกตว่าในใบงาน อาจารย์วาดหัวลูกศรชี้ไปยัง Linked List Node และมีสัญลักษณ์ กราวด์/Null ($\perp$) ปิดท้ายทุก List เสมอ</li>
        <li><strong>ตาราง Indegree Array:</strong> มีการลดค่า Indegree ทีละรอบ เมื่อโหนดใดมี Indegree ลดลงเหลือ 0 จะถูก <code>q.enqueue()</code> ทันที</li>
        <li><strong>การจำลอง Vertical Queue:</strong> ช่องคิวเขียนกลับด้านจาก <code>[6]</code> ลงมา <code>[0]</code> และมีตัวแปร <code>Currentsize</code>, <code>Front</code>, <code>back</code> กำกับ</li>
        <li><strong>ลำดับผลลัพธ์:</strong> <code>v1, v2, v5, v4, v3, v7, v6</code> (เขียนคั่นด้วย comma เท่านั้น ห้ามใส่ลูกศร)</li>
      </ul>

      <h4>3. ใบงานที่ 3: Shortest Path จาก Source Vertex = $v_3$</h4>
      <ul>
        <li><strong>การเปลี่ยนจุดเริ่มต้น (Source Vertex):</strong> อาจารย์จงใจเปลี่ยน Source Vertex จาก $v_1$ มาเป็น <strong>$v_3$</strong> เพื่อทดสอบว่านักศึกษาเข้าใจตรรกะ BFS จริงหรือไม่:
          โหนด $v_3$ จะเริ่มด้วย $d(v_3) = 0, p(v_3) = 0$ ขณะที่โหนดอื่นๆ ทั้งหมดเริ่มต้นด้วย $\infty, 0$</li>
        <li><strong>การถามหาระยะทางและเส้นทางระหว่างคู่โหนด:</strong>
          <ul>
            <li>จาก $v_3$ ไป $v_5$: ความยาว = <strong>3</strong> | เส้นทาง = <strong>$v_3, v_1, v_2, v_5$</strong></li>
            <li>จาก $v_3$ ไป $v_7$: ความยาว = <strong>3</strong> | เส้นทาง = <strong>$v_3, v_1, v_4, v_7$</strong></li>
            <li>จาก $v_4$ ไป $v_5$: ความยาว = <strong>1</strong> | เส้นทาง = <strong>$v_4, v_5$</strong></li>
          </ul>
        </li>
      </ul>
    </div>
"""

# Update quick nav for Tab 3 to include #th-worksheets
if "#th-worksheets" not in t3:
    t3 = t3.replace('<a href="#th-12traps" class="jump-pill danger">🚨 ตาราง 12 กับดัก 0 คะแนน</a>', '<a href="#th-worksheets" class="jump-pill alt">🎯 12. ถอดรหัสใบงานจริง 2569</a>\n      <a href="#th-12traps" class="jump-pill danger">🚨 ตาราง 12 กับดัก 0 คะแนน</a>')

if "12. ถอดรหัสและวิเคราะห์เจาะลึก 5 ใบงานจริงในห้องเรียน" not in t3:
    t3 = t3.replace('</div> <!-- END TAB 3 -->', tab3_section12 + '  </div> <!-- END TAB 3 -->')

with open(tab3_path, "w", encoding="utf-8") as f:
    f.write(t3)

print("generate_tab3.py updated with worksheet mastery guide successfully!")
