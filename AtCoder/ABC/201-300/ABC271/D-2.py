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
    n,s=m_input()
    abList = [l_input() for _ in range(n)]
    return n,s,abList

def solve(n,s,abList):
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        ai, bi = abList[i]
        for j in range(s+1):
            if j-ai >= 0:
                dp[i+1][j] |= dp[i][j-ai]
            if j-bi >= 0:
                dp[i+1][j] |= dp[i][j-bi]
    if not dp[n][s]:
        return ['No']
    series = ''
    x = s
    for i in range(1, n+1)[::-1]:
        ai, bi = abList[i-1]
        if x-ai >=0 and dp[i-1][x-ai]:
            series += 'H'
            x -= ai
        elif x-bi >= 0 and dp[i-1][x-bi]:
            series += 'T'
            x -= bi

    return ['Yes', series[::-1]]

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,s,abList=readinput()
    ans=solve(n,s,abList)
    printans(ans)
