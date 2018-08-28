def opponent(player):
    if (player == 'W'):
        return 'B'
    elif (player == 'B'):
        return 'W'


def create_board():
    # Create a new board.
    board = [['.' for _ in range(9)] for _ in range(9)]
    row = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
    # Add center
    board[4][4] = board[5][5] = 'W';board[4][5] = board[5][4] = 'B'
    # Add cordinate to 1st row and 1st column
    for y in range(9):
        for x in range(9):
            board[x][0] = row[x]
        board[0][y] = col[y]
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
        while (in_board(curX, curY) and
               board[curX][curY] == opponent(player)):
            (curX, curY) = (curX + direct[0], curY + direct[1])
            if (in_board(curX, curY) and
                board[curX][curY] == '.'):
                return (curX, curY)
    except IndexError:
        return None


def find_valid_choices(player, board):
    direction_list = [(0, 1), (0, -1), (1, -1), (-1, -1),
                      (1, 0), (-1, 0), (-1, 1), (1, 1)]
    position_list = []
    valid_choices = []
    for y in range(1, 9):
        for x in range(1, 9):
            if (board[x][y] == player):
                position_list.append((x, y))
    for pos in position_list:
        for direct in direction_list:
            if (find_valid(player, board, pos, direct) != None and
                find_valid(player, board, pos, direct) not in valid_choices):
                valid_choices.append(find_valid(player,
                                                board,
                                                pos,
                                                direct))
    return valid_choices


def valid_choices_easy_read(valid_choices):
    dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    string = 'Valid choices: '
    for i in valid_choices:
        if i[0] in dict:
            string += dict[i[0]] + str(i[1]) + ' '
    return string


def list_valid_choices(valid_choices):
    dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    list_valid_choices = []
    string = ''
    for i in valid_choices:
        string = dict[i[0]] + str(i[1])
        list_valid_choices.append(string)
    return list_valid_choices


def move_to_valid_choice(move):
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    if move[0] in dict:
        return [dict[move[0]], int(move[1])]


def valid_move(move, board, valid_choices):
    if (in_board(move[0], move[1])):
        if (move in valid_choices and board[move[0]][move[1]] == '.'):
            return True
        else:
            return False

        
def do_move(player, move, board):
    if (player == 'W'):
        board[move[0]][move[1]] = 'W'
    if (player == 'B'):
        board[move[0]][move[1]] = 'B'


def can_flip(player, board, move, direct):
    curx = move[0] + direct[0]
    cury = move[1] + direct[1]
    if (not in_board(curX, curY) or board[curX][curY] != opponent(player)):
        return False
    while True:
        curX += direct[0]
        curY += direct[1]
        if (not in_board(curX, curY) or board[curX][curY] == '.'):
            return False
        if (board[curX][curY] == player):
            return True
        

def do_flip(player, board, move):
    direction_list = [(0, 1), (0, -1), (1, -1), (-1, -1),
                      (1, 0), (-1, 0), (-1, 1), (1, 1)]
    for direct in direction_list:
        if (can_flip(player, board, move, direct)):
            curX = move[0] + direct[0]
            curY = move[1] + direct[1]
            while (board[curX][curY] == opponent(player)):
                board[curX][curY] = player
                curX += direct[0]
                curY += direct[1]


if __name__ == '__main__':
    player = 'B'
    board = create_board()
    print_board(board)
    while True:
        valid_choices = find_valid_choices(player, board)
        print(valid_choices_easy_read(valid_choices))
        list_valid_choices = list_valid_choices(valid_choices)
        move = input('Player ' + player + ': ')
        while (len(move) == 0 or move not in list_valid_choices):
            print('Invalid choice.')
            move = input('Player ' + player + ': ')
        move = move_to_valid_choice(move)
        print(move)
        do_move(player, board, move)
        print_board(board)
        do_flip(player, board, move)
        print_board(board)
        player = opponent(player)
