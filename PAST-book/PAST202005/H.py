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
    n,l=m_input()
    x=l_input()
    t1, t2, t3 = m_input()
    return n,l,x,t1,t2,t3

def solve(n,l,x,t1,t2,t3):
    dp = [INFTY]*(l+1)
    dp[0] = 0
    j = 0
    for i in range(1, l+1):
        dp[i] = min(dp[i], dp[i-1] + t1)
        if i-2 >= 0:
            dp[i] = min(dp[i], dp[i-2] + t1 + t2)
        if i-4 >= 0:
            dp[i] = min(dp[i], dp[i-4] + t1 + t2*3)
        if j < n and i == x[j]:
            dp[i] += t3
            j += 1
    dp[l] = min(dp[l], dp[l-1]+t1//2+t2//2)
    dp[l] = min(dp[l], dp[l-2]+t1//2+t2//2*3)
    dp[l] = min(dp[l], dp[l-3]+t1//2+t2//2*5)
    return dp[l]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l,x,t1,t2,t3=readinput()
    ans=solve(n,l,x,t1,t2,t3)
    printans(ans)
