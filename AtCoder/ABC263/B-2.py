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
    p=l_input()
    return n,p

def solve(n,p):
    p = [0, 0] + p
    dp = [0 for _ in range(n+1)] # dp[i] : i番目の人は1の何世代後か
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = dp[p[i]]+1

    return dp[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
