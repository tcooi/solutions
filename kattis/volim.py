from sys import stdin

position = int(stdin.readline().rstrip('\n'))
q = int(stdin.readline().rstrip('\n'))

total_time = 0
for i in range(q):
    time, outcome = stdin.readline().rstrip('\n').split(' ')

    total_time += int(time)

    if total_time >= 210:
        print(position)
        break

    if outcome == 'T':
        if position < 8:
            position += 1
        else:
            position = 1
