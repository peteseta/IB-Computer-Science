collection = [i for i in range(10)]
target = 3


def sequential_search(target, collection):
    index = 0
    for element in collection:
        if element == target:
            return f"found at position {index}"
        else:
            index += 1


print(collection)
print(sequential_search(target, collection))
