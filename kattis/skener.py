from sys import stdin

r, c, zr, zc = stdin.readline().rstrip('\n').split()

for _ in range(int(r)):
    x = stdin.readline().rstrip('\n')
    x = list(x)
    row = ""
    
    for i in x:
        for _ in range(int(zc)):
            row += i

    for _ in range(int(zr)):
        print(row)
