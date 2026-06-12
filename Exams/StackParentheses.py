#  stack = []  == False
# stack = ["1",... ]  == True


# def is_valid(s: str) -> bool:
#     stack = []
#     pairs = {")": "(", "]": "[", "}": "{"}
#     for c in s:
#         if c in "([{": stack.append(c)
#         elif not stack or stack.pop() != pairs[c]: return False
#     return not stack

# if __name__ == "__main__":
#     print(is_valid("([)]"))
#     print(is_valid("({[]})"))


def is_valid(s: str) -> bool:
    stack = []
    paris = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{": stack.append(c)
        elif not stack or stack.pop() != paris[c]: return False
    return True

if __name__ == "__main__":
    print(is_valid("([])"))