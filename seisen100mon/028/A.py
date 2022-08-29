import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

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
    for _ in range(n):
        tmp = l_input()
        u = tmp[0] - 1
        for i in range(tmp[1]):
            graph[u].append(tmp[i+2]-1)
    return n,graph

def solve(n,graph):
    depth = [-1]*n
    queue = deque()
    u = 0
    queue.append(u)
    depth[u] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] != -1:
                continue
            queue.append(v)
            depth[v] = depth[u] + 1
    ans=[]
    for i in range(n):
        ans.append((i+1, depth[i]))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
