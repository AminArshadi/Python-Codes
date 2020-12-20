###
###
###
def clean_words(list):
    list1 = []
    for ch in list:
        s = ''
        for chh in ch:
            if chh not in string.punctuation and chh not in '\n\t' and not chh.isdigit():
                s += chh
        s = s.strip()
        s = s.lower()
        list1.append(s)

    return list1

def name(list):
    test = []
    for ch in list:
        test.append(ch[0])

    dic = {}
    for ch in set(test):
        n = set()
        for chh in list:
            if ch == chh[0]:
                n.add(chh[1])
        dic[ch] = n

    return dic

###
###
###

def open_file():
    
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    file_name = True
    while file_name == True:
        try:
            file_name=input("Enter the name of the file: ").strip()
            open(file_name)
            
            
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name = True

        except KeyboardInterrupt:
            print("Try again.")
            file_name = True
            
            
    return open(file_name)  #.read()

##############################################################
import string

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    
    open = fp.read()
    
    list = open.split('\n')

    list1 = clean_words(list)

    '''list1 = []
    for ch in list:
        s = ''
        for chh in ch:
            if chh not in string.punctuation and chh not in '\n\t' and not chh.isdigit():
                s += chh

            # elif ch in '\n\t':
            # s += ' '

        s = s.strip()
        s = s.lower()
        list1.append(s)'''

    '''list2 = []                        #####changed
    for ch in list1:
        if ch != '':
            list2.append(ch)'''

    # print(list2)





    list3 = []
    for ch in list1:             #####changed list2 to list1
        list3.append(ch.split())


    '''list4 = []
    for ch in list3:
        list = []
        for chh in ch:
            if len(chh) >= 2:
                list.append(chh)
        list4.append(list)'''

    list5 = []
    for i in range(len(list3)):
        for ch in list3[i]:
            if len(ch) >= 2:
                list5.append([ch, i + 1])

    '''test = []
    for ch in list5:
        test.append(ch[0])

    list6 = []
    for ch in set(test):
        n = []
        for chh in list5:
            if ch == chh[0]:
                n.append(chh[1])
        list6.append([ch, n])

    list6 = sorted(list6)'''

    list6 = name(list5)

    '''list6 = sorted(list6)

    dic = {}
    for ch in list6:
        if not ch[0] in dic:
            dic[ch[0]] = set(ch[1])'''

    return list6

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

#print(find_coexistance(read_file(open_file()), '  the,54676543 6  is  of'))

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



    


    
            













