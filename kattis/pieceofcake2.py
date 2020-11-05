from sys import stdin

def main():
    n, h, v = map(int, stdin.readline().split())

    a = h*v
    b = (n-h)*v
    c = h*(n-v)
    d = (n-h)*(n-v)

    largest = max([a, b, c, d])
    print(largest*4)

if __name__ == '__main__':
    main()