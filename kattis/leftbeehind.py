from sys import stdin

x, y = map(int, stdin.readline().split())

while x > 0 or y > 0:
    if x + y == 13:
        print('Never speak again.')
    elif x > y:
        print('To the convention.')
    elif x < y:
        print('Left beehind.')
    elif x == y:
        print('Undecided.')

    x, y = map(int, stdin.readline().split())
