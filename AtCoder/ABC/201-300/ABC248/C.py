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
    dp = [ [0]*(k+1) for _ in range(n+1) ]
    dp[0][0] = 1
    for i in range(n+1):
        for j in range(1, k+1):
            for l in range(1, m+1):
                if 0 <= j-l: 
                    dp[i][j] += dp[i-1][j-l]
            dp[i][j] %= MOD
    ans=sum(dp[n]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k=readinput()
    ans=solve(n,m,k)
    printans(ans)
