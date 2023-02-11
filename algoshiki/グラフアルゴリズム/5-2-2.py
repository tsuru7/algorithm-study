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
    n,m,s,t=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        graph[a].append(b)
    return n,m,s,t,graph

def solve(n,m,s,t,graph):
    visited = [False for _ in range(n)]
    stack = []
    parent = [-1 for _ in range(n)]
    u = s
    stack.append(~u)
    stack.append(u)
    while len(stack) > 0:
        u = stack.pop()
        if u >= 0:
            if visited[u]:
                stack.pop()
                continue
            visited[u] = True
            for v in graph[u]:
                if visited[v]:
                    continue
                stack.append(~v)
                stack.append(v)
                parent[v] = u
        else:
            pass
    path = []
    now = t
    while now != -1:
        path.append(now)
        now = parent[now]
    path.reverse()
    return path

def printans(ans):
    print(len(ans))
    print(*ans)

if __name__=='__main__':
    n,m,s,t,graph=readinput()
    ans=solve(n,m,s,t,graph)
    printans(ans)
