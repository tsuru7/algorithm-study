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
    graph = [ [] for _ in range(n) ]
    for i in range(1, n):
        b = i_input()
        b -= 1
        graph[b].append(i)
    return n,graph

def dfs(u, graph):
    if len(graph[u]) == 0:
        return 1
    tmp = []
    for v in graph[u]:
        tmp.append(dfs(v, graph))
    return max(tmp) + min(tmp) + 1

def solve(n,graph):
    ans=dfs(0, graph)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
