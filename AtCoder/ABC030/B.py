def readinput():
    n, m = map(int, input().split())
    return n, m

def main(n, m):
    if n > 12:
        n -= 12
    x = 30*n + m / 2
    y = 6*m
    z = abs(x - y)
    # print(x, y, z)
    if z > 180:
        z = 360 - z
    return z

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, m = readinput()
    ans = main(n, m)
    printans(ans)
