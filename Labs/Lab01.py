# Data Type

print(42)
print(42.0)
print('42')
print(type(42))
print(type(42.0))
print(type('42'))

print(1 + 2)
print(1.0 + 2.0)
print(1 + 2.0)

print(4.7 // 2.3)
print(4.7 % 2.3)
print(1 + int('2'))

# Using Variables

pi = 3.14159265358979
print(pi)

r = 3
print(pi * r * r)

r = 5
print(pi * r * r)

# Keyboard Input

text = input('Enter any text: ')
print(text, type(text))
text = input('Enter any text: ')
print(text, type(text))

# Type Conversion

value = '42'
print(value, type(value))
converted_value = int(value)
print(converted_value, type(converted_value))
print(converted_value + 1)
print("print(value + 1) makes error!")

value = input('Enter a number: ')
print(value, type(value))
int_value = int(value)
float_value = float(value)
print(int_value, type(int_value))
print(float_value, type(float_value))