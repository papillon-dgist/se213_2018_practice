# Copying a list and copy() function
t1 = [42, 1024, 23]
t2 = t1
t3 = t1.copy() # copy t1
t4 = t1[:] # copy t1

t2[2]=6
t3[2]=28
t4[2]=496

print(t1,t2,t3,t4, sep='\n')