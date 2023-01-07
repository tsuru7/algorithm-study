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
    graph1 = [set() for _ in range(n)]
    graph0 = [set() for _ in range(n)]
    for _ in range(m):
        u, v, a = m_input()
        u -= 1
        v -= 1
        if a == 0:
            graph0[u].add(v)
            graph0[v].add(u)
        else:
            graph1[u].add(v)
            graph1[v].add(u)
    s = l_input()
    return n,m,k,graph0,graph1,s

def solve(n,m,k,graph0,graph1,s):
    visited0 = [False for _ in range(n)]
    visited1 = [False for _ in range(n)]
    depth0 = [INFTY for _ in range(n)]
    depth1 = [INFTY for _ in range(n)]
    s = set([s[i] - 1 for i in range(k)])
    queue = deque()
    queue.append((0, 1))   # 頂点:0, 通行状態:1
    visited1[0] = True
    depth1[0] = 0
    while len(queue) > 0:
        # print(f'queue: {queue}')
        u, st = queue.popleft()
        if st == 1:
            for v in graph1[u]:
                # if visited1[v]:
                #     continue
                if depth1[v] <= depth1[u] + 1:
                    continue
                queue.append((v, 1))
                visited1[v] = True
                depth1[v] = depth1[u] + 1
                if v in s:
                    if not visited0[v]:
                        queue.append((v, 0))
                        visited0[v] = True
                        depth0[v] = depth1[u] + 1
                    else:
                        if depth0[v] > depth1[u] + 1:
                            queue.append((v, 0))
                            depth0[v] = depth1[u] + 1
        else:
            for v in graph0[u]:
                # if visited0[v]:
                #     continue
                if depth0[v] <= depth0[u] + 1:
                    continue
                queue.append((v, 0))
                visited0[v] = True
                depth0[v] = depth0[u] + 1
                if v in s:
                    if not visited1[v]:
                        queue.append((v, 1))
                        visited1[v] = True
                        depth1[v] = depth0[u] + 1
                    else:
                        if depth1[v] > depth0[u] + 1:
                            queue.append((v, 1))
                            depth1[v] = depth0[u] + 1
    # print(f'depth0: {depth0}, depth1: {depth1}')
    if not visited0[n-1] and not visited1[n-1]:
        return -1
    return min(depth0[n-1], depth1[n-1])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,graph0,graph1,s=readinput()
    ans=solve(n,m,k,graph0,graph1,s)
    printans(ans)
