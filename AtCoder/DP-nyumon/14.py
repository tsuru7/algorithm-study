import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict
from math import gcd


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
    n,ma,mb=m_input()
    abcList = [l_input() for _ in range(n)]
    return n,ma,mb,abcList

def solve(n,ma,mb,abcList):
    dp = [[[INFTY for _ in range(401)] for _ in range(401)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        ai, bi, ci = abcList[i]
        for bj in range(401):
            for aj in range(401):
                dp[i+1][bj][aj] = min(dp[i+1][bj][aj], dp[i][bj][aj])
                if bj-bi >= 0 and aj-ai >= 0:
                    dp[i+1][bj][aj] = min(dp[i+1][bj][aj], dp[i][bj-bi][aj-ai]+ci)
    
    ans=INFTY
    i = 1
    while ma*i <= 400 and mb*i <= 400:
        ans = min(ans, dp[n][mb*i][ma*i])
        i += 1
    if ans == INFTY:
        return -1
    else:
        return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ma,mb,abcList=readinput()
    ans=solve(n,ma,mb,abcList)
    printans(ans)
