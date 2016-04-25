from sys import stdin

def main():
    name = list(stdin.readline().rstrip('\n'))

    res = name[0]
    for x in range(1, len(name)):
        if name[x] != name[x-1]:
            res += name[x]

    print(res)

if __name__ == '__main__':
    main()
