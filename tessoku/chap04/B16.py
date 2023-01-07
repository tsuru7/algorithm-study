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
    dp = [INFTY for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(dp[i], dp[i-1] + abs(h[i]-h[i-1]))
        if i-2 >= 0:
            dp[i] = min(dp[i], dp[i-2] + abs(h[i]-h[i-2]))
    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h=readinput()
    ans=solve(n,h)
    printans(ans)
