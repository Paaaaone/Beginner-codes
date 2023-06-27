number = int(input('Enter number: '))
factorial = 1
for i in range(number):
    factorial = factorial*(number-i)
print(factorial)
