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
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    maxlen = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i+1][j+1] = min(j-i, dp[i][j]+1)
                maxlen = max(maxlen, dp[i+1][j+1])

    return maxlen

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
