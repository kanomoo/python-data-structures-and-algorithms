# def bmiCal(name: str, weight: float, height: float) -> None:
#     bmi = weight / height ** 2
#     print("Hello", name)
#     print("Your BMI is", bmi)

# if __name__ == "__main__":
#     bmiCal("Paphavin", 54, 171)

# def Function(n: int) -> None:
#     i = s = 1
#     while s < n:
#         i += 1
#         s += i
#         print("*")

# if __name__ == "__main__":
#     Function(20)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def show(self):
        print(self.x, ", ", self.y, sep = "")

if __name__ == "__main__":
    point = Point(3, 7)
    point.show()