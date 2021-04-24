def readinput():
    n=int(input())
    nList=[]
    for _ in range(n+1):
        nList.append([])
    for _ in range(n):
        l=list(map(int,input().split()))
        u=l[0]
        k=l[1]
        v=l[2:]
        nList[u]=v
    
    return n,nList

d=[]
f=[]
color=[]
WHITE=0
GRAY=1
BLACK=2
_time=0

def dfs(s,nList):
    global d
    global f
    global color
    global _time

    #print('dfs: {}'.format(s))
    if(color[s]==WHITE):
        _time+=1
        color[s]=GRAY
        d[s]=_time
        for t in nList[s]:
            dfs(t,nList)
        _time+=1
        f[s]=_time
        color[s]=BLACK
    

def main(n,nList):
    global color
    global d
    global f
    global _time

    color=[WHITE]*(n+1)
    d=[0]*(n+1)
    f=[0]*(n+1)
    for i in range(1,n+1):
        dfs(i,nList)
    for i in range(1,n+1):
        print('{} {} {}'.format(i,d[i],f[i]))



if __name__=='__main__':
    n,nList=readinput()
    #print(nList)
    main(n,nList)
