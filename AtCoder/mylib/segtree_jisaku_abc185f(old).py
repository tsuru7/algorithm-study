def m_input():
    return map(int, input().split())
def l_input():
    return list(m_input())

def readinput():
    n, q = m_input()
    a = l_input()
    queries = []
    for _ in range(q):
        queries.append(l_input())
    return n, q, a, queries

segtree = None
INFTY = 2**31 -1

def init(n, a):
    '''セグメント木を初期化する (0-indexed)
    
    Parameters:
        n: int
            要素数
        a: list(int)
            初期値リスト

    Reterns:
        n: int
            セグメント木の大きさ(2のべき乗の大きさにする)

    '''
    global segtree

    # n以上の最小の2のべき乗を探す
    n_ = 1
    while n_ < n:
        n_ *= 2
    
    segtree = [0]*(2*n_ - 1)

    # leaf nodeに初期値リストをセット
    k = n_ - 1
    for i in range(n):
        segtree[k+i] = a[i]
    
    # segtreeを構築
    while k > 0:
        k = (k-1)//2
        for i in range(k+1):
            j = k+i
            segtree[j] = segtree[2*j+1]^segtree[2*j+2]
    
    return n_

def update(k, a, n):
    '''ノード k の値を a に更新 (0-indexed)

    '''

    global segtree

    k += n - 1
    segtree[k] ^= a
    while k > 0:
        k = (k-1)//2
        segtree[k] = segtree[2*k+1] ^ segtree[2*k+2]

def query(a, b, k, l, r):
    '''区間[a, b)について処理を行う。現在着目しているノード番号は k 、対応する区間は [l, r)

       ※区間[a,b)の xor を返す例

    Parameters:
        a, b: int
            対象区間 [a, b)
        k: int
            k番目の節点
        l, r: int
            k番目の節点に対応する区間 [l, r)

    Returns:
        ans: int
            xor
    '''
    if r <= a or b <= l:
        return 0
    elif a <= l and r <= b:
        return segtree[k]
    else:
        vl = query(a, b, 2*k+1, l, (l+r)//2)
        vr = query(a, b, 2*k+2, (l+r)//2, r)
        return vl ^ vr

def main(n, q, a, queries):
    ans = []
    n = init(n, a)
    # print(n)
    # print(a)
    # print(segtree)
    for t, x, y in queries:
        if t == 1:
            update(x-1, y, n)
        else:
            ans.append(query(x-1, y, 0, 0, n))
        # print(segtree)
    return ans

def printans(ans):
    for a in ans:
        print(a)
    
if __name__ == '__main__':
    n, q, a, queries = readinput()
    ans = main(n, q, a, queries)
    printans(ans)
