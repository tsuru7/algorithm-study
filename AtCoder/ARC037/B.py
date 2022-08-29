import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque
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
        graph[v].append(u)
        graph[u].append(v)
    return n,m,graph

def bfs(u, graph, visited):
    n = len(graph)
    parent = [-1]*n
    queue = deque()
    queue.append(u)
    visited[u] = True
    cyclic = False
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v] and v != parent[u]:
                cyclic = True
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return cyclic, visited


def main(n,m,graph):
    visited = [False]*n
    ans=0
    for i in range(n):
        if visited[i]:
            continue
        cyclic, visited = bfs(i, graph, visited)
        if not cyclic:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=main(n,m,graph)
    printans(ans)
