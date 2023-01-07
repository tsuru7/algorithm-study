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
    smap = [input() for _ in range(h)]
    return h,w,smap

def countangle(row, col, smap):
    ans = 0
    drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4):
        dr1, dc1 = drdc[i]
        ur, uc = row+dr1, col+dc1
        dr2, dc2 = drdc[(i+1)%4]
        vr, vc = row+dr2, col+dc2
        wr, wc = row+dr1+dr2, col+dc1+dc2
        if smap[ur][uc] == '#' and smap[vr][vc] == '#' and smap[wr][wc] == '.':
            ans += 1
        if smap[ur][uc] == '.' and smap[vr][vc] == '.':
            ans += 1
    return ans

def solve(h,w,smap):
    for row in range(h):
        for col in range(w):
            if smap[row][col] == '#':
                start = (row, col)
    queue = deque()
    visited = [[False for _ in range(w)] for _ in range(h)]
    sr, sc = start
    queue.append(start)
    visited[sr][sc] = True
    ans=0
    while len(queue) > 0:
        ur, uc = queue.popleft()
        ans += countangle(ur, uc, smap)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vr, vc = ur + dr, uc + dc
            if visited[vr][vc]:
                continue
            if smap[vr][vc] == '#':
                queue.append((vr, vc))
                visited[vr][vc] = True
    

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,smap=readinput()
    ans=solve(h,w,smap)
    printans(ans)
