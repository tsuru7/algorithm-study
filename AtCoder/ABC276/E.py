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
                start = (row, col)
    visited = [-1 for _ in range(h*w)]
    queue = deque()
    queue.append(start)
    visited[to1d(*start)] = 0
    while len(queue) > 0:
        ur, uc = queue.popleft()
        if (ur, uc) == start:
            break
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            vr = ur + dr
            vc = uc + dc
            if 0 <= vr < h and 0 <= vc < w and cmap[vr][vc] == '.':
                if visited[to1d(vr, vc)] == -1:
                    if (vr, vc) != start:
                        queue.append((vr, vc))
                        visited[to1d(vr, vc)] = visited[to1d(ur, uc)] + 1
                    else:
                        if visited[to1d(ur, uc)] >= 3:
                            queue.append((vr, vc))
                            visited[to1d(vr, vc)] = visited[to1d(ur, uc)] + 1
    if visited[to1d(*start)] >= 4:
        return 'Yes'
    else:
        return 'No'


def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=solve(h,w,cmap)
    printans(ans)
