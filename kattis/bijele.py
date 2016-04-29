from sys import stdin

a, b, c, d, e, f = [int(x) for x in stdin.readline().rstrip('\n').split(' ')]

print('%d' %(1-a) + ' %d' %(1-b) + ' %d' %(2-c) + ' %d' %(2-d) + ' %d' %(2-e) + ' %d' %(8-f))
