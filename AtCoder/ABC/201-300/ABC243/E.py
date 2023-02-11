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
    n,m=m_input()
    graph = [ [] for _ in range(n) ]
    nMap = [ [INFTY]*n for _ in range(n) ]
    for i in range(n):
        nMap[i][i] = 0
    for _ in range(m):
        a, b, c = m_input()
        a -= 1
        b -= 1
        nMap[a][b] = c
        nMap[b][a] = c
        graph[a].append((b,c))
        graph[b].append((a,c))
    return n,m,nMap,graph

def warshalFloyd(nv, nMap):
    '''
    ワーシャルフロイド法による全点対間最短経路問題(APSP)の解法

    グラフ G=(V,E)に対してGに含まれる頂点のすべての組の最短経路を求める
    負の重みのある辺があっても、負の閉路がなければ使用可能
    
    パラメーター
    nv: 頂点の数
    nMap: 隣接マップ
          但し、
          nMap[i][i]=0
          nMap[i][j]=INFTY ((i,j)間に辺がない場合)

    戻り値
    nMap: nMap[i][j] (i,j)間の最短コスト
          nMap[i][i] < 0 のとき、負の閉路が存在する

    '''
    cut = set()
    for k in range(nv):
        for i in range(nv):
            if(nMap[i][k]==INFTY):
                continue
            for j in range(nv):
                if(nMap[k][j]==INFTY):
                    continue
                if i == k or j == k or i == j:
                    continue
                if nMap[i][j] != INFTY and nMap[i][j] >= nMap[i][k] + nMap[k][j]:
                    cut.add( ( min(i,j), max(i,j)))
                    # nMap[i][j] = INFTY
                nMap[i][j] = min(nMap[i][j], nMap[i][k]+nMap[k][j])
    return nMap, len(cut)

def solve(n,m,nMap,graph):
    nMap, ncut = warshalFloyd(n, nMap)
    # ans=0
    # for a in range(n):
    #     for b, c in graph[a]:
    #         if b <= a:
    #             continue
    #         if nMap[a][b] < c:
    #             ans += 1

    return ncut

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nMap,graph=readinput()
    ans=solve(n,m,nMap,graph)
    printans(ans)
