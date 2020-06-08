from collections import deque
import sys

INFTY=sys.maxsize
WHITE=0
GRAY=1
BLACK=2

color=[]
d=[]
Q=deque([])
n=0
L=[]

def readinput():
    global n
    global L

    n=int(input())
    for i in range(n+1):
        L.append([])

    for i in range(n):
        inp=list(map(int,input().split()))
        L[inp[0]]=inp[2:]


def bfs(s):
    global color
    global d
    global Q

    for i in range(n+1):
        color=[WHITE]*(n+1)
        d=[-1]*(n+1)

    color[s]=GRAY
    d[s]=0
    Q.append(s)

    while(len(Q)>0):
        u = Q.popleft()
        for l in L[u]:
            if(color[l]==WHITE):
                color[l]=GRAY
                d[l]=d[u]+1
                Q.append(l)
        color[u]=BLACK

if __name__=='__main__':
    readinput()
    bfs(1)
    for i in range(1,n+1):
        print('{} {}'.format(i, d[i]))
