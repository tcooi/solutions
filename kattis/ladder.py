from sys import stdin
import math

height, angle = stdin.readline().rstrip('\n').split(' ')

height = float(height)
angle = float(angle)

ladder = height/math.sin(math.radians(angle))

print(int(math.ceil(ladder)))
