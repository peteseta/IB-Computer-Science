list1 = [1, 3, 5, 4, 7, 8, 9, 2, 11]
list2 = [52, 15, 12, 24, 13, 6, 7, 9, 8]

listOdd = []
listEven = []

# append odd numbers from list1 into odd list
for i in list1:
    if i % 2 != 0:
        listOdd.append(i)

# append even numbers from list2 into even list
for i in list2:
    if i % 2 == 0:
        listEven.append(i)

# sort listOdd and listEven in increasing order
listOdd.sort()
listEven.sort()

print("Odd numbers: ", listOdd)
print("Even numbers: ", listEven)
print("Combined list: ", listOdd + listEven)

# alternate appending from listOdd and listEven to alternatelist
alternateList = []
while len(listOdd) > 0 or len(listEven) > 0:
    if len(listOdd) > 0:
        alternateList.append(listOdd.pop(0))
    if len(listEven) > 0:
        alternateList.append(listEven.pop(0))

print("Alternating odd and even: ", alternateList)
