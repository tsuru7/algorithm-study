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
    n,m=m_input()
    amat = [l_input() for _ in range(m)]
    return n,m,amat

def solve(n,m,amat):
    ALL = 2**n
    dp = [[INFTY//2 for _ in range(ALL)] for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(ALL):
            # i 番目のクーポンを使わない場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]) 
            # i 番目のクーポンを使う場合
            jj = j
            for k in range(n):
                if amat[i][k] == 1:
                    jj |= (1<<k)
            dp[i+1][jj] = min(dp[i+1][jj], dp[i][j] + 1)
    # print(*dp, sep='\n')
    return dp[m][-1] if dp[m][-1] <= m else -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,amat=readinput()
    ans=solve(n,m,amat)
    printans(ans)
