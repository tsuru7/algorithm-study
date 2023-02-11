import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations
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
    m=i_input()
    graph = []
    for _ in range(9):
        graph.append([])
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    plist = l_input()
    start = ['0']*9
    for j in range(8):
        pj = plist[j]-1
        start[pj] = str(j+1)
    start = ''.join(start)
    return m,graph,start

def main(m,graph,start):
    # print(f'start: {start}')
    states = permutations('012345678')
    nList = dict()
    visited = dict()
    for state in states:
        # print(f'state: {state}')
        key = ''.join(state)
        nList[key] = []
        visited[key] = False
        izero = state.index('0')
        for v in graph[izero]:
            tmp = list(state)
            tmp[izero] = tmp[v]
            tmp[v] = '0'
            vkey = ''.join(tmp)
            nList[key].append(vkey)
    
    # print(f'nList[start]: {nList[start]}')

    ans=bfs(start, nList, visited)
    return ans

def bfs(start, nList, visited):
    queue = deque()
    depth = dict()
    u = start
    count = -1
    depth[u] = 0
    queue.append(u)
    visited[u] = True
    goal = '123456780'
    while len(queue) > 0:
        # print(f'queue: {queue}')
        u = queue.popleft()
        count += 1
        if u == goal:
            return depth[u]
        for v in nList[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                depth[v] = depth[u] + 1
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    m,graph,start=readinput()
    ans=main(m,graph,start)
    printans(ans)
