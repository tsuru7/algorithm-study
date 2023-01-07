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
    xyList = [l_input() for _ in range(n)]
    return n,xyList

def solve(n,xyList):
    dp = [INFTY for _ in range(n)]
    xyList.sort(key=lambda x: (x[0], -x[1]))
    ans = 0
    for i in range(n):
        yi = xyList[i][1]
        idx = bisect_left(dp, yi)
        dp[idx] = yi
        ans = max(ans, idx+1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xyList=readinput()
    ans=solve(n,xyList)
    printans(ans)
