number = int(input('Enter a non negative number: '))


def computefact(a):
    first_number = 0
    product = 1
    while first_number <= (a - 1):
        first_number = first_number + 1
        product = product * first_number
    print(str(product))

while True:
    if number > 0:
        computefact(number)
        break

    elif number == 0:
        print('1')
        break

    else:
        print('Your number cannot be negative!')
        number = int(input('Enter a non negative number this time: '))