# class Node:
#     def __init__(self, dataVal = None):
#         self.dataVal = dataVal
#         self.nextVal = None
    

# class SLinkedList:
#     def __init__(self):
#         self.headVal = None

#     def listPrint(self):
#         printVal = self.headVal
#         while printVal is not None:
#             print(printVal.dataVal)
#             printVal = printVal.nextVal

# if __name__ == "__main__":
#     List = SLinkedList()
#     List.headVal = Node("January")
#     n2, n3, n4 = Node("February"), Node("March"), Node("April")
    
#     List.headVal.nextVal = n2
#     n2.nextVal, n3.nextVal = n3, n4

#     List.listPrint()



class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

if __name__ == "__main__":
    List = SLinkedList()
    node = Node("1")
    n2 = Node("2")
    
    List.head = node
    node.next = n2

    List.display()