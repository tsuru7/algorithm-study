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
    k=i_input()
    return k

def solve(k):
    if k % 9 != 0:
        return 0
    MOD = 10**9+7
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for i in range(1, k+1):
        for j in range(1, min(9, i)+1):
            dp[i] += dp[i-j]
        dp[i] %= MOD
    return dp[k]

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=solve(k)
    printans(ans)
