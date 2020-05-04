# 拡張ユークリッドアルゴリズム
# (d, x, y): d=ax+by を満たすd, x, yを求める
# aとbが互いに素な整数であればgcd(a,b)=d=1, ax=1 (mod b)
# xは法bの元でaの乗法逆元a^-1になる
def exEuclid(a, b):
    if (b==0):
        return (a, 1, 0)
    else:
        (dd, xx, yy) = exEuclid(b, a % b)
        return (dd, yy, xx - (a//b)*yy)

def mycomb(n, k, p):
    k = min(n-k,k)
    fact=1
    finv=1
    for i in range(k):
        fact=fact*(n-i) % p
        finv=finv*(i+1) % p
    (d, x, y) = exEuclid(finv, p)
    return fact*x % p

x, y = list(map(int,input().split()))

if ((x+y)%3 != 0):
    print(0)
    exit()
else:
    n1 = (-x+2*y)//3
    n2 = (2*x -y)//3
    if( (n1<0) or (n2<0) ):
        print(0)
        exit()
    npath = mycomb(n1+n2, n2, 10**9+7)
    print(npath)

