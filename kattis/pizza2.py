from sys import stdin

r, c = stdin.readline().rstrip('\n').split(' ')

r = float(r)
c = float(c)

cheese = ((r-c)*(r-c)/r)/r*100

print(cheese)
