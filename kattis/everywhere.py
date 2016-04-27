from sys import stdin

cases = stdin.readline().rstrip('\n')

for _ in range(int(cases)):
    city_count = stdin.readline().rstrip('\n')

    city_list = []
    for _ in range(int(city_count)):
        city = stdin.readline().rstrip('\n')
        city_list.append(city)

    unique = set(city_list)

    print(len(unique))
