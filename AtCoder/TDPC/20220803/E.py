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
    d=i_input()
    n = input()
    return d,n

def solve(d,n):
    MOD = 10**9+7
    s = n
    l = len(s)
    dp = [[[0 for _ in range(d)] for _ in range(2)] for _ in range(l+1)]
    dp[0][0][0] = 1

    for i in range(l):
        di = int(s[i])
        # smaller -> smaller
        for j in range(d):
            for num in range(10):
                dp[i+1][1][(j+num)%d] += dp[i][1][j]
                dp[i+1][1][(j+num)%d] %= MOD
        # equal -> smaller
        for j in range(d):
            for num in range(di):
                dp[i+1][1][(j+num)%d] += dp[i][0][j]
                dp[i+1][1][(j+num)%d] %= MOD
        # equal -> equal
        for j in range(d):
            dp[i+1][0][(j+di)%d] += dp[i][0][j]
            dp[i+1][0][(j+di)%d] %= MOD

    # print(dp)
    # print(dp[l][0][0], dp[l][1][0])

    return (dp[l][0][0] + dp[l][1][0] - 1) % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    d,n=readinput()
    ans=solve(d,n)
    printans(ans)
