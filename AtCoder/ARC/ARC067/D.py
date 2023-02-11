import sys
INFTY = sys.maxsize

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,a,b=m_input()
    x=l_input()
    return n,a,b,x

def main(n,a,b,x):
    dp = [INFTY]*(n+1)
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(dp[i], dp[i-1]+b)
        dp[i] = min(dp[i], dp[i-1]+(x[i]-x[i-1])*a)
        # print(dp)
    return dp[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,x=readinput()
    ans=main(n,a,b,x)
    printans(ans)
