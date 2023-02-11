import sys
sys.setrecursionlimit(1000000)

def readinput():
    n,q=map(int,input().split())
    nList=[]
    for _ in range(n+1):
        nList.append([])
    for i in range(n-1):
        a,b=map(int,input().split())
        nList[a].append(b)
        nList[b].append(a)
    px=[]
    for i in range(q):
        p,x=map(int,input().split())
        px.append((p,x))
    return n,q,nList,px

childList=[]
def setDepth(s,nList):
    global depth
    global color
    global childList

    for next in nList[s]:
        if color[next]==WHITE:
            childList[s].append(next)
            depth[next]=depth[s]+1
            color[next]=GRAY
            childList[s].extend(setDepth(next,nList))
    color[s]=BLACK
    return childList[s]

def addCounter(s,x,nList):
    global depth
    global counter

    for next in nList[s]:
        if depth[next]>depth[s]:
            counter[next]+=x
            addCounter(next,x,nList)
    

WHITE=0
GRAY=1
BLACK=2
color=[]
depth=[]
counter=[]
def main(n,q,nList,px):
    global depth
    global color
    global counter
    global childList

    color=[WHITE]*(n+1)
    depth=[0]*(n+1)
    counter=[0]*(n+1)
    for _ in range(n+1):
        childList.append([])

    #print(nList)

    depth[1]=0
    color[1]=GRAY
    setDepth(1,nList)
    #print(depth)
    #print(childList)

    for p,x in px:
        # counter[p]+=x
        # addCounter(p,x,nList)
        counter[p]+=x
        for c in childList[p]:
            counter[c]+=x

    return counter[1:]

if __name__=='__main__':
    n,q,nList,px=readinput()
    ans=main(n,q,nList,px)
    print(' '.join(map(str,ans)))
