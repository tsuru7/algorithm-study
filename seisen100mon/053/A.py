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
    a = [i_input() for _ in range(n)]
    return n,a

def solve(n,a):
    dp = [INFTY for _ in range(n)]
    ans=0
    for i in range(n):
        ai = a[i]
        idx = bisect_left(dp, ai)
        if idx < n:
            dp[idx] = ai
            ans = max(ans, idx)
    return ans+1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
