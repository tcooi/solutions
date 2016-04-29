from sys import stdin

cases = int(stdin.readline().rstrip('\n'))

for i in range(cases):
    guests = int(stdin.readline().rstrip('\n'))
    numbers = [int(x) for x in stdin.readline().rstrip('\n').split(' ')]

    for j in numbers:
        if numbers.count(j) == 1:
            number = j

    print('Case #{}: {}'.format(i+1, number))
