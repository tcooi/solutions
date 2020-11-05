from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    b, p = map(float, stdin.readline().split(' '))

    possible_ABPM = ((60*b)/p)-(60/p)

    calculated_BPM = (60*b)/p

    maximum_possible_ABPM = ((60*b)/p)+(60/p)

    print('{} {} {}'.format(possible_ABPM, calculated_BPM, maximum_possible_ABPM))

