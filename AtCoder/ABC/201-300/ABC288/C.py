import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    return n,m,graph

def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, visited)
    return

def solve(n,m,graph):
    visited = [False for _ in range(n)]
    connected = 0
    for i in range(n):
        if not visited[i]:
            connected += 1
            dfs(i, graph, visited)
    tree_edge = n - connected
    return m - tree_edge

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
