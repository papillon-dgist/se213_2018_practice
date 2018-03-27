#tuple
t1 = (42, 1024, 6)
t2 = (42, )
print(t1[1])
print(t1[1:3])
print(len(t1))
print(min(t1))
print(max(t1))
t2 = t1 + t1
t3 = t1 *3
print(t2)
print(t3)

#t1[2] = 3
#=>TypeError: 'tuple' object does not support item assignment
#t2.append(0)
#=>AttributeError: 'tuple' object has no attribute 'append'