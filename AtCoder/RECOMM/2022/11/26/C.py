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
    n,m,k=m_input()
    return n,m,k

def solve(n,m,k):
    MOD = 998244353

    if k == 0:
        return pow(m, n, MOD)

    dp = [[0 for _ in range(m+2)] for _ in range(n)]
    for j in range(1, m+1):
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(1, m+1):
            ll = max(j-k+1, 0)
            lh = min(j+k, m+1)
            dp[i][0] += dp[i-1][j]
            dp[i][ll] -= dp[i-1][j]
            dp[i][lh] += dp[i-1][j]
        for j in range(1, m+1):
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
    ans=sum(dp[n-1][1:m+1]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k=readinput()
    ans=solve(n,m,k)
    printans(ans)
