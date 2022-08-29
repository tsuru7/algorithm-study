import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right
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
    a=l_input()
    b=l_input()
    c=l_input()
    return n,a,b,c

def XonY(a, b):
    n = len(a)
    AonB = [0]*n
    for ib in range(n):
        ia = bisect_left(a, b[ib])
        AonB[ib] = ia
    return AonB

def XunderY(x, y):
    n = len(x)
    XunderY = [0]*n
    for iy in range(n):
        ix = bisect_right(x, y[iy])
        XunderY[iy] = n - ix
    return XunderY

def main(n,a,b,c):
    a.sort()
    b.sort()
    c.sort()

    AonB = XonY(a, b)
    CunderB = XunderY(c, b)

    ans = 0
    for ib in range(n):
        ans += AonB[ib] * CunderB[ib]

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=main(n,a,b,c)
    printans(ans)
