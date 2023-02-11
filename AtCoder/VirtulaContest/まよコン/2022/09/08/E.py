import sys
sys.setrecursionlimit(10**6)
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
    n=i_input()
    edge = [l_input() for _ in range(n-1)]
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return n,edge,q,queries

def solve(n,edge,q,queries):
    graph = [[] for _ in range(n)]
    for a, b in edge:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    depth = [-1 for _ in range(n)]
    queue = deque()
    queue.append(0)
    depth[0] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            queue.append(v)
    c = [0 for _ in range(n)]
    for t, e, x in queries:
        if t == 1:
            e -= 1
            a, b = edge[e]
            a -= 1
            b -= 1
            if depth[a] < depth[b]:
                c[0] += x
                c[b] -= x
            else:
                c[a] += x
        else:
            e -= 1
            a, b = edge[e]
            a -= 1
            b -= 1
            if depth[b] < depth[a]:
                c[0] += x
                c[a] -= x
            else:
                c[b] += x
    visited = [False for _ in range(n)]
    u = 0
    queue = deque()
    queue.append(u)
    visited[u] = True
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v]:
                continue
            c[v] += c[u]
            queue.append(v)
            visited[v] = True
    return c

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,edge,q,queries=readinput()
    ans=solve(n,edge,q,queries)
    printans(ans)
