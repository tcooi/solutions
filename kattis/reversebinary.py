from sys import stdin

def main():
    i = stdin.readline().rstrip("\n")
    binary = bin(int(i))[2:]
    reverse_binary = str(binary)[::-1]
    res = int(reverse_binary, 2)
    print(res)

if __name__ == '__main__':
    main()
