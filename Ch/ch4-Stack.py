class Stack:
    def __init__(self, limit = 10):
        self.items = []
        self.limit = limit

    def is_empty(self):
        return len(self.items) <= 0

    # def push(self, item):
    #     self.items.append(item)

    def push(self, item):
        if len(self.items) >= self.limit:
            print("Stack Overflow, Cannot push ", item)
        else:
            self.items.append(item)

    # def pop(self):
    #     return self.items.pop()

    def pop(self):
        if len(self.items) <= 0:
            print("Stack Underflow")
        else:
            return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printstack(self):
        for i in range(len(self.items)):
            print(self.items[i], end = " ")

if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.printstack()
    print("\nSize:", s.size())

    s.pop()
    s.pop()
    s.printstack()
    print("\nSize:", s.size())

