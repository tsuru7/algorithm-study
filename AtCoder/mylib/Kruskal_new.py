import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop

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

def readinput():
    n,m,k=m_input()
    edge = []
    for _ in range(m):
        a, b, c = m_input()
        a -= 1
        b -= 1
        edge.append((c, a, b))
    return n,m,k,edge

def solve(n,m,k,edge):
    '''
    クラスカル法
    1. グラフ G(V, E) の辺　ei を重みの昇順に整列する
    2. 最小全域木の辺の集合を K とし、それを空に初期化する
    3. i = 1, 2, ..., |E| の順番に |K| が |V|-1 になるまで K U {ei} が閉路を作らないような ei を K に追加する
    '''
    if k == n:
        return 0
    edge.sort()
    S = UnionFind(n)
    ngroup = n
    ans = 0
    for i in range(m):
        c, a, b = edge[i]
        if not S.issame(a, b):
            S.unite(a, b)
            ans += c
            ngroup -= 1
            if ngroup == k:
                return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,edge=readinput()
    ans=solve(n,m,k,edge)
    printans(ans)
