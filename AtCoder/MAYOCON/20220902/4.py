import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    b=l_input()
    return n,a,b

def main(n,a,b):
    MOD = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(n+1)]
    for j in range(a[0], b[0]+1):
        dp[1][j] = 1
    for i in range(1, n):
        cum = [0] + list(accumulate(dp[i]))
        for j in range(a[i], b[i]+1):
            dp[i+1][j] = cum[min(j, b[i-1])+1] - cum[a[i-1]]
            dp[i+1][j] %= MOD

    ans=sum(dp[n]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    printans(ans)
