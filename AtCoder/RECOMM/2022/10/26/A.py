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
    n,m,q=m_input()
    queries = [l_input() for _ in range(q)]
    return n,m,q,queries

def dfs(now, n, m):
    global candidates

    if len(now) == n:
        candidates.append(now)
        return
    start = 1
    if len(now) > 0:
        start = now[-1]
    for i in range(start, m+1):
        dfs(now + [i], n, m)
    return
    

candidates = []
def solve(n,m,q,queries):
    global candidates

    dfs([], n, m)
    ans=0
    for alist in candidates:
        tmp = 0
        for a, b, c, d in queries:
            a -= 1
            b -= 1
            if alist[b] - alist[a] == c:
                tmp += d
        ans = max(ans, tmp)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,q,queries=readinput()
    ans=solve(n,m,q,queries)
    printans(ans)
