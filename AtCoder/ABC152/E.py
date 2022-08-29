import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import gcd

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def gcd_mod(x, y, MOD):
    if x < y:
        x, y = y, x
    while y > 0:
        # x = x // y
        inv = pow(y, MOD-2, MOD)
        x = x*inv % MOD
        y = x % y
    return y


def solve(n,a):
    if n == 1:
        return 1
    MOD = 10**9+7
    lcm = (a[0]*a[1]) % MOD
    inv = pow(gcd_mod(a[0], a[1], MOD), MOD-2, MOD)
    lcm = (lcm * inv) % MOD
    for i in range(2, n):
        inv = pow(gcd_mod(lcm, a[i], MOD), MOD-2, MOD)
        lcm = (lcm*a[i]*inv) % MOD

    # print(f'lcm: {lcm}')

    b = [0 for _ in range(n)]
    ans = 0
    for i in range(n):
        inv = pow(a[i], MOD-2, MOD)
        b[i] = lcm * inv % MOD
        ans += b[i]
        ans %= MOD
    # print(f'b: {b}')
    return ans

def solve2(n,a):
    if n == 1:
        return 1
    MOD = 10**9+7
    lcm = a[0]*a[1]//gcd(a[0], a[1])
    for i in range(2, n):
        lcm = lcm*a[i]//gcd(lcm, a[i])
    # print(f'lcm: {lcm}')
    # print(f'lcm(MOD): {lcm%MOD}')

    b = [0 for _ in range(n)]
    for i in range(n):
        b[i] = lcm//a[i]
    # print(f'b: {b}')
    b_mod = [b[i]%MOD for i in range(n)]
    # print(f'b_mod: {b_mod}')

    sum = 0
    for i in range(n):
        sum += b[i]
    # print(f'sum: {sum}')
    # print(f'sum(MOD): {sum % MOD}')
    return sum % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    # ans=solve(n,a)
    # printans(ans)

    ans=solve2(n,a)
    printans(ans)
