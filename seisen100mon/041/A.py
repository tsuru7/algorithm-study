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
    d,n=m_input()
    tlist = [i_input() for _ in range(d) ]
    abclist = [l_input() for _ in range(n)]
    return d,n,tlist,abclist

def solve(d,n,tlist,abclist):
    dp = [ [-1]*n for _ in range(d) ]
    t0 = tlist[0]
    for j, (a, b, c) in enumerate(abclist):
        if a <= t0 <= b:
            dp[0][j] = 0
    for i in range(1, d):
        ti = tlist[i]
        for j in range(n):
            aj, bj, cj = abclist[j]
            if ti < aj or bj < ti:
                continue
            for k in range(n):
                if dp[i-1][k] == -1:
                    continue
                ak, bk, ck = abclist[k]
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(cj-ck))
    
    return max(dp[d-1])

def printans(ans):
    print(ans)

if __name__=='__main__':
    d,n,tlist,abclist=readinput()
    ans=solve(d,n,tlist,abclist)
    printans(ans)
