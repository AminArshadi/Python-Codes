def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    # YOUR CODE GOES HERE
    cleanWord = ''
    for i in range(len(word)):
        if word[i] not in '!.?:,\'"-_\()[]{}%0123456789\t\n':
            cleanWord = cleanWord + word[i].lower()
        elif word[i] == ' ':
            cleanWord = cleanWord + ' '

    return cleanWord



def test_letters(w1, w2):
    '''(str,str, list of str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''

    # YOUR CODE GOES HERE
    answer = True
    for i in range(len(w1)):
        if w1[i] not in w2 : # w1.find(w1[i]) != w2.find(w1[i])
            answer =  False

    return answer



def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call test_anagram() function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.

    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''

    # YOUR CODE GOES HERE
    cleanedUp = clean_word(s)
    listed = cleanedUp.split(' ')

    result = []
    for i in listed:

        if i not in result:
            result.append(i)

    result = sorted(result)
    return result







def word_anagrams(word, wordbook):                                       #sorting problem
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook

    >>> word_anagrams("listen", wordbook)
    ['silent', 'enlist', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['care', 'acre']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''

    # YOUR CODE GOES HERE
    anagrams_list = []
    for ch in wordbook:
        if sorted(word) == sorted(ch) and ch != word:
            anagrams_list.append(ch)

    anagrams_list = sorted(anagrams_list)
    return anagrams_list






def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    # YOUR CODE GOES HERE
    result = []
    for i in l:
        count = 0
        for ch in wordbook:
            if sorted(i) == sorted(ch) and ch != i: # the same error
                count = count + 1
        result.append(count)

    return result





def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'race', 'ear']
    '''

    # YOUR CODE GOES HERE
    result = []
    for i in range(len(anagcount)):
        if str(k) == str(anagcount[i]):
            result.append(l[i])

    result = sorted(result)
    return result






def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)

    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['listen', 'item']
    '''

    # YOUR CODE GOES HERE
    maximum = max(anagcount)
    result = []
    for i in range(len(anagcount)):
        if anagcount[i] == maximum:
            result.append(l[i])

    result = sorted(result)
    return result






def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)

    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    # YOUR CODE GOES HERE
    result = []
    for i in range(len(anagcount)):
        if anagcount[i] == 0:
            result.append(l[i])

    result = sorted(result)
    return result


##############################
# main
##############################
wordbook = open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l, wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")

    print(max_anagram(l, anagcount))

    print('Here are there anagrams:')

    for ch in max_anagram(l, anagcount):
        print('Anagrams of ' + ch + ' are: ' + str(word_anagrams(ch, wordbook)))

    print('Here are the words from your file that have no anagrams: ')

    print(zero_anagram(l, anagcount))

    print('Say you are interested if there is  word in your file that has exactly k anagrams.')

    k = input('Enter an integer for k: ')


    while not k.isdigit():
        print('k must be an integer. Try again.')
        k = input('Enter an integer for k: ')


    print('Here is a word(s) in your file with exactly ' + str(k) + ' anagrams:')

    print(k_anagram(l, anagcount, k))





elif choice == '2':

    answer1 = input('Enter the letters that you have, one after another with no space: ')

    while ' ' in answer1:
        print('Error: you entered space(s).')
        answer1 = input('Enter the letters that you have, one after another with no space: ')

    print("Would you like help forming a word with")
    print("1. all these letters")
    print("2. all but one of these letters?")

    answer2 = input()


    while not (answer2 == '1' or answer2 == '2'):
        print('You must choose 1 or 2 Please try again.')
        print("Would you like help forming a word with")
        print("1. all these letters")
        print("2. all but one of these letters?")
        answer2 = input()


    if answer2 == '1':

        if word_anagrams(answer1, wordbook) != []:
            print('Here are the words that are comprised of letters: ' + answer1)
            print(word_anagrams(answer1, wordbook))

        elif word_anagrams(answer1, wordbook) == []:
            print('There is no word comprised of exactly these letters.')



    elif answer2 == '2':
        print('The letters you gave us are: ' + str(answer1))
        print('Let\'s see what we can get if we commit one of these letters.')

        for i in range(len(answer1)):
            mani_answer1 = answer1
            mani_answer1 = list(mani_answer1)
            mani_answer1.remove(answer1[i])
            mani_answer1 = ''.join(mani_answer1)
            print('Without the letter in position ' + str(i + 1) + ' we have letters ' + mani_answer1)

            if word_anagrams(mani_answer1, wordbook) != []:
                print('Here are the words that are comprised of letters: ' + mani_answer1)
                print(word_anagrams(mani_answer1, wordbook))

            elif word_anagrams(mani_answer1, wordbook) == []:
                print('There is no word comprised of letters: ' + mani_answer1)





else:
    print("Good bye")
