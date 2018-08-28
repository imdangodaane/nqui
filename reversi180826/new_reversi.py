def opponent(player):
    if (player == 'W'):
        return 'B'
    if (player == 'B'):
        return 'W'


def create_board():
    board = [['.' for _ in range(9)] for _ in range(9)]
    row = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
    for y in range(9):
        for x in range(9):
            board[x][0] = row[x]
        board[0][y] = col[y]
    board[4][4] = board[5][5] = 'W';board[4][5] = board[5][4] = 'B'
    return board


def print_board(board):
    for y in range(9):
        for x in range(9):
            print(board[x][y], end=' ')
        print()


def in_board(x, y):
    if (x > 0 and x < 9 and y > 0 and y < 9):
        return True
    else:
        return False


def find_valid(player, board, pos, direct):
    try:
        (curX, curY) = (pos[0] + direct[0], pos[1] + direct[1])
        while (board[curX][curY] == opponent(player) and in_board(curX, curY)):
            (curX, curY) = (curX + direct[0], curY + direct[1])
            if (in_board(curX, curY)):
                if (board[curX][curY] == '.'):
                    return (curX, curY)
    except IndexError:
        return None


def find_valid_choices(player, board):
    direction_list = [[0, -1], [1, -1], [1, 0], [1, 1],
                      [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    position_list = []
    valid_choices = []
    for y in range(1, 9):
        for x in range(1, 9):
            if (board[x][y] == player):
                position_list.append((x, y))
    for i in position_list:
        for j in direction_list:
            if (find_valid(player, board, i, j) != None and
                find_valid(player, board, i, j) not in valid_choices):
                valid_choices.append(find_valid(player,
                                               board,
                                               i,
                                               j))
    return valid_choices


def valid_choices_player_read(valid_choices):
    dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    string = 'Valid choices: '
    for i in valid_choices:
        if i[0] in dict:
            string += dict[i[0]] + str(i[1]) + ' '
    return string


def move_to_valid_choice(move):
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    if move[0] in dict:
        return (dict[move[0]], int(move[1]))


def valid_move(move, valid_choices):
    if (in_board(move[0], move[1]) and move in valid_choices
        and board[move[0]][move[1]] == '.'):
        return True
    else:
        return False


def do_move(player, board, move):
    if (player == 'W'):
        board[move[0]][move[1]] = 'W'
    elif (player == 'B'):
        board[move[0]][move[1]] = 'B'


def do_flip(player, board, move):
    direction_list = [(0, -1), (1, -1), (1, 0), (1, 1),
                      (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    for direct in direction_list:
        if (can_flip(player, board, move, direct)):
            curX = move[0] + direct[0]
            curY = move[1] + direct[1]
            while (board[curX][curY] == opponent(player)):
                board[curX][curY] = player
                curX = curX + direct[0]
                curY = curY + direct[1]


def can_flip(player, board, move, direct):
    curX = move[0] + direct[0]
    curY = move[1] + direct[1]
    if (not in_board(curX, curY)):
        return False
    if (board[curX][curY] != opponent(player)):
        return False
    while True:
        curX = curX + direct[0]
        curY = curY + direct[1]
        if (not in_board(curX, curY)):
            return False
        if (board[curX][curY] == player):
            return True
        if (board[curX][curY] == '.'):
            return False



################################# MAIN ##########################################
if __name__ == '__main__':
    player = 'B'
    board = create_board()
    print_board(board)
    while True:
        valid_choices = find_valid_choices(player, board)
        print(valid_choices)
        print(valid_choices_player_read(valid_choices))
        move = input('Player ' + player + ': ')
        move = move_to_valid_choice(move)
        while (valid_move(move, valid_choices) == False):
            print('Invalid Choice.')
            move = input('Player ' + player + ': ')
            move = move_to_valid_choice(move)
        do_move(player, board, move)
        print_board(board)
        do_flip(player, board, move)
        print_board(board)
        player = opponent(player)
