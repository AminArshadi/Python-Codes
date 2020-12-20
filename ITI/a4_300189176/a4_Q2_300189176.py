def two_length_run(list):
    '''(list)->bool
    Precondition: It must be assumed that the user will follow the instructions and enter a
    sequence of integers separated by spaces for the list and an integer for n.
    The function returns True if the given list has at least one run (of length at least two), and False otherwise.'''
    answer = False
    for i in range(len(list) - 1):
        if list[i] == list[i+1]:
            answer = True
    return answer

#main
list = input('Please input a list of numbers separated by space: ').strip().split()
print(two_length_run(list))