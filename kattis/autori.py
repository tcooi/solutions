from sys import stdin

n = list(stdin.readline().rstrip("\n"))
s = n[0]

for i, letter in enumerate(n):
    if letter == "-":
        s += n[i+1]

print(s)
