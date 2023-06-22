def greatest_prime_factor(n):
    greatest = 0
    
    for factor in range(2, n):    
        # if factor and is prime
        if n % factor == 0 and all(factor % j != 0 for j in range(2, factor)):
            greatest = factor
            
        return greatest

print(greatest_prime_factor(60085147143))
