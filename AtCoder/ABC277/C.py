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
    graph = dict()
    for _ in range(n):
        a, b = m_input()
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    return n,graph

def dfs(u, graph, visited):
    visited[u] = True
    if u not in graph:
        return
        
    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, visited)
    return

def solve(n,graph):
    visited = dict()
    for k, v in graph.items():
        visited[k] = False
    dfs(1, graph, visited)
    maxfloor = 1
    for floor, visited in visited.items():
        if visited:
            maxfloor = max(maxfloor, floor)
    return maxfloor

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
