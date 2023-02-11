import sys
INFTY=sys.maxsize
sys.setrecursionlimit(100000)

def readinput():
    n=int(input())
    nList=[]
    for _ in range(n+1):
        nList.append([])
    for _ in range(1,n):
        u,v,w=map(int,input().split())
        nList[u].append((v,w))
        nList[v].append((u,w))

    return n,nList

WHITE=0
GRAY=1
BLACK=2
status=[]
color=[]

def dfs(s,nList):
    for u,w in nList[s]:
        if status[u]==WHITE:
            if w%2==0:
                color[u]=color[s]
            else:
                color[u]=(color[s]+1)%2
            status[u]=GRAY
            dfs(u,nList)
    status[s]=BLACK

def main(n,nList):
    global status
    global color

    status=[WHITE]*(n+1)
    color=[WHITE]*(n+1)
    dfs(1,nList)

    for i in range(1,n+1):
        print(color[i])
    

if __name__=='__main__':
    n,nList=readinput()
    main(n,nList)
    #print(ans)
