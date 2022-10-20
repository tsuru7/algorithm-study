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
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,c,graph

def dfs(u, graph, c):
    global visited
    global good
    global used

    visited[u] = True
    if c[u] not in used:
        good.add(u)
        used.add(c[u])
    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, c)
    if u in good:
        used.remove(c[u])
    return

good = None
visited = None
used = None
def solve(n,c,graph):
    global good
    global visited
    global used

    good = set()
    visited = [False for _ in range(n)]
    used = set()
    dfs(0, graph, c)
    good = list(good)
    good.sort()
    ans = [v + 1 for v in good]
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,c,graph=readinput()
    ans=solve(n,c,graph)
    printans(ans)
