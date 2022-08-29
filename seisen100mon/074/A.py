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
    k = i_input()
    return n,k

def solve(n,k):
    MOD = 10**9+7
    m = n+k-1
    k = min(n-1,k)
    bunsi = 1
    bunbo = 1
    for i in range(k):
        bunsi *= m
        bunsi %= MOD
        bunbo *= k
        bunbo %= MOD
        m -= 1
        k -= 1
    return (bunsi * pow(bunbo, MOD-2, MOD)) % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
