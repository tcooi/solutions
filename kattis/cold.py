from sys import stdin

def main():
    days = stdin.readline().rstrip("\n")
    temps = stdin.readline().rstrip("\n").split(" ")

    count = 0
    for day in range(0, int(days)):
        if temps[day] < "0":
            count += 1

    print(count)

if __name__ == '__main__':
    main()
