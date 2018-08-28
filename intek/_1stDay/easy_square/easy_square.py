def easy_square():
    length = int(input())
    string = input()
    for y in range(length):
        for x in range(length):
            if ((y, x) == (0, 0) or (y, x) == (0, length - 1) or (y, x) == (length - 1, 0) or (y, x) ==  (length - 1, length - 1)):
                print(string[0], end='')
            elif (y == 0 and x > 0 and x < length - 1):
                print(string[1], end='')
            elif (x == 0 and y > 0 and y < length - 1):
                print(string[3], end='')
            elif (x == length - 1 and y > 0 and y < length - 1):
                print(string[4], end='')
            elif (y == length - 1 and x > 0 and x < length - 1):
                print(string[2], end='')
            else:
                print(' ', end='')
        print()
easy_square()
