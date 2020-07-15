def readinput():
    n,w=list(map(int,input().split()))
    wlist=[]
    vlist=[]
    for _ in range(n):
        ww,vv=list(map(int,input().split()))
        wlist.append(ww)
        vlist.append(vv)
    return n,w,wlist,vlist

def main(n,W,w,v):
    dp=[]
    for _ in range(n+1):
        dp.append([0]*(W+1))
    for i in range(1,n+1):
        for j in range(W+1):
            if j-w[i-1]>=0:
                dp[i][j]=max(dp[i-1][j-w[i-1]]+v[i-1], dp[i][j])
            dp[i][j]=max(dp[i-1][j], dp[i][j])
    return dp[n][W]

if __name__=='__main__':
    n,w,wlist,vlist=readinput()
    ans=main(n,w,wlist,vlist)
    print(ans)
