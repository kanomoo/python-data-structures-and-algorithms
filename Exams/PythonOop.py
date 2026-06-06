# # Encapsulation

# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.__name = name
#         self.__surname = surname
    
#     def toString(self) -> str:
#         return f"{self.__name}, {self.__surname}"

# if __name__ == "__main__":
#     person = Person("Paphavin", "Thitichunhakun")
#     print(person.toString())



# # Encapsulation : Underscore accessing

# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.__name = name
#         self.__surname = surname
    
#     def toString(self) -> str:
#         return f"{self.__name}, {self.__surname}"
    
# if __name__ == "__main__":
#     person = Person("Paphavin", "Thitichunhakun")
#     print(person.toString())
#     person._Person__name, person._Person__surname = "Name", "Surname"
#     print(person.toString())



# # Encapsulation : Getter & Setter

# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.__name = name
#         self.__surname = surname

#     def setName(self, name: str) -> None:
#         self.__name = name
    
#     def getName(self) -> str:
#         return self.__name
    
#     def setSurname(self, surname: str) -> None:
#         self.__surname = surname

#     def getSurname(self) -> str:
#         return self.__surname
    
#     def toString(self) -> str:
#         return f"{self.__name}, {self.__surname}"


# if __name__ == "__main__":
#     person = Person("Paphavin", "Thitichunhakun")
#     print(person.toString())
#     person.setName("Name"); person.setSurname("Surname")
#     print(person.toString())



# # Encapsulation : Property

# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.__name = name
#         self.__surname = surname

#     @property
#     def name(self) -> str:
#         return self.__name

#     @name.setter
#     def name(self, name: str) -> None:
#         self.__name = name
    
#     @property
#     def surname(self) -> str:
#         return self.__surname
    
#     @surname.setter
#     def surname(self, surname: str) -> None:
#         self.__surname = surname

    
#     def toString(self) -> str:
#         return f"{self.__name}, {self.__surname}"
    


# if __name__ == "__main__":
#     person = Person("Paphavin", "Thitichunhakun")
#     print(person.toString())
#     person.name, person.surname = "Name", "Surname"
#     print(person.toString())



# from Student import *

# if __name__ == "__main__":
#     std = Student("6806021612037", "Paphavin Thitichunhakun", 85)
#     print(std.toGrade())
#     std.id, std.name, std.score = "6806021611022", "Thitichunhakun Paphavin", 50
#     print(std.toGrade())




# # Static class

# class Employee:
#     count = 0 # static variable

#     def __init__(self, name: str, salary: int) -> None:
#         self.name, self.salary = name, salary
    
#     @staticmethod
#     def getCount(): #static method
#         return Employee.count 

# if __name__ == "__main__":
#     print(Employee.getCount())




# # Inheritance
# class Person:
#     def __init__(self, name):
#         self.__name = name
    
#     def setName(self, name):
#         self.__name = name
    
#     def getName(self):
#         return self.__name

# class Student(Person):
#     def __init__(self, name, gpa):
#         super().__init__(name)
#         self.__gpa = gpa
    
#     def setGpa(self, gpa):
#         self.__gpa = gpa
    
#     def getGpa(self):
#         return self.__gpa
    

# if __name__ == "__main__":
#     std = Student("Somchai", 3.10)
#     print(std.getName(), std.getGpa())






# # Overriding
# class Person:
#     def __init__(self, name):
#         self.__name = name
    
#     def setName(self, name):
#         self.__name = name
    
#     def getName(self):
#         return self.__name
    
#     def toString(self):
#         return self.__name

# class Student(Person):
#     def __init__(self, name, gpa):
#         super().__init__(name)
#         self.__gpa = gpa
    
#     def setGpa(self, gpa):
#         self.__gpa = gpa
    
#     def getGpa(self):
#         return self.__gpa
    
#     def toString(self):
#         return super().toString() , str(self.__gpa)

# if __name__ == "__main__":
#     std = Student("Somchai", 3.10)
#     print(std.toString())




# # Stack
# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def isEmpty(self):
#         return len(self.items) == 0
    
#     def push(self, item):
#         self.items.append(item)
    
#     def pop(self):
#         if not self.isEmpty():
#             return self.items.pop()
#         return None

#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1]
#         return None

#     def size(self):
#         return len(self.items)
    
#     def __str__(self):
#         return f"Stack: {self.items}"
    
# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(10)
#     stack.push(20)
#     stack.push(30)
#     print(stack)
#     print(stack.size())
#     print(stack.peek())

#     stack.pop()
#     print(stack)



# Queue
class Queue:

    def __init__(self):
        self.item = []
    
    def isEmpty(self):
        return len(self.item) == 0

    def enqueue(self, item):
        self.item.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            self.item.pop(0)
        return None
    
    def peek(self):
        if not self.isEmpty():
            self.item[0]
        return None
    
    def size(self):
        return len(self.item)
    
    def __str__(self):
        return str(self.item)
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q)

    q.dequeue()
    print(q)