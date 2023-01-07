import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        dp[n][i+1] = a[i]
    for i in range(1, n)[::-1]:
        if i % 2 == 1:
            taro = True
        else:
            taro = False
        for j in range(1, i+1):
            if taro:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
            else:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])
    return dp[1][1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
