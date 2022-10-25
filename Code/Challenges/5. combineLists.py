# does not support arbitrarily deep nesting
def combineLists(input):
    combinedList = []
    for list in input:
        # print("st1" + str(list))
        for number in list:
            # print("st2" + str(list))
            if number not in combinedList:
                combinedList.append(number)

    return combinedList


print(*combineLists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), sep=", ")

# traverses the list for any arbitrary depth


def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o


data = [[[1, 2, 3], [4, 5, 6], [[7, 8, 9], [10, 11, 12], [13, 14, 15]]]]
print(*list(traverse(data)), sep=", ")
