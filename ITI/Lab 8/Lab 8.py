import random
def find(l, v):
    Nsteps = 0
    answer = False
    for ch in l:
        Nsteps += 1
        if ch == v:
            answer = True
            break

    print('Number of steps: ' + str(Nsteps))
    return answer

#main
list = [random.randint(1,1000) for v in range(999)]
value = int(input('Enter a value: '))
print(find(list, value))

######################################################################
def find_m(l, v):
    Nsteps = 0
    for ch in l:
        for chh in ch:
            Nsteps += 1
            if chh == v:
                print('Number of steps: ' + str(Nsteps))
                return True
    return False

######################################################################

def count(l, v):

    counter  = 0
    Nsteps = 0
    for ch in l:
        Nsteps += 1
        if ch == v:
            counter += 1

    print('Number of steps: ' + str(Nsteps))
    return counter

#####################################################################

def binary_search(l, v):
    l = sorted(l)
    b = 0
    e = len(l) - 1
    Nsteps = 0
    answer = False
    while b <= e:
        Nsteps += 1
        mid = (b + e) // 2
        if v < l[mid]:
            e = mid - 1
        elif v > l[mid]:
            b = mid + 1
        else:
            answer = True
            break
    print('Number of steps: ' + str(Nsteps))
    return answer

####################################################################

def insertionSort(l):
    Nsteps = 0
    for i in range(1, len(l)):

        p = i
        v = l[i]
        while v < l[p - 1] and 0 < p:
            Nsteps += 1
            l[p] = l[p - 1]
            p = p - 1

        l[p] = v

    print(str(Nsteps))
    return l










