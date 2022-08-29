import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from heapq import heappush, heappop
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
    n,m,x,y=m_input()
    x -= 1
    y -= 1
    nList = []
    for _ in range(n):
        nList.append([])
    for _ in range(m):
        a, b, t, k = m_input()
        a -= 1
        b -= 1
        nList[a].append((b, t, k))
        nList[b].append((a, t, k))
    return n,m,x,y,nList

def waittime(t,k):
    if t % k == 0:
        return 0
    else:
        return k - (t % k)

def dijkstra(s,g,n,nList):
    '''優先度付きキューを使用したダイクストラ法

    パラメーター
    s: 始点
    g: ゴール
    n: 頂点の数
    nList: [ 
        [vertex1, cost1], [vertex2, cost2], ...
        [vertex1, cost1], [vertex2, cost2], ...
        ...
    ]

    返り値
    d: 始点sから各頂点vまでの最短経路上の辺の重みの総和d[v]のリスト
    '''

    WHITE=0
    GRAY=1
    BLACK=2
    color=[WHITE]*n
    d=[INFTY]*n

    HQ=[]

    d[s]=0
    heappush(HQ,(d[s],s))

    while(len(HQ)>0):
        du,u=heappop(HQ)
        color[u]=BLACK

        if u == g:
            return du

        if d[u]<du:
            continue

        for v,t,k in nList[u]:
            if color[v]!=BLACK:
                vw = waittime(du,k)+t
                if d[u] + vw < d[v]:
                    d[v] = d[u] + vw
                    color[v]=GRAY
                    heappush(HQ, (d[v], v))
    return -1


def main(n,m,x,y,nList):
    ans = dijkstra(x,y,n,nList)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,x,y,nList=readinput()
    ans=main(n,m,x,y,nList)
    printans(ans)
