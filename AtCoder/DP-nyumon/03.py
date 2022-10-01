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
    n,k=m_input()
    h=l_input()
    return n,k,h

def solve(n,k,h):
    dp = [INFTY for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        for j in range(1, k+1):
            if i+j < n:
                dp[i+j] = min(dp[i+j], dp[i] + abs(h[i+j]-h[i]))
    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,h=readinput()
    ans=solve(n,k,h)
    printans(ans)
