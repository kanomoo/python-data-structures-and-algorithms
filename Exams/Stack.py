# class Stack:
#     def __init__(self, limit = 10):
#         self.items = []
#         self.limit = limit
    
#     def is_empty(self):
#         return len(self.items) <= 0
    
#     def push(self, items):
#         self.items.append(items)
    
#     def pop(self):
#         self.items.pop()

#     def top(self):
#         return self.items[len(self.items) - 1]
    
#     def size(self):
#         return len(self.items)
    
#     def printstack(self):
#         for i in range(len(self.items)): print(self.items[i], end = " ")




# class Stack:
#     def __init__(self, limit = 10):
#         pass
    
#     def is_empty(self):
#         pass
    
#     def push(self, items):
#         pass
    
#     def pop(self):
#         pass

#     def top(self):
#         pass
    
#     def size(self):
#         pass
    
#     def printstack(self):
#         pass



# class Stack:
#     def __init__(self, limit = 10):
#         self.items = []
#         self.limit = limit
    
#     def is_empty(self):
#         return len(self.items) <= 0
    
#     def push(self, items):
#         if len(self.items) >= self.limit: print("Stack Overflow, Cannot push ", items)
#         else: self.items.append(items)
    
#     def pop(self):
#         if len(self.items) <= 0: print("Stack Underflow")
#         else: return self.items.pop()

#     def top(self):
#         return self.items[len(self.items) - 1]
    
#     def size(self):
#         return len(self.items)
    
#     def printstack(self):
#         for i in range(len(self.items)): print(self.items[i], end = " ")
#         print()

# if __name__ == "__main__":
#     s = Stack(5)
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.push(5)
#     s.push(6)
#     print(f"Stack has data: ", end = "")
#     s.printstack()
#     print(f"Stack has size: {s.size()}\n")

#     s.pop()
#     s.pop()
#     print(f"Stach has data: ", end = "")
#     s.printstack()

#     print(f"Stach has data: ", end = "")
#     s.printstack()

#     s.pop()
#     s.pop()
#     s.pop()
#     s.printstack()
#     s.pop()



# class Stack:
#     def __init__(self, limit = 10):
#         self.items = []
#         self.limit = limit
    
#     def is_empty(self):
#         return len(self.items) <= 0
    
#     def push(self, items):
#         if len(self.items) >= self.limit: print("Stack Overflow, Cannot push ", items)
#         else: self.items.append(items)
    
#     def pop(self):
#         if len(self.items) <= 0: print("Stack Underflow")
#         else: return self.items.pop()

#     def top(self):
#         return self.items[len(self.items) - 1]
    
#     def size(self):
#         return len(self.items)
    
#     def printstack(self):
#         for i in range(len(self.items)): print(self.items[i], end = " ")
#         print()

# if __name__ == "__main__":
#     s = Stack(5)
#     s.push(6)
#     s.push(5)
#     s.push(s.pop() + s.pop())
#     s.printstack()
#     s.push(8)
#     s.push(s.pop() * s.pop())
#     s.printstack()




class Stack():
    def __init__(self, limit):
        self.items = []
        self.limit = limit
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) <= 0
    
    def top(self):
        return self.items[-1]
    
    def push(self, item):
        if self.size() >= self.limit: print("Stack Overflow, Cannot push", item)
        else: self.items.append(item)
    
    def pop(self):
        if self.is_empty(): print("Stack Underflow")
        else: self.items.pop()
    
    def printstack(self):
        for i in range(self.size()): print(self.items[i], end = " ")
        print()

if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.printstack()
    s.push(2)
    s.printstack()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
