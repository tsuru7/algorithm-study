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
    n=i_input()
    sx, sy, tx, ty = m_input()
    circles = [l_input() for _ in range(n)]
    return n,sx,sy,tx,ty,circles

def bfs(start, goal, graph):
    queue = deque()
    n = len(graph)
    visited = [False for _ in range(n)]
    queue.append(start)
    visited[start] = True
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if v == goal:
                return True
            if visited[v]:
                continue
            queue.append(v)
            visited[v] = True
    return False

def solve(n,sx,sy,tx,ty,circles):
    if n == 1:
        return 'Yes'
    for i in range(n):
        cx, cy, r = circles[i]
        if (sx-cx)**2+(sy-cy)**2 == r**2:
            start = i
        if (tx-cx)**2+(ty-cy)**2 == r**2:
            goal = i
    graph = [[] for _ in range(n)]
    for i in range(n):
        cix, ciy, ri = circles[i]
        for j in range(n):
            if i == j:
                continue
            cjx, cjy, rj = circles[j]
            if (ri-rj)**2 <= (cix-cjx)**2 + (ciy-cjy)**2 <= (ri+rj)**2:
                graph[i].append(j)
                graph[j].append(i)

    if bfs(start, goal, graph):
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,sx,sy,tx,ty,circles=readinput()
    ans=solve(n,sx,sy,tx,ty,circles)
    printans(ans)
