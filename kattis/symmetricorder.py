from sys import stdin
import re

def main():
    strings = []
    for line in stdin:
        strings.append(line.rstrip('\n'))

    numbers = []
    names = []
    for i in range(0, len(strings)):
        if re.match('\d+', strings[i]):
            numbers.append(strings[i])
        else:
            names.append(strings[i])

    numbers.pop()

    skip = 0
    for i in range(0, len(numbers)):
        print('SET' + ' ' + str(i+1))

        list_up = []
        list_down = []
        for j in range(skip, int(numbers[i])+skip, 2):
            list_up.append(names[j])

        for j in range(skip+1, int(numbers[i])+skip, 2):
            list_down.append(names[j])

        skip += int(numbers[i])

        res = list_up + list_down[::-1]

        for name in res:
            print(name)

if __name__ == '__main__':
    main()
