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
    MOD = 10**9+7
    n = len(s)
    t = 'chokudai'
    m = len(t)
    dp = [ [0]*(n+1) for _ in range(m+1) ]
    dp[0] = [1]*(n+1)
    for i in range(1, m+1):
        ti = t[i-1]
        for j in range(1, n+1):
            sj = s[j-1]
            if sj == ti:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
            dp[i][j] = dp[i][j] % MOD
    return dp[m][n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
