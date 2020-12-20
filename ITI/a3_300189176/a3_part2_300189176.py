# Name: Amin Arshadi
# Student number:  300189176
# Course: IT1 1120
# Assignment Number 3, Part 2

##################################################################
# Question 1
###################################################################

def sum_odd_divisors(n):
    '''(int)->int or None
    If n is zero the fucntion returns None. Else the function returns the sum of all the positive odd divisor of n.'''

    if n == 0:
        return None

    else:
        a = 1
        sum = 0
        while abs(n) >= a:
            if n % a == 0:
                divisor = n / a
                sum = sum + divisor
                a = a + 2
            else:
                a = a + 2
        return int(abs(sum))

##################################################################
# Question 2
###################################################################

def series_sum():
    '''(None)->number or None
        If the user enters a negative integer, the function should return None otherwise the function should return the sum of the
        following series 1000 + 1/12 + 1/22 + 1/32 + 1/42 + ::: + 1/n2 for the given integer n. '''

    n = int(input('Please enter a non-negative integer: '))

    if n < 0:
        return None

    else:
        fn = 1
        sum = 1000
        while n >= fn:
            sum = sum + 1/(fn**2)
            fn = fn + 1
        return sum

##################################################################
# Question 3
###################################################################

from math import sqrt
from math import ceil

def pell(n):
    '''(int)->int or None
        If n is negative, the function returns None. Else, the function returns the pell number by
        using appropiate formula ((((1 + sqrt(2)) ** n) - ((1 - sqrt(2)) ** n)) / (2 * sqrt(2))).'''

    if n < 0:
        return None
    else:
        answer = (((1 + sqrt(2)) ** n) - ((1 - sqrt(2)) ** n)) / (2 * sqrt(2))
        return ceil(answer)

##################################################################
# Question 4
###################################################################

def countMembers(s):
    '''(str)->int
    The funtion counts how many times the characters the lower case letter between e and j
    (inclusive), the upper case letters between F and X (inclusive), numerals between 2 and 6 (inclusive), and
    the exclamation point (!), comma (,), and backslash (\) are used in s.'''

    n = 0
    result = 0
    a = 'FGHIJKLMNOPQRSTUVWXefghij23456!,\\'
    while len(s)-1 >= n:
        if s[n] in a:
            n = n + 1
            result = result +1

        else:
            n = n + 1

    return result

##################################################################
# Question 5
###################################################################

def casual_number(s):
    '''(str)->int or None
    Precondition: Commas are in meaningful places.
    Function should return an integer representing a number in s. If s does not look like a number, the function should return None.'''

    result = ''


    if s[0] == '-' and len(s) > 1 and s[1].isdigit():
        result = result + '-'

        for i in range(1, len(s)):
            if s[i].isdigit():
                result = result + s[i]

            elif s[i] == ',':
                result = result + ''

            else:
                return None

    elif s[0] != '-':
        for i in range(len(s)):
            if s[i].isdigit():
                result = result + s[i]

            elif s[i] == ',':
                result = result + ''

            else:
                return None

    else:
        return None



    return int(result)

##################################################################
# Question 6
###################################################################

def alienNumber(s):
    '''(str)->int
    Preconditions: No character in s outside of this set: {T,y, !,a, N, U}; T, y, k, a, N, U = 1024, 598, 121, 42, 6, 1.
    The funtions takes one string parameter s, and returns the integer value represented by s.'''

    return (s.count('T') * 1024) + (s.count('y') * 598) + (s.count('!') * 121) + (s.count('a') * 42) + (s.count('N') * 6) + (s.count('U') * 1)

##################################################################
# Question 7
###################################################################

def alienNumberAgain(s):
    '''(str)->str
    Preconditions: No character in s outside of this set: {T,y, !,a, N, U}; T, y, k, a, N, U = 1024, 598, 121, 42, 6, 1.
    The funtions takes one string parameter s, and returns the integer value represented by s.'''

    n = 0
    sum = 0
    while len(s) - 1 >= n:
        if s[n] == 'T':
            sum = sum + 1024
            n = n + 1
        elif s[n] == 'y':
            sum = sum + 598
            n = n + 1
        elif s[n] == '!':
            sum = sum + 121
            n = n + 1
        elif s[n] == 'a':
            sum = sum + 42
            n = n + 1
        elif s[n] == 'N':
            sum = sum + 6
            n = n + 1
        elif s[n] == 'U':
            sum = sum + 1
            n = n + 1

    return sum

##################################################################
# Question 8
###################################################################

def encrypt(s):
    '''(str)->str
    The function reverses s and starts on either side of the string and bring the characters together.'''

    r_s = s[::-1]
    result = r_s[0]

    for i in range(1, len(r_s)):


        i = i * -1
        result = result + r_s[i]
        i = i * -1
        result = result + r_s[i]


    return result[:len(r_s)]

##################################################################
# Question 9
###################################################################

def weavoep(s):
    '''(str)->str
    The funtion returns a string with the letters o and p inserted between every pair of consecutive characters of s, as
    follows. If the first character in the pair is uppercase, it inserts an uppercase O. If however,
    it is lowercase, it inserts the lowercase o. If the second character is uppercase, it inserts an uppercase P.
    If however, it is lowercase, it inserts the lowercase p. If at least one of the characters is not a letter in the alphabet,
    it does not insert anything between that pair. Finally, if s has one or less characters, the function returns the same string as s.'''

    result = ''
    if len(s) > 1:
        for i in range(len(s) - 1):
            if s[i].isdigit():
                result = result + s[i]


            elif s[i].isalpha() and s[i + 1].isalpha():
                if s[i].isupper() and s[i + 1].isupper():
                    result = result + s[i] + 'OP'

                elif s[i].isupper() and s[i + 1].islower():

                    result = result + s[i] + 'Op'

                elif s[i].islower() and s[i + 1].isupper():

                    result = result + s[i] + 'oP'

                elif s[i].islower() and s[i + 1].islower():

                    result = result + s[i] + 'op'

            elif s[i].isalpha() and not s[i + 1].isalpha():
                result = result + s[i]



        return result + s[-1]

    else:
        return s

##################################################################
# Question 10
###################################################################

def squarefree(s):
    '''(str)->bool
    The function returns True if s is squarefree (A squarefree word is a word that does
    not contain any subword twice in a row) and False otherwise.'''
    answer = True
    for d in range(1, (len(s)//2) + 1):
        for i in range(0, len(s)):
            if s[i:i + d] == s[i + d:i + d + d]:
                answer = False
                break


    return answer







