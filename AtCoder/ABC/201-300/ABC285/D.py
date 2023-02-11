import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    stList = []
    for _ in range(n):
        stList.append(input().split())
    return n,stList

def dfs(u, graph, visited):
    visited[u] = 1
    for v in graph[u]:
        if v in visited and visited[v] == 1:
            return True
        if v in visited and visited[v] == 2:
            continue
        if dfs(v, graph, visited):
            return True
    visited[u] = 2
    return False

def solve(n,stList):
    graph = dict()
    for s, t in stList:
        if s in graph:
            graph[s].append(t)
        else:
            graph[s] = [t]
        if t not in graph:
            graph[t] = []
    visited = dict()
    for i in range(n):
        if stList[i][0] in visited:
            continue
        flag = dfs(stList[i][0], graph, visited)
        if flag:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,stList=readinput()
    ans=solve(n,stList)
    printans(ans)
