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





# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head: # None มีค่าเป็น False
#             self.head = new_node
#             return
        
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def display(self):
#         nodes = []
#         current = self.head
#         while current:
#             nodes.append(str(current.data))
#             current = current.next
#         print(" -> ".join(nodes) if nodes else "List is empty")

# if __name__ == "__main__":
#     my_list = SLinkedList()
    
#     for month in ["January", "February", "March", "April"]:
#         my_list.append(month)

#     my_list.display()