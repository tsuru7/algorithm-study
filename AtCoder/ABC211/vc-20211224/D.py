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
    graph = [ [] for _ in range(n) ]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return n,m,graph

def main(n,m,graph):
    depth = [-1]*n
    queue = deque()
    queue.append(0)
    depth[0] = 0
    u = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            queue.append(v)
            depth[v] = depth[u] + 1
    if depth[n-1] < 0:
        return 0

    layers = [ set() for _ in range(depth[n-1]+1) ]
    for u in range(n):
        du = depth[u]
        if du >= depth[n-1]:
            continue
        layers[du].add(u)
    layers[depth[n-1]] = set([n-1])
    # print(f'layer: {layer}')
    MOD = 10**9+7
    path = [0]*n
    path[0] = 1
    for l in range(depth[n-1]):
        layer = layers[l]
        for u in layer:
            for v in graph[u]:
                if v in layers[l+1]:
                    path[v] = (path[v]+path[u]) % MOD

    return path[n-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=main(n,m,graph)
    printans(ans)
