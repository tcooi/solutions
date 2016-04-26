from sys import stdin

def main():
    numbers = stdin.readline().rstrip('\n')

    number_list = []
    for number in range(0, int(numbers)):
        number_list.append(stdin.readline().rstrip('\n'))

    for i in number_list:
        if int(i) % 2 == 0:
            print(str(i) + " is even")
        else:
            print(str(i) + " is odd")

if __name__ == '__main__':
    main()
