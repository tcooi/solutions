from sys import stdin

n = stdin.readline().rstrip('\n')
res = []

for __ in range(int(n)):
    estimate = stdin.readline().rstrip('\n')
    print(len(estimate))
