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
    amap = [ l_input() for _ in range(n) ]
    return n,amap

def has_bit(n, i):
    return (n & (1<<i) > 0)

def solve(n,amap):
    dp = [ [INFTY]*n for _ in range(2**n) ]
    dp[0][0] = 0
    for x in range(2**n):
        for i in range(n):
            for j in range(n):
                if has_bit(x, j) or i == j:
                    continue
                dp[x|(1<<j)][j] = min(dp[x|(1<<j)][j], dp[x][i] + amap[i][j])
    return dp[2**n-1][0]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amap=readinput()
    ans=solve(n,amap)
    printans(ans)
