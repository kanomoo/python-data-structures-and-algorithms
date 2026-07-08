# class Node:
#     def __init__(self, init_data):
#         self.data = init_data
#         self.next = None

#     def get_data(self):
#         return self.data

#     def set_data(self, new_data):
#         self.data = new_data
    
#     def get_next(self):
#         return self.next
    
#     def set_next(self, new_next):
#         self.next = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def is_empty(self):
#         return self.head == None
    
#     def add(self, item):
#         temp = Node(item)
#         temp.set_next(self.head)
#         self.head = temp
    
#     def search(self, item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.get_data() == item: found = True
#             else: current = current.get_next()
#         return found
    
#     def remove(self, item):
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.get_data() == item: found = True
#             else:
#                 previous = current
#                 current = current.get_next()
#         if not found: return
#         if previous == None: self.head = current.get_next()
#         else: previous.set_next(current.get_next())

#     def getdata(self):
#         current = self.head
#         if current != None:
#             print(current.get_data() , end = " ")
#             current = current.get_next()
#         else:
#             print("LinkedList is Empty")
#             return

#         while current != None:
#             print(current.get_data() , end = " ")
#             current = current.get_next()
#         print()

#     def insert(self, item, pos):
#         current = self.head
#         previous = None
#         temp = Node(item)
#         for _ in range(pos):
#             previous = current
#             current = current.get_next()
#         temp.set_next(current)
#         previous.set_next(temp)

# if __name__ == "__main__":
#     myList = LinkedList()
#     data = [96, 42, 18, 23, 77]
#     for i in data: myList.add(i)

#     print(myList.search(42))

#     myList.remove(42)
#     myList.getdata()

#     myList.insert(32, 3)
#     myList.getdata()





# class Node:
#     def __init__(self, init_data):
#         pass

#     def get_data(self):
#         pass

#     def set_data(self, new_data):
#         pass
    
#     def get_next(self):
#         pass
    
#     def set_next(self, new_next):
#         pass

# class LinkedList:
#     def __init__(self):
#         pass
    
#     def is_empty(self):
#         pass
    
#     def add(self, item):
#         pass
    
#     def search(self, item):
#         pass
    
#     def remove(self, item):
#         pass

#     def getdata(self):
#         pass

#     def insert(self, item, pos):
#         pass

# if __name__ == "__main__":
#     pass





# class Node:
#     def __init__(self, init_data):
#         self.data, self.next = init_data, None
    
#     def get_data(self):
#         return self.data

#     def set_data(self, new_data):
#         self.data = new_data
    
#     def get_next(self):
#         return self.next
    
#     def set_next(self, new_next):
#         self.next = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def add(self, item):
#         temp = Node(item)
#         temp.set_next(self.head)
#         self.head = temp
    
#     def search(self, item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.get_data() == item: found = True
#             else: current = current.get_next()
#         return found
    
#     def remove(self, item):
#         previous = None
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.get_data() == item: found = True
#             else:
#                 previous = current
#                 current = current.get_next()
#         if not found: return
#         if previous == None: self.head = current.get_next()
#         else: previous.set_next(current.get_next())

#     def getdata(self):
#         current = self.head
#         if self.head != None:
#             print(current.get_data(), end = " ")
#             current = current.get_next()
#         else: print("LinkLinked is Empty", end = "")

#         while current != None:
#             print(current.get_data(), end = " ")
#             current = current.get_next()
#         print()

#     def insert(self, item, pos):
#         previous = None
#         current = self.head
#         temp = Node(item)
#         if current == None: return
#         for _ in range(pos):
#             previous = current
#             current = current.get_next()
#         previous.set_next(temp)
#         temp.set_next(current)


# if __name__ == "__main__":
#     myList = LinkedList()
#     List = [96, 42, 18, 23, 77]
#     for i in List: myList.add(i)

#     print(myList.search(96))
#     myList.getdata()

#     myList.remove(77)
#     myList.getdata()

#     myList.insert(34, 2)
#     myList.getdata()






class Node:
    def __init__(self, init_data):
        self.data, self.next = init_data, None
    
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self) -> Node:
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def search(self, item) -> str:
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item: found = True
            else: current = current.get_next()
        return print(found)
    
    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item: found = True
            else:
                previous = current
                current = current.get_next()
        if not found: return
        elif previous == None: self.head = current.get_next()
        else: previous.set_next(current.get_next())

    def getdata(self):
        current = self.head
        if current != None:
            print(current.get_data(), end = " ")
            current = current.get_next()
        else: print("LinkedList is empty")
        while current != None:
            print(current.get_data(), end = " ")
            current = current.get_next()
        print()

    def insert(self, item, pos):
        if pos == 0:
            self.add(item)
            return
        previous = None
        current = self.head
        temp = Node(item)
        for _ in range(pos):
            if current is None: raise ValueError("index out of range")
            previous = current
            current = current.get_next()
        previous.set_next(temp)
        temp.set_next(current)


if __name__ == "__main__":
    # myList = LinkedList()
    # myList.add(96)
    # myList.add(42)
    # myList.add(18)
    # myList.add(23)
    # myList.add(77)
    # myList.search(18)
    # myList.insert(32, 2)
    # myList.getdata()mylist.head


    # mylist = LinkedList()
    # mylist.add(10)
    # mylist.insert(20, 1)
    # mylist.insert(30, 2)
    # mylist.getdata()



    # mylist = LinkedList()
    # mylist.add("D")
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # mylist.remove("B")
    # mylist.insert("B", 2)
    # mylist.getdata()



    # mylist = LinkedList()
    # mylist.add(3)
    # mylist.add(1)
    # mylist.add(2)
    # mylist.add(1)

    # mylist.remove(1)
    # mylist.getdata()



    # mylist = LinkedList()
    # mylist.add(3)
    # mylist.add(1)
    # mylist.add(2)
    # mylist.add(1)

    # mylist.remove(1)
    # mylist.remove(1)
    # mylist.add(1)
    # mylist.getdata()




    # mylist = LinkedList()
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")
    
    # mylist.head.next.next = mylist.head.get_next().get_next().get_next()
    # mylist.getdata()



    # mylist = LinkedList()
    # mylist.add("D")
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")
    
    # current_node : Node = mylist.head
    # current_node.next = current_node.next.next.next
    # mylist.getdata()


    # mylist = LinkedList()
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # mylist.remove("A")
    # mylist.add("X")
    # mylist.add("A")
    # mylist.getdata()


    # mylist = LinkedList()
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # mylist.remove("A")
    # mylist.add("X")
    # mylist.add("A")
    # mylist.getdata()



    # mylist = LinkedList()
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # node = Node("X")
    # node.set_next(mylist.head.get_next())
    # mylist.head.set_next(node)
    
    # mylist.getdata()

    # 6806021 612037
    mylist = LinkedList()
    mylist.add(6)
    mylist.add(1)
    mylist.insert(2, 1)
    mylist.add(0)
    mylist.insert(3, 3)
    mylist.insert(7, 5)
    
    # 0 1 2 3 6 7

    current_node = mylist.head
    node1 = mylist.head
    node2 = node1.get_next()
    node3 = node2.get_next()
    node4 = node3.get_next()
    node5 = node4.get_next()
    node6 = node5.get_next()

    node6.set_next(node2)
    node5.set_next(node1)
    node1.set_next(None)
    mylist.head = node6
    mylist.getdata()