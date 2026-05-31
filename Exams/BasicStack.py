# List in first out
# def reverse_word(word):
#     stack = []
#     for letter in word: stack.append(letter)
#     reversed_word = ""
#     while stack: reversed_word += stack.pop()
#     return reversed_word

# print(reverse_word(input("Enter a word to reverse: ")))

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop() # ไม่จำเป็นต้องมี return ก็ได้

    def isEmpty(self):
        return len(self.stack) == 0

    def getTop(self):
        return self.stack[-1]
    
    def display(self):
        for i in self.stack:
            print(i)

if __name__ == "__main__":
    stack = Stack()
    stack.push("Test1")
    stack.push("Test2")
    stack.push("Test3")
    stack.display()

    print()
    stack.pop()
    stack.display()