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
    w=i_input()
    n,k=m_input()
    abList = [l_input() for _ in range(n)]
    return w,n,k,abList

def solve(w,n,k,abList):
    dp = [[[0 for _ in range(w+1)] for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n):
        ai, bi = abList[i]
        for l in range(1, k+1):
            for j in range(w+1):
                dp[i+1][l][j] = max(dp[i+1][l][j], dp[i][l][j])
                if j-ai >= 0:
                    dp[i+1][l][j] = max(dp[i+1][l][j], dp[i][l-1][j-ai]+bi)
    ans = 0
    for l in range(1, k+1):
        for j in range(w+1):
            ans = max(ans, dp[-1][l][j])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    w,n,k,abList=readinput()
    ans=solve(w,n,k,abList)
    printans(ans)
