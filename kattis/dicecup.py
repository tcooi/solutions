from sys import stdin

numbers = stdin.readline().rstrip('\n').split()

numbers = list(map(int, numbers))

if numbers[0] == numbers[1]:
    print(numbers[0] + 1)
else:
    low = min(numbers)
    high = max(numbers)
    for i in range(low, high+1):
        print(i+1)
