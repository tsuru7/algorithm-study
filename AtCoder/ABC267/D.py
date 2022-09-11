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
    a=l_input()
    return n,m,a

def solve(n,m,a):
    dp = [[-INFTY for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        ai = a[i]
        for j in range(m+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+1 <= m:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+ai*(j+1))
    
    return dp[n][m]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
