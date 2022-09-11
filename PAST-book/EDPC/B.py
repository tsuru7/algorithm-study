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
    dp = [INFTY]*n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k+1):
            if i-j >= 0:
                dp[i] = min(dp[i], dp[i-j]+abs(h[i]-h[i-j]))
    ans=dp[n-1]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,h=readinput()
    ans=solve(n,k,h)
    printans(ans)
