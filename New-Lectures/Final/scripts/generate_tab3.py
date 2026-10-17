# -*- coding: utf-8 -*-
"""
Module to generate HTML for Tab 3:
📖 ชุดที่ 3: คลังสรุปทฤษฎี นิยามข้อเขียน & 12 กับดักได้ 0 คะแนน (Theory Mastery & 12 Zero-Score Traps)
Adheres strictly to the lectures and slide definitions of Assoc. Prof. Dr. Pradit Pitaksatheinkul.
Enforces exact English definitions, Thai translations, formulas, calculations, and zero-score prevention rules.
"""

def get_tab3_html():
    return r"""
  <!-- ========================================================================= -->
  <!-- TAB 3: THEORY MASTERY, DEFINITIONS, FORMULAS & 12 ZERO-SCORE TRAPS       -->
  <!-- ========================================================================= -->
  <div id="tab-theory" class="tab-content">
    <h1 class="section-heading theory-heading">
      📖 ชุดที่ 3: คลังสรุปทฤษฎี นิยามข้อเขียน &amp; 12 กับดักได้ 0 คะแนน (Theory Mastery, Exact Definitions &amp; Zero-Score Traps)
    </h1>

    <div class="rules-box" style="border-left-color:#b45309; background:#fffbeb;">
      <div class="rules-title" style="color:#b45309;">📌 คำแนะนำการใช้คลังทฤษฎีและการเตรียมตัวเข้าห้องสอบ:</div>
      <p style="margin:4px 0; font-size:13.5px;">
        รวบรวมนิยามภาษาอังกฤษ คำแปลภาษาไทย สูตรการคำนวณร้อยละ (Percentage) หลักการสำคัญที่ อ.ประดิษฐ์ มักนำมาออกเป็นข้อสอบข้อเขียนย่อย และตาราง 12 กับดักร้ายแรงที่ทำให้รุ่นพี่ได้ 0 คะแนนมาแล้ว ทุกข้อมีที่มาและหน้าอ้างอิงจากตำรา Mark Allen Weiss และสไลด์บรรยายของอาจารย์
      </p>
    </div>

    <!-- QUICK NAV FOR TAB 3 -->
    <div class="nav-jump-bar">
      <span class="nav-jump-label">⚡ ทางลัดหัวข้อทฤษฎี:</span>
      <a href="#th-wrap" class="jump-pill warn">1. หลักการ Wrap Around</a>
      <a href="#th-tablesize" class="jump-pill warn">2. การเลือก New TableSize</a>
      <a href="#th-r-val" class="jump-pill warn">3. การเลือกค่า R</a>
      <a href="#th-rehash-pct" class="jump-pill warn">4. สูตรเปอร์เซ็นต์ Rehashing</a>
      <a href="#th-sort-cases" class="jump-pill warn">5. Worst/Average/Best Sorting</a>
      <a href="#th-heap-theory" class="jump-pill warn">6. Binary Heap Array &amp; hole</a>
      <a href="#th-tree-nodes" class="jump-pill warn">7. Complete Binary Tree Nodes</a>
      <a href="#th-complete-graph" class="jump-pill warn">8. Complete Graph Edges</a>
      <a href="#th-ram-waste" class="jump-pill warn">9. RAM Waste Percentage</a>
      <a href="#th-properties" class="jump-pill warn">10. Two &amp; Three Properties</a>
      <a href="#th-12traps" class="jump-pill danger">🚨 ตาราง 12 กับดัก 0 คะแนน</a>
      <a href="#th-worksheets" class="jump-pill alt">🎯 12. ถอดรหัสใบงานจริง 2569</a>
      <a href="#th-primes" class="jump-pill" style="border-color:#10b981; color:#065f46; background:#ecfdf5;">🔢 13. ตารางจำนวนเฉพาะ &amp; ค่า R</a>
      <a href="#th-ascii" class="jump-pill" style="border-color:#8b5cf6; color:#5b21b6; background:#f5f3ff;">🔤 14. ตารางรหัส ASCII (0–127)</a>
    </div>

    <!-- 1. WRAP AROUND -->
    <div id="th-wrap" class="theory-box" style="border-left-color:#2563eb;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (Hashing), pp. 195-200 / สไลด์ Hashing อ.ประดิษฐ์ แผ่นที่ 22-26</div>
      <h3 style="margin-top:4px; color:#1e40af;">1. หลักการ Wrap Around ใน Hashing และ Circular Queue (Wrap Around Principle)</h3>
      <p><strong>คำจำกัดความตามสไลด์ภาษาอังกฤษ (Exact English Slide Definition):</strong></p>
      <blockquote style="margin:8px 0; padding:10px 15px; background:#eff6ff; border-left:4px solid #3b82f6; font-style:italic; font-family:'JetBrains Mono', Consolas, monospace; font-size:13.5px; color:#1e3a8a;">
        "When the key was mapped to the last index of hash table, it go back to the first index of hash table by mod tablesize one more time."
      </blockquote>
      <p><strong>คำอธิบายภาษาไทย (Thai Explanation):</strong></p>
      <div class="thai-trans" style="margin:6px 0;">
        <strong>หลักการ Wrap around ใน Hashing:</strong> คือเมื่อการคำนวณตำแหน่งโพรบ (Probe) ก้าวเดินไปจนเกินช่องสุดท้ายของ Hash Table (เกินดัชนี <code>TableSize - 1</code>) ระบบจะไม่ปล่อยให้ Index หลุดขอบอาร์เรย์ แต่จะวนกลับมาเริ่มต้นที่ช่องหมายเลข 0 ใหม่อีกครั้ง โดยอาศัยการนำตำแหน่งที่คำนวณได้มาทำการ <strong>Modulo ด้วย TableSize (mod TableSize)</strong> อีกรอบหนึ่งนั่นเอง
      </div>
      <p><strong>ใน Circular Queue:</strong> เมื่อ pointer <code>rear</code> หรือ <code>front</code> เดินไปถึง <code>capacity - 1</code> จะวนกลับมาช่อง 0 ด้วยสูตร <code>(rear + 1) % capacity</code> ป้องกันปัญหาหน่วยความจำสูญเปล่าทางซ้าย (False Overflow)</p>
    </div>

    <!-- 2. NEW TABLESIZE -->
    <div id="th-tablesize" class="theory-box" style="border-left-color:#0d9488;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (Rehashing), pp. 210-212 / สไลด์ Rehashing อ.ประดิษฐ์ แผ่นที่ 41</div>
      <h3 style="margin-top:4px; color:#0f766e;">2. หลักการเลือกขนาดตารางใหม่เมื่อทำ Rehashing (How to Choose a New TableSize is...)</h3>
      <p><strong>คำจำกัดความตามสไลด์ภาษาอังกฤษ (Exact English Slide Definition):</strong></p>
      <blockquote style="margin:8px 0; padding:10px 15px; background:#f0fdfa; border-left:4px solid #0d9488; font-style:italic; font-family:'JetBrains Mono', Consolas, monospace; font-size:13.5px; color:#0f766e;">
        "How to choose a new TableSize is 'Choose the smallest prime number but greater than or equal to double of the TableSize of the old Hash Table.'"
      </blockquote>
      <p><strong>คำอธิบายภาษาไทย (Thai Explanation):</strong></p>
      <div class="thai-trans" style="margin:6px 0;">
        <strong>การเลือกขนาด TableSize ใหม่:</strong> ให้เลือก TableSize ใหม่เป็น <strong>"เลขจำนวนเฉพาะ (Prime Number) ที่น้อยที่สุด แต่มากกว่าหรือเท่ากับ 2 เท่าของ TableSize ของ Hash Table เดิม"</strong>
      </div>
      <p><strong>สูตรคณิตศาสตร์:</strong> $$\text{NewTableSize} = \text{Smallest Prime} \ge 2 \times \text{OldTableSize}$$</p>
      <p><strong>ตารางเทียบขนาดตารางใหม่ตามสูตรที่มักออกสอบ:</strong></p>
      <table style="font-size:13px; text-align:center;">
        <thead>
          <tr style="background:#0f766e; color:white;">
            <th>Old TableSize</th>
            <th>$2 \times \text{OldSize}$</th>
            <th>จำนวนเฉพาะตัวถัดไปที่ $\ge 2 \times \text{OldSize}$</th>
            <th>New TableSize ที่ต้องตอบในข้อสอบ</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>7</strong></td><td>14</td><td>17 (14, 15, 16 ไม่ใช่จำนวนเฉพาะ)</td><td><strong style="color:#0f766e; font-size:15px;">17</strong></td></tr>
          <tr><td><strong>10</strong></td><td>20</td><td>23 (20, 21, 22 ไม่ใช่จำนวนเฉพาะ)</td><td><strong style="color:#0f766e; font-size:15px;">23</strong></td></tr>
          <tr><td><strong>11</strong></td><td>22</td><td>23</td><td><strong style="color:#0f766e; font-size:15px;">23</strong></td></tr>
          <tr><td><strong>13</strong></td><td>26</td><td>29</td><td><strong style="color:#0f766e; font-size:15px;">29</strong></td></tr>
          <tr><td><strong>17</strong></td><td>34</td><td>37</td><td><strong style="color:#0f766e; font-size:15px;">37</strong></td></tr>
          <tr><td><strong>19</strong> (ข้อสอบจริง)</td><td>38</td><td>41 (38, 39, 40 ไม่ใช่จำนวนเฉพาะ)</td><td><strong style="color:#0f766e; font-size:15px;">41</strong></td></tr>
        </tbody>
      </table>
    </div>

    <!-- 3. HOW TO CHOOSE R FOR DOUBLE HASHING -->
    <div id="th-r-val" class="theory-box" style="border-left-color:#b45309;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5, pp. 204-208 / ข้อสอบจริงปี 2561, 2564 &amp; สไลด์บรรยาย</div>
      <h3 style="margin-top:4px; color:#b45309;">3. การเลือกค่า $R$ ในสูตร Double Hashing (How to Choose R for Double Hashing)</h3>
      <p><strong>สูตร Double Hashing มาตรฐาน:</strong></p>
      $$h_i(X) = (h_0(X) + i \times hash_2(X)) \bmod \text{TableSize} \quad \text{where } hash_2(X) = R - (X \bmod R)$$
      <p><strong>กฎเกณฑ์การเลือกค่า $R$ (Rules for choosing $R$):</strong></p>
      <ul>
        <li>$R$ ต้องเป็น <strong>จำนวนเฉพาะ (Prime Number)</strong></li>
        <li>$R$ ต้องมีค่าน้อยกว่า TableSize อย่างเคร่งครัด: <strong>$R &lt; \text{TableSize}$</strong></li>
        <li>ตามหลักการออกแบบ: <strong>$R$ คือจำนวนเฉพาะที่มากที่สุดที่น้อยกว่า TableSize (Largest prime strictly less than TableSize)</strong></li>
      </ul>
      <p><strong>ตัวอย่างการเลือก $R$:</strong></p>
      <ul>
        <li>ถ้า $\text{TableSize} = 10 \implies R = \mathbf{7}$</li>
        <li>ถ้า $\text{TableSize} = 11 \implies R = \mathbf{7}$ (⚠️ <em>ห้ามเลือก 11 เพราะ $R$ ต้อง $&lt; \text{TableSize}$ อย่างเคร่งครัด!</em>)</li>
        <li>ถ้า $\text{TableSize} = 19 \implies R = \mathbf{17}$</li>
      </ul>
    </div>

    <!-- 4. REHASHING PERCENTAGE FORMULAS -->
    <div id="th-rehash-pct" class="theory-box" style="border-left-color:#7c3aed;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5, pp. 209-211 / ข้อสอบจริงปี 2561 หน้า 3 &amp; ปี 2564 หน้า 1, 6</div>
      <h3 style="margin-top:4px; color:#6d28d9;">4. สูตรการคำนวณร้อยละ (Percentage Calculation) และเกณฑ์การเกิด Rehashing</h3>
      <p><strong>สูตร Load Factor ($\lambda$):</strong></p>
      $$\text{Load Factor } \lambda = \frac{N}{\text{TableSize}} \times 100\% \quad \text{โดยที่ } N = \text{จำนวนคีย์ที่บันทึกอยู่ในตาราง}$$
      <p><strong>กรณีศึกษาที่ 1: ตารางขนาด 7 ช่อง (สไลด์สอนในห้องเรียน):</strong></p>
      <ul>
        <li>มีคีย์ 4 ตัว: $\lambda = \frac{4}{7} \times 100\% = \mathbf{57.14\%}$</li>
        <li>มีคีย์ 5 ตัว: $\lambda = \frac{5}{7} \times 100\% = \mathbf{71.42\%}$</li>
        <li>ถ้าเกณฑ์กำหนดให้ Rehash เมื่อข้อมูลเกิน <strong>70%</strong>: การแทรกคีย์ตัวที่ 5 จะมี $\lambda = 71.42\% &gt; 70\%$ ทำให้ <strong>เกิดการ Rehashing ทันที!</strong></li>
      </ul>
      <p><strong>กรณีศึกษาที่ 2: ข้อสอบจริงปี 2561 ($\text{TableSize} = 19$, เกณฑ์ Rehash &gt; 75%):</strong></p>
      <ul>
        <li>มีคีย์อยู่แล้ว 8 ตัว: $\lambda = \frac{8}{19} \times 100\% = \mathbf{42.11\%}$</li>
        <li>เกณฑ์ 75% ของ 19: $19 \times 0.75 = 14.25$ ช่อง &rarr; เกิน 75% คือต้องมีข้อมูลอย่างน้อย <strong>15 ตัว</strong></li>
        <li>จำนวนคีย์ที่ต้องใส่เพิ่ม: $15 - 8 = \mathbf{7 \text{ ตัว}}$</li>
      </ul>
      <p><strong>กรณีศึกษาที่ 3: ข้อสอบจริงปี 2564 ($\text{TableSize} = 19$, เกณฑ์ Rehash &gt; 80%):</strong></p>
      <ul>
        <li>มีคีย์อยู่แล้ว 8 ตัว: $\lambda = \frac{8}{19} \times 100\% = \mathbf{42.11\%}$</li>
        <li>เกณฑ์ 80% ของ 19: $19 \times 0.80 = 15.20$ ช่อง &rarr; เกิน 80% คือต้องมีข้อมูลอย่างน้อย <strong>16 ตัว</strong></li>
        <li>จำนวนคีย์ที่ต้องใส่เพิ่ม: $16 - 8 = \mathbf{8 \text{ ตัว}}$</li>
      </ul>
    </div>

    <!-- 5. SORTING CASES -->
    <div id="th-sort-cases" class="theory-box" style="border-left-color:#0284c7;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 7 (Sorting), pp. 281-305 / ข้อสอบจริงปี 2564 หน้า 9 &amp; 2561 หน้า 8</div>
      <h3 style="margin-top:4px; color:#0369a1;">5. ตารางวิเคราะห์ Worst Case, Average Case, และ Best Case ของ Sorting Algorithms</h3>
      <table style="font-size:12.5px;">
        <thead>
          <tr style="background:#0284c7; color:white;">
            <th>Algorithm</th>
            <th>Best-Case Time</th>
            <th>Average-Case Time</th>
            <th>Worst-Case Time</th>
            <th>สูตรจำนวน Position Moves / Swaps</th>
            <th>ลักษณะข้อมูล Worst Case</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Insertion Sort</strong></td>
            <td>$O(N)$<br>(เปรียบเทียบ $N-1$ ครั้ง)</td>
            <td>$O(N^2)$</td>
            <td>$O(N^2)$</td>
            <td>
              • Best: $0$ shifts (ย้ายเข้าที่เดิม)<br>
              • Average: $\approx \frac{N(N-1)}{4}$ shifts<br>
              • Worst: $\frac{N(N-1)}{2}$ shifts
            </td>
            <td>ข้อมูลเรียงกลับหลังจากมากไปน้อย (Strictly Descending Order)</td>
          </tr>
          <tr>
            <td><strong>Bubble Sort</strong></td>
            <td>$O(N)$<br>(ใช้ Flag ตรวจสอบรอบแรก)</td>
            <td>$O(N^2)$</td>
            <td>$O(N^2)$</td>
            <td>
              • Swaps = Inversions เสมอ!<br>
              • Worst Swaps: $\frac{N(N-1)}{2}$<br>
              • Average Swaps: $\frac{N(N-1)}{4}$
            </td>
            <td>ข้อมูลเรียงกลับหลังจากมากไปน้อย (มี Inversions สูงสุด)</td>
          </tr>
          <tr>
            <td><strong>Selection Sort</strong></td>
            <td>$O(N^2)$</td>
            <td>$O(N^2)$</td>
            <td>$O(N^2)$</td>
            <td>
              • Comparisons: $\frac{N(N-1)}{2}$ เท่ากันทุกกรณี!<br>
              • Swaps: อย่างมากที่สุด $N-1$ ครั้ง
            </td>
            <td>ทุกกรณีเทียบเท่ากัน (ไม่ขึ้นกับลำดับข้อมูล)</td>
          </tr>
          <tr>
            <td><strong>Quicksort</strong> (Median-of-3)</td>
            <td>$O(N \log N)$</td>
            <td>$O(N \log N)$</td>
            <td>$O(N^2)$</td>
            <td>Pivot แบ่งครึ่งเท่าๆ กันใน Best/Average Case, แบ่ง $0$ กับ $N-1$ ใน Worst Case</td>
            <td>เลือก Pivot ตัวต่ำสุดหรือสูงสุดตลอดเวลา (หากไม่ใช้ Median-of-Three)</td>
          </tr>
        </tbody>
      </table>
      <div class="thai-trans" style="margin-top:8px;">
        ⚠️ <strong>ข้อสอบชอบถาม:</strong> <em>"ทำไม Insertion Sort และ Bubble Sort จึงใช้เวลาเฉลี่ย $O(N^2)$?"</em><br>
        <strong>คำตอบ:</strong> เพราะข้อมูลที่สุ่มมาจะมี Inversion เฉลี่ยเท่ากับ $\frac{N(N-1)}{4}$ คู่ และการสลับตำแหน่ง (Swap) ของข้อมูล 2 ตัวที่ติดกันสามารถกำจัด Inversion ได้ทีละ 1 คู่เท่านั้น จึงต้องใช้จำนวนขั้นตอนการทำงานเป็นสัดส่วนกับ $N^2$ เสมอ!
      </div>
    </div>

    <!-- 6. BINARY HEAP THEORY -->
    <div id="th-heap-theory" class="theory-box" style="border-left-color:#16a34a;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 6 (Priority Queues), pp. 243-255 / สไลด์ Binary Heap ภาพที่ 5-9</div>
      <h3 style="margin-top:4px; color:#15803d;">6. การแทนค่า Binary Heap ด้วยอาร์เรย์ 1 มิติ และการ Trace ตัวแปร hole</h3>
      <p><strong>1. ทำไมจึงใช้ 1D Array แทน Binary Heap ได้อย่างสมบูรณ์แบบ?</strong></p>
      <div class="thai-trans" style="margin:4px 0;">
        เพราะคุณสมบัติ <strong>Structure Property</strong> กำหนดให้ Heap ต้องเป็น <strong>Complete Binary Tree</strong> (ต้นไม้ทวิภาคสมบูรณ์) ที่โหนดทุกชั้นถูกเติมเต็ม และชั้นสุดท้ายถูกเติมจากซ้ายไปขวาเสมอ จึงไม่มีช่องว่าง (Gaps) เกิดขึ้นในอาร์เรย์ ทำให้สามารถระบุตำแหน่ง Parent และ Child ได้ด้วยการคูณหารดัชนีในเวลา $O(1)$ โดยไม่ต้องเสียหน่วยความจำให้กับ Pointer
      </div>
      <p><strong>2. สูตรดัชนีแบบ 1-Based Indexing (ช่อง [0] ใส่ Sentinel $-\infty$):</strong></p>
      <ul>
        <li>$\text{Parent of } i = \lfloor i / 2 \rfloor$ (ภาษา Python: <code>i // 2</code>)</li>
        <li>$\text{Left Child of } i = 2 \times i$</li>
        <li>$\text{Right Child of } i = 2 \times i + 1$</li>
      </ul>
      <p><strong>3. ขั้นตอนการ Trace ฟังก์ชัน <code>insert(x)</code> ด้วยตัวแปร <code>hole</code>:</strong></p>
      <pre><code>hole = ++currentSize
while array[hole // 2] > x:
    array[hole] = array[hole // 2]  # เลื่อน parent ลงมา
    hole = hole // 2                # เลื่อน hole ขึ้นไป
array[hole] = x                     # วางค่า x ลงใน hole ที่ถูกต้อง</code></pre>
      <p><strong>4. ไวยากรณ์การเรียกเมธอด <code>deleteMin()</code>:</strong></p>
      <p>เรียกแบบ <code>min_val = myheap.deleteMin()</code> (ไม่มีพารามิเตอร์) ห้ามใส่ argument ลงในวงเล็บเด็ดขาด</p>
    </div>

    <!-- 7. COMPLETE BINARY TREE NODE COUNTS -->
    <div id="th-tree-nodes" class="theory-box" style="border-left-color:#e11d48;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 4, 6 / ข้อสอบจริงปี 2564 หน้า 13 &amp; ปี 2561 หน้า 15</div>
      <h3 style="margin-top:4px; color:#be123c;">7. จำนวนโหนดต่ำสุดและสูงสุดของ Complete Binary Tree ที่ความสูง $h$</h3>
      <p><strong>สูตรความสูง $h$ (นับ Root มีความสูงเป็น 0):</strong></p>
      $$\text{Minimum Nodes } = 2^h \qquad \text{Maximum Nodes } = 2^{h+1} - 1$$
      <p><strong>ตารางคำนวณสำเร็จรูปสำหรับเข้าห้องสอบ (ห้ามตอบติดเลขยกกำลัง!):</strong></p>
      <table style="font-size:13px; text-align:center;">
        <thead>
          <tr style="background:#be123c; color:white;">
            <th>ความสูง $h$</th>
            <th>สูตรจำนวนโหนดต่ำสุด ($2^h$)</th>
            <th>จำนวนโหนดต่ำสุด (จำนวนเต็ม)</th>
            <th>สูตรจำนวนโหนดสูงสุด ($2^{h+1}-1$)</th>
            <th>จำนวนโหนดสูงสุด (จำนวนเต็ม)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>$h = 3$</td><td>$2^3$</td><td><strong>8</strong></td><td>$2^4 - 1$</td><td><strong>15</strong></td></tr>
          <tr><td>$h = 4$</td><td>$2^4$</td><td><strong>16</strong></td><td>$2^5 - 1$</td><td><strong>31</strong></td></tr>
          <tr><td>$h = 5$</td><td>$2^5$</td><td><strong>32</strong></td><td>$2^6 - 1$</td><td><strong>63</strong></td></tr>
          <tr><td><strong>$h = 10$</strong> (ข้อสอบจริง)</td><td>$2^{10}$</td><td><strong style="color:#be123c; font-size:15px;">1,024</strong></td><td>$2^{11} - 1$</td><td><strong style="color:#be123c; font-size:15px;">2,047</strong></td></tr>
          <tr><td><strong>$h = 16$</strong> (ข้อสอบจริง)</td><td>$2^{16}$</td><td><strong style="color:#be123c; font-size:15px;">65,536</strong></td><td>$2^{17} - 1$</td><td><strong style="color:#be123c; font-size:15px;">131,071</strong></td></tr>
        </tbody>
      </table>
    </div>

    <!-- 8. COMPLETE GRAPH EDGES -->
    <div id="th-complete-graph" class="theory-box" style="border-left-color:#4f46e5;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9 (Graph Algorithms), pp. 363-366 / ข้อสอบจริงปี 2564 หน้า 13</div>
      <h3 style="margin-top:4px; color:#4338ca;">8. สูตรจำนวนเส้นเชื่อมใน Complete Graph แบบไม่มีทิศทาง ($K_V$)</h3>
      <p><strong>สูตรจำนวนเส้นเชื่อม (Number of Undirected Edges):</strong></p>
      $$|E| = \frac{V(V-1)}{2}$$
      <p><strong>ตารางคำนวณจำนวนเส้นเชื่อมที่มักออกสอบ:</strong></p>
      <table style="font-size:13px; text-align:center;">
        <thead>
          <tr style="background:#4338ca; color:white;">
            <th>จำนวนจุดยอด ($V$)</th>
            <th>แสดงวิธีคิด $\frac{V(V-1)}{2}$</th>
            <th>จำนวนเส้นเชื่อมที่ต้องตอบ (จำนวนเต็มเท่านั้น)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>$V = 5$ ($K_5$)</td><td>$\frac{5 \times 4}{2} = 10$</td><td><strong>10 เส้น</strong></td></tr>
          <tr><td>$V = 7$ ($K_7$)</td><td>$\frac{7 \times 6}{2} = 21$</td><td><strong>21 เส้น</strong></td></tr>
          <tr><td><strong>$V = 10$ ($K_{10}$)</strong> (ข้อสอบจริง)</td><td>$\frac{10 \times 9}{2} = \frac{90}{2}$</td><td><strong style="color:#4338ca; font-size:15px;">45 เส้น</strong></td></tr>
          <tr><td><strong>$V = 16$ ($K_{16}$)</strong> (ข้อสอบจริง)</td><td>$\frac{16 \times 15}{2} = \frac{240}{2}$</td><td><strong style="color:#4338ca; font-size:15px;">120 เส้น</strong></td></tr>
          <tr><td>$V = 20$ ($K_{20}$)</td><td>$\frac{20 \times 19}{2} = \frac{380}{2}$</td><td><strong>190 เส้น</strong></td></tr>
        </tbody>
      </table>
      <div class="alert-box">
        ⚠️ <strong>คำเตือนจุดตัด 0 คะแนน:</strong> อ.ประดิษฐ์ สั่งชัดเจนว่า <em>"ให้ตอบเป็นตัวเลขจำนวนเต็มเท่านั้น ห้ามติดสมการ"</em> ใครตอบติดรูป $\frac{10(9)}{2}$ หรือ $\frac{16(15)}{2}$ จะถูกหักคะแนนจนเหลือ 0 ทันที!
      </div>
    </div>

    <!-- 9. RAM WASTE PERCENTAGE -->
    <div id="th-ram-waste" class="theory-box" style="border-left-color:#059669;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 9, pp. 364-367 / สไลด์เรื่อง Graph อ.ประดิษฐ์</div>
      <h3 style="margin-top:4px; color:#047857;">9. การคำนวณร้อยละความสูญเสียใน RAM (Graph Memory Waste Percentage)</h3>
      <p>เมื่อแทนกราฟด้วย <strong>Adjacency Matrix</strong> ขนาด $|V| \times |V|$:</p>
      <ul>
        <li><strong>จำนวนช่องทั้งหมดในหน่วยความจำ:</strong> $|V|^2$ ช่อง</li>
        <li><strong>ช่องที่มีข้อมูลจริง (มีเส้นเชื่อม Edge = 1):</strong> $|E|$ ช่อง (สำหรับ Directed Graph)</li>
        <li><strong>ร้อยละการใช้งานหน่วยความจำ (Actively Used %):</strong> $$\text{Used } \% = \frac{|E|}{|V|^2} \times 100\%$$</li>
        <li><strong>ร้อยละความสูญเปล่าในหน่วยความจำ (Wasted %):</strong> $$\text{Wasted } \% = \frac{|V|^2 - |E|}{|V|^2} \times 100\% = 100\% - \text{Used } \%$$</li>
      </ul>
      <p><strong>ตัวอย่างการคำนวณสำหรับกราฟ $|V| = 7, |E| = 12$:</strong></p>
      <ul>
        <li>ช่องทั้งหมด $= 7 \times 7 = \mathbf{49 \text{ ช่อง}}$</li>
        <li>ช่องที่มีเส้นเชื่อม $= \mathbf{12 \text{ ช่อง}}$ &rarr; ใช้งานจริง $= \frac{12}{49} \times 100\% = \mathbf{24.49\%}$</li>
        <li>ช่องที่ว่างเปล่า (มีค่า 0) $= 49 - 12 = \mathbf{37 \text{ ช่อง}}$ &rarr; สูญเปล่า $= \frac{37}{49} \times 100\% = \mathbf{75.51\%}$</li>
      </ul>
      <p><strong>เมื่อเทียบกับ Adjacency List:</strong></p>
      <p>สำหรับ Sparse Graph (กราฟเส้นเชื่อมน้อย เช่น $V = 10, E = 20$): Adjacency Matrix ใช้ $10 \times 10 = 100$ หน่วย ขณะที่ Adjacency List ใช้ $10 + 20 = 30$ หน่วย ช่วยประหยัดพื้นที่หน่วยความจำได้ถึง <strong>70%</strong></p>
    </div>

    <!-- 10. TWO AND THREE PROPERTIES -->
    <div id="th-properties" class="theory-box" style="border-left-color:#3b82f6;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapters 4, 5, 6, 9 / สไลด์บรรยาย อ.ประดิษฐ์</div>
      <h3 style="margin-top:4px; color:#1d4ed8;">10. สรุปคุณสมบัติ 2 ประการ และ 3 ประการ ของโครงสร้างข้อมูล (Two &amp; Three Properties)</h3>
      <table style="font-size:13px;">
        <thead>
          <tr style="background:#1d4ed8; color:white;">
            <th>โครงสร้างข้อมูล</th>
            <th>จำนวนคุณสมบัติ</th>
            <th>รายละเอียดคุณสมบัติ (Properties Description)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Binary Min-Heap</strong></td>
            <td><strong>2 Properties</strong></td>
            <td>
              <strong>1. Structure Property:</strong> ต้องเป็น Complete Binary Tree (เติมเต็มทุกชั้น เติมซ้ายไปขวา)<br>
              <strong>2. Heap-Order Property:</strong> ค่าของ Parent ต้องน้อยกว่าหรือเท่ากับ Children เสมอ (Parent &le; Children)
            </td>
          </tr>
          <tr>
            <td><strong>Tree (ในทางทฤษฎีกราฟ)</strong></td>
            <td><strong>2 Properties</strong></td>
            <td>
              <strong>1. Connected:</strong> กราฟต้องเชื่อมโยงถึงกันทุกโหนด<br>
              <strong>2. Acyclic:</strong> กราฟต้องไม่มีวงรอบเด็ดขาด (มี $V-1$ เส้นเชื่อมเสมอ)
            </td>
          </tr>
          <tr>
            <td><strong>AVL Tree</strong></td>
            <td><strong>2 Properties</strong></td>
            <td>
              <strong>1. BST Property:</strong> Left &lt; Root &lt; Right<br>
              <strong>2. Balance Property:</strong> ผลต่างความสูงสองฝั่ง $|h_L - h_R| \le 1$ ทุกโหนด
            </td>
          </tr>
          <tr>
            <td><strong>Hashing (ในอุดมคติ)</strong></td>
            <td><strong>3 Properties</strong></td>
            <td>
              <strong>1. Deterministic &amp; Fast ($O(1)$):</strong> คำนวณง่าย รวดเร็ว ค่าเดิมได้ผลเดิมเสมอ<br>
              <strong>2. Uniform Distribution:</strong> กระจายคีย์ทั่วทุกช่องในตารางอย่างสม่ำเสมอ<br>
              <strong>3. Collision-Free (One-to-One):</strong> ข้อมูลต่างกันต้องได้ดัชนีไม่ซ้ำกันเลย (เป็นไปไม่ได้จริงในทางปฏิบัติเพราะ Pigeonhole Principle)
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 11. 12 ZERO-SCORE TRAPS MATRIX -->
    <div id="th-12traps" class="theory-box" style="border-left-color:#dc2626; background:#fff5f5;">
      <h3 style="margin-top:4px; color:#991b1b; display:flex; align-items:center; gap:8px;">
        🚨 ตารางวิเคราะห์ 12 กับดักร้ายแรงที่ทำให้ได้ 0 คะแนน (Zero-Score Traps Cheat Sheet)
      </h3>
      <p style="font-size:13.5px; color:#7f1d1d; margin-bottom:12px;">
        คัดกรองจากลายมือตรวจข้อสอบจริงและจุดตัดคะแนนของ รศ.ดร.ประดิษฐ์ พิทักษ์เสถียรกุล ทุกจุดหากตอบผิดแม้แต่นิดเดียว อาจารย์จะขีดกากบาทสีแดงและให้ 0 คะแนนทันทีทั้งข้อ
      </p>

      <table style="font-size:12px;">
        <thead>
          <tr style="background:#991b1b; color:white;">
            <th style="width:40px; text-align:center;">ลำดับ</th>
            <th style="width:130px;">หัวข้อโจทย์</th>
            <th style="width:230px;">ข้อผิดพลาดยอดฮิต (ได้ 0 คะแนน!)</th>
            <th style="width:230px;">คำตอบที่ถูกต้องตามมาตรฐาน (ได้คะแนนเต็ม)</th>
            <th>สาเหตุที่ อ.ประดิษฐ์ หักเหลือ 0 และข้อควรระวัง</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="text-align:center; font-weight:bold;">1</td>
            <td><strong>Python Hash Table vs C++ Struct</strong></td>
            <td style="color:#dc2626; font-weight:bold;">นำโครงสร้าง C++ รุ่นเก่า (Struct HashEntry ที่มี element และ info: 'A') มาใส่ในคำตอบวิชาภาษา Python</td>
            <td style="color:#15803d; font-weight:bold;">ในหลักสูตร Python 2569 ของ อ.ประดิษฐ์ ตารางแฮชคือ 1D List <code>[None] * TableSize</code> ช่องว่างเก็บ <code>None</code> ช่องที่มีข้อมูลเก็บตัวเลข Key นั้นตรงๆ โดยไม่มีแถว Info</td>
            <td>วิชาที่เรียนและสอบในปีการศึกษา 2569 คือภาษา Python ไม่มีการใช้ struct info เหมือน C++ ยุคปี 2564 ตารางแฮชจึงมีเพียงแถวดัชนีและแถวข้อมูล (Key) เท่านั้น</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">2</td>
            <td><strong>การเลือกค่า R</strong></td>
            <td style="color:#dc2626; font-weight:bold;">เลือก $R = 11$ เมื่อ TableSize = 11 หรือเลือก $R = 9$</td>
            <td style="color:#15803d; font-weight:bold;">เลือก $R = 7$ (จำนวนเฉพาะที่มากที่สุดที่ <strong>น้อยกว่า</strong> TableSize)</td>
            <td>ถ้า $R = \text{TableSize}$ เมื่อ mod $R$ จะได้ 0 ทำให้ค่าก้าวเดิน $hash_2 = 0$ วนลูปไม่รู้จบ!</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">3</td>
            <td><strong>นิยาม Wrap Around</strong></td>
            <td style="color:#dc2626; font-weight:bold;">ตอบสั้นๆ ว่า "วนกลับ" หรือ "หมุนเป็นวงกลม" โดยไม่มี mod tablesize</td>
            <td style="color:#15803d; font-weight:bold;">เขียนประโยค: <em>"When key was mapped to last index, it go back to first index by mod tablesize one more time"</em></td>
            <td>อาจารย์ตรวจคีย์เวิร์ดภาษาอังกฤษ <strong>mod tablesize</strong> หากไม่มีถือว่าไม่เข้าใจกลไกคณิตศาสตร์</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">4</td>
            <td><strong>New TableSize</strong></td>
            <td style="color:#dc2626; font-weight:bold;">ตอบ $2 \times \text{OldSize}$ เช่น Old=7 ตอบ 14, Old=19 ตอบ 38</td>
            <td style="color:#15803d; font-weight:bold;">Old=7 ตอบ <strong>17</strong>, Old=10 ตอบ <strong>23</strong>, Old=19 ตอบ <strong>41</strong></td>
            <td>ต้องเป็น <strong>Prime Number</strong> ที่น้อยที่สุดที่ $\ge 2 \times \text{OldSize}$ เสมอ</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">5</td>
            <td><strong>Rehash Threshold %</strong></td>
            <td style="color:#dc2626; font-weight:bold;">นับจำนวนคีย์ผิด หรือคิดว่า Rehash เมื่อ $\ge 80\%$ แทนที่จะเป็น strictly $&gt; 80\%$</td>
            <td style="color:#15803d; font-weight:bold;">$19 \times 0.8 = 15.2 \implies$ ต้องการ 16 ตัว ใส่เพิ่มอีก <strong>8 ตัว</strong></td>
            <td>คำว่า "มากกว่า 80%" หมายถึง $N &gt; 15.2$ ดังนั้นที่ 15 ตัวยังไม่ Rehash ต้องเป็นตัวที่ 16</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">6</td>
            <td><strong>Heap Array [0]</strong></td>
            <td style="color:#dc2626; font-weight:bold;">ใส่ Root ไว้ที่ช่อง <code>array[0]</code></td>
            <td style="color:#15803d; font-weight:bold;">เว้นช่อง <code>array[0]</code> ว่างไว้ (หรือใส่ Sentinel $-\infty$) และใส่ Root ที่ <code>array[1]</code></td>
            <td>ถ้า Root อยู่ที่ช่อง 0 สูตร $2i$ และ $2i+1$ จะพังทันที ($2 \times 0 = 0$)</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">7</td>
            <td><strong>ไวยากรณ์ deleteMin</strong></td>
            <td style="color:#dc2626; font-weight:bold;">เขียน <code>myheap.deleteMin(x)</code> หรือ <code>del_min()</code></td>
            <td style="color:#15803d; font-weight:bold;">เขียน <code>myheap.deleteMin()</code> (ไม่มี argument)</td>
            <td>ฟังก์ชัน <code>deleteMin()</code> ลบค่าที่น้อยที่สุด (Root) เสมอ ไม่จำเป็นต้องส่งค่าใดๆ เข้าไป</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">8</td>
            <td><strong>การเขียนวิถีเดิน Graph</strong></td>
            <td style="color:#dc2626; font-weight:bold;">เขียนลูกศร เช่น <code>1 -&gt; 4 -&gt; 5</code></td>
            <td style="color:#15803d; font-weight:bold;">เขียนคั่นด้วยเครื่องหมาย Comma เท่านั้น เช่น <strong><code>1, 4, 5</code></strong></td>
            <td>ในเฉลยข้อสอบปี 2564 อ.ประดิษฐ์ หักคะแนนผู้ที่เขียนลูกศรทั้งหมด ต้องเขียนคั่นด้วย comma</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">9</td>
            <td><strong>Topological Order</strong></td>
            <td style="color:#dc2626; font-weight:bold;">หยิบโหนดที่มี indegree &gt; 0 หรือเขียนลำดับโดยไม่มีตาราง trace Indegree</td>
            <td style="color:#15803d; font-weight:bold;">แสดงตารางลดค่า Indegree ทุกรอบ และเอาโหนดที่ Indegree เป็น 0 เข้า Queue</td>
            <td>Topological Sort ต้องใช้กับ Directed Acyclic Graph (DAG) เท่านั้น และต้องลด indegree ทีละรอบ</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">10</td>
            <td><strong>จำนวนโหนด Tree</strong></td>
            <td style="color:#dc2626; font-weight:bold;">ตอบติดเลขยกกำลัง เช่น $2^{10}$ หรือ $2^{16}$</td>
            <td style="color:#15803d; font-weight:bold;">คำนวณออกมาเป็นตัวเลขจำนวนเต็ม: <strong>1,024</strong> และ <strong>65,536</strong></td>
            <td>โจทย์กำหนดชัดเจนว่า "ตอบเป็นจำนวนเต็มเท่านั้น ห้ามติดเลขยกกำลัง" ติดสูตรได้ 0 คะแนน</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">11</td>
            <td><strong>จำนวนเส้นเชื่อม Graph</strong></td>
            <td style="color:#dc2626; font-weight:bold;">ตอบติดรูปสูตร $\frac{10(9)}{2}$ หรือ $\frac{16(15)}{2}$</td>
            <td style="color:#15803d; font-weight:bold;">ตอบตัวเลขผลลัพธ์สุทธิ: <strong>45 เส้น</strong> และ <strong>120 เส้น</strong></td>
            <td>เช่นเดียวกับข้อ 10 การตอบติดรูปสูตรแสดงว่าไม่ได้ใช้เครื่องคิดเลขคำนวณ ได้ 0 คะแนน</td>
          </tr>
          <tr>
            <td style="text-align:center; font-weight:bold;">12</td>
            <td><strong>Bubble Inversions</strong></td>
            <td style="color:#dc2626; font-weight:bold;">นับจำนวนครั้งการวน Loop (Passes) แทนจำนวนครั้งการสลับที่ (Swaps)</td>
            <td style="color:#15803d; font-weight:bold;">นับจำนวนครั้งที่เกิดการสลับข้อมูลจริง ซึ่งมีค่าเท่ากับ <strong>Inversions</strong> เสมอ</td>
            <td>อาจารย์ถามจำนวน Inversion หรือ Swaps ซึ่งต้องเท่ากับจำนวนคู่ที่เรียงสลับลำดับกัน</td>
          </tr>
        </tbody>
      </table>
    </div>

      <!-- 12. CLASSROOM WORKSHEETS DEEP DIVE -->
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

    <!-- 13. PRIME NUMBERS & REHASHING/R MATRIX -->
    <div id="th-primes" class="theory-box" style="border-left-color:#10b981; background:#f0fdf4;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (Hashing &amp; Rehashing) / ตารางจำนวนเฉพาะสำหรับเปิดห้องสอบ Open Book</div>
      <h3 style="margin-top:4px; color:#065f46; display:flex; align-items:center; gap:8px;">
        🔢 13. ตารางจำนวนเฉพาะ (Prime Numbers Quick Cheatsheet 1–1,000) &amp; กฎการเลือก TableSize / ค่า R
      </h3>
      <p style="font-size:13.5px; color:#166534; margin-bottom:12px;">
        คลังข้อมูลจำนวนเฉพาะทั้งหมด 168 จำนวน (ช่วง 1 ถึง 1,000) สำหรับเปิดใช้ในห้องสอบ Open Book ทันทีเมื่อต้องหา <strong>ขนาดตารางใหม่ในการ Rehash ($\text{Next Prime} \ge 2 \times \text{TableSize}$)</strong> และ <strong>ค่าคงที่ $R$ ใน Double Hashing (จำนวนเฉพาะที่มากที่สุดที่ $R < \text{TableSize}$)</strong>:
      </p>

      <div style="background:#ffffff; border:1px solid #bbf7d0; border-radius:8px; padding:14px; margin-bottom:15px;">
        <h4 style="margin:0 0 8px 0; color:#15803d; font-size:14.5px;">⚡ ตารางสำเร็จรูปจับคู่ Rehashing TableSize &amp; Double Hashing ค่า R (ที่ออกสอบบ่อยที่สุด):</h4>
        <table class="blank-table" style="font-size:12.5px;">
          <tr style="background:#15803d; color:#ffffff;">
            <th>ขนาดตารางเดิม ($M$)</th>
            <th>$2 \times M$</th>
            <th>ขนาดตารางใหม่ (Rehashing New Prime)</th>
            <th>ค่าคงที่ $R$ ใน Double Hashing ($R < M$)</th>
            <th>ข้อควรระวัง &amp; จุดดัก 0 คะแนน</th>
          </tr>
          <tr><td><strong>5</strong></td><td>10</td><td style="color:#15803d; font-weight:bold;">11</td><td style="color:#2563eb; font-weight:bold;">3</td><td>11 เป็นจำนวนเฉพาะถัดไป &ge; 10</td></tr>
          <tr style="background:#f8fafc;"><td><strong>7</strong></td><td>14</td><td style="color:#15803d; font-weight:bold;">17</td><td style="color:#2563eb; font-weight:bold;">5</td><td><strong>ออกสอบบ่อยสุดในสไลด์!</strong> $2 \times 7 = 14 \implies 17$</td></tr>
          <tr><td><strong>10</strong></td><td>20</td><td style="color:#15803d; font-weight:bold;">23</td><td style="color:#2563eb; font-weight:bold;">7</td><td>10 ไม่ใช่ Prime; $R=7$ (จำนวนเฉพาะมากสุดที่ &lt; 10)</td></tr>
          <tr style="background:#fef2f2;"><td><strong>11</strong></td><td>22</td><td style="color:#15803d; font-weight:bold;">23</td><td style="color:#dc2626; font-weight:bold;">7 (🚨 ห้ามตอบ 11!)</td><td><strong>กับดักยอดฮิต:</strong> $R$ ต้อง <em>strictly less than</em> $M$ ดังนั้น $R=7$ ไม่ใช่ 11</td></tr>
          <tr><td><strong>13</strong></td><td>26</td><td style="color:#15803d; font-weight:bold;">29</td><td style="color:#2563eb; font-weight:bold;">11</td><td>$2 \times 13 = 26 \implies 29$; $R = 11$</td></tr>
          <tr style="background:#f8fafc;"><td><strong>17</strong></td><td>34</td><td style="color:#15803d; font-weight:bold;">37</td><td style="color:#2563eb; font-weight:bold;">13</td><td>$2 \times 17 = 34 \implies 37$; $R = 13$</td></tr>
          <tr><td><strong>19</strong></td><td>38</td><td style="color:#15803d; font-weight:bold;">41</td><td style="color:#2563eb; font-weight:bold;">17</td><td><strong>โจทย์ Tab 1 ข้อ 1.1!</strong> $R = 17$</td></tr>
          <tr style="background:#f8fafc;"><td><strong>23</strong></td><td>46</td><td style="color:#15803d; font-weight:bold;">47</td><td style="color:#2563eb; font-weight:bold;">19</td><td>$2 \times 23 = 46 \implies 47$; $R = 19$</td></tr>
          <tr><td><strong>31</strong></td><td>62</td><td style="color:#15803d; font-weight:bold;">67</td><td style="color:#2563eb; font-weight:bold;">29</td><td>$2 \times 31 = 62 \implies 67$; $R = 29$</td></tr>
          <tr style="background:#f8fafc;"><td><strong>37</strong></td><td>74</td><td style="color:#15803d; font-weight:bold;">79</td><td style="color:#2563eb; font-weight:bold;">31</td><td>$2 \times 37 = 74 \implies 79$; $R = 31$</td></tr>
          <tr><td><strong>47</strong></td><td>94</td><td style="color:#15803d; font-weight:bold;">97</td><td style="color:#2563eb; font-weight:bold;">43</td><td>$2 \times 47 = 94 \implies 97$; $R = 43$</td></tr>
        </table>
      </div>

      <h4 style="margin:12px 0 6px 0; color:#166534; font-size:14px;">📋 บัญชีจำนวนเฉพาะทั้งหมด 168 ตัว (1 ถึง 1,000) จัดหมวดหมู่เพื่อการค้นหาเร็ว:</h4>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:10px; font-family:'JetBrains Mono', Consolas, monospace; font-size:12px;">
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">1 – 100 (25 ตัว)</div>
          2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">101 – 200 (21 ตัว)</div>
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">201 – 300 (16 ตัว)</div>
          211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">301 – 400 (16 ตัว)</div>
          307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">401 – 500 (17 ตัว)</div>
          401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">501 – 600 (14 ตัว)</div>
          503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">601 – 700 (16 ตัว)</div>
          601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">701 – 800 (14 ตัว)</div>
          701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">801 – 900 (15 ตัว)</div>
          809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887
        </div>
        <div style="background:#ffffff; padding:10px; border-radius:6px; border:1px solid #cbd5e1;">
          <div style="font-weight:bold; color:#1e40af; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:4px;">901 – 1,000 (14 ตัว)</div>
          907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
        </div>
      </div>
    </div>

    <!-- 14. COMPLETE ASCII TABLE & STRING HASHING -->
    <div id="th-ascii" class="theory-box" style="border-left-color:#8b5cf6; background:#faf5ff;">
      <div class="ref-tag">📖 อ้างอิง: Weiss Chapter 5 (String Hashing) / สไลด์การแฮชสตริง อ.ประดิษฐ์ &amp; ข้อสอบเก่าปี 2561</div>
      <h3 style="margin-top:4px; color:#5b21b6; display:flex; align-items:center; gap:8px;">
        🔤 14. ตารางรหัส ASCII ฉบับสมบูรณ์ (Complete ASCII Table 0–127) สำหรับ String Hashing &amp; Character Math
      </h3>
      <p style="font-size:13.5px; color:#6b21a8; margin-bottom:12px;">
        รหัส ASCII มาตรฐาน 0–127 สำหรับคำนวณ Hash Function ของคีย์ที่เป็นตัวอักษรและสตริง พร้อมตัวอย่างสูตรคำนวณที่ออกสอบจริง:
      </p>

      <!-- QUICK HIGHLIGHT BOX -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(230px, 1fr)); gap:10px; margin-bottom:15px;">
        <div style="background:#ffffff; border:2px solid #8b5cf6; border-radius:8px; padding:10px;">
          <div style="font-weight:bold; color:#5b21b6; font-size:13.5px;">🔢 ตัวเลข (Digits '0' – '9')</div>
          <div style="font-size:13px; font-family:'JetBrains Mono', Consolas, monospace; color:#1e293b; margin-top:4px;">
            <strong>'0' = 48</strong> (0x30) &bull; <strong>'1' = 49</strong><br>
            <strong>'5' = 53</strong> &bull; <strong>'9' = 57</strong> (0x39)
          </div>
          <div style="font-size:11.5px; color:#64748b; margin-top:3px;">สูตรแปลง: <code>int = ord(c) - 48</code></div>
        </div>

        <div style="background:#ffffff; border:2px solid #2563eb; border-radius:8px; padding:10px;">
          <div style="font-weight:bold; color:#1d4ed8; font-size:13.5px;">🔠 ตัวพิมพ์ใหญ่ ('A' – 'Z')</div>
          <div style="font-size:13px; font-family:'JetBrains Mono', Consolas, monospace; color:#1e293b; margin-top:4px;">
            <strong>'A' = 65</strong> (0x41) &bull; <strong>'B' = 66</strong> &bull; <strong>'C' = 67</strong><br>
            <strong>'M' = 77</strong> &bull; <strong>'Z' = 90</strong> (0x5A)
          </div>
          <div style="font-size:11.5px; color:#64748b; margin-top:3px;">ลำดับในภาษาอังกฤษ: <code>ord(c) - 64</code></div>
        </div>

        <div style="background:#ffffff; border:2px solid #059669; border-radius:8px; padding:10px;">
          <div style="font-weight:bold; color:#047857; font-size:13.5px;">🔡 ตัวพิมพ์เล็ก ('a' – 'z')</div>
          <div style="font-size:13px; font-family:'JetBrains Mono', Consolas, monospace; color:#1e293b; margin-top:4px;">
            <strong>'a' = 97</strong> (0x61) &bull; <strong>'b' = 98</strong> &bull; <strong>'c' = 99</strong><br>
            <strong>'m' = 109</strong> &bull; <strong>'z' = 122</strong> (0x7A)
          </div>
          <div style="font-size:11.5px; color:#64748b; margin-top:3px;">⚡ <strong>ต่างจากตัวใหญ่ 32:</strong> <code>ord('a') - ord('A') = 32</code></div>
        </div>

        <div style="background:#ffffff; border:2px solid #d97706; border-radius:8px; padding:10px;">
          <div style="font-weight:bold; color:#b45309; font-size:13.5px;">⭐ อักขระพิเศษสำคัญ</div>
          <div style="font-size:13px; font-family:'JetBrains Mono', Consolas, monospace; color:#1e293b; margin-top:4px;">
            <strong>Space = 32</strong> &bull; <strong>'+' = 43</strong> &bull; <strong>'-' = 45</strong><br>
            <strong>'*' = 42</strong> &bull; <strong>'/' = 47</strong> &bull; <strong>'_' = 95</strong>
          </div>
          <div style="font-size:11.5px; color:#64748b; margin-top:3px;">Null = 0, Enter/LF = 10, CR = 13</div>
        </div>
      </div>

      <!-- STRING HASHING EXAMPLES -->
      <div style="background:#ffffff; border:1px solid #ddd6fe; border-radius:8px; padding:12px; margin-bottom:15px;">
        <h4 style="margin:0 0 6px 0; color:#5b21b6; font-size:14px;">🧮 ตัวอย่างการคำนวณ String Hashing ในข้อสอบจริง:</h4>
        <div style="font-size:13px; line-height:1.7;">
          <p style="margin:4px 0;"><strong>สูตรที่ 1 (ผลบวก ASCII ธรรมดา - Simple ASCII Sum):</strong></p>
          $$\text{hash}(s) = \left( \sum_{i=0}^{k-1} \text{ASCII}(s[i]) \right) \bmod \text{TableSize}$$
          <ul>
            <li>คำนวณคีย์ <code>"CAT"</code> สำหรับตารางขนาด 11 ($M=11$):
              <br>$\text{ASCII}('C') = 67, \quad \text{ASCII}('A') = 65, \quad \text{ASCII}('T') = 84$
              <br>$\text{Sum} = 67 + 65 + 84 = \mathbf{216}$
              <br>$\text{hash}("CAT") = 216 \bmod 11 = \mathbf{7}$ &rarr; <strong>ตกช่องดัชนี 7</strong>
            </li>
            <li>คำนวณคีย์ <code>"DOG"</code> สำหรับตารางขนาด 11 ($M=11$):
              <br>$\text{ASCII}('D') = 68, \quad \text{ASCII}('O') = 79, \quad \text{ASCII}('G') = 71$
              <br>$\text{Sum} = 68 + 79 + 71 = \mathbf{218}$
              <br>$\text{hash}("DOG") = 218 \bmod 11 = \mathbf{9}$ &rarr; <strong>ตกช่องดัชนี 9</strong>
            </li>
          </ul>
          <p style="margin:6px 0 2px 0;"><strong>สูตรที่ 2 (Polynomial Hash ในตำรา Weiss):</strong></p>
          $$\text{hash}(s) = (s[0] + s[1] \cdot 32 + s[2] \cdot 32^2) \bmod \text{TableSize}$$
        </div>
      </div>

      <!-- COMPLETE ASCII TABLE (0 - 127) IN 4 COLUMNS -->
      <h4 style="margin:10px 0 6px 0; color:#5b21b6; font-size:14px;">📋 ตารางรหัส ASCII มาตรฐาน 0 ถึง 127 ฉบับเต็ม (Full ASCII Table):</h4>
      <div style="overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; font-size:11.5px; font-family:'JetBrains Mono', Consolas, monospace; text-align:center; border:1px solid #cbd5e1;">
          <thead>
            <tr style="background:#5b21b6; color:#ffffff;">
              <th style="padding:4px; border:1px solid #7c3aed;">Dec</th><th style="padding:4px; border:1px solid #7c3aed;">Hex</th><th style="padding:4px; border:1px solid #7c3aed;">Char</th>
              <th style="padding:4px; border:1px solid #7c3aed;">Dec</th><th style="padding:4px; border:1px solid #7c3aed;">Hex</th><th style="padding:4px; border:1px solid #7c3aed;">Char</th>
              <th style="padding:4px; border:1px solid #7c3aed;">Dec</th><th style="padding:4px; border:1px solid #7c3aed;">Hex</th><th style="padding:4px; border:1px solid #7c3aed;">Char</th>
              <th style="padding:4px; border:1px solid #7c3aed;">Dec</th><th style="padding:4px; border:1px solid #7c3aed;">Hex</th><th style="padding:4px; border:1px solid #7c3aed;">Char</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>0</td><td>00</td><td>NUL</td><td>32</td><td>20</td><td>[Space]</td><td>64</td><td>40</td><td>@</td><td>96</td><td>60</td><td>`</td></tr>
            <tr style="background:#f8fafc;"><td>1</td><td>01</td><td>SOH</td><td>33</td><td>21</td><td>!</td><td>65</td><td>41</td><td><strong>A</strong></td><td>97</td><td>61</td><td><strong>a</strong></td></tr>
            <tr><td>2</td><td>02</td><td>STX</td><td>34</td><td>22</td><td>"</td><td>66</td><td>42</td><td><strong>B</strong></td><td>98</td><td>62</td><td><strong>b</strong></td></tr>
            <tr style="background:#f8fafc;"><td>3</td><td>03</td><td>ETX</td><td>35</td><td>23</td><td>#</td><td>67</td><td>43</td><td><strong>C</strong></td><td>99</td><td>63</td><td><strong>c</strong></td></tr>
            <tr><td>4</td><td>04</td><td>EOT</td><td>36</td><td>24</td><td>$</td><td>68</td><td>44</td><td><strong>D</strong></td><td>100</td><td>64</td><td><strong>d</strong></td></tr>
            <tr style="background:#f8fafc;"><td>5</td><td>05</td><td>ENQ</td><td>37</td><td>25</td><td>%</td><td>69</td><td>45</td><td><strong>E</strong></td><td>101</td><td>65</td><td><strong>e</strong></td></tr>
            <tr><td>6</td><td>06</td><td>ACK</td><td>38</td><td>26</td><td>&amp;</td><td>70</td><td>46</td><td><strong>F</strong></td><td>102</td><td>66</td><td><strong>f</strong></td></tr>
            <tr style="background:#f8fafc;"><td>7</td><td>07</td><td>BEL</td><td>39</td><td>27</td><td>'</td><td>71</td><td>47</td><td><strong>G</strong></td><td>103</td><td>67</td><td><strong>g</strong></td></tr>
            <tr><td>8</td><td>08</td><td>BS</td><td>40</td><td>28</td><td>(</td><td>72</td><td>48</td><td><strong>H</strong></td><td>104</td><td>68</td><td><strong>h</strong></td></tr>
            <tr style="background:#f8fafc;"><td>9</td><td>09</td><td>HT</td><td>41</td><td>29</td><td>)</td><td>73</td><td>49</td><td><strong>I</strong></td><td>105</td><td>69</td><td><strong>i</strong></td></tr>
            <tr><td>10</td><td>0A</td><td>LF</td><td>42</td><td>2A</td><td>*</td><td>74</td><td>4A</td><td><strong>J</strong></td><td>106</td><td>6A</td><td><strong>j</strong></td></tr>
            <tr style="background:#f8fafc;"><td>11</td><td>0B</td><td>VT</td><td>43</td><td>2B</td><td>+</td><td>75</td><td>4B</td><td><strong>K</strong></td><td>107</td><td>6B</td><td><strong>k</strong></td></tr>
            <tr><td>12</td><td>0C</td><td>FF</td><td>44</td><td>2C</td><td>,</td><td>76</td><td>4C</td><td><strong>L</strong></td><td>108</td><td>6C</td><td><strong>l</strong></td></tr>
            <tr style="background:#f8fafc;"><td>13</td><td>0D</td><td>CR</td><td>45</td><td>2D</td><td>-</td><td>77</td><td>4D</td><td><strong>M</strong></td><td>109</td><td>6D</td><td><strong>m</strong></td></tr>
            <tr><td>14</td><td>0E</td><td>SO</td><td>46</td><td>2E</td><td>.</td><td>78</td><td>4E</td><td><strong>N</strong></td><td>110</td><td>6E</td><td><strong>n</strong></td></tr>
            <tr style="background:#f8fafc;"><td>15</td><td>0F</td><td>SI</td><td>47</td><td>2F</td><td>/</td><td>79</td><td>4F</td><td><strong>O</strong></td><td>111</td><td>6F</td><td><strong>o</strong></td></tr>
            <tr><td>16</td><td>10</td><td>DLE</td><td>48</td><td>30</td><td><strong>0</strong></td><td>80</td><td>50</td><td><strong>P</strong></td><td>112</td><td>70</td><td><strong>p</strong></td></tr>
            <tr style="background:#f8fafc;"><td>17</td><td>11</td><td>DC1</td><td>49</td><td>31</td><td><strong>1</strong></td><td>81</td><td>51</td><td><strong>Q</strong></td><td>113</td><td>71</td><td><strong>q</strong></td></tr>
            <tr><td>18</td><td>12</td><td>DC2</td><td>50</td><td>32</td><td><strong>2</strong></td><td>82</td><td>52</td><td><strong>R</strong></td><td>114</td><td>72</td><td><strong>r</strong></td></tr>
            <tr style="background:#f8fafc;"><td>19</td><td>13</td><td>DC3</td><td>51</td><td>33</td><td><strong>3</strong></td><td>83</td><td>53</td><td><strong>S</strong></td><td>115</td><td>73</td><td><strong>s</strong></td></tr>
            <tr><td>20</td><td>14</td><td>DC4</td><td>52</td><td>34</td><td><strong>4</strong></td><td>84</td><td>54</td><td><strong>T</strong></td><td>116</td><td>74</td><td><strong>t</strong></td></tr>
            <tr style="background:#f8fafc;"><td>21</td><td>15</td><td>NAK</td><td>53</td><td>35</td><td><strong>5</strong></td><td>85</td><td>55</td><td><strong>U</strong></td><td>117</td><td>75</td><td><strong>u</strong></td></tr>
            <tr><td>22</td><td>16</td><td>SYN</td><td>54</td><td>36</td><td><strong>6</strong></td><td>86</td><td>56</td><td><strong>V</strong></td><td>118</td><td>76</td><td><strong>v</strong></td></tr>
            <tr style="background:#f8fafc;"><td>23</td><td>17</td><td>ETB</td><td>55</td><td>37</td><td><strong>7</strong></td><td>87</td><td>57</td><td><strong>W</strong></td><td>119</td><td>77</td><td><strong>w</strong></td></tr>
            <tr><td>24</td><td>18</td><td>CAN</td><td>56</td><td>38</td><td><strong>8</strong></td><td>88</td><td>58</td><td><strong>X</strong></td><td>120</td><td>78</td><td><strong>x</strong></td></tr>
            <tr style="background:#f8fafc;"><td>25</td><td>19</td><td>EM</td><td>57</td><td>39</td><td><strong>9</strong></td><td>89</td><td>59</td><td><strong>Y</strong></td><td>121</td><td>79</td><td><strong>y</strong></td></tr>
            <tr><td>26</td><td>1A</td><td>SUB</td><td>58</td><td>3A</td><td>:</td><td>90</td><td>5A</td><td><strong>Z</strong></td><td>122</td><td>7A</td><td><strong>z</strong></td></tr>
            <tr style="background:#f8fafc;"><td>27</td><td>1B</td><td>ESC</td><td>59</td><td>3B</td><td>;</td><td>91</td><td>5B</td><td>[</td><td>123</td><td>7B</td><td>{</td></tr>
            <tr><td>28</td><td>1C</td><td>FS</td><td>60</td><td>3C</td><td>&lt;</td><td>92</td><td>5C</td><td>\</td><td>124</td><td>7C</td><td>|</td></tr>
            <tr style="background:#f8fafc;"><td>29</td><td>1D</td><td>GS</td><td>61</td><td>3D</td><td>=</td><td>93</td><td>5D</td><td>]</td><td>125</td><td>7D</td><td>}</td></tr>
            <tr><td>30</td><td>1E</td><td>RS</td><td>62</td><td>3E</td><td>&gt;</td><td>94</td><td>5E</td><td>^</td><td>126</td><td>7E</td><td>~</td></tr>
            <tr style="background:#f8fafc;"><td>31</td><td>1F</td><td>US</td><td>63</td><td>3F</td><td>?</td><td>95</td><td>5F</td><td>_</td><td>127</td><td>7F</td><td>DEL</td></tr>
          </tbody>
        </table>
      </div>
    </div>

  </div> <!-- END TAB 3 -->
"""

if __name__ == "__main__":
    print("generate_tab3.py generated successfully!")
