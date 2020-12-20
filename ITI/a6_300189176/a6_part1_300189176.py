def clean_words(str):
    '''(str)->list'''
    str = str.lower()
    s = ''
    for ch in str:
        if ch not in string.punctuation and not ch.isdigit():
            s += ch

    return s.split('\n')

def list_maker(list):
    '''(list)->list'''
    list2 = []
    for ch in list:
        list2.append(ch.strip().split())

    return list2

def dict_maker(list2):
    '''(list)->dictionaty'''
    dic1 = {}
    for i in range(len(list2)):
        for ch in list2[i]:
            if len(ch) >= 2:
                if ch not in dic1:
                    dic1[ch] = {i + 1}
                else:
                    dic1[ch].add(i + 1)
    return dic1

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    file_name = True
    while file_name == True:
        try:
            file_name = input("Enter the name of the file: ").strip()
            open(file_name)


        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name = True

        except KeyboardInterrupt:
            print("Try again.")
            file_name = True

    return open(file_name)  # .read()


##############################################################
import string


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE

    open = fp.read()

    list1 = clean_words(open)
    
    list2 = list_maker(list1)
    
    dic1 = dict_maker(list2)

    return dic1


##############################################################

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    query = query.strip().split()
    list1 = []
    for ch in query:
        s = ''
        for chh in ch:
            if chh not in string.punctuation and chh not in '\n\t':
                s += chh

            elif ch in '\n\t':
                s += ' '

        s = s.strip()
        s = s.lower()
        list1.append(s)

    list2 = []
    for ch in list1:
        if ch != '':
            list2.append(ch)

    z = D[list2[0]]
    for i in range(1, len(list2)):
        z = z.intersection(D[list2[i]])

    z = sorted(list(z))
    return z


# print(find_coexistance(read_file(open_file()), '  the,54676543 6  is  of'))

##############################
# main
##############################
file = open_file()
d = read_file(file)
query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
while query.lower() != 'q':
    try:
        answer = find_coexistance(d, query)

        if len(answer) != 0:
            print('The one or more words you entered coexisted in the following lines of file:')
            for ch in answer:
                print(ch, end = ' ')
            print()
        else:
            print('The one or more words you entered does not coexist in a same line of the file.')

    except KeyError as a:
        print('Word ' + str(a) + ' not in the file.')

    except IndexError:
        print('Word " not in the file.')

    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()





















