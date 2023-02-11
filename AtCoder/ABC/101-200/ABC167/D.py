def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    tbl={}
    for i in range(1,n+1):
        tbl[i]=a[i-1]
    machi=1
    for i in range(k):
        machi=tbl[machi]
    return machi

def main2(n,k,a):
    a.insert(0,0)
    #print(a)
    nvisited=[0 for i in range(n+1)]
    #print(nvisited)
    visited=[]
    current=1
    visited.append(current)
    nvisited[current]+=1
    next=a[current]
    #print('next='+str(next))
    while(nvisited[next]==0):
        current=next
        visited.append(current)
        nvisited[current]+=1
        next=a[current]
    loophead=next
    #print('loophead:'+str(loophead))
    #print('visited'+str(visited))
    beforeloop=visited.index(loophead)
    #print('beforeloop:'+str(beforeloop))
    loop=visited[beforeloop:]
    #print('loop:'+str(loop))
    looplen=len(loop)

    if (k<beforeloop):
        return visited[k+1]
    else:
        return loop[(k-beforeloop)%looplen]

def detectloop(a):
        # loopを検出して
        # loopに入る前に訪れた町リスト:head
        # loop内で訪れる町リスト:loop
        # を返す
    nvisit=[0 for i in range(len(a))]
    visited=[]
    n=a[0]
    while(nvisit[n-1]==0):
        nvisit[n-1]+=1
        visited.append(n)
        n=a[n-1]
    #print(visited,n)
    i=visited.index(n)
    #print(i)
    if(i==0):
        loop=visited[:]
        head=[]
    else:
        loop=visited[i:]
        head=visited[:i]
    return head,loop

def main3(n,k,a):
    head,loop=detectloop(a)
    #print(head,loop,k)
    if(k<=len(head)):
        return head[k-1]
    else:
        return loop[(k-len(head))%len(loop) -1]





if __name__=='__main__':
    n,k,a=readinput()
    ans=main3(n,k,a)
    print(ans)
