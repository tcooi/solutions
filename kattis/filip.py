from sys import stdin

a, b = stdin.readline().split()

print(max(int(a[::-1]), int(b[::-1])))
