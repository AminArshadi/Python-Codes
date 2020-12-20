import random

def elementary_school_quiz(q_type,q_number):
    '''(int,int)->int
    Preconditions: integer q_type can only have values of 0 or 1, and integer q_number only takes values 1, or 2.
    Prints the number of questions that the student answered correctly'''

    n_main1_f = random.randint(1,10)
    n_main2_f = random.randint(1,10)
    n_main3_f = random.randint(1,10)
    n_main4_f = random.randint(1,10)

    n1_f = n_main1_f - n_main2_f
    n11_f = n_main3_f - n_main4_f

    n2_f = n_main1_f ** n_main2_f
    n22_f = n_main3_f ** n_main4_f

    if q_type == 0 and q_number == 1:
        print('Question 1:')
        a = input('What is the result of ' + str(n_main1_f) + '-' + str(n_main2_f) + '? ')
        if a == n1_f:
            print('1')
        else:
            print('0')

    elif q_type == 0 and q_number == 2:
        print('Question 1:')
        a = input('What is the result of ' + str(n_main1_f) + '-' + str(n_main2_f) + '? ')
        print('Question 2:')
        b = input('What is the result of ' + str(n_main3_f) + '-' + str(n_main4_f) + '? ')
        if a == n1_f and b == n11_f:
            print('2')
        elif (a == n1_f and b != n11_f) or (a != n1_f and b == n11_f):
            print('1')
        else:
            print('0')

    elif q_type == 1 and q_number == 1:
        print('Question 1:')
        a = input('What is the result of ' + str(n_main1_f) + '^' + str(n_main2_f) + '? ')
        if a == n2_f:
            print('1')
        else:
            print('0')

    elif q_type == 1 and q_number == 2:
        print('Question 1:')
        a = input('What is the result of ' + str(n_main1_f) + '^' + str(n_main2_f) + '? ')
        print('Question 2:')
        b = input('What is the result of ' + str(n_main3_f) + '^' + str(n_main4_f) + '? ')
        if a == n2_f and b == n22_f:
            print('2')
        elif (a == n2_f and b != n22_f) or (a != n2_f and b == n22_f):
            print('1')
        else:
            print('0')

elementary_school_quiz(1,1)

##########################################################################################################################################

from math import sqrt

def high_school_quiz(a,b,c):
    '''(number,number,number)->None
    Prints the equation first and then prints its solutions.'''

    if (b**2) - (4 * a * c) > 0 and a != 0:
        print('The quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' has the following real roots:')
        print(str((-b + sqrt((b ** 2) - (4 * a * c))) / (2*a)) + ' and ' + str((-b - sqrt((b ** 2) - (4 * a * c))) / (2*a)))

    elif (b**2) - (4 * a * c) == 0 and a != 0:
        print('The quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' has the following real roots:')
        print((str((-b + sqrt((b ** 2) - (4 * a * c))) / (2*a))) + ' and ' + str((-b - sqrt((b ** 2) - (4 * a * c))) / (2*a)))

    elif (b**2) - (4 * a * c) < 0 and a != 0:
        print('The deteminant is negative; therefore, the quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' is not satisfied for no number x')

    elif a == 0 and b !=0:
        print('The linear equation ' + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' has the following real root/solution:')
        print((str(-c/b)))

    elif a == 0 and b == 0 and c == 0:
        print('The quadratic equation ' + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' is not satisfied for all numbers x')

    elif a == 0 and b == 0 and c != 0:
        print('The quadratic equation ' + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' is not satisfied for no number x')

high_school_quiz(2,4,2)

##########################################################################################################################################

from math import sqrt
import random


def elementary_school_quiz(q_type, q_number):
    '''(int,int)->int
    Preconditions: integer q_type can only have values of 0 or 1, and integer q_number only takes values 1, or 2.
    Prints the number of questions that the student answered correctly'''

    n_main1_f = random.randint(1, 10)
    n_main2_f = random.randint(1, 10)
    n_main3_f = random.randint(1, 10)
    n_main4_f = random.randint(1, 10)

    n1_f = n_main1_f - n_main2_f
    n11_f = n_main3_f - n_main4_f

    n2_f = n_main1_f ** n_main2_f
    n22_f = n_main3_f ** n_main4_f

    if q_type == '0' and q_number == '1':
        print('Question 1:')
        a = int(input('What is the result of ' + str(n_main1_f) + '-' + str(n_main2_f) + '? '))
        if a == n1_f:
            print('Congratulations ' + name + '! You will probably get an A tomorrow.')
            print('Goodbye' + name + '!')
        else:
            print('I think you need some more practice ' + name)
            print('Goodbye' + name + '!')
    elif q_type == '0' and q_number == '2':
        print('Question 1:')
        a = int(input('What is the result of ' + str(n_main1_f) + '-' + str(n_main2_f) + '? '))
        print('Question 2:')
        b = int(input('What is the result of ' + str(n_main3_f) + '-' + str(n_main4_f) + '? '))
        if a == n1_f and b == n11_f:
            print('Congratulations ' + name + '! You will probably get an A tomorrow.')
            print('Goodbye' + name + '!')
        elif (a == n1_f and b != n11_f) or (a != n1_f and b == n11_f):
            print('You did ok ' + name + ' ,but I know you can do better.')
            print('Goodbye' + name + '!')
        else:
            print('I think you need some more practice ' + name)
            print('Goodbye' + name + '!')

    elif q_type == '1' and q_number == '1':
        print('Question 1:')
        a = int(input('What is the result of ' + str(n_main1_f) + '^' + str(n_main2_f) + '? '))
        if a == n2_f:
            print('Congratulations ' + name + '! You will probably get an A tomorrow.')
            print('Goodbye' + name + '!')
        else:
            print('I think you need some more practice ' + name)
            print('Goodbye' + name + '!')

    elif q_type == '1' and q_number == '2':
        print('Question 1:')
        a = int(input('What is the result of ' + str(n_main1_f) + '^' + str(n_main2_f) + '? '))
        print('Question 2:')
        b = int(input('What is the result of ' + str(n_main3_f) + '^' + str(n_main4_f) + '? '))
        if a == n2_f and b == n22_f:
            print('Congratulations ' + name + '! You will probably get an A tomorrow.')
            print('Goodbye' + name + '!')
        elif (a == n2_f and b != n22_f) or (a != n2_f and b == n22_f):
            print('You did ok ' + name + ' ,but I know you can do better.')
            print('Goodbye' + name + '!')
        else:
            print('I think you need some more practice ' + name)
            print('Goodbye' + name + '!')


def high_school_quiz(a, b, c):
    '''(number,number,number)->None
    Prints the equation first and then prints its solutions.'''

    if (b ** 2) - (4 * a * c) > 0 and a != 0:
        print('The quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' has the following real roots:')
        print(str((-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)) + ' and ' + str((-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)))

    elif (b ** 2) - (4 * a * c) == 0 and a != 0:
        print('The quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' has the following real roots:')
        print((str((-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a))) + ' and ' + str((-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)))

    elif (b ** 2) - (4 * a * c) < 0 and a != 0:
        print('The deteminant is negative; therefore, the quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' is not satisfied for no number x')

    elif a == 0 and b != 0:
        print('The linear equation ' + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' has the following real root/solution:')
        print((str(-c / b)))

    elif a == 0 and b == 0 and c == 0:
        print('The quadratic equation ' + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' is not satisfied for all numbers x')

    elif a == 0 and b == 0 and c != 0:
        print('The quadratic equation ' + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0' + ' is not satisfied for no number x')


print('*********************************************')
print('**')
print('*__Welcome to mt math quiz-generator__*')
print('**')
print('*********************************************')

name = input('What is your name? ')
input('Hi ' + name + '. ' + 'Are you in?')
print('1 for elementary school')
print('2 for high school')
print('3 or other character(s) for none of the above')
answer = input()


if answer == '1':
    print('*********************************************')
    print('**')
    print('*__' + name + ' ,welcome to mt math quiz-generator for elementry school students__*')
    print('**')
    print('*********************************************')

    input(name + ' what would you like to practice? (press enter) ')
    print('0 for subtraction')
    print('1 for exponentiation')
    q_type = input()
    if q_type == '0' or q_type == '1':
        print('How many paractice questions would you like to do? (enter 0 or 1 or 2) ')
        q_number = input()
        if q_number == '1' or q_number == '2':
            print(name + ' ,here is your ' + str(q_number) + ' question(s)')
            elementary_school_quiz(q_type, q_number)
        elif q_number == '0':
            print('Zero questions. Ok. Good bye.')
        else:
            print('Only 0,1, or 2 are valid choices for the number of questions.')
            print('Good bye ' + name + '!')
    else:
        print('Invalid chose. Only 0 or 1 is accepted.')
        
    answer = input('Another example run: ')    

elif answer == '2':

    print('*********************************************')
    print('**')
    print('*__' + 'quadratic equation, a.x^2 + b.x +c=0_solver for ' + name + '__*')
    print('**')
    print('*********************************************')

    flag = True
    while flag:
        question = input(name + ", would you like a quadratic equation solved? ")
        yes = 'yes' or 'YES' or 'Yes' or 'YEs' or 'YeS' or 'yES' or 'yeS' or 'yEs'

        if question == yes:
            print("Good choice!")
            a = int(input('Enter a number the coefficient a: '))
            b = int(input('Enter a number the coefficient b: '))
            c = int(input('Enter a number the coefficient c: '))
            high_school_quiz(a, b, c)

        else:
            flag = False


else:
    print(name + 'you are not  target audience for this software.')
    print('Good bye ' + name + '!')















