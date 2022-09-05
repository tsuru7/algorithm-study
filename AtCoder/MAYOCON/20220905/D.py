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
    txaList = [l_input() for _ in range(n)]
    return n,txaList

def solve(n,txaList):
    tn = txaList[-1][0]
    txa = [[0, 0] for _ in range(tn+1)]
    for t, x, a in txaList:
        txa[t][0] = x
        txa[t][1] = a
    dp = [[-INFTY for _ in range(5)] for _ in range(tn+1)]
    dp[0][0] = 0
    for t in range(tn):
        x, a = txa[t+1]
        for j in range(5):
            if j == x:
                if j-1 >= 0:
                    dp[t+1][j] = max(dp[t+1][j], dp[t][j-1]+a)
                dp[t+1][j] = max(dp[t+1][j], dp[t][j]+a)
                if j+1 < 5:
                    dp[t+1][j] = max(dp[t+1][j], dp[t][j+1]+a)
            else:
                if j-1 >= 0:
                    dp[t+1][j] = max(dp[t+1][j], dp[t][j-1])
                dp[t+1][j] = max(dp[t+1][j], dp[t][j])
                if j+1 < 5:
                    dp[t+1][j] = max(dp[t+1][j], dp[t][j+1])

    return max(dp[tn])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,txaList=readinput()
    ans=solve(n,txaList)
    printans(ans)
