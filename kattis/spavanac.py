from sys import stdin

def main():
    time = stdin.readline().rstrip("\n").split(" ")
    hour = time[0]
    minute = time[1]

    if int(hour) == 0 and int(minute) < 45:
        hour = 23
        minute = 60-(45-int(minute))
        print_time(hour, minute)
    elif int(minute) >= 45:
        minute = int(minute)-45
        print_time(hour, minute)
    else:
        hour = int(hour)-1
        minute = 60-(45-int(minute))
        print_time(hour, minute)

def print_time(hour, minute):
    print(str(hour) + " " + str(minute))

if __name__ == '__main__':
    main()
