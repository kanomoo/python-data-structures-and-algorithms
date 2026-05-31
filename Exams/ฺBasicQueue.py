# First in first out
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = deque()
    
#     def enqueue(self, order):
#         self.queue.append(order)
    
#     def dequeue(self):
#         if not self.is_empty(): self.queue.popleft()
    
#     def is_empty(self):
#         return len(self.queue) == 0

#     def display_queue(self):
#         for order in self.queue: print(order)

# if __name__ == "__main__":
#     queue = Queue()
#     queue.enqueue("apple")
#     queue.enqueue("banana")
#     queue.enqueue("orange")
#     queue.display_queue()

#     print()
#     queue.dequeue()
#     queue.display_queue()


class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0) # ไม่จำเป็นต้องมี return ก็ได้
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def getFront(self):
        return self.queue[0]
    
    def display(self):
        for i in self.queue:
            print(i)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Test1")
    queue.enqueue("Test2")
    queue.enqueue("Test3")
    queue.display()

    print()
    queue.dequeue()
    queue.display()
