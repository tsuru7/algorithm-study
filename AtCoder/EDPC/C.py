def readinput():
    n=int(input())
    a=[]
    b=[]
    c=[]
    for _ in range(n):
        aa,bb,cc=list(map(int,input().split()))
        a.append(aa)
        b.append(bb)
        c.append(cc)
    return n,a,b,c

def main(n,a,b,c):
    dp=[]
    dp.append([0]*n)
    dp.append([0]*n)
    dp.append([0]*n)

    dp[0][0]=a[0]
    dp[1][0]=b[0]
    dp[2][0]=c[0]

    for i in range(1,n):
        dp[0][i]=max(dp[0][i],dp[1][i-1]+a[i])
        dp[0][i]=max(dp[0][i],dp[2][i-1]+a[i])
        dp[1][i]=max(dp[1][i],dp[2][i-1]+b[i])
        dp[1][i]=max(dp[1][i],dp[0][i-1]+b[i])
        dp[2][i]=max(dp[2][i],dp[0][i-1]+c[i])
        dp[2][i]=max(dp[2][i],dp[1][i-1]+c[i])
    ans=max(dp[0][n-1], dp[1][n-1])
    ans=max(ans,dp[2][n-1])
    return ans

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=main(n,a,b,c)
    print(ans)
