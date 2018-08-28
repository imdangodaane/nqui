# def rock_paper_scissors():
#     p1 = input('Player 1? ')
#     p2 = input('Player 2? ')
#     _dict = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
#     if (p1 not in _dict or p2 not in _dict):
#         print('Error.')
#     else:
#         for i in _dict.keys():
#             if (p1 == i and p2 == _dict[i]):
#                 print('Player 2 wins.')
#             else:
#                 print('Player 1 wins.')
# rock_paper_scissors()
def rock_paper_scissors():
    p1 = input('Player 1? ')
    p2 = input('Player 2? ')
    _list = ['rock', 'paper', 'scissors']
    if (p1 not in _list or p2 not in _list):
        return 'Error.'
    else:
        if (p1 == p2):
            return 'Draw.'
        else:
            if (p1 == 'rock'):
                if (p2 == 'paper'):
                    return 'Player 2 wins.'
                else:
                    return 'Player 1 wins.'
            elif (p1 == 'paper'):
                if (p2 == 'scissors'):
                    return 'Player 2 wins.'
                else:
                    return 'Player 1 wins.'
            elif (p1 == 'scissors'):
                if (p2 == 'rock'):
                    return 'Player 2 wins.'
                else:
                    return 'Player 1 wins.'
            else:
                return 'Error.'
rock_paper_scissors()
