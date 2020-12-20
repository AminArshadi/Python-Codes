def move_zeros_v1(list):
    tmp = []
    count = 0
    for ch in list:
        if ch != 0:
            tmp.append(ch)
        elif ch == 0:
            count += 1
    for chh in range(count):
        tmp.append(0)
    

def move_zeros_v2(list):
    for ch in list:
        if ch == 0:
            list.remove(ch)
            list.append(ch)
    


def move_zeros_v3(list):
    n = 0
    while len(list) >= n:
        for i in range(len(list) - 1):
            if list[i] == 0:
                list[i] = list[i+1]
                list[i+1] = 0
        n += 1
