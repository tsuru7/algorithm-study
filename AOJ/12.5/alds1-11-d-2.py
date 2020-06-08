from collections import deque

def bfs(s,nList,color,icol):

  
    UNVISITED=0
    ENTERED=1
    VISITED=2
    state=[UNVISITED]*len(nList)
    Q=deque([])

    Q.append(s)
    state[s]=ENTERED
    color[s]=icol
    while(len(Q)>0):
        current=Q.popleft()
        for next in nList[current]:
            if state[next]==UNVISITED:
                Q.append(next)
                state[next]=ENTERED
                color[next]=icol
        state[current]=VISITED

    return

def main():
    n,m=list(map(int,input().split()))
    nList=[]
    for _ in range(n):
        nList.append([])

    for _ in range(m):
        s,t=list(map(int,input().split()))
        nList[s].append(t)
        nList[t].append(s)

    q=int(input())

    icol=-1
    color=[icol]*n
    for i in range(n):
        if (color[i]==-1):
            icol+=1
            bfs(i,nList,color,icol)
        

    for _ in range(q):
        s,t=list(map(int,input().split()))
        if (color[s] == color[t]):
            print('yes')
        else:
            print('no')
    
if __name__=='__main__':
    main()


    

