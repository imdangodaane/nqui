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


def main():
    create_board()
    print_board()
