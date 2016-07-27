from sys import stdin
# import operator

questions = stdin.readline().rstrip('\n')
answers = stdin.readline().rstrip('\n')

names = ['Adrian', 'Bruno', 'Goran']
guess = ['ABC', 'BABC', 'CCAABB']

for x in range(len(guess)):
    while len(guess[x]) < int(questions):
        guess[x] += guess[x]

# best = []
# point = 0

# for x in range(len(names)):
#     current = map(operator.eq, guess[x], answers).count(True)
#     if current > point:
#         point = current
#         best = [names[x]]
#     elif current == point:
#         best.append(names[x])

current = 0
best = 0
winners = []

for x in range(len(guess)):
    i_guess = guess[x]

    for index in range(len(answers)):
        if answers[index] == i_guess[index]:
            current += 1

    if current > best:
        best = current
        winners = [names[x]]
    elif current == best:
        winners.append(names[x])

    current = 0

print(best)
for winner in winners:
    print(winner)
