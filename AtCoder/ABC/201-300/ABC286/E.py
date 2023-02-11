import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    n=i_input()
    a=l_input()
    sList = [input() for _ in range(n)]
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return n,a,sList,queries

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

    for k in range(nv):
        for i in range(nv):
            if(nMap[i][k]==INFTY):
                continue
            for j in range(nv):
                if(nMap[k][j]==INFTY):
                    continue
                nMap[i][j] = min(nMap[i][j], nMap[i][k]+nMap[k][j])
    return nMap

def solve(n,a,sList,queries):
    # 隣接行列を作る
    DIRECT = 10**12
    nMap = [[INFTY for _ in range(n)] for _ in range(n)]
    for i in range(n):
        nMap[i][i] = 0
    for i in range(n):
        s = sList[i]
        for j in range(n):
            if s[j] == 'Y':
                nMap[i][j] = DIRECT - a[j]
    ansMap = warshalFloyd(n, nMap)
    ans=[]
    for u, v in queries:
        u -= 1
        v -= 1
        if ansMap[u][v] == INFTY:
            ans.append((-1, -1))
        else:
            flight = ansMap[u][v] // DIRECT + 1
            souvenir = flight*DIRECT - ansMap[u][v] + a[u]
            ans.append((flight, souvenir))

    return ans

def printans(ans):
    for f, s in ans:
        if f == -1 and s == -1:
            print('Impossible')
        else:
            print(f, s)

if __name__=='__main__':
    n,a,sList,queries=readinput()
    ans=solve(n,a,sList,queries)
    printans(ans)
