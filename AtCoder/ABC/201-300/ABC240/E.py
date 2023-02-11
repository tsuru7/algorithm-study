import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    graph = [ [] for _ in range(n) ]
    for _ in range(n-1):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,graph

def dfs(u, graph, visited, segments, nseg):
    leaf = True
    left_most = nseg+1
    right_most = 0
    for v in graph[u]:
        if visited[v]:
            continue
        visited[v] = True
        leaf = False
        seg_, nseg = dfs(v, graph, visited, segments, nseg)
        left, right = seg_
        left_most = min(left_most, left)
        right_most = max(right_most, right)
    if leaf:
        nseg += 1
        segments[u] = [nseg, nseg]
    else:
        segments[u] = [left_most, right_most]

    return segments[u], nseg


def solve(n,graph):
    visited = [False]*n
    segments = [ [0, 0] for _ in range(n) ]
    u = 0
    visited[u] = True
    dfs(u, graph, visited, segments, 0)

    ans=[ segments[u] for u in range(n) ]
    return ans

def printans(ans):
    for segment in ans:
        print(*segment)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
