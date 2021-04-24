def readinput():
    w, h, n = map(int, input().split())
    xya = []
    for _ in range(n):
        xya.append(list(map(int, input().split())))
    return w, h, xya

def main(w, h, xya):
    xmin = 0
    xmax = w
    ymin = 0
    ymax = h
    for x, y, a in xya:
        if a == 1:
            xmin = max(xmin, x)
        elif a == 2:
            xmax = min(xmax, x)
        elif a == 3:
            ymin = max(ymin, y)
        elif a == 4:
            ymax = min(ymax, y)
    if xmax < xmin or ymax < ymin:
        return 0
    else:
        return (xmax - xmin) * (ymax - ymin)

def printans(ans):
    print(ans)

if __name__ == '__main__':
    w, h, xya = readinput()
    ans = main(w, h, xya)
    printans(ans)
