random_list = ["A", "A", "B", "C", "B", "D", "D", "A", "B"]

# initialize a dictionary
element_freq = {}

# loop through the list and check if the element is present in the dictionary or not
# if the element is present, then increase its count
# if the element is not present, then add it to the dictionary with count 1
for element in random_list:
    if element in element_freq:
        element_freq[element] += 1
    else:
        element_freq[element] = 1

print(element_freq)
