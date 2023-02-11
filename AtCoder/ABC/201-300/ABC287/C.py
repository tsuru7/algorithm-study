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
    n,m=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,graph

class Graph:
    def __init__(self, graph, directed=False):
        self.graph = graph
        self.n = len(graph)
        self.directed = directed
        self.visited = [-1 for _ in range(self.n)]
        self.parent = [-1 for _ in range(self.n)]
        self.cycle = False
        self.nsegment = 0
        return
    
    def dfsAll(self):
        for i in range(self.n):
            if self.visited[i] == -1:
                self.dfs(i)
                self.nsegment += 1
        return

    def dfs(self, u):
        self.visited[u] = 1
        for v in graph[u]:
            if not self.directed and v == self.parent[u]:
                continue
            if self.visited[v] == 1:
                self.cycle = True
                continue
            if self.visited[v] == -1:
                self.parent[v] = u
                self.dfs(v)
        self.visited[u] = 2
        return

    def isConnected(self):
        return self.nsegment == 1
    
    def hasCycle(self):
        return self.cycle
    
    def getDegreeList(self):
        return [len(graph[i]) for i in range(self.n)]
    
    def getInDegreeList(self):
        inDegree = [0 for _ in range(self.n)]
        for i in range(self.n):
            for j in graph[i]:
                inDegree[j] += 1
        return inDegree
    
    def getOutDegreeList(self):
        return self.getDegreeList()


def solve(n,m,graph):
    G = Graph(graph)
    G.dfsAll()
    if not G.isConnected():
        return 'No'
    if G.hasCycle():
        return 'No'
    degree = G.getDegreeList()
    if max(degree) > 2:
        return 'No'

    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
