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

class SegTree:
    def __init__(self, n, a):
        '''
        1-indexedのセグメント木を用意
        '''
        m = 1
        while 1<<m < n:
            m += 1
        self.siz = m
        self.data = [0 for _ in range(2*m)]
        return
    

    
    def update(self, pos, x):
        pos += self.siz - 1


def readinput():
    n,q=m_input()
    queries = [l_input() for _ in range(q)]
    return n,q,queries

def update(segtree, pos, x):
    m = len(segtree)//2
    pos += m - 1
    segtree[pos] = x
    pos //= 2
    while pos > 0:
        segtree[pos] = max(segtree[2*pos], segtree[2*pos+1])
        pos //= 2
    return

def solve(n,q,queries):
    m = 1
    while 1<<m < n:
        m += 1
    segtree = [0 for _ in range(2*m)]
    for q in queries:
        if q[0] == 1:
            pos = q[1]
            x = q[2]
            update(segtree, pos, x)
        else:
            l = q[1]
            r = q[2]

    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,q,queries=readinput()
    ans=solve(n,q,queries)
    printans(ans)
