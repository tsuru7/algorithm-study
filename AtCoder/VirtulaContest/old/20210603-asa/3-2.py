import sys
sys.setrecursionlimit(10**5)
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
    n,k=m_input()
    r, s, p = m_input()
    t=input()
    return n,k,r,s,p,t

def solve(r,s,p,t):
    n = len(t)
    rps = ['r', 'p', 's']
    dp = [[0]*3 for _ in range(n)]  # r: 0, p: 1, s: 2
    if t[0] == 'r':
        dp[0][1] = p
    elif t[0] == 'p':
        dp[0][2] = s
    elif t[0] == 's':
        dp[0][0] = r
    for i in range(1, n):
        if t[i] == 'r':
            dp[i][0] = max(dp[i][0], dp[i-1][1])
            dp[i][0] = max(dp[i][0], dp[i-1][2])
            dp[i][1] = max(dp[i][1], dp[i-1][0]+p)
            dp[i][1] = max(dp[i][1], dp[i-1][2]+p)
            dp[i][2] = max(dp[i][2], dp[i-1][0])
            dp[i][2] = max(dp[i][2], dp[i-1][1])
        elif t[i] == 'p':
            dp[i][0] = max(dp[i][0], dp[i-1][1])
            dp[i][0] = max(dp[i][0], dp[i-1][2])
            dp[i][1] = max(dp[i][1], dp[i-1][0])
            dp[i][1] = max(dp[i][1], dp[i-1][2])
            dp[i][2] = max(dp[i][2], dp[i-1][0]+s)
            dp[i][2] = max(dp[i][2], dp[i-1][1]+s)
        if t[i] == 's':
            dp[i][0] = max(dp[i][0], dp[i-1][1]+r)
            dp[i][0] = max(dp[i][0], dp[i-1][2]+r)
            dp[i][1] = max(dp[i][1], dp[i-1][0])
            dp[i][1] = max(dp[i][1], dp[i-1][2])
            dp[i][2] = max(dp[i][2], dp[i-1][0])
            dp[i][2] = max(dp[i][2], dp[i-1][1])
    # print(t, dp)
    ans = max(dp[n-1])
    return ans

def main(n,k,r,s,p,t):
    tsub = ['']*k
    for i in range(n):
        tsub[i%k] += t[i]
    ans = 0
    for i in range(k):
        ans += solve(r,s,p,tsub[i])

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,r,s,p,t=readinput()
    ans=main(n,k,r,s,p,t)
    printans(ans)
