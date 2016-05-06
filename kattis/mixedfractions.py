from sys import stdin

while True:
    # a, b = [int(x) for x in stdin.readline().rstrip('\n').split(' ')]
    a, b = map(int, raw_input().split(' '))
    if a == 0 and b == 0:
        break

    remainder = a%b
    whole = (a-remainder)/b

    print('{} {} / {}'.format(whole, remainder, b))
