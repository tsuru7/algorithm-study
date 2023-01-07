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
    n,w=m_input()
    wvList = [l_input() for _ in range(n)]
    return n,w,wvList

def solve(n,w,wvList):
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        wi, vi = wvList[i]
        for j in range(w+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j-wi >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-wi]+vi)
    ans=max(dp[n])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,w,wvList=readinput()
    ans=solve(n,w,wvList)
    printans(ans)
