import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heapify, heappush, heappop

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
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
    return n,m,graph

def solve(n,m,graph):
    in_deg = [0 for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            in_deg[j] += 1
    heap = []
    order = []
    for i in range(n):
        if in_deg[i] == 0:
            heappush(heap, i)
    while len(heap) > 0:
        u = heappop(heap)
        order.append(u)
        for v in graph[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                heappush(heap, v)
    if sum(in_deg) > 0:
        return [-1]
    else:
        return [x + 1 for x in order]

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
