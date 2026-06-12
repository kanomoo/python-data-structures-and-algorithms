# class Queue():
#     def __init__(self, limit = 5):
#         self.item = []
#         self.limit = limit
#         self.front = 0
#         self.rear = -1
#         self.size = 0
    
#     def isEmpty(self):
#         return self.size < 0
    
#     def enQueue(self, item):
#         self.item.append(item)
#         self.rear += 1
#         self.size += 1
    
#     def deQueue(self):
#         self.item.pop(0)
#         self.size = self.size - 1
#         self.rear = self.size - 1
    
#     def printqueue(self):
#         for i in range(self.size): 
#             print(self.item[i], end = " ")
#         print()
    
# if __name__ == "__main__":
#     myqueue = Queue(5)
#     myqueue.enQueue(3)
#     myqueue.enQueue(4)
#     myqueue.enQueue(5)
    
#     myqueue.printqueue()

#     myqueue.deQueue()
#     myqueue.deQueue()
#     print("After Dequeue")
#     myqueue.printqueue()





# class Queue:
#     def __init__(self, limit):
#         self.item = []
#         self.limit = limit
#         self.front = 0
#         self.rear = -1
#         self.size = 0

#     def isEmpty(self):
#         return self.size < 0
    
#     def enQueue(self, item):
#         if self.size > self.limit: return
#         self.item.append(item)
#         self.rear += 1
#         self.size += 1
    
#     def deQueue(self):
#         if not self.isEmpty(): return
#         self.item.pop(0)
#         self.rear -= 1
#         self.size -= 1

#     def printQueue(self):
#         for i in range(self.size): print(self.item[i], end = " ")
#         print()

# if __name__ == "__main__":
#     queue = Queue(5)
#     queue.deQueue()
#     print(queue.isEmpty())


class Queue():
    def __init__(self, limit):
        self.items = []
        self.limit = limit
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.size >= self.limit: print("Stack Overflow, Cannot enqueue", item)
        else: 
            self.items.append(item)
            self.rear += 1
            self.size += 1
    
    def dequeue(self):
        if self.isempty(): print("Stack Underflow")
        else: 
            self.items.pop(0)
            self.rear -= 1
            self.size -= 1
    
    def isempty(self):
        return self.size <= 0

    def printqueue(self):
        for i in range(self.size): print(self.items[i], end = " ")
        print()

if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.printqueue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.printqueue()
    queue.dequeue()

