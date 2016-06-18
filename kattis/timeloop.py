from sys import stdin

chants = stdin.readline().rstrip('\n')

for x in range(int(chants)):
    print(str(x+1) + ' Abracadabra')
