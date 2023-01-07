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
    n,p=m_input()
    return n,p

def solve(n,p):
    MOD = 998244353
    inv100 = pow(100, MOD-2, MOD)
    p_mod = (p * inv100) % MOD
    q_mod = (1 - p_mod) % MOD

    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = p_mod * dp[i-2] + q_mod * dp[i-1] + 1
        dp[i] %= MOD

    # print(f'dp: {dp}')
    return dp[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
