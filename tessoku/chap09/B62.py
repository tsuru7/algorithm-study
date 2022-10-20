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
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = m_input()
        graph[a].append(b)
        graph[b].append(a)
    return n,graph

def dfs(u, n, graph, visited):
    path.append(u)
    visited[u] = True
    if u == n:
        return path
    ans = None
    for v in graph[u]:
        if visited[v]:
            continue
        ans = dfs(v, n, graph, visited)
        if ans is not None:
            return ans
    path.pop()
    return ans

path = None
def solve(n,graph):
    global path

    path = []
    visited = [False for _ in range(n+1)]
    ans = dfs(1, n, graph, visited)
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
