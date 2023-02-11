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
    h,w=m_input()
    cmap = [input() for _ in range(h)]
    return h,w,cmap

def solve(h,w,cmap):
    def to1d(row, col):
        return row * w + col

    for row in range(h):
        for col in range(w):
            if cmap[row][col] == 'S':
                srow = row
                scol = col

    for sr, sc in [(srow-1, scol), (srow+1, scol), (srow, scol-1), (srow, scol+1)]:
        if not (0 <= sr < h and 0 <= sc < w and cmap[sr][sc] == '.'):
            continue
        queue = deque()
        visited = [-1 for _ in range(h*w)]
        queue.append((sr, sc))
        visited[to1d(sr, sc)] = 0
        while len(queue) > 0:
            ur, uc = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                vr = ur + dr
                vc = uc + dc
                if 0 <= vr < h and 0 <= vc < w and cmap[vr][vc] == '.' and visited[to1d(vr, vc)] == -1:
                    visited[to1d(vr, vc)] = visited[to1d(ur, uc)] + 1
                    queue.append((vr, vc))
        for r, c in [(srow-1, scol), (srow+1, scol), (srow, scol-1), (srow, scol+1)]:
            if 0 <= r < h and 0 <= c < w and visited[to1d(r, c)] > 0:
                return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=solve(h,w,cmap)
    printans(ans)
