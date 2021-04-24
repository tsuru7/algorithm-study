def m_input():
    return map(int, input().split())
def l_input():
    return list(m_input())

def readinput():
    n, q = m_input()
    queries = []
    for _ in range(q):
        queries.append(l_input())
    return n, q, queries

segtree = None
INFTY = 2**31 -1

def init(n):
    global segtree

    n_ = 1
    while n_ < n:
        n_ *= 2
    
    segtree = [INFTY]*(2*n_ - 1)
    return n_

def update(k, a, n):
    global segtree

    k += n - 1
    segtree[k] = a
    while k > 0:
        k = (k-1)//2
        segtree[k] = min(segtree[2*k+1], segtree[2*k+2])

def query(a, b, k, l, r):
    # print(a, b, k, l, r)
    '''区間[a,b)の最小値を返す

    Parameters:
        a, b: int
            対象区間 [a, b)
        k: int
            k番目の節点
        l, r: int
            k番目の節点に対応する区間 [l, r)

    Returns:
        ans: int
            最小値
    '''
    if r <= a or b <= l:
        return INFTY
    elif a <= l and r <= b:
        return segtree[k]
    else:
        vl = query(a, b, 2*k+1, l, (l+r)//2)
        vr = query(a, b, 2*k+2, (l+r)//2, r)
        return min(vl, vr)

def main(n, q, queries):
    ans = []
    n = init(n)
    # print(n)
    # print(segtree)
    for c, x, y in queries:
        if c == 0:
            update(x, y, n)
        else:
            ans.append(query(x, y+1, 0, 0, n))
        # print(segtree)
    return ans

def printans(ans):
    for a in ans:
        print(a)
    
if __name__ == '__main__':
    n, q, queries = readinput()
    ans = main(n, q, queries)
    printans(ans)
