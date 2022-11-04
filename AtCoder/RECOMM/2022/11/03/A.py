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
    n,a,b=m_input()
    x=l_input()
    return n,a,b,x

def solve(n,a,b,x):
    dp = [0 for _ in range(n)]
    for i in range(1, n):
        dist = x[i] - x[i-1]
        dp[i] = dp[i-1] + min(dist*a, b)
    return dp[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,x=readinput()
    ans=solve(n,a,b,x)
    printans(ans)
