var = 42
string = 'Answer'
pi = 3.141592653589793
s1 = 'The %s is %d.' % (string, var)
print(s1)
print('0123456789'*2)
print('%10d' % var)
print('%010d' % var)
print('%-10d' % var)
print('%f' % pi)
print('%.2f' % pi)
print('%.10f' % pi)
print('%10.2f' % pi)
print('%g, %g, %g' % (var, pi, 10000000000))
print('%(name)s: %(average)g' %
     {'name': 'Alice', 'average': 99.9})