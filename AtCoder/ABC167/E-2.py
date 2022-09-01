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
    n,m,k=m_input()
    return n,m,k

def solve(n,m,k):
    MOD = 998244353
    fact = [0 for _ in range(2*10**5+1)]
    inv  = [0 for _ in range(2*10**5+1)]
    fact[0] = 1
    fact[1] = 1
    inv[0] = 1
    inv[1] = 1
    for i in range(2, n):
        fact[i] = (fact[i-1]*i) % MOD
        inv[i] = pow(fact[i], MOD-2, MOD)
    ans=0
    for i in range(k+1):
        comb = fact[n-1]*inv[i]*inv[n-1-i]
        tmp = comb * m * pow(m-1, n-1-i, MOD)
        tmp %= MOD
        ans += tmp
        ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k=readinput()
    ans=solve(n,m,k)
    printans(ans)
