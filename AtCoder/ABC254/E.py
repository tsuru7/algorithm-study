import sys
sys.setrecursionlimit(10**6)
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
    n,m=m_input()
    graph = [ [] for _ in range(n) ]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    q = i_input()
    queries = [ l_input() for _ in range(q) ]
    return n,m,graph,q,queries

def bfs(u, k, visited, depth):

    n = len(graph)
    # visited = [False]*n
    # depth = [0]*n
    cumsum = 0
    queue = deque()
    queue.append(u)
    apexes = []
    visited[u] = True
    apexes.append(u)
    while len(queue) > 0:
        u = queue.popleft()
        cumsum += u+1
        # print(f'u: {u}, depth[u]: {depth[u]}, cumsum: {cumsum}')
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            depth[v] = depth[u] + 1
            apexes.append(v)
            if depth[v] <= k:
                queue.append(v)
    for v in apexes:
        visited[v] = False
        depth[v] = 0
    return cumsum

def solve(n,m,graph,q,queries):

    visited = [False]*n
    depth = [0]*n
    # cumsums = []
    # for i in range(n):
    #     u = i
    #     cumsums.append(bfs(u))
    # # print(f'cumsums: {cumsums}')
    ans=[]
    for x, k in queries:
        x -= 1
        cumsum = bfs(x, k, visited, depth)
        ans.append(cumsum)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,graph,q,queries=readinput()
    ans=solve(n,m,graph,q,queries)
    printans(ans)
