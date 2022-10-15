import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

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
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, c = m_input()
        graph[a].append((b, c, i+1))
    e=l_input()

    print(*graph, sep='\n')

    return n,m,k,graph,e

def dijkstra(s, graph, e):
    queue = []
    u = s
    depth = [INFTY for _ in range(n)]
    done = [False for _ in range(n)]
    heappush(queue, (0, u, 0))
    depth[u] = 0
    while len(queue) > 0:
        print(f'queue: {queue}')
        du, u, eu = heappop(queue)
        if done[u]:
            continue
        done[u] = True
        for v, cv, ev in graph[u]:
            print(f'v: {v}, cv: {cv}, ev: {ev}, depth[v]: {depth[v]}, depth[u]: {depth[u]}')
            if depth[v] > depth[u] + cv:
                try:
                    idx = e[ev:].index(ev)
                except ValueError:
                    print('VE')
                    continue
                depth[v] = depth[u] + cv
                heappush(queue, (depth[v], v, idx+1))
    return depth


def solve(n,m,k,graph,e):
    # for i in range(k):
    #     e[i] -= 1
    
    graph[0] = [(1, 0, 0)]
    depth = dijkstra(1, graph, e)
    if depth[n-1] == INFTY:
        return -1
    else:
        return depth[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,graph,e=readinput()
    ans=solve(n,m,k,graph,e)
    printans(ans)
