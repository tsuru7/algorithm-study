import sys
sys.setrecursionlimit(10**5)
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
    nList = []
    for _ in range(n):
        nList.append([])
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        nList[a].append(b)
        nList[b].append(a)
    return n,nList

def bfs(u, nList):
    n = len(nList)
    d = [0]*n
    visited = [False]*n
    queue = deque()
    visited[u] = True
    queue.append(u)
    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                queue.append(v)
    return d

def main(n,nList):
    d = bfs(0, nList)
    if d[n-1] == 2:
        return 'POSSIBLE'
    else:
        return 'IMPOSSIBLE'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,nList=readinput()
    ans=main(n,nList)
    printans(ans)
