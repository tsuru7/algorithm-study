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
    # graph[u]: 頂点 u を終点とする辺の始点のリスト
    graph = [[] for _ in range(n)]
    # deg_o[u]: 頂点 u の出次数
    deg_o = [0 for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        graph[b].append(a)
        deg_o[a] += 1
    for i in range(n):
        graph[i].sort()
    return n,m,graph,deg_o

def solve(n,m,graph,deg_o):
    queue = deque()
    order = []
    # 出次数が 0 の頂点をキューに入れる
    for i in range(n):
        if deg_o[i] == 0:
            queue.append(i)
    while len(queue) > 0:
        # キューに入っているのはトポロジカルソートの終点候補
        u = queue.popleft()
        order.append(u)
        # キューから取り出した頂点 u を終点とする辺を削除し、削除した辺の始点の出次数も減算する
        for v in graph[u]:
            deg_o[v] -= 1
            # 出次数が 0 になったらキューへ入れる
            if deg_o[v] == 0:
                queue.append(v)
    order.reverse()
    return order

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,graph,deg_o=readinput()
    ans=solve(n,m,graph,deg_o)
    printans(ans)
