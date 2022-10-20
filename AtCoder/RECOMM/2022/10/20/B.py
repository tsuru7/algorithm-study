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
    c=l_input()
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b=m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,c,graph

def dfs(u, graph, c):
    global used
    global good
    global visited

    visited[u] = True
    if used[c[u]] == 0:
        good[u] = True
    used[c[u]] += 1
    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, c)
    used[c[u]] -= 1
    return

used = None
good = None
visited = None
def solve(n,c,graph):
    global used
    global good
    global visited

    used = [0 for _ in range(10**5+1)]
    good = [False for _ in range(n)]
    visited = [False for _ in range(n)]
    dfs(0, graph, c)
    ans = []
    for i in range(n):
        if good[i]:
            ans.append(i+1)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,c,graph=readinput()
    ans=solve(n,c,graph)
    printans(ans)
