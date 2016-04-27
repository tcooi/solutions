from sys import stdin

def main():
    while True:
        n = int(stdin.readline().rstrip('\n'))
        if n == -1:
            break

        total = 0
        result = 0
        for number in range(0, int(n)):
            speed, time = stdin.readline().rstrip('\n').split(' ')

            result += int(speed)*(int(time)-total)
            total = int(time)

        print(str(result) + ' miles')

if __name__ == '__main__':
    main()
