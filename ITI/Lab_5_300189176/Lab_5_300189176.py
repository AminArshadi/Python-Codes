#################################################################################################################
#Exercise 4 (version 1):
#################################################################################################################

def count(string, ch):

    count = 0
    for i in range(len(string) - len(ch)):
        if ch == string[i: i + len(ch)]:
            count = count + 1

    if string[-len(ch):] == ch:
        count += 1

    return count


#main
str = input('Enter a chain of characters: ')
print(count(str, 'a'))

#################################################################################################################
#Exercise 4 (version 2):
#################################################################################################################

def count(string, ch):

    result = string.count(ch)
    return result


#main
str = input('Enter a chain of characters: ')
print(count(str, 'a'))

#################################################################################################################
#Exercise 5:
#################################################################################################################

def spaces(str):
    list1 = list(str)

    result = ' '.join(list1)

    result = "'" + result + "'"

    return result

#main
str = raw_input('Enter a chain of characters: ')
print(spaces(str))

#################################################################################################################
#Exercise 6:
#################################################################################################################

def code(str):
    list2 = []
    list1 = list(str)

    for i in range(0, len(list1) - 1, 2):
        list2.append(list1[i + 1])
        list2.append(list1[i])

    str = ''.join(list2)
    str = "'" + str + "'"

    return str


#main
str = input('Enter a chain of characters: ')
print(code(str))





















