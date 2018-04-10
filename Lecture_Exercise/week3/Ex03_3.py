def add1(value1, value2=1, value3=2):
    return value1 + value2 + value3

print(add1(42, 1024, 23))
print(add1(42, 1024))
print(add1(42))

def power(base, exponent):
    return base ** exponent

print(power(2,10))
print(power(base=2, exponent=10))
print(power(exponent=10, base=2))