import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
        ai, bi = abList[i]
        for j in range(bi+1):
            for k in range(j*ai, x+1):
                dp[i+1][k] |= dp[i][k-j*ai]
    if dp[n][x]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,abList=readinput()
    ans=solve(n,x,abList)
    printans(ans)
