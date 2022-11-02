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
    a=l_input()
    return n,a

def solve(n,a):
    graph = [[] for _ in range(2*n+2)]
    for i in range(1, n+1):
        ai = a[i-1]
        graph[ai].append(2*i)
        graph[ai].append(2*i+1)
    
    depth = [-1 for _ in range(2*n+2)]
    queue = deque()
    queue.append(1)
    depth[1] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            queue.append(v)
    return depth[1:]

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
