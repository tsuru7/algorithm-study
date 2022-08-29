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
    n,t=m_input()
    abList = [l_input() for _ in range(n)]
    return n,t,abList

def solve(n,t,abList):
    dp = [[[-INFTY for _ in range(t+1)] for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        ai, bi = abList[i]
        for j in range(t+1):
            dp[i+1][0][j] = max(dp[i+1][0][j], dp[i][0][j])
            dp[i+1][1][j] = max(dp[i+1][1][j], dp[i][1][j])
            if j-ai >= 0:
                dp[i+1][0][j] = max(dp[i+1][0][j], dp[i][0][j-ai]+bi)
                dp[i+1][1][j] = max(dp[i+1][1][j], dp[i][1][j-ai]+bi)
            if j-1 >= 0:
                dp[i+1][1][j] = max(dp[i+1][1][j], dp[i][0][j-1]+bi)

    ans = 0
    for j in range(t+1):
        for k in range(2):
            ans = max(ans, dp[n][k][j])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,t,abList=readinput()
    ans=solve(n,t,abList)
    printans(ans)
