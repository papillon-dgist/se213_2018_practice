import random # using random module
print(random.random()) # float, 0.0 <= x < 1.0
print(random.uniform(1, 10)) # float, 1.0 <= x < 10.0
print(random.randrange(10)) # int, 0 <= x < 10
print(random.randint(1, 10)) # int, 1 <= x <= 10
# choice(): select one element in a given sequence
print(random.choice('abc'))