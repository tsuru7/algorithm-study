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
    n,l,r=m_input()
    x=l_input()
    return n,l,r,x

def solve(n,l,r,x):
    now = 0
    idx_l = bisect_left(x, now+l) + 1
    idx_r = bisect_right(x, now+r) - 1
    now = x[idx_r]
    count += 1
    while idx_r < n-1:


    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l,r,x=readinput()
    ans=solve(n,l,r,x)
    printans(ans)