from sys import stdin

cases = int(stdin.readline().rstrip('\n'))

for _ in range(cases):
    name, studies, dob, courses = stdin.readline().rstrip('\n').split(' ')

    if int(studies.split('/')[0]) >= 2010 or int(dob.split('/')[0]) >= 1991:
        print(str(name) + ' eligible')
    elif int(courses) >= 41:
        print(str(name) + ' ineligible')
    else:
        print(str(name) + ' coach petitions')
