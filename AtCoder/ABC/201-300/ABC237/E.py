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
    graph = [ [] for _ in range(n) ]
    geta = 0
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        if h[u] >= h[v]:
            graph[u].append((v, -(h[u]-h[v])))
            graph[v].append((u, 2*(h[u]-h[v])))
            geta = max(geta, (h[u]-h[v]))
        else:
            graph[u].append((v, 2*(h[v]-h[u])))
            graph[v].append((u, -(h[v]-h[u])))
            geta = max(geta, (h[v]-h[u]))

    return n,m,graph,geta

def solve(n,m,graph,geta):
    print(f'graph: {graph}, geta: {geta}')
    # for u in range(n):
    #     newlist = []
    #     for v, w in graph[u]:
    #         newlist.append((v, w+geta))
    #     graph[u] = newlist
    
    heap = []
    heappush(heap, (0, 0))
    depth = [-1]*n
    depth[0] = 0
    dist = [-1]*n
    dist[0] = 0
    done = [False]*n
    while len(heap) > 0:
        _, u = heappop(heap)
        if done[u]:
            continue
        done[u] = True

        for v, w in graph[u]:
            depth[v] = depth[u] + 1
            if dist[v] == -1 or dist[v] > dist[u] + w + geta*depth[v]:
                dist[v] = dist[u] + w - geta*depth[v]
                heappush(heap, (dist[v], v))
    print(f'dist: {dist}')
    ans=-min(dist)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph,geta=readinput()
    ans=solve(n,m,graph,geta)
    printans(ans)
