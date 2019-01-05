import math

t = int(input())

for _ in range(t):
    n = int(input())
    f = math.factorial(n)
    print(f%10)
