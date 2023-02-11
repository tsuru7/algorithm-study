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
    n,m,k=m_input()
    graph = [[] for _ in range(n*2)]
    for _ in range(m):
        u, v, a = m_input()
        u -= 1
        v -= 1
        graph[u*2+a].append((v*2+a, 1))
        graph[v*2+a].append((u*2+a, 1))
    s=l_input()
    for si in s:
        si -= 1
        graph[si*2].append((si*2+1, 0))
        graph[si*2+1].append((si*2, 0))
    return n,graph

def solve(n,graph):

    # print(f'graph: {graph}')

    heap = []
    depth = [INFTY for _ in range(2*n)]
    done = [False for _ in range(2*n)]
    heappush(heap, (0, 1))
    depth[1] = 0
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
    if depth[2*n-1] == INFTY and depth[2*n-2] == INFTY:
        return -1
    else:
        return min(depth[2*n-1], depth[2*n-2])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
