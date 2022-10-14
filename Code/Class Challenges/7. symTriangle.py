n = 9

for i in range(n):
    # for the first row there are n-1 spaces. each row after that has one less space
    print(" " * (n - 1 - i), end="")
    # for the first row there are 1 star. each row after that has two more stars
    print("*" * ((i * 2) + 1), end="")
    print()  # newline
