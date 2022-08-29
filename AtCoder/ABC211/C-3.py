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
    s = input()
    return s

def main(s):
    n = len(s)
    t = 'chokudai'
    m = len(t)
    MOD = 10**9+7
    # dp[i+1][j+1]: Sのi文字までを使って、Tのj文字までを作る通り数
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        si = s[i]
        for j in range(m+1):
            tj = t[j-1] if j > 0 else ''
            # s[i]を使わない場合
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
            # s[i]を使う場合はs[i]==t[j]である必要がある
            if si == tj:
                dp[i+1][j] += dp[i][j-1]
                dp[i+1][j] %= MOD
    return dp[n][m]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
