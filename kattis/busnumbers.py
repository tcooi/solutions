from sys import stdin

def main():
    buses = stdin.readline().rstrip("\n")
    numbers = stdin.readline().rstrip("\n")
    res = []

    nums = numbers.split(" ")
    num = sorted(nums, key=int)

    res.append(num[0])
    for i in range(1, len(num)):
        if i == len(num)-1:
            res.append(num[i])
        elif int(num[i]) == int(num[i-1])+1 and int(num[i+1]) == int(num[i])+1:
            res.append("-")
        else:
            res.append(num[i])

    for check in range(1, len(res)):
        if res[check] == "-" and res[check-1] == "-":
            res[check-1] = "x"

    result = [item for item in res if item != "x"]

    output = result[0]
    for i in range(1, len(result)):
        if result[i] != "-" and result[i-1] != "-":
            output += " " + result[i]
        else:
            output += result[i]

    print(output)

if __name__ == '__main__':
    main()
