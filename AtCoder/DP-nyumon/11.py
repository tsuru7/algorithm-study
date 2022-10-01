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
    h,w=m_input()
    amap = [input() for _ in range(h)]
    return h,w,amap

def solve(h,w,amap):
    MOD = 10**9+7
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for row in range(h):
        for col in range(w):
            if amap[row][col] == '#':
                continue
            if row-1 >= 0:
                dp[row][col] += dp[row-1][col]
            if col-1 >= 0:
                dp[row][col] += dp[row][col-1]
            dp[row][col] %= MOD

    return dp[h-1][w-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,amap=readinput()
    ans=solve(h,w,amap)
    printans(ans)
