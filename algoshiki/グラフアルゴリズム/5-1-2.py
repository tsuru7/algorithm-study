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
    n,m,s,t=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        graph[a].append(b)
    return n,m,s,t,graph

def solve(n,m,s,t,graph):
    visited = [False for _ in range(n)]
    queue = deque()
    queue.append(s)
    visited[s] = True
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    if visited[t]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,s,t,graph=readinput()
    ans=solve(n,m,s,t,graph)
    printans(ans)
