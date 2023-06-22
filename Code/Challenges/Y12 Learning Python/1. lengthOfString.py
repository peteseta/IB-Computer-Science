# returns the length of the string str
def los(str):
    return len(str)


def losLoop(str):
    count = 0
    for char in str:
        count += 1

    return count


string = "Amazing"
print(los(string))
print(losLoop(string))
