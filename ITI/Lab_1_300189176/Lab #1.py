# Exercise 1

def formula(f_n,s_n):
    result_1 = f_n // s_n
    result_2 = f_n % s_n
    print(result_1,result_2)

formula(100,3)
#######################################################
# Exercise 2

def c_to_f(celcius):
    f = (celcius*9/5) + 32
    return float(f)

print(c_to_f(100))
#######################################################
# Exercise 3

def compute(hw_average, midterm, final):
    total = hw_average * (25.0 / 100) + midterm * (25.0 / 100) + final * (50.0 / 100)
    print(total)

compute(98, 95, 95)
#######################################################
# Exercise 4

from math import sqrt

def area(side1, side2, side3):
    p = side1 + side2 + side3
    area = sqrt(p * (p - 2 * side1) * (p - 2 * side2) * (p - 2 * side3)) / 4
    return area

print area(20, 30, 40)