def double(arg):
    for i in range(len(arg)):
        arg[i] = 2 * arg[i]
    return arg
t1 = [42, 1024, 23]
t2 = double(t1)
t3 = double(t1.copy())
t2[2] = 6
t3[2] = 28
print(t1, t2, t3, sep='\n')