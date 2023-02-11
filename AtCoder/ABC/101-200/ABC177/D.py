from collections import deque 
def readinput():
    n,m=map(int,input().split())
    nList=[]
    for _ in range(n+1):
        nList.append([])
    for i in range(m):
        a,b=map(int,input().split())
        nList[a].append(b)
        nList[b].append(a)
    return n,nList

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
    print(d)
    return max(d)

def main(n,nList):
    ans=0
    for i in range(n):
        d=bfs(i,n,nList)
        ans=max(ans,d)
    return ans+1

if __name__=='__main__':
    n,nList=readinput()
    ans=main(n,nList)
    print(ans)
