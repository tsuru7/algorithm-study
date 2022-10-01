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
    x,y=m_input()
    abList = [l_input() for _ in range(n)]
    return n,x,y,abList

def solve(n,x,y,abList):
    dp = [[[INFTY for _ in range(x+1)] for _ in range((y+1))] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        ai, bi = abList[i]
        for j in range(y+1):
            bj = min(y, j+bi)
            for k in range(x+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                ak = min(x, k+ai)
                dp[i+1][bj][ak] = min(dp[i+1][bj][ak], dp[i][j][k]+1)
    if dp[n][y][x] == INFTY:
        return -1
    else:
        return dp[n][y][x]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,abList=readinput()
    ans=solve(n,x,y,abList)
    printans(ans)
