from sys import stdin

a, b, c = [int(x) for x in stdin.readline().rstrip('\n').split(' ')]

if a == b + c:
    print('{}={}+{}'.format(a, b, c))
elif a == b - c:
    print('{}={}-{}'.format(a, b, c))
elif a == b * c:
    print('{}={}*{}'.format(a, b, c))
elif a == b / c:
    print('{}={}/{}'.format(a, b, c))
elif c == a + b:
    print('{}+{}={}'.format(a, b, c))
elif c == a - b:
    print('{}-{}={}'.format(a, b, c))
elif c == a * b:
    print('{}*{}={}'.format(a, b, c))
elif c == a / b:
    print('{}/{}={}'.format(a, b, c))
