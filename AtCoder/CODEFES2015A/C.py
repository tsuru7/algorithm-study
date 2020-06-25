def readinput():
    n,t=list(map(int,input().split()))
    aList=[]
    bList=[]
    for _ in range(n):
        a,b=list(map(int,input().split()))
        aList.append(a)
        bList.append(a-b)
    return n,t,aList,bList

def main(n,t,aList,bList):
    suma=0
    for a in aList:
        suma+=a
    res=suma-t
    bs=sorted(bList,reverse=True)
    i=0
    while(res>0 and i<n):
        res-=bs[i]
        i+=1
    if res>0 and i==n:
        return -1
    elif res<=0:
        return i

if __name__=='__main__':
    n,t,aList,bList=readinput()
    ans=main(n,t,aList,bList)
    print(ans)
