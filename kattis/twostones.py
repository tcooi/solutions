# from sys import stdin
#
# stones = int(stdin.readline().rstrip('\n'))
#
# if stones % 2 == 0:
#     print('Bob')
# else:
#     print('Alice')

from sys import stdin

def isodd(num):
    return num & 1 and 'Alice' or 'Bob'

stones = int(stdin.readline().rstrip('\n'))

print(isodd(stones))
