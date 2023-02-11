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

def main(n,x,y,abList):
    dp = [[[INFTY for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        ai, bi = abList[i]
        for j in range(x+1):
            for k in range(y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k]) # i番目の弁当を買わないとき
                dp[i+1][min(x, j+ai)][min(y, k+bi)] = min(dp[i+1][min(x, j+ai)][min(y, k+bi)], dp[i][j][k] + 1) # i番目を買うとき
    if dp[n][x][y] >= INFTY:
        return -1
    else:
        return dp[n][x][y]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,abList=readinput()
    ans=main(n,x,y,abList)
    printans(ans)
