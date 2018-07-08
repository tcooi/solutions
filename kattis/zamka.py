from sys import stdin

l = int(stdin.readline())
d = int(stdin.readline())
x = int(stdin.readline())

n = 0
for i in range(l, d+1):
    n = map(int, str(i))
    if sum(n) == x:
        n = i
        break
print(n)

m = 0
for i in reversed(range(l, d+1)):
    m = map(int, str(i))
    if sum(m) == x:
        m = i
        break
print(m)
