from sys import stdin

def main():
    moves = list(stdin.readline().rstrip("\n"))
    position = 1

    for move in moves:
        if move == "A":
            position = switch(position, 1, 2, 1)
        if move == "B":
            position = switch(position, 2, 3, 1)
        if move == "C":
            position = switch(position, 1, 3, 2)

    print(position)

def switch(position, position_a, position_b, change):
    if position == position_a or position == position_b:
        if position == position_a:
            position += change
        else:
            position -= change
    return position

if __name__ == '__main__':
    main()
