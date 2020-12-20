def histo_n(x):
    dic = {}
    re = []
    for ch in x:
        if ch not in re:
            re.append(ch)
            count = x.count(ch)
            dic[ch] = count
    return dic


#main
tuple = (1,2,-3,3,4,-3,3,3)
a = histo_n(tuple)
b = list(a.items())
print(b)