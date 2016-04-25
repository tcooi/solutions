from sys import stdin

def main():
    cases = stdin.readline().rstrip("\n")

    for case in range(0, int(cases)):
        a = stdin.readline().rstrip("\n")
        b = stdin.readline().rstrip("\n")

        diff = ""
        if a == b:
            for i in range(0, int(len(a))):
                diff += "."
        else:
            for i in range(0, int(len(a))):
                if a[i] != b[i]:
                    diff += "*"
                else:
                    diff += "."

        print(a)
        print(b)
        print(diff)
        print("")

if __name__ == '__main__':
    main()
