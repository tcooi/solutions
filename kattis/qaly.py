periods = int(input())
qaly = 0

for _ in range(periods):
    q, y = map(float, input().split())
    qaly += q * y

print('{0:.3f}'.format(qaly))
