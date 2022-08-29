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
    n,k=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,k,graph

def solve(n,k,graph):
    MOD = 10**9+7
    queue = deque()
    color = [-1 for _ in range(n)]
    u = 0
    queue.append(u)
    color[0] = k
    while len(queue) > 0:
        u = queue.popleft()
        gp = 0
        for v in graph[u]:
            if color[v] > 0:
                gp += 1
        used = 1 + gp
        for v in graph[u]:
            if color[v] >= 0:
                continue
            color[v] = max(0, k - used)
            used += 1
            queue.append(v)
    ans=1
    for i in range(n):
        ans *= color[i]
        ans %= MOD
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,graph=readinput()
    ans=solve(n,k,graph)
    printans(ans)
