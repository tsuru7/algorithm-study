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
    graph = [[]]
    for _ in range(n):
        tmp = l_input()
        u = tmp[0]
        k = tmp[1]
        v = tmp[2:]
        graph.append(v)
    return n,graph

def dfs(u, graph, visited, finished, elapsed):
    for v in graph[u]:
        if visited[v] > 0:
            continue
        elapsed += 1
        visited[v] = elapsed
        elapsed = dfs(v, graph, visited, finished, elapsed)
    elapsed += 1
    finished[u] = elapsed
    return elapsed

def solve(n,graph):
    visited = [0]*(n+1)
    finished = [0]*(n+1)
    elapsed = 0
    for i in range(1, n+1):
        if visited[i] > 0:
            continue
        elapsed += 1
        visited[i] = elapsed
        elapsed = dfs(i, graph, visited, finished, elapsed)
    ans=[]
    for i in range(1, n+1):
        ans.append((i, visited[i], finished[i]))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
