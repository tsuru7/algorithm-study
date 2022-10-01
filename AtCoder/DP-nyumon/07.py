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
    n,m=m_input()
    a = [i_input() for _ in range(m)]
    return n,m,a

def solve(n,m,a):
    MOD = 10**9+7
    b = [False for _ in range(n+1)]
    for i in range(m):
        ai = a[i]
        b[ai] = True
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        if b[i]:
            continue
        dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
        dp[i] %= MOD
    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
