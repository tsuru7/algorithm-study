import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    t=i_input()
    n=i_input()
    staff = [l_input() for _ in range(n)]
    return t,n,staff

def solve(t,n,staff):
    working = [0 for _ in range(t+1)]
    for l, r in staff:
        working[l] += 1
        working[r] -= 1
    ans = list(accumulate(working))[:t]
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    t,n,staff=readinput()
    ans=solve(t,n,staff)
    printans(ans)
