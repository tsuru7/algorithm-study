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
    n,m=m_input()
    abList = [l_input() for _ in range(m)]
    return n,m,abList

def solve(n,m,abList):
    uft = UnionFind(n)
    huben = n*(n-1)//2
    ans=[huben]
    for i in range(m)[::-1]:
        a, b = abList[i]
        a -= 1
        b -= 1
        if not uft.issame(a, b):
            x = uft.size(a)
            y = uft.size(b)
            uft.unite(a,b)
            huben1 = x*(x-1)//2 if x > 1 else 0
            huben2 = y*(y-1)//2 if y > 1 else 0
            huben += huben1 + huben2 - (x+y)*(x+y-1)//2
        ans.append(huben)
    return ans[:-1][::-1]

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,abList=readinput()
    ans=solve(n,m,abList)
    printans(ans)
