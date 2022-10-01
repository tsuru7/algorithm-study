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
    MOD = 10**9+7
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] += dp[i-1]
        if i-l >= 0:
            dp[i] += dp[i-l]
        dp[i] %= MOD
    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l=readinput()
    ans=solve(n,l)
    printans(ans)
