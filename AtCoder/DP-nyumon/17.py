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
    n,a=m_input()
    x=l_input()
    return n,a,x

def solve(n,a,x):
    # dp[i][j][k]: i枚目までにj枚選んだときの合計値がkとなる通り数
    dp = [[[0 for _ in range(50*n+1)] for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        xi = x[i-1]
        for j in range(i+1):
            for k in range(50*n+1):
                dp[i][j][k] += dp[i-1][j][k]  # i枚目を選ばないとき
                if j-1 >= 0 and k-xi >= 0:
                    dp[i][j][k] += dp[i-1][j-1][k-xi]   # i枚目を選んだとき
    ans = 0
    for j in range(1, n+1):
        ans += dp[n][j][j*a]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,x=readinput()
    ans=solve(n,a,x)
    printans(ans)
