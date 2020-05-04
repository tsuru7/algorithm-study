weekday = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
s=input()
for i in range(0, 7):
    if (weekday[i] == s):
        print(7-i)

