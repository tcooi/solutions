from sys import stdin

x = []
y = []
p_x = ''
p_y = ''

for _ in range(3):
    point_x,point_y = (stdin.readline().rstrip('\n').split(' '))
    x.append(point_x)
    y.append(point_y)

for point_x in x:
    if x.count(point_x) == 1:
        p_x = point_x

for point_y in y:
    if y.count(point_y) == 1:
        p_y = point_y

print(p_x, p_y)
