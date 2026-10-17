class Queue():
    def __init__(self, capacity):
        self.the_array = [None] * capacity
        self.current_size = 0
        self.front = 0
        self.back = 0

    def enQueue(self, item):
        self.the_array[self.back] = item
        self.back = self._increment(self.back)
        self.current_size += 1
        
    def _increment(self, index):
        index += 1
        if index == len(self.the_array):
            index = 0
        return index

    def dequeue(self):
        item = self.the_array[self.front]
        self.the_array[self.front] = None
        self.front = self._increment(self.front)
        self.current_size -= 1
        return item

    def print_queue(self):
        print("ข้อมูลใน queue: ", end = "")
        curr = self.front
        for _ in range(self.current_size):
            print(self.the_array[curr], end = " ")
            curr = self._increment(curr)
        print()

if __name__ == "__main__":
    myqueue = Queue(5)
    myqueue.enQueue(3)
    myqueue.enQueue(4)
    myqueue.enQueue(5)

    myqueue.print_queue()

    myqueue.dequeue()
    myqueue.dequeue()
    print("After Dequeue")

    myqueue.print_queue()

    myqueue.enQueue(12)
    myqueue.enQueue(13)
    myqueue.enQueue(14)
    myqueue.enQueue(14)
    myqueue.enQueue(14)
    myqueue.print_queue()