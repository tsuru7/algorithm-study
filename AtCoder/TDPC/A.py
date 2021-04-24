def readinput():
    n=int(input())
    p=list(map(int,input().split()))
    return n,p

def main(n,p):
    manten=0
    for pp in p:
        manten+=pp

    dp=[]
    for i in range(n+1):
        dp.append([0]*(manten+1))

    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(manten+1):
            # i問めを解かない
            dp[i][j]=max(dp[i][j],dp[i-1][j])
            # 解く
            if j-p[i-1]>=0:
                dp[i][j]=max(dp[i-1][j-p[i-1]],dp[i][j])
    ans=0
    for j in range(manten+1):
        ans+=dp[n][j]
    return ans

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    print(ans)
