'''
I understand the importance of professional integrity in my education and future career
in engineering or computer science. I hereby certify that I have done and will do all work
on this examination entirely by myself, without outside assistance or the use of unauthorized
information sources. Furthermore, I will not provide assistance to others.
'''
# Amin Arshadi 300189176


def diff_start_end(l, q):
    '''(list of int, list of int) -> (int, int)

l and q are two parallel lists i.e. len(l)==len(q)
The function returns the following two integers (i.e. a tuple with
the following two integers).
- the index where l and q first differ, and
- the index where l and q last differ. This index should be NEGATIVE

Preconditions: len(l)==len(q)>=1, and l != q ***(The 2 lists are NOT the same)***

>>> diff_start_end([0,1,6,0,7,2,3,4], [0,1,8,0,9,2,3,4])
(2, -4)
>>> diff_start_end([6],[8])
(0, -1)
>>> diff_start_end([0,0,0,1,0],[0,0,0,22,0])
(3, -2)
>>> diff_start_end([0,1,1],[1,1,1])
(0, -3)
>>> diff_start_end([0,1,1,0],[0,0,0,0])
(1, -2)
'''

#YOUR CODE GOES HERE
    list = []
    for i in range(len(l)):
        if l[i] == q[i]:
            list.append(0)
        else:
            list.append(1)

    a = list.index(1)
    inverse = list[::-1]
    b = inverse.index(1)
    c = -b-1

    return (a, c)


#print(diff_start_end([0,1,1,0],[0,0,0,0]))
