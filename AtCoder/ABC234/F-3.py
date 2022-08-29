import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter

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
    s = input()
    return s

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

fact_memo = None
inv_memo = None
finv_memo = None
def init_choose(n):
    global fact_memo
    global inv_memo
    global finv_memo

    MOD = 998244353
    fact_memo = [1]*(n+1)
    inv_memo = [1]*(n+1)
    finv_memo = [1]*(n+1)

    fact_memo[0] = 1
    inv_memo[0] = pow(1, MOD-2, MOD)
    finv_memo[0] = inv_memo[0]
    for i in range(1, n+1):
        fact_memo[i] = fact_memo[i-1]*i
        fact_memo[i] %= MOD
        # inv_memo[i] = pow(i, MOD-2, MOD)
        # finv_memo[i] = finv_memo[i-1]*inv_memo[i]
        # finv_memo[i] %= MOD

        (d, x, y) = exEuclid(i, MOD)
        inv_memo[i] = x
        finv_memo[i] = (finv_memo[i-1]*inv_memo[i]) % MOD

def choose(n, r):
    MOD = 998244353
    return (fact_memo[n]*finv_memo[r]*finv_memo[n-r])%MOD

def solve(s):
    MOD = 998244353
    n = len(s)
    init_choose(n)
    alp_cnt = Counter(s)
    dp = [ [0]*(n+1) for _ in range(26+1) ]

    for i in range(26+1):
        dp[i][0] = 1
    # print(f'dp: {dp}')

    for i in range(1, 27):
        ni = alp_cnt[chr(ord('a')+i-1)]
        for j in range(1, n+1):
            for k in range(ni+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]*choose(j, k)
                    dp[i][j] %= MOD
                else:
                    break
            # print(f'i: {i}, j: {j}, dp[i][j]: {dp[i][j]}')
    # print(f'n: {n}, dp: {dp}')
    ans = sum(dp[26][1:n+1]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
