// scratch/build_trace_test.js
function buildTopologicalSortTrace() {
  const trace = [];

  const graph = {
    1: [2, 4, 3],
    2: [4, 5],
    3: [6],
    4: [6, 7, 3],
    5: [4, 7],
    6: [],
    7: [6]
  };

  // Step 0: Initial Scan
  let curIndeg = { 1: 0, 2: 1, 3: 2, 4: 3, 5: 1, 6: 3, 7: 2 };
  let curQueue = [];
  let curQueueSlots = [null, null, null, null, null, null, null];
  let curFront = 0;
  let curBack = 6;
  let curSize = 0;
  let curTopo = [];

  trace.push({
    line: 3,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'INIT INDEGREES',
    boundary: true,
    note: 'เริ่มต้น: ตรวจนับจำนวนเส้นชี้เข้า (Indegree) ของจุดยอดทั้ง 7 จุด: v1=0, v2=1, v3=2, v4=3, v5=1, v6=3, v7=2 รวม 12 เส้น',
    watch: { 'Phase': 'Initialization', 'Total Vertices': 7, 'Total Edges': 12, 'Queue': '[]' }
  });

  // Step 1: Find 0-indegree -> Enqueue v1
  curQueue = [1];
  curQueueSlots[0] = 1;
  curFront = 0;
  curBack = 0;
  curSize = 1;

  trace.push({
    line: 11,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v1',
    boundary: false,
    note: 'ตรวจพบจุดยอดที่มี Indegree = 0 คือ v1 (ไม่มีงานก่อนหน้าค้างอยู่)  →  Enqueue(1) เข้าคิวช่อง [0] (Currentsize=1, Front=0, Back=0)',
    watch: { 'v': 'None', 'indegree[1]': 0, 'Queue': '[1]', 'Currentsize': 1, 'Front': 0, 'Back': 0 }
  });

  // Iteration 1: Process v1
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 1)',
    boundary: true,
    note: 'เข้าสู่ลูป while not q.is_empty(): คิวไม่ว่าง มีจุดยอด [1] รอรับการประมวลผล',
    watch: { 'q.is_empty()': false, 'Queue': '[1]', 'Currentsize': 1 }
  });

  // Dequeue v1
  curQueue = [];
  curFront = 1;
  curSize = 0;
  trace.push({
    line: 17,
    activeV: 1,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v1',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [0]  →  ได้จุดยอดที่พร้อมทำงาน v = 1 (Front ขยับเป็น 1, Currentsize = 0)',
    watch: { 'v': 'v1', 'Queue': '[]', 'Currentsize': 0, 'Front': 1, 'Back': 0 }
  });

  // Append v1 to topo_order
  curTopo = [1];
  trace.push({
    line: 18,
    activeV: 1,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v1',
    boundary: false,
    note: 'บันทึกจุดยอด 1 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1]',
    watch: { 'v': 'v1', 'topo_order': '[1]', 'len(topo_order)': 1 }
  });

  // Edge 1 -> 2
  trace.push({
    line: 21,
    activeV: 1,
    targetW: 2,
    activeEdge: [1, 2],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (1 → 2)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 1 → 2: ปลายทางคือเพื่อนบ้าน w = 2 (Indegree เดิม = 1)',
    watch: { 'v': 'v1', 'w': 'v2', 'indegree[2]': 1 }
  });

  curIndeg[2] = 0;
  trace.push({
    line: 22,
    activeV: 1,
    targetW: 2,
    activeEdge: [1, 2],
    indegrees: { ...curIndeg },
    decrementedW: 2,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(2)',
    boundary: false,
    note: 'ลดค่า Indegree ของจุดยอด 2 ลง 1: indegree[2] = 1 - 1 = 0',
    watch: { 'v': 'v1', 'w': 'v2', 'indegree[2]': 0 }
  });

  curQueue = [2];
  curQueueSlots[1] = 2;
  curBack = 1;
  curSize = 1;
  trace.push({
    line: 24,
    activeV: 1,
    targetW: 2,
    activeEdge: [1, 2],
    indegrees: { ...curIndeg },
    decrementedW: 2,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v2',
    boundary: false,
    note: 'indegree[2] กลายเป็น 0 แล้ว!  →  Enqueue(2) เข้าคิวช่อง [1] (Currentsize=1, Back=1)',
    watch: { 'v': 'v1', 'w': 'v2', 'Queue': '[2]', 'Currentsize': 1, 'Front': 1, 'Back': 1 }
  });

  // Edge 1 -> 4
  trace.push({
    line: 21,
    activeV: 1,
    targetW: 4,
    activeEdge: [1, 4],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (1 → 4)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 1 → 4: ปลายทางคือเพื่อนบ้าน w = 4 (Indegree เดิม = 3)',
    watch: { 'v': 'v1', 'w': 'v4', 'indegree[4]': 3 }
  });

  curIndeg[4] = 2;
  trace.push({
    line: 22,
    activeV: 1,
    targetW: 4,
    activeEdge: [1, 4],
    indegrees: { ...curIndeg },
    decrementedW: 4,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(4)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 4 ลง 1: indegree[4] = 3 - 1 = 2 (ยังไม่เป็น 0 จึงยังไม่เข้าคิว)',
    watch: { 'v': 'v1', 'w': 'v4', 'indegree[4]': 2 }
  });

  // Edge 1 -> 3
  trace.push({
    line: 21,
    activeV: 1,
    targetW: 3,
    activeEdge: [1, 3],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (1 → 3)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 1 → 3: ปลายทางคือเพื่อนบ้าน w = 3 (Indegree เดิม = 2)',
    watch: { 'v': 'v1', 'w': 'v3', 'indegree[3]': 2 }
  });

  curIndeg[3] = 1;
  trace.push({
    line: 22,
    activeV: 1,
    targetW: 3,
    activeEdge: [1, 3],
    indegrees: { ...curIndeg },
    decrementedW: 3,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(3)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 3 ลง 1: indegree[3] = 2 - 1 = 1 (ยังไม่เป็น 0) — ประมวลผลเพื่อนบ้านของ v1 ครบถ้วน',
    watch: { 'v': 'v1', 'w': 'v3', 'indegree[3]': 1 }
  });

  // Iteration 2: Process v2
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 2)',
    boundary: true,
    note: 'วนลูป while รอบที่ 2: คิวมีจุดยอด [2] รออยู่',
    watch: { 'q.is_empty()': false, 'Queue': '[2]', 'Currentsize': 1 }
  });

  curQueue = [];
  curFront = 2;
  curSize = 0;
  trace.push({
    line: 17,
    activeV: 2,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v2',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [1]  →  ได้จุดยอด v = 2 (Front ขยับเป็น 2, Currentsize = 0)',
    watch: { 'v': 'v2', 'Queue': '[]', 'Currentsize': 0, 'Front': 2, 'Back': 1 }
  });

  curTopo = [1, 2];
  trace.push({
    line: 18,
    activeV: 2,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v2',
    boundary: false,
    note: 'บันทึกจุดยอด 2 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1, 2]',
    watch: { 'v': 'v2', 'topo_order': '[1, 2]', 'len(topo_order)': 2 }
  });

  // Edge 2 -> 4
  trace.push({
    line: 21,
    activeV: 2,
    targetW: 4,
    activeEdge: [2, 4],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (2 → 4)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 2 → 4: ปลายทางคือเพื่อนบ้าน w = 4 (Indegree เดิม = 2)',
    watch: { 'v': 'v2', 'w': 'v4', 'indegree[4]': 2 }
  });

  curIndeg[4] = 1;
  trace.push({
    line: 22,
    activeV: 2,
    targetW: 4,
    activeEdge: [2, 4],
    indegrees: { ...curIndeg },
    decrementedW: 4,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(4)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 4 ลง 1: indegree[4] = 2 - 1 = 1 (ยังไม่เป็น 0)',
    watch: { 'v': 'v2', 'w': 'v4', 'indegree[4]': 1 }
  });

  // Edge 2 -> 5
  trace.push({
    line: 21,
    activeV: 2,
    targetW: 5,
    activeEdge: [2, 5],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (2 → 5)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 2 → 5: ปลายทางคือเพื่อนบ้าน w = 5 (Indegree เดิม = 1)',
    watch: { 'v': 'v2', 'w': 'v5', 'indegree[5]': 1 }
  });

  curIndeg[5] = 0;
  trace.push({
    line: 22,
    activeV: 2,
    targetW: 5,
    activeEdge: [2, 5],
    indegrees: { ...curIndeg },
    decrementedW: 5,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(5)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 5 ลง 1: indegree[5] = 1 - 1 = 0',
    watch: { 'v': 'v2', 'w': 'v5', 'indegree[5]': 0 }
  });

  curQueue = [5];
  curQueueSlots[2] = 5;
  curBack = 2;
  curSize = 1;
  trace.push({
    line: 24,
    activeV: 2,
    targetW: 5,
    activeEdge: [2, 5],
    indegrees: { ...curIndeg },
    decrementedW: 5,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v5',
    boundary: false,
    note: 'indegree[5] กลายเป็น 0 แล้ว!  →  Enqueue(5) เข้าคิวช่อง [2] (Currentsize=1, Back=2)',
    watch: { 'v': 'v2', 'w': 'v5', 'Queue': '[5]', 'Currentsize': 1, 'Front': 2, 'Back': 2 }
  });

  // Iteration 3: Process v5
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 3)',
    boundary: true,
    note: 'วนลูป while รอบที่ 3: คิวมีจุดยอด [5] รออยู่',
    watch: { 'q.is_empty()': false, 'Queue': '[5]', 'Currentsize': 1 }
  });

  curQueue = [];
  curFront = 3;
  curSize = 0;
  trace.push({
    line: 17,
    activeV: 5,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v5',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [2]  →  ได้จุดยอด v = 5 (Front ขยับเป็น 3, Currentsize = 0)',
    watch: { 'v': 'v5', 'Queue': '[]', 'Currentsize': 0, 'Front': 3, 'Back': 2 }
  });

  curTopo = [1, 2, 5];
  trace.push({
    line: 18,
    activeV: 5,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v5',
    boundary: false,
    note: 'บันทึกจุดยอด 5 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1, 2, 5]',
    watch: { 'v': 'v5', 'topo_order': '[1, 2, 5]', 'len(topo_order)': 3 }
  });

  // Edge 5 -> 4
  trace.push({
    line: 21,
    activeV: 5,
    targetW: 4,
    activeEdge: [5, 4],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (5 → 4)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 5 → 4: ปลายทางคือเพื่อนบ้าน w = 4 (Indegree เดิม = 1)',
    watch: { 'v': 'v5', 'w': 'v4', 'indegree[4]': 1 }
  });

  curIndeg[4] = 0;
  trace.push({
    line: 22,
    activeV: 5,
    targetW: 4,
    activeEdge: [5, 4],
    indegrees: { ...curIndeg },
    decrementedW: 4,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(4)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 4 ลง 1: indegree[4] = 1 - 1 = 0',
    watch: { 'v': 'v5', 'w': 'v4', 'indegree[4]': 0 }
  });

  curQueue = [4];
  curQueueSlots[3] = 4;
  curBack = 3;
  curSize = 1;
  trace.push({
    line: 24,
    activeV: 5,
    targetW: 4,
    activeEdge: [5, 4],
    indegrees: { ...curIndeg },
    decrementedW: 4,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v4',
    boundary: false,
    note: 'indegree[4] กลายเป็น 0 แล้ว!  →  Enqueue(4) เข้าคิวช่อง [3] (Currentsize=1, Back=3)',
    watch: { 'v': 'v5', 'w': 'v4', 'Queue': '[4]', 'Currentsize': 1, 'Front': 3, 'Back': 3 }
  });

  // Edge 5 -> 7
  trace.push({
    line: 21,
    activeV: 5,
    targetW: 7,
    activeEdge: [5, 7],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (5 → 7)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 5 → 7: ปลายทางคือเพื่อนบ้าน w = 7 (Indegree เดิม = 2)',
    watch: { 'v': 'v5', 'w': 'v7', 'indegree[7]': 2 }
  });

  curIndeg[7] = 1;
  trace.push({
    line: 22,
    activeV: 5,
    targetW: 7,
    activeEdge: [5, 7],
    indegrees: { ...curIndeg },
    decrementedW: 7,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(7)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 7 ลง 1: indegree[7] = 2 - 1 = 1 (ยังไม่เป็น 0) — ประมวลผลเพื่อนบ้านของ v5 ครบถ้วน',
    watch: { 'v': 'v5', 'w': 'v7', 'indegree[7]': 1 }
  });

  // Iteration 4: Process v4
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 4)',
    boundary: true,
    note: 'วนลูป while รอบที่ 4: คิวมีจุดยอด [4] รออยู่',
    watch: { 'q.is_empty()': false, 'Queue': '[4]', 'Currentsize': 1 }
  });

  curQueue = [];
  curFront = 4;
  curSize = 0;
  trace.push({
    line: 17,
    activeV: 4,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v4',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [3]  →  ได้จุดยอด v = 4 (Front ขยับเป็น 4, Currentsize = 0)',
    watch: { 'v': 'v4', 'Queue': '[]', 'Currentsize': 0, 'Front': 4, 'Back': 3 }
  });

  curTopo = [1, 2, 5, 4];
  trace.push({
    line: 18,
    activeV: 4,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v4',
    boundary: false,
    note: 'บันทึกจุดยอด 4 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1, 2, 5, 4]',
    watch: { 'v': 'v4', 'topo_order': '[1, 2, 5, 4]', 'len(topo_order)': 4 }
  });

  // Edge 4 -> 6
  trace.push({
    line: 21,
    activeV: 4,
    targetW: 6,
    activeEdge: [4, 6],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (4 → 6)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 4 → 6: ปลายทางคือเพื่อนบ้าน w = 6 (Indegree เดิม = 3)',
    watch: { 'v': 'v4', 'w': 'v6', 'indegree[6]': 3 }
  });

  curIndeg[6] = 2;
  trace.push({
    line: 22,
    activeV: 4,
    targetW: 6,
    activeEdge: [4, 6],
    indegrees: { ...curIndeg },
    decrementedW: 6,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(6)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 6 ลง 1: indegree[6] = 3 - 1 = 2 (ยังไม่เป็น 0)',
    watch: { 'v': 'v4', 'w': 'v6', 'indegree[6]': 2 }
  });

  // Edge 4 -> 3
  trace.push({
    line: 21,
    activeV: 4,
    targetW: 3,
    activeEdge: [4, 3],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (4 → 3)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 4 → 3: ปลายทางคือเพื่อนบ้าน w = 3 (Indegree เดิม = 1)',
    watch: { 'v': 'v4', 'w': 'v3', 'indegree[3]': 1 }
  });

  curIndeg[3] = 0;
  trace.push({
    line: 22,
    activeV: 4,
    targetW: 3,
    activeEdge: [4, 3],
    indegrees: { ...curIndeg },
    decrementedW: 3,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(3)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 3 ลง 1: indegree[3] = 1 - 1 = 0',
    watch: { 'v': 'v4', 'w': 'v3', 'indegree[3]': 0 }
  });

  curQueue.push(3);
  curQueueSlots[4] = 3;
  curBack = 4;
  curSize += 1;
  trace.push({
    line: 24,
    activeV: 4,
    targetW: 3,
    activeEdge: [4, 3],
    indegrees: { ...curIndeg },
    decrementedW: 3,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v3',
    boundary: false,
    note: 'indegree[3] กลายเป็น 0 แล้ว!  →  Enqueue(3) เข้าคิวช่อง [4] (Currentsize=1, Back=4)',
    watch: { 'v': 'v4', 'w': 'v3', 'Queue': '[3]', 'Currentsize': curSize, 'Front': curFront, 'Back': curBack }
  });

  // Edge 4 -> 7
  trace.push({
    line: 21,
    activeV: 4,
    targetW: 7,
    activeEdge: [4, 7],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (4 → 7)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 4 → 7: ปลายทางคือเพื่อนบ้าน w = 7 (Indegree เดิม = 1)',
    watch: { 'v': 'v4', 'w': 'v7', 'indegree[7]': 1 }
  });

  curIndeg[7] = 0;
  trace.push({
    line: 22,
    activeV: 4,
    targetW: 7,
    activeEdge: [4, 7],
    indegrees: { ...curIndeg },
    decrementedW: 7,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(7)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 7 ลง 1: indegree[7] = 1 - 1 = 0',
    watch: { 'v': 'v4', 'w': 'v7', 'indegree[7]': 0 }
  });

  curQueue.push(7);
  curQueueSlots[5] = 7;
  curBack = 5;
  curSize += 1;
  trace.push({
    line: 24,
    activeV: 4,
    targetW: 7,
    activeEdge: [4, 7],
    indegrees: { ...curIndeg },
    decrementedW: 7,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v7',
    boundary: false,
    note: 'indegree[7] กลายเป็น 0 แล้ว!  →  Enqueue(7) เข้าคิวช่อง [5] — ตอนนี้คิวมี [3, 7] (Currentsize=2, Back=5)',
    watch: { 'v': 'v4', 'w': 'v7', 'Queue': '[3, 7]', 'Currentsize': curSize, 'Front': curFront, 'Back': curBack }
  });

  // Iteration 5: Process v3
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 5)',
    boundary: true,
    note: 'วนลูป while รอบที่ 5: คิวมีจุดยอด [3, 7] รออยู่ (ตามหลัก FIFO ดึง 3 ออกก่อน)',
    watch: { 'q.is_empty()': false, 'Queue': '[3, 7]', 'Currentsize': 2 }
  });

  curQueue.shift(); // remove 3
  curFront = 5;
  curSize -= 1;
  trace.push({
    line: 17,
    activeV: 3,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v3',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [4]  →  ได้จุดยอด v = 3 (Front ขยับเป็น 5, ในคิวเหลือ [7])',
    watch: { 'v': 'v3', 'Queue': '[7]', 'Currentsize': curSize, 'Front': curFront, 'Back': curBack }
  });

  curTopo.push(3);
  trace.push({
    line: 18,
    activeV: 3,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v3',
    boundary: false,
    note: 'บันทึกจุดยอด 3 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1, 2, 5, 4, 3]',
    watch: { 'v': 'v3', 'topo_order': '[1, 2, 5, 4, 3]', 'len(topo_order)': 5 }
  });

  // Edge 3 -> 6
  trace.push({
    line: 21,
    activeV: 3,
    targetW: 6,
    activeEdge: [3, 6],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (3 → 6)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 3 → 6: ปลายทางคือเพื่อนบ้าน w = 6 (Indegree เดิม = 2)',
    watch: { 'v': 'v3', 'w': 'v6', 'indegree[6]': 2 }
  });

  curIndeg[6] = 1;
  trace.push({
    line: 22,
    activeV: 3,
    targetW: 6,
    activeEdge: [3, 6],
    indegrees: { ...curIndeg },
    decrementedW: 6,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(6)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 6 ลง 1: indegree[6] = 2 - 1 = 1 (ยังไม่เป็น 0) — จุดยอด v3 ไม่มีเพื่อนบ้านอื่นแล้ว',
    watch: { 'v': 'v3', 'w': 'v6', 'indegree[6]': 1 }
  });

  // Iteration 6: Process v7
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 6)',
    boundary: true,
    note: 'วนลูป while รอบที่ 6: คิวมีจุดยอด [7] รออยู่',
    watch: { 'q.is_empty()': false, 'Queue': '[7]', 'Currentsize': 1 }
  });

  curQueue.shift(); // remove 7
  curFront = 6;
  curSize = 0;
  trace.push({
    line: 17,
    activeV: 7,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v7',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [5]  →  ได้จุดยอด v = 7 (Front ขยับเป็น 6, Currentsize = 0)',
    watch: { 'v': 'v7', 'Queue': '[]', 'Currentsize': 0, 'Front': 6, 'Back': 5 }
  });

  curTopo.push(7);
  trace.push({
    line: 18,
    activeV: 7,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v7',
    boundary: false,
    note: 'บันทึกจุดยอด 7 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1, 2, 5, 4, 3, 7]',
    watch: { 'v': 'v7', 'topo_order': '[1, 2, 5, 4, 3, 7]', 'len(topo_order)': 6 }
  });

  // Edge 7 -> 6
  trace.push({
    line: 21,
    activeV: 7,
    targetW: 6,
    activeEdge: [7, 6],
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'EXAMINE EDGE (7 → 6)',
    boundary: false,
    note: 'ตรวจเส้นเชื่อม 7 → 6: ปลายทางคือเพื่อนบ้าน w = 6 (Indegree เดิม = 1)',
    watch: { 'v': 'v7', 'w': 'v6', 'indegree[6]': 1 }
  });

  curIndeg[6] = 0;
  trace.push({
    line: 22,
    activeV: 7,
    targetW: 6,
    activeEdge: [7, 6],
    indegrees: { ...curIndeg },
    decrementedW: 6,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DECREMENT in(6)',
    boundary: false,
    note: 'ลดค่า Indegree ของ 6 ลง 1: indegree[6] = 1 - 1 = 0',
    watch: { 'v': 'v7', 'w': 'v6', 'indegree[6]': 0 }
  });

  curQueue.push(6);
  curQueueSlots[6] = 6;
  curBack = 6;
  curSize = 1;
  trace.push({
    line: 24,
    activeV: 7,
    targetW: 6,
    activeEdge: [7, 6],
    indegrees: { ...curIndeg },
    decrementedW: 6,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ENQUEUE v6',
    boundary: false,
    note: 'indegree[6] กลายเป็น 0 แล้ว!  →  Enqueue(6) เข้าคิวช่อง [6] (Currentsize=1, Back=6)',
    watch: { 'v': 'v7', 'w': 'v6', 'Queue': '[6]', 'Currentsize': 1, 'Front': 6, 'Back': 6 }
  });

  // Iteration 7: Process v6
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'WHILE LOOP (รอบ 7)',
    boundary: true,
    note: 'วนลูป while รอบที่ 7: คิวมีจุดยอด [6] รออยู่',
    watch: { 'q.is_empty()': false, 'Queue': '[6]', 'Currentsize': 1 }
  });

  curQueue.shift(); // remove 6
  curFront = 0; // wrap around to 0! (circular queue index 6+1 mod 7 = 0)
  curSize = 0;
  trace.push({
    line: 17,
    activeV: 6,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DEQUEUE v6',
    boundary: false,
    note: 'Dequeue หัวคิวช่อง [6]  →  ได้จุดยอด v = 6 (Front วนครบกลับมาเป็น 0! Currentsize = 0)',
    watch: { 'v': 'v6', 'Queue': '[]', 'Currentsize': 0, 'Front': 0, 'Back': 6 }
  });

  curTopo.push(6);
  trace.push({
    line: 18,
    activeV: 6,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'ORDER v6',
    boundary: false,
    note: 'บันทึกจุดยอด 6 ลงใน Topological Order  →  ลำดับปัจจุบัน: [1, 2, 5, 4, 3, 7, 6]',
    watch: { 'v': 'v6', 'topo_order': '[1, 2, 5, 4, 3, 7, 6]', 'len(topo_order)': 7 }
  });

  // v6 has no neighbors
  trace.push({
    line: 21,
    activeV: 6,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'SINK NODE v6',
    boundary: false,
    note: 'จุดยอด v6 เป็น Sink Node (ไม่มีเส้นชี้ออก, w ∈ ∅)  →  ไม่ต้องลด Indegree ของใคร',
    watch: { 'v': 'v6', 'graph[v6]': '[]', 'neighbors': 'Empty' }
  });

  // While loop check: queue is empty!
  trace.push({
    line: 16,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'QUEUE EMPTY',
    boundary: true,
    note: 'คิวว่างเปล่าแล้ว (q.is_empty() = True)  →  หลุดออกจากลูป while!',
    watch: { 'q.is_empty()': true, 'Currentsize': 0, 'Front': 0, 'Back': 6 }
  });

  // Cycle check
  trace.push({
    line: 26,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'DAG CHECK PASSED',
    boundary: false,
    note: 'ตรวจสอบ: len(topo_order) = 7 เท่ากับจำนวนจุดยอดทั้งหมด (|V| = 7)  →  กราฟนี้เป็น DAG ปราศจาก Cycle!',
    watch: { 'len(topo_order)': 7, '|V|': 7, 'Has Cycle': false }
  });

  // Return result
  trace.push({
    line: 28,
    activeV: null,
    targetW: null,
    activeEdge: null,
    indegrees: { ...curIndeg },
    decrementedW: null,
    queue: [...curQueue],
    queueSlots: [...curQueueSlots],
    front: curFront,
    back: curBack,
    currentSize: curSize,
    topoOrder: [...curTopo],
    badge: 'COMPLETE 100%',
    boundary: true,
    note: '✔ สิ้นสุดขั้นตอนวิธี Topological Sort สมบูรณ์! คำตอบข้อสอบ: 1, 2, 5, 4, 3, 7, 6 (ห้ามเขียนลูกศร -> เด็ดขาด)',
    watch: { 'Topological Order': '1, 2, 5, 4, 3, 7, 6', 'Result': 'Success' }
  });

  return trace;
}

const trace = buildTopologicalSortTrace();
console.log('Total steps generated:', trace.length);
console.log('Step 0:', trace[0].note);
console.log('Last step:', trace[trace.length - 1].note);
