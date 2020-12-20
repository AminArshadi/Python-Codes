def draw_w_stars(n):
    '''(int)->None
Preconditions: n is positive odd integer
Draws a figure as depicted in Question 5 with n stars in top and bottom raws
'''
    list = []
    for i in range(n):
        list.append('*')

    list2 = []
    for i in range(n):
        list2.append(list)



    k = 0
    for i in range(((len(list2)//2)+1)):
        print(''.join(list2[0]))

        list2[i][k] = ' '
        list2[i][(-k)-1] = ' '

        k+=1





draw_w_stars(3)
