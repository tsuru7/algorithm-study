from collections import deque 

def readinput():
    n,m=list(map(int,input().split()))
    nList=[]
    for _ in range(n+1):
        nList.append([])
    for _ in range(m):
        a,b=list(map(int,input().split()))
        nList[0].append(a)
        nList[a].append(b)
        nList[b].append(a)
    return n,m,nList


def bfs(s,n,nList):
    WHITE=0
    GRAY=1
    BLACK=2
    color=[WHITE]*(n+1)
    d=[0]*(n+1)
    Q = deque([])
    Q.append(s)
    while(len(Q)>0):
        u=Q.popleft()
        for t in nList[u]:
            if color[t]==WHITE:
                color[t]=GRAY
                d[t]=d[u]+1
                Q.append(t)
        color[u]=BLACK
    count=0
    for i in range(1,n+1):
        if d[i]==2:
            count+=1
    return count



def main(n,m,nList):
    for i in range(1,n+1):
        print(bfs(i, n, nList))

if __name__=='__main__':
    n,m,nList=readinput()
    main(n,m,nList)

        
        
