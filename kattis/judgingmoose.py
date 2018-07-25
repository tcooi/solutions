from sys import stdin

l, r = map(int, stdin.readline().split())

if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print('Even {}'.format(r*2))
else:
    print('Odd {}'.format(max(l,r)*2))
