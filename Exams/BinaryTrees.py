# class Node:
#     def __init__(self, value: str) -> None:
#         self.value = value
#         self.left = None
#         self.right = None

# class Stack:
#     def __init__(self, limit = 100):
#         self.items = []
#         self.limit = limit
    
#     def size(self):
#         return len(self.items)
    
#     def isEmpty(self):
#         return self.size() <= 0
    
#     def top(self):
#         return self.items[-1]
    
#     def push(self, item):
#         if self.size() >= self.limit: print("Stack Overflow, Cannot push", item)
#         else: self.items.append(item)
    
#     def pop(self):
#         if self.isEmpty(): print("Stack Underflow")
#         else: return self.items.pop()
    
#     def printStack(self):
#         print(*self.items)

# def isOrder(char: str) -> bool:
#     return char in "+-*/^"

# def constructingExpressionTree(postfix: str) -> Node:
#     stack = Stack()
#     for symbol in postfix:
#         if not isOrder(symbol):
#             node = Node(symbol)
#             stack.push(node)
#         else:
#             t2 = stack.pop()
#             t1 = stack.pop()
#             new_tree = Node(symbol)
#             new_tree.left = t1
#             new_tree.right = t2
#             stack.push(new_tree)
#     return stack.pop()

# def inorder_traversal(root: Node) -> str:
#     if root is not None:
#         if isOrder(root.value):
#             print("(", end = "")
        
#         inorder_traversal(root.left)
#         print(root.value, end = "")
#         inorder_traversal(root.right)

#         if isOrder(root.value):
#             print(")", end = "")



# if __name__ == "__main__":
#     postfix_input = "ab+cde+**"

#     print(f"Input Postfix: {postfix_input}")

#     root_node = constructingExpressionTree(postfix_input)

#     print("Output Infix(Inorder Traversal): ", end = "")
#     inorder_traversal(root_node)
#     print()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Stack:
    def __init__(self, limit = 100):
        self.items = []
        self.limit = limit

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() <= 0

    def top(self):
        return self.items[-1]

    def push(self, item):
        if self.size() >= self.limit: print("Stack Overflow, Cannot push", item)
        else: self.items.append(item)

    def pop(self):
        if self.isEmpty(): print("Stack Underflow")
        else: return self.items.pop()

    def printStack(self):
        print(*self.items)

def isOperator(char):
    return char in "+-*/^"

def constructingExpressionTree(postfix):
    stack = Stack()
    for symbol in postfix:
        if not isOperator(symbol):
            node = Node(symbol)
            stack.push(node)
        else:
            t2 = stack.pop()
            t1 = stack.pop()
            
            new_node = Node(symbol)
            new_node.left = t1
            new_node.right = t2
            stack.push(new_node)

    return stack.pop()

def inorder_traversal(root: Node):
    if root is not None:
        if isOperator(root.value):
            print("(", end = "")

        inorder_traversal(root.left)
        print(root.value, end = "")
        inorder_traversal(root.right)

        if isOperator(root.value):
            print(")", end = "")

def preOrder(root: Node) -> str: # root left right
    pass

def inOrder(root: Node) -> str: # left root right
    pass

def postOrder(root: Node) -> str: # left right root
    pass


if __name__ == "__main__":
    tree = constructingExpressionTree("ab+cde+**")
    inorder_traversal(tree)
    preOrder(tree)




