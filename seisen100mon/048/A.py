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
    queries = []
    while n != 0:
        queries.append(l_input())
        n = i_input()
    return queries

def dfs(l, r, dp, w):
    # print(f'(l, r): ({l}, {r})')
    if dp[l][r] != -1:
        return dp[l][r]
    
    if r == l+1:
        if abs(w[l]-w[r]) <= 1:
            dp[l][r] = 2
        else:
            dp[l][r] = 0
        return dp[l][r]
    
    tmp = 0
    if abs(w[l]-w[r]) <= 1:
        tmp2 = dfs(l+1, r-1, dp, w)
        if tmp2 == r-l-1:
            tmp = max(tmp, tmp2 + 2)
    for k in range(l+1, r):
        tmp = max(tmp, dfs(l, k, dp, w) + dfs(k+1, r, dp, w))
    dp[l][r] = tmp
    return dp[l][r]

def solve(queries):
    ans=[]
    for w in queries:
        n = len(w)
        l = 0
        r = n-1
        dp = [ [-1]*n for _ in range(n) ]
        for i in range(n):
            dp[i][i] = 0
        ans.append(dfs(l, r, dp, w))
        # print(f'dp: {dp}')
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
