
a = int(input())
b = int(input())
q = ""

if a > 0:
    q = 1 if b > 0 else 4
else:
    q = 2 if b > 0 else 3

print(q)
