n = int(input())

for _ in range(n):
    row = list(map(int, input().split(' ')))
    k = row.pop(0)
    max_appliances = sum(row)-(k-1)
    print(max_appliances)