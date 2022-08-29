import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop

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
    n,m,r=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        s, t, d = m_input()
        graph[s].append((t, d))
    return n,m,r,graph

def solve(n,m,r,graph):
    heap = []
    dist = [INFTY for _ in range(n)]
    visited = [False for _ in range(n)]
    heappush(heap, (0, r))
    dist[r] = 0
    while len(heap) > 0:
        du, u = heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, dv in graph[u]:
            if not visited[v] and dist[v] > du + dv:
                dist[v] = du + dv
                heappush(heap, (dist[u]+dv, v))
    return dist

def printans(ans):
    for a in ans:
        if a == INFTY:
            print('INF')
        else:
            print(a)

if __name__=='__main__':
    n,m,r,graph=readinput()
    ans=solve(n,m,r,graph)
    printans(ans)
