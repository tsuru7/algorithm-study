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
    n,x=m_input()
    abList = [l_input() for _ in range(n)]
    return n,x,abList

def solve(n,x,abList):
    dp = [[False for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        ai, bi = abList[i-1]
        for j in range(x+1):
            if j+ai <= x:
                dp[i+1][j+ai] |= dp[i][j]
            if j+bi <= x:
                dp[i+1][j+bi] |= dp[i][j]
    if dp[-1][x]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,abList=readinput()
    ans=solve(n,x,abList)
    printans(ans)
