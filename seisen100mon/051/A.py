from lzma import MODE_FAST
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
    s = input()
    return n,s

def solve(n,s):
    MOD = 10007
    dp = [[0 for i in range(8)] for j in range(n+1)]
    dp[0][4] = 1
    for i in range(1, n+1):
        si = s[i-1]
        if si == 'J':
            bit = 4
        elif si == 'O':
            bit = 2
        else:
            bit = 1
        for jstate in range(1, 8):
            if jstate & bit == 0:
                continue
            for kstate in range(1, 8):
                if jstate & kstate == 0:
                    continue
                dp[i][jstate] += dp[i-1][kstate]
            dp[i][jstate] %= MOD

    ans=sum(dp[-1]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
