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
    h, w = m_input()
    smap = [ input() for _ in range(h) ]
    return h, w, smap

def solve(h, w, smap):
    if smap[0][0] == '#' or smap[h-1][w-1] == '#':
        return -1

    count = 0
    for row in range(h):
        for col in range(w):
            if smap[row][col] == '.':
                count += 1
    
    visited = [ [-1]*w for _ in range(h) ]
    queue = deque()
    u = (0, 0)
    queue.append(u)
    visited[0][0] = 1
    while len(queue) > 0:
        row, col = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1) ]:
            if 0 <= row+dr < h and 0 <= col+dc < w and smap[row+dr][col+dc] == '.':
                if visited[row+dr][col+dc] < 0:
                    v = (row+dr, col+dc)
                    visited[row+dr][col+dc] = visited[row][col] + 1
                    queue.append(v)
    if visited[h-1][w-1] == -1:
        return -1
    else:
        return count - visited[h-1][w-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    h, w, smap=readinput()
    ans=solve(h, w, smap)
    printans(ans)
