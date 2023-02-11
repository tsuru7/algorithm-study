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
        graph[a].append(b)
        graph[b].append(a)
    return n,m,graph

def solve(n,m,graph):
    BLACK = 0
    WHITE = 1
    color = [-1 for _ in range(n)]
    queue = deque()
    for i in range(n):
        if color[i] == -1:
            queue.append(i)
            color[i] = BLACK
            while len(queue) > 0:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] != -1:
                        if color[v] == color[u]:
                            return 'No'
                    else:
                        color[v] = BLACK if color[u] == WHITE else WHITE
                        queue.append(v)
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
