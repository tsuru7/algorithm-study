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

smap = None
def readinput():
    global smap

    n=i_input()
    ax, ay = m_input()
    bx, by = m_input()
    smap = [ input() for _ in range(n) ]
    return n,ax,ay,bx,by

depth = None
def bfs(start, goal):
    global visited
    global depth
    global smap

    # print(f'start: {start}')
    # print(f'goal: {goal}')
    n = len(smap)
    queue = deque()
    depth = [ [0]*n for _ in range(n) ]
    row, col = start
    visited[row][col] = True
    queue.append(start)
    while len(queue) > 0:
        # print(f'queue: {queue}')
        urow, ucol = queue.popleft()
        if (urow, ucol) == goal:
            return depth[urow][ucol]

        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:

            vrow = urow+dr
            vcol = ucol+dc
            while 0 <= vrow < n and 0 <= vcol < n:
                if not visited[vrow][vcol]:
                    if smap[vrow][vcol] == '.':
                        queue.append((vrow, vcol))
                        visited[vrow][vcol] = True
                        depth[vrow][vcol] = depth[urow][ucol]+1
                    else:
                        break
                vrow += dr
                vcol += dc
                # print(f'queue1: {queue}')

        
        
    return -1

visited = None
def solve(n,ax,ay,bx,by):
    global visited

    visited = [ [False]*n for _ in range(n) ]
    start = (ax-1, ay-1)
    goal = (bx-1, by-1)
    ans = bfs(start, goal)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ax,ay,bx,by=readinput()
    ans=solve(n,ax,ay,bx,by)
    printans(ans)
