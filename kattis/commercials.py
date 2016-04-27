# https://en.wikipedia.org/wiki/Maximum_subarray_problem
from sys import stdin

def main():
    n, p = stdin.readline().rstrip('\n').split(' ')
    line2 = stdin.readline().rstrip('\n').split(' ')
    listen = map(int, line2)

    profits = []
    for i in range(0, int(n)):
        profits.append(max_subarray(listen, i, p))

    print(max(profits))

def max_subarray(A, i, p):
    max_so_far = 0
    max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x - ((int(i)+1)*int(p)))
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == '__main__':
    main()
