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

def readinput():
    q=i_input()
    queries = []
    for _ in range(q):
        queries.append(l_input())
    return q, queries

def main(q, queries):
    n = 2**20
    segtree = [False]*(2*n+1)
    OFFSET = n
    a = [-1]*n
    ans=[]
    for t, x in queries:
        # print(f't: {t}, x: {x}')
        if t == 2:
            j = x % n
            ans.append(a[j])
            continue
        # 以下 t == 1
        j = x % n
        # print(f'j: {j}, j+OFFSET: {j+OFFSET}')
        # 更新する要素を取得

        v = segtree_query(j+OFFSET, segtree, n)
        # print(f'v: {v}')
        if v == n-1:
            if a[n-1] != -1:
                v = segtree_query(0+OFFSET, segtree, n)
        a[v] = x
        segtree_update(v, segtree, n)

    return ans

def segtree_query(i, segtree, size):
    """ i 番目を起点として右向きに探索して一番左の未更新ノードの番号を返す
    """
    OFFSET = size
    def isLeaf(x):
        return x >= OFFSET
    def isRight(x):
        return x % 2 == 1

    # print(f'i: {i}, i - OFFSET: {i - OFFSET}')
    if segtree[i] == False:
        if isLeaf(i):
            return i - OFFSET
        else:
            return segtree_query(2*i, segtree, size)
    else:
        # 現在ノードが True
        if isRight(i):
            if i - OFFSET < size-1:
                return segtree_query(i+1, segtree, size)
            else:
                return size-1
        else:
            # 左側ノード
            if segtree[i//2]:
                # True になるノードには必ず親ノードがある(ルートは必ずFalse)
                return segtree_query(i//2, segtree, size)
            else:
                # 必ず右側ノードがある
                return segtree_query(i+1, segtree, size)

def segtree_update(i, segtree, size):
    OFFSET = size
    k = i + OFFSET
    segtree[k] = True
    p = k // 2
    while p > 0:
        segtree[p] = segtree[2*p] and segtree[2*p+1]
        p = p // 2
    return




def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    q, queries=readinput()
    ans=main(q, queries)
    printans(ans)
