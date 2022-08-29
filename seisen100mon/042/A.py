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
    dlist = [i_input() for _ in range(n)]
    clist = [i_input() for _ in range(m)]
    return n,m,dlist,clist

def solve(n,m,dlist,clist):
    dp = [ [INFTY]*(n+1) for _ in range(m+1) ]
    for i in range(m+1):
        dp[i][0] = 0
    for i in range(1, m+1):
        ci = clist[i-1]
        for j in range(1, n+1):
            dj = dlist[j-1]
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            dp[i][j] = min(dp[i][j], dp[i-1][j-1]+ci*dj)
    return dp[m][n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,dlist,clist=readinput()
    ans=solve(n,m,dlist,clist)
    printans(ans)
