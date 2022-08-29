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
    n,t=m_input()
    abList = [l_input() for _ in range(n)]
    return n,t,abList

def solve(n,t,abList):
    asum = 0
    bsum = 0
    for ai, bi in abList:
        asum += ai
        bsum += bi
    print(f'asum: {asum}, bsum: {bsum}')

    amax, _ = max(abList, key=lambda x: x[0])
    print(f'amax: {amax}')
    dp = [[-INFTY for _ in range(t+amax)] for _ in range(n+1)]
    tmax = [0 for _ in range(t+amax)]
    dp[0][0] = 0
    for i in range(n):
        ai, bi = abList[i]
        for j in range(t+amax):
            if dp[i+1][j] < dp[i][j]:
                dp[i+1][j] = dp[i][j]
            if j-ai >= 0:
                if dp[i+1][j] < dp[i][j-ai]+bi:
                    dp[i+1][j] = dp[i][j-ai]+bi
                    tmax[j] = max(tmax[j], ai)
    ans=max(dp[n][:t+1])
    print(f'ans1: {ans}')
    print(f'tmax: {tmax}')
    for j in range(t+1, t+amax):
        if j - tmax[j] < t:
            ans = max(ans, dp[n][j])
        print(f'j: {j}, tmax[j]: {tmax[j]}, dp[n][j]: {dp[n][j]}, ans: {ans}')


    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,t,abList=readinput()
    ans=solve(n,t,abList)
    printans(ans)
