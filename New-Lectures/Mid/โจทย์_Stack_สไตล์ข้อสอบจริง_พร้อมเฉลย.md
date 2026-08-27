# 📚 ชุดโจทย์ฝึกทำข้อสอบ: Stack ADT (สไตล์ข้อสอบจริง Midterm พร้อมเฉลยละเอียด)

> [!NOTE] **รูปแบบและลักษณะข้อสอบ (Exam Blueprint)**
> - ถอดแบบจากข้อสอบจริงวิชา Data Structures & Algorithms (ลักษณะเดียวกับข้อสอบ Linked List และ Stack ในรูป `Mid/` และ `exam.txt`)
> - อนุญาตให้ใช้เฉพาะ Method มาตรฐานของ `Stack` (`push()`, `pop()`, `top()`, `is_empty()`, `size()`) และ `Queue` (`enQueue()`, `deQueue()`, `isEmpty()`)
> - ห้ามเข้าถึง Private Attributes หรือใช้ Python List Method โดยตรงใน main program

---

## 📑 สารบัญชุดข้อสอบ Stack
1. [ข้อที่ 1 (Style ข้อสอบจริง 1): การกรองและลบสมาชิกเฉพาะค่าใน Stack โดยใช้ Queue](#ข้อที่-1-การกรองและลบสมาชิกเฉพาะค่าใน-stack-โดยใช้-queue)
2. [ข้อที่ 2 (Style ข้อสอบจริง 2): การแทรกข้อมูลลงก้น Stack (Insert at Bottom)](#ข้อที่-2-การแทรกข้อมูลลงก้น-stack-insert-at-bottom)
3. [ข้อที่ 3 (Style ข้อสอบจริง 3): Special Boundary Cases ของ Stack](#ข้อที่-3-special-boundary-cases-ของ-stack)
4. [ข้อที่ 4 (Style ข้อสอบจริง 4): การเรียงลำดับ/กลับลำดับ Stack ด้วย Auxiliary Queue](#ข้อที่-4-การกลับลำดับข้อมูลใน-stack)
5. [ข้อที่ 5 (Style ข้อสอบจริง 5): Sequence Push/Pop Simulation & Tracing](#ข้อที่-5-sequence-pushpop-simulation--tracing)
6. [ข้อที่ 6 (Style ข้อสอบจริง 6): Parentheses Matching Tracing (ตรวจวงเล็บสมดุล)](#ข้อที่-6-parentheses-matching-tracing)

---

# 📝 ตัวข้อสอบ (Question Sheet)

---

### ข้อที่ 1: การกรองและลบสมาชิกเฉพาะค่าใน Stack โดยใช้ Queue (5 คะแนน)
**Question (English):**  
If there is an existing Stack's instance variable `s` which has 6 elements `[15, 8, 23, 4, 12, 7]` *(where `15` is at the Bottom and `7` is at the Top: `[Bottom: 15 -> 8 -> 23 -> 4 -> 12 -> 7 :Top]`)*.  
Write statements in `main` program to delete elements `8` and `4` from the instance variable `s` by using the existing Queue's instance variable `q` so that the final result in `s` is `[15, 23, 12, 7]` *(Bottom: 15, Top: 7)* by using class `Stack`'s and `Queue`'s methods that we learned only.

```python
# Starting state: s = [Bottom: 15, 8, 23, 4, 12, 7 :Top], q is empty
# Write your statements below:
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
```

---

### ข้อที่ 2: การแทรกข้อมูลลงที่ก้น Stack (Insert at Bottom) (5 คะแนน)
**Question (English):**  
Suppose you have an existing Stack `s` with 4 elements: `[50, 40, 30, 20]` *(Bottom: 50, Top: 20)*.  
You want to insert a new value `99` to become the **Bottom** element, resulting in `s = [99, 50, 40, 30, 20]` *(Bottom: 99, Top: 20)*.  
Write statements in the `main` program using an auxiliary Queue `q` to achieve this.

```python
# Starting state: s = [Bottom: 50, 40, 30, 20 :Top], new value = 99
# Write your statements below:
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
```

---

### ข้อที่ 3: Special Boundary Cases ของ Stack (5 คะแนน)
**Question (English):**  
When we implement or use the `Stack` ADT (with a fixed maximum capacity limit $N=5$), there are several special/boundary cases and exceptional situations that we must handle.  
Write at least **3 special cases** by giving concrete examples (method calls with state) and explain what error/behavior occurs if not handled properly.

```text
Special Case 1: __________________________________________________________________
Explanation:    __________________________________________________________________

Special Case 2: __________________________________________________________________
Explanation:    __________________________________________________________________

Special Case 3: __________________________________________________________________
Explanation:    __________________________________________________________________
```

---

### ข้อที่ 4: การกลับลำดับข้อมูลใน Stack (Reverse Stack) (5 คะแนน)
**Question (English):**  
Given a Stack `s` with elements `['A', 'B', 'C', 'D']` *(where `'A'` is Bottom and `'D'` is Top)*.  
Write statements in the `main` program to reverse the elements of Stack `s` so that `'D'` becomes Bottom and `'A'` becomes Top: `['D', 'C', 'B', 'A']` by using Queue `q`.

```python
# Write your statements below:
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
```

---

### ข้อที่ 5: Sequence Push/Pop Simulation & Tracing (5 คะแนน)
**Question (English):**  
An empty Stack `s` performs the following sequence of operations:
1. `s.push(10)`
2. `s.push(20)`
3. `a = s.pop()`
4. `s.push(30)`
5. `s.push(40)`
6. `b = s.top()`
7. `c = s.pop()`
8. `s.push(a + c)`
9. `d = s.pop()`

**Task:**  
- เติมค่าของตัวแปร: `a = ___`, `b = ___`, `c = ___`, `d = ___`
- สภาพข้อมูลที่เหลืออยู่ใน Stack `s` จาก Bottom ไป Top คือ: `[ ____________ ]`

---

### ข้อที่ 6: Parentheses Matching Tracing (ตรวจวงเล็บสมดุล) (5 คะแนน)
**Question (English):**  
Given the algorithm for checking balanced parentheses using a Stack, trace the Stack content step-by-step for the string:  
$$\text{Expression: } \{ [ ( ) ] ( ) \}$$

| Step | Symbol อ่านได้ | การกระทำ (Action: Push / Pop / Match) | สถานะของ Stack (Bottom $\to$ Top) | ข้อผิดพลาด (ถ้ามี) |
| :---: | :---: | :--- | :--- | :--- |
| 1 | `{` | Push opening bracket | `{` | ไม่มี |
| 2 | `[` | Push opening bracket | `{ [` | ไม่มี |
| 3 | `(` | Push opening bracket | `{ [ (` | ไม่มี |
| 4 | `)` | Pop and match with `(` | `{ [` | จับคู่ถูกต้อง |
| ... | ... | ... | ... | ... |

---
---

# 💡 เฉลยละเอียดและขั้นตอนการคิด (Solutions & Detailed Walkthrough)

---

## เฉลยข้อที่ 1: การกรองและลบสมาชิกเฉพาะค่าใน Stack โดยใช้ Queue

### 🎯 แนวคิด (Core Concept):
- Stack เป็น **LIFO (Last-In, First-Out)** เวลา `pop()` จะได้ข้อมูลจาก **Top ลงมา Bottom**
- เริ่มต้น `s = [Bottom: 15, 8, 23, 4, 12, 7 :Top]`
- เมื่อ `pop()` ทีละตัว:
  1. `7` $\implies$ เก็บ (ใส่ `q`)
  2. `12` $\implies$ เก็บ (ใส่ `q`)
  3. `4` $\implies$ **ทิ้ง (ไม่ใส่ `q`)**
  4. `23` $\implies$ เก็บ (ใส่ `q`)
  5. `8` $\implies$ **ทิ้ง (ไม่ใส่ `q`)**
  6. `15` $\implies$ เก็บ (ใส่ `q`)
- ตอนนี้ Queue `q = [Front: 7, 12, 23, 15 :Rear]`
- **การกู้คืนลำดับเดิม (Order Restoration):**
  - เทจาก `q` เข้า `s`: `s = [Bottom: 7, 12, 23, 15 :Top]`
  - เทจาก `s` เข้า `q`: `q = [Front: 15, 23, 12, 7 :Rear]`
  - เทจาก `q` เข้า `s`: `s = [Bottom: 15, 23, 12, 7 :Top]` 🎉 ได้ลำดับที่ถูกต้องสมบูรณ์!

### 💻 โค้ดคำตอบ:
```python
# ขั้นที่ 1: Pop ทีละตัว และ Enqueue เฉพาะค่าที่ไม่ใช่ 8 และ 4
val = s.pop()       # 7
q.enQueue(val)
val = s.pop()       # 12
q.enQueue(val)
s.pop()             # 4 (ลบทิ้ง ไม่เก็บ)
val = s.pop()       # 23
q.enQueue(val)
s.pop()             # 8 (ลบทิ้ง ไม่เก็บ)
val = s.pop()       # 15
q.enQueue(val)
# ตอนนี้ q = [Front: 7, 12, 23, 15 :Rear]

# ขั้นที่ 2: ใช้ Loop ถ่ายโอนข้อมูลสลับไปมาเพื่อรักษาระเบียบ LIFO เดิม
while not q.isEmpty():
    s.push(q.deQueue())    # s = [Bottom: 7, 12, 23, 15 :Top]

while not s.is_empty():
    q.enQueue(s.pop())     # q = [Front: 15, 23, 12, 7 :Rear]

while not q.isEmpty():
    s.push(q.deQueue())    # s = [Bottom: 15, 23, 12, 7 :Top]
```

---

## เฉลยข้อที่ 2: การแทรกข้อมูลลงก้น Stack (Insert at Bottom)

### 🎯 แนวคิด:
- ต้องการเอา `99` ไปไว้ล่างสุดของ `[50, 40, 30, 20]`
- ถ่ายข้อมูลทั้งหมดใน `s` ไปฝากไว้ใน `q` $\rightarrow$ `q = [Front: 20, 30, 40, 50 :Rear]`
- `push(99)` ลงใน `s` ที่ว่างอยู่ $\rightarrow$ `s = [Bottom: 99 :Top]`
- ถ้า Dequeue จาก `q` ใส่ `s` ตรงๆ จะได้ `[Bottom: 99, 20, 30, 40, 50 :Top]` (ลำดับกลับด้าน)
- ดังนั้นต้องกลับลำดับใน `q` ให้ถูกต้องก่อน หรือถ่ายเข้า `s` แล้วสลับด้วย `q` อีก 1 รอบ

### 💻 โค้ดคำตอบ:
```python
# 1. เทของเดิมใน s ทั้งหมดลง q
while not s.is_empty():
    q.enQueue(s.pop())      # q = [Front: 20, 30, 40, 50 :Rear]

# 2. ใส่ 99 ลงก้น Stack
s.push(99)                  # s = [Bottom: 99 :Top]

# 3. สลับลำดับสมาชิกใน q เพื่อให้เทกลับเข้า s แล้วได้ 50 อยู่ล่างสุดตามเดิม
# เท q ทั้งหมดเข้า s ชั่วคราว (ทับ 99)
while not q.isEmpty():
    s.push(q.deQueue())     # s = [Bottom: 99, 20, 30, 40, 50 :Top]

# Pop 50..20 ออกมาเก็บใน q (แต่เหลือ 99 ไว้ที่ก้น)
while s.size() > 1:
    q.enQueue(s.pop())      # q = [Front: 50, 40, 30, 20 :Rear], s = [99]

# เท q กลับเข้า s จะได้ 50 เข้าก่อน ตามด้วย 40, 30, 20
while not q.isEmpty():
    s.push(q.deQueue())     # s = [Bottom: 99, 50, 40, 30, 20 :Top]
```

---

## เฉลยข้อที่ 3: Special Boundary Cases ของ Stack

1. **Stack Underflow (การ Pop หรือ Top ขณะ Stack ว่างเปล่า):**
   - *ตัวอย่าง:* `s = Stack()`, เรียก `s.pop()` หรือ `s.top()`
   - *คำอธิบาย:* เมื่อไม่มีข้อมูลใน Stack การเรียก `pop()` บน List ว่างจะทำให้เกิด `IndexError: pop from empty list` ต้องเช็ค `if self.is_empty():` ก่อนเสมอ
2. **Stack Overflow (การ Push ข้อมูลเกินขนาดความจุสูงสุด Limit):**
   - *ตัวอย่าง:* กำหนด `s = Stack(limit=5)` มีข้อมูลอยู่แล้ว 5 ตัว แล้วเรียก `s.push(99)`
   - *คำอธิบาย:* หาก Stack มีการจำกัดขนาด Array การ push เกินจะทำให้ Memory ล้น ต้องตรวจเงื่อนไข `if len(self.items) >= self.limit:` เพื่อปฏิเสธการ push
3. **การเข้าถึงหรือลบข้อมูลตัวล่างสุด/ตัวกลาง (Accessing Non-Top Elements):**
   - *ตัวอย่าง:* ต้องการอ่านหรือลบข้อมูลที่อยู่ Bottom โดยไม่ใช้ตัวแปรชั่วคราว
   - *คำอธิบาย:* Stack ไม่อนุญาตให้เข้าถึงแบบ Random Index (`s[0]`) หากฝืนเข้าถึง private attribute จะผิดหลักการ Encapsulation ของ ADT ต้อง Pop ตัวบนออกเก็บไว้ในโครงสร้างช่วย (Auxiliary Queue/Stack) ก่อนเสมอ

---

## เฉลยข้อที่ 4: การกลับลำดับข้อมูลใน Stack (Reverse Stack)

### 🎯 แนวคิด:
- คุณสมบัติธรรมชาติ: นำข้อมูลจาก **Stack (LIFO)** ใส่เข้า **Queue (FIFO)** แล้วนำออกจาก Queue กลับเข้า Stack จะได้ผลลัพธ์เป็นการ **Reverse ลำดับ** ทันที!
- เริ่มต้น: `s = [Bottom: 'A', 'B', 'C', 'D' :Top]`
- Pop ออก: ได้ `'D'`, `'C'`, `'B'`, `'A'` ใส่เข้า Queue $\rightarrow$ `q = [Front: 'D', 'C', 'B', 'A' :Rear]`
- Dequeue ออก: ได้ `'D'` (เข้าก้น s), `'C'`, `'B'`, `'A'` (อยู่บนสุด)
- ได้ `s = [Bottom: 'D', 'C', 'B', 'A' :Top]`

### 💻 โค้ดคำตอบ:
```python
# 1. ถ่ายข้อมูลทั้งหมดจาก Stack s ไปยัง Queue q
while not s.is_empty():
    q.enQueue(s.pop())

# 2. ถ่ายข้อมูลจาก Queue q กลับเข้า Stack s
while not q.isEmpty():
    s.push(q.deQueue())
```

---

## เฉลยข้อที่ 5: Sequence Push/Pop Simulation & Tracing

### 🔍 Trace ทีละขั้นตอน:
1. `s.push(10)` $\rightarrow$ `s = [10]`
2. `s.push(20)` $\rightarrow$ `s = [10, 20]`
3. `a = s.pop()` $\rightarrow$ `a = 20`, `s = [10]`
4. `s.push(30)` $\rightarrow$ `s = [10, 30]`
5. `s.push(40)` $\rightarrow$ `s = [10, 30, 40]`
6. `b = s.top()` $\rightarrow$ `b = 40` (ดูค่าบนสุด ไม่ได้นำออก), `s = [10, 30, 40]`
7. `c = s.pop()` $\rightarrow$ `c = 40`, `s = [10, 30]`
8. `s.push(a + c)` $\rightarrow$ `a + c = 20 + 40 = 60` $\rightarrow$ `s.push(60)` $\rightarrow$ `s = [10, 30, 60]`
9. `d = s.pop()` $\rightarrow$ `d = 60`, `s = [10, 30]`

### 📌 สรุปคำตอบ:
- `a = 20`
- `b = 40`
- `c = 40`
- `d = 60`
- สภาพคงเหลือใน `s`: `[Bottom: 10, 30 :Top]`

---

## เฉลยข้อที่ 6: Parentheses Matching Tracing (ตรวจวงเล็บสมดุล)

นิพจน์: `{ [ ( ) ] ( ) }`

| Step | Symbol | การกระทำ (Action) | สถานะ Stack (ล่าง $\to$ บน) | ผลการตรวจ |
| :---: | :---: | :--- | :--- | :--- |
| **1** | `{` | Push opening bracket | `{` | ผ่าน |
| **2** | `[` | Push opening bracket | `{ [` | ผ่าน |
| **3** | `(` | Push opening bracket | `{ [ (` | ผ่าน |
| **4** | `)` | Pop `(` และจับคู่กับ `)` | `{ [` | ตรงกัน (Match) |
| **5** | `]` | Pop `[` และจับคู่กับ `]` | `{` | ตรงกัน (Match) |
| **6** | `(` | Push opening bracket | `{ (` | ผ่าน |
| **7** | `)` | Pop `(` และจับคู่กับ `)` | `{` | ตรงกัน (Match) |
| **8** | `}` | Pop `{` และจับคู่กับ `}` | *(Empty)* | ตรงกัน (Match) |

**สรุปผล:** วงเล็บทุกคู่เปิด-ปิดถูกต้อง และ Stack ว่างเปล่าเมื่อจบสตริง $\implies$ **Balanced (สมดุล)**
