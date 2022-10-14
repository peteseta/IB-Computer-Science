import random

a = random.sample(range(1, 25), random.randint(5, 10))
b = random.sample(range(1, 25), random.randint(5, 10))
new_list = []

for i in a:
    if i in b and not i in new_list:
        new_list.append(i)

fast_list = list(set(i for i in a if i in b))

fast_fast_list = list(set(a) & set(b))

print(fast_fast_list)
