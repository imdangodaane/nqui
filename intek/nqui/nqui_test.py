def create_board_game():
    board_game = [
                  [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                  ['1', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['2', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['4', '.', '.', '.', 'W', 'B', '.', '.', '.'],
                  ['5', '.', '.', '.', 'B', 'W', '.', '.', '.'],
                  ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['8', '.', '.', '.', '.', '.', '.', '.', '.']
                 ]
    board = [['.' for x in range(9)] for x in range(9)]
    print(board)
    for i in board_game:
        for j in range(len(i)):
            print(i[j], end=' ')
        print()
    choices = {
                'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              }


def current_player_color(args):
    if (PlayerA):
        return 'W'
    else:
        return 'B'

def find_element_on_board(color):
    pos = []
    for i in range(1, len(board_game)):
        for j in range(1, len(i)):
            if (board_game[i][j] == 'W'):
                pos.append([i, j])


def find_valid_choice(args):


def fill_valid_choice():


def valid_change():


def find_score():


def end_turn():
