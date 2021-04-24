def readinput():
    s=int(input())
    return s

def comb(n,k,p):
    """power_funcを用いて(nCk) mod p を求める"""
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=factorial(n) %p
    b=factorial(k) %p
    c=factorial(n-k) %p
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p

def power_func(a,b,p):
    """a^b mod p を求める"""
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p

def main(s):
    MOD=10**9+7
    n=s//3
    r=s%3
    ans=0
    while n>=1:
        hnr=comb(n+r-1,r,MOD)
        ans=(ans+hnr)%MOD
        n-=1
        r+=3
    return ans

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
