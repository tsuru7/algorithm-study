import sys
sys.setrecursionlimit(10**6)
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
    p=l_input()
    return n,p


def next_(p):
    if len(p) == 1:
        return None
    tmp = next_(p[1:])
    if tmp is None:
        p0 = p[0]
        q = sorted(p)
        idx = bisect_left(q, p0)
        if idx == len(q):
            return None
        p0new = q[idx]
        return [p0new] + q[:idx] + q[idx+1:]
    else:
        return [p[0]] + tmp

def solve(n,p):
    q = p[::-1]
    r = next_(q)
    ans=r[::-1]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
