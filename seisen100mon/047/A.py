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
    a = [i_input() for _ in range(n)]
    return n,a

def dfs(a, l, r, dp):
    if dp[l][r] != -1:
        return dp[l][r]
    if r == l+1:
        dp[l][r] = min(a[l], a[r])
        return dp[l][r]
     
    if a[l] > a[r]:
        ltmp = l+1
        rtmp = r
    else:
        ltmp = l
        rtmp = r-1
    vl = dfs(a, ltmp+1, rtmp, dp) + a[ltmp]
    vr = dfs(a, ltmp, rtmp-1, dp) + a[rtmp]
    # dp[ltmp][rtmp] = max(vl, vr)
    dp[l][r] = max(vl, vr)
    return dp[l][r]

def solve(n,a):
    ans = 0
    for i in range(n):
        b = a[i+1:]+a[:i]
        dp = [ [-1]*(n-1) for _ in range(n-1) ]
        for i in range(n-1):
            dp[i][i] = 0
        tmp = dfs(b, 0, n-2, dp) + a[i]
        print(f'tmp: {tmp}')
        print(f'dp: {dp}')
        ans = max(ans, tmp)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
