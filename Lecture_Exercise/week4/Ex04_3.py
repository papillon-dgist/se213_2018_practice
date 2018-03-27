t1 = [42, 1024, 23]
print(1024 in t1)
print(7 in t1)
print(1024 not in t1)
print(len(t1)) # the number of elements
print(min(t1)) # the minimum value
print(max(t1)) # the maximum value
t2 = [6, 28, 496]
t3 = t1 + t2 # concatenation
print(t3)
t4 = t2 * 2 # repetition
print(t4)
print(t4[:4]+t4[5:])