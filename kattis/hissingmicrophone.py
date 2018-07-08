from sys import stdin

input = list(stdin.readline().rstrip('\n'))

hiss = False

for x in range(0, len(input)-1):
    if input[x] == "s" and input[x+1] == "s":
        hiss = True
        break

if hiss:
    print("hiss")
else:
    print("no hiss")
