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
    n,m=m_input()
    h=l_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        if h[u] > h[v]:
            graph[u].append((v, 0))
            graph[v].append((u, h[u]-h[v]))
        else:
            graph[v].append((u, 0))
            graph[u].append((v, h[v]-h[u]))
    return n,m,h,graph

def solve(n,m,h,graph):
    done = [False for _ in range(n)]
    dist = [INFTY for _ in range(n)]
    heap = []
    heappush(heap, (0, 0))
    dist[0] = 0
    while len(heap) > 0:
        _, u = heappop(heap)
        if done[u]:
            continue
        done[u] = True
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heappush(heap, (dist[v], v))
    ans=-INFTY
    for i in range(n):
        ans = max(ans, h[0] - h[i] - dist[i])
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,h,graph=readinput()
    ans=solve(n,m,h,graph)
    printans(ans)
