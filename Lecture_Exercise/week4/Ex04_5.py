t1=[]
t1.append(42)
t1.append(1024)
t1.append(23)
print(t1)
t2 = [6, 28, 496]
# equivalent to t1 += t2
t1.extend(t2)
print(t1)