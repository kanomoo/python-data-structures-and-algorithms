/**
 * DsaLab Exercises & Assignment Curriculum Data
 * Pre-bundled exercises, Python starter code, solutions, and visualizer specifications.
 */

window.DSA_EXERCISES = [
  // ==========================================
  // Category 1: 🎯 การบ้าน & ข้อสอบในห้องเรียน (Assignments & Exams)
  // ==========================================
  {
    id: 'assign1_linkedlist',
    category: 'exam',
    badge: 'Assignment 1',
    title: '🔗 Assignment 1: Singly Linked List (ระบบรายชื่อนักศึกษา)',
    subtitle: 'สร้าง Linked List จัดการข้อมูลนักศึกษา (ID, Name, GPA) พร้อมแทรกและลบโหนด',
    visualizer: 'linked_list',
    defaultData: [
      { id: '612037', name: 'Somchai', gpa: 3.50 },
      { id: '612045', name: 'Somsak', gpa: 2.85 },
      { id: '612089', name: 'Wichai', gpa: 3.90 },
      { id: '612102', name: 'Apinya', gpa: 3.15 }
    ],
    theory: `
### 🎯 โจทย์ Assignment 1: Singly Linked List
ในสไลด์และแบบฝึกหัด Assignment 1 อาจารย์ให้นักศึกษาเขียนคลาส **Node** และ **SinglyLinkedList** เพื่อเก็บข้อมูลทะเบียนนักศึกษา:
1. **Node**: บรรจุข้อมูล \`student_id\`, \`name\`, \`gpa\` และตัวชี้ \`next\`
2. **SinglyLinkedList**:
   - \`insert_front(id, name, gpa)\`: แทรกหัวแถว $O(1)$
   - \`insert_end(id, name, gpa)\`: แทรกท้ายแถว $O(n)$ หรือ $O(1)$ ถ้ามี tail
   - \`delete(id)\`: ค้นหารหัสนักศึกษาและปลดพอยน์เตอร์ข้ามโหนด $O(n)$
   - \`search(id)\`: วิ่งค้นหาข้อมูลโหนดทีละตัว $O(n)$

> [!TIP]
> สังเกตการเปลี่ยนพอยน์เตอร์ใน **Interactive Debugger** ด้านล่าง: ตัวชี้ \`p\` (Current) และ \`prev\` จะก้าวไปทีละโหนด เมื่อพบโหนดที่ต้องการลบจะตั้ง \`prev.next = p.next\`
`,
    starterCode: `class StudentNode:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_front(self, student_id, name, gpa):
        new_node = StudentNode(student_id, name, gpa)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f"Inserted front: {student_id} ({name})")

    def insert_end(self, student_id, name, gpa):
        new_node = StudentNode(student_id, name, gpa)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1
        print(f"Inserted end: {student_id} ({name})")

    def delete(self, student_id):
        curr = self.head
        prev = None
        while curr and curr.student_id != student_id:
            prev = curr
            curr = curr.next
        if not curr:
            print(f"Not found: {student_id}")
            return False
        if not prev:
            self.head = curr.next
        else:
            prev.next = curr.next
        self.size -= 1
        print(f"Deleted student: {student_id}")
        return True

    def display(self):
        curr = self.head
        res = []
        while curr:
            res.append(f"[{curr.student_id}: {curr.name} ({curr.gpa})]")
            curr = curr.next
        print(" -> ".join(res) if res else "List is empty")

# ทดสอบการทำงาน
slist = StudentLinkedList()
slist.insert_front("612037", "Somchai", 3.50)
slist.insert_end("612045", "Somsak", 2.85)
slist.insert_end("612089", "Wichai", 3.90)
slist.insert_front("612102", "Apinya", 3.15)
slist.display()
slist.delete("612045")
slist.display()
`
  },

  {
    id: 'test1_queue',
    category: 'exam',
    badge: 'Test Program 1',
    title: '📥 Test Program 1: Circular Array Queue',
    subtitle: 'จำลองการทำงานของคิววงกลม (Circular Queue) พร้อมตัวชี้ front, rear และ size',
    visualizer: 'queue',
    capacity: 6,
    defaultData: [10, 20, 30, 40],
    theory: `
### 📥 โจทย์ Test Program 1: Circular Queue
การทำคิวด้วย Array แบบดั้งเดิมจะเกิดปัญหา **False Full** (ช่องด้านหน้าว่างแต่ขยับไม่ได้) อาจารย์จึงสอน **Circular Queue** โดยใช้สมการวงกลมผ่านโมดูลัส:
$$\\text{rear} = (\\text{rear} + 1) \\pmod{\\text{capacity}}$$
$$\\text{front} = (\\text{front} + 1) \\pmod{\\text{capacity}}$$

- **Enqueue (ใส่ข้อมูล)**: นำเข้าที่ตำแหน่ง \`rear\`
- **Dequeue (นำข้อมูลออก)**: ดึงออกจากตำแหน่ง \`front\`
- ควบคุมจำนวนข้อมูลด้วยตัวแปร \`size\` หรือ \`count\`
`,
    starterCode: `class CircularQueue:
    def __init__(self, capacity=6):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue", item)
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item} at index {self.rear}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued {item}, new front is index {self.front}")
        return item

    def display(self):
        print("Queue Array:", self.queue, f"| Front: {self.front}, Rear: {self.rear}, Size: {self.size}")

# ทดสอบรัน
q = CircularQueue(6)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.dequeue()
q.display()
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.display()
`
  },

  {
    id: 'lecture5_bst_delete',
    category: 'exam',
    badge: 'Lecture 5.2',
    title: '🌲 Lecture 5.2: BST Deletion (กรณีโหนดมีลูก 2 ตัว)',
    subtitle: 'ค้นหา In-order Successor (ค่าน้อยสุดในกิ่งขวา) มาแทนที่โหนดที่ถูกลบ',
    visualizer: 'bst',
    defaultData: [50, 30, 70, 20, 40, 60, 80, 65],
    theory: `
### 🌲 การลบโหนดใน Binary Search Tree (3 Cases)
การลบโหนดใน BST แบ่งเป็น 3 กรณีสำคัญ:
1. **โหนดเป็น Leaf Node (ลูก 0 ตัว)**: ตัดลิงก์จากโหนดพ่อทิ้งได้ทันที
2. **โหนดมีลูก 1 ตัว**: ให้ลูกขึ้นมาเชื่อมต่อกับโหนดพ่อแทนตัวเอง
3. **โหนดมีลูก 2 ตัว (Two Children - ไฮไลต์ข้อสอบ)**:
   - กฎ: ห้ามตัดโครงสร้างมั่วซั่ว ต้องรักษาคุณสมบัติ BST ($Left < Root < Right$)
   - ขั้นที่ 1: หา **In-order Successor** (ค่าน้อยที่สุดในซับทรีย่อยฝั่งขวา) หรือ In-order Predecessor
   - ขั้นที่ 2: คัดลอกค่านั้นมาทับตำแหน่งโหนดปัจจุบัน
   - ขั้นที่ 3: สั่งลบโหนด In-order Successor ตัวเดิมออก (ซึ่งจะกลายเป็นกรณีลูก 0 หรือ 1 ตัวเสมอ!)
`,
    starterCode: `class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def find_min(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            successor = self.find_min(node.right)
            print(f"Replacing node {node.key} with In-order Successor: {successor.key}")
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def inorder(self, node, res=None):
        if res is None: res = []
        if node:
            self.inorder(node.left, res)
            res.append(node.key)
            self.inorder(node.right, res)
        return res

# ทดลองสร้าง BST ตามสไลด์
bst = BinarySearchTree()
for val in [50, 30, 70, 20, 40, 60, 80, 65]:
    bst.insert(val)

print("In-order ก่อนลบ:", bst.inorder(bst.root))
print("--- ลบโหนด 70 (ซึ่งมีลูก 2 ตัว: 60 และ 80) ---")
bst.delete(70)
print("In-order หลังลบ 70:", bst.inorder(bst.root))
`
  },

  {
    id: 'assign3_heap',
    category: 'exam',
    badge: 'Assignment 3',
    title: '🔺 Assignment 3: Binary Min-Heap (Percolate Up & Down)',
    subtitle: 'โครงสร้างฮีปแบบ Complete Binary Tree ใน Array: Insert & DeleteMin',
    visualizer: 'heap',
    defaultData: [10, 12, 20, 14, 16, 25, 30, 22],
    theory: `
### 🔺 การทำงานของ Binary Min-Heap (Array Representation)
ฮีปเก็บใน Array 1 มิติ (นิยมเริ่ม index 1 เพื่อง่ายต่อสูตรคำนวณ):
- **Parent ของโหนด $i$**: $\\lfloor i / 2 \\rfloor$
- **Left Child**: $2i$
- **Right Child**: $2i + 1$

**การแทรก (Insert / Percolate Up)**:
1. ใส่ข้อมูลใหม่ไว้ที่ตำแหน่งถัดไปท้าย Array ($O(1)$)
2. สลับกับ Parent ขึ้นไปเรื่อยๆ จนกว่า Parent จะมีค่าน้อยกว่า ($O(\\log n)$)

**การลบค่าต่ำสุด (DeleteMin / Percolate Down)**:
1. ดึงราก \`heap[1]\` ออกมา ($O(1)$)
2. นำข้อมูลตัวสุดท้ายของ Array มาแปะที่รากแทน
3. สลับกับลูกตัวที่น้อยที่สุด (Min Child) ไหลลงมาเรื่อยๆ จนถูกต้อง ($O(\\log n)$)
`,
    starterCode: `class MinHeap:
    def __init__(self):
        self.heap = [0]

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)
        print(f"Inserted {val} -> Heap Array: {self.heap[1:]}")

    def _percolate_up(self, i):
        while i // 2 > 0:
            parent = i // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def delete_min(self):
        if len(self.heap) <= 1:
            return None
        min_val = self.heap[1]
        last_val = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = last_val
            self._percolate_down(1)
        print(f"Deleted min {min_val} -> Heap Array: {self.heap[1:]}")
        return min_val

    def _percolate_down(self, i):
        while (i * 2) < len(self.heap):
            min_child = self._min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break

    def _min_child(self, i):
        if i * 2 + 1 >= len(self.heap):
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            return i * 2 + 1

# ทดลองรัน Min-Heap
h = MinHeap()
for v in [10, 12, 20, 14, 16, 25, 30, 22]:
    h.insert(v)

print("--- ลบ Min 3 ครั้ง ---")
h.delete_min()
h.delete_min()
h.delete_min()
`
  },

  {
    id: 'test2_sorting',
    category: 'exam',
    badge: 'Test Program 2',
    title: '📊 Test Program 2: Sorting Comparison (Bubble, Selection, Insertion, Quick)',
    subtitle: 'เปรียบเทียบการเรียงลำดับข้อมูล นับจำนวน Comparisons และ Swaps',
    visualizer: 'sorting',
    defaultData: [45, 12, 89, 34, 70, 23, 56, 18],
    theory: `
### 📊 สรุปอัลกอริทึมการจัดเรียง (Sorting Comparison)
| Algorithm | Best | Average | Worst | Swaps | Stable? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | Yes |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(n)$ | No |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | Yes |
| **Quick Sort** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n^2)$ | $O(n \\log n)$ | No |

กดปุ่ม **Step Next** ในเครื่องมือจำลองด้านล่างเพื่อดูการสลับคู่ข้อมูลและการจัดเรียงทีละขั้นตอน!
`,
    starterCode: `def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    comps = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comps, swaps

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    comps = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comps, swaps

def insertion_sort(arr):
    a = arr.copy()
    comps = 0
    swaps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                swaps += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comps, swaps

data = [45, 12, 89, 34, 70, 23, 56, 18]
print("ข้อมูลตั้งต้น:", data)
res_b, c_b, s_b = bubble_sort(data)
res_s, c_s, s_s = selection_sort(data)
res_i, c_i, s_i = insertion_sort(data)

print(f"Bubble Sort:    ผลลัพธ์ = {res_b} (Comps: {c_b}, Swaps: {s_b})")
print(f"Selection Sort: ผลลัพธ์ = {res_s} (Comps: {c_s}, Swaps: {s_s})")
print(f"Insertion Sort: ผลลัพธ์ = {res_i} (Comps: {c_i}, Swaps: {s_i})")
`
  },

  {
    id: 'assign4_dijkstra',
    category: 'exam',
    badge: 'Assignment 4',
    title: '🗺️ Assignment 4: Shortest Path (Dijkstra Algorithm)',
    subtitle: 'คำนวณวิถีสั้นสุดบนกราฟถ่วงน้ำหนักจุดยอด v1 - v7 ตามสไลด์การบ้าน',
    visualizer: 'dijkstra',
    nodes: ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7'],
    edges: [
      { u: 'v1', v: 'v2', w: 2 },
      { u: 'v1', v: 'v4', w: 1 },
      { u: 'v2', v: 'v4', w: 3 },
      { u: 'v2', v: 'v5', w: 10 },
      { u: 'v3', v: 'v1', w: 4 },
      { u: 'v3', v: 'v6', w: 5 },
      { u: 'v4', v: 'v3', w: 2 },
      { u: 'v4', v: 'v5', w: 2 },
      { u: 'v4', v: 'v6', w: 8 },
      { u: 'v4', v: 'v7', w: 4 },
      { u: 'v5', v: 'v7', w: 6 },
      { u: 'v7', v: 'v6', w: 1 }
    ],
    theory: `
### 🗺️ โจทย์ Assignment 4 & Lecture 11: Dijkstra's Algorithm
คำนวณวิถีสั้นสุดจากจุดเริ่มต้น $v_1$ ไปยังทุกจุดยอดในกราฟ:
- **ตารางคำนวณ**:
  - \`Vertex (v)\`: จุดยอด
  - \`Known\`: ค่าความจริง (True/False) ว่าจุดยอดนี้ได้ระยะสั้นสุดที่แท้จริงแล้วหรือยัง
  - \`d_v\`: ระยะทางสั้นที่สุดจากจุดเริ่มต้น (ตั้งต้น $v_1 = 0$, ตัวอื่น $=\\infty$)
  - \`p_v\`: จุดยอดก่อนหน้า (Previous vertex) ที่ใช้ในการเดินมา

> [!NOTE]
> ในแต่ละรอบ เลือกจุดยอด $v$ ที่มีค่า \`Known == False\` และมี \`d_v\` น้อยที่สุด จากนั้นปรับระยะทาง (Relaxation) ของเพื่อนบ้านทุกตัวที่เชื่อมต่ออยู่:
> $$\\text{if } d_v + c(v, w) < d_w \\implies d_w = d_v + c(v, w), \\quad p_w = v$$
`,
    starterCode: `import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    known = set()

    print(f"{'Vertex':<8} {'Known':<8} {'Dist (dv)':<12} {'Prev (pv)':<8}")
    print("-" * 38)

    while pq:
        d, u = heapq.heappop(pq)
        if u in known:
            continue
        known.add(u)
        print(f"{u:<8} {'True':<8} {dist[u]:<12} {str(prev[u]):<8}")

        for weight, neighbor in graph[u]:
            if neighbor not in known:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
                    prev[neighbor] = u
                    heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist, prev

graph_assignment = {
    'v1': [(2, 'v2'), (1, 'v4')],
    'v2': [(3, 'v4'), (10, 'v5')],
    'v3': [(4, 'v1'), (5, 'v6')],
    'v4': [(2, 'v3'), (2, 'v5'), (8, 'v6'), (4, 'v7')],
    'v5': [(6, 'v7')],
    'v6': [],
    'v7': [(1, 'v6')]
}

dist, prev = dijkstra(graph_assignment, 'v1')
print("\\nสรุประยะทางสั้นสุดจาก v1:")
for v in sorted(dist.keys()):
    path = []
    curr = v
    while curr:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    print(f"-> ถึง {v}: ระยะทาง = {dist[v]}, เส้นทาง = {' -> '.join(path)}")
`
  },

  {
    id: 'stack_postfix',
    category: 'linear',
    badge: 'Lecture 4',
    title: '🥞 Stack & การประเมินผล Postfix Expression',
    subtitle: 'ใช้ Stack อ่านโทเค็นนิพจน์ Postfix แล้วคำนวณผลลัพธ์ทีละคู่',
    visualizer: 'stack',
    defaultData: ['5', '3', '+', '8', '2', '-', '*', '4', '/'],
    theory: `
### 🥞 การประเมินผล Postfix Expression ด้วย Stack
นิพจน์ Postfix เช่น \`5 3 + 8 2 - * 4 /\` มีขั้นตอนประเมินผล:
1. อ่านโทเค็นทีละตัวจากซ้ายไปขวา
2. ถ้าเป็น **ตัวเลข (Operand)**: ให้ **Push** ลง Stack
3. ถ้าเป็น **เครื่องหมายคำนวณ (Operator)**:
   - **Pop** ค่าตัวเลขออกมา 2 ตัว (ตัวแรกคือ \`b\`, ตัวที่สองคือ \`a\`)
   - คำนวณผลลัพธ์ \`result = a [op] b\`
   - **Push** \`result\` กลับลงใน Stack
4. เมื่ออ่านจบ โทเค็นสุดท้ายที่ค้างอยู่ใน Stack คือคำตอบ!
`,
    starterCode: `def eval_postfix(tokens):
    stack = []
    print(f"{'Token':<8} {'Operation':<24} {'Stack Content':<20}")
    print("-" * 54)

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            print(f"{token:<8} Push {token:<19} {str(stack):<20}")
        else:
            b = stack.pop()
            a = stack.pop()
            res = 0
            if token == '+': res = a + b
            elif token == '-': res = a - b
            elif token == '*': res = a * b
            elif token == '/': res = a // b
            stack.append(res)
            print(f"{token:<8} Pop {b},{a} -> {a}{token}{b}={res:<6} {str(stack):<20}")

    return stack[0]

expr = ['5', '3', '+', '8', '2', '-', '*', '4', '/']
ans = eval_postfix(expr)
print("\\nคำตอบสุดท้าย =", ans)
`
  }
];
