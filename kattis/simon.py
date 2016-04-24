from sys import stdin

def main():
    cases = stdin.readline().rstrip("\n")

    for case in range(0, int(cases)):
        sentence = stdin.readline().rstrip("\n")

        if "simon says " in sentence:
            print(sentence.split(" ", 2)[2])
        else:
            print("")

if __name__ == '__main__':
    main()
