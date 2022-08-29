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
    r,c=m_input()
    sy, sx = m_input()
    sy -= 1
    sx -= 1
    gy, gx = m_input()
    gy -= 1
    gx -= 1
    cmap = [ input() for _ in range(r) ]
    return r,c,sy,sx,gy,gx,cmap

def solve(r,c,sy,sx,gy,gx,cmap):
    rc2ind = lambda row, col: row*c+col
    ind2rc = lambda x: divmod(x, c)

    queue = deque()
    visited = [-1]*(r*c)
    start = (sy, sx)
    goal = (gy, gx)
    u = start
    queue.append(u)
    visited[rc2ind(sy, sx)] = 0
    while len(queue) > 0:
        u = queue.popleft()
        if u == goal:
            break
        row = u[0]
        col = u[1]
        for dr,dc in [ (-1, 0), (+1, 0), (0, -1), (0, +1) ]:
            if 0 <= row+dr < r and 0 <= col+dc < c and cmap[row+dr][col+dc] == '.':
                if visited[rc2ind(row+dr,col+dc)] >= 0:
                    continue
                queue.append((row+dr, col+dc))
                visited[rc2ind(row+dr, col+dc)] = visited[rc2ind(row, col)] + 1
        # print(f'queue: {queue}, visited: {visited}')
    return visited[rc2ind(gy, gx)]

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,c,sy,sx,gy,gx,cmap=readinput()
    ans=solve(r,c,sy,sx,gy,gx,cmap)
    printans(ans)
