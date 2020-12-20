def number_divisible(list, n):
    '''(list)->int
    Precondition: It must be assumed that the user will follow the instructions and enter a
    sequence of integers separated by spaces for the list and an integer for n.
    The function returns the number of elements in the list that are divisible by n.'''

    count = 0
    for i in range(len(list)):
        if int(list[i]) % int(n) == 0:
            count = count + 1

    return count


#main
list = input('Please input a list of numbers separated by space: ').strip().split()
n = input('Please input an integer: ')
print('The number of elements divisible by ' + n + ' is ' + str(number_divisible(list, n)))