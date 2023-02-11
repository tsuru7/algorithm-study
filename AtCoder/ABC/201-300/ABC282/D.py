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
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,graph

def nextcolor(c):
    if c == 1:
        return 2
    else:
        return 1

def solve(n,m,graph):
    renketsu = []
    ans=0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i] == 0:
            nedge = 0
            napex = 0
            u = i
            queue = deque()
            queue.append(u)
            visited[u] = 1  # color = 1
            ncolor1 = 1
            ncolor2 = 0
            while len(queue):
                u = queue.popleft()
                napex += 1
                for v in graph[u]:
                    nedge += 1
                    if visited[v] == 0:
                        visited[v] = nextcolor(visited[u])
                        if visited[v] == 1:
                            ncolor1 += 1
                        else:
                            ncolor2 += 1
                        queue.append(v)
                    else:
                        if visited[v] == visited[u]:  # 二部グラフではない
                            return 0
            renketsu.append(napex)
            # print(f'ncolor1: {ncolor1}, ncolor2: {ncolor2}, nedge: {nedge}, napex: {napex}')
            ans += ncolor1 * ncolor2 - nedge // 2
    ans2 = 0
    for x in renketsu:
        ans2 += x * (n-x)
                   
    return ans + ans2 // 2

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
