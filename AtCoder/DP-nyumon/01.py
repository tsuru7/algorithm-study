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
    h=l_input()
    return n,h

def solve(n,h):
    dp = [INFTY for _ in range(n+1)]
    dp[1] = 0
    for i in range(1, n+1):
        if i+1 <= n:
            dp[i+1] = min(dp[i+1], dp[i] + abs(h[i-1]-h[i]))
        if i+2 <= n:
            dp[i+2] = min(dp[i+2], dp[i] + abs(h[i-1]-h[i+1]))
    return dp[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h=readinput()
    ans=solve(n,h)
    printans(ans)
