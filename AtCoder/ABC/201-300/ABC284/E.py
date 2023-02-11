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
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,graph

total = 0
def dfs(u, graph, visited):
    global total

    visited[u] = True
    total += 1
    if total >= 10**6:
        return

    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v, graph, visited)
    visited[u] = False
    return

def solve(n,m,graph):
    global total

    visited = [False for _ in range(n)]

    dfs(0, graph, visited)

    return min(total, 10**6)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
