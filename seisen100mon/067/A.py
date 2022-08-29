import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    n=i_input()
    xylist = [l_input() for _ in range(n)]
    return n,xylist

def solve(n,xylist):
    edge = []
    xlist = [(xylist[i][0], i) for i in range(n)]
    xlist.sort()
    for i in range(n-1):
        j = xlist[i][1]
        k = xlist[i+1][1]
        xj, yj = xylist[j]
        xk, yk = xylist[k]
        cost = min(abs(xk-xj), abs(yk-yj))
        edge.append((cost, j, k))
    ylist = [(xylist[i][1], i) for i in range(n)]
    ylist.sort()
    for i in range(n-1):
        j = ylist[i][1]
        k = ylist[i+1][1]
        xj, yj = xylist[j]
        xk, yk = xylist[k]
        cost = min(abs(xk-xj), abs(yk-yj))
        edge.append((cost, j, k))
    edge.sort()
    # print(f'edge: {edge}')
    S = UnionFind(n)
    ngroup = n
    ans=0
    for cost, i, j in edge:
        if S.issame(i,j):
            continue
        S.unite(i,j)
        ans += cost
        ngroup -= 1
        if ngroup == 1:
            return ans
    # print(f'ngroup: {ngroup}')

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xylist=readinput()
    ans=solve(n,xylist)
    printans(ans)
