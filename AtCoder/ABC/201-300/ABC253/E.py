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
    dp = [ [0]*(m+1) for _ in range(n) ]
    for j in range(1, m+1):
        dp[0][j] = j
    for i in range(1, n):
        for j in range(1, m+1):
            dp[i][j] = dp[i][j-1]
            if k > 0:
                klo = max(0, j-k)
                dp[i][j] += dp[i-1][klo]
                khi = min(m+1, k+j)
                dp[i][j] += dp[i-1][m] - dp[i-1][khi-1]
            else:
                dp[i][j] += dp[i-1][m]
            dp[i][j] %= MOD
    ans=dp[n-1][m]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k=readinput()
    ans=solve(n,m,k)
    printans(ans)
