import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import sqrt

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
    xylist = [ l_input() for _ in range(n) ]
    return n,xylist

def solve(n,xylist):
    ans=0
    for i in range(n):
        xi, yi = xylist[i]
        for j in range(i+1, n):
            xj, yj = xylist[j]
            ans = max(ans, (xi-xj)**2 + (yi-yj)**2)
    return sqrt(ans)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xylist=readinput()
    ans=solve(n,xylist)
    printans(ans)
