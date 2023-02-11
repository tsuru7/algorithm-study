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
    n,m,k=m_input()
    graph0 = [[] for _ in range(n)]
    graph1 = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a = m_input()
        u -= 1
        v -= 1
        if a == 0:
            graph0[u].append(v)
            graph0[v].append(u)
        else:
            graph1[u].append(v)
            graph1[v].append(u)
    s=set([si-1 for si in l_input()])
    return n,m,k,graph0,graph1,s

def solve(n,m,k,graph0,graph1,s):

    queue = deque()
    visited0 = [False for _ in range(n)]
    visited1 = [False for _ in range(n)]
    depth0 = [INFTY for _ in range(n)]
    depth1 = [INFTY for _ in range(n)]
    queue.append((0, 1))
    visited1[0] = True
    depth1[0] = 0
    while len(queue) > 0:
        u, st = queue.popleft()
        if st == 1:
            for v in graph1[u]:
                if visited1[v]:
                    continue
                queue.append((v, 1))
                visited1[v] = True
                depth1[v] = depth1[u] + 1
            if u in s and not visited0[u]:
                visited0[u] = True
                queue.appendleft((u, 0))
                depth0[u] = depth1[u]
        else:
            for v in graph0[u]:
                if visited0[v]:
                    continue
                queue.append((v, 0))
                visited0[v] = True
                depth0[v] = depth0[u] + 1
            if u in s and not visited1[u]:
                visited1[u] = True
                queue.appendleft((u, 1))
                depth1[u] = depth0[u]

    if not visited0[n-1] and not visited1[n-1]:
        return -1
    else:
        return min(depth0[n-1], depth1[n-1])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,graph0,graph1,s=readinput()
    ans=solve(n,m,k,graph0,graph1,s)
    printans(ans)
