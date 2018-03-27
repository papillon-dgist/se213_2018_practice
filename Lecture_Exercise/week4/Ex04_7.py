def display(sequence):
    for v in sequence:
        print(v, end=' ')
    print()

t1 = [42, 1024, 23]
t2 = [6, 28, 496]
display(t1)
display(t2)

print("/////random_list/////")

import random

def random_list(n, k):
    new_list = []
    for i in range(k):
        new_list.append(random.randrange(n))
    return new_list

t = random_list(5,2)
print(t)
print(random_list(10, 3))