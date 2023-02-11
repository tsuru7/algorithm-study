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
    n,x,y=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,x,y,graph

def solve(n,x,y,graph):
    x -= 1
    y -= 1
    queue = deque()
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    queue.append(x)
    visited[x] = True
    parent[x] = -1
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            parent[v] = u
            queue.append(v)

    # print(f'parent: {parent}')

    path = [y+1]
    next = parent[y]
    while next != -1:
        path.append(next+1)
        next = parent[next]

    ans=path[::-1]
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,x,y,graph=readinput()
    ans=solve(n,x,y,graph)
    printans(ans)
