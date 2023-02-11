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
    n,m,k=m_input()
    friend = [l_input() for _ in range(m)]
    block = [l_input() for _ in range(k)]
    return n,m,k,friend,block

def solve(n,m,k,friend,block):
    uft = UnionFind(n)
    for a, b in friend:
        a -= 1
        b -= 1
        uft.unite(a, b)
    ncandidates = [uft.size(i)-1  for i in range(n)]
    for a, b in friend:
        a -= 1
        b -= 1
        ncandidates[a] -= 1
        ncandidates[b] -= 1
    for c, d, in block:
        c -= 1
        d -= 1
        if uft.issame(c, d):
            ncandidates[c] -= 1
            ncandidates[d] -= 1

    return ncandidates

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,k,friend,block=readinput()
    ans=solve(n,m,k,friend,block)
    printans(ans)
