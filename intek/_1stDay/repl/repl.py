import sys


def repl():
    string = ''
    while (string != 'quit'):
        string = str(input('relp> '))
        if (len(string) == 0):
            continue
        if (len(string) == 6):
            print('My length is 6')
        if (string[0] in ['a', 'e', 'i', 'o', 'u']):
            for _ in range(4):
                print(string[1] + string[2] + string[3])
        if (string == 'ls' or string == 'cat' or string == 'rev' or string =='pwd'):
            print('I know the command ' + string + ' !!')
        if (string[0] == '0' and string[-1] != '9'):
            for i in range(len(string)):
                if(string[i].isdigit()):
                    print(string[i])
    else:
        sys.exit()
repl()
