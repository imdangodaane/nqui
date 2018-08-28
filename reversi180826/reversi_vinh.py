def print_board(a):
    # in dong dau tien cua ban co
    print('  a b c d e f g h')
    for j in range(len(a)):
        print(str(j + 1) + " ", end='')
        print(' '.join(i for i in a[j]))


def init_board(a):
    # duyet theo dong
    for i in range(8):
        # them phan tu dong
        a.append([])
        for j in range(8):
            a[i].append('.')
    a[3][3] = a[4][4] = 'W'
    a[3][4] = a[4][3] = 'B'


# Ham kiem tra da ket thuc game(Khong con nuoc di) hay chua
def end_game(a, turn):
    return len(find_valid_choice(a, turn)) == 0


def in_board(a, x, y):
    return y < len(a) and x < len(a[0]) and y >= 0 and x >= 0


# ham tim toa do
def move(a, i, j, v, player, opponent):
    y = i + v[1]
    x = j + v[0]
    check = False
    while in_board(a, x, y) and a[y][x] == opponent:
        y += v[1]
        x += v[0]
        check = True
    if in_board(a, x, y) and a[y][x] == player and check:
        return (x, y)
    else:
        return ()


# ham tim toa do cua nguoi choi de danh
def find_valid_choice(a, player='B'):
    if player == 'B':
        opponent = 'W'
    elif player == 'W':
        opponent = 'B'
    valid_choice = {}
    vs = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for j in range(len(a[0])):
        for i in range(len(a)):
            if a[i][j] == '.':
                choice = []
                for z in range(len(vs)):
                    valid_choice_ij = move(a, i, j, vs[z], player, opponent)
                    if len(valid_choice_ij) > 0:
                        choice.append([vs[z], valid_choice_ij])
                if len(choice) > 0:
                    valid_choice[(j, i)] = choice
    return valid_choice


def print_valid_player(valid_choice):
    s = ""
    i = 0
    validList = []
    for key in valid_choice.keys():
        x = chr(key[0] + ord('a'))
        y = str(key[1] + 1)
        s = x+""+y
        validList.append(s)
        if i != len(valid_choice) - 1:
            i += 1
    validList.sort()
    print("Valid choices:", ' '.join(i for i in validList))


def Player(a, valid_choice, player, opponent):
    while True:
        print_valid_player(valid_choice)
        command = input("Player " + player + ": ")
        if len(command) != 2:
            print(command + ": Invalid choice")
            continue
        c1 = command[0]
        c2 = command[1]
        if c1 < 'a' or c1 > 'h' or c2 < '1' or c2 > '8':
            print(command + ": Invalid choice")
            continue
        x = ord(c1) - ord('a')
        y = int(c2) - 1
        if (x, y) in valid_choice:
            a[y][x] = player
            choice = valid_choice[(x, y)]
            for c in choice:
                vv = c[0][1]
                vx = c[0][0]
                xx = x + vx
                yy = y + vv
                while a[yy][xx] != player:
                    a[yy][xx] = player
                    xx = xx + vx
                    yy = yy + vv
            break
        else:
            print(command + ": Invalid choice")


def Score(a, player):
    score = 0
    for row in a:
        for c in row:
            if c == player:
                score += 1
    return score


# Main game
def main_game():
    a = []
    init_board(a)

    print_board(a)
    turn = 'B'
    number_cannot_play = 0
    while True:
        valid_choice = find_valid_choice(a, player='B')
        if len(valid_choice) > 0:
            number_cannot_play = 0
            Player(a, valid_choice, 'B', 'W')
            print_board(a)
        else:
            print("Player B cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

        valid_choice = find_valid_choice(a, player='W')
        if len(valid_choice) > 0:
            number_cannot_play = 0
            Player(a, valid_choice, 'W', 'B')
            print_board(a)
        else:
            print("Player W cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

    score_w = Score(a, 'W')
    score_b = Score(a, 'B')
    print("End of the game. W: " + score_w + ", B: " + score_b)
    if score_w > score_b:
        print("B wins.")
    else:
        print("W wins.")


# Chay ham main game
def main_game():
    a = []
    init_board(a)
    turn = 'B'
    number_cannot_play = 0
    # Vao vong lap de choi game
    # Lap cho den khi kiem tra game da ket thuc(Khong con nuoc de di)
    while True:

        # Nguoi choi 'B'
        valid_choice = find_valid_choice(a, player='B')
        if len(valid_choice) > 0:
            print_board(a)
            number_cannot_play = 0
            Player(a, valid_choice, 'B', 'W')

        else:
            print_board(a)
            print("Player B cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

        # Nguoi choi 'W'
        valid_choice = find_valid_choice(a, player='W')
        if len(valid_choice) > 0:
            print_board(a)
            number_cannot_play = 0
            Player(a, valid_choice, 'W', 'B')
        else:
            print_board(a)
            print("Player W cannot play.")
            number_cannot_play += 1
            if number_cannot_play == 2:
                break

    score_w = Score(a, 'W')
    score_b = Score(a, 'B')
    print("End of the game. W: " + str(score_w) + ", B: " + str(score_b))
    if score_w > score_b:
        print("W wins.")
    else:
        print("B wins.")


# Chay ham main
main_game()

# reference from google and others team
