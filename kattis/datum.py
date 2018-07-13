from sys import stdin

day, month = map(int, stdin.readline().rstrip('\n').split())

year = 4
total = 0

if month == 1:
    total += 6
elif month == 2:
    total += 2
elif month == 3:
    total += 2
elif month == 4:
    total += 5
elif month == 5:
    total += 0
elif month == 6:
    total += 3
elif month == 7:
    total += 5
elif month == 8:
    total += 1
elif month == 9:
    total += 4
elif month == 10:
    total += 6
elif month == 11:
    total += 2
else:
    total += 4

total += year+day

weekday = total%7

if weekday == 1:
    day = "Monday"
elif weekday == 2:
    day = "Tuesday"
elif weekday == 3:
    day = "Wednesday"
elif weekday == 4:
    day = "Thursday"
elif weekday == 5:
    day = "Friday"
elif weekday == 6:
    day = "Saturday"
else:
    day = "Sunday"

print(day)
