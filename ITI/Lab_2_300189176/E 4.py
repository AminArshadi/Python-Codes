a = float(input('What is the value of a? '))
b = float(input('What is the value of b? '))
c = float(input('What is the value of c? '))

if (b ** 2) - (4 * a * c) > 0:
    print('For ' + str(a) + ', ' + str(b) + ' and ' + str(c) + ', there are two distinct real roots!')
elif (b ** 2) - (4 * a * c) == 0:
    print('For ' + str(a) + ', ' + str(b) + ' and ' + str(c) + ', there is only one distinct real roots!')
elif (b ** 2) - (4 * a * c) < 0:
    print('For ' + str(a) + ', ' + str(b) + ' and ' + str(c) + ', there is no real roots!')
