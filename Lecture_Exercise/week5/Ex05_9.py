number = 10
for i in range(2, number):
    print(i)
else:
    print('End of for loop')
    
number = int(input("Enter an integer : "))
for i in range(2, number):
    if number % i == 0:
        print(number, 'is not a prime number.')
        break
else:
    print(number, 'is a prime number.')
print('End of primality test.')