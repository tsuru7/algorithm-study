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
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,graph

def dfs(u, graph, visited, l_list, r_list, next_leaf):
    visited[u] = True
    l_min = n
    r_max = 1
    num_children = 0
    for v in graph[u]:
        if visited[v]:
            continue
        next_leaf = dfs(v, graph, visited, l_list, r_list, next_leaf)
        l_min = min(l_min, l_list[v])
        r_max = max(r_max, r_list[v])
        num_children += 1
    if num_children:
        l_list[u] = l_min
        r_list[u] = r_max
    else:
        l_list[u] = next_leaf
        r_list[u] = next_leaf
        next_leaf += 1
    return next_leaf

def solve(n,graph):
    visited = [False for _ in range(n)]
    l_list = [0 for _ in range(n)]
    r_list = [0 for _ in range(n)]
    _ = dfs(0, graph, visited, l_list, r_list, 1)
    ans=[(l_list[i], r_list[i]) for i in range(n)]
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
