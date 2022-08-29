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
    crlist = [ l_input() for _ in range(n) ]
    return n,crlist

def dfs(l, r, dp, crlist):
    # print(f'(l, r): ({l}, {r})')
    if dp[l][r] != INFTY:
        return dp[l][r]

    rl, cl = crlist[l]
    rr, cr = crlist[r]
    if r == l+1:
        dp[l][r] = rl*cl*cr
        return dp[l][r]
    tmpmin = INFTY
    for k in range(l, r):
        rk, ck = crlist[k]
        tmp = dfs(l, k, dp, crlist) + dfs(k+1, r, dp, crlist) + rl*ck*cr
        if tmp < tmpmin:
            tmpmin = tmp
    dp[l][r] = tmpmin
    return dp[l][r]
            

def solve(n,crlist):
    dp = [ [INFTY]*n for _ in range(n) ]
    for i in range(n):
        dp[i][i] = 0
    
    ans=dfs(0, n-1, dp, crlist)
    # print(f'dp: {dp}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,crlist=readinput()
    ans=solve(n,crlist)
    printans(ans)
