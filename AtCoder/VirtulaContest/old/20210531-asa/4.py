import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque
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
    n=i_input()
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, c = m_input()
        graph[a].append((b,c))
        graph[b].append((a,c))
    q, k = m_input()
    xylist = []
    for _ in range(q):
        xylist.append(l_input())
    return n,graph,q,k,xylist

def bfs(u, graph, depth):
    visited = [False]*len(graph)
    queue = deque()
    queue.append(u)
    visited[u] = True
    depth[u] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v, l in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            depth[v] = depth[u] + l
            queue.append(v)
    return depth

def main(n,graph,q,k,xylist):
    depth = [0]*(n+1)
    depth = bfs(k, graph, depth)
    ans=[]
    for x, y in xylist:
        ans.append(depth[x]+depth[y])
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,graph,q,k,xylist=readinput()
    ans=main(n,graph,q,k,xylist)
    printans(ans)
