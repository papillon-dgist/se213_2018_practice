d = 42
f = 3.14
s = 'apple'
print('{} {} {}'.format(d, f, s))
print('{2} {0} {1}'.format(d, f, s))
print('{0} is {0}'.format(s))
print('{d} {f} {s}'.format(d=6, f=1.618, s='pineapple'))
print('{0:d} {0:f} {0:g}'.format(42))
print()
print('0123456789' * 2)
print('{:10d}'.format(42))
print('{:>10d}'.format(42))
print('{:<10d}'.format(42))
print('{:^10d}'.format(42))
print('{:10.2f}'.format(3.1415926535))
print('{:1d}'.format(42))
print('{:5.5f}'.format(3.1415926535))