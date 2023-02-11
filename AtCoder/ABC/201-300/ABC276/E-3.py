import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


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

    uft = UnionFind(h*w)
    for row in range(h):
        for col in range(w):
            if cmap[row][col] == '#':
                continue
            elif cmap[row][col] == 'S':
                srow = row
                scol = col
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                vr = row + dr
                vc = col + dc
                if 0 <= vr < h and 0 <= vc < w and cmap[vr][vc] == '.':
                    uft.unite(to1d(row, col), to1d(vr, vc))
    for sr1, sc1 in [(srow-1, scol), (srow+1, scol), (srow, scol-1), (srow, scol+1)]:
        for sr2, sc2 in [(srow-1, scol), (srow+1, scol), (srow, scol-1), (srow, scol+1)]:
            if (sr1, sc1) == (sr2, sc2):
                continue
            if not (0 <= sr1 < h and 0 <= sc1 < w and 0 <= sr2 < h and 0 <= sc2 < w):
                continue
            if uft.issame(to1d(sr1, sc1), to1d(sr2, sc2)):
                return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,cmap=readinput()
    ans=solve(h,w,cmap)
    printans(ans)
