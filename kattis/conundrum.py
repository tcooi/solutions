from sys import stdin

cipher = list(stdin.readline().rstrip('\n'))

i = 0
change = 0
while i < len(cipher):
    if cipher[i] != 'P':
        change += 1

    if cipher[i+1] != 'E':
        change += 1

    if cipher[i+2] != 'R':
        change += 1

    i += 3

print(change)
