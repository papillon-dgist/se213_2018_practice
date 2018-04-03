pi = 3.14159265
width = 10
precision = 2
print('0123456789' * 3)
print(f'{pi}')
print(f'{pi:10.2f}')
print(f'{pi:{width}.{precision}f}')
print(f'{max(width, precision)}')
t = [42, 1024, 23]
for i in range(len(t)):
    print(f'{i}: {t[i]}')