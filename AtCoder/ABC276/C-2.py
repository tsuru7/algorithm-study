import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left

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
    p=l_input()
    return n,p

def solve(n,p):
    ptmp = p[-2:]
    q = sorted(ptmp)
    if q != ptmp:
        return p[:-2] + q
    for i in range(3, n+1):
        ptmp = p[-i:]
        pre = p[-i]
        q = sorted(ptmp)
        idx = bisect_left(q, pre)
        if idx == 0:
            continue
        qtmp = q[:idx-1] + q[idx:]
        return p[:-i] + [q[idx-1]] + sorted(qtmp, reverse=True)


def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
