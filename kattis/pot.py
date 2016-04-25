from sys import stdin

def main():
    cases = stdin.readline().rstrip("\n")

    res = 0
    for case in range(0, int(cases)):
        i = list(stdin.readline().rstrip("\n"))
        num = "".join(i[0:len(i)-1])
        power = i.pop()
        
        res += int(num)**int(power)

    print(res)

if __name__ == '__main__':
    main()
