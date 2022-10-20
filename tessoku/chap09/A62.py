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
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,graph

def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, visited)
    return

def solve(n,graph):
    visited = [False for _ in range(n)]
    dfs(0, graph, visited)
    if sum(visited) == n:
        return 'The graph is connected.'
    else:
        return ' The graph is not connected.'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
