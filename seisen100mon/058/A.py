import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque
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
    n,m,k,s=m_input()
    p,q = m_input()
    c = set([i_input()-1 for _ in range(k)])
    # print(f'c: {c}')
    graph = [set() for _ in range(n+1)]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        if a in c:
            graph[n].add(b)
        elif b in c:
            graph[n].add(a)
        else:
            graph[a].add(b)
            graph[b].add(a)
    return n,m,k,s,p,q,graph

def solve(n,m,k,s,p,q,graph):
    cost = [p for _ in range(n)]
    dist = [INFTY for _ in range(n+1)]
    queue = deque()
    queue.append(n)
    dist[n] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in list(graph[u]):
            if dist[v] == INFTY:
                dist[v] = dist[u] + 1
                if dist[v] <= s:
                    cost[v] = q
                queue.append(v)
    
    # print(f'graph[n]: {graph[n]}')
    # print(f'cost: {cost}')

    dist = [INFTY for _ in range(n)]
    heap = []
    visited = [False for _ in range(n)]
    ans=0
    heappush(heap, (0, 0))
    dist[0] = 0
    while len(heap) > 0:
        du, u = heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v in list(graph[u]):
            if not visited[v] and dist[v] > du + cost[v]:
                dist[v] = du + cost[v]
                heappush(heap, (dist[v], v))
    
    return dist[n-1]-cost[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,s,p,q,graph=readinput()
    ans=solve(n,m,k,s,p,q,graph)
    printans(ans)
