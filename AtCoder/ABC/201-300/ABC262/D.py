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
    a=l_input()
    return n,a

def solve(n,a):
    MOD = 998244353
    ans=0
    for i in range(1, n+1):
        dp = [[[0 for l in range(i)] for k in range(n+1)] for j in range(n+1)]
        dp[0][0][0] = 1
        for j in range(1, n+1):
            aj = a[j-1]
            for k in range(j+1):
                for l in range(i):
                    dp[j][k][l] += dp[j-1][k][l]
                    if k-1 >= 0:
                        dp[j][k][l] += dp[j-1][k-1][(l-aj) % i]
                    dp[j][k][l] %= MOD
        ans += dp[n][i][0]
        ans %= MOD

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
