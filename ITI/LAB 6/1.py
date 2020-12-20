def histogram(string):
    dic = {}
    for ch in string:
        dic[ch] = dic.get(ch, 0) + 1


    dic = sorted(list(dic.items()))
    return dic

#main
string = input('Please enter a string: ')
a = histogram(string)
print(a)
