def readinput():
    x, y = map(int, input().split())
    return x, y

def main(x, y):
    if y == 0:
        if x < 0:
            return abs(x)
        else:
            return x + 1
    elif abs(x) < abs(y):
        if x > 0 and y > 0:
            return abs(y) - abs(x)
        elif y < 0 and x < 0:
            return abs(y) - abs(x) + 2
        else:
            return abs(y) - abs(x) + 1
    elif abs(x) == abs(y):
        if x*y >= 0:
            return 0
        else:
            return 1
    elif abs(x) > abs(y):
        if y > 0 and x > 0:
            return abs(x) - abs(y) + 2
        elif x < 0 and y < 0:
            return abs(x) - abs(y)
        else:
            return abs(x) - abs(y) + 1

def printans(ans):
    print(ans)

if __name__ == '__main__':
    x, y = readinput()
    ans = main(x, y)
    printans(ans)
