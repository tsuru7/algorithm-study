import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop

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
    a=l_input()
    graph = [set() for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].add(v)
        graph[v].add(u)
    return n,m,a,graph

def solve(n,m,a,graph):
    heap = []
    for i in range(n):
        heappush(heap, (-a[i], i))
    ans=0
    while len(heap) > 0:
        _, u = heappop(heap)
        sum = 0
        for v in graph[u]:
            sum += a[v]
            graph[v].remove(u)
        ans = max(ans, sum)
        
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,graph=readinput()
    ans=solve(n,m,a,graph)
    printans(ans)
