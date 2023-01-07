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
    cmap = [input() for _ in range(h)]
    return h,w,cmap

def solve(h,w,cmap):
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for row in range(h):
        for col in range(w):
            if col+1 < w and cmap[row][col+1] == '.':
                dp[row][col+1] += dp[row][col]
            if row+1 < h and cmap[row+1][col] == '.':
                dp[row+1][col] += dp[row][col]
    return dp[-1][-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=solve(h,w,cmap)
    printans(ans)
