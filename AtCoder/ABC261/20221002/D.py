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
    x=l_input()
    cyList = [l_input() for _ in range(m)]
    return n,m,x,cyList

def solve(n,m,x,cyList):
    bonus = [0 for _ in range(n+1)]
    for c, y in cyList:
        bonus[c] = y
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        xi = x[i-1]
        for j in range(i+1):
            if j-1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + xi + bonus[j])
            dp[i][0] = max(dp[i][0], dp[i-1][j])

    return max(dp[n])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,x,cyList=readinput()
    ans=solve(n,m,x,cyList)
    printans(ans)
