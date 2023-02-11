import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    return n

def g(k):
    MOD = 998244353

    ans = 9*10**(k-1) % MOD
    ans *= 9*10**(k-1)+1
    ans %= MOD
    inv2 = pow(2, MOD-2, MOD)
    ans *= inv2
    ans %= MOD
    return ans

def solve(n):
    MOD = 998244353
    k = len(str(n))
    # print(f'g(1): {g(1)}')
    # print(f'g(2): {g(2)}')
    ans=0
    for i in range(1, k):
        ans += g(i)
        ans %= MOD
        # print(f'k: {i}, ans: {ans}')
    m = n - 10**(k-1) + 1
    # print(f'm: {m}, k: {k}, ans: {ans}')
    a = m % MOD
    a *= m+1
    a %= MOD
    inv2 = pow(2, MOD-2, MOD)
    a *= inv2
    a %= MOD
    ans += a
    ans %= MOD

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
