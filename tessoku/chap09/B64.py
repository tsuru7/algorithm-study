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
    p = [-1 for _ in range(n)]
    heap = []
    depth[0] = 0
    heappush(heap, (0, 0))
    while len(heap) > 0:
        _, u = heappop(heap)
        if done[u]:
            continue
        done[u] = True
        for v, c in graph[u]:
            if depth[v] < depth[u] + c:
                continue
            p[v] = u
            depth[v] = depth[u] + c
            heappush(heap, (depth[v], v))
    # print(f'depth: {depth}')
    # print(f'p: {p}')
    path = []
    now = n-1
    while now != -1:
        path.append(now+1)
        now = p[now]
    return path[::-1]

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
