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
    n,m,x,y=m_input()
    x -= 1
    y -= 1
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, t, k = l_input()
        a -= 1
        b -= 1
        graph[a].append((b, t, k))
        graph[b].append((a, t, k))
    return n,x,y,graph

def solve(n,x,y,graph):
    heap = []
    dist = [INFTY for _ in range(n)]
    done = [False for _ in range(n)]
    heappush(heap, (0, x))
    dist[x] = 0
    while len(heap) > 0:
        ut, u = heappop(heap)
        if done[u]:
            continue
        done[u] = True
        for v, t, k in graph[u]:
            wait = -ut % k
            vt = ut + t + wait
            if dist[v] > vt:
                dist[v] = vt
                heappush(heap, (vt, v))
    if dist[y] == INFTY:
        return -1
    else:
        return dist[y]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,graph=readinput()
    ans=solve(n,x,y,graph)
    printans(ans)
