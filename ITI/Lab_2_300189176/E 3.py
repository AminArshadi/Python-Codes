number = int(input('What is your number? '))

if (number % 2 == 0) and (number % 3 == 0):
    print(str(number) + ' is divisible by both 2 and 3')
elif (number % 2 == 0) or (number % 3 == 0):
    print(str(number) + ' is divisible by either 2 or 3')
elif (number % 2 != 0) and (number % 3 != 0):
    print(str(number) + ' is divisible by neither 2 nor 3')