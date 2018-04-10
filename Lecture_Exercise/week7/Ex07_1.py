s='123'
print(s.ljust(5))
print(s.rjust(5))
print(s.center(5))
print(s.ljust(5,'*'))
print(s.rjust(5,'-'))
print(s.center(5, '.'))
print(s) # no change on s

print('  a string  '.strip())
print('  a string  '.lstrip())
print('  a string  '.rstrip())

print('.'.join('abc'))
print('.'.join(['foo', 'bar']))
print('*-*'.join(['foo', 'bar']))
print('\n'.join(['foo', 'bar']))