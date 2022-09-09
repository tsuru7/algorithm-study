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
    n,m=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,graph

def dfs(u, graph, visited, parent):
    cycle = 0
    visited[u] = 1
    for v in graph[u]:
        if parent[u] == v:
            continue
        if visited[v] == 2:
            continue
        if visited[v] == 1:
            cycle += 1
            continue
        parent[v] = u
        cycle += dfs(v, graph, visited, parent)
    visited[u] = 2
    # print(f'u: {u}, cycle: {cycle}')
    return cycle

def solve(n,m,graph):
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    loop = []
    for i in range(n):
        connected = sum(visited)//2
        # print(f'visited: {visited}')
        if visited[i] == 0:
            loop.append(dfs(i, graph, visited, parent))
            if sum(visited)//2 - connected == 2:
                loop.append(2)
    # print(f'loop: {loop}')
    ans=1
    MOD = 998244353
    for l in loop:
        if l > 1:
            return 0
        ans *= 2
        ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
