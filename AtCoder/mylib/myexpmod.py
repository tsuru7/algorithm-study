def myexpmod(x, n, MOD):
    ans = 1
    xn = x
    while n > 0:
        if n % 2 == 1:
            ans = (ans * xn) % MOD
        xn = (xn * xn) % MOD
        n = n >> 1
    return ans

if __name__=='__main__':
    x,n=list(map(int,input().split()))
    print(myexpmod(x,n,10**9+7))
