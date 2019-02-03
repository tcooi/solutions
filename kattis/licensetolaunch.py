import sys

days = int(input().strip())
junk = input().strip().split(" ")

junk = list(map(int, junk))

junk_lowest = sys.maxsize
days_wait = 0

for current_day, junk in enumerate(junk):
    if junk < junk_lowest:
        junk_lowest = junk
        days_wait = current_day

print(days_wait)
