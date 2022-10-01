import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(float, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n=i_input()
    p=l_input()
    return n,p

def solve(n,p):
    dp = [[0.0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1.0
    for i in range(1, n+1):
        pi = p[i-1]
        for j in range(i+1):
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]*pi
            dp[i][j] += dp[i-1][j]*(1-pi)

    # print(sum(dp[n]))
    # print(*dp, sep='\n')

    ans=sum(dp[n][n//2+1:])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
