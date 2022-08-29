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
    n,q=m_input()
    graph = [ [] for _ in range(n) ]
    for _ in range(n-1):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    queries = [ l_input() for _ in range(q) ]
    return n,q,graph,queries

def dfs(u, graph, visited, counter):
    visited[u] = True
    for v in graph[u]:
        if visited[v]:
            continue
        counter[v] += counter[u]
        dfs(v, graph, visited, counter)

def solve(n,q,graph,queries):
    counter = [0]*n
    for p, x in queries:
        p -= 1
        counter[p] += x
    visited = [False]*n
    dfs(0, graph, visited, counter)
    return counter

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,q,graph,queries=readinput()
    ans=solve(n,q,graph,queries)
    printans(ans)
