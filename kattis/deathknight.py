from sys import stdin

battles = int(stdin.readline())

for _ in range(0, battles):
    if 'CD' in stdin.readline():
        battles -= 1

print(battles)
