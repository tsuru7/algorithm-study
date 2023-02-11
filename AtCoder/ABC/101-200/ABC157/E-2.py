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
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]


def readinput():
    n=i_input()
    s = input()
    q = i_input()
    queries = [input().split() for _ in range(q)]
    return n,s,q,queries

def solve(n,s,q,queries):
    op = lambda x, y: x | y
    e = lambda : 0
    v = [1<<(ord(s[i]) - ord('a')) for i in range(n)]
    segtree = SegTree(op, e, n, v)

    ans=[]
    for query in queries:
        if query[0] == '1':
            i = int(query[1])-1
            c = 1<<(ord(query[2])-ord('a'))
            segtree.set(i, c)
        else:
            l = int(query[1])-1
            r = int(query[2])-1
            tmp = segtree.prod(l, r+1)
            # print(f'l: {l}, r: {r}, tmp: {bin(tmp)}')
            ans.append(bin(tmp).count('1'))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,s,q,queries=readinput()
    ans=solve(n,s,q,queries)
    printans(ans)
