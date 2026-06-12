class Stack:
    def __init__(self, limit):
        self.items = []
        self.limit = limit
    
    def size(self) -> int:
        return len(self.items)

    def is_empty(self):
        return self.size() <= 0
    
    def top(self):
        return self.items[-1]

    def push(self, item):
        if self.size() >= self.limit: print("Stack Overflow, Cannot push", item)
        elif str(item) in "+-*/":
            match item:
                case "+": self.items.append(self.pop() + self.pop())
                case "-": self.items.append(self.pop() - self.pop())
                case "*": self.items.append(self.pop() * self.pop())
                case "/": self.items.append(self.pop() / self.pop())
        else: self.items.append(item)
    
    def pop(self):
        if self.is_empty(): print("Stack Underflow")
        else: return self.items.pop()

    def printstack(self):
        for i in range(self.size()): print(self.items[i], end = " ")
        print()



if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.printstack()
    s.push(6)

    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.printstack()
    s.pop()

    s.push(6)
    s.push(5)
    s.push(2)
    s.push(3)
    s.push("+")
    s.push(8)
    s.push("*")
    s.push("+")
    s.push(3)
    s.push("+")
    s.push("*")
    s.printstack()