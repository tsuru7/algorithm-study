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
    x=l_input()
    cydict = dict()
    for _ in range(m):
        c, y = m_input()
        cydict[c] = y
    return n,m,x,cydict

def solve(n,m,x,cydict):
    # print(f'cydict: {cydict}')
    dp = [ [-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i+1][0] = max(dp[i])
        for j in range(1, n+1):
            if j in cydict:
                bonus = cydict[j]
            else:
                bonus = 0
            if dp[i][j-1] < 0:
                continue
            # print(f'i+i: {i+1}, j: {j}, bonus: {bonus}')
            dp[i+1][j] = dp[i][j-1]+x[i]+bonus
    # print(*dp, sep='\n')
    return max(dp[n])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,x,cydict=readinput()
    ans=solve(n,m,x,cydict)
    printans(ans)
