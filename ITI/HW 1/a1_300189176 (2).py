# Family name: Amin Arshadi
# Student number: 300189176
# Course: IT1 1120
# Assignment Number 1
# year 2020

##################################################################################################################
# Question 1
##################################################################################################################
def poem_generator():
    name = input('Enter your name: ')
    city_of_birth = input('Enter your city of birth: ')
    print('here was a small boy from '+city_of_birth)
    print('Who was buried in snow to his neck')
    print(name+' replied that the weather is cold!')
    print('But we don’t call this cold in '+city_of_birth)
##################################################################################################################
# Question 2
##################################################################################################################
def impl2loz(w):
    l = int(w)
    o = float((w-l)*16)
    print(l,o)
##################################################################################################################
# Question 3
##################################################################################################################
def pale(n):
    f_d = n % 10
    r1 = n // 10
    s_d = r1 % 10
    r2 = r1 // 10
    t_d = r2 % 10
    r3 = r2 // 10

    c1 = n > 0
    c2 = len(str(n)) == 4
    c3 = f_d ** s_d != 27
    c33 = s_d ** f_d != 27
    c4 = s_d ** t_d != 27
    c44 = t_d ** s_d != 27
    c5 = t_d ** r3 != 27
    c55 = r3 ** t_d != 27
    c6 = f_d % 4 != 0

    result = c1 and c2 and c3 and c33 and c4 and c44 and c5 and c55 and c6
    print(result)
###################################################################################################################
# Question 4
##################################################################################################################
def bibformat(author,title,city,publisher,year):
    print("'"+author+'('+str(year)+')'+'. '+title+'. '+city+': '+publisher+".'")
###################################################################################################################
# Question 5
##################################################################################################################
def bibformat(author,title,city,publisher,year):
    print(author+'('+str(year)+')'+'. '+title+'. '+city+': '+publisher+'.')

def bibformat_display():
    in1 = input('Enter the name of a book: ')
    in2 = input('Enter the name of the author? ')
    in3 = input('What year was the book published? ')
    in4 = input('Enter the name of the publisher: ')
    in5 = input('In what city are the headquarters of the publisher?')
    bibformat(in2, in1, in5, in4, in3)
###################################################################################################################
# Question 6
##################################################################################################################
def compound(x,y,z):
    f_c = x % 2 == 0 and y % 2 != 0 and z % 2 != 0
    s_c = x + y > 100 or y + z > 100 or x + z > 100
    print(f_c and s_c)
###################################################################################################################
# Question 7
##################################################################################################################
from math import log
from math import sqrt

def funct(p):
    r = sqrt(log(p - 10) / log(5))
    print('The solution is ' + str(r))
###################################################################################################################
# Question 8
##################################################################################################################
def gol(n):
    s_c = n // 2 + round(((n % 2)/2))
    print(int(s_c))
###################################################################################################################
# Question 9
##################################################################################################################
def cad_cashier(price,payment):
    number = payment - price
    number = round(number*100/5)*5/100
    return number

print(cad_cashier(10.58, 11))
###################################################################################################################
# Question 10
##################################################################################################################
def cad_cashier(price,payment):
    number = payment - price
    number = round(number*100/5)*5/100
    return number

def min_CAD_coins(price, payment):
    change = cad_cashier(price, payment)
    change = round(change * 100)
    n = change / 5
    t = n // 40 
    n = n % 40
    l = n // 20
    n = n % 20
    q = n // 5
    n = n % 5
    d = n // 2
    n = n % 2

    print (int(t), int(l), int(q), int(d), int(n))
