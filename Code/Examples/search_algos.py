import random


# prompt the user for a number to search for
def prompt(min, max):
    return input(f"Enter a number to search for between {min} and {max}: ")


LIST_LENGTH = 10

collection = [i for i in range(LIST_LENGTH)]
target = int(prompt(collection[0], collection[-1]))

random.shuffle(collection)


# sequential search
def sequential_search(target, collection):
    index = 0
    for element in collection:
        if element == target:
            return f"found at position {index}"
        else:
            index += 1
    return "NOT FOUND"


print(collection)
print("SEQUENTIAL SEARCH: " + sequential_search(target, collection))
