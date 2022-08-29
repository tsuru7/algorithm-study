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
    queue.append(n)
    depth[n] = 0
    while len(queue) > 0:
        # print(f'queue: {queue}')
        u = queue.popleft()
        if u % a == 0:
            v = u // a
            if v not in depth:
                queue.append(v)
                depth[v] = depth[u] + 1
                if v == 1:
                    return depth[v]
        ustr = str(u)
        if len(ustr) > 1 and ustr[1] == '0':
            continue
        v = int(ustr[1:]+ustr[0])
        if v not in depth:
            queue.append(v)
            depth[v] = depth[u] + 1
            if v == 1:
                return depth[v]
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,n=readinput()
    ans=solve(a,n)
    printans(ans)
