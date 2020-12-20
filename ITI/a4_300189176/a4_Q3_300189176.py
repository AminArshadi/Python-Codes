def longest_run(list):
    '''(list)->int
    Precondition: It must be assumed that the user will follow the instructions and enter a
    sequence of integers separated by spaces for the list and an integer for n.
    The function returns the length of the longest run.'''
    max_repeat = 0
    counter = 1

    if len(list) > 1:
        for i in range(len(list) - 1):
            if list[i] == list[i+1]:
                counter += 1

                if counter > max_repeat:
                    max_repeat = counter

            else:
                if counter > max_repeat:
                    max_repeat = counter

                counter = 1
        return max_repeat


    elif len(list) == 1:
        return 1


    else:
        return max_repeat


#main
list = input('Please input a list of numbers separated by space: ').strip().split()
print(longest_run(list))
