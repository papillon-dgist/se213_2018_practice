counter = 0
while counter <3:
    print(counter)
    counter += 1
    
# a simple for loop
for value in [42, 1024, 6]:
    print(value)

# nested for loop
for v1 in [42, 1024]:
    print(v1)
    for v2 in [6, 23]:
        print(v1 + v2)

for index in range(5):
    print(index)

print('Examples on range()')
print(range(5))
print(list(range(5)))
print(list(range(1,4)))

print('with range(len())')
t = [42, 1024, 23]
for i in range(len(t)):
    print('t[', i, '] = ', t[i], sep='')
    t[i] = 2 * t[i]

print(t)