import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    n, w = m_input()
    vwlist = [ l_input() for _ in range(n) ]
    return n,w,vwlist

def solve(n,w,vwlist):
    dp = [ [-INFTY]*(w+1) for _ in range(n+1) ]
    dp[0][0] = 0
    for i in range(1, n+1):
        vi, wi = vwlist[i-1]
        for j in range(w+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j])
            if j-wi >= 0:
                dp[i][j] = max(dp[i][j], dp[i][j-wi]+vi)
    return max(dp[n])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,w,vwlist=readinput()
    ans=solve(n,w,vwlist)
    printans(ans)
