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
    n,k=m_input()
    ablist = [ l_input() for _ in range(k) ]
    return n,k,ablist

def solve(n,k,ablist):
    MOD = 10000
    dp = [ [ [0]*2 for j in range(3) ] for i in range(n) ]
    fixed = dict()
    for a, b in ablist:
        fixed[a-1] = b-1

    if 0 not in fixed:
        for j in range(3):
            dp[0][j][0] = 1
    else:
        dp[0][fixed[0]][0] = 1

    for i in range(n):
        if i in fixed:
            j = fixed[i]
            # dp[i][j][0]
            for jj in range(3):
                if jj == j:
                    continue
                dp[i][j][0] += dp[i-1][jj][0]
                dp[i][j][0] += dp[i-1][jj][1]
            dp[i][j][0] %= MOD
            # dp[i][j][1]
            dp[i][j][1] = dp[i-1][j][0]
        else:
            for j in range(3):
                for jj in range(3):
                    if jj == j:
                        dp[i][j][1] = dp[i-1][j][0]
                    else:
                        dp[i][j][0] += dp[i-1][jj][0]
                        dp[i][j][0] += dp[i-1][jj][1]
                dp[i][j][0] %= MOD
    ans = 0
    for j in range(3):
        ans += dp[n-1][j][0]
        ans += dp[n-1][j][1]
    ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,ablist=readinput()
    ans=solve(n,k,ablist)
    printans(ans)
