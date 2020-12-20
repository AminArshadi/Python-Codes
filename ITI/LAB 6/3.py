def sum_of_three(x):
    for i in range(len(x) - 2):
        if (x[i] + x[i+1] + x[i+2]) == 0:
            return True
    return False