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
    return n

def solve(n):
    dp = [INFTY for _ in range(n+1)]
    dp[0] = 0
    for i in range(n):
        dp[i+1] = min(dp[i+1], dp[i]+1)  # 1円を追加で支払う
        j = 1
        while i+6**j <= n:
            dp[i+6**j] = min(dp[i+6**j], dp[i]+1) # 6**j円を追加で支払う
            j += 1
        j = 1
        while i+9**j <= n:
            dp[i+9**j] = min(dp[i+9**j], dp[i]+1) # 9**j円を追加で支払う
            j += 1
    return dp[n]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
