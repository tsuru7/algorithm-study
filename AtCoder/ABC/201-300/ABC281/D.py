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
    n,k,d=m_input()
    a=l_input()
    return n,k,d,a

def solve(n,k,d,a):
    dp = [[[-INFTY for _ in range(d)] for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        ai = a[i]
        for j in range(n+1):
            for l in range(d):
                dp[i+1][j][l] = max(dp[i+1][j][l], dp[i][j][l])
                if j+1 <= n:
                    dp[i+1][j+1][(l+ai)%d] = max(dp[i+1][j+1][(l+ai)%d], dp[i][j][l]+ai)
    # print(dp)
    return dp[n][k][0] if dp[n][k][0] >= 0 else -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,d,a=readinput()
    ans=solve(n,k,d,a)
    printans(ans)
