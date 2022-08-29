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
    s = input()
    return n,s

def solve(n,s):
    MOD = 10**9+7
    t = 'atcoder'
    m = len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    # for j in range(m+1):
    #     dp[0][j] = 1
    for i in range(1, n+1):
        si = s[i-1]
        for j in range(1, m+1):
            tj = t[j-1]
            dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD
            if tj == si:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] %= MOD
    return dp[n][m]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
