from sys import stdin

def main():
    names = int(stdin.readline().rstrip('\n'))

    name_list = []
    for x in range(0, int(names)):
        name_list.append(stdin.readline().rstrip('\n'))

    name_list_increase = sorted(name_list)
    name_list_decrease = sorted(name_list, reverse=True)

    if name_list == name_list_increase:
        print('INCREASING')
    elif name_list == name_list_decrease:
        print('DECREASING')
    else:
        print('NEITHER')

if __name__ == '__main__':
    main()
