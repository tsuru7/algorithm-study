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
    a=l_input()
    b=l_input()
    return n,k,a,b

def solve(n,k,a,b):
    dp = [ [False, False] for _ in range(n) ]
    dp[0][0] = True
    dp[0][1] = True
    for i in range(1, n):
        if dp[i-1][0]:
            if abs(a[i-1]-a[i]) <= k:
                dp[i][0] = True
            if abs(a[i-1]-b[i]) <= k:
                dp[i][1] = True
        if dp[i-1][1]:
            if abs(b[i-1]-a[i]) <= k:
                dp[i][0] = True
            if abs(b[i-1]-b[i]) <= k:
                dp[i][1] = True
    if dp[n-1][0] or dp[n-1][1]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,b=readinput()
    ans=solve(n,k,a,b)
    printans(ans)
