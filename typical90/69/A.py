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
    n,k=m_input()
    return n,k

def solve(n,k):
    MOD = 10**9+7
    if n == 1:
        return k % MOD
    elif n == 2:
        return k*(k-1) % MOD
    ans=k*(k-1) % MOD
    m = n - 2
    x = k - 2
    while m > 0:
        if m % 2 == 1:
            ans *= x
            ans %= MOD
        m //= 2
        x *= x
        x %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
