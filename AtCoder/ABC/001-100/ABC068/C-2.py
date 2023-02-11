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

def readinput():
    n,m=m_input()
    nlist = [[] for _ in range(n)]
    for _ in range(m):
        a,b = m_input()
        a -= 1
        b -= 1
        nlist[a].append(b)
        nlist[b].append(a)
    return n,m,nlist

def bfs(u, nlist):
    visited = [False]*len(nlist)
    depth = [-1]*len(nlist)
    queue = deque()
    queue.append(u)
    visited[u] = True
    depth[u] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in nlist[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                depth[v] = depth[u] + 1
                if v == n-1:
                    if depth[v] == 2:
                        return True
                    else:
                        return False
    return False


def main(n,m,nlist):
    if bfs(0, nlist):
        return 'POSSIBLE'
    else:
        return 'IMPOSSIBLE'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nlist=readinput()
    ans=main(n,m,nlist)
    printans(ans)
