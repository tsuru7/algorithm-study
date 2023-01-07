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
    n=i_input()
    paList = [l_input() for _ in range(n)]
    return n,paList

def solve(n,paList):
    dp = [[-INFTY for _ in range(n+1)] for _ in range(n+1)]
    dp[1][n] = 0
    for nb in range(n-1, 0, -1):
        for l in range(1, n-nb+1+1):
            r = l + nb - 1
            if l-1 >= 1:
                p, a = paList[l-1-1]
                score1 = a if l <= p <= r else 0
                dp[l][r] = max(dp[l][r], dp[l-1][r] + score1)
            if r+1 <= n:
                p, a = paList[r+1-1]
                score2 = a if l <= p <= r else 0
                dp[l][r] = max(dp[l][r], dp[l][r+1] + score2)
    ans=0
    for i in range(1, n+1):
        ans = max(ans, dp[i][i])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,paList=readinput()
    ans=solve(n,paList)
    printans(ans)
