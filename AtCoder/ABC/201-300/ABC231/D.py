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
    n,m=m_input()
    ablist = []
    for _ in range(m):
        ablist.append(l_input())
    return n,m,ablist

def main(n,m,ablist):
    graph = [ [] for _ in range(n) ]
    for a, b in ablist:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    visited = [False]*n
    for i in range(n):
        if len(graph[i]) > 2:
            return 'No'
        if visited[i]:
            continue
        if isCyclic(i, graph, visited):
            return 'No'
    return 'Yes'

def isCyclic(i, graph, visited):
    queue = deque()
    u = i
    queue.append(u)
    visited[u] = True
    while len(queue) > 0:
        u = queue.popleft()
        visited_count = 0
        for v in graph[u]:
            if visited[v]:
                visited_count += 1
                continue
            queue.append(v)
            visited[v] = True
        if visited_count == 2:
            return True
    return False


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,ablist=readinput()
    ans=main(n,m,ablist)
    printans(ans)
