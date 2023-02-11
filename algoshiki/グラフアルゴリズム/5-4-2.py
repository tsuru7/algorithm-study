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

def solve(n,m,graph):
    color = [-1 for _ in range(n)]
    WHITE = 0
    BLACK = 1
    stack = []
    for i in range(n):
        if color[i] != -1:
            continue
        u = i
        stack.append(~u)
        stack.append(u)
        current = WHITE
        while len(stack) > 0:
            u = stack.pop()
            if u >= 0:
                if color[u] != -1:
                    stack.pop()
                    continue
                color[u] = current
                for v in graph[u]:
                    if color[v] != -1:
                        if color[v] == current:
                            return 'No'
                    stack.append(~v)
                    stack.append(v)
                current = 1 - current
            else:
                current = 1 - current
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
