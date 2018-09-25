P, T = map(int, input().split())

solved = 0

for _ in range(P):
    check = False
    for _ in range(T):
        x = input()
        x = x[0].lower() + x[1:]
        for i in range(len(x)):
            if x[i].isupper():
                check = True
                break
        # if x.islower() == False:
        #     check = True
        #     break
    if not check:
        solved += 1

print(solved)
