def readinput():
    n,a,b=map(int,input().split())
    return n,a,b

def myexpmod(x, n, MOD):
    ans = 1
    xn = x
    while n > 0:
        if n % 2 == 1:
            ans = (ans * xn) % MOD
        xn = (xn * xn) % MOD
        n = n >> 1
    return ans

from math import floor
def exEuclid(a, b):
    ''' 拡張ユークリッドアルゴリズム

        (d, x, y): d=gcd(a,b) = ax+by を満たすd, x, yを求める
        aとbが互いに素な整数であればd = gcd(a,b)=1であるので, ax+by=1となり
        xは法bの元で ax = 1であるので、aの乗法逆元a^-1になる
    '''
    if (b==0):
        return (a, 1, 0)
    else:
        (dd, xx, yy) = exEuclid(b, a % b)
        d = dd
        x = yy
        y = xx - int(floor(a/b))*yy
        return (d, x, y)

def com(n, a, MOD):
    ans = 1
    a = min(a, n-a)
    for i in range(1, a+1):
        ans = (ans*n)%MOD
        (d, x, y) = exEuclid(a, MOD)
        ans = (ans*x)%MOD
        n -= 1
        a -= 1
    return ans

def main(n,a,b):
    MOD = 10**9+7
    ans = (myexpmod(2, n, MOD) - 1)%MOD
    ans = (ans - com(n, a, MOD))%MOD
    ans = (ans - com(n, b, MOD))%MOD
    return ans

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    print(ans)

