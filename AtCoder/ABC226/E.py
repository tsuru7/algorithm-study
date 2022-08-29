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
    graph = []
    for _ in range(n):
        graph.append([])
    for i in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,graph

def main(n,m,graph):
    ans=0
    for i in range(n):
        if len(graph[i]) == 1:
            graph[i] = []
    ans = bfs(0, graph)
    return ans

def bfs(u, graph):
    # print(f'graph: {graph}')
    MOD = 998244353
    queue = deque()
    n = len(graph)
    visited = [False]*n
    ans = 0
    queue.append(u)
    visited[u] = True
    while len(queue) > 0:
        u = queue.popleft()
        visited_count = 0
        unvisited_count = 0
        for v in graph[u]:
            if visited[v]:
                visited_count += 1
            else:
                unvisited_count += 1
                queue.append(v)
                visited[v] = True
        ans += visited_count * unvisited_count
        ans = ans % MOD
    return ans


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=main(n,m,graph)
    printans(ans)
