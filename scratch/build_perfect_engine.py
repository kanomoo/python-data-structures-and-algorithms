# -*- coding: utf-8 -*-
"""
Builds the perfect visualizer engine for all 48 diagrams
"""
import sys, io, json, re

def build():
    # Model templates for the newly refined diagrams
    
    # 5. Python Memory Reference Model (Chapter 02.1 - Diagram 1)
    py_ref_html = r'''
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 60px 1.4fr 60px 1fr;gap:12px;align-items:center;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;">Variable: a</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#94a3b8;font-size:12px;margin-top:4px;">Reference Pointer</div>
                <div style="color:#38bdf8;font-size:11px;font-family:'JetBrains Mono',monospace;margin-top:6px;">➔ 0x7f8a</div>
              </div>
              <div style="text-align:center;font-size:24px;color:#38bdf8;">➔</div>
              <div style="background:#181a26;border:2px solid #10b981;border-radius:12px;padding:18px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#10b981;font-weight:700;font-size:16px;">PyList Object in Heap</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#34d399;font-size:11.5px;margin-bottom:10px;">Memory Address: 0x7f8a</div>
                <div style="display:flex;gap:8px;justify-content:center;align-items:center;">
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#10b981;"><span class="cell-val">1</span></div>
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#10b981;"><span class="cell-val">2</span></div>
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#10b981;"><span class="cell-val">3</span></div>
                  <div class="dsa-heap-cell" style="padding:8px 14px;border-color:#f59e0b;background:rgba(245,158,11,0.15);"><span class="cell-val" style="color:#fbbf24;">4</span></div>
                </div>
                <div style="font-size:11px;color:#94a3b8;margin-top:8px;font-family:'JetBrains Mono',monospace;">b.append(4) แก้ไขที่อ็อบเจกต์นี้</div>
              </div>
              <div style="text-align:center;font-size:24px;color:#38bdf8;">🠔</div>
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;color:#4fd1e8;font-weight:700;font-size:15px;">Variable: b (b = a)</div>
                <div style="font-family:'JetBrains Mono',monospace;color:#94a3b8;font-size:12px;margin-top:4px;">Reference Pointer</div>
                <div style="color:#38bdf8;font-size:11px;font-family:'JetBrains Mono',monospace;margin-top:6px;">➔ 0x7f8a</div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">💡 Python Reference Rule: ตัวแปร <code>b = a</code> ไม่ได้สร้าง List สำเนาใหม่ แต่แชร์พอยน์เตอร์ชี้ไปที่ Heap Object <code>0x7f8a</code> ตัวเดียวกัน เมื่อสั่ง <code>b.append(4)</code> ตัวแปร <code>a</code> จึงเปลี่ยนเป็น <code>[1, 2, 3, 4]</code> ด้วยทันที!</span>
            </div>
          </div>
    '''

    # 25. Golden BST Rule (Chapter 05.2 - Diagram 1)
    bst_rule_html = r'''
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 560 230" style="width:100%;max-width:560px;">
              ${svgDefs}
              <line x1="280" y1="36" x2="160" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="280" y1="36" x2="400" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="85" x2="100" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="160" y1="85" x2="220" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="100" y1="135" x2="60" y2="185" stroke="#334155" stroke-width="2.5" />
              <line x1="60" y1="185" x2="30" y2="215" stroke="#334155" stroke-width="2.5" />

              <circle cx="280" cy="36" r="22" fill="#181a26" stroke="#f59e0b" stroke-width="3" filter="url(#dsa-glow-amber)" />
              <text x="280" y="41" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="15" text-anchor="middle">6</text>
              <text x="280" y="14" fill="#f59e0b" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">Root</text>

              <circle cx="160" cy="85" r="20" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" filter="url(#dsa-glow-cyan)" />
              <text x="160" y="90" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="14" text-anchor="middle">4</text>
              <text x="160" y="65" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">4 &lt; 6 (ซ้าย)</text>

              <circle cx="400" cy="85" r="20" fill="#181a26" stroke="#10b981" stroke-width="2.2" filter="url(#dsa-glow-emerald)" />
              <text x="400" y="90" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="14" text-anchor="middle">7</text>
              <text x="400" y="65" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9.5" text-anchor="middle">7 &gt; 6 (ขวา)</text>

              <circle cx="100" cy="135" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="100" y="140" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">3</text>
              <text x="100" y="115" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">3 &lt; 4</text>

              <circle cx="220" cy="135" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" />
              <text x="220" y="140" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="13" text-anchor="middle">5</text>
              <text x="220" y="115" fill="#38bdf8" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">5 &gt; 4</text>

              <circle cx="60" cy="185" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" />
              <text x="60" y="189" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="12" text-anchor="middle">2</text>

              <circle cx="30" cy="215" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.5" />
              <text x="30" y="219" fill="#fff" font-family="'Chakra Petch',sans-serif" font-weight="700" font-size="11" text-anchor="middle">1</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🌲 กฎทองคำของ BST: ทุกโหนดในกิ่งซ้ายต้องน้อยกว่า Root (&lt; Root) และทุกโหนดในกิ่งขวาต้องมากกว่า Root (&gt; Root) ตลอดทั้งโครงสร้าง</span>
            </div>
          </div>
    '''

    # 29. BST Deletion Case 1 Leaf Node (Chapter 05.3 - Diagram 2)
    bst_del_case1_html = r'''
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="background:#181a26;border:1px solid #334155;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#f87171;font-size:14px;margin-bottom:8px;">1. ก่อนลบ: โหนด 4 ต้องการลบ (เป้าหมาย)</div>
                <svg viewBox="0 0 260 170" style="width:100%;max-width:260px;">
                  <line x1="130" y1="26" x2="65" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="130" y1="26" x2="195" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="65" y1="70" x2="35" y2="120" stroke="#334155" stroke-width="2" />
                  <line x1="65" y1="70" x2="95" y2="120" stroke="#334155" stroke-width="2" />
                  <circle cx="130" cy="26" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="130" y="30" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">6</text>
                  <circle cx="65" cy="70" r="17" fill="rgba(239,68,68,0.25)" stroke="#ef4444" stroke-width="2.5" /><text x="65" y="74" fill="#fca5a5" font-size="12" font-weight="700" text-anchor="middle">4 ✂️</text>
                  <circle cx="195" cy="70" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="195" y="74" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">7</text>
                  <circle cx="35" cy="120" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="35" y="124" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">3</text>
                  <circle cx="95" cy="120" r="14" fill="#064e3b" stroke="#10b981" stroke-width="2" /><text x="95" y="124" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">5 ⭐</text>
                </svg>
                <div style="font-size:11.5px;color:#94a3b8;margin-top:6px;">Inorder Successor คือ 5 (ค่าน้อยสุดในกิ่งขวา)</div>
              </div>
              <div style="background:#181a26;border:1px solid #10b981;border-radius:10px;padding:16px;text-align:center;">
                <div style="font-family:'Chakra Petch',sans-serif;font-weight:700;color:#34d399;font-size:14px;margin-bottom:8px;">2. หลังลบ: นำ Successor 5 มาแทนตำแหน่ง 4</div>
                <svg viewBox="0 0 260 170" style="width:100%;max-width:260px;">
                  <line x1="130" y1="26" x2="65" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="130" y1="26" x2="195" y2="70" stroke="#334155" stroke-width="2" />
                  <line x1="65" y1="70" x2="35" y2="120" stroke="#334155" stroke-width="2" />
                  <circle cx="130" cy="26" r="16" fill="#181a26" stroke="#f59e0b" stroke-width="2" /><text x="130" y="30" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">6</text>
                  <circle cx="65" cy="70" r="17" fill="#064e3b" stroke="#10b981" stroke-width="2.5" /><text x="65" y="74" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">5</text>
                  <circle cx="195" cy="70" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="195" y="74" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">7</text>
                  <circle cx="35" cy="120" r="14" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="35" y="124" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">3</text>
                </svg>
                <div style="font-size:11.5px;color:#34d399;margin-top:6px;">ก๊อปปี้ค่า 5 มาแทน แล้วลบโหนดใบ 5 เดิมทิ้ง (Case 1)</div>
              </div>
            </div>
          </div>
    '''

    # 30. BST Deletion Case 2 Single Child (Chapter 05.3 - Diagram 3)
    bst_del_case2_html = r'''
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 480 220" style="width:100%;max-width:480px;">
              ${svgDefs}
              <line x1="240" y1="36" x2="150" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="240" y1="36" x2="330" y2="85" stroke="#334155" stroke-width="2.5" />
              <line x1="150" y1="85" x2="100" y2="135" stroke="#334155" stroke-width="2.5" />
              <line x1="150" y1="85" x2="200" y2="135" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 4" />
              <line x1="200" y1="135" x2="160" y2="185" stroke="#334155" stroke-width="2" />
              <!-- Direct Bypass Arrow from 2 to 3 -->
              <path d="M 150 100 Q 130 150 160 175" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" stroke-dasharray="4 4" />

              <circle cx="240" cy="36" r="18" fill="#181a26" stroke="#f59e0b" stroke-width="2.5" /><text x="240" y="41" fill="#fff" font-weight="700" font-size="14" text-anchor="middle">6</text>
              <circle cx="330" cy="85" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2" /><text x="330" y="90" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">8</text>
              <circle cx="150" cy="85" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.5" /><text x="150" y="90" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">2</text>
              <circle cx="100" cy="135" r="16" fill="#181a26" stroke="#4fd1e8" stroke-width="1.8" /><text x="100" y="139" fill="#fff" font-weight="700" font-size="12" text-anchor="middle">1</text>

              <circle cx="200" cy="135" r="18" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="2.5" />
              <text x="200" y="140" fill="#f87171" font-weight="700" font-size="13" text-anchor="middle">4 ✂️</text>

              <circle cx="160" cy="185" r="18" fill="#064e3b" stroke="#10b981" stroke-width="2.5" filter="url(#dsa-glow-emerald)" />
              <text x="160" y="190" fill="#34d399" font-weight="800" font-size="13" text-anchor="middle">3</text>
              <text x="160" y="212" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="9" text-anchor="middle">ลูกเดี่ยว (Bypassed)</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">✂️ Case 2 (Single Child): ลบโหนด 4 ที่มีลูกซ้ายคือ 3 เพียงตัวเดียว ให้พอยน์เตอร์ขวาของโหนด 2 ชี้ข้าม (Bypass) ไปที่โหนด 3 ทันที</span>
            </div>
          </div>
    '''

    # 43. Dijkstra's Algorithm State Machine Flowchart (Chapter 10.1 - Diagram 2)
    dijkstra_flowchart_html = r'''
          <div class="dsa-native-wrap">
            <div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:10px;align-items:stretch;">
              <div style="background:#181a26;border:1.5px solid #4fd1e8;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#4fd1e8;font-weight:700;font-size:13px;margin-bottom:4px;">1. Initialize</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">dist[src]=0<br/>dist[v]=∞<br/>visited=set()<br/>push (0, src) เข้า PQ</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #f59e0b;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#f59e0b;font-weight:700;font-size:13px;margin-bottom:4px;">2. Pop Min</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">ดึงโหนด u ที่มีค่า dist[u] น้อยสุดออกจาก Min-Heap</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #b794f6;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#b794f6;font-weight:700;font-size:13px;margin-bottom:4px;">3. Visited Check</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">ถ้า u เคยแวะแล้ว ➔ ข้าม<br/>ถ้ายังไม่แวะ ➔ เพิ่ม u เข้า visited set</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #10b981;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#10b981;font-weight:700;font-size:13px;margin-bottom:4px;">4. Relaxation</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">สำหรับเพื่อนบ้าน v:<br/>ถ้า dist[u]+w &lt; dist[v]:<br/>dist[v] = dist[u]+w<br/>push (dist[v], v)</div>
              </div>
              <div style="background:#181a26;border:1.5px solid #38bdf8;border-radius:10px;padding:12px;">
                <div style="font-family:'JetBrains Mono',monospace;color:#38bdf8;font-weight:700;font-size:13px;margin-bottom:4px;">5. Terminate</div>
                <div style="font-size:12px;color:#c7cad6;line-height:1.5;">ทำซ้ำจน Priority Queue ว่างเปล่า<br/>ได้ตาราง Shortest Path ครบทุกโหนด</div>
              </div>
            </div>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🗺️ Dijkstra State Machine: ใช้หลักการ Greedy ร่วมกับ Min-Heap ให้ความเร็ว O((V + E) log V) สำหรับกราฟถ่วงน้ำหนักบวกทุกเส้น</span>
            </div>
          </div>
    '''

    # 44. Dijkstra 7-Vertex Graph Model (Chapter 10.1 - Diagram 3)
    dijkstra_7node_html = r'''
          <div class="dsa-native-wrap">
            <svg viewBox="0 0 620 280" style="width:100%;max-width:620px;">
              ${svgDefs}
              <!-- Edges -->
              <line x1="160" y1="60" x2="300" y2="60" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="160" y1="60" x2="230" y2="150" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="300" y1="60" x2="230" y2="150" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="300" y1="60" x2="450" y2="60" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="80" y1="150" x2="160" y2="60" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" />
              <line x1="80" y1="150" x2="230" y2="240" stroke="#10b981" stroke-width="2.5" marker-end="url(#dsa-arrow-emerald)" />
              <line x1="230" y1="150" x2="80" y2="150" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="230" y1="150" x2="230" y2="240" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="230" y1="150" x2="450" y2="60" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="230" y1="150" x2="390" y2="210" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="450" y1="60" x2="390" y2="210" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />
              <line x1="390" y1="210" x2="230" y2="240" stroke="#334155" stroke-width="2" marker-end="url(#dsa-arrow-cyan)" />

              <!-- Vertices -->
              <circle cx="160" cy="60" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="160" y="65" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v1</text>
              <circle cx="300" cy="60" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="300" y="65" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v2</text>
              <circle cx="80" cy="150" r="22" fill="#064e3b" stroke="#10b981" stroke-width="3" filter="url(#dsa-glow-emerald)" /><text x="80" y="155" fill="#fff" font-weight="800" font-size="14" text-anchor="middle">v3</text>
              <text x="80" y="122" fill="#34d399" font-family="'JetBrains Mono',monospace" font-size="10" text-anchor="middle">Start (v3)</text>
              <circle cx="230" cy="150" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="230" y="155" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v4</text>
              <circle cx="450" cy="60" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="450" y="65" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v5</text>
              <circle cx="230" cy="240" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="230" y="245" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v6</text>
              <circle cx="390" cy="210" r="18" fill="#181a26" stroke="#4fd1e8" stroke-width="2.2" /><text x="390" y="215" fill="#fff" font-weight="700" font-size="13" text-anchor="middle">v7</text>
            </svg>
            <div class="dsa-tree-footer">
              <span class="dsa-tree-chip">🗺️ กราฟ 7 โหนดพร้อมเส้นทางเชื่อมต่อ (Start ที่ v3): Dijkstra จะสำรวจเพื่อนบ้าน (v1 และ v6) แล้วอัปเดตระยะทางที่สั้นที่สุดตามลำดับ Priority Queue</span>
            </div>
          </div>
    '''

    print("Templates prepared.")

if __name__ == '__main__':
    build()
