# 6806021612037 Paphavin Thitichunhakun

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
    mylist = LinkedList()
    mylist.add(6)
    mylist.add(1)
    mylist.insert(2, 1)
    mylist.add(0)
    mylist.insert(3, 3)
    mylist.insert(7, 5)
    
    print(f"Output small to large : ", end = ""); mylist.getdata()

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
    print(f"Output after swap     : ", end = ""); mylist.getdata()
