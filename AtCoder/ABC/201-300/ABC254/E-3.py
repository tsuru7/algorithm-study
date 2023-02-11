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

def bfs(x, k, graph):
    ans = 0
    queue = deque()
    depth = dict()
    queue.append(x)
    depth[x] = 0
    while len(queue) > 0:
        u = queue.popleft()
        ans += u+1
        for v in graph[u]:
            if v in depth:
                continue
            depth[v] = depth[u] + 1
            if depth[v] <= k:
                queue.append(v)
    return ans

def solve(n,m,graph,q,queries):
    ans=[]
    for x, k in queries:
        x -= 1
        ans.append(bfs(x, k, graph))

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,graph,q,queries=readinput()
    ans=solve(n,m,graph,q,queries)
    printans(ans)
