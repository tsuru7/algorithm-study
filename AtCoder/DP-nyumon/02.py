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
    dp = [INFTY for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(dp[i], dp[i-1]+abs(a[i]-a[i-1]))
        if i+1 < n:
            dp[i+1] = min(dp[i+1], dp[i-1]+abs(a[i+1]-a[i-1]))
    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
