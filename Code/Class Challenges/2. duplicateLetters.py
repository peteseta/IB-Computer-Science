def dup(string):

    uniqueLetters = []
    duplicate = False

    for char in string:
        if char not in uniqueLetters:
            uniqueLetters.append(char)
        duplicate = True

    print("unique letters:" + str(uniqueLetters))
    if duplicate:
        return True
    return False


print(dup("Beef"))
