class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data
    
    def get_next(self):
        return self.next
    
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
            if current.get_data() == item: found = True
            else: current = current.get_next()
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item: found = True
            else:
                previous = current
                current = current.get_next()
        if not found: return
        if previous == None: current = current.get_next()
        else: previous.set_next(current.get_next())

    def getdata(self):
        current = self.head
        if current != None:
            print(current.get_data() , end = " ")
            current = current.get_next()
        else:
            print("LinkedList is Empty")
            return

        while current != None:
            print(current.get_data() , end = " ")
            current = current.get_next()
        print()

    def insert(self, item, pos):
        current = self.head
        previous = None
        temp = Node(item)
        for _ in range(pos):
            previous = current
            current = current.get_next()
        temp.set_next(current)
        previous.set_next(temp)

if __name__ == "__main__":
    myList = LinkedList()
    data = [96, 42, 18, 23, 77]
    for i in data: myList.add(i)

    print(myList.search(42))

    myList.remove(42)
    myList.getdata()

    myList.insert(32, 3)
    myList.getdata()
