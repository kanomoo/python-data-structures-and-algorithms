# -*- coding: utf-8 -*-
"""
Script to add Section 13 (Prime Numbers Table 1-1,000 & Rehashing/R Matrix)
and Section 14 (Complete ASCII Table 0-127 & String Hashing Methods)
to generate_tab3.py
"""

import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab3.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update quick jump nav in tab3
old_nav = r"""      <a href="#th-worksheets" class="jump-pill alt">🎯 12. ถอดรหัสใบงานจริง 2569</a>
      <a href="#th-12traps" class="jump-pill danger">🚨 ตาราง 12 กับดัก 0 คะแนน</a>
    </div>"""

new_nav = r"""      <a href="#th-12traps" class="jump-pill danger">🚨 ตาราง 12 กับดัก 0 คะแนน</a>
      <a href="#th-worksheets" class="jump-pill alt">🎯 12. ถอดรหัสใบงานจริง 2569</a>
      <a href="#th-primes" class="jump-pill" style="border-color:#10b981; color:#065f46; background:#ecfdf5;">🔢 13. ตารางจำนวนเฉพาะ &amp; ค่า R</a>
      <a href="#th-ascii" class="jump-pill" style="border-color:#8b5cf6; color:#5b21b6; background:#f5f3ff;">🔤 14. ตารางรหัส ASCII (0–127)</a>
    </div>"""

if old_nav in text:
    text = text.replace(old_nav, new_nav)
    print("Quick nav updated with Sections 13 and 14!")
else:
    print("Warning: old_nav pattern not found in generate_tab3.py")

# 2. Prepare Section 13 and 14 HTML
prime_ascii_html = r"""
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
"""

# Insert Section 13 and 14 before </div> <!-- END TAB 3 -->
marker = r"""  </div> <!-- END TAB 3 -->"""
if marker in text:
    text = text.replace(marker, prime_ascii_html + "\n  </div> <!-- END TAB 3 -->")
    print("Section 13 and 14 injected into generate_tab3.py successfully!")
else:
    print("Error: marker '</div> <!-- END TAB 3 -->' not found in generate_tab3.py")

with open(r"C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\scripts\generate_tab3.py", "w", encoding="utf-8") as f:
    f.write(text)

print(f"generate_tab3.py updated! File length: {len(text)} chars")
