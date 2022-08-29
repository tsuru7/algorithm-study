import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n=i_input()
    xyList = [l_input() for _ in range(n)]
    return n,xyList

def solve(n,xyList):
    x = [xyList[i][0] for i in range(n)]
    y = [xyList[i][1] for i in range(n)]
    x.sort()
    y.sort()
    m = n//2
    mx = x[m]
    my = y[m]

    ans=0
    for i in range(n):
        ans += abs(x[i]-mx) + abs(y[i]-my)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xyList=readinput()
    ans=solve(n,xyList)
    printans(ans)
