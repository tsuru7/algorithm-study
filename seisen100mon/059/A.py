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
    n,k=m_input()
    crlist = [l_input() for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(k):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,k,crlist,graph

def solve(n,k,crlist,graph):
    graph2 = [[] for _ in range(n)]
    for i in range(n):
        ci, ri = crlist[i]
        dest = []
        dist = [-1 for _ in range(n)]
        queue = deque()
        queue.append(i)
        dist[i] = 0
        while len(queue) > 0:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    if dist[v] <= ri:
                        queue.append(v)
                        dest.append(v)
        graph2[i] = dest
        # print(f'i: {i}, graph2[i]: {dest}')
    
    dist = [INFTY for _ in range(n)]
    visited = [False for _ in range(n)]
    heap = []
    heappush(heap, (0,0))
    while len(heap) > 0:
        du, u = heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v in graph2[u]:
            if not visited[v] and dist[v] > du + crlist[u][0]:
                dist[v] = du + crlist[u][0]
                heappush(heap, (dist[v], v))

    return dist[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,crlist,graph=readinput()
    ans=solve(n,k,crlist,graph)
    printans(ans)
