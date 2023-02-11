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
        graph[a].append(b)
    for i in range(n):
        graph[i].sort()
    return n,m,graph

def dfs(u, graph, visited, order):
    visited[u] = True
    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, visited, order)
    order.append(u)
    return

def solve(n,m,graph):
    visited = [False for _ in range(n)]
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited, order)
    order.reverse()
    return order

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
