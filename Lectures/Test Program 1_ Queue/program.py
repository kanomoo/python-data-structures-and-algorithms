#Paphavin Thitichunhakun 6806021612037
class Queue():
    def __init__(self, limit):
        self.items = []
        self.limit = limit
        self.front = 0
        self.rear = -1
        self.size = 0
        
    def isEmpty(self):
        return len(self.items) <= 0
    
    def enQueue(self, item):
        if len(self.items) >= self.limit: print("Queue is overflow")
        else: 
            self.items.append(item)
            self.rear += 1
            self.size += 1
    
    def deQueue(self):
        if self.isEmpty(): print("Queue is underflow")
        else: 
            self.items.pop(0)
            self.size = self.size - 1
            self.rear = self.size - 1
    
    def printqueue(self):
        for i in range(self.size):
            print(self.items[i], end = ' ')
        print()

if __name__ == "__main__":
    print("Paphavin Thitichunhakun 6806021612037")
    queue = Queue(5)
    queue.enQueue(6)
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(0)
    queue.enQueue(3)
    queue.printqueue()
    queue.enQueue(7)

    print("\nPaphavin Thitichunhakun 6806021612037")
    queue = Queue(6)
    queue.enQueue(6)
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(0)
    queue.enQueue(3)
    queue.enQueue(7)
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    queue.printqueue()
    queue.deQueue()
