from sys import stdin

def main():
    cases = stdin.readline().rstrip("\n")

    for case in range(0, int(cases)):
        command = stdin.readline().rstrip("\n")
        
        if command.startswith("Simon says "):
            print(command[11:])

if __name__ == '__main__':
    main()
