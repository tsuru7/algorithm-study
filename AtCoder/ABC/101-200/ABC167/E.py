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
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[1][0] = m
    for i in range(2, n+1):
        for j in range(min(i-1, k)+1):
            dp[i][j] += dp[i-1][j]*(m-1)
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD
    return sum(dp[n]) % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k=readinput()
    ans=solve(n,m,k)
    printans(ans)
