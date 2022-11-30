a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a, b, c, d <= 10) and ((a <= b) and (c <= d))):
    print('\t', end='')
    for i in range(c, d+1):
        print(i, '\t', end='')
    for j in range(a, b+1):
        print()
        print(j, '\t', end='')
        for i in range(c, d+1):
            print(i * j, '\t', end='')