from sys import stdin
import re

def main():
    sentence = list(stdin.readline().rstrip("\n"))
    decoded = ""

    count = 0
    while count < len(sentence):
        decoded += sentence[count]
        if re.match("[aeiou]", sentence[count]):
            count += 3
        else:
            count += 1

    print(decoded)

if __name__ == '__main__':
    main()
