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
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
    return n,m,graph

def dfs(u, graph, visited, finished, order):
    visited[u] = True
    for v in graph[u]:
        if visited[v] and not finished[v]:
            return
        elif visited[v]:
            continue
        dfs(v, graph, visited, finished, order)
    order.append(u)
    finished[u] = True
    return


def solve(n,m,graph):
    for i in range(n):
        graph[i].sort()
    visited = [False for _ in range(n)]
    finished = [False for _ in range(n)]
    order = []
    for i in range(n)[::-1]:
        if visited[i]:
            continue
        dfs(i, graph, visited, finished, order)
    # print(f'finished: {finished}')
    if sum(finished) < n:
        return [-1]
    else:
        ans = [x + 1 for x in order[::-1]]
        return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
