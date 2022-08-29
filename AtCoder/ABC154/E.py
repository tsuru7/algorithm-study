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
    n = input()
    k = i_input()
    return n,k

def solve(n,k):
    d = list(n)
    l = len(n)
    dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(l+1)]
    equal = 0
    small = 1
    dp[0][equal][0] = 1
    for i in range(1, l+1):
        di = int(d[i-1])
        for j in range(k+1):
            # equal -> equal
            if di == 0:
                # di = 0
                if j > 0:
                    dp[i][equal][j] += dp[i-1][equal][j]
            else:
                # di > 0
                if j+1 <= k:
                    dp[i][equal][j+1] += dp[i-1][equal][j]
            # equal -> small
            if di == 0:
                # di = 0のケースはない
                pass
            else:
                # di > 0, 0 < ei < di
                if j+1 <= k:
                    dp[i][small][j+1] += dp[i-1][equal][j]*(di-1)
                # di > 0, ei = 0
                # if j > 0:
                dp[i][small][j] += dp[i-1][equal][j]
            # small -> small
            if j+1 <= k:
                dp[i][small][j+1] += dp[i-1][small][j]*9
            # if j > 0:
            dp[i][small][j] += dp[i-1][small][j]

    # print(f'dp: {dp}')

    return dp[l][equal][k] + dp[l][small][k]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
