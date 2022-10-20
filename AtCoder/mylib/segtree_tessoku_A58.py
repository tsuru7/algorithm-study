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
        
########################################################
class SegTree:
    def __init__(self, n):
        '''
        1-indexedのセグメント木用配列を用意
        '''
        m = 1
        while 1<<m < n:
            m += 1
        self.siz = 1<<m
        self.data = [0 for _ in range(2*self.siz)]
        return
     
    def update(self, pos, x):
        '''
        pos: 1 始まりとしたときの値を変更する leaf の位置
        '''
        pos += self.siz - 1
        # print(f'pos: {pos}, len(data): {len(self.data)}')
        self.data[pos] = x
        pos //= 2
        while pos > 0:
            self.data[pos] = max(self.data[2*pos], self.data[2*pos+1])
            pos //= 2
        return

    def query(self, l, r):
        '''
        1 始まりとしたときの半開区間 [l, r) での最大値を返す
        '''
        a = 1
        b = self.siz+1
        u = 1
        return self.query_(l, r, a, b, u)


    def query_(self, l, r, a, b, u):
        # print(f'[query_] l: {l}, r: {r}, a: {a}, b: {b}, u: {u}')
        if r <= a or b <= l:
            return -INFTY
        if l <= a and b <= r:
            return self.data[u]
        m = (a+b)//2
        ansl = self.query_(l, r, a, m, u*2)
        ansr = self.query_(l, r, m, b, 2*u+1)
        return max(ansl, ansr)

    def print(self):
        print(self.data)

#########################################################

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
    segtree = SegTree(n)
    # segtree.print()
    ans = []
    for q in queries:
        if q[0] == 1:
            pos = q[1]
            x = q[2]
            segtree.update(pos, x)
        else:
            l = q[1]
            r = q[2]
            x = segtree.query(l, r)
            ans.append(x)
        # segtree.print()
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,queries=readinput()
    ans=solve(n,q,queries)
    printans(ans)
