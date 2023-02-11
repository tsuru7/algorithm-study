import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict
from bisect import bisect_left, bisect_right

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
    h,w,rs,cs=m_input()
    n = i_input()
    walls = [l_input() for _ in range(n)]
    q = i_input()
    queries = [input().split() for _ in range(q)]
    return h,w,rs,cs,n,walls,q,queries

def solve(h,w,rs,cs,n,walls,q,queries):
    tate = defaultdict(list)
    yoko = defaultdict(list)
    for r, c in walls:
        tate[c].append(r)
        yoko[r].append(c)
    for _, v in tate.items():
        v.sort()
    for _, v in yoko.items():
        v.sort()
    row = rs
    col = cs
    ans = []
    for d, l in queries:
        l = int(l)
        if d == 'R':
            if row in yoko:
                walls = yoko[row]
                idx = bisect_left(walls, col)
                if idx == len(walls):
                    col = min(w, col+l)
                else:
                    next_wall = walls[idx]
                    col = min(next_wall-1, col+l)
            else:
                col = min(w, col+l)
        elif d == 'L':
            if row in yoko:
                walls = yoko[row]
                idx = bisect_left(walls, col)
                if idx == 0:
                    col = max(1, col-l)
                else:
                    next_wall = walls[idx-1]
                    col = max(next_wall+1, col-l)
            else:
                col = max(1, col-l)
        elif d == 'U':
            if col in tate:
                walls = tate[col]
                idx = bisect_left(walls, row)
                if idx == 0:
                    row = max(1, row-l)
                else:
                    next_wall = walls[idx-1]
                    row = max(next_wall+1, row-l)
            else:
                row = max(1, row-l)
        else:
            if col in tate:
                walls = tate[col]
                idx = bisect_left(walls, row)
                if idx == len(walls):
                    row = min(h, row+l)
                else:
                    next_wall = walls[idx]
                    row = min(next_wall-1, row+l)
            else:
                row = min(h, row+l)
        ans.append((row, col))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    h,w,rs,cs,n,walls,q,queries=readinput()
    ans=solve(h,w,rs,cs,n,walls,q,queries)
    printans(ans)
