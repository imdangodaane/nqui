def in_tek():
    num = int(input('Value? '))
    for i in range(1, num+1):
        if (i % 45 == 0):
            print('InTek')
        elif (i % 9 == 0):
            print('Tek')
        elif (i % 5 == 0):
            print('In')
        else:
            print(i)
in_tek()
