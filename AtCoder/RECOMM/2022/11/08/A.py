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
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,graph

def solve(n,graph):
    queue = deque()
    order = []
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    leaf = [False for _ in range(n)]
    l_list = [0 for _ in range(n)]
    r_list = [0 for _ in range(n)]
    queue.append(0)
    order.append(0)
    visited[0] = True
    while len(queue) > 0:
        u = queue.popleft()
        count = 0
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            parent[v] = u
            queue.append(v)
            order.append(v)
            count += 1
        if count == 0:
            leaf[u] = True
    num = 1
    for u in order[::-1]:
        # print(f'u: {u}')
        # print(f'l_list: {l_list}')
        # print(f'r_list: {r_list}')
        if leaf[u]:
            l_list[u] = num
            r_list[u] = num
            num += 1
            continue
        l_min = n
        r_max = 1
        for v in graph[u]:
            # print(f'v: {v}')
            if v == parent[u]:
                continue
            l_min = min(l_min, l_list[v])
            r_max = max(r_max, r_list[v])
        l_list[u] = l_min
        r_list[u] = r_max
    # print(f'l_list: {l_list}')
    # print(f'r_list: {r_list}')

    ans=[(l_list[i], r_list[i]) for i in range(n)]
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
