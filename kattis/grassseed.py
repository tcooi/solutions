from sys import stdin

cost = stdin.readline().rstrip('\n')
lawns = stdin.readline().rstrip('\n')

total = 0

for _ in range(int(lawns)):
    a, b = stdin.readline().rstrip('\n').split()
    total += float(a) * float(b) * float(cost)

print(round(total, 7))
