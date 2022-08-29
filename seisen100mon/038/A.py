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
    q=i_input()
    queries = []
    for _ in range(q):
        queries.append((input(), input()))
    return q, queries

def solve(q, queries):
    ans = []
    for s, t in queries:
        n = len(s)
        m = len(t)
        dp = [ [0]*(m+1) for _ in range(n+1) ]
        dpii = dp[0]
        for i in range(1, n+1):
            si = s[i-1]
            for j in range(1, m+1):
                tj = t[j-1]
                if si == tj:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i-1][j] if dp[i-1][j] > dp[i][j-1] else dp[i][j-1]
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        ans.append(dp[n][m])

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q, queries=readinput()
    ans=solve(q, queries)
    printans(ans)
