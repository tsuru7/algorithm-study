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


def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    a.sort()
    MOD = 998244353
    INV2 = exEuclid(2, MOD)[1]
    # print('exEuclid(2, MOD): ', end='')
    # print(exEuclid(2, MOD))
    # print(f'INV2: {INV2}')
    ans=0
    partial = 0
    for j in range(1, n):
        partial = (partial + a[j]*pow(2, j-1, MOD))%MOD
    # print(f'partial: {partial}')
    for i in range(n):
        ans = (ans + ((partial+a[i])%MOD * a[i])%MOD)%MOD
        # print(f'ans: {ans}')
        if i+1 < n:
            partial = ((partial - a[i+1])*INV2)%MOD
        else:
            partial = 0
        # print(f'partial: {partial}')
        

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
