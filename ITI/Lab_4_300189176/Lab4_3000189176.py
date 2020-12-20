##############################################################
#Activity 1:
##############################################################

def avarage(value):
    list_of_value = list(eval(value))
    formula = sum(list_of_value)/len(list_of_value)
    print(formula)

def findAvarage():
    value = input('Please enter some values seprated by commas: ')
    avarage(value)


findAvarage()

##############################################################
#Activity 2:
##############################################################

def avarage_max_min(value):
    list_of_value = list(eval(value))
    formula1 = sum(list_of_value)/len(list_of_value)
    formula2 = max(list_of_value)
    formula3 = min(list_of_value)
    print([formula1, formula2, formula3])

def find_avarage_max_min():
    value = (input('Please enter your marks seperated by commas: '))
    avarage_max_min(value)


find_avarage_max_min()

##############################################################
#Activity 3:
##############################################################

import math

def distance(velocity):
    for i in range(0,10):
        x = (math.pi * (i*10)) / 180
        formula = (2 * (velocity**(2)) * math.cos(x) * math.sin(x)) / 9.8
        print('Distance[' + str(i) + ']: ' + str(formula))


def distance_calculator():
    velocity = int(input('Please enter the velocity: '))
    distance(velocity)


distance_calculator()

##############################################################
#Activity 4:
##############################################################

import math

def standard_deviation(value):
    list_of_value = list(eval(value))
    a = sum(list_of_value) / len(list_of_value)

    top = ((list_of_value[0] - a)**2)
    for i in range(len(list_of_value) - 1):
        top = top + ((list_of_value[i + 1] - a)**2)

    s = math.sqrt(top/(len(list_of_value) - 1))

    print(s)


def standard_deviation_calculator():
    value = input('Please enter your values seperated my commas: ')
    standard_deviation(value)


standard_deviation_calculator()

















