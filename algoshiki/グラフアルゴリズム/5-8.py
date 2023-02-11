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
    return n,m,graph

WHITE = 0 # 未訪問
GRAY = 1  # 処理中
BLACK = 2 # 処理完了
def dfs(u, graph, color):
    # DFSしながらサイクルを検出したら True を返す
    color[u] = GRAY
    for v in graph[u]:
        if color[v] == GRAY:
            return True
        elif color[v] == BLACK:
            continue
        if dfs(v, graph, color):
            return True
    color[u] = BLACK
    return False

def solve(n,m,graph):
    color = [WHITE for _ in range(n)]
    for i in range(n):
        if color[i] == WHITE:
            loop = dfs(i, graph, color)
            if loop:
                return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
