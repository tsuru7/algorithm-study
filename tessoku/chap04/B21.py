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
    dp = [[-INFTY for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 1
    for slen in range(2, n+1):
        for l in range(1, n-slen+1+1):
            r = l + slen - 1
            if s[l-1] == s[r-1]:
                if r == l+1:
                    dp[l][r] = 2
                else:
                    dp[l][r] = max(dp[l][r], dp[l+1][r-1] + 2)
            else:
                dp[l][r] = max(dp[l][r], dp[l+1][r])
                dp[l][r] = max(dp[l][r], dp[l][r-1])

    return dp[1][n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
