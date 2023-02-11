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
    rs, cs = m_input()
    rs -= 1
    cs -= 1
    rt, ct = m_input()
    rt -= 1
    ct -= 1
    smap = [input() for _ in range(h)]
    return h,w,rs,cs,rt,ct,smap

def solve(h,w,rs,cs,rt,ct,smap):
    to1d = lambda row, col: row * w + col
    to2d = lambda x: divmod(x, w)

    queue = deque()
    depth = [[INFTY for _ in range(h*w)] for _ in range(4)]

    dirs = [0, 1, 2, 3] # u, d, l, r
    drdc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    start = to1d(rs, cs)
    goal = to1d(rt, ct)

    for dir in dirs:
        queue.append((start, dir))
        depth[dir][start] = 0

    while len(queue) > 0:
        u, udir = queue.popleft()
        ur, uc = to2d(u)
        dr, dc = drdc[udir]
        vr = ur + dr
        vc = uc + dc
        v = to1d(vr, vc)
        if 0 <= vr < h and 0 <= vc < w and smap[vr][vc] == '.':
            if depth[udir][v] <= depth[udir][u]:
                continue
            depth[udir][v] = depth[udir][u]
            queue.appendleft((v, udir))
        for vdir in dirs:
            if vdir == udir:
                continue
            dr, dc = drdc[vdir]
            vr = ur + dr
            vc = uc + dc
            v = to1d(vr, vc)
            if 0 <= vr < h and 0 <= vc < w and smap[vr][vc] == '.':
                if depth[vdir][v] <= depth[udir][u] + 1:
                    continue
                depth[vdir][v] = depth[udir][u] + 1
                queue.append((v, vdir))

    ans = INFTY
    for dir in dirs:
        # print(f'dir: {dir}, depth[dir]: {depth[dir]}')
        ans = min(ans, depth[dir][goal])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,rs,cs,rt,ct,smap=readinput()
    ans=solve(h,w,rs,cs,rt,ct,smap)
    printans(ans)
