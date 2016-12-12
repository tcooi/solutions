from sys import stdin

cups = int(stdin.readline().rstrip('\n'))

answers = {}

for i in range(cups):
    x, y = stdin.readline().rstrip('\n').split()

    if x.isdigit():
        answers[float(x)/2] = y
    else:
        answers[int(y)] = x

for k, v in sorted(answers.items()):
    print(v)
