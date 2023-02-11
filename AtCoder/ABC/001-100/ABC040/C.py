import sys
INFTY=sys.maxsize

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    dp=[INFTY]*(n+1)
    dp[1]=0
    for i in range(2,n+1):
        dp[i]=min(dp[i], dp[i-1]+abs(a[i-1]-a[i-2]))
        if i>=3:
            dp[i]=min(dp[i], dp[i-2]+abs(a[i-1]-a[i-3]))
        #print(dp)
    return dp[n]

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
