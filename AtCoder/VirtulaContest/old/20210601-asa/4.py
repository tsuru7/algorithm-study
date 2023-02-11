import sys
sys.setrecursionlimit(10**5)
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
        graph[b].append(a)
    return n,m,graph

def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)


def main(n,m,graph):
    visited = [False]*n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, graph, visited)
    return count - 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=main(n,m,graph)
    printans(ans)
