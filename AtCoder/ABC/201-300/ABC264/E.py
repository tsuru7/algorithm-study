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
    n,m,e=m_input()
    edges = [l_input() for _ in range(e)]
    q = i_input()
    queries = [i_input()-1 for _ in range(q)]
    return n,m,e,edges,q,queries

def solve(n,m,e,edges,q,queries):
    uft = UnionFind(n+m)
    for i in range(n, n+m-1):
        uft.unite(i, n+m-1)
    qset = set(queries)
    for i, (u, v) in enumerate(edges):
        u -= 1
        v -= 1
        if i in qset:
            continue
        uft.unite(u, v)
    ans=[uft.size(n+m-1)]
    for x in queries[::-1]:
        u, v = edges[x]
        u -= 1
        v -= 1
        uft.unite(u, v)
        ans.append(uft.size(n+m-1))

    ans = ans[:-1][::-1]
    ans1 = []
    for a in ans:
        ans1.append(a-m)
    return ans1

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,e,edges,q,queries=readinput()
    ans=solve(n,m,e,edges,q,queries)
    printans(ans)
