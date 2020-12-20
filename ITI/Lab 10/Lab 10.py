def are_digits(list, len):
    if len == 0:
        print(True)

    elif str(list[len-1]).isdigit():
        are_digits(list, len-1)

    else:
        print(False)

########################################################
########################################################
def list_maker(list, n):
    if n-1 == 0:
        list.append(0)
    else:
        list.append(n-1)
        list_maker(list, n-1)


#main
list1 = []
n = int(input('Enter a value for n: '))
list_maker(list1, n)
print(list1[::-1])

########################################################
########################################################
def bcd(x, y):
    if x >= y and x % y is 0:
        print(str(y))
    elif x < y:
        bcd(y, x)
    else:
        bcd(y, x % y)
