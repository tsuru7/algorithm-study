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
    cards = [i_input() for _ in range(n)]
    return n,cards

def solve(n,cards):
    dp = [INFTY for _ in range(n)]
    maxlen = 0
    for i in range(n):
        ci = cards[i]
        idx = bisect_left(dp, ci)
        if idx < n:
            dp[idx] = ci
            maxlen = max(maxlen, idx)
    return n - (maxlen+1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,cards=readinput()
    ans=solve(n,cards)
    printans(ans)
