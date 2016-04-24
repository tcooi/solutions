from sys import stdin

def main():
    n = int(stdin.readline().rstrip("\n"))
    before_del = stdin.readline().rstrip("\n")
    after_del = stdin.readline().rstrip("\n")
    inverse_state = list(before_del)

    # find correct after deletion state
    for i in range(0, len(inverse_state)):
        if inverse_state[i] == "1":
            inverse_state[i] = "0"
        else:
            inverse_state[i] = "1"

    inverse_state = "".join(inverse_state)

    if n % 2 == 1 and after_del == inverse_state:
        print("Deletion succeeded")
    elif n % 2 == 0 and before_del == after_del:
        print("Deletion succeeded")
    else:
        print("Deletion failed")

if __name__ == '__main__':
    main()
