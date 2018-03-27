t = [42, 1024, 23, 6, 28, 496]
print(t)
print(t[1:4])
print(t[3:])
print(t[:2])
print(t[:]) # copy of a list*

print(t)
t[2:5] = [2, 3, 5]
print(t)

print(t[1:5:2]) # extended slicing
print(t[5:0:-1])