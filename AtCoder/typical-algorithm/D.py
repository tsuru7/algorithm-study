import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from heapq import heappush, heappop

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,m=m_input()
    nlist = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = m_input()
        nlist[u].append((c, v))
    return n,m,nlist

def dijkstra(u, nlist):
    visited = [False]*len(nlist)
    dist = [-1]*len(nlist)
    done = [False]*len(nlist)
    heap = []
    dist[0] = 0
    visited[0] = True
    heappush(heap, (0, 0))
    while len(heap) > 0:
        cu, u = heappop(heap)
        if done[u]:
            continue

        done[u] = True

        for cv, v in nlist[u]:
            if not visited[v] or dist[v] > dist[u] + cv:
                heappush(heap, (dist[u]+cv, v))
                visited[v] = True
                dist[v] = dist[u]+cv

    return dist[n-1]

def main(n,m,nlist):
    return dijkstra(0,nlist)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nlist=readinput()
    ans=main(n,m,nlist)
    printans(ans)
