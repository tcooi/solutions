from sys import stdin

cards = list(stdin.readline().rstrip('\n'))

total = 0
min_set = []

for c in set(cards):
    types = cards.count(c)
    total += types**2
    if len(set(cards)) == 3:
        min_set.append(types)
    else:
        min_set.append(0)

print(total + min(min_set)*7)
