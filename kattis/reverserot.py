from sys import stdin

def main():
    messages = []
    for line in stdin:
        messages.append(line.rstrip('\n'))

    messages.pop()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '.']

    for i in range(0, len(messages)):
        data = messages[i].split(' ')
        rot = int(data[0])
        msg = data[1]

        msg_reverse = list(msg[::-1])

        res = ''
        for letter in range(0, len(msg_reverse)):
            for i in range(0, len(alphabet)):
                if msg_reverse[letter] == alphabet[i]:
                    # print(i)
                    new_position = 0
                    if i+rot > 27:
                        new_position = i+rot-28
                    else:
                        new_position = i+rot

                    res += alphabet[new_position]

        print(res)

if __name__ == '__main__':
    main()
