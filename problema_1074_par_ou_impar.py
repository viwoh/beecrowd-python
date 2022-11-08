n = int(input(''))
for i in range (n):
    nx = int(input(''))
    if nx == 0:
        print('NULL')
    elif nx % 2 == 0:
        if nx > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if nx > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
