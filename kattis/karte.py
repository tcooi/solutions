from sys import stdin

deck = []
pkht = [[],[],[],[]]

line = stdin.readline().rstrip('\n')

for i in range(0, len(line), 3):
    deck.append(line[i:i+3])

if len(deck) != len(set(deck)):
    print('GRESKA')
else:
    for i in deck:
        if i.startswith('P'):
            pkht[0].append(i)
        elif i.startswith('K'):
            pkht[1].append(i)
        elif i.startswith('H'):
            pkht[2].append(i)
        else:
            pkht[3].append(i)

    print(str(13-len(pkht[0])) + ' ' + str(13-len(pkht[1])) + ' ' + str(13-len(pkht[2])) + ' ' + str(13-len(pkht[3])))
