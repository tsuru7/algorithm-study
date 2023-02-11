def readinput():
    n,k=map(int,input().split())
    lr=[]
    for _ in range(k):
        l,r=map(int,input().split())
        lr.append((l,r))
    return n,k,lr

def main(n,k,lr):
    lrs=sorted(lr,key=lambda x:x[0])
    MOD=998244353
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(1,n):
        #print(i)
        if dp[i]==0:
            continue
        skip=False
        for l,r in lrs:
            for j in range(l,r+1):
                #print('i+j: {}'.format(i+j))
                if i+j>n:
                    skip=True
                    break
                dp[i+j]=(dp[i+j]+dp[i])%MOD
                #print(dp)
            if skip:
                break
    return dp[n]

def main2(n,k,lr):
    lrs=sorted(lr,key=lambda x:x[0])
    MOD=998244353
    dp=[0]*(n+1)
    ruiseki=[0]*(n+1)
    dp[1]=1
    ruiseki[1]=1
    for i in range(2,n+1):
        for l,r in lrs:
            if i-l<1:
                break
            dp[i]+=ruiseki[i-l]-ruiseki[max(1,i-r)-1]
        dp[i]=dp[i]%MOD
        ruiseki[i]=(ruiseki[i-1]+dp[i])%MOD
    return dp[n]

if __name__=='__main__':
    n,k,lr=readinput()
    ans=main2(n,k,lr)
    print(ans)
