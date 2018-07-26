from sys import stdin

winners = []

teams = int(stdin.readline())

for _ in range(0, teams):
    uni, team = stdin.readline().split()

    if uni not in winners:
        winners.append(uni)
        print('{} {}'.format(uni, team))
        
        if len(winners) == 12:
            break
