from sys import stdin

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = stdin.readline().rstrip('\n')
a, b = msg[:len(msg)//2], msg[len(msg)//2:]

def rotate(x):
    v = 0
    w = ''

    for i in x:
        if abc.find(i):
            v += abc.find(i)

    for i in x:
        if abc.find(i) == 'A':
            w += abc[v]
        else:
            w += abc[(abc.find(i)+v) % len(abc)]

    return w

v = 0
decrypt = ''

for x,y in zip(rotate(b), rotate(a)):
    if abc.find(x) == 'A':
        v = 0
    else:
        v += abc.find(x)

    decrypt += abc[(abc.find(y) + abc.find(x)) % len(abc)]

print(decrypt)
