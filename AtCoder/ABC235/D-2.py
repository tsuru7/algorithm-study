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
    a,n=m_input()
    return a,n

def solve(a,n):
    depth = dict()
    queue = deque()
    queue.append(1)
    depth[1] = 0
    while len(queue) > 0:
        # print(f'queue: {queue}')
        u = queue.popleft()
        if u*a <= n*10:
            v = u * a
            if v not in depth:
                queue.append(v)
                depth[v] = depth[u] + 1
                if v == n:
                    return depth[v]
        if u % 10 == 0:
            continue
        ustr = str(u)
        v = int(ustr[-1]+ustr[:-1])
        if v not in depth:
            queue.append(v)
            depth[v] = depth[u] + 1
            if v == n:
                return depth[v]
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,n=readinput()
    ans=solve(a,n)
    printans(ans)
