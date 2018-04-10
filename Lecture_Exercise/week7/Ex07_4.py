fileobj = open('quotes.txt', 'r')
file_contents = fileobj.read()
fileobj.close()

with open('quotes.tet', 'r') as fileobj:
    file_contents = fileobj.read()
    

fileobj = open('test.txt','wt')
print('Hello, world!', file=fileobj)
print('Hi, again.', file=fileobj)
fileobj.close()

with open('test.txt','wt') as fileobj:
    print('Hello, world!', file=fileobj)
