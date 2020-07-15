import sys
INFTY=sys.maxsize

def readinput():
    n=int(input())
    return n

def main(n):
    dp=[INFTY]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=min(dp[i],dp[i-1]+1)  # 1円
        k=1
        while(i-6**k>=0):
            dp[i]=min(dp[i],dp[i-6**k]+1)
            k+=1
        k=1
        while(i-9**k>=0):
            dp[i]=min(dp[i],dp[i-9**k]+1)
            k+=1
    return dp[n]

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
