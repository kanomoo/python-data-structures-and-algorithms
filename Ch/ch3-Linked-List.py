class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next : Node = None

    def get_data(self):
        return self.data

    def get_next(self) -> Node:
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def getdata(self):
        current = self.head
        if current != None:
            print(current.get_data(), end = " ")
            current = current.get_next()
        else:
            print("LinkedList is Empty")
            return
        while current != None:
            print(current.get_data(), end = " ")
            current = current.get_next()

    def insert(self, item, pos):
        current = self.head
        i = 0
        previous = None
        temp = Node(item)
        for i in range(pos):
            previous = current
            current = current.get_next()
        temp.set_next(current)
        previous.set_next(temp)


if __name__ == "__main__":
    mylist = LinkedList()

#  1
    # mylist.add(10)
    # mylist.insert(20, 1)
    # mylist.insert(30, 2)
    # mylist.getdata()

# 2 

    # mylist.add(4)
    # mylist.add(3)
    # mylist.add(2)
    # mylist.add(1)

    # mylist.remove(1)
    # mylist.getdata()

# 3

    # mylist.add("D")
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # mylist.remove("B")
    # mylist.insert("B", 2)
    # mylist.getdata()

#  4

    # mylist.add(3)
    # mylist.add(1)
    # mylist.add(2)
    # mylist.add(1)

    # mylist.remove(1)
    # mylist.getdata()

# 5

    # mylist.add(3)
    # mylist.add(1)
    # mylist.add(2)
    # mylist.add(1)

    # mylist.remove(1)
    # mylist.remove(1)
    # mylist.add(1)
    # mylist.getdata()

# 6

    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # node = mylist.head
    # node.next = node.next.next
    # mylist.getdata()

# 7

    # mylist.add("D")
    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # node = mylist.head
    # node.next = node.next.next.next
    # mylist.getdata()

# 8

    # mylist.add("C")
    # mylist.add("B")
    # mylist.add("A")

    # temp = Node("X")
    # node = mylist.head
    # temp.next = node.next
    # node.next = temp
    # mylist.getdata()


# For example 1

    # mylist = LinkedList()
    # mylist.add(1)
    # mylist.insert(2, 1)
    # mylist.insert(3, 2)
    # mylist.insert(4, 3)
    # mylist.insert(5, 4)
    # mylist.getdata()

# For example 2

    # mylist.add(3)

    # mylist.add(1)
    # mylist.insert(2, 1)
    # mylist.insert(4, 3)
    # mylist.insert(5, 4)
    # mylist.getdata()

# For example 2. 3

    mylist.add(3)

    mylist.add(1)
    mylist.insert(2, 1)
    mylist.insert(4, 3)
    mylist.insert(5, 4)

    node1 = mylist.head
    node2 = node1.next
    node3 = node2.next
    node4 = node3.next
    node5 = node4.next

    node1.next = node4 # 1 (4->5) 2 3
    node3.next = node2 # 1 (4->5) -> (3->2)
    node4.next = node3 # 1 4 3 (2->3) | 5->None
    node2.next = node5 # 1 4 3 2 5

    mylist.getdata()



# Assign 1: Linked List
#     68060216 120347

    mylist = LinkedList()
    mylist.add(1)        # 1
    mylist.insert(2, 1)  # 1 2
    mylist.add(0)        # 0 1 2
    mylist.insert(3, 3)  # 0 1 2 3
    mylist.insert(4, 4)  # 0 1 2 3 4
    mylist.insert(7, 5)  # 0 1 2 3 4 7

    node1 = mylist.head
    node2 = node1.next
    node3 = node2.next
    node4 = node3.next
    node5 = node4.next
    node6 = node5.next

    node6.next = node2
    node5.next = node1
    node1.next = None
    mylist.head = node6

    mylist.getdata()
