from sys import stdin

for _ in range(0, int(stdin.readline())):
    test = stdin.readline().rstrip('\n')
    if '=' in test:
        print('skipped')
    else:
        a, b = map(int, test.split('+'))
        print(a + b)
