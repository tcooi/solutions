import sys

def main():
    winner = 0
    high_score = 0
    for x in range(0,5):
        points = sys.stdin.readline().split(" ")
        points = map(int, points)
        total_score = sum(points)

        if total_score > high_score:
            winner = x + 1
            high_score = total_score

    print(str(winner) + " " + str(high_score))

if __name__ == '__main__':
    main()
