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

    def __init__(self, n, operator=max, identity=-INFTY):
        '''
        1-indexedのセグメント木用配列を用意

        operator, identityの例

        operator: add
        identity: 0

        operator: mul
        identity: 1

        operator: min
        identity: INFTY

        operator: max
        identity: -INFTY

        operator: gcd
        identity: 1

        operator: xor
        identity: 0

        '''
        self.operator = operator
        self.identity = identity

        m = 1
        while 1<<m < n:
            m += 1
        self.siz = 1<<m
        self.data = [self.identity for _ in range(2*self.siz)]
        return

    def set(self, pos, x):
        '''
        pos: 1 始まりとしたときの値を変更する leaf の位置
        '''
        pos += self.siz - 1
        self.data[pos] = x
        pos //= 2
        while pos > 0:
            self.data[pos] = self.operator(self.data[2*pos], self.data[2*pos+1])
            pos //= 2
        return

    def get(self, pos):
        '''
        pos: 1 始まりとしたときの leaf の値を返す
        '''
        pos += self.siz - 1
        return self.data[pos]

    def query(self, l, r):
        '''
        1 始まりとしたときの半開区間 [l, r) での operator の結果を返す
        '''
        a = 1
        b = self.siz+1
        u = 1
        return self.query_(l, r, a, b, u)


    def query_(self, l, r, a, b, u):
        if r <= a or b <= l:
            return self.identity
        if l <= a and b <= r:
            return self.data[u]
        m = (a+b)//2
        ansl = self.query_(l, r, a, m, u*2)
        ansr = self.query_(l, r, m, b, 2*u+1)
        return self.operator(ansl, ansr)

    def print(self):
        print(self.data)
#########################################################


def readinput():
    n,q=m_input()
    a=l_input()
    queries = [l_input() for _ in range(q)]
    return n,q,a,queries

def solve(n,q,a,queries):
    segtree = SegTree(n,operator=lambda x, y: x^y, identity=0)
    for i in range(n):
        segtree.set(i+1, a[i])
    # segtree.print()
    ans=[]
    for t, x, y in queries:
        if t == 1:
            # print(f't: {t}, x: {x}, y: {y}')
            segtree.set(x, segtree.get(x)^y)
            # segtree.print()
        elif t == 2:
            # print(f't:{t}, x: {x}, y: {y}')
            ans.append(segtree.query(x, y+1))
            # segtree.print()
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
