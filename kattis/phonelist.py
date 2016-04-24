from sys import stdin

def main():
    cases = stdin.readline().rstrip("\n")

    for case in range(0, int(cases)):
        numbers = []
        unique_numbers = stdin.readline().rstrip("\n")

        for num in range(0, int(unique_numbers)):
            number = stdin.readline().rstrip("\n")
            numbers.append(number)

        # sorted list means that list is not consistent if the right item of two neighbors starts with the left item
        numbers.sort()

        failed = False
        for check in range(1, int(unique_numbers)):
            if numbers[check].startswith(numbers[check-1]):
                print("NO")
                failed = True
                break

        if not failed:
            print("YES")

if __name__ == '__main__':
    main()
