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

choose_memo = None
def init_choose(n):
    global choose_memo

    MOD = 998244353
    choose_memo = [ [1]*(n+1) for _ in range(n+1) ]

    for i in range(1, n+1):
        choose_memo[i][0] = 1
        choose_memo[i][i] = 1
        for j in range(1, i):
            choose_memo[i][j] = (choose_memo[i-1][j] + choose_memo[i-1][j-1]) % MOD
    # print(f'choose_memo: {choose_memo}')

def choose(n, r):
    MOD = 998244353
    return choose_memo[n][r]

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
