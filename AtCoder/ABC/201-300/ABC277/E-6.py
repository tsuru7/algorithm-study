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
    n,m,k=m_input()
    # graph0 = [[] for _ in range(n)]
    # graph1 = [[] for _ in range(n)]
    graph = [[[] for _ in range(n)] for _ in range(2)]

    for _ in range(m):
        u, v, a = m_input()
        u -= 1
        v -= 1
        graph[a][u].append(v)
        graph[a][v].append(u)
    s=set([si-1 for si in l_input()])
    return n,m,k,graph,s

def solve(n,m,k,graph,s):

    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(2)]
    depth = [[INFTY for _ in range(n)] for _ in range(2)]
    queue.append((0, 1))
    visited[1][0] = True
    depth[1][0] = 0
    while len(queue) > 0:
        u, st = queue.popleft()
        for v in graph[st][u]:
            if visited[st][v]:
                continue
            queue.append((v, st))
            visited[st][v] = True
            depth[st][v] = depth[st][u] + 1
        if u in s and not visited[(st+1)%2][u]:
            queue.appendleft((u,(st+1)%2))
            depth[(st+1)%2][u] = depth[st][u]

    ans = min(depth[0][n-1], depth[1][n-1])
    if ans == INFTY:
        ans = -1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,graph,s=readinput()
    ans=solve(n,m,k,graph,s)
    printans(ans)
