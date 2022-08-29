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
    rt, ct = m_input()
    smap = [input() for _ in range(h)]
    return h,w,rs,cs,rt,ct,smap

def solve(h,w,rs,cs,rt,ct,smap):
    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1
    queue = deque()
    depth = [[-1 for _ in range(w)] for _ in range(h)]
    u = (rs, cs)
    depth[rs][cs] = 0
    queue.append((rs,cs))
    while len(queue) > 0:
        ur, uc = queue.popleft()
        if ur == rt and uc == ct:
            return depth[ur][uc] - 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vr = ur+dr
            vc = uc+dc
            while 0 <= vr < h and 0 <= vc < w and smap[vr][vc] == '.':
                if depth[vr][vc] < 0:
                    depth[vr][vc] = depth[ur][uc] + 1
                    queue.append((vr, vc))
                vr += dr
                vc += dc

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,rs,cs,rt,ct,smap=readinput()
    ans=solve(h,w,rs,cs,rt,ct,smap)
    printans(ans)
