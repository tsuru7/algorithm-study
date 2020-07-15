def power(x,n,MOD):
    res=1
    if n>0:
        res=power(x,n//2,MOD)
        if (n%2==0):
            res=(res*res)%MOD
        else:
            res=(((res*res)%MOD)*x)%MOD
    return res

if __name__=='__main__':
    x,n=list(map(int,input().split()))
    print(power(x,n,10**9+7))
