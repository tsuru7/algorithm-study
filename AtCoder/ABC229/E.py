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
    graph = []
    for _ in range(n):
        graph.append([])
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        if a < b:
            graph[a].append(b)
        else:
            graph[b].append(a)
    return n,m,graph

def main(n,m,graph):
    uft = UnionFindTree(n)
    uft_size = n
    count = 0
    ans = []
    ans.append(count)
    for i in range(n)[::-1]:
        for v in graph[i]:
            if not uft.same(i, v):
                uft.unite(i, v)
                uft_size -= 1
        # print(f'uft_size: {uft_size}', end=', ')
        # uft.print()
        ans.append(uft_size-i)
    return ans[:-1]

def printans(ans):
    for a in ans[::-1]:
        print(a)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=main(n,m,graph)
    printans(ans)
