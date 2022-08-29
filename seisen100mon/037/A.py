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
    c=l_input()
    return n,m,c

def solve(n,m,c):
    dp = [ [INFTY]*(n+1) for _ in range(m+1) ]
    dp[0][0] = 0
    for i in range(1, m+1):
        ci = c[i-1]
        for j in range(n+1):
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j-ci >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j-ci]+1)
        # print(f'i: {i}, dp[i]: {dp[i]}')
    return dp[m][n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,c=readinput()
    ans=solve(n,m,c)
    printans(ans)
