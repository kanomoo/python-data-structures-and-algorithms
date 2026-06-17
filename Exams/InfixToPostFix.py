#  https://gemini.google.com/share/cc48e0f025be

#  https://gemini.google.com/share/8746e44a615d

class Stack:
    def __init__(self, limit = 100) -> None:
        self.items = []
        self.limit = limit
    
    def size(self) -> int:
        return len(self.items)

    def isEmpty(self) -> bool:
        return self.size() <= 0

    def top(self):
        if self.isEmpty(): return None
        return self.items[-1]
    
    def push(self, item):
        if self.size() >= self.limit: return print("Stack Overflow, Cannot push", item)
        else: self.items.append(item)
    
    def pop(self):
        if self.isEmpty(): return print("Stack Underflow")
        else: return self.items.pop()

    def printStack(self):
        for i in range(self.size()): print(self.items[i], end = " ")
        print()


# เขียนแบบใช้ for loop ใช้การได้เกือบถูกยกเว้นระดับความสำคัญของ item เท่ากัน เมื่อ stack มีหลายระดับ จะ bug
# class ConversionInfixToPostfix:
#     def __init__(self):
#         self.stack = Stack()
#         self.items = self.stack.items
#         self.indexParentheses = []
#         self.result = []

#     def precedence(self, item) -> int:
#         if item == "^": return 3
#         elif item in "*/": return 2
#         elif item in "+-": return 1
#         else: return 0
    
#     def push(self, item: str):
#         if item.isalpha(): self.result.append(item)
#         elif item in "()" or len(self.indexParentheses) > 0:
#             match item:
#                 case "(":
#                     self.stack.push(item)
#                     self.indexParentheses.append(self.stack.size() - 1)
#                 case ")":
#                     for _ in range(self.stack.size() - self.indexParentheses[-1] - 1): 
#                             self.result.append(self.stack.pop())
#                     self.indexParentheses.pop()
#                     self.stack.pop()
#                 case _:
#                     if self.precedence(item) > self.precedence(self.stack.top()): self.stack.push(item)
#                     elif self.precedence(item) == self.precedence(self.stack.top()):
#                         self.result.append(self.stack.pop())
#                         self.stack.push(item)
#                     else:
#                         for _ in range(self.stack.size() - self.indexParentheses[-1] - 1): 
#                             if self.precedence(item) > self.precedence(self.stack.top()): self.result.append(self.stack.pop())
#                         self.stack.push(item)
#         elif item in "^*/+-()":
#             if self.stack.isEmpty() or self.precedence(item) > self.precedence(self.stack.top()): self.stack.push(item) 
#             elif self.precedence(item) == self.precedence(self.stack.top()):
#                 self.result.append(self.stack.pop())
#                 self.stack.push(item)
#             else: 
#                 for _ in range(self.stack.size()): 
#                     if self.precedence(item) > self.precedence(self.stack.top()): self.result.append(self.stack.pop())
#                 self.stack.push(item)

#     def pushShow(self, item):
#         self.push(item)
#         self.stack.printStack()
#         self.printResult()
#         print("--")

#     def pushText(self, item):
#         for i in item: self.push(i)
#         for _ in range(self.stack.size()): self.result.append(self.stack.pop())

#     def printResult(self):
#         # for i in range(len(self.result)): print(self.result[i], end = " ")
#         # print()
#         print(*self.result)


class ConversionInfixToPostfix:
    def __init__(self):
        self.stack = Stack()
        self.items = self.stack.items
        self.indexParentheses = []
        self.result = []

    def precedence(self, item) -> int:
        if item == "^": return 3
        elif item in "*/": return 2
        elif item in "+-": return 1
        else: return 0
    
    def push(self, item: str):
        if item.isalpha(): self.result.append(item)
        elif item in "()" or len(self.indexParentheses) > 0:
            match item:
                case "(":
                    self.stack.push(item)
                    self.indexParentheses.append(self.stack.size() - 1)
                case ")":
                    for _ in range(self.stack.size() - self.indexParentheses[-1] - 1): 
                            self.result.append(self.stack.pop())
                    self.indexParentheses.pop()
                    self.stack.pop()
                case _:
                    while self.stack.size() > self.indexParentheses[-1] + 1 and self.precedence(self.stack.top()) >= self.precedence(item):
                        self.result.append(self.stack.pop())
                    self.stack.push(item)
        elif item in "^*/+-()":
            while not self.stack.isEmpty() and self.precedence(self.stack.top()) >= self.precedence(item):
                self.result.append(self.stack.pop())
            self.stack.push(item)

    def pushShow(self, item):
        self.push(item)
        self.stack.printStack()
        self.printResult()
        print("--")

    def pushText(self, item):
        for i in item: self.push(i)
        # for _ in range(self.stack.size()): self.result.append(self.stack.pop())
        while not self.stack.isEmpty(): self.result.append(self.stack.pop())

    def printResult(self):
        # for i in range(len(self.result)): print(self.result[i], end = " ")
        # print()
        print(*self.result)


    
if __name__ == "__main__":
    # s = Stack(5)
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # s.push(4)
    # s.push(5)
    # s.printStack()
    # s.push(6)

    # s.pop()
    # s.pop()
    # s.pop()
    # s.pop()
    # print(s.top())
    # s.pop()
    # s.printStack()
    # s.pop()

    con = ConversionInfixToPostfix()
    # con.pushShow("a")
    # con.pushShow("+")
    # con.pushShow("b")
    # con.pushShow("*")
    # con.pushShow("c")
    # con.pushShow("+")
    # con.pushShow("(")
    # con.pushShow("d")
    # con.pushShow("*")
    # con.pushShow("e")
    # con.pushShow("+")
    # con.pushShow("f")
    # con.pushShow(")")
    # con.pushShow("*")
    # con.pushShow("g")
    
    # con.pushText("a+b*c+(d*e+f)*g")
    # con.printResult()

    con.pushText("((a+b)*c)-d")
    con.printResult()