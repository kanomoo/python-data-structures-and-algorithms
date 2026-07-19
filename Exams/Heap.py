# https://claude.ai/public/artifacts/3be9a554-8360-460f-9fad-c041859bccdb
# https://www.perplexity.ai/computer/a/8e421185-9a16-4483-9acd-9905f4bdd0c4

class BinaryHeap:
    def __init__(self, capacity = 100):
        # สร้าง list ที่มีขนาด capacity + 1 (index 0 ไม่ถูกใช้งาน)
        self.array = [None] * (capacity + 1)
        self.currentSize = 0
    
    def is_empty(self):
        return self.currentSize == 0

    def is_full(self):
        return self.currentSize == len(self.array) - 1
    
    def find_min(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.array[1]

    def insert(self, x):
        if self.is_full():
            print("Heap is full")
            return

        self.currentSize += 1
        hole = self.currentSize

        while hole > 1 and x < self.array[hole // 2]:
            self.array[hole] = self.array[hole // 2]
            hole //= 2
        self.array[hole] = x
    
    def delete_min(self):
        if self.is_empty():
            print("Heap is empty")
            return
        min_item = self.array[1]
        self.array[1] = self.array[self.currentSize]
        self.currentSize -= 1
        self._percolate_down(1)
        return min_item
    
    def _percolate_down(self, hole):
        temp = self.array[hole]
        while hole * 2 <= self.currentSize:
            child = hole * 2
            if child != self.currentSize and self.array[child + 1] < self.array[child]:
                child += 1
            if self.array[child] < temp:
                self.array[hole] = self.array[child]
            else:
                break
            hole = child
        self.array[hole] = temp
