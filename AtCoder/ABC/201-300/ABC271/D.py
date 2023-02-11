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
    dp = [[(0, ' ') for _ in range(10001)] for _ in range(n+1)]
    dp[0][0] = (1, ' ')
    for i in range(1, n+1):
        ai, bi = abList[i-1]
        for j in range(10001):
            if j-ai >= 0 and dp[i-1][j-ai][0] > 0:
                dp[i][j] = (ai, 'H')
            if j-bi >= 0 and dp[i-1][j-bi][0] > 0:
                dp[i][j] = (bi, 'T')
    if dp[n][s][0] == 0:
        return ['No']
    seq = ''
    x = s
    for i in range(1, n+1)[::-1]:
        seq += dp[i][x][1]
        x -= dp[i][x][0]
    ans = ['Yes', seq[::-1]]
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,s,abList=readinput()
    ans=solve(n,s,abList)
    printans(ans)
