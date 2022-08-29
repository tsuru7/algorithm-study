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
    w,h=m_input()
    amap = [ [0] + l_input() + [0] for _ in range(h) ]
    amap.insert(0, [0]*(w+2))
    amap.append([0]*(w+2))
    return w,h,amap

def count_wall(u, amap):
    count = 0
    row, col = u
    for dr, dc in get_dirs(row):
        if 0 <= row+dr <= h+1 and 0 <= col+dc <= w+1 and amap[row+dr][col+dc] == 1:
            count += 1
    return count

def get_dirs(row):
    if row % 2 == 0:
        dirs = [ (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1) ]
    else:
        dirs = [ (-1, 1), (0, 1), (1, 1), (1, 0),  (0, -1), (-1, 0)  ]
    return dirs

def solve(w,h,amap):
    ans=0
    visited = [ [False]*(w+2) for _ in range(h+2) ]
    queue = deque()
    visited[0][0] = True
    u = (0, 0)
    ans += count_wall(u, amap)
    queue.append(u)
    while len(queue) > 0:
        row, col = queue.popleft()
        for dr, dc in get_dirs(row):
            if 0 <= row+dr <= h+1 and 0 <= col+dc <= w+1 and amap[row+dr][col+dc] == 0:
                if visited[row+dr][col+dc]:
                    continue
                visited[row+dr][col+dc] = True
                v = (row+dr, col+dc)
                ans += count_wall(v, amap)
                queue.append(v)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    w,h,amap=readinput()
    ans=solve(w,h,amap)
    printans(ans)
