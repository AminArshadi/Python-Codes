def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    friends.remove(friends[0])
    network = []

    # YOUR CODE GOES HERE
    friendsList = []
    for ch in friends:
        friendsList.append(ch.split(' '))

    friendsList2 = []
    for ch in friendsList:
        friendsList2.append([int(ch[0]), int(ch[1])])
        friendsList2.append([int(ch[1]), int(ch[0])])
    friendsList2.sort()

    userIDs = []
    for ch in friendsList2:
        if [ch[0]] not in userIDs:
            userIDs.append([ch[0]])

    for ch in userIDs:
        l = []
        for chh in friendsList2:
            if chh[0] == ch[0]:
                l.append(chh[1])
        network.append((ch[0], l))







    return network

##############################################################################
def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs,
    and friends of user 1 and user 2 sorted
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common = []

    # YOUR CODE GOES HERE
    for ch in network:
        if ch[0] == user1:
            userOne = ch[1]
        elif ch[0] == user2:
            userTwo = ch[1]
    
    for ch in userOne:
        if ch in userTwo:
            common.append(ch)
            

    return common

#############################################################################

def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.

    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    for ch in network:
        if ch[0] == user:
            userFriends = ch[1]
            userUser = network.index(ch)


    commonCount = []
    for ch in network:
        count = 0
        for chh in userFriends:
            if chh in ch[1] and user not in ch[1]:
                count += 1
        commonCount.append(count)
    #print(commonCount)
    
    commonCount[userUser] = 0
    #print(commonCount)
    


    '''maxCommon = commonCount.index(max(commonCount))
    print(str(maxCommon))

    commonCount[maxCommon] = 0
    print(commonCount)'''

    maxCommon = commonCount.index(max(commonCount))
    #print(str(maxCommon))
    



    if maxCommon > 0:
        return network[maxCommon][0]
    '''else:
        return None'''

#print(recommend(114, create_network('net3.txt')))

#############################################################################

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    count = 0
    for ch in network:
        if len(ch[1]) >= k:
            count += 1
            
    return count

#############################################################################

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    maximum = 0
    for ch in network:
        if len(ch[1]) > maximum:
            maximum = len(ch[1])
            
    return maximum

#############################################################################

def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    numFriends = 0
    for ch in network:
        numFriends += len(ch[1])
            
    return numFriends/len(network)

#############################################################################

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends = []
    friendsNum = []
    # YOUR CODE GOES HERE
    for ch in network:
        friendsNum.append(len(ch[1]))
        
    maximum = max(friendsNum)
    
    for i in range(len(friendsNum)):
        if friendsNum[i] == maximum:
            max_friends.append(network[i][0])
        
    return max_friends

#############################################################################

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''

    # YOUR CODE GOES HERE
    everyone = []
    for ch in network:
        everyone.append(ch[0])

    
    for ch in network:
        ch[1].append(ch[0])
        
        if sorted(everyone) == sorted(ch[1]):
            return True
        
    return False

#############################################################################


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    # YOUR CODE GOES HERE

    everyone = []
    for ch in network:
        everyone.append(ch[0])



    while True:
        a = input('Enter an integer for a user ID: ')
        if not a.isdigit():
            print('That was not an integer. Please try again.')

        elif int(a) not in everyone:
            print('That user ID does not exist. Try again.')
        
        else:
            break











