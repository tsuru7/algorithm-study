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
    graph = [ [] for _ in range(n) ]
    for _ in range(m):
        x, y = m_input()
        x -= 1
        y -= 1
        graph[x].append(y)
    return n,m,graph

def dfs(u, graph, pathlen):
    if pathlen[u] != -1:
        return pathlen[u]

    if len(graph[u]) == 0:
        pathlen[u] = 0
        return pathlen[u]
    path = 0
    for v in graph[u]:
        path = max(path, dfs(v, graph, pathlen))
    pathlen[u] = path + 1
    return pathlen[u]

def solve(n,m,graph):
    pathlen = [-1]*n
    inorder = [0]*n
    for x in range(n):
        for y in graph[x]:
            inorder[y] += 1
    
    ans=0
    for x in range(n):
        if inorder[x] == 0:
            path = dfs(x, graph, pathlen)
            ans = max(ans, path)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
