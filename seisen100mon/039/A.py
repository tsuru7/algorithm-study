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
    a=l_input()
    return n,a

def solve(n,a):
    dp = [ [0]*21 for _ in range(n-1) ]
    dp[0][a[0]] = 1
    for i in range(1, n-1):
        ai = a[i]
        for j in range(21):
            if j-ai >= 0:
                dp[i][j] += dp[i-1][j-ai]
            if j+ai <= 20:
                dp[i][j] += dp[i-1][j+ai]
    return dp[n-2][a[n-1]]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
