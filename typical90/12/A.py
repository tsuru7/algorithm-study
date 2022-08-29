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
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return h,w,q,queries

def solve(h,w,q,queries):
    def to1d(row, col):
        return row*w+col
    def to2d(idx):
        row, col = divmod(idx, w)
    uft = UnionFind(h*w)
    redset = set()
    ans=[]
    for query in queries:
        if query[0] == 1:
            r, c = query[1:]
            r -= 1
            c -= 1
            idx = to1d(r, c)
            redset.add(idx)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= r+dr < h and 0 <= c+dc < w:
                    idx2 = to1d(r+dr, c+dc)
                    if idx2 in redset:
                        uft.unite(idx2, idx)
        else:
            ra, ca, rb, cb = query[1:]
            ra -= 1
            ca -= 1
            rb -= 1
            cb -= 1
            idx1 = to1d(ra, ca)
            idx2 = to1d(rb, cb)
            if idx1 not in redset or idx2 not in redset:
                ans.append('No')
            else:
                if uft.issame(idx1, idx2):
                    ans.append('Yes')
                else:
                    ans.append('No')


    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    h,w,q,queries=readinput()
    ans=solve(h,w,q,queries)
    printans(ans)
