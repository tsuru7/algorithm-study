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
    t = input()
    return s,t

def solve(s,t):
    lens = len(s)
    lent = len(t)
    dp = [[INFTY for _ in range(lent+1)] for _ in range(lens+1)]
    for i in range(lens+1):
        dp[i][0] = i
    for j in range(lent+1):
        dp[0][j] = j
    for i in range(lens):
        si = s[i]
        for j in range(lent):
            tj = t[j]
            if si == tj:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
            else:
                dp[i+1][j+1] = min(dp[i+1][j+1], min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1)
    return dp[lens][lent]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=solve(s,t)
    printans(ans)
