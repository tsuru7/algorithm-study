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

class UnionFindTree:
    def __init__(self,size):
        self.rank=[0]*size
        self.p=[0]*size
        for i in range(size):
            self.makeSet(i)
    
    def makeSet(self,i):
        self.p[i]=i
        self.rank[i]=0
    
    def same(self,x,y):
        return self.findSet(x) == self.findSet(y)
    
    def unite(self, x,y):
        self.link(self.findSet(x), self.findSet(y))
    
    def link(self, x, y):
        if(self.rank[x] > self.rank[y]):
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y]+=1
     
    def findSet(self, x):
        if(x!=self.p[x]):
            self.p[x]=self.findSet(self.p[x])
        return self.p[x]

    def print(self):
        print(self.p)

def readinput():
    n,m=m_input()
    abcList_p = []
    abcList_m = []
    for _ in range(m):
        a, b, c = m_input()
        a -= 1
        b -= 1
        if c >= 0:
            abcList_p.append((c, a, b))
        else:
            abcList_m.append((c, a, b))
    return n,m,abcList_p,abcList_m

def main(n,m,abcList_p,abcList_m):
    uft = UnionFindTree(n)
    ans=0

    for c, a, b in abcList_m:
        uft.unite(a, b)
    # uft.print()

    abcList_p.sort()
    for c, a, b in abcList_p:
        if uft.same(a, b):
            ans += c
        else:
            uft.unite(a, b)
    # uft.print()
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,abcList_p,abcList_m=readinput()
    ans=main(n,m,abcList_p,abcList_m)
    printans(ans)
