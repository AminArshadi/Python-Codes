def is_up_monotone(X, d):
    '''(str,str)->(None,None)
    Preconditions: This function has two parameters, a string X and a string d. These two strings can
    be assumed to be such that each looks like a positive integer and such that the number of digits in x is
    divisible by the integer represented by d.
    The function returns True if the sequences is up-monotone and False otherwise.
    '''

    result = ''
    for i in range(0, len(X), int(d)):
        result = result + X[i:i + int(d)] + ','

    result = result[:-1]

    print(result)

    result2 = True
    if len(X) != len(d):
        for i in range(0, len(X) - int(d), int(d)):

            if X[i:i + int(d)] < X[int(d) + i:2 * (i + int(d))]:
                result2 = True

            else:
                result2 = False
                break

        return result2






# main
print('*********************************************')
print('**')
print('*__Welcome to up-monotone inquiry__*')
print('**')
print('*********************************************')

name = input('What is your name? ')

print('*********************************************')
print('**')
print('*__' + name + ' ,welcome to up-monotone inquiry.__*')
print('**')
print('*********************************************')

flag = True
while flag:
    question = input(name + ", would you like to test if a number admits an up-monotone split of given size? ")
    question = (question.strip()).lower()
    if question == 'no':
        flag = False

    elif question == 'yes':
        print('Good choice!')
        X = input('Enter a positive integer: ')
        if X.isdigit() and int(X) > 0:
            print('Enter the split. The split has to divide the length of ' + X + ' i.e. ' + str(len(X)))
            d = input()

            if d.isdigit() and len(X) % int(d) == 0:
                a = is_up_monotone(X, d)


                if a:
                    print('The sequence is up-monotone')
                else:
                    print('The sequence is not up-monotone')



            elif d.isdigit() and len(X) % int(d) != 0:
                print(d + ' does not divide ' + str(len(X)) + '. Try again.')


            else:
                print('The input can only contain digits. Try again.')


        elif X[1:].isdigit() and X[0] == '-':
            print('The input has to be a positive integer. Try again.')


        else:
            print('The input can only contain digits. Try again.')



    else:
        print('Please enter yes or no. Try again.')

print('*****************')
print('**')
print('*__Good bye ' + name + '__*')
print('**')
print('*****************')