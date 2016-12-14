from sys import stdin
import math

days = int(stdin.readline().rstrip('\n'))

# for i in range(days):
#     calories = int(stdin.readline().rstrip('\n'))
#     answer = (calories / 400) + (calories % 400 > 0)
#     print(answer)

for i in range(days):
    calories = float(stdin.readline().rstrip('\n'))
    answer = (calories / 400)
    print(int(math.ceil(answer)))
