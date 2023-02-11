def readinput():
    n=int(input())
    d=list(map(int,input().split()))
    return n,d

def power(x,n,MOD):
    res=1
    if n>0:
        res=power(x,n//2,MOD)
        if (n%2==0):
            res=(res*res)%MOD
        else:
            res=(((res*res)%MOD)*x)%MOD
    #print(x,n,MOD,res)
    return res

def main(n,d):
    MOD=998244353
    hist=[0]*(n+1)
    maxd=0
    for i in range(n):
        hist[d[i]]+=1
        maxd=max(maxd,d[i])
    #print(hist,maxd)

    ans=1
    if hist[0]>1:
        return 0
    if d[0]!=0:
        return 0
    for i in range(1,maxd+1):
        #print(i, hist[i-1], hist[i])
        ans=(ans*power(hist[i-1], hist[i], MOD))%MOD
        #print(ans)

    return ans

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    print(ans)
