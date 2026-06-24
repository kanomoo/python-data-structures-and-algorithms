# def Function(n: int) -> None:
#     i = s = 1
#     while s < n:
#         i = i + 1
#         s = s + i
#         print("*")

# if __name__ == "__main__":
#     Function(20)

def Function(n: int) -> None:
    i = s = 1
    while s < n:
        i += 1
        s += i
        print("*")

if __name__ == "__main__":
    Function(20)