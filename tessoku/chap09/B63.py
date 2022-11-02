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
    sy,sx=m_input()
    gy,gx=m_input()
    cmap = [input() for _ in range(r)]
    return r,c,sy,sx,gy,gx,cmap

def solve(r,c,sy,sx,gy,gx,cmap):
    def to1d(row, col):
        return row * c + col
    depth = [-1 for _ in range(r*c)]
    queue = deque()
    queue.append((sy-1,sx-1))
    depth[(sy-1)*c + sx-1] = 0
    while len(queue) > 0:
        ur, uc = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vr = ur+dr
            vc = uc+dc
            if 0 <= vr < r and 0 <= vc < c and cmap[vr][vc] == '.':
                if depth[to1d(vr, vc)] >= 0:
                    continue
                depth[to1d(vr, vc)] = depth[to1d(ur,uc)] + 1
                queue.append((vr, vc))
    return depth[to1d(gy-1, gx-1)]

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,c,sy,sx,gy,gx,cmap=readinput()
    ans=solve(r,c,sy,sx,gy,gx,cmap)
    printans(ans)
