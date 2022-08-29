import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque
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
    a=l_input()
    return n,a

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


def main(n,a):
    uft = UnionFindTree(2*10**5)
    for i in range(n):
        if a[i] != a[n-1-i]:
            uft.unite(a[i]-1, a[n-1-i]-1)
    
    count = [0]*(2*10**5)
    for i in range(2*10**5):
        count[uft.findSet(i)] += 1
    
    ans = 0
    for i in range(2*10**5):
        if count[i] > 0:
            ans += count[i] - 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
