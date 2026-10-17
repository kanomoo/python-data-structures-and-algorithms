# -*- coding: utf-8 -*-
"""
Script to fix generate_tab2.py:
1. Remove spoilers in Q1.1: Remove h_0(X) = X mod 19 and R = 17 from problem statement.
2. Remove 'and for every occupied slot, mark the Info field with 'A'' from Q1.1 statement.
3. Remove Info row from Q1.1 blank sheet table, replace Element with Value (Key).
4. Rephrase Q1.6 so it asks for R rather than giving R = 17 in the question title.
5. In Q3.3, replace C++ template code with Python def insertion_sort(a):.
6. In Q7.2, add clear context on Python vs legacy 2564 C++ struct.
"""
import sys, re

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab2.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Q1.1 problem statement (remove R = 17 and h_0 spoilers)
old_q1_statement = r"""    <p><strong>Question Statement (EN):</strong> Given an empty Hash Table of size $\text{TableSize} = 19$ (indexed from $0$ to $18$) using Open Addressing with <strong>Double Hashing</strong> defined by:</p>
    $$\text{Primary Hash: } h_0(X) = X \bmod 19$$
    $$\text{Probe Formula: } h_i(X) = (h_0(X) + i \times (R - (X \bmod R))) \bmod 19 \quad \text{where } R = 17$$
    <p>Rehashing is triggered when the load factor strictly exceeds <strong>75%</strong>. Insert the following 8 keys sequentially into the hash table:</p>
    $$\mathbf{323, 17, 969, 868, 340, 370, 357, 391}$$
    <p>Show the step-by-step probe sequence for each key, fill the resulting Hash Table, and for every occupied slot, mark the <code>Info</code> field with <strong>'A'</strong> (Active).</p>"""

new_q1_statement = r"""    <p><strong>Question Statement (EN):</strong> Given an empty Hash Table of size $\text{TableSize} = 19$ (indexed from $0$ to $18$) in Python using Open Addressing with <strong>Double Hashing</strong> where probe step function is defined as $f(i) = i \times \text{hash}_2(X)$. Rehashing is triggered when the load factor strictly exceeds <strong>75%</strong>.</p>
    <p>Insert the following 8 keys sequentially into the hash table:</p>
    $$\mathbf{323, 17, 969, 868, 340, 370, 357, 391}$$
    <p>Show the step-by-step probe calculations for each key, determine the appropriate prime constant $R$, and fill the resulting Hash Table array in Python (empty slots remain <code>None</code>).</p>"""

content = content.replace(old_q1_statement, new_q1_statement)

# 2. Fix Thai translation of Q1.1
old_q1_thai = r"""      <strong>(คำแปลภาษาไทย - จากข้อสอบจริงปี 2561 หน้า 1):</strong> โครงสร้าง Hash Table ชนิด Open Addressing กำหนดวิธีการแก้การชนกันเป็นแบบ Double Hashing กำหนด TableSize ให้เป็น 19 คิดเปอร์เซ็นต์ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่มากกว่า 75% ให้นักศึกษาทำการ insert ข้อมูลจำนวน 8 ตัว ดังต่อไปนี้: <strong>323, 17, 969, 868, 340, 370, 357, 391</strong> เข้าไปใน HashTable ดังกล่าว โดยแสดงวิธีคิดการคำนวณการชนและการแก้การชน และนำตัวเลขมาใส่ในตาราง Hash Table ช่องใดเป็น Active ให้เขียน Info เป็น 'A' ด้วย"""

new_q1_thai = r"""      <strong>(คำแปลภาษาไทย - ข้อสอบจริงปี 2561 หน้า 1):</strong> โครงสร้าง Hash Table ชนิด Open Addressing กำหนดวิธีการแก้การชนกันเป็นแบบ Double Hashing กำหนด TableSize ให้เป็น 19 คิดเปอร์เซ็นต์ของการทำ Rehashing เมื่อ Table ใกล้จะเต็มที่มากกว่า 75% ให้นักศึกษาทำการ insert ข้อมูลจำนวน 8 ตัว ดังต่อไปนี้: <strong>323, 17, 969, 868, 340, 370, 357, 391</strong> เข้าไปใน HashTable ดังกล่าว โดยแสดงวิธีคิดการคำนวณการชนและการแก้การชน และนำตัวเลขมาใส่ในตาราง Hash Table ในภาษา Python (ช่องว่างเก็บ None)"""

content = content.replace(old_q1_thai, new_q1_thai)

# 3. Fix blank sheet table for Q1.1 (remove Info row, replace Element with Value (Key))
old_table = r"""      <table style="text-align:center; font-size:12px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:75px; text-align:center;">Slot</th>
            <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Element</td>
            <td style="height:30px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          </tr>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Info</td>
            <td style="height:25px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          </tr>
        </tbody>
      </table>
      <table style="text-align:center; font-size:12px; margin-top:8px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:75px; text-align:center;">Slot</th>
            <th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th><th>[16]</th><th>[17]</th><th>[18]</th><th style="background:#475569;">-</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Element</td>
            <td style="height:30px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#f1f5f9;">-</td>
          </tr>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Info</td>
            <td style="height:25px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#f1f5f9;">-</td>
          </tr>
        </tbody>
      </table>"""

new_table = r"""      <table style="text-align:center; font-size:12px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:95px; text-align:center;">Slot</th>
            <th>[0]</th><th>[1]</th><th>[2]</th><th>[3]</th><th>[4]</th><th>[5]</th><th>[6]</th><th>[7]</th><th>[8]</th><th>[9]</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Value (Key)</td>
            <td style="height:32px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
          </tr>
        </tbody>
      </table>
      <table style="text-align:center; font-size:12px; margin-top:8px;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th style="width:95px; text-align:center;">Slot</th>
            <th>[10]</th><th>[11]</th><th>[12]</th><th>[13]</th><th>[14]</th><th>[15]</th><th>[16]</th><th>[17]</th><th>[18]</th><th style="background:#475569;">-</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="font-weight:bold; background:#f0fdfa;">Value (Key)</td>
            <td style="height:32px;"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#f1f5f9;">-</td>
          </tr>
        </tbody>
      </table>"""

content = content.replace(old_table, new_table)

# 4. Fix Q1.6 so it asks for R instead of spoiling R=17
old_q16 = r"""    <h3 class="question-title past-q">
      <span>1.6 การเลือกค่า R ในสูตร Double Hashing (How to choose R for Double Hashing)</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> Why is $R = 17$ chosen for $\text{TableSize} = 19$? If the TableSize was <strong>11</strong>, what value of $R$ must be chosen?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> เหตุใดในโจทย์ข้อนี้จึงเลือก $R = 17$ เมื่อ TableSize = 19? และหากตารางแฮชมีขนาด <strong>11</strong> ช่อง จะต้องเลือกค่า $R$ เป็นเท่าใด เพราะเหตุใด?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        เกณฑ์การเลือกค่า R: $R$ ต้องเป็นจำนวนเฉพาะที่ .................................................................... กับ TableSize<br>
        สำหรับ TableSize = 11 จะต้องเลือก $R =$ ............ (ห้ามเลือก 11 เด็ดขาด เพราะ ....................................................)
      </p>
    </div>"""

new_q16 = r"""    <h3 class="question-title past-q">
      <span>1.6 กฎการเลือกค่า R ในสูตร Double Hashing (How to choose constant R)</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <p><strong>Question Statement (EN):</strong> State the rule for choosing the prime constant $R$ in Double Hashing. What value of $R$ is chosen when $\text{TableSize} = 19$? If $\text{TableSize} = 11$, what value of $R$ must be chosen and why?</p>
    <div class="thai-trans">
      <strong>(คำแปลภาษาไทย):</strong> จงระบุกฎเกณฑ์ในการเลือกค่าคงที่ $R$ ใน Double Hashing, สำหรับ TableSize = 19 จะได้ค่า $R$ เป็นเท่าใด? และหากตารางมีขนาด 11 ช่อง จะต้องเลือกค่า $R$ เป็นเท่าใด เพราะเหตุใด?
    </div>
    <div class="blank-sheet-box compact">
      <p style="margin:0; font-size:14px; line-height:2;">
        เกณฑ์การเลือกค่า R: $R$ ต้องเป็นจำนวนเฉพาะที่ .................................................................... กับ TableSize<br>
        สำหรับ TableSize = 19 จะได้ค่า $R =$ ............ | สำหรับ TableSize = 11 จะต้องเลือก $R =$ ............ (เพราะ ....................................................)
      </p>
    </div>"""

content = content.replace(old_q16, new_q16)

# 5. Fix Q3.3 Insertion Sort C++ code -> Python
old_q33_code = r"""      <pre style="margin:0; background:#f8fafc; color:#0f172a; border:1px solid #cbd5e1;"><code>template &lt;class Comparable&gt;
void insertionSort( vector&lt;Comparable&gt; &amp; a )
{
    // จงเขียนโค้ดฟังก์ชันที่แก้ไขแล้วตรงนี้:
    ....................................................................................................
}</code></pre>"""

new_q33_code = r"""      <pre style="margin:0; background:#f8fafc; color:#0f172a; border:1px solid #cbd5e1;"><code>def insertion_sort(a):
    # จงเขียนโค้ดฟังก์ชันภาษา Python ที่แก้ไขเพื่อนับและพิมพ์ Position Moves แต่ละรอบ (p) และยอดรวมทั้งหมด:
    ....................................................................................................
    ....................................................................................................
    ....................................................................................................</code></pre>"""

content = content.replace(old_q33_code, new_q33_code)

# Also update the solution in Q3.3 to feature Python first
old_q33_sol = r"""      <p><strong>3.3 ฟังก์ชันที่แก้ไขแล้ว (C++ &amp; Python):</strong></p>
      <pre><code>// C++ Implementation:
template &lt;class Comparable&gt;
void insertionSort( vector&lt;Comparable&gt; &amp; a ) {
    int total_moves = 0;
    for( int p = 1; p &lt; a.size(); ++p ) {
        Comparable tmp = std::move( a[ p ] );
        int j;
        int pass_moves = 0;
        for( j = p; j &gt; 0 &amp;&amp; tmp &lt; a[ j - 1 ]; --j ) {
            a[ j ] = std::move( a[ j - 1 ] );
            pass_moves++;
            total_moves++;
        }
        a[ j ] = std::move( tmp );
        cout &lt;&lt; "Pass p = " &lt;&lt; p &lt;&lt; ", Moves = " &lt;&lt; pass_moves &lt;&lt; ", j = " &lt;&lt; j &lt;&lt; endl;
    }
    cout &lt;&lt; "Total Moves = " &lt;&lt; total_moves &lt;&lt; endl;
}</code></pre>"""

new_q33_sol = r"""      <p><strong>3.3 ฟังก์ชันที่แก้ไขแล้ว (Python - ตรงตามโค้ดในห้องเรียน Exams/InsertionSort.py):</strong></p>
      <pre><code>def insertion_sort(a):
    total = 0
    print("Original: ", a, "Position Move")
    for p in range(1, len(a)):
        tmp = a[p]
        j = p
        swap = 0
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
            swap += 1
        a[j] = tmp
        total += swap
        print(f"After p = {p}", a, swap)
    print(f"Result : {a}")
    print(f"Total Moves: {total}")

# (หมายเหตุ: ในข้อสอบเก่า C++ ปี 2564 ใช้ template <class Comparable> void insertionSort(vector<Comparable>& a))</code></pre>"""

content = content.replace(old_q33_sol, new_q33_sol)

# 6. Fix Q7.2: Python vs legacy C++ explanation
old_q72 = r"""    <h3 class="question-title past-q">
      <span>7.2 ประโยคคำสั่งแทน HashEntry ในคลาส HashTable [ข้อสอบจริงปี 2564 หน้า 13 ข้อ 7.2]</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย):</strong> จงเขียนประโยคคำสั่ง (Statement) เพื่อใช้แทนฟังก์ชัน HashEntry ใน member function insert ของ Class HashTable โดยมีการเรียกใช้งาน: <code>array[ currentPos ] = HashEntry( x, ACTIVE );</code>
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียด:</div>
      <p>ในภาษา C++/Python สามารถเขียนกำหนดค่าให้กับฟิลด์ภายใน Struct หรือ Object ได้โดยตรง:</p>
      <pre><code>// ในภาษา C++:
array[ currentPos ].element = x;
array[ currentPos ].info = ACTIVE;

# ในภาษา Python:
self.array[currentPos] = HashEntry(x, 'ACTIVE')
# หรือหากแยกเป็นลิสต์:
self.elements[currentPos] = x
self.info[currentPos] = 'ACTIVE'</code></pre>
    </div>"""

new_q72 = r"""    <h3 class="question-title past-q">
      <span>7.2 การกำหนดค่าใน HashTable: Python List vs Struct C++ [ข้อสอบประวัติศาสตร์ปี 2564 หน้า 13 ข้อ 7.2]</span>
      <span class="score-badge past-badge">Score: 2 Marks</span>
    </h3>
    <div class="thai-trans">
      <strong>(โจทย์ภาษาไทย &amp; บริบทเปรียบเทียบ):</strong> ในข้อสอบปี 2564 (C++) ข้อสอบถามประโยคคำสั่งเพื่อใช้แทนฟังก์ชัน <code>HashEntry(x, ACTIVE)</code> ในคำสั่ง <code>array[currentPos] = HashEntry(x, ACTIVE);</code><br>
      จงอธิบายความแตกต่างระหว่างการเก็บข้อมูลในตารางแฮชภาษา C++ ปี 2564 กับภาษา Python ในหลักสูตรปัจจุบัน 2569 ของ อ.ประดิษฐ์
    </div>
    <div class="solution-box">
      <div class="solution-title">💡 เฉลยละเอียดและเปรียบเทียบเชิงสถาปัตยกรรม:</div>
      <p><strong>1. ในภาษา Python (หลักสูตรปัจจุบัน 2569 อ.ประดิษฐ์):</strong></p>
      <ul>
        <li>ตารางแฮชถูกสร้างเป็น 1D List ธรรมดา เช่น <code>self.table = [None] * TableSize</code></li>
        <li>ช่องว่างจะเก็บค่า <code>None</code></li>
        <li>เมื่อทำการแทรกข้อมูล จะบันทึกค่าลงช่องตรงๆ: <code>self.table[currentPos] = x</code> (ไม่มี struct <code>info</code> หรือสถานะ <code>'A'</code> มาเกะกะ)</li>
      </ul>
      <p><strong>2. ในภาษา C++ (ข้อสอบเก่าประวัติศาสตร์ปี 2564):</strong></p>
      <ul>
        <li>ใช้ Struct ซ้อนเรียกว่า <code>HashEntry</code> มี 2 ฟิลด์คือ <code>element</code> และ <code>info</code> (ACTIVE, EMPTY, DELETED)</li>
        <li>คำสั่งที่ใช้แทน Constructor <code>HashEntry(x, ACTIVE)</code> คือ:<br>
          <code>array[ currentPos ].element = x;</code><br>
          <code>array[ currentPos ].info = ACTIVE;</code>
        </li>
      </ul>
    </div>"""

content = content.replace(old_q72, new_q72)

with open(r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab2.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_tab2.py updated successfully!")
