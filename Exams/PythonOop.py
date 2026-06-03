# class Person:
#     def __init__(self, name, surname):
#         self.__name = name # Private
#         self.__surname = surname
    
#     def toString(self):
#         return f"{self.__name}, {self.__surname}"


## Encapsulation : Underscore accessing
# if __name__ == "__main__":
#     p1 = Person("Somchai", "cheingpongpan")
#     p2 = Person("Jason", "Smith")
#     print(p1.toString())
#     print(p2.toString())
#     p1._Person__name = "test" # Private
#     p1.__name = "TEST" #ประกาศไม่ถูก
#     print(p1.toString())


## Encapsulation : Getter & Setter
# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.__name, self.__surname = name, surname

#     def setName(self, name: str) -> None:
#         self.__name = name
    
#     def getName(self) -> str:
#         return self.__name
    
#     def setSurname(self, surname: str) -> None:
#         self.__surname = surname
    
#     def getSurname(self) -> str:
#         return self.__surname
    
#     def toString(self) -> str:
#         return f"{self.getName()}, {self.getSurname()}"

# if __name__ == "__main__":
#     person = Person("Paphavin", "Thitichunhakun")
#     print(person.toString())

#     person.setName("Somchai")
#     person.setSurname("Chein")
#     print(person.getName())
#     print(person.getSurname())



## Encapsulation : Property
# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.__name, self.__surname = name, surname

#     def setName(self, name: str) -> None:
#         self.__name = name
    
#     def getName(self) -> str:
#         return self.__name
    
#     def setSurname(self, surname: str) -> None:
#         self.__surname = surname
    
#     def getSurname(self) -> str:
#         return self.__surname
    
#     def toString(self) -> str:
#         return f"{self.getName()}, {self.getSurname()}"

#     name = property(getName, setName) # ไม่ต้องใช้ .__Class_name__attribute_name แล้ว
#     surname = property(getSurname, setSurname)

# if __name__ == "__main__":
#     person = Person("Paphavin", "Thitichunhakun")
#     print(person.toString())

#     person.name = "Somchai"
#     person.surname = "Cheingpongpan"
#     print(person.name)
#     print(person.surname)




## Encapsulation : Property 2
class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.__name, self.__surname = name, surname

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self.__surname = surname
    
    def toString(self) -> str:
        return f"{self.name}, {self.surname}"


if __name__ == "__main__":
    person = Person("Paphavin", "Thitichunhakun")
    print(person.toString())

    person.name = "Jason"
    person.surname = "Smith"
    print(person.name)
    print(person.surname)