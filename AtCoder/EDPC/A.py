import sys
INFTY=sys.maxsize

def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

def main(n,h):
    dp=[INFTY]*(n+3)
    dp[0]=0
    for i in range(1,n):
        dp[i]=min(dp[i],dp[i-1]+abs(h[i]-h[i-1]))
        if (i>=2):
            dp[i]=min(dp[i],dp[i-2]+abs(h[i]-h[i-2]))    
    
    return dp[n-1]

if __name__=='__main__':
    n,h=readinput()
    ans=main(n,h)
    print(ans)
