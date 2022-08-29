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
    n=i_input()
    ax,ay=m_input()
    bx,by=m_input()
    smap = [input() for _ in range(n)]
    return n,ax,ay,bx,by,smap

def solve(n,ax,ay,bx,by,smap):
    ax -= 1
    ay -= 1
    bx -= 1
    by -= 1
    queue = deque()
    ul = 0
    ur = 1
    dr = 2
    dl = 3
    dirx = [-1, 1, 1, -1]
    diry = [-1, -1, 1, 1]
    depth = [[[INFTY for _ in range(n)] for _ in range(n)] for _ in range(4)]
    for dir in [ul, ur, dr, dl]:
        queue.append((ax, ay, dir))
        depth[dir][ax][ay] = 0
    while len(queue) > 0:
        ux, uy, udir = queue.popleft()
        if ux == bx and uy == by:
            return depth[udir][ux][uy]+1
        dx = dirx[udir]
        dy = diry[udir]
        vx = ux + dx
        vy = uy + dy
        if 0 <= vx < n and 0 <= vy < n and smap[vx][vy] == '.':
            for vdir in [ul, ur, dr, dl]:
                if vdir == udir:
                    cost = depth[udir][ux][uy]
                else:
                    cost = depth[udir][ux][uy] + 1
                if cost < depth[vdir][vx][vy]:
                    depth[vdir][vx][vy] = cost
                    if vdir == udir:
                        queue.appendleft((vx, vy, vdir))
                    else:
                        queue.append((vx, vy, vdir))
    # print(*depth, sep='\n')
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ax,ay,bx,by,smap=readinput()
    ans=solve(n,ax,ay,bx,by,smap)
    printans(ans)
