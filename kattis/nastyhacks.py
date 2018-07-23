from sys import stdin

for _ in range(0, int(stdin.readline())):
    r, e, c = map(int, stdin.readline().split())
    if r < (e-c):
        print("advertise")
    elif r == (e-c):
        print("does not matter")
    else:
        print("do not advertise")
