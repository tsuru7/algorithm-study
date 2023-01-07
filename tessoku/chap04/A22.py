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
    b=l_input()
    return n,a,b

def solve(n,a,b):
    dp = [-INFTY for _ in range(n)]
    dp[0] = 0
    for i in range(n-1):
        if dp[i] < 0:
            continue
        ai = a[i]-1
        bi = b[i]-1
        dp[ai] = max(dp[ai], dp[i] + 100)
        dp[bi] = max(dp[bi], dp[i] + 150)
    return dp[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=solve(n,a,b)
    printans(ans)
