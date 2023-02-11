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
    n=i_input()
    xyList = [l_input() for _ in range(n)]
    return n,xyList

def neighbor(hex1, hex2):
    x1, y1 = hex1
    x2, y2 = hex2
    if (x2, y2) == (x1-1, y1-1) \
        or (x2, y2) == (x1-1, y1) \
        or (x2, y2) == (x1, y1-1) \
        or (x2, y2) == (x1, y1+1) \
        or (x2, y2) == (x1+1, y1) \
        or (x2, y2) == (x1+1, y1+1) \
        or (x1, y1) == (x2-1, y2-1) \
        or (x1, y1) == (x2-1, y2) \
        or (x1, y1) == (x2, y2-1) \
        or (x1, y1) == (x2, y2+1) \
        or (x1, y1) == (x2+1, y2) \
        or (x1, y1) == (x2+1, y2+1):
        return True
    else:
        return False

def solve(n,xyList):
    uft = UnionFind(n)
    connected = n
    for i in range(n):
        hex1 = xyList[i]
        for j in range(i+1, n):
            hex2 = xyList[j]
            if uft.issame(i, j):
                continue
            if neighbor(hex1, hex2):
                uft.unite(i, j)
                connected -= 1
    return connected

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xyList=readinput()
    ans=solve(n,xyList)
    printans(ans)
