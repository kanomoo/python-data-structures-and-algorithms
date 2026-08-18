# 📝 แนวข้อสอบกลางภาค: Data Structures and Algorithms (พร้อมเฉลยละเอียด)

> [!INFO] **ข้อมูลการสอบ (Exam Information)**
> - **คะแนนเต็ม:** 70 คะแนน (หาร 2 เหลือ 35 คะแนน)
> - **เงื่อนไข:** เปิดตำราได้ (Open Book / Open Notes)
> - **ภาษา:** คำถามเป็นภาษาอังกฤษ / อนุโลมให้ตอบเป็นภาษาไทยหรือภาษาอังกฤษได้
> - **การเขียนตอบ:** เขียนคำตอบด้วยปากกา / รูป Tree สามารถวาดด้วยดินสอได้
> - **อ้างอิง:** รวบรวมจากเนื้อหาบรรยาย, เอกสารประกอบการสอน, และข้อสอบเก่าจริงภาควิชา

---

## 📑 สารบัญ (Table of Contents)
- [Part 1: Singly Linked List (10 คะแนน)](#part-1-singly-linked-list-10-คะแนน)
- [Part 2: Stack & Queue (10 คะแนน)](#part-2-stack--queue-10-คะแนน)
- [Part 3: Binary Search Tree (15 คะแนน)](#part-3-binary-search-tree-15-คะแนน)
- [Part 4: Expression Tree & Infix/Postfix (15 คะแนน)](#part-4-expression-tree--infixpostfix-15-คะแนน)
- [Part 5: หลักการและทฤษฎีพื้นฐาน (10 คะแนน)](#part-5-หลักการและทฤษฎีพื้นฐาน-10-คะแนน)
- [Part 6: คำถามย่อยและการ Trace Code (10 คะแนน)](#part-6-คำถามย่อยและการ-trace-code-10-คะแนน)

---

# 📋 ส่วนข้อสอบ (Examination Paper)

## Part 1: Singly Linked List (10 คะแนน)

### ข้อ 1.1 (5 คะแนน)
**Question:**  
Write statements in `main` program using an instance variable `listA` with ordered inputs are `[1, 3, 8, 7, 9]` and has result outputs are `[9, 5, 1, 3, 7, 2, 8]` by using class `LinkedList`'s methods that we learned only (`add`, `insert`, `remove`, `search`).

```python
# Initial State: listA = 1 -> 3 -> 8 -> 7 -> 9
# Write your statements here:





```

---

### ข้อ 1.2 (5 คะแนน)
**Question:**  
When we implement a Singly Linked List, there are many special cases we must check. If the elements of a list are `[34, 12, 52, 16, 15]`, write at least **3 special cases** by giving method call examples and explaining why each case is special.

```text
Case 1: __________________________________________________________________________
Case 2: __________________________________________________________________________
Case 3: __________________________________________________________________________
```

---

## Part 2: Stack & Queue (10 คะแนน)

### ข้อ 2.1 (10 คะแนน)
**Question:**  
If there is the existing Stack's instance variable `s` which has 5 elements `[8, 4, 6, 9, 2]` *(Bottom: 8, Top: 2)* already.  
Write statements in `main` program to delete elements `4` and `9` from the instance variable `s` with using the existing Queue's instance variable `q` and has result output are `[8, 6, 2]` *(Bottom: 8, Top: 2)* by using class `Stack`'s and `Queue`'s methods that we learned only.

*(Allowed methods: Stack $\to$ `push()`, `pop()`, `top()`, `is_empty()` | Queue $\to$ `enQueue()`, `deQueue()`, `isEmpty()`)*

```python
# Write your statements here:









```

---

## Part 3: Binary Search Tree (15 คะแนน)

### ข้อ 3.1: Recursive Step Tracing (8 คะแนน)
**Question:**  
กำหนดโค้ดฟังก์ชัน `_insert_recursive` ของ Binary Search Tree:
```python
def _insert_recursive(self, current_node: Node, value: int):
    if value < current_node.value:
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            self._insert_recursive(current_node.left, value)
    elif value > current_node.value:
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            self._insert_recursive(current_node.right, value)
```

เมื่อทำการเรียก `tree.insert(25)` ลงใน BST ที่มีโหนดเดิมคือ `50, 20, 70, 30` (Root คือ `50`)  
จงเขียนขั้นตอนการทำงานในแต่ละรอบของ Recursive ลงในตาราง:

| Call ครั้งที่ | `current_node.value` | `value` | เงื่อนไขที่ตรวจสอบและผลลัพธ์ (`True`/`False`) | ประโยคคำสั่งที่ถูกทำ |
| :---: | :---: | :---: | :--- | :--- |
| **1** | `50` | `25` | `25 < 50` is `True` (left ไม่ว่าง) | `self._insert_recursive(current_node.left, 25)` |
| **2** | | | | |
| **3** | | | | |

---

### ข้อ 3.2: การสร้าง Tree จากลำดับการเดินท่อง (7 คะแนน)
**Question:**  
กำหนดผลการเดินท่อง (Traversal) ของ Binary Search Tree ดังนี้:
- **Pre-order Traversal:** `60, 30, 15, 40, 35, 80, 70, 95`
- **In-order Traversal:** `15, 30, 35, 40, 60, 70, 80, 95`

1. จงวาดภาพโครงสร้าง **Binary Search Tree** ที่ถูกต้องสมบูรณ์
2. จงเขียนลำดับผลลัพธ์การเดินท่องแบบ **Post-order Traversal**

---

## Part 4: Expression Tree & Infix/Postfix (15 คะแนน)

### ข้อ 4.1: การแปลง Infix เป็น Postfix ด้วย Stack (8 คะแนน)
**Question:**  
จงแสดงขั้นตอนการแปลงนิพจน์คณิตศาสตร์ Infix ต่อไปนี้ให้เป็น Postfix:
$$\text{Infix Expression: } ((A + B) \times C - (D - E) \div (F + G))$$

จงเติมตารางแสดงสถานะของ Operator Stack และ Output ในแต่ละ Token:

| ลำดับ | Token ที่อ่านได้ | การกระทำ (Action) | สถานะ Stack (ล่าง $\to$ บน) | Postfix Output |
| :---: | :---: | :--- | :--- | :--- |
| 1 | `(` | Push to stack | `(` | |
| 2 | `(` | Push to stack | `( (` | |
| 3 | `A` | Operand $\to$ Output | `( (` | `A` |
| 4 | `+` | Push operator | `( ( +` | `A` |
| 5 | `B` | Operand $\to$ Output | `( ( +` | `A B` |
| 6 | `)` | Pop จนเจอ `(` | `(` | `A B +` |
| ... | ... | ... | ... | ... |

---

### ข้อ 4.2: Expression Tree และการคำนวณผลลัพธ์ (7 คะแนน)
**Question:**  
กำหนด Postfix Expression:
$$5 \quad 3 \quad + \quad 8 \quad 6 \quad 2 \quad / \quad - \quad \times$$

1. จงแสดงสถานะ Stack ของโหนดขณะสร้าง Expression Tree
2. วาดภาพ **Expression Tree**
3. คำนวณค่าผลลัพธ์สุดท้าย (Evaluation Result)

---

## Part 5: หลักการและทฤษฎีพื้นฐาน ("หลักการอะไรเอ่ย") (10 คะแนน)

1. **(2.5 คะแนน)** หลักการ **LIFO (Last-In, First-Out)** คืออะไร? Data Structure ใดที่ใช้หลักการนี้ และยกตัวอย่างการใช้งานจริงในระบบคอมพิวเตอร์ 1 ตัวอย่าง
2. **(2.5 คะแนน)** กฎคุณสมบัติสำคัญของ **Binary Search Tree (BST)** ที่กำหนดความสัมพันธ์ระหว่างค่าใน Parent Node, Left Subtree และ Right Subtree คืออะไร?
3. **(2.5 คะแนน)** ใน Hash Table เมื่อเกิด **Collision** (ข้อมูลแย่งช่องเก็บเดียวกัน) วิธี **Chaining** และวิธี **Open Addressing (Linear Probing)** มีหลักการแก้ปัญหาต่างกันอย่างไร?
4. **(2.5 คะแนน)** การเข้าถึงข้อมูลตำแหน่งใดๆ ด้วยดัชนี (เช่น ดึงข้อมูลตัวที่ $i$) ระหว่าง **Array (List)** กับ **Singly Linked List** มี Time Complexity $O(1)$ หรือ $O(n)$ เพราะเหตุใด?

---

## Part 6: คำถามย่อยและการ Trace Code (10 คะแนน)

### ข้อ 6.1: Hash Table และการสร้าง List ใน Python (5 คะแนน)
พิจารณาโค้ด Python:
```python
table_size = 7
my_strings = [None] * table_size

def simple_hash(key_str):
    hash_val = 0
    for char in key_str:
        hash_val += ord(char)
    return hash_val % table_size
```
กำหนดค่ารหัส ASCII:
- `"cat"` $\rightarrow$ ผลบวก ASCII = $312$
- `"dog"` $\rightarrow$ ผลบวก ASCII = $314$
- `"bird"` $\rightarrow$ ผลบวก ASCII = $417$

**คำถาม:**
1. จงคำนวณ Index ของตาราง `my_strings` ที่ใช้เก็บคำว่า `"cat"`, `"dog"`, `"bird"`
2. คำสั่ง `my_strings = [None] * 7` แตกต่างจาก `my_strings = []` อย่างไรในการจัดการหน่วยความจำและเข้าถึงข้อมูล?

---

### ข้อ 6.2: Output Tracing ของฟังก์ชัน Recursive (5 คะแนน)
จงหาค่า Output ที่ได้จากการรันโปรแกรมนี้:
```python
def mystery(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return n + mystery(n - 1)
    else:
        return n * mystery(n - 2)

print(mystery(5))
```

---
---

# 💡 เฉลยละเอียดและวิธีคิด (Detailed Solutions)

---

## เฉลย Part 1: Singly Linked List

### ข้อ 1.1: คำสั่ง Main Program
- **โจทย์:** เริ่มต้น `1 -> 3 -> 8 -> 7 -> 9` ต้องการได้ `9 -> 5 -> 1 -> 3 -> 7 -> 2 -> 8`
- **วิธีคิด:**
  - `add(item)` จะนำข้อมูลไปวางที่ **หัวแถว (Head)** เสมอ
  - `insert(item, pos)` จะนำข้อมูลไปแทรกตาม index ตำแหน่งที่ระบุ
  - `remove(item)` จะค้นหาและลบค่าแรกที่เจอ
- **ลำดับคำสั่ง:**
```python
# 1. ลบ 9 และ 8 เดิมออก
listA.remove(9)       # เหลือ 1 -> 3 -> 8 -> 7
listA.remove(8)       # เหลือ 1 -> 3 -> 7

# 2. แทรก 8 และ 2 ที่ท้าย/ตำแหน่งที่ต้องการ
listA.insert(8, 3)     # ได้ 1 -> 3 -> 7 -> 8
listA.insert(2, 3)     # ได้ 1 -> 3 -> 7 -> 2 -> 8

# 3. ใช้ add() นำ 5 และ 9 ไปใส่ไว้หน้าสุด
listA.add(5)          # ได้ 5 -> 1 -> 3 -> 7 -> 2 -> 8
listA.add(9)          # ได้ 9 -> 5 -> 1 -> 3 -> 7 -> 2 -> 8
```

---

### ข้อ 1.2: Special Cases ใน Linked List
1. **Search/Delete ข้อมูลที่ไม่พบใน List (Item Not Found):**  
   - *ตัวอย่าง:* `listA.remove(99)` หรือ `listA.search(99)`  
   - *เหตุผล:* หากไม่ตรวจ `current != None` ก่อนเข้าลูปหรือขยับ pointer จะทำให้เกิด `AttributeError: 'NoneType' object has no attribute 'next'`
2. **การลบหรือแทรกที่ตำแหน่งแรกสุด (Head Node / Index 0):**  
   - *ตัวอย่าง:* `listA.remove(34)` หรือ `listA.insert(99, 0)`  
   - *เหตุผล:* โหนดแรกไม่มี previous node ชี้มา ต้องอัปเดต `self.head` โดยตรง
3. **การแทรกที่ตำแหน่งเกินความยาวของ List (Index Out of Range):**  
   - *ตัวอย่าง:* `listA.insert(88, 10)` ในขณะที่ List มีสมาชิกแค่ 5 ตัว  
   - *เหตุผล:* ลูปจะวิ่งจน `current` หลุดเป็น `None` ทำให้ไม่สามารถเรียก `.set_next()` ได้

---

## เฉลย Part 2: Stack & Queue

### ข้อ 2.1: การลบข้อมูล 4 และ 9 ออกจาก Stack ด้วย Queue
- **เริ่มต้น:** Stack `s = [Bottom: 8, 4, 6, 9, 2 :Top]`
- **เป้าหมาย:** Stack `s = [Bottom: 8, 6, 2 :Top]`
- **หลักการ:**
  - Stack นำออกด้วย `pop()` ได้ลำดับ $2, 9, 6, 4, 8$
  - กรองเอาเฉพาะ $2, 6, 8$ ใส่ Queue `q` $\implies$ `q = [Front: 2, 6, 8 :Rear]`
  - นำจาก `q` เข้า `s` ชั่วคราว $\implies$ `s = [Bottom: 2, 6, 8 :Top]`
  - นำจาก `s` เข้า `q` $\implies$ `q = [Front: 8, 6, 2 :Rear]`
  - นำจาก `q` กลับเข้า `s` $\implies$ `s = [Bottom: 8, 6, 2 :Top]` (ถูกต้องตรงตามลำดับเดิม)

```python
# ขั้นที่ 1: Pop ออกจาก Stack และคัดเลือกเฉพาะตัวที่ไม่ใช่ 4 และ 9 ใส่ Queue
val = s.pop()    # ได้ 2
q.enQueue(val)
s.pop()          # ได้ 9 (ทิ้ง)
val = s.pop()    # ได้ 6
q.enQueue(val)
s.pop()          # ได้ 4 (ทิ้ง)
val = s.pop()    # ได้ 8
q.enQueue(val)

# ขั้นที่ 2: สลับลำดับกลับคืนด้วย Stack และ Queue
while not q.isEmpty():
    s.push(q.deQueue())

while not s.is_empty():
    q.enQueue(s.pop())

while not q.isEmpty():
    s.push(q.deQueue())
```

---

## เฉลย Part 3: Binary Search Tree (BST)

### ข้อ 3.1: Recursive Step Tracing Table
- มีโหนดเดิม: `50`, `20` (ซ้ายของ 50), `70` (ขวาของ 50), `30` (ขวาของ 20)
- ต้องการ Insert ค่า `25`:

| Call ครั้งที่ | `current_node.value` | `value` | เงื่อนไขที่ตรวจสอบและผลลัพธ์ | ประโยคคำสั่งที่ถูกทำ |
| :---: | :---: | :---: | :--- | :--- |
| **1** | `50` | `25` | `25 < 50` $\to$ `True` (left มีโหนด 20) | `self._insert_recursive(current_node.left, 25)` |
| **2** | `20` | `25` | `25 > 20` $\to$ `True` (right มีโหนด 30) | `self._insert_recursive(current_node.right, 25)` |
| **3** | `30` | `25` | `25 < 30` $\to$ `True` (left ว่าง `is None`) | `current_node.left = Node(25)` *(สร้าง Node สำเร็จ)* |

---

### ข้อ 3.2: การวาด Tree และ Post-order Traversal
**1. รูปผังโครงสร้าง Binary Search Tree:**
```text
          60
        /    \
      30      80
     /  \    /  \
   15   40  70  95
        /
       35
```

**2. Post-order Traversal (Left $\to$ Right $\to$ Root):**  
$$\mathbf{15, 35, 40, 30, 70, 95, 80, 60}$$

---

## เฉลย Part 4: Expression Tree & Postfix

### ข้อ 4.1: ตาราง Infix to Postfix Conversion
นิพจน์: `((A + B) * C - (D - E) / (F + G))`

| Step | Token | Action | Operator Stack | Postfix Output |
| :---: | :---: | :--- | :--- | :--- |
| 1 | `(` | Push | `(` | |
| 2 | `(` | Push | `( (` | |
| 3 | `A` | Output | `( (` | `A` |
| 4 | `+` | Push | `( ( +` | `A` |
| 5 | `B` | Output | `( ( +` | `A B` |
| 6 | `)` | Pop until `(` | `(` | `A B +` |
| 7 | `*` | Push | `( *` | `A B +` |
| 8 | `C` | Output | `( *` | `A B + C` |
| 9 | `-` | Pop `*` then push `-` | `( -` | `A B + C *` |
| 10 | `(` | Push | `( - (` | `A B + C *` |
| 11 | `D` | Output | `( - (` | `A B + C * D` |
| 12 | `-` | Push | `( - ( -` | `A B + C * D` |
| 13 | `E` | Output | `( - ( -` | `A B + C * D E` |
| 14 | `)` | Pop until `(` | `( -` | `A B + C * D E -` |
| 15 | `/` | Push | `( - /` | `A B + C * D E -` |
| 16 | `(` | Push | `( - / (` | `A B + C * D E -` |
| 17 | `F` | Output | `( - / (` | `A B + C * D E - F` |
| 18 | `+` | Push | `( - / ( +` | `A B + C * D E - F` |
| 19 | `G` | Output | `( - / ( +` | `A B + C * D E - F G` |
| 20 | `)` | Pop until `(` | `( - /` | `A B + C * D E - F G +` |
| 21 | `)` | Pop all until `(` | | `A B + C * D E - F G + / -` |

**ผลลัพธ์ Postfix:** `A B + C * D E - F G + / -`

---

### ข้อ 4.2: Expression Tree และการหาค่าคำตอบ
Postfix: `5 3 + 8 6 2 / - *`

**1. รูปโครงสร้าง Expression Tree:**
```text
            *
        /       \
       +         -
      / \       / \
     5   3     8   /
                  / \
                 6   2
```

**2. การคำนวณผลลัพธ์ (Evaluation):**
- กิ่งซ้าย: $5 + 3 = 8$
- กิ่งขวา:
  - $6 / 2 = 3$
  - $8 - 3 = 5$
- โหนดราก: $8 \times 5 = 40$

**คำตอบ:** **40**

---

## เฉลย Part 5: หลักการและทฤษฎีพื้นฐาน

1. **LIFO (Last-In, First-Out):**
   - คือหลักการที่ข้อมูลที่ถูกใส่เข้าไปหลังสุดจะถูกนำออกมาใช้งานเป็นลำดับแรก
   - Data Structure ที่ใช้คือ **Stack**
   - ตัวอย่างการใช้งานจริง: **Function Call Stack** (การจดจำจุดเรียกฟังก์ชันย้อนกลับ), **Undo/Redo** ในโปรแกรมพิมพ์เอกสาร, หรือ **Browser Back Button**
2. **กฎคุณสมบัติของ BST:**
   - ข้อมูลทุกตัวใน **Left Subtree** ต้องมีค่าน้อยกว่า Root/Parent Node
   - ข้อมูลทุกตัวใน **Right Subtree** ต้องมีค่ามากกว่า Root/Parent Node
3. **การแก้ Collision ใน Hash Table:**
   - **Chaining:** ในแต่ละช่องตารางจะเก็บ Linked List ไว้ เมื่อมีข้อมูลชนกันจะนำไปต่อเป็น Node ใหม่ใน Linked List ของช่องนั้นๆ
   - **Open Addressing (Linear Probing):** ข้อมูลจะถูกเก็บในอาเรย์หลักโดยตรง หากช่องที่ Hash ได้ไม่ว่าง จะวนหาช่องว่างถัดไปทีละ 1 ช่อง ($index = (hash + 1) \pmod{size}$)
4. **Time Complexity ในการ Indexing:**
   - **Array:** $O(1)$ เพราะจัดเก็บในหน่วยความจำแบบต่อเนื่อง (Contiguous Memory) สามารถคำนวณ Memory Address ด้วย $Address = Base + (index \times size)$ ได้ทันที
   - **Singly Linked List:** $O(n)$ เพราะข้อมูลกระจายใน Memory ต้องเริ่มเดินตาม Pointer `next` ตั้งแต่ `head` ทีละโหนดไปจนถึงโหนดที่ $i$

---

## เฉลย Part 6: คำถามย่อยและการ Trace Code

### ข้อ 6.1: Hash Table และการสร้าง List
1. **คำนวณ Index:**
   - `"cat"`: $312 \pmod 7 = 4$ $\rightarrow$ เก็บที่ `my_strings[4] = "cat"`
   - `"dog"`: $314 \pmod 7 = 6$ $\rightarrow$ เก็บที่ `my_strings[6] = "dog"`
   - `"bird"`: $417 \pmod 7 = 4$ $\rightarrow$ เกิด Collision ที่ Index 4
2. **ความแตกต่าง:**
   - `my_strings = [None] * 7`: จองหน่วยความจำล่วงหน้าเป็น List ขนาดคงที่ 7 ช่อง แต่ละช่องมีค่าเป็น `None` ทำให้สามารถกำหนดค่าหรือเข้าถึงด้วย Index ได้ทันที เช่น `my_strings[4] = "cat"`
   - `my_strings = []`: สร้าง Empty List ที่มีความยาวเริ่มต้นเป็น 0 หากเข้าถึงด้วย `my_strings[4]` จะเกิดข้อผิดพลาด `IndexError: list assignment index out of range` ทันที ต้องใช้ `.append()` หรือ `.insert()` เท่านั้น

---

### ข้อ 6.2: Output Tracing
- เมื่อเรียก `mystery(5)`:
  1. $n = 5$ (เลขคี่) $\implies 5 \times \text{mystery}(3)$
  2. $n = 3$ (เลขคี่) $\implies 3 \times \text{mystery}(1)$
  3. $n = 1$ (เข้า Base Case $n \le 1$) $\implies \text{return } 1$
- คำนวณย้อนกลับ:
  - $\text{mystery}(3) = 3 \times 1 = 3$
  - $\text{mystery}(5) = 5 \times 3 = 15$

**Output:** `15`
