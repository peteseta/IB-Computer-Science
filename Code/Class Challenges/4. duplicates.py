input = [1, 1, 2, 3, 4, 4]

# method 1 - casting into a dictionary
list1 = list(dict.fromkeys(input))
print(list1)

# method 2 - using a loop
list2 = []
for i in input:
    if i not in list2:
        list2.append(i)
print(list2)
