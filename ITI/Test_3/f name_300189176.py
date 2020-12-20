def make_teams(players, num_teams):

    '''(list of str, int)->2D list
Make num_teams teams out of the players in list players by counting off.
Players is a list of players' names and num_teams is the desired number of teams
Return a 2D list where each sublist is representing a team.
Preconditions: num_teams>= 1

>>> make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 3)
[['pele', 'venus', 'lionel'], ['maradona', 'fed'], ['serena', 'rafa']]
>>> make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 2)
[['pele', 'serena', 'fed', 'lionel'], ['maradona', 'venus', 'rafa']]
>>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3)
[['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
>>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)
[['1', '2', '3', '4', '5', '6', '7', '8', '9']]
>>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 4)
[['1', '5', '9'], ['2', '6'], ['3', '7'], ['4', '8']]
>>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 7)
[['1', '8'], ['2', '9'], ['3'], ['4'], ['5'], ['6'], ['7']]
>>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 11)
[['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], [], []]
>>> make_teams( [] , 3)
[[], [], []]
'''

    #YOUR CODE GOES HERE

    a = [[] for p in range(num_teams)]


    b = 0
    while len(players) > b:
        a[b % num_teams].append(players[b])

        b = b + 1


    return a







#print(make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 2))













