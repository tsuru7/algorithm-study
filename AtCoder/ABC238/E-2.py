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
    n,q=m_input()
    graph = [ [] for _ in range(n+1) ]
    for _ in range(q):
        l, r = m_input()
        graph[l-1].append(r)
        graph[r].append(l-1)
    return n,q,graph

def solve(n,q,graph):
    queue = deque()
    visited = [False]*(n+1)
    u = 0
    visited[u] = True
    queue.append(u)
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            queue.append(v)
    if visited[n]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,q,graph=readinput()
    ans=solve(n,q,graph)
    printans(ans)
