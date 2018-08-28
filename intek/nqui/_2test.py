player = playerB
def create_board():
    # create new board and fill all with '.'
    board = [['.' for x in range(9)] for x in range(9)]

    # replace center element with 'W' and 'B'
    board[4][4] = board[5][5] = 'W'; board[4][5] = board[5][4] = 'B'

    # replace first row and first col with below list
    order_row = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    order_col = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
    for i in board:
        for y in range(len(board)):
            board[0][y] = order_row[y]
            board[y][0] = order_col[y]
    return board


def print_board(board):
    # print board on terminal for visual view
    for i in board:
        for j in range(len(i)):
            print(i[j], end=' ')
        print()


# def find_current_player():
#    # find current player (PlayerA or PlayerB)
#     if():
#         return 'PlayerA'
#     else:
#         return 'PlayerB'


def player_color(player):
    # find color of PlayerA or PlayerB
    if (player == 'PlayerA'):
        return 'W'
    if (player == 'PlayerB'):
        return 'B'


def find_elements_on_board(color):
    # find all posions of color and return to a list | Ex: [[2, 3], [5, 1]]
    position_list = []
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if (board[i][j] == color):
                position_list.append([i, j])
    return position_list


def find_valid_choices():
    position_list = []
