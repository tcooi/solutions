from sys import stdin

def main():
    jon = stdin.readline().rstrip("\n")
    requirement = stdin.readline().rstrip("\n")

    if len(jon) >= len(requirement):
        print("go")
    else:
        print("no")

if __name__ == '__main__':
    main()
