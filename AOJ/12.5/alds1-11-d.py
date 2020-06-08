from collections import deque

def bfs(s,t,nList,color,icol):

  
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

    return (color[s]==color[t])

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
    for _ in range(q):
        s,t=list(map(int,input().split()))
        if(color[s] == -1) and (color[t] == -1):
            icol+=1
            res=bfs(s,t,nList,color,icol)
            if(res==True):
                print('yes')
            else:
                print('no')
        elif (color[s]==-1) or (color[t]==-1):
            print('no')
        elif (color[s] == color[t]):
            print('yes')
        else:
            print('no')
    
if __name__=='__main__':
    main()


    

