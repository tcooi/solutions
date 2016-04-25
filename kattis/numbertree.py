from sys import stdin

def main():
    line = stdin.readline().rstrip("\n").split(" ")
    height = int(line[0])
    path = list(line[1])
    nodes = (2**(height+1))-1

    if height == 0:
        print(1)
    elif line[1] == "":
        print(nodes)
    else:
        find_node(nodes, path)

def find_node(nodes, path):
    binary = ""

    # use path to create a binary representation of the correct position
    for i in range(0, len("".join(path))):
        if path[i] == "L":
            binary += "0"
        else:
            binary += "1"

    # skip to right "level" and find correct number with our binary value
    skip = (2**(len(path)))-1
    reverse_numbers = range(1, nodes+1)[::-1]
    res = reverse_numbers[skip+int(binary, 2)]

    print(res)

if __name__ == '__main__':
    main()
