# 法Pの下での組み合わせ数 nCk を求める
# MAX: nの最大値

MAX = (10**6)*2//3 +1  # (X+Y)/3より大きい整数 1 <= X, Y <= 10**6
P = (10**9)+7

fac=[1 for x in range(MAX)]
inv=[1 for x in range(MAX)]
finv=[1 for x in range(MAX)]

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

def COMinit():
    for i in range(2,MAX):
        fac[i] = fac[i-1]*i % P
        (d, x, y) = exEuclid(i, P)
        inv[i] = x
        finv[i] = (finv[i-1]*inv[i]) % P

def COM(n, k):
    if(n<k):
        return 0
    elif ( (n<0)or(k<0)):
        return 0
    else:
        return (fac[n]* (finv[n-k]*finv[k] % P)) % P

