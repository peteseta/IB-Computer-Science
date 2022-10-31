def sum_of_vowels(str):
    vowels = {"A": 4, "E": 3, "I": 1, "O": 0, "U": 0}
    return sum(vowels[char.upper()] for char in str if char.upper() in vowels)


print(sum_of_vowels("Let's test this function.'"))
