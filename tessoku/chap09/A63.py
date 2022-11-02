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
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,graph

def solve(n,graph):
    queue = deque()
    depth = [-1 for _ in range(n)]
    queue.append(0)
    depth[0] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            queue.append(v)
    return depth

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
