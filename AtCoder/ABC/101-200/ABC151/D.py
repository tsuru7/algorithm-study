from heapq import heappush, heappop
import sys
INFTY=sys.maxsize

def readinput():
    h,w=map(int,input().split())
    sMat=[]
    for _ in range(h):
        sMat.append(list(input()))
    nList=[]
    for _ in range(h*w):
        nList.append(set())
    for i in range(h):
        for j in range(w):
            if sMat[i][j]=='#':
                continue
            ij=i+j*h
            if i-1>=0 and sMat[i-1][j]=='.':
                nList[ij].add(ij-1)
            if i+1<h and sMat[i+1][j]=='.':
                nList[ij].add(ij+1)
            if j-1>=0 and sMat[i][j-1]=='.':
                nList[ij].add(ij-h)
            if j+1<w and sMat[i][j+1]=='.':
                nList[ij].add(ij+h)
    for i in range(h*w):
        nList[i]=list(nList[i])
    return h,w,nList

def dijkstra(s,n,nList):
    '''優先度付きキューを使用したダイクストラ法

    パラメーター
    s: 始点
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
    for i in range(h*w):
        if len(nList[i])==0:
            d[i]=0

    HQ=[]

    d[s]=0
    heappush(HQ,(d[s],s))

    while(len(HQ)>0):
        du,u=heappop(HQ)
        color[u]=BLACK

        if d[u]<du:
            continue

        for v in nList[u]:
            vw=1
            if color[v]!=BLACK:
                if d[u] + vw < d[v]:
                    d[v] = d[u] + vw
                    color[v]=GRAY
                    heappush(HQ, (d[v], v))
    return d

def main(h,w,nList):
    #print(nList)
    ans=0
    for i in range(h*w):
        if len(nList[i])>0:
            d=dijkstra(i,h*w,nList)
            #print(d)
            dmax=max(d)
            ans=max(ans,dmax)
    return ans

if __name__=='__main__':
    h,w,nList=readinput()
    ans=main(h,w,nList)
    print(ans)
