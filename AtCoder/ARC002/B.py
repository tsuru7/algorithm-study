def isUruu(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

y, m, d = map(int, input().split('/'))

while True: 
    check = y % (m*d) == 0
    if check:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            break
        elif (m == 4 or m == 6 or m == 9 or m == 11) and d <= 30:
            break
        elif m == 2 and not isUruu(y) and d <= 28:
            break
        elif m == 2 and isUruu(y) and d <= 29:
            break

    d += 1
    if d > 31:
        m +=1
        d = 1
    if m > 12:
        y += 1
        m = 1
        d = 1

print('{:04d}/{:02d}/{:02d}'.format(y, m, d))
