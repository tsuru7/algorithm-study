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
    return n

def solve(n):
    MOD = 998244353
    dp = [ [0]*9 for _ in range(n) ]
    dp[0] = [1]*9
    for i in range(1, n):
        for j in range(9):
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]
            if j+1 <= 8:
                dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD
            
    ans=sum(dp[n-1]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
