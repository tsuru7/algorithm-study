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
    queries = []
    n, m = m_input()
    while not (n == 0 and m == 0):
        clist = [i_input() for _ in range(m)]
        xlist = [i_input() for _ in range(n)]
        queries.append((clist, xlist))
        n, m = m_input()
    return queries

def solve(queries):
    min2 = lambda x, y: x if x <= y else y
    ans=[]
    for clist, xlist in queries:
        n = len(xlist)
        m = len(clist)
        dp = [ [INFTY]*256 for _ in range(n+1) ]
        dp[0][128] = 0
        for i in range(n):
            xi = xlist[i]
            for j in range(256):
                if dp[i][j] == INFTY:
                    continue
                for k in range(m):
                    ck = clist[k]
                    jnext = j+ck
                    if jnext < 0:
                        jnext = 0
                    elif jnext > 255:
                        jnext = 255
                    cost_next = (jnext - xi)**2
                    dp[i+1][jnext] = min2(dp[i+1][jnext], dp[i][j]+cost_next)
        ans.append(min(dp[n]))
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
