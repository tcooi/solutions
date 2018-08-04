from sys import stdin

n, t = map(int, stdin.readline().split())
tasks = list(map(int, stdin.readline().split()))

complete = 0
time = 0

for i in range(n):
    time += tasks[i]
    if time <= t:
        complete += 1
    if time >= t:
        break

print(complete)
