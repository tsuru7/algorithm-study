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

def to1d(u, stat):
    return 2*u+stat

def readinput():
    n,m,k=m_input()
    graph = [[] for _ in range(n*2)]
    for _ in range(m):
        u, v, a = m_input()
        u -= 1
        v -= 1
        graph[to1d(u, a)].append((to1d(v, a), 1))
        graph[to1d(v, a)].append((to1d(u, a), 1))
    s=l_input()
    for si in s:
        si -= 1
        graph[to1d(si, 0)].append((to1d(si, 1), 0))
        graph[to1d(si, 1)].append((to1d(si, 0), 0))
    return n,graph

def solve(n,graph):

    # print(f'graph: {graph}')

    heap = []
    depth = [INFTY for _ in range(2*n)]
    done = [False for _ in range(2*n)]
    u = to1d(0, 1)
    ucost = 0
    heappush(heap, (ucost, u))
    depth[u] = 0
    while len(heap) > 0:
        ucost, u = heappop(heap)
        if done[u]:
            continue
        done[u] = True
        for v, vcost in graph[u]:
            if depth[v] < depth[u] + vcost:
                continue
            depth[v] = depth[u] + vcost
            heappush(heap, (depth[v], v))
    if depth[to1d(n-1, 0)] == INFTY and depth[to1d(n-1, 1)] == INFTY:
        return -1
    else:
        return min(depth[to1d(n-1, 0)], depth[to1d(n-1, 1)])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
