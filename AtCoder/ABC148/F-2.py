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
    n,u,v=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,u,v,graph

def solve(n,u,v,graph):
    taka = u-1
    aoki = v-1

    if aoki in graph[taka]:
        return 0

    p = [-1 for _ in range(n)]
    depth = [-1 for _ in range(n)]
    queue = deque()
    queue.append(taka)
    depth[taka] = 0
    while len(queue) > 0:
        u = queue.popleft()
        if u == aoki:
            break
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            queue.append(v)
            p[v] = u
    # print(f'depth: {depth}')
    # print(f'depth[aoki]: {depth[aoki]}')
    # print(f'p: {p}')

    half_depth = depth[aoki] // 2

    # print(f'half_depth: {half_depth}')

    now = aoki
    for i in range(half_depth):
        now = p[now]
    depth = [-1 for _ in range(n)]
    depth[now] = INFTY

    # print(f'pnr: {now}')

    u = taka
    queue = deque()
    queue.append(u)
    depth[u] = 0
    taka_leaves = []
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            queue.append(v)
        if len(graph[u]) == 1:
            taka_leaves.append(u)

    # print(f'taka_leaves: {taka_leaves}')

    u = aoki
    depth = [-1 for _ in range(n)]
    queue = deque()
    queue.append(u)
    depth[u] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            queue.append(v)

    # print(f'depth(aoki): {depth}')

    maxdist = 0
    for u in taka_leaves:
        if maxdist < depth[u]:
            maxdist = depth[u]
    
    # print(f'maxdist: {maxdist}')

    # if (maxdist - taka_fardepth) % 2 == 1:
    #     return maxdist - 1
    # else:
    #     return maxdist

    return maxdist - 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,u,v,graph=readinput()
    ans=solve(n,u,v,graph)
    printans(ans)
