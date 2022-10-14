def char_replace(str, curr_char, new_char):
    replacedStr = ""

    for char in str:
        if char == curr_char:
            replacedStr += new_char
        else:
            replacedStr += char

    return replacedStr


print(char_replace("Hello", "l", "s"))
print(char_replace("World", "W", "A"))
print(char_replace("Python", "P", "x"))
print(char_replace("Python", "p", "a"))
