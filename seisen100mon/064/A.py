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
        s, t, w = m_input()
        graph[s].append((t, w))
        graph[t].append((s, w))
    return n,m,graph

def solve(n,m,graph):
    marked = [False for _ in range(n)]
    marked_count = 0
    queue = []

    marked[0] = True
    marked_count = 1
    for v, c in graph[0]:
        heappush(queue, (c, v))
    
    ans=0
    while marked_count < n:
        c, u = heappop(queue)
        if marked[u]:
            continue
        marked[u] = True
        marked_count += 1
        ans += c
        for v, c in graph[u]:
            if marked[v]:
                continue
            heappush(queue, (c, v))

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
