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
    n,q=m_input()
    a=l_input()
    queries = [l_input() for _ in range(q)]
    return n,q,a,queries

def prepare(tbl, nmax):
    '''
    1回の操作の変換テーブル tbl から最大 nmax 回変換したときの変換先を求めるためのダブリングテーブルを作る
    '''
    n = len(tbl)
    dbl = [tbl]
    i = 1
    while (1<<i) <= nmax:
        dbl.append([0 for _ in range(n)])
        for j in range(n):
            dbl[i][j] = dbl[i-1][dbl[i-1][j]]
        i += 1
    return dbl

def doubling(x, n, dbl):
    '''
    ダブリングテーブル dbl を使って、x を n 回変換した結果を返す
    '''
    nmax = len(dbl)
    now = x
    for i in range(nmax)[::-1]:
        if n & (1<<i) > 0:
            now = dbl[i][now]
    return now

def solve(n,q,a,queries):
    a.insert(0,0)
    dbl = prepare(a, 10**9)
    ans = []
    for x, y in queries:
        ans.append(doubling(x, y, dbl))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
