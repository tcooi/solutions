from sys import stdin

remainder = []

for _ in range(10):
    i = int(stdin.readline().rstrip('\n'))
    remainder.append(i%42)

print(len(set(remainder)))
