def min_enclosing_rectangle(circle_radius,x_coordinates,y_coordinates):
    '''(number,number,number)->(number,number) or None
    Prints the x and y coordinates of the bottom-left corner of the rectangle'''
    if circle_radius >= 0:
        x_c = x_coordinates - circle_radius
        y_c = y_coordinates - circle_radius
        return (x_c,y_c)
    else:
        return None
print(min_enclosing_rectangle(2,10,2))
#################################################################################################################
def vote_percentage(results):
    '''(None)->float
    Preconditions:The function takes a string as input; string results has at least one yes or no ; the only words
    present are yes, no and/or abstained
    Prints the percentage of 'yes's among 'no's '''
    n_yes = 'yes'
    answer_1 = results.count(n_yes)
    n_no = 'no'
    answer_2 = results.count(n_no)
    return answer_1 / (answer_1 + answer_2)

print(vote_percentage('yes yes yes yes yes abstained yes yes yes yes'))
#################################################################################################################
def vote_percentage(results):
    '''(None)->float
    Preconditions:The function takes a string as input; string results has at least one yes or no ; the only words
    present are yes, no and/or abstained
    Prints the percentage of 'yes's among 'no's '''
    n_yes = 'yes'
    answer_1 = results.count(n_yes)
    n_no = 'no'
    answer_2 = results.count(n_no)
    return answer_1 / (answer_1 + answer_2)

def vote():
    '''(None)->None
    Prints proposal passes unanimously, If all the votes are yes; prints the proposal passes with super majority, if at least 2/3 of the votes are
    yes; prints proposal passes with simple majority, if at least 1/2 of the votes are yes and prints proposal fails, if the yes are less that 1/2'''
    vote = input('Enter the yes, no, abstained votes one by one and then press enter: ')
    n_v = vote_percentage(vote)
    if n_v == 1:
        print('Proposal passes unanimously')
    elif 1 > n_v >= 2/3:
        print('Proposal passes with super majority')
    elif 2/3 > n_v >= 1/2:
        print('proposal passes with simple majority')
    else:
        print('Proposal fails')

vote()