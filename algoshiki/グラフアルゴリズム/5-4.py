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
        graph[a].append(b)
        graph[b].append(a)
    return n,m,graph

BLACK = 0
WHITE = 1
def dfs(u, graph, color):
    result = True
    for v in graph[u]:
        if color[v] != -1:
            if color[v] == color[u]:
                result = False
            continue
        if color[u] == BLACK:
            color[v] = WHITE
        else:
            color[v] = BLACK
        result = dfs(v, graph, color) and result
    return result
    

def solve(n,m,graph):
    color = [-1 for _ in range(n)]
    ans=True
    for i in range(n):
        if color[i] == -1:
            color[i] = BLACK
            result = dfs(i, graph, color)
            ans = ans and result
    if ans:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
