from sys import stdin
import math

n, w, h = map(int, stdin.readline().split())

fit = math.sqrt(w**2 + h**2)

for __ in range(0, n):
    match = int(stdin.readline())
    if match <= fit:
        print("DA")
    else:
        print("NE")
