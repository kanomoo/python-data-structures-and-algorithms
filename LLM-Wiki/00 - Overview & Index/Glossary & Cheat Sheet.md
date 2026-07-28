# 📖 Master Glossary & Cheat Sheet (สรุปศัพท์และสูตรสำคัญสำหรับสอบ LLM)

> [!NOTE]
> หน้านี้รวบรวม **คำศัพท์อักษรย่อ (Acronyms)**, **สูตรคณิตศาสตร์สำคัญ** และ **สูตรประมาณการคำนวณหน่วยความจำ (VRAM Estimation Formulas)** ที่มักถูกออกสอบในวิชา Large Language Models และ Natural Language Processing

---

## 🔤 คำศัพท์และอักษรย่อที่ต้องจำ (Key Acronyms)

| อักษรย่อ | ชื่อเต็ม | ความหมายย่อ |
| :--- | :--- | :--- |
| **LLM** | Large Language Model | โมเดลภาษาขนาดใหญ่ที่ถูกเทรนด้วยข้อมูลมหาศาลเพื่อทำนายโทเคนถัดไป |
| **BPE** | Byte-Pair Encoding | อัลกอริทึม Subword Tokenization ที่รวมคู่ตัวอักษรที่พบบ่อยที่สุดเข้าด้วยกัน |
| **MHA** | Multi-Head Attention | การทำ Self-Attention หลายๆ Head ขนานกันเพื่อจับความสัมพันธ์ในหลายมิติ |
| **MQA** | Multi-Query Attention | Self-Attention ที่ทุก Head แชร์ Key ($K$) และ Value ($V$) ร่วมกันเพื่อประหยัด VRAM |
| **GQA** | Grouped-Query Attention | Self-Attention ที่แบ่ง Query เป็นกลุ่มๆ และแต่ละกลุ่มแชร์ $K$ และ $V$ ร่วมกัน |
| **RoPE** | Rotary Position Embedding | การใส่ข้อมูลตำแหน่งคำโดยใช้การหมุน Rotation Matrix บน Vector ใน Complex Plane |
| **SFT** | Supervised Fine-Tuning | การ Fine-tune โมเดลด้วยข้อมูลรูปแบบคำสั่ง (Instruction - Response) |
| **RLHF** | Reinforcement Learning from Human Feedback | การจัดระเบียบโมเดลด้วยการเรียนรู้แบบเสริมแรงโดยอิงจากความพึงพอใจของมนุษย์ |
| **DPO** | Direct Preference Optimization | การปรับ Alignment โมเดลโดยตรงผ่าน Closed-form Implicit Reward Loss โดยไม่ต้องมี Reward Model แยก |
| **GRPO** | Group Relative Policy Optimization | อัลกอริทึม RL สำหรับ LLM ที่เปรียบเทียบผลลัพธ์ภายในกลุ่ม (Group Baseline) เพื่อตัดความจำเป็นของ Critic Model (นิยมใน DeepSeek-R1) |
| **LoRA** | Low-Rank Adaptation | เทคนิค PEFT ที่หยุดอัปเดตน้ำหนักหลัก $W_0$ แล้วใช้ Low-rank matrices $A$ และ $B$ มาเรียนรู้การเปลี่ยนแปลงแทน |
| **QLoRA** | Quantized Low-Rank Adaptation | LoRA ที่ใช้ Base Model ในรูปแบบ 4-bit NormalFloat (NF4) |
| **RAG** | Retrieval-Augmented Generation | การดึงข้อมูลภายนอก (Context) จาก Vector DB มาช่วยเสริมในการสร้างคำตอบของ LLM |
| **MoE** | Mixture of Experts | สถาปัตยกรรมที่เปิดใช้งานเฉพาะ Sub-networks (Experts) บางส่วนในแต่ละโทเคนผ่าน Router |
| **PPL** | Perplexity | ตัววัดประสิทธิภาพโมเดลภาษา (ยิ่งน้อยยิ่งดี) แสดงถึงความสับสนในการทำนายโทเคนถัดไป |

---

## 📐 สูตรคณิตศาสตร์ที่ต้องจำเข้าห้องสอบ (Essential Formulas)

### 1. Self-Attention Formula
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- $Q \in \mathbb{R}^{N \times d_k}$, $K \in \mathbb{R}^{M \times d_k}$, $V \in \mathbb{R}^{M \times d_v}$
- ตัวหาร $\sqrt{d_k}$ ใส่เพื่อป้องกันปัญหา **Vanishing Gradients** ในสเกลใหญ่เมื่อ $d_k$ มีขนาดมาก

### 2. LoRA Decomposition Formula
$$\Delta W = B \cdot A$$
$$W_{\text{final}} = W_0 + \frac{\alpha}{r} (B \cdot A)$$
- $W_0 \in \mathbb{R}^{d \times k}$, $A \in \mathbb{R}^{r \times k}$, $B \in \mathbb{R}^{d \times r}$ โดยที่ $r \ll \min(d, k)$
- จำนวนพารามิเตอร์ที่ต้องเทรนลดลงจาก $d \times k$ เหลือเพียง $r(d + k)$

### 3. Temperature Softmax Formula
$$P(y_i) = \frac{\exp(z_i / T)}{\sum_{j} \exp(z_j / T)}$$
- $T \to 0$: คำตอบกลายเป็น **Greedy Search** (Deterministic)
- $T > 1.0$: คำตอบมีความหลากหลายและสุ่มมากขึ้น (High Diversity)

### 4. Cross-Entropy Loss (Next Token Prediction)
$$\mathcal{L}_{\text{CLM}} = -\frac{1}{N} \sum_{i=1}^{N} \log P(x_i \mid x_1, x_2, \dots, x_{i-1})$$

---

## 🧮 สูตรคำนวณหน่วยความจำ (VRAM Estimation Cheat Sheet)

> [!IMPORTANT]
> **การคำนวณ VRAM สำหรับ Inference (อย่างง่าย)**:
> $$\text{VRAM}_{\text{Inference}} \approx P \times S + \text{KV Cache Memory} + \text{Activation Overhead}$$
> โดยที่ $P$ คือจำนวนพารามิเตอร์ (พ้นล้าน - Billions), $S$ คือขนาดประเภทข้อมูล (Bytes per parameter):
> - **FP32** (Float 32-bit) = 4 Bytes/param
> - **FP16 / BF16** (Float 16-bit) = 2 Bytes/param
> - **INT8** (8-bit Quantized) = 1 Byte/param
> - **INT4** (4-bit Quantized) = 0.5 Bytes/param

> [!EXAMPLE]
> **ตัวอย่างข้อสอบ**: โมเดล Llama-3 8B แบบ FP16 ต้องใช้ VRAM สำหรับโหลดพารามิเตอร์เท่าใด?
> $$\text{VRAM} = 8 \times 10^9 \text{ params} \times 2 \text{ bytes} = 16 \text{ GB}$$
> *(ต้องบวกสำรอง KV Cache และ Overhead อีกประมาณ 20-30% เป็น 20 GB)*

---

## 🔗 หน้าเชื่อมโยงย่อยใน Obsidian
- ไปยังดัชนีหลัก: [[Index]]
- เข้าสู่ Module 01: [[01.1 - Introduction to LLMs & NLP History]]
