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
    for i in range(1, n+1):
        wi, vi = wvList[i-1]
        for j in range(w+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j-wi >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-wi]+vi)
    return max(dp[n])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,w,wvList=readinput()
    ans=solve(n,w,wvList)
    printans(ans)
