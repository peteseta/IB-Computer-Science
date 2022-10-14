def consecutive_zeros(num):
    return max(len(i) for i in str(num).split("1"))


print(consecutive_zeros(1001101000110))
print(consecutive_zeros(1000011110001000110))
