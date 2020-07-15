import sys
INFTY=sys.maxsize

def readinput():
    n,k=list(map(int,input().split()))
    h=list(map(int,input().split()))
    return n,k,h

def main(n,k,h):
    dp=[INFTY]*n
    dp[0]=0
    for i in range(n):
        for j in range(1,k+1):
            if i+j<n:
                dp[i+j]=min(dp[i+j],dp[i]+abs(h[i]-h[i+j]))
    return dp[n-1]

if __name__=='__main__':
    n,k,h=readinput()
    ans=main(n,k,h)
    print(ans)
