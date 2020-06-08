def readinput():
    n,m=list(map(int,input().split()))
    rooms = [
        [[],-1,-1] for _ in range(n)
        ]
    for _ in range(m):
        a,b = list(map(int,input().split()))
        rooms[a-1][0].append(b)
        rooms[b-1][0].append(a)
    return n,m,rooms

def labelNext(target, rooms, nokori, cost):
    oitaList=[]
    idx = list(nokori)
    for ii in idx:
        i = ii-1
        room=rooms[i]
        if (target in room[0]) and (room[1] == -1):
            room[1] = target
            room[2] = cost
            oitaList.append(i+1) # 道しるべをおいた部屋番号のリストにするので+1
    nokori -= set(oitaList)  #　道しるべを置いた部屋番号を削除
    return oitaList

def main(n,m,rooms):
    nokori=set(range(2,n+1))  # 道しるべを置いてない部屋番号の集合 (1を除くすべて)
    target=1
    cost=1
    nextList=labelNext(target,rooms, nokori, cost)
    while(len(nokori)>0):
        cost+=1
        nl=[]
        for n in nextList:
            nl.append(labelNext(n,rooms,nokori,cost))
            if(len(nokori)==0):
                break
        nextList=nl
    labelList=[]
    for room in rooms:
        labelList.append(room[1])   
    labelList.pop(0)     
    return labelList

if __name__=='__main__':
    n,m,rooms=readinput()
    labelList=main(n,m,rooms)
    print('Yes')
    for l in labelList:
        print(l)
    
