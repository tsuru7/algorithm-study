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

if __name__ == '__main__':
    d, x, y = exEuclid(37, 39)
    print(d, x, y)