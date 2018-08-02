from sys import stdin

capacity, events = map(int, stdin.readline().split(' '))

denied = 0

for _ in range(0, events):
    event, people = stdin.readline().split(' ')

    if event == 'enter' and int(people) <= capacity:
        capacity -= int(people)
    elif event == 'enter' and int(people) > capacity:
        denied += 1
    else:
        capacity += int(people)

print(denied)
