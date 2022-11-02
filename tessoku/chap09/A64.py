import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappop, heappush

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
        a, b, c = m_input()
        a -= 1
        b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    return n,graph

def solve(n,graph):
    depth = [INFTY for _ in range(n)]
    done = [False for _ in range(n)]
    heap = []
    heappush(heap, (0, 0))
    depth[0] = 0
    while len(heap) > 0:
        _, u = heappop(heap)
        if done[u]:
            continue
        done[u] = True
        for v, c in graph[u]:
            if depth[v] > depth[u] + c:
                depth[v] = depth[u] + c
                heappush(heap, (depth[v], v))
    for i in range(n):
        if depth[i] == INFTY:
            depth[i] = -1
    return depth

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
