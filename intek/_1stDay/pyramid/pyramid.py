def pyramid():
    num = int(input())
    if (num % 2 == 0):
        num -= 1
    lines = int(num/2 + 1)
    spaces = int(num/2 - 0.5)
    block = 1
    for l in range(lines):
        for s in range(spaces):
            print(' ', end='')
        for n in range(block):
            print('#', end='')
        spaces -= 1
        block += 2
        print()


pyramid()
