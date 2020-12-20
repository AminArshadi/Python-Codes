def atlantic(a):
    '''(none)->none'''
    if len(str(a)) >= 9:
        print('new')
    else:
        print('old')
####################################################################################
def southern(a):
    '''(int)->none'''
    if a == 1:
        b = input('Enter a number of the weight in pounds: ')
        c = input('Enter a number of the weight in ounces: ')
        formula = (b * 16 + c) * 0.02835
        print(str(b) + ' pounds and ' + str(c) + 'ounces is (approximately) ' + str(formula) + ' kilograms.')
    elif a == 2:
        name = input('What is your name? ')
        c = str(input('What is your student number? '))

        print(name + ' you have a ' + str(atlantic(c)) + ' student number.')
####################################################################################
def pacific(a,b,c):
    '''(float,float,float)->bool'''
    c_1 = a >= 50 and b >= 50 and c >= 50 and (a >= 80 or b >= 80 or c >= 80)
    print(c_1)
####################################################################################
def arctic(number):
    '''(int)->bool'''
    a_1 = number % 10
    b = number // 10
    a_2 = b % 10
    b = b // 10
    a_3 = b % 10
    b_1 = b // 10

    a_4 = b_1 % 10
    b_2 = b_1 // 10
    a_5 = b_2 % 10
    b_2 = b_2 // 10



    if len(str(number)) == 4:
        if a_1 == b_1 and a_2 == a_3:
            return True
        else:
            return False

    elif len(str(number)) == 6:
        if a_1 == b_2 and a_2 == a_5 and a_3 == a_4:
            return True
        else:
            return False

print(arctic(222221))
