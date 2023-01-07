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
    x=l_input()
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    queries = [l_input() for _ in range(q)]
    return n,q,x,graph,queries

def solve(n,q,x,graph,queries):
    depth = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    seq = []
    queue = deque()
    queue.append(0)
    depth[0] = 0
    while len(queue) > 0:
        u = queue.popleft()
        seq.append(u)
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            queue.append(v)
            depth[v] = depth[u] + 1
            parent[v] = u
    # print(f'seq: {seq}')
    values = [[x[i]] for i in range(n)]
    # print(f'values: {values}')
    for u in seq[::-1]:
        tmp = values[u]
        for v in graph[u]:
            if v == parent[u]:
                continue
            tmp += values[v]
        tmp.sort(reverse=True)
        values[u] = tmp[:20]
        # print(f'u: {u}, values[u]: {values[u]}')
    # print(values)
    ans=[]
    for v, k in queries:
        v -= 1
        k -= 1
        ans.append(values[v][k])
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,q,x,graph,queries=readinput()
    ans=solve(n,q,x,graph,queries)
    printans(ans)
