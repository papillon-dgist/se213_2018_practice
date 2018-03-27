my_list=[42,1024,23]
print(enumerate(my_list))
print(list(enumerate(my_list)))
for i,j in enumerate(my_list):
    print('my_list[', i,'] = ',j, sep='')
    