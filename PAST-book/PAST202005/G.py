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
    n,x,y=m_input()
    blocks = [ l_input() for _ in range(n) ]
    return n,x,y,blocks

def solve(n,x,y,blocks):
    start = (0, 0)
    goal = (x, y)
    queue = deque()
    visited = {}
    visited[start] = 0
    queue.append(start)
    while len(queue) > 0:
        ux, uy = queue.popleft()
        for vx, vy in [ (ux+1, uy+1), (ux, uy+1), (ux-1, uy+1), (ux+1, uy), (ux-1, uy), (ux, uy-1)]:
            if (vx, vy) in visited:
                continue
            if [vx, vy] in blocks:
                continue
            if vx < -201 or 201 < vx or vy < -201 or 201 < vy:
                continue
            queue.append((vx, vy))
            visited[(vx, vy)] = visited[(ux, uy)] + 1
            if (vx, vy) == goal:
                return visited[(vx, vy)]
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,blocks=readinput()
    ans=solve(n,x,y,blocks)
    printans(ans)
