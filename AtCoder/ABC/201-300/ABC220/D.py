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

def main(n,a):
    MOD = 998244353
    dp = []
    for i in range(n):
        dp.append([0] * 10)
    dp[0][a[0]] = 1
    for i in range(1, n):
        for j in range(10):
            k = (a[i] + j) % 10
            dp[i][k] += dp[i-1][j]
            dp[i][k] = dp[i][k] % MOD
            k = (a[i]*j) % 10
            dp[i][k] += dp[i-1][j]
            dp[i][k] = dp[i][k] % MOD
    ans=[dp[n-1][j] for j in range(10)]
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
