"""
Swap two value
1. make a tuple (var2, var1) with values of var2 and var1
2. unpack the tuple to var1 and var2
"""

var1 = 42
var2 = 1024
var1, var2 = var2, var1
print(var1, var2)

print("XOR 교체 알고리즘")
a = 60
b = 13
print(a,b)
print('a:',bin(a),'\nb:', bin(b))
a ^= b
print('a:', bin(a))
b ^= a
print('b:', bin(b))
a ^= b
print('a:', bin(a))
print(a,b)