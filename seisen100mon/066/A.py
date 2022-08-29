import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import sqrt

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
    queries = []
    n = i_input()
    while n != 0:
        cells = [list(map(float, input().split())) for _ in range(n)]
        queries.append(cells)
        n = i_input()
    return queries

def solve(queries):
    ans=[]
    for cells in queries:
        n = len(cells)
        if n == 1:
            ans.append(0.0)
            continue
        edges = []
        for i in range(n):
            xi, yi, zi, ri = cells[i]
            for j in range(i+1, n):
                xj, yj, zj, rj = cells[j]
                dij = sqrt((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)
                edges.append( (max(0.0, dij - (ri+rj)), i, j) )
        edges.sort()
        S = UnionFind(n)
        cost = 0
        ngroup = n
        for edge in edges:
            c, i, j = edge
            if not S.issame(i, j):
                S.unite(i, j)
                cost += c
                ngroup -= 1
                if ngroup == 1:
                    ans.append(cost)
                    break
        
    return ans

def printans(ans):
    for a in ans:
        print('{:.3f}'.format(a))

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
