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
    a,b=m_input()
    return a,b

def solve(a,b):
    if 2*b - a >= 0:
        return a
    ac = 0
    wa = 10**13
    while wa - ac > 1:
        wj = (ac + wa) // 2
        if b <= a / (2.0 * sqrt((wj+1)**3)):
            ac = wj
        else:
            wa = wj
    ans = min(a/sqrt(ac+1) + ac*b, a/sqrt(wa+1) + wa*b)
    return ans

def printans(ans):
    print('{:.10f}'.format(ans))

if __name__=='__main__':
    a,b=readinput()
    ans=solve(a,b)
    printans(ans)
