from sys import stdin
from decimal import *

atbat = int(stdin.readline())
b = map(int, stdin.readline().rstrip("\n").split(" "))
bases = 0

for i in b:
    if i == -1:
        atbat -= 1
    else:
        bases += i

getcontext().prec = 17
print(Decimal(bases)/Decimal(atbat))
