WHITE=0
GRAY=1
BLACK=2

def readinput():
    global L
    global n

    n=int(input())
    for i in range(n+1):
        L.append([])

    for i in range(n):
        inp=list(map(int,input().split()))
        L[inp[0]]=inp[2:]
    return

n=0
L=[]
S=[]
time_=0
color=[]
d=[]
f=[]

def dfs_visit(u):
    global S
    global time_
    global color
    global d
    global f

    S.append(u)
    color[u] = GRAY
    time_+=1
    d[u]=time_

    while(len(S)>0):
        uu=S[-1]
        uuList=L[uu]
        if (len(uuList)!=0):
            v=uuList.pop(0)
            if(color[v]==WHITE):
                color[v]=GRAY
                time_+=1
                d[v]=time_
                S.append(v)
        else:
            S.pop()
            color[uu]=BLACK
            time_+=1
            f[uu]=time_



def dfs_init():
    global color
    global d
    global f
    global n

    for i in range(n+1):
        color.append(WHITE)
    d=[0]*(n+1)
    f=[0]*(n+1)


if __name__=='__main__':
    readinput()
    #print(L)
    dfs_init()
    for u in range(1,n+1):
        if(color[u]==WHITE):
            dfs_visit(u)
    
    for u in range(1,n+1):
        print('{} {} {}'.format(u,d[u],f[u]))
