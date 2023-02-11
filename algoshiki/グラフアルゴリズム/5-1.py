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
    n,m,s,t=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        graph[a].append(b)
    return n,m,s,t,graph

def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)
    return

def solve(n,m,s,t,graph):
    visited = [False for _ in range(n)]
    u = s
    dfs(u, graph, visited)
    if visited[t]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,s,t,graph=readinput()
    ans=solve(n,m,s,t,graph)
    printans(ans)
