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
    n,k=m_input()
    return n,k

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

def solve(n,k):
    tbl = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        tmp = 0
        x = i
        while x > 0:
            tmp += x % 10
            x //= 10
        tbl[i] = i-tmp

    dbl = prepare(tbl, k)

    ans = []
    for i in range(1, n+1):
        ans.append(doubling(i, k, dbl))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
