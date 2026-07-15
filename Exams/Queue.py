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


# class Queue():
#     def __init__(self, limit):
#         self.items = []
#         self.limit = limit
#         self.front = 0
#         self.rear = -1
#         self.size = 0

#     def enqueue(self, item):
#         if self.size >= self.limit: print("Stack Overflow, Cannot enqueue", item)
#         else:
#             self.items.append(item)
#             self.rear += 1
#             self.size += 1
    
#     def dequeue(self):
#         if self.isempty(): print("Stack Underflow")
#         else:
#             self.items.pop(0)
#             self.rear -= 1
#             self.size -= 1
    
#     def isempty(self):
#         return self.size <= 0

#     def printqueue(self):
#         for i in range(self.size): print(self.items[i], end = " ")
#         print()

# if __name__ == "__main__":
#     # queue = Queue(5)
#     # queue.enqueue(1)
#     # queue.enqueue(2)
#     # queue.enqueue(3)
#     # queue.enqueue(4)
#     # queue.enqueue(5)
#     # queue.enqueue(6)
#     # queue.printqueue()
#     # queue.dequeue()
#     # queue.dequeue()
#     # queue.dequeue()
#     # queue.dequeue()
#     # queue.dequeue()
#     # queue.printqueue()
#     # queue.dequeue()
#     queue = Queue(10)
#     queue.enqueue(20)
#     queue.enqueue(30)
#     queue.enqueue(40)
#     queue.dequeue()
#     queue.enqueue(50)
#     queue.dequeue()
#     queue.enqueue(60)
#     queue.printqueue()


class Queue:
    def __init__(self, capacity):
        self.the_array = [None] * capacity
        self.current_size = 0
        self.front = 0
        self.back = 0

    def enQueue(self, item):
        if self.current_size < len(self.the_array):
            self.the_array[self.back] = item
            self.back = self._increment(self.back)
            self.current_size += 1
        else: print("Queue is Overflow")

    def deQueue(self):
        if not self.isEmpty():
            item = self.the_array[self.front]
            self.the_array[self.front] = None
            self.front = self._increment(self.front)
            self.current_size -= 1
            return item
        else: print("Queue is Underflow")

    def _increment(self, index):
        index += 1
        if index == len(self.the_array): index = 0
        return index
    
    def isEmpty(self):
        return self.current_size <= 0

    def print_queue(self):
        print("Queue: ", end = "")
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
    myqueue.enQueue(5)
    myqueue.enQueue(5)
    myqueue.enQueue(5)

    myqueue.print_queue()

    myqueue.deQueue()
    myqueue.deQueue()
    myqueue.deQueue()
    myqueue.deQueue()
    myqueue.deQueue()
    myqueue.deQueue()
    myqueue.print_queue()