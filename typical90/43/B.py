from calendar import TUESDAY
import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

input = sys.stdin.readline

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

smap = None
def readinput():
    global smap

    h,w=m_input()
    rs, cs = m_input()
    rt, ct = m_input()
    smap = [input() for _ in range(h)]
    return h,w,rs,cs,rt,ct

# def isreachable(r, c, h, w, smap):
#     if 0 <= r < h and 0 <= c < w and smap[r][c] == '.':
#         return True
#     else:
#         return False

depth = None
def solve(h,w,rs,cs,rt,ct):
    global depth

    isreachable = lambda r, c: 0 <= r < h and 0 <= c < w and smap[r][c] == '.'

    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1

    # depth = [[[INFTY for _ in range(4)] for _ in from calendar import TUESDAY
import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

input = sys.stdin.readline

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

smap = None
def readinput():
    global smap

    h,w=m_input()
    rs, cs = m_input()
    rt, ct = m_input()
    smap = [input() for _ in range(h)]
    return h,w,rs,cs,rt,ct

# def isreachable(r, c, h, w, smap):
#     if 0 <= r < h and 0 <= c < w and smap[r][c] == '.':
#         return True
#     else:
#         return False

depth = None
def solve(h,w,rs,cs,rt,ct):
    global depth

    isreachable = lambda r, c: 0 <= r < h and 0 <= c < w and smap[r][c] == '.'

    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1

    depth = [[[INFTY for _ in range(w)] for _ in range(h)] for _ in range(4)]
    # depth = [[[INFTY for _ in range(4)] for _ in range(w)] for _ in range(h)]
    # depth = [INFTY for _ in range(h*w*4)]
    to1d = lambda r,c,dir: r*w*4 + c*4 + dir
    dr = [-1, 1, 0, 0] # up, down, left, right
    dc = [0, 0, -1, 1]
    queue = deque()

    # マスの位置と、マスでの向きを「状態」とする
    for udir in range(4):
        ustate = (rs, cs, udir)
        # depth[rs][cs][udir] = 0
        depth[udir][rs][cs] = 0
        # depth[to1d(rs,cs,udir)] = 0
        # # 次のマスが到達不能ならスキップ
        # if not isreachable(rs+dr[udir], cs+dc[udir]):
        #     continue
        # 「状態」をキューに入れる
        queue.append(ustate)

    while len(queue) > 0:
        ur, uc, udir = queue.popleft()
        # キューから取り出した「状態」の次のマスは「状態」に含まれる向きで決まる
        vr = ur + dr[udir]
        vc = uc + dc[udir]
        if not isreachable(vr, vc):
            continue
        # 次のマスでの向きを全て列挙して、それぞれの「状態」でのコストを計算する
        for vdir in range(4):
            vstate = (vr, vc, vdir)
            ex = (0 if vdir == udir else 1)
            # cost = depth[ur][uc][udir] + ex
            cost = depth[udir][ur][uc] + ex
            # cost = depth[to1d(ur,uc,udir)] + ex
            # 次のマスの「状態」のコストを更新できるとき、
            # コストが増加していなければキューの先頭に、増加していればキューの末尾に追加する
            # (01-BFS)
            # if depth[vr][vc][vdir] > cost:
            #     depth[vr][vc][vdir] = cost
            # if depth[to1d(vr,vc,vdir)] > cost:
            #     depth[to1d(vr,vc,vdir)] = cost
            if depth[vdir][vr][vc] > cost:
                depth[vdir][vr][vc] = cost
                if vdir == udir:
                    queue.appendleft(vstate)
                else:
                    queue.append(vstate)

    # for row in range(h):
    #     print(*depth[row])
    # ans = INFTY
    # for dir in range(4):
    #     ans=min(ans, depth[to1d(rt, ct, dir)])
    ans = INFTY
    for dir in range(4):
        ans=min(ans, depth[dir][rt][ct])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,rs,cs,rt,ct=readinput()
    ans=solve(h,w,rs,cs,rt,ct)
    printans(ans)
