import sys
INFTY = sys.maxsize

def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def main(n, a):
    mincost=INFTY
    for x in range(-100, 101):
        cost = 0
        for i in range(n):
            cost += (a[i] - x)**2
        mincost = min(mincost, cost)
    return mincost

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a = readinput()
    ans = main(n, a)
    printans(ans)
