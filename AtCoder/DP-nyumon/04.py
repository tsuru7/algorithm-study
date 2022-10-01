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
    abclist = [l_input() for _ in range(n)]
    return n,abclist

def solve(n,abclist):
    dp = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        abc = abclist[i-1]
        for j in range(3):
            for k in range(3):
                if k == j:
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k]+abc[j])

    return max(dp[-1])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,abclist=readinput()
    ans=solve(n,abclist)
    printans(ans)
