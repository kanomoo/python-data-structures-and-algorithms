# First in first out
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, order):
        self.queue.append(order)
    
    def dequeue(self):
        if not self.is_empty(): self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        for order in self.queue: print(order)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("apple")
    queue.enqueue("banana")
    queue.enqueue("orange")
    queue.display_queue()

    print()
    queue.dequeue()
    queue.display_queue()