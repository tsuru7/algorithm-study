import sys
INFTY=sys.maxsize

def readinput():
    n,m=list(map(int,input().split()))
    a=[]
    for _ in range(m):
        a.append(int(input()))
    return n,m,a

def main(n,m,a):
    MOD=10**9+7
    dp=[0]*(n+3)
    dp[0]=1
    ia=0
    for i in range(n+1):
        if ia<m and i==a[ia]:
            ia+=1
            #print(ia)
            continue
        dp[i+1]=(dp[i+1]+dp[i])%MOD
        dp[i+2]=(dp[i+2]+dp[i])%MOD
        #print(dp)
    return dp[n]

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)

