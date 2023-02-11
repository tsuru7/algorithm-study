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

def solve(n,m,graph):
    stack = []
    WHITE = 0
    GRAY = 1
    BLACK = 2
    visited = [WHITE for _ in range(n)]
    for i in range(n):
        if visited[i] != WHITE:
            continue
        u = i
        stack.append(~u)
        stack.append(u)
        while len(stack) > 0:
            u = stack.pop()
            if u >= 0:
                if visited[u] == BLACK:
                    stack.pop()
                    continue
                visited[u] = GRAY
                for v in graph[u]:
                    if visited[v] == GRAY:
                        return 'Yes'
                    if visited[v] == BLACK:
                        continue
                    stack.append(~v)
                    stack.append(v)
            else:
                visited[~u] = BLACK
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
