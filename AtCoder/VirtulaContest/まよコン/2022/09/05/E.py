from email.policy import default
import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque
from collections import defaultdict

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
    m=i_input()
    graph = [[] for _ in range(9)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    p = l_input()
    return m,graph,p

def swap(ustate, u, v):
    ulist = list(ustate)
    ulist[u], ulist[v] = ulist[v], ulist[u]
    return ''.join(ulist)

def solve(m,graph,p):
    start = ['0' for _ in range(9)]
    for i in range(8):
        pi = p[i]
        start[pi-1] = str(i+1)
    start = ''.join(start)
    # print(f'p: {p}, start: {start}')
    goal = '123456780'
    queue = deque()
    visited = set()
    depth = defaultdict(int)
    queue.append(start)
    visited.add(start)
    depth[start] = 0
    while len(queue) > 0:
        # print(f'queue: {queue}')
        ustate = queue.popleft()
        if ustate == goal:
            return depth[ustate]
        u = ustate.index('0')
        for v in graph[u]:
            vstate = swap(ustate, u, v)
            if vstate in visited:
                continue
            visited.add(vstate)
            depth[vstate] = depth[ustate] + 1
            queue.append(vstate)
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    m,graph,p=readinput()
    ans=solve(m,graph,p)
    printans(ans)
