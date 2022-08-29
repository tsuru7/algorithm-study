import sys
# sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

n, m = m_input()
graph = [ [] for _ in range(n) ]
for _ in range(m):
    a, b = m_input()
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
q = i_input()
ans = []
depth = [-1]*n
for _ in range(q):
    queue = deque()
    x, k = m_input()
    x -= 1
# def bfs(u, k):
    tmp = 0
    visited = []
    queue.append(x)
    tmp += x+1
    # print(f'depth: {depth}')
    depth[x] = 0
    visited.append(x)
    while len(queue) > 0:
        u = queue.popleft()
        if depth[u] == k:
            break
        for v in graph[u]:
            if depth[v] < 0:
                depth[v] = depth[u] + 1
                visited.append(v)
                queue.append(v)
                tmp += v+1
    ans.append(tmp)
    for v in visited:
        depth[v] = -1


print(*ans)


