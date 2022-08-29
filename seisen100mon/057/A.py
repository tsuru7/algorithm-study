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
    n,k=m_input()
    queries = [l_input() for _ in range(k)]
    return n,k,queries

def daiku(s, t, graph):
    n = len(graph)
    dist = [INFTY for _ in range(n)]
    visited = [False for _ in range(n)]
    heap = []
    heappush(heap, (0, s))
    dist[s] = 0
    while len(heap) > 0:
        du, u = heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, dv in graph[u].items():
            if not visited[v] and dist[v] > du + dv:
                dist[v] = du + dv
                heappush(heap, (du+dv, v))
    if dist[t] == INFTY:
        return -1
    else:
        return dist[t]

def solve(n,k,queries):
    graph = [dict() for _ in range(n)]
    ans=[]
    for query in queries:
        if query[0] == 1:
            c, d, e = query[1:]
            c -= 1
            d -= 1
            if d in graph[c] and graph[c][d] < e:
                continue
            else:
                graph[c][d] = e
                graph[d][c] = e
        else:
            a, b = query[1:]
            a -= 1
            b -= 1
            ans.append(daiku(a, b, graph))

    
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,k,queries=readinput()
    ans=solve(n,k,queries)
    printans(ans)
