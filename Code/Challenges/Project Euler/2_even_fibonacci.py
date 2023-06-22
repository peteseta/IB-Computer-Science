even = 0

a = 0
b = 1

while b < 4000000:
    a, b = b, a+b
    if b % 2 == 0:
        even += b
        
print(even)