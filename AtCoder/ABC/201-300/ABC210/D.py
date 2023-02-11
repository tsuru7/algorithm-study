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
    h,w,c=m_input()
    aMap = []
    for _ in range(h):
        aMap.append(l_input())
    return h,w,c,aMap

def get_mincost(h, w, c, aMap):
    dp = []
    for _ in range(h):
        dp.append([INFTY]*w)
    dp[0][1] = aMap[0][0] + aMap[0][1] + c
    mincost = dp[0][1]
    for j in range(1, w):
        dp[0][j] = min(dp[0][j], dp[0][j-1] - aMap[0][j-1] + aMap[0][j] + c)
        dp[0][j] = min(dp[0][j], aMap[0][j-1] + aMap[0][j] + c)
        mincost = min(mincost, dp[0][j])
    dp[1][0] = aMap[0][0] + aMap[1][0] + c
    mincost = min(mincost, dp[1][0])
    for i in range(1, h):
        dp[i][0] = min(dp[i][0], dp[i-1][0] - aMap[i-1][0] + aMap[i][0] + c)
        dp[i][0] = min(dp[i][0], aMap[i-1][0] + aMap[i][0] + c)
        mincost = min(mincost, dp[i][0])
    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = min(dp[i][j], dp[i][j-1] - aMap[i][j-1] + aMap[i][j] + c)
            dp[i][j] = min(dp[i][j], aMap[i][j-1] + aMap[i][j] + c)
            dp[i][j] = min(dp[i][j], dp[i-1][j] - aMap[i-1][j] + aMap[i][j] + c)
            dp[i][j] = min(dp[i][j], aMap[i-1][j] + aMap[i][j] + c)
            mincost = min(mincost, dp[i][j])
    return mincost

def main(h,w,c,aMap):
    ans = get_mincost(h, w, c, aMap)
    for i in range(h):
        aMap[i] = aMap[i][::-1]
    ans = min(ans, get_mincost(h, w, c, aMap))

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,c,aMap=readinput()
    ans=main(h,w,c,aMap)
    printans(ans)
