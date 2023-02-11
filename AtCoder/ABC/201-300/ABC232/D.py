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
    cmap = [ input() for _ in range(h) ]
    return h,w,cmap

def main(h,w,cmap):
    queue = deque()
    visited = [ [False]*w for _ in range(h) ]
    depth = [ [0]*w for _ in range(h) ]
    u = (0,0)
    queue.append(u)
    visited[0][0] = True
    depth[0][0] = 1
    maxdepth = 1
    while len(queue):
        u = queue.popleft()
        row, col = u
        next_boxes = []
        if row < h-1 and cmap[row+1][col] == '.':
            next_boxes.append((row+1, col))
        if col < w-1 and cmap[row][col+1] == '.':
            next_boxes.append((row, col+1))
        for v in next_boxes:
            vrow, vcol = v
            if visited[vrow][vcol]:
                continue
            queue.append(v)
            visited[vrow][vcol] = True
            depth[vrow][vcol] = depth[row][col]+1
            if maxdepth < depth[vrow][vcol]:
                maxdepth = depth[vrow][vcol]
    return maxdepth

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=main(h,w,cmap)
    printans(ans)
