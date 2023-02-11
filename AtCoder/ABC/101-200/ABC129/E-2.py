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
    l = input()
    return l

def solve(l):
    MOD = 10**9+7
    ll = len(l)
    dp = [[0 for _ in range(2)] for _ in range(ll+1)]
    dp[0][0] = 1

    for i in range(ll):
        li = int(l[i])
        # smaller -> smaller
        dp[i+1][1] += dp[i][1]*3
        dp[i+1][1] %= MOD
        # equal -> smaller
        if li == 1:
            dp[i+1][1] += dp[i][0]
            dp[i+1][1] %= MOD
        # equal -> equal
        if li == 1:
            dp[i+1][0] += dp[i][0]*2
        else:
            dp[i+1][0] += dp[i][0]
        dp[i+1][0] %= MOD

    return (dp[ll][0] + dp[ll][1]) % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    l=readinput()
    ans=solve(l)
    printans(ans)
