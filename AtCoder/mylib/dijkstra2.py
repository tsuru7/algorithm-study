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
    return n,m,graph

def dijkstra(s, graph):
    queue = []
    u = s
    depth = [INFTY for _ in range(n)]
    done = [False for _ in range(n)]
    heappush(queue, (0, u))
    depth[u] = 0
    while len(queue) > 0:
        _, u = heappop(queue)
        if done[u]:
            continue
        done[u] = True
        for v, cv in graph[u]:
            if depth[v] > depth[u] + cv:
                depth[v] = depth[u] + cv
                heappush(queue, (depth[v], v))
    return depth

def solve(n,m,graph):
    depth1 = dijkstra(0, graph)
    depthn = dijkstra(n-1, graph)

    ans=[]
    for i in range(n):
        ans.append(depth1[i]+depthn[i])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
