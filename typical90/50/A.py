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
    n,l=m_input()
    return n,l

def solve(n,l):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    MOD = 10**9+7
    for i in range(n):
        dp[i+1] += dp[i]
        dp[i+1] %= MOD
        if i+l <= n:
            dp[i+l] += dp[i]
            dp[i+l] %= MOD
    return dp[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l=readinput()
    ans=solve(n,l)
    printans(ans)
