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
    snukes = [l_input() for _ in range(n)]
    return n,snukes

def solve(n,snukes):
    dp = [[-INFTY for _ in range(5)] for _ in range(n+1)]
    dp[0][0] = 0
    t0 = 0
    for i in range(n):
        t, x, a = snukes[i]
        for j in range(5):
            # 現時点で座標jにいる
            for k in range(5):
                # 前の時点で座標kにいた
                if abs(j-k) > t - t0:
                    # 移動不可能なケースはスキップ
                    continue
                if j == x:
                    # すぬけゲット
                    dp[i+1][j] = max(dp[i+1][j], dp[i][k] + a)
                else:
                    # すぬけゲットせず(移動のみ)
                    dp[i+1][j] = max(dp[i+1][j], dp[i][k])
        t0 = t
    # print(*dp, sep='\n')
    return max(dp[n])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,snukes=readinput()
    ans=solve(n,snukes)
    printans(ans)
