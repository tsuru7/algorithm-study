import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from heapq import heappop, heappush
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
    nMap = []
    for i in range(n):
        nMap.append([INFTY]*n)
    for i in range(n):
        nMap[i][i] = 0
    for i in range(m):
        a,b,c = m_input()
        a -= 1
        b -= 1
        nMap[a][b]=c
    return n,nMap

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
    total = 0
    for k in range(nv):
        for i in range(nv):
            if(nMap[i][k]==INFTY):
                continue
            for j in range(nv):
                if(nMap[k][j]==INFTY):
                    continue
                nMap[i][j] = min(nMap[i][j], nMap[i][k]+nMap[k][j])
        for i in range(nv):
            for j in range(nv):
                if nMap[i][j] == INFTY:
                    continue
                total += nMap[i][j]
    return total


def main(n,nMap):
    ans = warshalFloyd(n, nMap)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,nMap=readinput()
    ans=main(n,nMap)
    printans(ans)
