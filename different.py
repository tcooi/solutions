from sys import stdin

def main():
    for line in stdin:
        data = line.rstrip("\n")
        numbers = data.split(" ")
        a = numbers[0]
        b = numbers[1]

        diff = abs(int(a)-int(b))

        print(diff)

if __name__ == '__main__':
    main()
