# List in first out
def reverse_word(word):
    stack = []
    for letter in word: stack.append(letter)
    reversed_word = ""
    while stack: reversed_word += stack.pop()
    return reversed_word

print(reverse_word(input("Enter a word to reverse: ")))