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
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(k):
        for j in range(n):
            for l in range(1, m+1):
                jj = j + l
                if jj > n:
                    jj = n - (jj-n)
                dp[i+1][jj] += dp[i][j]

    minv = pow(m, MOD-2, MOD)
    divisor = minv
    ans = 0
    for i in range(1, k+1):
        ans += dp[i][n] * divisor
        ans %= MOD
        divisor *= minv
        divisor %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k=readinput()
    ans=solve(n,m,k)
    printans(ans)
