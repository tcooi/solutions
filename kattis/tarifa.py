from sys import stdin

x = int(stdin.readline().rstrip("\n"))
n = int(stdin.readline().rstrip("\n"))

usage = 0
for i in stdin:
    usage += int(i)

tot = x*(n+1)
available = tot-usage

print(available)
