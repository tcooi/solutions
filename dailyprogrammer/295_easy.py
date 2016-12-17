from sys import stdin

a = list(stdin.readline().rstrip('\n'))
b = list(stdin.readline().rstrip('\n'))

result = a

print(''.join(a))

for i in range(len(list(a))):
    if a[i] != b[i]:
        result[i] = b[i]
        print(''.join(result))
