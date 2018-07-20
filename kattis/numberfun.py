from sys import stdin

cases = int(stdin.readline())

for __ in range(0, cases):
    a, b, c = map(float, stdin.readline().split())
    if c == a + b or c == a - b or c == b - a or c == a / b or c == b / a or c == a * b:
        print("possible")
    else:
        print("Impossible")
