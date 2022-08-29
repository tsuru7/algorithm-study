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

def dfs(l, r, a, dp, joi_turn):
    # print(f'(l, r): ({l}, {r})')
    if dp[l][r] != -1:
        return dp[l][r]
    

    if not joi_turn:
        if a[l] < a[r]:
            dp[l][r] = dfs(l, r-1, a, dp, True)
        else:
            dp[l][r] = dfs(l+1, r, a, dp, True)
    else:
        dp[l][r] = max(a[l]+dfs(l+1, r, a, dp, False), dfs(l, r-1, a, dp, False)+a[r])

    return dp[l][r]

def solve(n,a):
    joi_turn = True
    a2 = a+a
    dp = [ [-1]*(2*n) for _ in range(2*n) ]
    if n % 2 == 1:
        for i in range(2*n):
            dp[i][i] = a2[i]
    else:
        for i in range(2*n):
            dp[i][i] = 0
    
    ans=0
    for i in range(n):
        tmp = a2[i] + dfs(i+1, n-1+i, a2, dp, not joi_turn)
        ans = max(ans, tmp)
    # print(f'dp: {dp}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
