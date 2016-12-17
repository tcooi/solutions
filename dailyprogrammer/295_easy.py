# https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/
from sys import stdin

a = list(stdin.readline().rstrip('\n'))
b = list(stdin.readline().rstrip('\n'))

result = a

print(''.join(a))

for i in range(len(list(a))):
    if a[i] != b[i]:
        result[i] = b[i]
        print(''.join(result))
