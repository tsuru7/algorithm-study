from collections import deque

WHITE=0
GRAY=1
BLACK=2

nList = []
labelList = []
color = []
Q = deque([])

def readinput():
    global nList
    global color
    global Q
    global labelList

    n,m=list(map(int,input().split()))
    nList = []
    for _ in range(n+1):
        nList.append([])  # 1-オリジンの隣接リスト

    for _ in range(m):
        a,b = list(map(int,input().split()))
        nList[a].append(b)
        nList[b].append(a)

    labelList = [0]*(n+1)
    color = [WHITE]*(n+1)
    Q = deque([])

    #print(nList)

def bfs(p):
    global Q
    global nList
    global color
    global labelList

    Q.append(p)
    color[p]=GRAY
    #print(Q)
    #print(color)
    while(len(Q)>0):
        current=Q.popleft()
        for next in nList[current]:
            if(color[next]==WHITE):
                Q.append(next)
                color[next]=GRAY
                labelList[next]=current
                #print(Q)
                #print(color)
                #print(labelList)
        color[current]=BLACK

def main():

    bfs(1)


if __name__=='__main__':
    readinput()

    main()
    print('Yes')
    for l in labelList[2:]:
        print(l)
    
