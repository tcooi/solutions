from sys import stdin

phrase = stdin.readline().split()

if len(phrase) == len(set(phrase)):
    print("yes")
else:
    print("no")
