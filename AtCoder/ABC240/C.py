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
    ablist = [l_input() for _ in range(n)]
    return n,x,ablist

def solve(n,x,ablist):
    dp = [ [False]*(x+1) for _ in range(n+1) ]
    dp[0][0] = True
    for i in range(1, n+1):
        ai, bi = ablist[i-1]
        for j in range(x+1):
            if j-ai >= 0:
                dp[i][j] |= dp[i-1][j-ai]
            if j-bi >= 0:
                dp[i][j] |= dp[i-1][j-bi]
    if dp[n][x]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,ablist=readinput()
    ans=solve(n,x,ablist)
    printans(ans)
